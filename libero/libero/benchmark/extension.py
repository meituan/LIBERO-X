import numpy as np
from typing import Dict

from libero.libero.utils.bddl_generation_utils import (
    get_xy_region_kwargs_list_from_regions_info,
)
from libero.libero.utils.mu_utils import InitialSceneTemplates, register_mu
from libero.libero.envs.objects import get_object_dict
from .multi_level_testset_builder import make_expanded_region_scene


@register_mu(scene_type="study")
class ExtensionStudyL3Scene1(InitialSceneTemplates):
    """
    Simple L3-style scene with two books and a desk caddy on the study table.

    Intended for tasks like: \"organize the desk so that both books are stored inside the desk caddy\".
    """

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy": 1,
            "black_book": 1,
            "yellow_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024

        # Desk caddy near top-left of the table.
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.16, 0.24],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        # Two books placed apart on the tabletop.
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, -0.12],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, -0.20],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )

        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
        ]



@register_mu(scene_type="study")
class ExtensionStudyScene1(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "study_table": 1,
        }

        object_num_info = {
            "black_book": 1,
            "yellow_book": 1,
            "white_yellow_mug": 1,
            "red_coffee_mug": 1,
            "desk_caddy": 1,
        }

        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.25],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.2],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, -0.15],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(-np.pi, np.pi),
                
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, -0.05],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.2],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
        ]
        return states

@register_mu(scene_type="study")
class ExtensionStudyScene2(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "study_table": 1,
        }

        object_num_info = {
            "black_book": 1,
            "yellow_book": 1,
            "white_yellow_mug": 1,
            "red_coffee_mug": 1,
            "desk_caddy": 1,
        }

        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.25],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.2],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, -0.15],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(-np.pi, np.pi),
                
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, -0.05],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.2],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            
        ]
        return states


@register_mu(scene_type="study")
class ExtensionStudyScene3(InitialSceneTemplates):
    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "black_book": 2,
            "yellow_book": 1,
            "white_yellow_mug": 1,
            "red_coffee_mug": 1,
            "desk_caddy": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book  = 0.026
        half_mug   = 0.014

        # caddy 左上（与前两个略有差别，防止完全重复）
        self.regions.update(self.get_region_dict(
            region_centroid_xy=[-0.16, 0.25],
            region_name="desk_caddy_init_region",
            target_name=self.workspace_name,
            region_half_len=half_caddy,
        ))

        # 黑书 A/B（右侧错位）
        self.regions.update(self.get_region_dict(
            region_centroid_xy=[0.14, 0.10],
            region_name="black_book_A_init_region",
            target_name=self.workspace_name,
            region_half_len=half_book,
        ))
        self.regions.update(self.get_region_dict(
            region_centroid_xy=[0.02, -0.20],
            region_name="black_book_B_init_region",
            target_name=self.workspace_name,
            region_half_len=half_book,
        ))

        # 黄书（更靠左下）
        self.regions.update(self.get_region_dict(
            region_centroid_xy=[-0.12, -0.22],
            region_name="yellow_book_init_region",
            target_name=self.workspace_name,
            region_half_len=half_book,
        ))

        # 杯子靠中线，一上一下
        self.regions.update(self.get_region_dict(
            region_centroid_xy=[-0.05, -0.06],
            region_name="white_yellow_mug_init_region",
            target_name=self.workspace_name,
            region_half_len=half_mug,
            yaw_rotation=(-np.pi, np.pi),
        ))
        

        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "black_book_1", "study_table_black_book_A_init_region"),
            ("On", "black_book_2", "study_table_black_book_B_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene4(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "study_table": 1,
        }

        object_num_info = {
            "black_book": 1,
            "yellow_book": 1,
            "green_book": 1,
            "red_coffee_mug": 1,
            "desk_caddy": 1,
        }

        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.25],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, -0.15],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(-np.pi, np.pi),
                
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, -0.05],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.2],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.2],
                region_name="green_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "green_book_1", "study_table_green_book_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
        ]
        return states


@register_mu(scene_type="study")
class ExtensionStudyScene5(InitialSceneTemplates):
    """Desk caddy + mug + three new colored books laid out without overlap."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy": 1,
            "red_coffee_mug": 1,
            "red_book": 1,
            "orange_book": 1,
            "striped_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, 0.24],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.12, -0.08],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.06, -0.19],
                region_name="red_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.02, -0.25],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.19, 0.05],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene6(InitialSceneTemplates):
    """Mix of classic and new books with staggered placements."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy": 1,
            "red_coffee_mug": 1,
            "yellow_book": 1,
            "red_book": 1,
            "striped_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.22],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.16],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, -0.14],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.18],
                region_name="red_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.12, 0.02],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene7(InitialSceneTemplates):
    """Four colorful books plus a mug, spaced around the tabletop perimeter."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "black_book": 1,
            "yellow_book": 1,
            "white_yellow_mug": 1,
            "desk_caddy": 1,
            "orange_book": 1,
            "striped_book": 1,
            "green_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_mug = 0.014
        half_book = 0.024
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.22],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=0.02,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.0],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.16, 0.05],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, -0.2],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.16, -0.12],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, -0.21],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.16],
                region_name="green_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
            ("On", "green_book_1", "study_table_green_book_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene8(InitialSceneTemplates):
    """Desk caddy fixed left-top, duplicate red books plus mixed colors."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy": 1,
            
            "red_book": 2,
            "orange_book": 1,
            "striped_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, 0.25],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.16, -0.23],
                region_name="red_book_A_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.2, -0.04],
                region_name="red_book_B_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, -0.19],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.12, -0.16],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
       
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "red_book_1", "study_table_red_book_A_init_region"),
            ("On", "red_book_2", "study_table_red_book_B_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene9(InitialSceneTemplates):
    """Two yellow books plus green/red variants, all reachable near the caddy."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy": 1,
            "white_yellow_mug": 1,
            "yellow_book": 2,
            "green_book": 1,
            "red_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.014

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, 0.25],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.17, -0.12],
                region_name="yellow_book_A_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.02, -0.2],
                region_name="yellow_book_B_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, 0.18],
                region_name="green_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.14, -0.05],
                region_name="red_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.02, -0.06],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_A_init_region"),
            ("On", "yellow_book_2", "study_table_yellow_book_B_init_region"),
            ("On", "green_book_1", "study_table_green_book_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene10(InitialSceneTemplates):
    """Two striped books plus classics; mug kept away from books, caddy fixed."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy": 1,
            "red_coffee_mug": 1,
            "striped_book": 2,
            "black_book": 1,
            "orange_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, 0.25],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.03, -0.08],
                region_name="striped_book_A_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.17, 0.13],
                region_name="striped_book_B_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, -0.2],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.14, -0.16],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.22, -0.3],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_A_init_region"),
            ("On", "striped_book_2", "study_table_striped_book_B_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
        ]
    
@register_mu(scene_type="study")
class ExtensionStudyScene11(InitialSceneTemplates):
    """Mirrored version of Scene 1 (desk caddy on right)."""
    def __init__(self):

        fixture_num_info = {
            "study_table": 1,
        }

        object_num_info = {
            "black_book": 1,
            "yellow_book": 1,
            "white_yellow_mug": 1,
            "red_coffee_mug": 1,
            "desk_caddy_right": 1,
        }

        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.25],
                region_name="desk_caddy_right_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.2],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.15],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(-np.pi, np.pi),
                
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, 0.05],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.2],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "desk_caddy_right_1", "study_table_desk_caddy_right_init_region"),
        ]
        return states



@register_mu(scene_type="study")
class ExtensionStudyScene12(InitialSceneTemplates):
    """Mirrored version of Scene 2 (desk caddy on right)."""
    def __init__(self):

        fixture_num_info = {
            "study_table": 1,
        }

        object_num_info = {
            "black_book": 1,
            "yellow_book": 1,
            "white_yellow_mug": 1,
            "red_coffee_mug": 1,
            "desk_caddy_right": 1,
        }

        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.25],
                region_name="desk_caddy_right_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.2],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.15],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(-np.pi, np.pi),
                
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, 0.05],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.2],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "desk_caddy_right_1", "study_table_desk_caddy_right_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            
        ]
        return states




@register_mu(scene_type="study")
class ExtensionStudyScene13(InitialSceneTemplates):
    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "black_book": 2,
            "yellow_book": 1,
            "white_yellow_mug": 1,
            "red_coffee_mug": 1,
            "desk_caddy_right": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book  = 0.026
        half_mug   = 0.014

        self.regions.update(self.get_region_dict(
            region_centroid_xy=[-0.16, -0.25],
            region_name="desk_caddy_right_init_region",
            target_name=self.workspace_name,
            region_half_len=half_caddy,
        ))

        self.regions.update(self.get_region_dict(
            region_centroid_xy=[0.14, -0.1],
            region_name="black_book_A_init_region",
            target_name=self.workspace_name,
            region_half_len=half_book,
        ))
        self.regions.update(self.get_region_dict(
            region_centroid_xy=[0.02, 0.2],
            region_name="black_book_B_init_region",
            target_name=self.workspace_name,
            region_half_len=half_book,
        ))

        self.regions.update(self.get_region_dict(
            region_centroid_xy=[-0.12, 0.22],
            region_name="yellow_book_init_region",
            target_name=self.workspace_name,
            region_half_len=half_book,
        ))

        self.regions.update(self.get_region_dict(
            region_centroid_xy=[-0.05, 0.06],
            region_name="white_yellow_mug_init_region",
            target_name=self.workspace_name,
            region_half_len=half_mug,
            yaw_rotation=(-np.pi, np.pi),
        ))
        

        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_right_1", "study_table_desk_caddy_right_init_region"),
            ("On", "black_book_1", "study_table_black_book_A_init_region"),
            ("On", "black_book_2", "study_table_black_book_B_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            
        ]




@register_mu(scene_type="study")
class ExtensionStudyScene14(InitialSceneTemplates):
    """Mirrored version of Scene 4 (desk caddy on right)."""
    def __init__(self):

        fixture_num_info = {
            "study_table": 1,
        }

        object_num_info = {
            "black_book": 1,
            "yellow_book": 1,
            "green_book": 1,
            "red_coffee_mug": 1,
            "desk_caddy_right": 1,
        }

        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.25],
                region_name="desk_caddy_right_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.15],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(-np.pi, np.pi),
                
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, 0.05],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.2],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.2],
                region_name="green_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "green_book_1", "study_table_green_book_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "desk_caddy_right_1", "study_table_desk_caddy_right_init_region"),
        ]
        return states




@register_mu(scene_type="study")
class ExtensionStudyScene15(InitialSceneTemplates):
    """Desk caddy + mug + three new colored books laid out without overlap."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy_right": 1,
            "red_coffee_mug": 1,
            "red_book": 1,
            "orange_book": 1,
            "striped_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, -0.24],
                region_name="desk_caddy_right_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.12, 0.08],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.06, 0.19],
                region_name="red_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.02, 0.25],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.19, -0.05],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_right_1", "study_table_desk_caddy_right_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]




@register_mu(scene_type="study")
class ExtensionStudyScene16(InitialSceneTemplates):
    """Mix of classic and new books with staggered placements."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy_right": 1,
            "red_coffee_mug": 1,
            "yellow_book": 1,
            "red_book": 1,
            "striped_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.22],
                region_name="desk_caddy_right_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, -0.16],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, 0.14],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.18],
                region_name="red_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.12, -0.02],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_right_1", "study_table_desk_caddy_right_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]




@register_mu(scene_type="study")
class ExtensionStudyScene17(InitialSceneTemplates):
    """Four colorful books plus a mug, spaced around the tabletop perimeter."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "black_book": 1,
            "yellow_book": 1,
            "white_yellow_mug": 1,
            "desk_caddy_right": 1,
            "orange_book": 1,
            "striped_book": 1,
            "green_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_mug = 0.014
        half_book = 0.024
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.22],
                region_name="desk_caddy_right_init_region",
                target_name=self.workspace_name,
                region_half_len=0.02,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, 0],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.16, -0.05],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, 0.2],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.16, 0.12],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, 0.21],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.16],
                region_name="green_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            ("On", "desk_caddy_right_1", "study_table_desk_caddy_right_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
            ("On", "green_book_1", "study_table_green_book_init_region"),
        ]




@register_mu(scene_type="study")
class ExtensionStudyScene18(InitialSceneTemplates):
    """Desk caddy fixed left-top, duplicate red books plus mixed colors."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy_right": 1,
            
            "red_book": 2,
            "orange_book": 1,
            "striped_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, -0.25],
                region_name="desk_caddy_right_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.16, 0.23],
                region_name="red_book_A_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.2, 0.04],
                region_name="red_book_B_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, 0.19],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.12, 0.16],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
       
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_right_1", "study_table_desk_caddy_right_init_region"),
            ("On", "red_book_1", "study_table_red_book_A_init_region"),
            ("On", "red_book_2", "study_table_red_book_B_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]




@register_mu(scene_type="study")
class ExtensionStudyScene19(InitialSceneTemplates):
    """Two yellow books plus green/red variants, all reachable near the caddy."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy_right": 1,
            "white_yellow_mug": 1,
            "yellow_book": 2,
            "green_book": 1,
            "red_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.014

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, -0.25],
                region_name="desk_caddy_right_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.17, 0.12],
                region_name="yellow_book_A_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.02, 0.2],
                region_name="yellow_book_B_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, -0.18],
                region_name="green_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.14, 0.05],
                region_name="red_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.02, 0.06],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_right_1", "study_table_desk_caddy_right_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_A_init_region"),
            ("On", "yellow_book_2", "study_table_yellow_book_B_init_region"),
            ("On", "green_book_1", "study_table_green_book_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
        ]




@register_mu(scene_type="study")
class ExtensionStudyScene20(InitialSceneTemplates):
    """Two striped books plus classics; mug kept away from books, caddy fixed."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy_right": 1,
            "red_coffee_mug": 1,
            "striped_book": 2,
            "black_book": 1,
            "orange_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, -0.25],
                region_name="desk_caddy_right_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.03, 0.08],
                region_name="striped_book_A_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.17, -0.13],
                region_name="striped_book_B_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, 0.2],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.14, 0.16],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.22, 0.3],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_right_1", "study_table_desk_caddy_right_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_A_init_region"),
            ("On", "striped_book_2", "study_table_striped_book_B_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene21(InitialSceneTemplates):
    """Back-row caddy variant of Scene1."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "black_book": 1,
            "yellow_book": 1,
            "white_yellow_mug": 1,
            "red_coffee_mug": 1,
            "desk_caddy_back": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.014

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.0],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.18],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, -0.16],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.05],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.2],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene22(InitialSceneTemplates):
    """Back-row caddy counterpart of Scene2."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "black_book": 1,
            "yellow_book": 1,
            "white_yellow_mug": 1,
            "red_coffee_mug": 1,
            "desk_caddy_back": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.014

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.0],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.06, 0.22],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, 0.05],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.04, -0.11],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, -0.21],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene23(InitialSceneTemplates):
    """Two black books with the caddy located at the back."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "black_book": 2,
            "yellow_book": 1,
            "white_yellow_mug": 1,
            "red_coffee_mug": 1,
            "desk_caddy_back": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.026
        half_mug = 0.014

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.0],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.16, 0.1],
                region_name="black_book_A_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.02, -0.22],
                region_name="black_book_B_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.14, -0.22],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, -0.06],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, -0.04],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "black_book_1", "study_table_black_book_A_init_region"),
            ("On", "black_book_2", "study_table_black_book_B_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene24(InitialSceneTemplates):
    """Back-row caddy with black/yellow/green books."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "black_book": 1,
            "yellow_book": 1,
            "green_book": 1,
            "red_coffee_mug": 1,
            "desk_caddy_back": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.0],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.02, -0.04],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.13, -0.22],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, 0.05],
                region_name="green_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.12, -0.12],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "green_book_1", "study_table_green_book_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene25(InitialSceneTemplates):
    """Back-row caddy with red/orange/striped books."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy_back": 1,
            "red_coffee_mug": 1,
            "red_book": 1,
            "orange_book": 1,
            "striped_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.0],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.1],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.02, -0.25],
                region_name="red_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, -0.14],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, -0.08],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene26(InitialSceneTemplates):
    """Back-row caddy version of Scene6 (yellow/red/striped mix)."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy_back": 1,
            "red_coffee_mug": 1,
            "yellow_book": 1,
            "red_book": 1,
            "striped_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.0],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.02, 0.2],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, -0.16],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.08, -0.22],
                region_name="red_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, -0.02],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene27(InitialSceneTemplates):
    """Back-row caddy with multiple colorful books (Scene7 variant)."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy_back": 1,
            "white_yellow_mug": 1,
            "black_book": 1,
            "yellow_book": 1,
            "orange_book": 1,
            "striped_book": 1,
            "green_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_mug = 0.014
        half_book = 0.024

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.0],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.02, 0.02],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.08, 0.18],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.12, -0.2],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, -0.22],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.04, -0.24],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, -0.02],
                region_name="green_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
            ("On", "green_book_1", "study_table_green_book_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene28(InitialSceneTemplates):
    """Two red books with the caddy at the back."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy_back": 1,
            "red_book": 2,
            "orange_book": 1,
            "striped_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.0],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, -0.25],
                region_name="red_book_A_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, -0.06],
                region_name="red_book_B_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.02],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.02, 0.18],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "red_book_1", "study_table_red_book_A_init_region"),
            ("On", "red_book_2", "study_table_red_book_B_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene29(InitialSceneTemplates):
    """Two yellow books plus green/red variants with the caddy at the back."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy_back": 1,
            "white_yellow_mug": 1,
            "yellow_book": 2,
            "green_book": 1,
            "red_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.014

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.0],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, -0.10],
                region_name="yellow_book_A_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.22],
                region_name="yellow_book_B_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.16, 0.18],
                region_name="green_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.12, 0.0],
                region_name="red_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.02, 0.16],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_A_init_region"),
            ("On", "yellow_book_2", "study_table_yellow_book_B_init_region"),
            ("On", "green_book_1", "study_table_green_book_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene30(InitialSceneTemplates):
    """Two striped books plus classics with the caddy at the back."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy_back": 1,
            "red_coffee_mug": 1,
            "striped_book": 2,
            "black_book": 1,
            "orange_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.0],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.04, 0.18],
                region_name="striped_book_A_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, -0.04],
                region_name="striped_book_B_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, -0.2],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.08, -0.2],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.05],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_A_init_region"),
            ("On", "striped_book_2", "study_table_striped_book_B_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
        ]


# ----------------------
# Dual-caddy study scenes
# ----------------------

@register_mu(scene_type="study")
class ExtensionStudyScene31(InitialSceneTemplates):
    """Dual caddies: left-top + back. Variant of Scene21."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "black_book": 1,
            "yellow_book": 1,
            "white_yellow_mug": 1,
            "red_coffee_mug": 1,
            "desk_caddy": 1,
            "desk_caddy_back": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.014

        # front-left caddy (like scenes 1-10)
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, 0.25],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        # back caddy (like scenes 21-30)
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.2],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.18],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, -0.16],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.05],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.2],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene32(InitialSceneTemplates):
    """Dual caddies: left + back. """

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "black_book": 1,
            "yellow_book": 1,
            "red_book": 1,
            "red_coffee_mug": 1,
            "desk_caddy": 1,
            "desk_caddy_back": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.014

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, 0.25],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.2],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, 0.05],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.04, -0.11],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, -0.21],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.2, -0.20],
                region_name="red_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene33(InitialSceneTemplates):
    """Dual caddies: left-top + back. Variant of Scene23 (two black books)."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "black_book": 2,
            "yellow_book": 1,
            "white_yellow_mug": 1,
            "red_coffee_mug": 1,
            "desk_caddy": 1,
            "desk_caddy_back": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.026
        half_mug = 0.014

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, 0.25],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.2],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.16, 0.1],
                region_name="black_book_A_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.08, -0.22],
                region_name="black_book_B_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.14, -0.22],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, -0.06],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, -0.04],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "black_book_1", "study_table_black_book_A_init_region"),
            ("On", "black_book_2", "study_table_black_book_B_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene34(InitialSceneTemplates):
    """Dual caddies: left-top + back. Variant of Scene24."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "black_book": 1,
            "yellow_book": 1,
            "green_book": 1,
            "red_coffee_mug": 1,
            "desk_caddy": 1,
            "desk_caddy_back": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, 0.25],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.2],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.02, -0.04],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.10, -0.22],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, 0.05],
                region_name="green_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.12, -0.12],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "green_book_1", "study_table_green_book_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene35(InitialSceneTemplates):
    """Dual caddies: left-top + back. Variant of Scene25."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy": 1,
            "desk_caddy_back": 1,
            "red_coffee_mug": 1,
            "red_book": 1,
            "orange_book": 1,
            "striped_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, 0.25],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.2],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.1],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.02, -0.25],
                region_name="red_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, -0.14],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, -0.08],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene36(InitialSceneTemplates):
    """Dual caddies: left-top + back. Variant of Scene26 (yellow/red/striped)."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy": 1,
            "desk_caddy_back": 1,
            "red_coffee_mug": 1,
            "yellow_book": 1,
            "red_book": 1,
            "striped_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, 0.25],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.2],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.02, 0.0],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, -0.16],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.08, -0.22],
                region_name="red_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, -0.02],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene37(InitialSceneTemplates):
    """Dual caddies: left-top + back. Variant of Scene27 (multi-color + mug)."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy": 1,
            "desk_caddy_back": 1,
            "white_yellow_mug": 1,
            "black_book": 1,
            "yellow_book": 1,
            "orange_book": 1,
            "striped_book": 1,
            "green_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_mug = 0.014
        half_book = 0.024

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, 0.25],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.2],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.02, 0.02],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.08, -0.08],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.12, -0.2],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, -0.22],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.04, -0.24],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, -0.02],
                region_name="green_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
            ("On", "green_book_1", "study_table_green_book_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene38(InitialSceneTemplates):
    """Dual caddies: left-top + back. Variant of Scene28 (two red books)."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy": 1,
            "desk_caddy_back": 1,
            "red_book": 2,
            "orange_book": 1,
            "striped_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, 0.25],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.2],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, -0.25],
                region_name="red_book_A_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, -0.06],
                region_name="red_book_B_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.02],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.22, 0.18],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "red_book_1", "study_table_red_book_A_init_region"),
            ("On", "red_book_2", "study_table_red_book_B_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene39(InitialSceneTemplates):
    """Dual caddies: left-top + back. Variant of Scene29 (two yellow + green/red + mug)."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy": 1,
            "desk_caddy_back": 1,
            "white_yellow_mug": 1,
            "yellow_book": 2,
            "green_book": 1,
            "red_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.014

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, 0.25],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.2],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, -0.10],
                region_name="yellow_book_A_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.22],
                region_name="yellow_book_B_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.16, 0.18],
                region_name="green_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.12, 0.0],
                region_name="red_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.16, -0.16],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_A_init_region"),
            ("On", "yellow_book_2", "study_table_yellow_book_B_init_region"),
            ("On", "green_book_1", "study_table_green_book_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene40(InitialSceneTemplates):
    """Dual caddies: left-top + back. Variant of Scene30 (two striped books)."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "desk_caddy": 1,
            "desk_caddy_back": 1,
            "striped_book": 2,
            "black_book": 1,
            "orange_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, 0.25],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.2],
                region_name="desk_caddy_back_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.17, 0.18],
                region_name="striped_book_A_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, -0.04],
                region_name="striped_book_B_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, -0.2],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.08, -0.2],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
       
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_A_init_region"),
            ("On", "striped_book_2", "study_table_striped_book_B_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
        ]
    
        
@register_mu(scene_type="study")
class ExtensionStudyScene41(InitialSceneTemplates):
    """Scene 11 variant using a wooden_two_layer_shelf instead of desk_caddy_right."""
    def __init__(self):

        fixture_num_info = {
            "study_table": 1,
        }

        object_num_info = {
            "black_book": 1,
            "yellow_book": 1,
            "white_yellow_mug": 1,
            "red_coffee_mug": 1,
            "wooden_two_layer_shelf": 1,
        }

        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.2],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.15],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, 0.05],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.2],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "wooden_two_layer_shelf_1", "study_table_wooden_two_layer_shelf_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene42(InitialSceneTemplates):
    """Scene 12 variant using a wooden_two_layer_shelf instead of desk_caddy_right."""
    def __init__(self):

        fixture_num_info = {
            "study_table": 1,
        }

        object_num_info = {
            "black_book": 1,
            "yellow_book": 1,
            "white_yellow_mug": 1,
            "red_coffee_mug": 1,
            "wooden_two_layer_shelf": 1,
        }

        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.2],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.15],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, 0.05],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.2],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "wooden_two_layer_shelf_1", "study_table_wooden_two_layer_shelf_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene43(InitialSceneTemplates):
    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "black_book": 2,
            "yellow_book": 1,
            "white_yellow_mug": 1,
            "wooden_two_layer_shelf": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book  = 0.026
        half_mug   = 0.014

        self.regions.update(self.get_region_dict(
            region_centroid_xy=[-0.16, -0.25],
            region_name="wooden_two_layer_shelf_init_region",
            target_name=self.workspace_name,
            region_half_len=half_caddy,
        ))

        self.regions.update(self.get_region_dict(
            region_centroid_xy=[0.14, -0.1],
            region_name="black_book_A_init_region",
            target_name=self.workspace_name,
            region_half_len=half_book,
        ))
        self.regions.update(self.get_region_dict(
            region_centroid_xy=[0.02, 0.2],
            region_name="black_book_B_init_region",
            target_name=self.workspace_name,
            region_half_len=half_book,
        ))

        self.regions.update(self.get_region_dict(
            region_centroid_xy=[-0.12, 0.22],
            region_name="yellow_book_init_region",
            target_name=self.workspace_name,
            region_half_len=half_book,
        ))

        self.regions.update(self.get_region_dict(
            region_centroid_xy=[-0.05, 0.06],
            region_name="white_yellow_mug_init_region",
            target_name=self.workspace_name,
            region_half_len=half_mug,
            yaw_rotation=(-np.pi, np.pi),
        ))
        
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "wooden_two_layer_shelf_1", "study_table_wooden_two_layer_shelf_init_region"),
            ("On", "black_book_1", "study_table_black_book_A_init_region"),
            ("On", "black_book_2", "study_table_black_book_B_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene44(InitialSceneTemplates):
    """Scene 14 variant using a wooden_two_layer_shelf instead of desk_caddy_right."""
    def __init__(self):

        fixture_num_info = {
            "study_table": 1,
        }

        object_num_info = {
            "black_book": 1,
            "yellow_book": 1,
            "green_book": 1,
            "red_coffee_mug": 1,
            "wooden_two_layer_shelf": 1,
        }

        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.15],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, 0.05],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.2],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.2],
                region_name="green_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "green_book_1", "study_table_green_book_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "wooden_two_layer_shelf_1", "study_table_wooden_two_layer_shelf_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene45(InitialSceneTemplates):
    """Scene 15 variant using a wooden_two_layer_shelf instead of desk_caddy_right."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "wooden_two_layer_shelf": 1,
            "red_coffee_mug": 1,
            "red_book": 1,
            "orange_book": 1,
            "striped_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, -0.24],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.12, 0.08],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.06, 0.19],
                region_name="red_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.02, 0.25],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.19, -0.05],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "wooden_two_layer_shelf_1", "study_table_wooden_two_layer_shelf_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene46(InitialSceneTemplates):
    """Scene 16 variant using a wooden_two_layer_shelf instead of desk_caddy_right."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "wooden_two_layer_shelf": 1,
            "red_coffee_mug": 1,
            "yellow_book": 1,
            "red_book": 1,
            "striped_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.22],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, -0.16],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, 0.14],
                region_name="yellow_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, 0.06],
                region_name="red_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.12, 0.16],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "wooden_two_layer_shelf_1", "study_table_wooden_two_layer_shelf_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene47(InitialSceneTemplates):
    """Scene 17 variant using a wooden_two_layer_shelf instead of desk_caddy_right."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "wooden_two_layer_shelf": 1,
            "red_coffee_mug": 1,
            "red_book": 2,
            "orange_book": 1,
            "striped_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, -0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.16, 0.23],
                region_name="red_book_A_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.2, 0.04],
                region_name="red_book_B_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.01, 0.0],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, 0.19],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.12, 0.16],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "wooden_two_layer_shelf_1", "study_table_wooden_two_layer_shelf_init_region"),
            ("On", "red_book_1", "study_table_red_book_A_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "red_book_2", "study_table_red_book_B_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene48(InitialSceneTemplates):
    """Scene 18 variant using a wooden_two_layer_shelf instead of desk_caddy_right."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "wooden_two_layer_shelf": 1,
            "red_book": 2,
            "orange_book": 1,
            "striped_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, -0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.16, 0.23],
                region_name="red_book_A_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.2, 0.04],
                region_name="red_book_B_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, 0.19],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.12, 0.16],
                region_name="striped_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "wooden_two_layer_shelf_1", "study_table_wooden_two_layer_shelf_init_region"),
            ("On", "red_book_1", "study_table_red_book_A_init_region"),
            ("On", "red_book_2", "study_table_red_book_B_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene49(InitialSceneTemplates):
    """Scene 19 variant using a wooden_two_layer_shelf instead of desk_caddy_right."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "wooden_two_layer_shelf": 1,
            "white_yellow_mug": 1,
            "yellow_book": 2,
            "green_book": 1,
            "red_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.014

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, -0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.17, 0.12],
                region_name="yellow_book_A_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.02, 0.2],
                region_name="yellow_book_B_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.18, -0.18],
                region_name="green_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.14, 0.05],
                region_name="red_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.02, 0.06],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "wooden_two_layer_shelf_1", "study_table_wooden_two_layer_shelf_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_A_init_region"),
            ("On", "yellow_book_2", "study_table_yellow_book_B_init_region"),
            ("On", "green_book_1", "study_table_green_book_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
        ]


@register_mu(scene_type="study")
class ExtensionStudyScene50(InitialSceneTemplates):
    """Scene 20 variant using a wooden_two_layer_shelf instead of desk_caddy_right."""

    def __init__(self):
        fixture_num_info = {"study_table": 1}
        object_num_info = {
            "wooden_two_layer_shelf": 1,
            "red_coffee_mug": 1,
            "striped_book": 2,
            "black_book": 1,
            "orange_book": 1,
        }
        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        half_caddy = 0.012
        half_book = 0.024
        half_mug = 0.012

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.18, -0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=half_caddy,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.03, 0.08],
                region_name="striped_book_A_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.17, -0.13],
                region_name="striped_book_B_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, 0.2],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.14, 0.16],
                region_name="orange_book_init_region",
                target_name=self.workspace_name,
                region_half_len=half_book,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.22, 0.3],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=half_mug,
                yaw_rotation=(-np.pi, np.pi),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "wooden_two_layer_shelf_1", "study_table_wooden_two_layer_shelf_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_A_init_region"),
            ("On", "striped_book_2", "study_table_striped_book_B_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
        ]



@register_mu(scene_type="kitchen")
class LiberoExtensionKitchenScene1(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
        }

        object_num_info = {
            "orange_juice": 1,
            "cream_cheese": 1,
            "akita_green_bowl": 1,
            "akita_yellow_bowl": 1,
            "plate": 2,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.0],
                region_name="akita_green_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.125, 0.125],
                region_name="akita_yellow_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.25],
                region_name="plate_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.25],
                region_name="plate_2_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.15],
                region_name="orange_juice_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.02,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.15],
                region_name="cream_cheese_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.02,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        states = [
            ("On", "akita_green_bowl_1", "kitchen_table_akita_green_bowl_1_init_region"),
            ("On", "akita_yellow_bowl_1", "kitchen_table_akita_yellow_bowl_1_init_region"),
            ("On", "plate_1", "kitchen_table_plate_1_init_region"),
            ("On", "plate_2", "kitchen_table_plate_2_init_region"),
            ("On", "orange_juice_1", "kitchen_table_orange_juice_1_init_region"),
            ("On", "cream_cheese_1", "kitchen_table_cream_cheese_1_init_region"),
        ]
        return states


@register_mu(scene_type="living_room")
class LiberoExtensionLivingRoomScene1(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "living_room_table": 1,
        }

        object_num_info = {
            "orange_juice": 1,
            "cream_cheese": 1,
            "akita_green_bowl": 1,
            "akita_yellow_bowl": 1,
            "plate": 2,
        }

        super().__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.0],
                region_name="akita_green_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.125, 0.125],
                region_name="akita_yellow_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.25],
                region_name="plate_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.25],
                region_name="plate_2_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.15],
                region_name="orange_juice_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.02,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.15],
                region_name="cream_cheese_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.02,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        states = [
            ("On", "akita_green_bowl_1", "living_room_table_akita_green_bowl_1_init_region"),
            ("On", "akita_yellow_bowl_1", "living_room_table_akita_yellow_bowl_1_init_region"),
            ("On", "plate_1", "living_room_table_plate_1_init_region"),
            ("On", "plate_2", "living_room_table_plate_2_init_region"),
            ("On", "orange_juice_1", "living_room_table_orange_juice_1_init_region"),
            ("On", "cream_cheese_1", "living_room_table_cream_cheese_1_init_region"),
        ]
        return states


@register_mu(scene_type="study")
class LiberoExtensionStudySceneTwoBowl1(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "floor": 1,
            "wooden_cabinet": 1,
        }

        object_num_info = {
            "akita_small_red_bowl": 1,
            "akita_large_red_bowl": 1,
            "plate": 1,
        }

        super().__init__(
            workspace_name="floor",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.30],
                region_name="wooden_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi),
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.0],
                region_name="akita_small_red_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.125, 0.125],
                region_name="akita_large_red_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.25],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        states = [
            ("On", "akita_small_red_bowl_1", "floor_akita_small_red_bowl_1_init_region"),
            ("On", "akita_large_red_bowl_1", "floor_akita_large_red_bowl_1_init_region"),
            ("On", "plate_1", "floor_plate_init_region"),
            ("On", "wooden_cabinet_1", "floor_wooden_cabinet_init_region"),
        ]
        return states

from functools import partial

def create_scene_classes():
    # object_names = [obj for obj in get_object_dict().keys() if obj not in ['cherries', 'corn', 'mayo', 'chefmate_8_frypan', 'target_zone', 'flat_stove', 'basin_faucet']]
    object_names = [obj for obj in get_object_dict().keys() if obj in ['flat_stove']]
    classes = []

    for obj_name in object_names:
        
        class_name = f"LiberoExtension{''.join(word.capitalize() for word in obj_name.split('_'))}Display"

        # 使用 partial 来绑定 obj_name 到 super().__init__ 的参数
        def __init__(self, obj=obj_name):
            fixture_num_info = {"floor": 1}
            object_num_info = {obj: 1}
            super(self.__class__, self).__init__(
                workspace_name="floor",
                fixture_num_info=fixture_num_info,
                object_num_info=object_num_info,
            )

        def define_regions(self, obj=obj_name):
            region_name = f"{obj}_1_init_region"
            self.regions.update(
                self.get_region_dict(
                    region_centroid_xy=[0.0, 0.0],
                    region_name=region_name,
                    target_name=self.workspace_name,
                    region_half_len=0.025,
                )
            )
            self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

        @property
        def init_states(self, obj=obj_name):
            return [("On", f"{obj}_1", f"floor_{obj}_1_init_region")]

        # 创建基础类
        class_dict = {
            "__init__": __init__,
            "define_regions": define_regions,
            "init_states": init_states
        }

        base_class = type(class_name, (InitialSceneTemplates,), class_dict)
        base_class = register_mu(scene_type="study")(base_class)
        classes.append(base_class)

    return classes
create_scene_classes()


@register_mu(scene_type="kitchen")
class ExtensionKitchenScene1(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_cabinet": 1,
        }

        object_num_info = {
            "akita_yellow_bowl": 1,
            "akita_green_bowl": 1,
            "akita_red_bowl": 1,
            "plate": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.30],
                region_name="wooden_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi),
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.0],
                region_name="akita_yellow_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.2],
                region_name="akita_green_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, 0.25],
                region_name="akita_red_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.25, 0],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_yellow_bowl_1", "kitchen_table_akita_yellow_bowl_init_region"),
            ("On", "akita_green_bowl_1", "kitchen_table_akita_green_bowl_init_region"),
            ("On", "akita_red_bowl_1", "kitchen_table_akita_red_bowl_init_region"),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("On", "wooden_cabinet_1", "kitchen_table_wooden_cabinet_init_region"),
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene2(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_cabinet": 1,
        }

        object_num_info = {
            "akita_yellow_bowl": 1,
            "akita_green_bowl": 1,
            "akita_red_bowl": 1,
            "plate": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.20],
                region_name="wooden_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi),
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.0],
                region_name="akita_yellow_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.1],
                region_name="akita_red_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.2],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_yellow_bowl_1", "kitchen_table_akita_yellow_bowl_init_region"),
            ("On", "akita_green_bowl_1", "wooden_cabinet_1_top_side"),
            ("On", "akita_red_bowl_1", "kitchen_table_akita_red_bowl_init_region"),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("On", "wooden_cabinet_1", "kitchen_table_wooden_cabinet_init_region"),
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene3(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_cabinet": 1,
        }

        object_num_info = {
            "akita_yellow_bowl": 1,
            "akita_green_bowl": 1,
            "akita_red_bowl": 1,
            "plate": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.30],
                region_name="wooden_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi),
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.2],
                region_name="akita_yellow_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.2, -0.1],
                region_name="akita_green_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.2, 0.05],
                region_name="akita_red_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, -0.1],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_yellow_bowl_1", "kitchen_table_akita_yellow_bowl_init_region"),
            ("On", "akita_green_bowl_1", "kitchen_table_akita_green_bowl_init_region"),
            ("On", "akita_red_bowl_1", "kitchen_table_akita_red_bowl_init_region"),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("On", "wooden_cabinet_1", "kitchen_table_wooden_cabinet_init_region"),
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene4(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "white_cabinet": 1,
        }

        object_num_info = {
            "akita_yellow_bowl": 1,
            "akita_green_bowl": 1,
            "akita_red_bowl": 1,
            "plate": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.20],
                region_name="white_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.30],
                region_name="akita_yellow_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.1],
                region_name="akita_red_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_yellow_bowl_1", "kitchen_table_akita_yellow_bowl_init_region"),
            ("On", "akita_green_bowl_1", "white_cabinet_1_top_side"),
            ("On", "akita_red_bowl_1", "kitchen_table_akita_red_bowl_init_region"),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("On", "white_cabinet_1", "kitchen_table_white_cabinet_init_region"),
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene5(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "white_cabinet": 1,
        }

        object_num_info = {
            "akita_yellow_bowl": 1,
            "akita_green_bowl": 1,
            "akita_red_bowl": 1,
            "plate": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.20],
                region_name="white_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.30],
                region_name="akita_yellow_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.1],
                region_name="akita_red_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_yellow_bowl_1", "kitchen_table_akita_yellow_bowl_init_region"),
            ("On", "akita_green_bowl_1", "white_cabinet_1_top_side"),
            ("On", "akita_red_bowl_1", "kitchen_table_akita_red_bowl_init_region"),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("On", "white_cabinet_1", "kitchen_table_white_cabinet_init_region"),
            ("Open", "white_cabinet_1_bottom_region")
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene6(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "white_cabinet": 1,
        }

        object_num_info = {
            "akita_yellow_bowl": 1,
            "akita_green_bowl": 1,
            "akita_red_bowl": 1,
            "plate": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.20],
                region_name="white_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.30],
                region_name="akita_yellow_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.2],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_yellow_bowl_1", "kitchen_table_akita_yellow_bowl_init_region"),
            ("On", "akita_green_bowl_1", "white_cabinet_1_top_side"),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("On", "white_cabinet_1", "kitchen_table_white_cabinet_init_region"),
            ("Open", "white_cabinet_1_bottom_region"),
            ("In", "akita_red_bowl_1", "white_cabinet_1_bottom_region"),
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene7(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "white_cabinet": 1,
            "bowl_drainer": 1,
        }

        object_num_info = {
            "akita_yellow_bowl": 1,
            "akita_green_bowl": 1,
            "plate": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, 0.20],
                region_name="white_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, -0.10],
                region_name="bowl_drainer_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.30],
                region_name="akita_yellow_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.1],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_yellow_bowl_1", "kitchen_table_akita_yellow_bowl_init_region"),
            ("On", "akita_green_bowl_1", "white_cabinet_1_top_side"),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("On", "white_cabinet_1", "kitchen_table_white_cabinet_init_region"),
            ("On", "bowl_drainer_1", "kitchen_table_bowl_drainer_init_region"),
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene8(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "white_cabinet": 1,
            "bowl_drainer": 1,
        }

        object_num_info = {
            "akita_black_bowl": 2,
            "plate": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, 0.30],
                region_name="white_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, -0.05],
                region_name="bowl_drainer_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.30],
                region_name="akita_black_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.0],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_black_bowl_1", "kitchen_table_akita_black_bowl_init_region"),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("On", "akita_black_bowl_2", "plate_1"),
            ("On", "white_cabinet_1", "kitchen_table_white_cabinet_init_region"),
            ("On", "bowl_drainer_1", "kitchen_table_bowl_drainer_init_region"),
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene9(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "flat_stove": 1,
            "bowl_drainer": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "akita_green_bowl": 1,
            "plate": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.2],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, -0.15],
                region_name="bowl_drainer_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.0],
                region_name="akita_black_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.2],
                region_name="akita_green_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_black_bowl_1", "kitchen_table_akita_black_bowl_1_init_region"),
            ("On", "akita_green_bowl_1", "kitchen_table_akita_green_bowl_1_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "bowl_drainer_1", "kitchen_table_bowl_drainer_init_region"),
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene10(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "flat_stove": 1,
            "bowl_drainer": 1,
            'wine_rack': 1
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "akita_green_bowl": 1,
            "plate": 1,
            "wine_bottle": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.25, 0.25],
                region_name="wine_rack_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.0],
                region_name="wine_bottle_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.2],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, -0.15],
                region_name="bowl_drainer_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.1],
                region_name="akita_black_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.3],
                region_name="akita_green_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wine_bottle_1", "kitchen_table_wine_bottle_init_region"),
            ("On", "wine_rack_1", "kitchen_table_wine_rack_init_region"),
            ("On", "akita_black_bowl_1", "kitchen_table_akita_black_bowl_1_init_region"),
            ("On", "akita_green_bowl_1", "kitchen_table_akita_green_bowl_1_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "bowl_drainer_1", "kitchen_table_bowl_drainer_init_region"),
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene11(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "flat_stove": 1,
            "bowl_drainer": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "akita_green_bowl": 1,
            "plate": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, -0.2],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.15],
                region_name="bowl_drainer_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.0],
                region_name="akita_black_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.2],
                region_name="akita_green_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_black_bowl_1", "kitchen_table_akita_black_bowl_1_init_region"),
            ("On", "akita_green_bowl_1", "kitchen_table_akita_green_bowl_1_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "bowl_drainer_1", "kitchen_table_bowl_drainer_init_region"),
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene12(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
            "bowl_drainer": 1,
        }

        object_num_info = {
            "akita_yellow_bowl": 1,
            "akita_green_bowl": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.2],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.15],
                region_name="bowl_drainer_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.0],
                region_name="akita_yellow_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.2],
                region_name="akita_green_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_green_bowl_1", "kitchen_table_akita_green_bowl_1_init_region"),
            ("On", "akita_yellow_bowl_1", "kitchen_table_akita_yellow_bowl_1_init_region"),
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "bowl_drainer_1", "kitchen_table_bowl_drainer_init_region"),
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene13(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "chefmate_8_frypan": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.2],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.15],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.0],
                region_name="frypan_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "chefmate_8_frypan_1", "kitchen_table_frypan_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene14(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "chefmate_8_frypan": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.0],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.05],
                region_name="frypan_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "chefmate_8_frypan_1", "kitchen_table_frypan_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene15(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "chefmate_8_frypan": 1,
            "moka_pot": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.1],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.05],
                region_name="moka_pot_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "chefmate_8_frypan_1", "wooden_two_layer_shelf_1_top_side"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "moka_pot_1", "kitchen_table_moka_pot_init_region"), 
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene16(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "chefmate_8_frypan": 1,
            "moka_pot": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.1],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.05],
                region_name="moka_pot_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "chefmate_8_frypan_1", "wooden_two_layer_shelf_1_bottom_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "moka_pot_1", "kitchen_table_moka_pot_init_region"), 
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene17(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "chefmate_8_frypan": 1,
            "moka_pot": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.1],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.05],
                region_name="moka_pot_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "chefmate_8_frypan_1", "wooden_two_layer_shelf_1_bottom_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "moka_pot_1", "kitchen_table_moka_pot_init_region"), 
            ("Turnon", "flat_stove_1")
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene18(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "chefmate_8_frypan": 1,
            "moka_pot": 1,
            "plate": 1,
            "akita_black_bowl": 1
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.2],
                region_name="akita_black_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.1],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.05],
                region_name="moka_pot_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "chefmate_8_frypan_1", "wooden_two_layer_shelf_1_bottom_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "moka_pot_1", "kitchen_table_moka_pot_init_region"), 
            ("On", "akita_black_bowl_1", "kitchen_table_akita_black_bowl_init_region"),
            ("On", "plate_1", "wooden_two_layer_shelf_1_top_region"),
            ("Turnon", "flat_stove_1")
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene19(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "chefmate_8_frypan": 1,
            "moka_pot": 1,
            "plate": 1,
            "akita_black_bowl": 1
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.05],
                region_name="akita_black_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.1],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.15],
                region_name="moka_pot_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "chefmate_8_frypan_1", "flat_stove_1_cook_region"),
            ("On", "moka_pot_1", "kitchen_table_moka_pot_init_region"), 
            ("On", "akita_black_bowl_1", "kitchen_table_akita_black_bowl_init_region"),
            ("On", "plate_1", "wooden_two_layer_shelf_1_top_region"),
            ("Turnon", "flat_stove_1")
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene20(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "chefmate_8_frypan": 1,
            "moka_pot": 1,
            "plate": 1,
            "akita_black_bowl": 1
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.05],
                region_name="akita_black_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.1],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.15],
                region_name="moka_pot_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.35],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "chefmate_8_frypan_1", "flat_stove_1_cook_region"),
            ("On", "moka_pot_1", "kitchen_table_moka_pot_init_region"), 
            ("On", "akita_black_bowl_1", "kitchen_table_akita_black_bowl_init_region"),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("Turnon", "flat_stove_1")
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene21(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "chefmate_8_frypan": 1,
            "basket": 1,
            "plate": 1,
            "akita_red_bowl": 1,
            "akita_green_bowl": 1
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.35],
                region_name="akita_red_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.1],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.15],
                region_name="basket_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.05],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "chefmate_8_frypan_1", "flat_stove_1_cook_region"),
            ("On", "basket_1", "kitchen_table_basket_init_region"),
            ("On", "akita_red_bowl_1", "kitchen_table_akita_red_bowl_init_region"),
            ("On", "akita_green_bowl_1", "wooden_two_layer_shelf_1_top_region"),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("Turnon", "flat_stove_1")
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene22(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "chefmate_8_frypan": 1,
            "basket": 1,
            "plate": 1,
            "akita_black_bowl": 1,
            "akita_green_bowl": 1
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.05],
                region_name="akita_black_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.1],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.15],
                region_name="basket_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.35],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "chefmate_8_frypan_1", "flat_stove_1_cook_region"),
            ("On", "basket_1", "kitchen_table_basket_init_region"), 
            ("On", "akita_black_bowl_1", "kitchen_table_akita_black_bowl_init_region"),
            ("On", "akita_green_bowl_1", "wooden_two_layer_shelf_1_top_region"),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("Turnon", "flat_stove_1")
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene23(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
        }

        object_num_info = {
            "wooden_tray": 1,
            "plate": 1,
            "akita_black_bowl": 1,
            "akita_green_bowl": 1,
            "akita_blue_bowl": 1
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.05],
                region_name="akita_black_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, 0.05],
                region_name="akita_blue_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.15],
                region_name="wooden_tray_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
                yaw_rotation=(np.pi/2, np.pi/2)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.35],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "wooden_tray_1", "kitchen_table_wooden_tray_init_region"), 
            ("On", "akita_black_bowl_1", "kitchen_table_akita_black_bowl_init_region"),
            ("On", "akita_green_bowl_1", "wooden_two_layer_shelf_1_top_region"),
            ("On", "akita_blue_bowl_1", "kitchen_table_akita_blue_bowl_init_region"),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("Turnon", "flat_stove_1")
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene24(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
        }

        object_num_info = {
            "wooden_tray": 1,
            "plate": 2,
            "akita_black_bowl": 1,
            "akita_green_bowl": 1,
            "akita_blue_bowl": 1
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.05],
                region_name="akita_green_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.15],
                region_name="wooden_tray_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
                yaw_rotation=(np.pi/2, np.pi/2)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.35],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, 0.05],
                region_name="plate_2_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "wooden_tray_1", "kitchen_table_wooden_tray_init_region"), 
            ("On", "akita_green_bowl_1", "kitchen_table_akita_green_bowl_init_region"),
            ("On", "akita_black_bowl_1", "wooden_two_layer_shelf_1_top_region"),
            ("On", "akita_blue_bowl_1", "wooden_tray_1_contain_region"),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("On", "plate_2", "kitchen_table_plate_2_init_region"),
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene25(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_shelf": 1
        }

        object_num_info = {
            "wooden_tray": 1,
            "plate": 2,
            "akita_green_bowl": 1,
            "akita_blue_bowl": 1,
            "white_bowl": 1
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.05],
                region_name="akita_green_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.15],
                region_name="wooden_tray_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
                yaw_rotation=(np.pi/2, np.pi/2)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.35],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, 0.05],
                region_name="plate_2_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, 0.25],
                region_name="wooden_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wooden_tray_1", "kitchen_table_wooden_tray_init_region"), 
            ("On", "akita_green_bowl_1", "kitchen_table_akita_green_bowl_init_region"),
            ("On", "akita_blue_bowl_1", "wooden_tray_1_contain_region"),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("On", "plate_2", "kitchen_table_plate_2_init_region"),
            ("On", "wooden_shelf_1", "kitchen_table_wooden_shelf_init_region"),
            ("On", "white_bowl_1", "wooden_shelf_1_top_side")
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene26(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "microwave": 1
        }

        object_num_info = {
            "plate": 1,
            "akita_green_bowl": 1,
            "white_bowl": 1
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.2],
                region_name="akita_green_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.3],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, -0.25],
                region_name="microwave_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_green_bowl_1", "kitchen_table_akita_green_bowl_init_region"),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("On", "microwave_1", "kitchen_table_microwave_init_region"),
            ("Open", "microwave_1"),
            ("On", "white_bowl_1", "microwave_1_top_side")
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene27(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "short_cabinet": 1
        }

        object_num_info = {
            "plate": 2,
            "akita_green_bowl": 1,
            "akita_blue_bowl": 1,
            "white_bowl": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.2],
                region_name="akita_green_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, 0],
                region_name="akita_blue_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.3],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.1],
                region_name="plate_2_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, -0.15],
                region_name="short_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_green_bowl_1", "kitchen_table_akita_green_bowl_init_region"),
            ("On", "akita_blue_bowl_1", "kitchen_table_akita_blue_bowl_init_region"),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("On", "short_cabinet_1", "kitchen_table_short_cabinet_init_region"),
            ("On", "white_bowl_1", "short_cabinet_1_top_region"),
            ("On", "plate_2", "kitchen_table_plate_2_init_region"),
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene28(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "short_cabinet": 1
        }

        object_num_info = {
            "plate": 2,
            "akita_green_bowl": 1,
            "akita_blue_bowl": 1,
            "white_bowl": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.22],
                region_name="akita_green_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, 0.05],
                region_name="akita_blue_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, 0.3],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.05],
                region_name="white_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, -0.15],
                region_name="short_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi/2, np.pi/2)
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_green_bowl_1", "kitchen_table_akita_green_bowl_init_region"),
            ("On", "akita_blue_bowl_1", "kitchen_table_akita_blue_bowl_init_region"),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("On", "short_cabinet_1", "kitchen_table_short_cabinet_init_region"),
            ("On", "white_bowl_1", "kitchen_table_white_bowl_init_region"),
            ("On", "plate_2", "short_cabinet_1_top_region"),
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene29(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
            "bowl_drainer": 1,
        }

        object_num_info = {
            "akita_yellow_bowl": 1,
            "akita_green_bowl": 1,
            "akita_black_bowl": 1
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.2],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.15],
                region_name="bowl_drainer_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.0],
                region_name="akita_yellow_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.2],
                region_name="akita_green_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_green_bowl_1", "kitchen_table_akita_green_bowl_1_init_region"),
            ("On", "akita_yellow_bowl_1", "kitchen_table_akita_yellow_bowl_1_init_region"),
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "bowl_drainer_1", "kitchen_table_bowl_drainer_init_region"),
            ("On", "akita_black_bowl_1", "wooden_two_layer_shelf_1_top_region"),
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene30(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "chefmate_8_frypan": 1,
            "glazed_rim_porcelain_ramekin": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.0],
                region_name="glazed_rim_porcelain_ramekin_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.2],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.15],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.0],
                region_name="frypan_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "chefmate_8_frypan_1", "kitchen_table_frypan_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "glazed_rim_porcelain_ramekin_1", "kitchen_table_glazed_rim_porcelain_ramekin_init_region"),
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene31(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "flat_stove": 1,
            "bowl_drainer": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "small_akita_black_bowl": 1,
            "large_akita_black_bowl": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.2],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, -0.15],
                region_name="bowl_drainer_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.0],
                region_name="akita_black_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.2],
                region_name="small_akita_black_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.2],
                region_name="large_akita_black_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_black_bowl_1", "kitchen_table_akita_black_bowl_1_init_region"),
            ("On", "small_akita_black_bowl_1", "kitchen_table_small_akita_black_bowl_1_init_region"),
            ("On", "large_akita_black_bowl_1", "kitchen_table_large_akita_black_bowl_1_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "bowl_drainer_1", "kitchen_table_bowl_drainer_init_region"),
        ]
        return states
    

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene32(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "flat_stove": 1,
            "bowl_drainer": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "small_akita_black_bowl": 1,
            "large_akita_black_bowl": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.2],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.15],
                region_name="bowl_drainer_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.2],
                region_name="akita_black_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.0],
                region_name="small_akita_black_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.2],
                region_name="large_akita_black_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_black_bowl_1", "kitchen_table_akita_black_bowl_1_init_region"),
            ("On", "small_akita_black_bowl_1", "kitchen_table_small_akita_black_bowl_1_init_region"),
            ("On", "large_akita_black_bowl_1", "kitchen_table_large_akita_black_bowl_1_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "bowl_drainer_1", "kitchen_table_bowl_drainer_init_region"),
            ("Turnon", "flat_stove_1")
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene33(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "bowl_drainer": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "small_akita_black_bowl": 1,
            "large_akita_black_bowl": 1,
            "cream_cheese": 1
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.2],
                region_name="cream_cheese_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.15],
                region_name="bowl_drainer_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.2],
                region_name="akita_black_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.0],
                region_name="small_akita_black_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.2],
                region_name="large_akita_black_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_black_bowl_1", "kitchen_table_akita_black_bowl_1_init_region"),
            ("On", "small_akita_black_bowl_1", "kitchen_table_small_akita_black_bowl_1_init_region"),
            ("On", "large_akita_black_bowl_1", "kitchen_table_large_akita_black_bowl_1_init_region"),
            ("On", "bowl_drainer_1", "kitchen_table_bowl_drainer_init_region"),
            ("On", "cream_cheese_1", "kitchen_table_cream_cheese_init_region"),
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene34(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "bowl_drainer": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "small_akita_black_bowl": 1,
            "large_akita_black_bowl": 1,
            "akita_green_bowl": 1,
            "cream_cheese": 1
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.2],
                region_name="cream_cheese_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.15],
                region_name="bowl_drainer_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.2],
                region_name="akita_black_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.0],
                region_name="small_akita_black_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.2],
                region_name="large_akita_black_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, -0.1],
                region_name="akita_green_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_black_bowl_1", "kitchen_table_akita_black_bowl_1_init_region"),
            ("On", "small_akita_black_bowl_1", "kitchen_table_small_akita_black_bowl_1_init_region"),
            ("On", "large_akita_black_bowl_1", "kitchen_table_large_akita_black_bowl_1_init_region"),
            ("On", "bowl_drainer_1", "kitchen_table_bowl_drainer_init_region"),
            ("On", "cream_cheese_1", "kitchen_table_cream_cheese_init_region"),
            ("On", "akita_green_bowl_1", "kitchen_table_akita_green_bowl_1_init_region"),
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene35(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "bowl_drainer": 1,
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "small_akita_black_bowl": 1,
            "large_akita_black_bowl": 1,
            "cream_cheese": 1
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.2],
                region_name="cream_cheese_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.1],
                region_name="bowl_drainer_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, -0.2],
                region_name="akita_black_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.0],
                region_name="small_akita_black_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, -0.2],
                region_name="large_akita_black_bowl_1_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "akita_black_bowl_1", "kitchen_table_akita_black_bowl_1_init_region"),
            ("On", "small_akita_black_bowl_1", "kitchen_table_small_akita_black_bowl_1_init_region"),
            ("On", "large_akita_black_bowl_1", "kitchen_table_large_akita_black_bowl_1_init_region"),
            ("On", "bowl_drainer_1", "kitchen_table_bowl_drainer_init_region"),
            ("On", "cream_cheese_1", "kitchen_table_cream_cheese_init_region")
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene36(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_cabinet": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "moka_pot": 1,
            "plate": 1,
            "white_yellow_mug": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.15],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, -0.2],
                region_name="wooden_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.2],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.05],
                region_name="moka_pot_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wooden_cabinet_1", "kitchen_table_wooden_cabinet_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "moka_pot_1", "kitchen_table_moka_pot_init_region"), 
            ("On", "white_yellow_mug_1", "kitchen_table_white_yellow_mug_init_region"),
            ("On", "plate_1", "wooden_cabinet_1_top_side"),
            ("Turnon", "flat_stove_1")
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene37(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "chefmate_8_frypan": 1,
            "moka_pot": 1,
            "plate": 1,
            "white_yellow_mug": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.05],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.1],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.15],
                region_name="moka_pot_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "chefmate_8_frypan_1", "flat_stove_1_cook_region"),
            ("On", "moka_pot_1", "kitchen_table_moka_pot_init_region"), 
            ("On", "white_yellow_mug_1", "kitchen_table_white_yellow_mug_init_region"),
            ("On", "plate_1", "wooden_two_layer_shelf_1_top_side"),
            ("Turnon", "flat_stove_1")
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene38(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_two_layer_shelf": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "chefmate_8_frypan": 1,
            "moka_pot": 1,
            "plate": 1,
            "white_yellow_mug": 1,
            "red_coffee_mug": 1
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.05],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, -0.30],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.25],
                region_name="wooden_two_layer_shelf_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.1],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.15],
                region_name="moka_pot_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "chefmate_8_frypan_1", "flat_stove_1_cook_region"),
            ("On", "moka_pot_1", "kitchen_table_moka_pot_init_region"), 
            ("On", "white_yellow_mug_1", "kitchen_table_white_yellow_mug_init_region"),
            ("On", "plate_1", "wooden_two_layer_shelf_1_top_side"),
            ("On", "red_coffee_mug_1", "kitchen_table_red_coffee_mug_init_region"),
            ("Turnon", "flat_stove_1")
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene39(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "moka_pot": 1,
            "plate": 1,
            "white_yellow_mug": 1,
            "red_coffee_mug": 1,
            "porcelain_mug": 1
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.25],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.2],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.25],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.05],
                region_name="porcelain_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.25],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.05],
                region_name="moka_pot_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "moka_pot_1", "kitchen_table_moka_pot_init_region"), 
            ("On", "white_yellow_mug_1", "kitchen_table_white_yellow_mug_init_region"),
            ("On", "red_coffee_mug_1", "kitchen_table_red_coffee_mug_init_region"),
            ("On", "porcelain_mug_1", "kitchen_table_porcelain_mug_init_region"),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("Turnon", "flat_stove_1")
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene40(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "moka_pot": 1,
            "white_yellow_mug": 1,
            "red_coffee_mug": 1,
            "basket": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.25],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.2],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.1],
                region_name="basket_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.25],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.05],
                region_name="moka_pot_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "moka_pot_1", "kitchen_table_moka_pot_init_region"), 
            ("On", "white_yellow_mug_1", "kitchen_table_white_yellow_mug_init_region"),
            ("On", "red_coffee_mug_1", "kitchen_table_red_coffee_mug_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "basket_1", "kitchen_table_basket_init_region"),
            ("Turnon", "flat_stove_1")
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene41(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "short_cabinet": 1,
        }

        object_num_info = {
            "moka_pot": 1,
            "white_yellow_mug": 1,
            "red_coffee_mug": 1,
            "basket": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, -0.25],
                region_name="basket_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.2],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, 0.1],
                region_name="short_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, -0.15],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.0],
                region_name="moka_pot_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "moka_pot_1", "kitchen_table_moka_pot_init_region"), 
            ("On", "white_yellow_mug_1", "kitchen_table_white_yellow_mug_init_region"),
            ("On", "red_coffee_mug_1", "kitchen_table_red_coffee_mug_init_region"),
            ("On", "short_cabinet_1", "kitchen_table_short_cabinet_init_region"),
            ("On", "basket_1", "kitchen_table_basket_init_region"),
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene42(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "short_cabinet": 1,
        }

        object_num_info = {
            "white_yellow_mug": 1,
            "red_coffee_mug": 1,
            "basket": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, -0.2],
                region_name="basket_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, 0.15],
                region_name="short_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.15],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "white_yellow_mug_1", "short_cabinet_1_top_region"),
            ("On", "red_coffee_mug_1", "kitchen_table_red_coffee_mug_init_region"),
            ("On", "short_cabinet_1", "kitchen_table_short_cabinet_init_region"),
            ("On", "basket_1", "kitchen_table_basket_init_region"),
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene43(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "microwave": 1,
        }

        object_num_info = {
            "white_yellow_mug": 1,
            "red_coffee_mug": 1,
            "plate": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.2],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, 0.2],
                region_name="microwave_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.15],
                region_name="red_coffee_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "white_yellow_mug_1", "microwave_1_top_side"),
            ("On", "red_coffee_mug_1", "kitchen_table_red_coffee_mug_init_region"),
            ("On", "microwave_1", "kitchen_table_microwave_init_region"),
            ('Close', 'microwave_1'),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene44(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "microwave": 1,
        }

        object_num_info = {
            "white_yellow_mug": 1,
            "porcelain_mug": 1,
            "plate": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, 0.2],
                region_name="plate_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, -0.2],
                region_name="microwave_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "white_yellow_mug_1", "plate_1"),
            ("On", "porcelain_mug_1", "microwave_1_top_side"),
            ("On", "microwave_1", "kitchen_table_microwave_init_region"),
            ('Close', 'microwave_1'),
            ("On", "plate_1", "kitchen_table_plate_init_region"),
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene45(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "microwave": 1,
            "white_cabinet": 1,
        }

        object_num_info = {
            "small_akita_black_bowl": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, 0.3],
                region_name="white_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, -0.2],
                region_name="microwave_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "small_akita_black_bowl_1", "microwave_1_top_side"),
            ("On", "microwave_1", "kitchen_table_microwave_init_region"),
            ('Open', 'microwave_1'),
            ('Open', 'white_cabinet_1_top_region'),
            ('Open', 'white_cabinet_1_middle_region'),
            ("On", "white_cabinet_1", "kitchen_table_white_cabinet_init_region"),
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene46(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wine_rack": 1,
            "white_cabinet": 1,
        }

        object_num_info = {
            "wine_bottle": 2,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, 0.3],
                region_name="white_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, -0.2],
                region_name="wine_rack_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.05],
                region_name="wine_bottle_2_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wine_rack_1", "kitchen_table_wine_rack_init_region"),
            ("In", "wine_bottle_1", "white_cabinet_1_top_region"),
            ("On", "wine_bottle_2", "kitchen_table_wine_bottle_2_init_region"),
            ('Open', 'white_cabinet_1_top_region'),
            ("On", "white_cabinet_1", "kitchen_table_white_cabinet_init_region"),
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene47(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wine_rack": 1,
            "white_cabinet": 1,
        }

        object_num_info = {
            "wine_bottle": 1,
            "small_akita_black_bowl": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, 0.2],
                region_name="white_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, -0.2],
                region_name="wine_rack_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wine_rack_1", "kitchen_table_wine_rack_init_region"),
            ("On", "wine_bottle_1", "white_cabinet_1_top_side"),
            ("In", "small_akita_black_bowl_1", "white_cabinet_1_bottom_region"),
            ('Open', 'white_cabinet_1_bottom_region'),
            ("On", "white_cabinet_1", "kitchen_table_white_cabinet_init_region"),
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene48(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_cabinet": 1,
        }

        object_num_info = {
            "small_porcelain_mug": 1,
            "small_akita_black_bowl": 1,
            "plate": 3,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.2],
                region_name="plate_nearest_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, 0.2],
                region_name="plate_middle_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.2],
                region_name="plate_farthest_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, -0.2],
                region_name="wooden_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "small_porcelain_mug_1", "wooden_cabinet_1_top_side"),
            ("In", "small_akita_black_bowl_1", "wooden_cabinet_1_bottom_region"),
            ('Open', 'wooden_cabinet_1_bottom_region'),
            ("On", "wooden_cabinet_1", "kitchen_table_wooden_cabinet_init_region"),
            ("On", "plate_1", "kitchen_table_plate_nearest_init_region"),
            ("On", "plate_2", "kitchen_table_plate_middle_init_region"),
            ("On", "plate_3", "kitchen_table_plate_farthest_init_region"),
        ]
        return states
    
@register_mu(scene_type="kitchen")
class ExtensionKitchenScene49(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_cabinet": 1,
        }

        object_num_info = {
            "porcelain_mug": 2,
            "plate": 3,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, 0.2],
                region_name="plate_nearest_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, 0.2],
                region_name="plate_middle_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, 0.2],
                region_name="plate_farthest_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, -0.2],
                region_name="wooden_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("In", "porcelain_mug_1", "wooden_cabinet_1_top_region"),
            ('Open', 'wooden_cabinet_1_top_region'),
            ("On", "wooden_cabinet_1", "kitchen_table_wooden_cabinet_init_region"),
            ("On", "plate_1", "kitchen_table_plate_nearest_init_region"),
            ("On", "plate_2", "kitchen_table_plate_middle_init_region"),
            ("On", "plate_3", "kitchen_table_plate_farthest_init_region"),
            ("On", "porcelain_mug_2", "plate_3"),
        ]
        return states

@register_mu(scene_type="kitchen")
class ExtensionKitchenScene50(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "wooden_cabinet": 1,
        }

        object_num_info = {
            "porcelain_mug": 1,
            "small_akita_black_bowl": 1,
            "plate": 3,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.3, -0.2],
                region_name="plate_nearest_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.1, -0.2],
                region_name="plate_middle_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.1, -0.2],
                region_name="plate_farthest_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0, 0.2],
                region_name="wooden_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                # yaw_rotation=(-np.pi, -np.pi)
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ('Open', 'wooden_cabinet_1_bottom_region'),
            ("In", "small_akita_black_bowl_1", "wooden_cabinet_1_bottom_region"),
            ("On", "wooden_cabinet_1", "kitchen_table_wooden_cabinet_init_region"),
            ("On", "plate_1", "kitchen_table_plate_nearest_init_region"),
            ("On", "plate_2", "kitchen_table_plate_middle_init_region"),
            ("On", "plate_3", "kitchen_table_plate_farthest_init_region"),
            ("On", "porcelain_mug_1", "plate_2"),
        ]
        return states
