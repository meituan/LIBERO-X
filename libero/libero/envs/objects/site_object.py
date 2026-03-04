import os
import numpy as np

from robosuite.utils.mjcf_utils import string_to_array
import robosuite.utils.transform_utils as transform_utils

import pathlib

absolute_path = pathlib.Path(__file__).parent.parent.parent.absolute()


class SiteObject:
    def __init__(
        self,
        name,
        parent_name=None,
        joints=None,
        size=None,
        rgba=None,
        site_type="box",
        site_pos="0 0 0",
        site_quat="1 0 0 0",
        object_properties={},
    ):
        self.name = name
        self.parent_name = parent_name
        self.joints = joints
        self.site_pos = string_to_array(site_pos)
        self.site_quat = string_to_array(site_quat)
        self.size = size if type(size) is not str else string_to_array(size)
        self.rgba = rgba
        self.site_type = site_type
        self.object_properties = object_properties

    def in_box(self, this_position, this_mat, other_position):
        """
        Checks whether the point `other_position` lies inside this site-aligned box.

        We transform the world-space delta into the site's local frame (using R^T),
        then compare against the site's half-sizes. This is robust to site rotations
        (e.g., front/left/right regions with different quaternions).

        Args:
            this_position: world-space 3D position of this SiteObject center
            this_mat: 3x3 rotation from site local frame to world (MuJoCo xmat)
            other_position: world-space 3D position to test
        """
        this_position = np.asarray(this_position, dtype=float)
        other_position = np.asarray(other_position, dtype=float)
        size_local = np.asarray(self.size, dtype=float)

        # 改动：对矩阵逐元素取绝对值，再与半尺寸相乘
        # total_size = np.abs(this_mat @ self.size)
        # 对应 half_extent_world = |R| @ half_extent_local
        total_half = (np.abs(this_mat) @ size_local)

        lb = this_position - total_half
        ub = this_position + total_half

        # 统一各轴容差
        eps = 0.02
        inside_lower = (other_position >= lb - eps)
        inside_upper = (other_position <= ub + eps)
        

        return bool(np.all(inside_lower & inside_upper))
        # # Rotation local->world; need world->local for transforming deltas
        # R = this_mat
        # R_T = R.T

        # # Local delta in site frame
        # delta_local = R_T @ (other_position - this_position)
        # half_sizes = np.array(self.size, dtype=float)

        # # Small tolerance only towards world-down direction
        # lb_local = -half_sizes.copy()
        # ub_local = half_sizes.copy()
        # margin_z = 0.1
        # # Determine which local axis aligns most with world up, then extend
        # # the bound on the opposite (world-down) side along that axis.
        # up_local = R_T @ np.array([0.0, 0.0, 1.0])
        # axis = int(np.argmax(np.abs(up_local)))  # 0:x, 1:y, 2:z in local frame
        # sign = 1.0 if up_local[axis] >= 0 else -1.0
        # if sign > 0:
        #     # world up aligns with +local axis => bottom is local negative side
        #     lb_local[axis] -= margin_z
        # else:
        #     # world up aligns with -local axis => bottom is local positive side
        #     ub_local[axis] += margin_z

        # return np.all(delta_local > lb_local) and np.all(delta_local < ub_local)

    def __str__(self):
        return (
            f"Object {self.name} : \n geom type: {self.site_type} \n size: {self.size}"
        )

    def under(self, this_position, this_mat, other_position, other_height=0.10):
        """
        Checks whether an object is on this SiteObject.
        Useful for when the CompositeObject has holes and the object should
        be within one of the holes. Makes an approximation by treating the
        object as a point, and the SiteObject as an axis-aligned grid.
        Args:
            this_position: 3D position of this SiteObject
            other_position: 3D position of object to test for insertion
        """
        total_size = self.size  # np.abs(this_mat @ self.size)

        delta_position = this_mat @ (other_position - this_position)
        # print(total_size, " | ", delta_position)
        # print(total_size[2] < delta_position[2] < total_size[2] + other_height, np.all(np.abs(delta_position[:2]) < total_size[:2]))
        return total_size[2] - 0.005 < delta_position[2] < total_size[
            2
        ] + other_height and np.all(np.abs(delta_position[:2]) < total_size[:2])
