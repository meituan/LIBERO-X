import robosuite.utils.transform_utils as transform_utils
import os
import numpy as np


class BaseObjectState:
    def __init__(self):
        pass

    def get_geom_state(self):
        raise NotImplementedError

    def check_contact(self, other):
        raise NotImplementedError

    def check_contain(self, other):
        raise NotImplementedError

    def get_joint_state(self):
        raise NotImplementedError

    def is_open(self):
        raise NotImplementedError

    def is_close(self):
        raise NotImplementedError

    def get_size(self):
        raise NotImplementedError

    def check_ontop(self, other):
        raise NotImplementedError


class ObjectState(BaseObjectState):
    def __init__(self, env, object_name, is_fixture=False):
        self.env = env
        self.object_name = object_name
        self.is_fixture = is_fixture
        self.query_dict = (
            self.env.fixtures_dict if self.is_fixture else self.env.objects_dict
        )
        self.object_state_type = "object"
        self.has_turnon_affordance = hasattr(
            self.env.get_object(self.object_name), "turn_on"
        )

    def get_geom_state(self):
        object_pos = self.env.sim.data.body_xpos[self.env.obj_body_id[self.object_name]]
        object_quat = self.env.sim.data.body_xquat[
            self.env.obj_body_id[self.object_name]
        ]
        return {"pos": object_pos, "quat": object_quat}

    def check_contact(self, other):
        object_1 = self.env.get_object(self.object_name)
        object_2 = self.env.get_object(other.object_name)
        return self.env.check_contact(object_1, object_2)

    def check_contain(self, other):
        object_1 = self.env.get_object(self.object_name)
        object_1_position = self.env.sim.data.body_xpos[
            self.env.obj_body_id[self.object_name]
        ]
        object_2 = self.env.get_object(other.object_name)
        object_2_position = self.env.sim.data.body_xpos[
            self.env.obj_body_id[other.object_name]
        ]
        return object_1.in_box(object_1_position, object_2_position)

    def get_joint_state(self):
        # Return None if joint state does not exist
        joint_states = []
        for joint in self.env.get_object(self.object_name).joints:
            qpos_addr = self.env.sim.model.get_joint_qpos_addr(joint)
            joint_states.append(self.env.sim.data.qpos[qpos_addr])
        return joint_states

    def check_ontop(self, other):
        this_object = self.env.get_object(self.object_name)
        this_object_position = self.env.sim.data.body_xpos[
            self.env.obj_body_id[self.object_name]
        ]
        other_object = self.env.get_object(other.object_name)
        # Default: use object's root body position
        other_object_position = self.env.sim.data.body_xpos[
            self.env.obj_body_id[other.object_name]
        ]
        # If both top_site and bottom_site exist, use their中点作为近似“几何中心”
        try:
            bottom_site_name = f"{other.object_name}_bottom_site"
            top_site_name = f"{other.object_name}_top_site"
            bottom_world = self.env.sim.data.get_site_xpos(bottom_site_name)
            top_world = self.env.sim.data.get_site_xpos(top_site_name)
            if bottom_world is not None and top_world is not None:
                other_object_position = 0.5 * (bottom_world + top_world)
        except Exception:
            pass
        return (
            (this_object_position[2] <= other_object_position[2])
            and self.check_contact(other)
            and (
                np.linalg.norm(this_object_position[:2] - other_object_position[:2])
                < 0.03
            )
        )

    def set_joint(self, qpos=1.5):
        for joint in self.env.get_object(self.object_name).joints:
            self.env.sim.data.set_joint_qpos(joint, qpos)

    def is_open(self):
        for joint in self.env.get_object(self.object_name).joints:
            qpos_addr = self.env.sim.model.get_joint_qpos_addr(joint)
            qpos = self.env.sim.data.qpos[qpos_addr]
            if self.env.get_object(self.object_name).is_open(qpos):
                return True
        return False

    def is_close(self):
        for joint in self.env.get_object(self.object_name).joints:
            qpos_addr = self.env.sim.model.get_joint_qpos_addr(joint)
            qpos = self.env.sim.data.qpos[qpos_addr]
            if not (self.env.get_object(self.object_name).is_close(qpos)):
                return False
        return True

    def turn_on(self):
        for joint in self.env.get_object(self.object_name).joints:
            qpos_addr = self.env.sim.model.get_joint_qpos_addr(joint)
            qpos = self.env.sim.data.qpos[qpos_addr]
            if self.env.get_object(self.object_name).turn_on(qpos):
                return True
        return False

    def turn_off(self):
        for joint in self.env.get_object(self.object_name).joints:
            qpos_addr = self.env.sim.model.get_joint_qpos_addr(joint)
            qpos = self.env.sim.data.qpos[qpos_addr]
            if not (self.env.get_object(self.object_name).turn_off(qpos)):
                return False
        return True

    def update_state(self):
        if self.has_turnon_affordance:
            self.turn_on()


class SiteObjectState(BaseObjectState):
    """
    This is to make site based objects to have the same API as normal Object State.
    """

    def __init__(self, env, object_name, parent_name, is_fixture=False):
        self.env = env
        self.object_name = object_name
        self.parent_name = parent_name
        self.is_fixture = self.parent_name in self.env.fixtures_dict
        self.query_dict = (
            self.env.fixtures_dict if self.is_fixture else self.env.objects_dict
        )
        self.object_state_type = "site"

    def get_geom_state(self):
        object_pos = self.env.sim.data.get_site_xpos(self.object_name)
        object_quat = transform_utils.mat2quat(
            self.env.sim.data.get_site_xmat(self.object_name)
        )
        return {"pos": object_pos, "quat": object_quat}

    def check_contain(self, other):
        this_object = self.env.object_sites_dict[self.object_name]
        this_object_position = self.env.sim.data.get_site_xpos(self.object_name)
        this_object_mat = self.env.sim.data.get_site_xmat(self.object_name)

        other_object = self.env.get_object(other.object_name)
        # 1) Start with object's root body position
        other_object_position = self.env.sim.data.body_xpos[
            self.env.obj_body_id[other.object_name]
        ].copy()

        # 2) Try using midpoint of bottom/top sites (if both exist) as a better center
        bottom_world = None
        top_world = None
        center_source = "body"
        try:
            bottom_site_name = f"{other.object_name}_bottom_site"
            top_site_name = f"{other.object_name}_top_site"
            bottom_world = self.env.sim.data.get_site_xpos(bottom_site_name)
            top_world = self.env.sim.data.get_site_xpos(top_site_name)
            if bottom_world is not None and top_world is not None:
                other_object_position = 0.5 * (bottom_world + top_world)
                center_source = "mid(bottom,top)"
        except Exception:
            pass

        # 3) If still body center (which may coincide with bottom),
        #    estimate center via the world's AABB from BOX geoms only (full XYZ)
        if center_source == "body":
            try:
                import numpy as _np
                obid = self.env.obj_body_id[other.object_name]
                x_min = y_min = z_min = _np.inf
                x_max = y_max = z_max = -_np.inf
                any_box = False
                geom_infos = []
                for gid in range(self.env.sim.model.ngeom):
                    if self.env.sim.model.geom_bodyid[gid] != obid:
                        continue
                    gtype = int(self.env.sim.model.geom_type[gid])
                    # MuJoCo mjtGeom: BOX == 6 (0:PLANE,1:HFIELD,2:SPHERE,3:CAPSULE,4:ELLIPSOID,5:CYLINDER,6:BOX,7:MESH)
                    if gtype != 6:
                        continue
                    any_box = True
                    pos_g = self.env.sim.data.geom_xpos[gid]
                    Rg = self.env.sim.data.geom_xmat[gid].reshape(3, 3)
                    sx, sy, sz = self.env.sim.model.geom_size[gid]
                    x_half = abs(Rg[0, 0]) * sx + abs(Rg[0, 1]) * sy + abs(Rg[0, 2]) * sz
                    y_half = abs(Rg[1, 0]) * sx + abs(Rg[1, 1]) * sy + abs(Rg[1, 2]) * sz
                    z_half = abs(Rg[2, 0]) * sx + abs(Rg[2, 1]) * sy + abs(Rg[2, 2]) * sz
                    x_min = min(x_min, pos_g[0] - x_half)
                    x_max = max(x_max, pos_g[0] + x_half)
                    y_min = min(y_min, pos_g[1] - y_half)
                    y_max = max(y_max, pos_g[1] + y_half)
                    z_min = min(z_min, pos_g[2] - z_half)
                    z_max = max(z_max, pos_g[2] + z_half)
                    # collect info for debug
                    try:
                        gname = self.env.sim.model.geom_id2name(gid)
                    except Exception:
                        gname = str(gid)
                    geom_infos.append((gname, gtype, pos_g.copy(), (sx, sy, sz), (x_half, y_half, z_half)))
                if any_box and all(_np.isfinite(v) for v in (x_min, x_max, y_min, y_max, z_min, z_max)):
                    other_object_position = _np.array([
                        0.5 * (x_min + x_max),
                        0.5 * (y_min + y_max),
                        0.5 * (z_min + z_max),
                    ], dtype=float)
                    center_source = "AABBxyz(box)"
            except Exception:
                pass

        # Optional debug: print oriented-box details for site contain check
        try:
            import numpy as _np
            R = this_object_mat
            R_T = R.T
            half = _np.asarray(this_object.size, dtype=float)
            delta_local = R_T @ (other_object_position - this_object_position)
            up_local = R_T @ _np.array([0.0, 0.0, 1.0])
            axis = int(_np.argmax(_np.abs(up_local)))
            sign = 1.0 if up_local[axis] >= 0 else -1.0
            margin = 0.01
            lb_local = -half.copy(); ub_local = half.copy()
            if sign > 0:
                lb_local[axis] -= margin
            else:
                ub_local[axis] += margin

            # Also compute world AABB for reference
            half_world = (_np.abs(R) @ half)
            lb_world = this_object_position - half_world
            ub_world = this_object_position + half_world

            def _fmt(a):
                return _np.array2string(_np.asarray(a), formatter={'float_kind': lambda x: f"{x:.2f}"})

            # Prepare more object details
            try:
                body_pos = self.env.sim.data.body_xpos[self.env.obj_body_id[other.object_name]].copy()
            except Exception:
                body_pos = other_object_position.copy()

            # If we collected geom box info above, include a brief summary
            try:
                type_names = {0:"PLANE",1:"HFIELD",2:"SPHERE",3:"CAPSULE",4:"ELLIPSOID",5:"CYLINDER",6:"BOX",7:"MESH"}
            except Exception:
                type_names = {}

            # print(
            #     f"[ContainDebug] site={self.object_name}, obj={other.object_name}\n"
            #     f"  site_pos={_fmt(this_object_position)}, obj_pos={_fmt(other_object_position)}\n"
            #     f"  obj_center_from={center_source}, body_pos={_fmt(body_pos)}\n"
            #     f"  bottom_site={_fmt(bottom_world) if bottom_world is not None else 'N/A'}, top_site={_fmt(top_world) if top_world is not None else 'N/A'}\n"
            #     f"  R_row0={_fmt(R[0])}, R_row1={_fmt(R[1])}, R_row2={_fmt(R[2])}\n"
            #     f"  half_local={_fmt(half)}, up_local={_fmt(up_local)}, axis={axis}, sign={sign:.2f}\n"
            #     f"  bounds_local=[{_fmt(lb_local)}, {_fmt(ub_local)}], delta_local={_fmt(delta_local)}\n"
            #     f"  aabb_world=[{_fmt(lb_world)}, {_fmt(ub_world)}]"
            # )

            # Detailed geom list for this object (BOX geoms and their half extents)
            try:
                if 'geom_infos' in locals() and geom_infos:
                    # print("  geom_boxes:")
                    for (gname, gtype, p, szs, halves) in geom_infos:
                        tname = type_names.get(gtype, str(gtype))
                        # print(f"    - name={gname}, type={tname}, pos={_fmt(p)}, size={_fmt(szs)}, half={_fmt(halves)}")
                else:
                    # Also print a compact summary of all geoms attached to this body
                    obid = self.env.obj_body_id[other.object_name]
                    # print("  geoms(all for body):")
                    for gid in range(self.env.sim.model.ngeom):
                        if self.env.sim.model.geom_bodyid[gid] != obid:
                            continue
                        gtype = int(self.env.sim.model.geom_type[gid])
                        try:
                            gname = self.env.sim.model.geom_id2name(gid)
                        except Exception:
                            gname = str(gid)
                        # print(f"    - name={gname}, type={type_names.get(gtype, str(gtype))}")
            except Exception:
                pass
        except Exception:
            pass
        return this_object.in_box(
            this_object_position, this_object_mat, other_object_position
        )

    def check_contact(self, other):
        """
        There is no dynamics for site objects, so we return true all the time.
        """
        return True

    def check_ontop(self, other):
        this_object = self.env.object_sites_dict[self.object_name]
        if hasattr(this_object, "under"):
            this_object_position = self.env.sim.data.get_site_xpos(self.object_name)
            this_object_mat = self.env.sim.data.get_site_xmat(self.object_name)
            other_object = self.env.get_object(other.object_name)
            other_object_position = self.env.sim.data.body_xpos[
                self.env.obj_body_id[other.object_name]
            ]
            # print(self.object_name, this_object_position)
            # print(other_object_position)

            parent_object = self.env.get_object(self.parent_name)
            if parent_object is None:
                return this_object.under(
                    this_object_position, this_object_mat, other_object_position
                )
            else:
                return this_object.under(
                    this_object_position, this_object_mat, other_object_position
                ) and self.env.check_contact(parent_object, other_object)
        else:
            return True

    def set_joint(self, qpos=1.5):
        for joint in self.env.object_sites_dict[self.object_name].joints:
            self.env.sim.data.set_joint_qpos(joint, qpos)

    def is_open(self):
        for joint in self.env.object_sites_dict[self.object_name].joints:
            qpos_addr = self.env.sim.model.get_joint_qpos_addr(joint)
            qpos = self.env.sim.data.qpos[qpos_addr]
            if self.env.get_object(self.parent_name).is_open(qpos):
                return True
        return False

    def is_close(self):
        for joint in self.env.object_sites_dict[self.object_name].joints:
            qpos_addr = self.env.sim.model.get_joint_qpos_addr(joint)
            qpos = self.env.sim.data.qpos[qpos_addr]
            if not (self.env.get_object(self.parent_name).is_close(qpos)):
                return False
        return True
