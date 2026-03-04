from typing import List
import numpy as np


class Expression:
    def __init__(self):
        raise NotImplementedError

    def __call__(self):
        raise NotImplementedError


class UnaryAtomic(Expression):
    def __init__(self):
        pass

    def __call__(self, arg1):
        raise NotImplementedError


class BinaryAtomic(Expression):
    def __init__(self):
        pass

    def __call__(self, arg1, arg2):
        raise NotImplementedError


class MultiarayAtomic(Expression):
    def __init__(self):
        pass

    def __call__(self, *args):
        raise NotImplementedError


class TruePredicateFn(MultiarayAtomic):
    def __init__(self):
        super().__init__()

    def __call__(self, *args):
        return True


class FalsePredicateFn(MultiarayAtomic):
    def __init__(self):
        super().__init__()

    def __call__(self, *args):
        return False


class InContactPredicateFn(BinaryAtomic):
    def __call__(self, arg1, arg2):
        return arg1.check_contact(arg2)


class In(BinaryAtomic):
    def __call__(self, arg1, arg2):
        return arg2.check_contact(arg1) and arg2.check_contain(arg1)


class ExactIn(BinaryAtomic):
    """Stricter "in": inside region AND bottom is at expected vertical height.

    For site regions, compute vertical delta along world up-axis and compare to
    the site's vertical half-size projected onto world up. For non-site, fallback
    to check_ontop.
    """

    def __call__(self, arg1, arg2):
        # first: must be inside
        try:
            contain_ok = arg2.check_contain(arg1)
        except Exception:
            contain_ok = False

        bottom_ok = False
        reg_type = getattr(arg2, 'object_state_type', '?')
        if reg_type == 'site':
            try:
                env = arg2.env
                site_name = arg2.object_name
                site_obj = env.object_sites_dict[site_name]
                site_pos = env.sim.data.get_site_xpos(site_name)
                site_mat = env.sim.data.get_site_xmat(site_name)
                obj_pos = env.sim.data.body_xpos[env.obj_body_id[arg1.object_name]]

                z_world = np.array([0.0, 0.0, 1.0])

                table_top_z = float(env.workspace_offset[2])

                bottom_site_name = f"{arg1.object_name}_bottom_site"
                obj_bottom_world = None
                try:
                    obj_bottom_world = env.sim.data.get_site_xpos(bottom_site_name)
                except Exception:

                    obj_bottom_world = obj_pos

                delta_z_world = float(obj_bottom_world[2] - table_top_z)

                z_eps = 0.04
                bottom_ok = abs(delta_z_world) <= z_eps
            except Exception as e:
                print(f"[ExactInZ WARNING] geometric calc failed: {e}")
                try:
                    bottom_ok = arg2.check_ontop(arg1)
                except Exception:
                    bottom_ok = False
            else:
                # only runs if above try success
                # print(
                #     f"[ExactInZ] obj={arg1.object_name}, reg={site_name}, "
                #     f"contain={contain_ok}, delta_z_world={delta_z_world:.4f}, "
                #     f"table_top_z={table_top_z:.4f}, eps={z_eps:.4f}, bottom_ok={bottom_ok}"
                # )
                pass
        else:
            # non-site: fallback
            try:
                bottom_ok = arg2.check_ontop(arg1)
            except Exception:
                bottom_ok = False

        result = contain_ok and bottom_ok
        try:
            reg_name = getattr(arg2, "object_name", "<unknown_region>")
            obj_name = getattr(arg1, "object_name", "<unknown_obj>")
            # print(
            #     f"[DEBUG ExactIn] obj={obj_name}, region={reg_name}, "
            #     f"contain_ok={contain_ok}, bottom_ok={bottom_ok}, result={result}"
            # )
        except Exception:
            pass

        return result
   


class On(BinaryAtomic):
    def __call__(self, arg1, arg2):
        return arg2.check_ontop(arg1)

        # if arg2.object_state_type == "site":
        #     return arg2.check_ontop(arg1)
        # else:
        #     obj_1_pos = arg1.get_geom_state()["pos"]
        #     obj_2_pos = arg2.get_geom_state()["pos"]
        #     # arg1.on_top_of(arg2) ?
        #     # TODO (Yfeng): Add checking of center of mass are in the same regions
        #     if obj_1_pos[2] >= obj_2_pos[2] and arg2.check_contact(arg1):
        #         return True
        #     else:
        #         return False


class Up(BinaryAtomic):
    def __call__(self, arg1):
        return arg1.get_geom_state()["pos"][2] >= 1.0


class Stack(BinaryAtomic):
    def __call__(self, arg1, arg2):
        return (
            arg1.check_contact(arg2)
            and arg2.check_contain(arg1)
            and arg1.get_geom_state()["pos"][2] > arg2.get_geom_state()["pos"][2]
        )


class PrintJointState(UnaryAtomic):
    """This is a debug predicate to allow you print the joint values of the object you care"""

    def __call__(self, arg):
        print(arg.get_joint_state())
        return True


class Open(UnaryAtomic):
    def __call__(self, arg):
        return arg.is_open()


class Close(UnaryAtomic):
    def __call__(self, arg):
        return arg.is_close()


class TurnOn(UnaryAtomic):
    def __call__(self, arg):
        return arg.turn_on()


class TurnOff(UnaryAtomic):
    def __call__(self, arg):
        return arg.turn_off()


# -----------------------------
# Orientation-aware ON variants
# -----------------------------

def _object_up_vector(env, obj_name):
    """Estimate object's upward vector in world frame.

    Priority:
    1) If both bottom_site and top_site exist for the object, use the vector top-bottom
    2) Otherwise, use body orientation's z-axis (assuming local z is 'up')
    """
    try:
        b = env.sim.data.get_site_xpos(f"{obj_name}_bottom_site")
        t = env.sim.data.get_site_xpos(f"{obj_name}_top_site")
        v = t - b
        n = np.linalg.norm(v)
        if n > 1e-6:
            return v / n
    except Exception:
        pass

    # fallback: body xmat's local z-axis
    try:
        bid = env.obj_body_id[obj_name]
        R = env.sim.data.body_xmat[bid].reshape(3, 3)
        v = R[:, 2]
        n = np.linalg.norm(v)
        if n > 1e-6:
            return v / n
    except Exception:
        pass
    return np.array([0.0, 0.0, 1.0])


def _surface_normal(env, arg2_state):
    """Approximate surface normal (world) of arg2.

    - If arg2 is a site, use its rotation to find the axis most aligned with world-up,
      ensuring it points upwards (positive dot with world-up).
    - Otherwise fallback to world-up.
    """
    z_world = np.array([0.0, 0.0, 1.0])
    if getattr(arg2_state, 'object_state_type', None) == 'site':
        try:
            env = arg2_state.env
            site_name = arg2_state.object_name
            R = env.sim.data.get_site_xmat(site_name)
            # choose axis most aligned with world up
            dots = [abs(np.dot(R[:, i], z_world)) for i in range(3)]
            axis = int(np.argmax(dots))
            n = R[:, axis]
            if np.dot(n, z_world) < 0:
                n = -n
            return n / (np.linalg.norm(n) + 1e-9)
        except Exception:
            pass
    return z_world


class UprightOn(BinaryAtomic):
    """Object rests on the support with its bottom face (upright).

    Conditions:
    - arg1 is on arg2 (contact + vertical placement)
    - object's up-vector is aligned with surface normal (dot >= cos_thresh)
    """

    def __call__(self, arg1, arg2):
        try:
            if not arg2.check_ontop(arg1):
                return False
            env = arg2.env
            obj_up = _object_up_vector(env, arg1.object_name)
            n_surf = _surface_normal(env, arg2)
            cos = float(np.clip(np.dot(obj_up, n_surf), -1.0, 1.0))
            cos_thresh = 0.8  # ~36.9deg tolerance
            return cos >= cos_thresh
        except Exception:
            return False


class SideOn(BinaryAtomic):
    """Object rests on the support with a side face (lying on side).

    Conditions:
    - arg1 is on arg2 (contact + vertical placement)
    - object's up-vector is near perpendicular to surface normal (|dot| <= sin_thresh)
    """

    def __call__(self, arg1, arg2):
        try:
            if not arg2.check_ontop(arg1):
                return False
            env = arg2.env
            obj_up = _object_up_vector(env, arg1.object_name)
            n_surf = _surface_normal(env, arg2)
            d = abs(float(np.clip(np.dot(obj_up, n_surf), -1.0, 1.0)))
            # If dot is small, up is horizontal w.r.t surface normal => side face resting
            sin_thresh = 0.3  # ~17.5deg from 90°
            return d <= sin_thresh
        except Exception:
            return False
