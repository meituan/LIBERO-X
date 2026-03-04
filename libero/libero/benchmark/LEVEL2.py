#!/usr/bin/env python3
from libero.libero.utils.bddl_generation_utils import (
    get_xy_region_kwargs_list_from_regions_info,
)
from libero.libero.utils.mu_utils import InitialSceneTemplates, register_mu


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.200],
                region_name='akita_green_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.063,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.250],
                region_name='akita_red_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.063,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.000],
                region_name='akita_yellow_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.085,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.250, 0.000],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.063,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.300],
                region_name='wooden_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.070,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.100],
                region_name='akita_red_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.050,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.000],
                region_name='akita_yellow_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.050,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.200],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.101,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.200],
                region_name='wooden_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.020,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.200, -0.100],
                region_name='akita_green_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.035,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.200, 0.050],
                region_name='akita_red_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.035,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.200],
                region_name='akita_yellow_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.085,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.100, -0.100],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.072,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.300],
                region_name='wooden_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.032,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.100],
                region_name='akita_red_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.085,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.300],
                region_name='akita_yellow_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.085,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.000],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.101,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.200],
                region_name='white_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.061,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.100],
                region_name='akita_red_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.085,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.300],
                region_name='akita_yellow_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.085,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.000],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.101,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.200],
                region_name='white_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.061,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.300],
                region_name='akita_yellow_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.072,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, -0.200],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.072,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.200],
                region_name='white_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.144,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.300],
                region_name='akita_yellow_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.072,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, -0.100],
                region_name='bowl_drainer_init_region',
                target_name='kitchen_table',
                region_half_len=0.032,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.100],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.140,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.200],
                region_name='white_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.070,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.300],
                region_name='akita_black_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.095,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, -0.050],
                region_name='bowl_drainer_init_region',
                target_name='kitchen_table',
                region_half_len=0.055,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.000],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.162,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.300],
                region_name='white_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.095,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.000],
                region_name='akita_black_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.200],
                region_name='akita_green_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, -0.150],
                region_name='bowl_drainer_init_region',
                target_name='kitchen_table',
                region_half_len=0.088,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.200],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.020,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        states = [
            ("On", "akita_black_bowl_1", "kitchen_table_akita_black_bowl_1_init_region"),
            ("On", "akita_green_bowl_1", "kitchen_table_akita_green_bowl_1_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "bowl_drainer_1", "kitchen_table_bowl_drainer_init_region"),
        ]
        return states


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, -0.100],
                region_name='akita_black_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, -0.300],
                region_name='akita_green_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, -0.150],
                region_name='bowl_drainer_init_region',
                target_name='kitchen_table',
                region_half_len=0.010,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.200],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.020,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.000],
                region_name='wine_bottle_init_region',
                target_name='kitchen_table',
                region_half_len=0.030,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.250, 0.250],
                region_name='wine_rack_init_region',
                target_name='kitchen_table',
                region_half_len=0.067,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.000],
                region_name='akita_black_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.200],
                region_name='akita_green_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.150],
                region_name='bowl_drainer_init_region',
                target_name='kitchen_table',
                region_half_len=0.072,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.100, -0.200],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.032,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        states = [
            ("On", "akita_black_bowl_1", "kitchen_table_akita_black_bowl_1_init_region"),
            ("On", "akita_green_bowl_1", "kitchen_table_akita_green_bowl_1_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "bowl_drainer_1", "kitchen_table_bowl_drainer_init_region"),
        ]
        return states
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.200],
                region_name='akita_green_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.000],
                region_name='akita_yellow_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.150],
                region_name='bowl_drainer_init_region',
                target_name='kitchen_table',
                region_half_len=0.072,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.200],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='kitchen_table',
                region_half_len=0.061,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        states = [
            ("On", "akita_green_bowl_1", "kitchen_table_akita_green_bowl_1_init_region"),
            ("On", "akita_yellow_bowl_1", "kitchen_table_akita_yellow_bowl_1_init_region"),
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "bowl_drainer_1", "kitchen_table_bowl_drainer_init_region"),
        ]
        return states


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.150],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.045,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.000],
                region_name='frypan_init_region',
                target_name='kitchen_table',
                region_half_len=0.065,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.200],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='kitchen_table',
                region_half_len=0.061,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "chefmate_8_frypan_1", "kitchen_table_frypan_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
        ]
        return states
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.000],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.065,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.050],
                region_name='frypan_init_region',
                target_name='kitchen_table',
                region_half_len=0.098,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='kitchen_table',
                region_half_len=0.078,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "chefmate_8_frypan_1", "kitchen_table_frypan_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
        ]
        return states
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.100],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.122,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.050],
                region_name='moka_pot_init_region',
                target_name='kitchen_table',
                region_half_len=0.128,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='kitchen_table',
                region_half_len=0.078,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "chefmate_8_frypan_1", "wooden_two_layer_shelf_1_top_side"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "moka_pot_1", "kitchen_table_moka_pot_init_region"), 
        ]
        return states


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.100],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.082,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.050],
                region_name='moka_pot_init_region',
                target_name='kitchen_table',
                region_half_len=0.088,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='kitchen_table',
                region_half_len=0.078,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "chefmate_8_frypan_1", "wooden_two_layer_shelf_1_bottom_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "moka_pot_1", "kitchen_table_moka_pot_init_region"), 
        ]
        return states
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.100],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.122,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.050],
                region_name='moka_pot_init_region',
                target_name='kitchen_table',
                region_half_len=0.128,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='kitchen_table',
                region_half_len=0.078,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.200],
                region_name='akita_black_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.035,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.100],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.146,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.050],
                region_name='moka_pot_init_region',
                target_name='kitchen_table',
                region_half_len=0.045,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='kitchen_table',
                region_half_len=0.088,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.050],
                region_name='akita_black_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.100],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.146,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.150],
                region_name='moka_pot_init_region',
                target_name='kitchen_table',
                region_half_len=0.070,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='kitchen_table',
                region_half_len=0.045,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.050],
                region_name='akita_black_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.100],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.055,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.150],
                region_name='moka_pot_init_region',
                target_name='kitchen_table',
                region_half_len=0.070,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, -0.350],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.095,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='kitchen_table',
                region_half_len=0.045,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, -0.350],
                region_name='akita_red_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.095,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.150],
                region_name='basket_init_region',
                target_name='kitchen_table',
                region_half_len=0.020,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.100],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.055,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.050],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='kitchen_table',
                region_half_len=0.045,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.050],
                region_name='akita_black_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.150],
                region_name='basket_init_region',
                target_name='kitchen_table',
                region_half_len=0.020,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.100],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.055,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, -0.350],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.095,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='kitchen_table',
                region_half_len=0.045,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.050],
                region_name='akita_black_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.040,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.050, 0.050],
                region_name='akita_blue_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.040,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, -0.350],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.051,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.150],
                region_name='wooden_tray_init_region',
                target_name='kitchen_table',
                region_half_len=0.023,
                yaw_rotation=(1.571, 1.571),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='kitchen_table',
                region_half_len=0.023,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.050],
                region_name='akita_green_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.065,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.100, 0.050],
                region_name='plate_2_init_region',
                target_name='kitchen_table',
                region_half_len=0.042,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, -0.350],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.061,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.150],
                region_name='wooden_tray_init_region',
                target_name='kitchen_table',
                region_half_len=0.022,
                yaw_rotation=(1.571, 1.571),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='kitchen_table',
                region_half_len=0.032,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.050],
                region_name='akita_green_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.045,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.100, 0.050],
                region_name='plate_2_init_region',
                target_name='kitchen_table',
                region_half_len=0.032,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, -0.350],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.031,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.250],
                region_name='wooden_shelf_init_region',
                target_name='kitchen_table',
                region_half_len=0.022,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.150],
                region_name='wooden_tray_init_region',
                target_name='kitchen_table',
                region_half_len=0.022,
                yaw_rotation=(1.571, 1.571),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.200],
                region_name='akita_green_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.118,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.250],
                region_name='microwave_init_region',
                target_name='kitchen_table',
                region_half_len=0.080,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.300],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.118,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.050, 0.000],
                region_name='akita_blue_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.039,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.200],
                region_name='akita_green_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.010,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.100],
                region_name='plate_2_init_region',
                target_name='kitchen_table',
                region_half_len=0.010,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.300],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.118,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.150],
                region_name='short_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.010,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.050, 0.050],
                region_name='akita_blue_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.035,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.220],
                region_name='akita_green_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.045,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.100, 0.300],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.068,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.150],
                region_name='short_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.023,
                yaw_rotation=(1.571, 1.571),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.050],
                region_name='white_bowl_init_region',
                target_name='kitchen_table',
                region_half_len=0.035,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.200],
                region_name='akita_green_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.000],
                region_name='akita_yellow_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.150],
                region_name='bowl_drainer_init_region',
                target_name='kitchen_table',
                region_half_len=0.072,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.200],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='kitchen_table',
                region_half_len=0.061,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.150],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.010,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.000],
                region_name='frypan_init_region',
                target_name='kitchen_table',
                region_half_len=0.040,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.000],
                region_name='glazed_rim_porcelain_ramekin_init_region',
                target_name='kitchen_table',
                region_half_len=0.025,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.200],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='kitchen_table',
                region_half_len=0.020,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        states = [
            ("On", "wooden_two_layer_shelf_1", "kitchen_table_wooden_two_layer_shelf_init_region"),
            ("On", "chefmate_8_frypan_1", "kitchen_table_frypan_init_region"),
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "glazed_rim_porcelain_ramekin_1", "kitchen_table_glazed_rim_porcelain_ramekin_init_region"),
        ]
        return states


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.000],
                region_name='akita_black_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, -0.150],
                region_name='bowl_drainer_init_region',
                target_name='kitchen_table',
                region_half_len=0.072,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.200],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.030,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, -0.200],
                region_name='large_akita_black_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.200],
                region_name='small_akita_black_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.200],
                region_name='akita_black_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.150],
                region_name='bowl_drainer_init_region',
                target_name='kitchen_table',
                region_half_len=0.097,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.200],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.030,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, -0.200],
                region_name='large_akita_black_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.000],
                region_name='small_akita_black_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.200],
                region_name='akita_black_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.150],
                region_name='bowl_drainer_init_region',
                target_name='kitchen_table',
                region_half_len=0.097,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.200],
                region_name='cream_cheese_init_region',
                target_name='kitchen_table',
                region_half_len=0.090,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, -0.200],
                region_name='large_akita_black_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.000],
                region_name='small_akita_black_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.200],
                region_name='akita_black_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, -0.100],
                region_name='akita_green_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.150],
                region_name='bowl_drainer_init_region',
                target_name='kitchen_table',
                region_half_len=0.047,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.200],
                region_name='cream_cheese_init_region',
                target_name='kitchen_table',
                region_half_len=0.061,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, -0.200],
                region_name='large_akita_black_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.000],
                region_name='small_akita_black_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, -0.200],
                region_name='akita_black_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.100],
                region_name='bowl_drainer_init_region',
                target_name='kitchen_table',
                region_half_len=0.072,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.200],
                region_name='cream_cheese_init_region',
                target_name='kitchen_table',
                region_half_len=0.090,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.100, -0.200],
                region_name='large_akita_black_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.000],
                region_name='small_akita_black_bowl_1_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.200],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.106,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.050],
                region_name='moka_pot_init_region',
                target_name='kitchen_table',
                region_half_len=0.070,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.150],
                region_name='white_yellow_mug_init_region',
                target_name='kitchen_table',
                region_half_len=0.050,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.050, -0.200],
                region_name='wooden_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.045,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.100],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.086,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.150],
                region_name='moka_pot_init_region',
                target_name='kitchen_table',
                region_half_len=0.050,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.050],
                region_name='white_yellow_mug_init_region',
                target_name='kitchen_table',
                region_half_len=0.050,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='kitchen_table',
                region_half_len=0.045,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.100],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.122,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.150],
                region_name='moka_pot_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.050, -0.300],
                region_name='red_coffee_mug_init_region',
                target_name='kitchen_table',
                region_half_len=0.050,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.050],
                region_name='white_yellow_mug_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='kitchen_table',
                region_half_len=0.045,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.250],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.088,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.050],
                region_name='moka_pot_init_region',
                target_name='kitchen_table',
                region_half_len=0.035,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, 0.250],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, 0.050],
                region_name='porcelain_mug_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.250],
                region_name='red_coffee_mug_init_region',
                target_name='kitchen_table',
                region_half_len=0.110,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.200],
                region_name='white_yellow_mug_init_region',
                target_name='kitchen_table',
                region_half_len=0.025,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.100],
                region_name='basket_init_region',
                target_name='kitchen_table',
                region_half_len=0.072,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.250],
                region_name='flat_stove_init_region',
                target_name='kitchen_table',
                region_half_len=0.088,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, 0.050],
                region_name='moka_pot_init_region',
                target_name='kitchen_table',
                region_half_len=0.045,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.250],
                region_name='red_coffee_mug_init_region',
                target_name='kitchen_table',
                region_half_len=0.105,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, 0.200],
                region_name='white_yellow_mug_init_region',
                target_name='kitchen_table',
                region_half_len=0.035,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.100, -0.250],
                region_name='basket_init_region',
                target_name='kitchen_table',
                region_half_len=0.032,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, 0.000],
                region_name='moka_pot_init_region',
                target_name='kitchen_table',
                region_half_len=0.073,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, -0.150],
                region_name='red_coffee_mug_init_region',
                target_name='kitchen_table',
                region_half_len=0.072,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.100],
                region_name='short_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.047,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.200],
                region_name='white_yellow_mug_init_region',
                target_name='kitchen_table',
                region_half_len=0.063,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.050, -0.200],
                region_name='basket_init_region',
                target_name='kitchen_table',
                region_half_len=0.023,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.150],
                region_name='red_coffee_mug_init_region',
                target_name='kitchen_table',
                region_half_len=0.063,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.150],
                region_name='short_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.088,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        states = [
            ("On", "white_yellow_mug_1", "short_cabinet_1_top_region"),
            ("On", "red_coffee_mug_1", "kitchen_table_red_coffee_mug_init_region"),
            ("On", "short_cabinet_1", "kitchen_table_short_cabinet_init_region"),
            ("On", "basket_1", "kitchen_table_basket_init_region"),
        ]
        return states


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.200],
                region_name='microwave_init_region',
                target_name='kitchen_table',
                region_half_len=0.110,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, -0.200],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.112,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.150],
                region_name='red_coffee_mug_init_region',
                target_name='kitchen_table',
                region_half_len=0.112,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.200],
                region_name='microwave_init_region',
                target_name='kitchen_table',
                region_half_len=0.134,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, 0.200],
                region_name='plate_init_region',
                target_name='kitchen_table',
                region_half_len=0.174,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.200],
                region_name='microwave_init_region',
                target_name='kitchen_table',
                region_half_len=0.175,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.100, 0.300],
                region_name='white_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.175,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.100, 0.300],
                region_name='white_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.080,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.050],
                region_name='wine_bottle_2_init_region',
                target_name='kitchen_table',
                region_half_len=0.065,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.200],
                region_name='wine_rack_init_region',
                target_name='kitchen_table',
                region_half_len=0.075,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.200],
                region_name='white_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.200],
                region_name='wine_rack_init_region',
                target_name='kitchen_table',
                region_half_len=0.070,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.200],
                region_name='plate_farthest_init_region',
                target_name='kitchen_table',
                region_half_len=0.040,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.100, 0.200],
                region_name='plate_middle_init_region',
                target_name='kitchen_table',
                region_half_len=0.040,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.200],
                region_name='plate_nearest_init_region',
                target_name='kitchen_table',
                region_half_len=0.040,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.200],
                region_name='wooden_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.086,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.200],
                region_name='plate_farthest_init_region',
                target_name='kitchen_table',
                region_half_len=0.040,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.100, 0.200],
                region_name='plate_middle_init_region',
                target_name='kitchen_table',
                region_half_len=0.040,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.200],
                region_name='plate_nearest_init_region',
                target_name='kitchen_table',
                region_half_len=0.040,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.200],
                region_name='wooden_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.096,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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


@register_mu(scene_type='kitchen')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, -0.200],
                region_name='plate_farthest_init_region',
                target_name='kitchen_table',
                region_half_len=0.040,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.100, -0.200],
                region_name='plate_middle_init_region',
                target_name='kitchen_table',
                region_half_len=0.040,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.200],
                region_name='plate_nearest_init_region',
                target_name='kitchen_table',
                region_half_len=0.040,
                yaw_rotation=(3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.200],
                region_name='wooden_cabinet_init_region',
                target_name='kitchen_table',
                region_half_len=0.066,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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

@register_mu(scene_type='study')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.050],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, 0.250],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.062,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, -0.150],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.200],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.066,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, -0.200],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.066,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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


@register_mu(scene_type='study')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.050, -0.050],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.016,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, 0.250],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.082,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, -0.150],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.016,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.200],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.075,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, -0.200],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.065,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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



@register_mu(scene_type='study')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.140, 0.100],
                region_name='black_book_A_init_region',
                target_name='study_table',
                region_half_len=0.054,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.020, -0.200],
                region_name='black_book_B_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.160, 0.250],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.044,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.050, -0.060],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.038,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.120, -0.220],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
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



@register_mu(scene_type='study')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.050],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, 0.250],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.052,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.200],
                region_name='green_book_init_region',
                target_name='study_table',
                region_half_len=0.056,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, -0.150],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, -0.200],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.056,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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



@register_mu(scene_type='study')
class ExtensionStudyScene5(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, 0.240],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.088,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.020, -0.250],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.010,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.060, -0.190],
                region_name='red_book_init_region',
                target_name='study_table',
                region_half_len=0.010,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.120, -0.080],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.034,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.190, 0.050],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.034,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]



@register_mu(scene_type='study')
class ExtensionStudyScene6(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.220],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.043,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.180],
                region_name='red_book_init_region',
                target_name='study_table',
                region_half_len=0.041,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.160],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.021,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.120, 0.020],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.021,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, -0.140],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.126,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]



@register_mu(scene_type='study')
class ExtensionStudyScene7(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.160, 0.050],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.015,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, 0.220],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.069,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.160],
                region_name='green_book_init_region',
                target_name='study_table',
                region_half_len=0.015,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.160, -0.120],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.050, -0.210],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.000],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.024,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.100, -0.200],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.035,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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



@register_mu(scene_type='study')
class ExtensionStudyScene8(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, 0.250],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.069,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.050, -0.190],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.019,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.160, -0.230],
                region_name='red_book_A_init_region',
                target_name='study_table',
                region_half_len=0.019,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.200, -0.040],
                region_name='red_book_B_init_region',
                target_name='study_table',
                region_half_len=0.032,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.120, -0.160],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.032,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "red_book_1", "study_table_red_book_A_init_region"),
            ("On", "red_book_2", "study_table_red_book_B_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]



@register_mu(scene_type='study')
class ExtensionStudyScene9(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, 0.250],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.064,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, 0.180],
                region_name='green_book_init_region',
                target_name='study_table',
                region_half_len=0.067,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.140, -0.050],
                region_name='red_book_init_region',
                target_name='study_table',
                region_half_len=0.040,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.020, -0.060],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.030,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.170, -0.120],
                region_name='yellow_book_A_init_region',
                target_name='study_table',
                region_half_len=0.041,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.020, -0.200],
                region_name='yellow_book_B_init_region',
                target_name='study_table',
                region_half_len=0.030,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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



@register_mu(scene_type='study')
class ExtensionStudyScene10(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.050, -0.200],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.032,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, 0.250],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.065,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.140, -0.160],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.028,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.220, -0.300],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.059,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.030, -0.080],
                region_name='striped_book_A_init_region',
                target_name='study_table',
                region_half_len=0.028,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.170, 0.130],
                region_name='striped_book_B_init_region',
                target_name='study_table',
                region_half_len=0.086,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    

@register_mu(scene_type='study')
class ExtensionStudyScene11(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.050],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, -0.250],
                region_name='desk_caddy_right_init_region',
                target_name='study_table',
                region_half_len=0.062,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.150],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.200],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.086,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, 0.200],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.066,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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




@register_mu(scene_type='study')
class ExtensionStudyScene12(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.050, 0.050],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.016,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, -0.250],
                region_name='desk_caddy_right_init_region',
                target_name='study_table',
                region_half_len=0.062,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.150],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.016,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.200],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.065,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, 0.200],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.085,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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





@register_mu(scene_type='study')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.140, -0.100],
                region_name='black_book_A_init_region',
                target_name='study_table',
                region_half_len=0.084,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.020, 0.200],
                region_name='black_book_B_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.160, -0.250],
                region_name='desk_caddy_right_init_region',
                target_name='study_table',
                region_half_len=0.094,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.050, 0.060],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.038,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.120, 0.220],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
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





@register_mu(scene_type='study')
class ExtensionStudyScene14(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.050],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, -0.250],
                region_name='desk_caddy_right_init_region',
                target_name='study_table',
                region_half_len=0.052,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.200],
                region_name='green_book_init_region',
                target_name='study_table',
                region_half_len=0.066,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.150],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, 0.200],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.066,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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





@register_mu(scene_type='study')
class ExtensionStudyScene15(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, -0.240],
                region_name='desk_caddy_right_init_region',
                target_name='study_table',
                region_half_len=0.068,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.020, 0.250],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.010,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.060, 0.190],
                region_name='red_book_init_region',
                target_name='study_table',
                region_half_len=0.010,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.120, 0.080],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.034,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.190, -0.050],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.034,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_right_1", "study_table_desk_caddy_right_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]





@register_mu(scene_type='study')
class ExtensionStudyScene16(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, -0.220],
                region_name='desk_caddy_right_init_region',
                target_name='study_table',
                region_half_len=0.063,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.180],
                region_name='red_book_init_region',
                target_name='study_table',
                region_half_len=0.061,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, -0.160],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.120, -0.020],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, 0.140],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.086,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_right_1", "study_table_desk_caddy_right_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]





@register_mu(scene_type='study')
class ExtensionStudyScene17(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.160, -0.050],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.015,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, -0.220],
                region_name='desk_caddy_right_init_region',
                target_name='study_table',
                region_half_len=0.049,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.160],
                region_name='green_book_init_region',
                target_name='study_table',
                region_half_len=0.015,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.160, 0.120],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.050, 0.210],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.000],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.034,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.100, 0.200],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.035,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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





@register_mu(scene_type='study')
class ExtensionStudyScene18(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, -0.250],
                region_name='desk_caddy_right_init_region',
                target_name='study_table',
                region_half_len=0.099,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.050, 0.190],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.019,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.160, 0.230],
                region_name='red_book_A_init_region',
                target_name='study_table',
                region_half_len=0.019,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.200, 0.040],
                region_name='red_book_B_init_region',
                target_name='study_table',
                region_half_len=0.032,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.120, 0.160],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.032,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_right_1", "study_table_desk_caddy_right_init_region"),
            ("On", "red_book_1", "study_table_red_book_A_init_region"),
            ("On", "red_book_2", "study_table_red_book_B_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]





@register_mu(scene_type='study')
class ExtensionStudyScene19(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, -0.250],
                region_name='desk_caddy_right_init_region',
                target_name='study_table',
                region_half_len=0.084,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, -0.180],
                region_name='green_book_init_region',
                target_name='study_table',
                region_half_len=0.077,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.140, 0.050],
                region_name='red_book_init_region',
                target_name='study_table',
                region_half_len=0.040,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.020, 0.060],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.030,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.170, 0.120],
                region_name='yellow_book_A_init_region',
                target_name='study_table',
                region_half_len=0.041,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.020, 0.200],
                region_name='yellow_book_B_init_region',
                target_name='study_table',
                region_half_len=0.030,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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





@register_mu(scene_type='study')
class ExtensionStudyScene20(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.050, 0.200],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.032,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, -0.250],
                region_name='desk_caddy_right_init_region',
                target_name='study_table',
                region_half_len=0.085,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.140, 0.160],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.028,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.220, 0.300],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.059,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.030, 0.080],
                region_name='striped_book_A_init_region',
                target_name='study_table',
                region_half_len=0.028,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.170, -0.130],
                region_name='striped_book_B_init_region',
                target_name='study_table',
                region_half_len=0.086,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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



@register_mu(scene_type='study')
class ExtensionStudyScene21(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.050],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.034,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.000],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.035,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, -0.160],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.034,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.180],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.097,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, -0.200],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.066,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
        ]



@register_mu(scene_type='study')
class ExtensionStudyScene22(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.040, -0.110],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.046,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.000],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.035,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, 0.050],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.066,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.060, 0.220],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.087,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.100, -0.210],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.046,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
        ]



@register_mu(scene_type='study')
class ExtensionStudyScene23(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.160, 0.100],
                region_name='black_book_A_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.020, -0.220],
                region_name='black_book_B_init_region',
                target_name='study_table',
                region_half_len=0.020,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.000],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.039,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, -0.040],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.050, -0.060],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.041,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.140, -0.220],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.020,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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



@register_mu(scene_type='study')
class ExtensionStudyScene24(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.020, -0.040],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.041,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.000],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.039,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, 0.050],
                region_name='green_book_init_region',
                target_name='study_table',
                region_half_len=0.050,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.120, -0.120],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.041,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.130, -0.220],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.065,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "green_book_1", "study_table_green_book_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
        ]



@register_mu(scene_type='study')
class ExtensionStudyScene25(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.000],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.034,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.120, -0.140],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.034,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.020, -0.250],
                region_name='red_book_init_region',
                target_name='study_table',
                region_half_len=0.034,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.100],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.058,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, -0.080],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.058,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]



@register_mu(scene_type='study')
class ExtensionStudyScene26(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.000],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.030,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.080, -0.220],
                region_name='red_book_init_region',
                target_name='study_table',
                region_half_len=0.064,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.020, 0.200],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.109,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, -0.020],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.072,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.120, -0.160],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.064,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "red_coffee_mug_1", "study_table_red_coffee_mug_init_region"),
            ("On", "yellow_book_1", "study_table_yellow_book_init_region"),
            ("On", "red_book_1", "study_table_red_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]



@register_mu(scene_type='study')
class ExtensionStudyScene27(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.080, 0.180],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.054,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.000],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.032,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, -0.020],
                region_name='green_book_init_region',
                target_name='study_table',
                region_half_len=0.042,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.120, -0.220],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.041,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.040, -0.240],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.010,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.020, 0.020],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.042,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.120, -0.200],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.010,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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



@register_mu(scene_type='study')
class ExtensionStudyScene28(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.000],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.030,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.020],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.052,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.120, -0.250],
                region_name='red_book_A_init_region',
                target_name='study_table',
                region_half_len=0.090,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, -0.060],
                region_name='red_book_B_init_region',
                target_name='study_table',
                region_half_len=0.052,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.020, 0.180],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    @property
    def init_states(self):
        return [
            ("On", "desk_caddy_back_1", "study_table_desk_caddy_back_init_region"),
            ("On", "red_book_1", "study_table_red_book_A_init_region"),
            ("On", "red_book_2", "study_table_red_book_B_init_region"),
            ("On", "orange_book_1", "study_table_orange_book_init_region"),
            ("On", "striped_book_1", "study_table_striped_book_init_region"),
        ]



@register_mu(scene_type='study')
class ExtensionStudyScene29(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.000],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.033,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.160, 0.180],
                region_name='green_book_init_region',
                target_name='study_table',
                region_half_len=0.051,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.120, 0.000],
                region_name='red_book_init_region',
                target_name='study_table',
                region_half_len=0.052,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.020, 0.160],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.051,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.120, -0.100],
                region_name='yellow_book_A_init_region',
                target_name='study_table',
                region_half_len=0.045,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.220],
                region_name='yellow_book_B_init_region',
                target_name='study_table',
                region_half_len=0.045,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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



@register_mu(scene_type='study')
class ExtensionStudyScene30(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.120, -0.200],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.060,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, 0.000],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.035,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.080, -0.200],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.054,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.050],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.028,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.040, 0.180],
                region_name='striped_book_A_init_region',
                target_name='study_table',
                region_half_len=0.028,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, -0.040],
                region_name='striped_book_B_init_region',
                target_name='study_table',
                region_half_len=0.034,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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


@register_mu(scene_type='study')
class ExtensionStudyScene31(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.050],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.024,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.200],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.035,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, 0.250],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.059,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, -0.160],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.034,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, 0.180],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.057,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, -0.200],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.025,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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



@register_mu(scene_type='study')
class ExtensionStudyScene32(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.040, -0.110],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.046,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.200],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.040,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, 0.250],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.096,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.200, -0.200],
                region_name='red_book_init_region',
                target_name='study_table',
                region_half_len=0.052,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, 0.050],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.066,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.100, -0.210],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.046,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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



@register_mu(scene_type='study')
class ExtensionStudyScene33(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.160, 0.100],
                region_name='black_book_A_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.080, -0.220],
                region_name='black_book_B_init_region',
                target_name='study_table',
                region_half_len=0.043,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.200],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, 0.250],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.068,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, -0.040],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.050, -0.060],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.052,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.140, -0.220],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.041,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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



@register_mu(scene_type='study')
class ExtensionStudyScene34(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.020, -0.040],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.041,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.200],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.040,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, 0.250],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.056,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, 0.050],
                region_name='green_book_init_region',
                target_name='study_table',
                region_half_len=0.050,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.120, -0.120],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.100, -0.220],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.058,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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



@register_mu(scene_type='study')
class ExtensionStudyScene35(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.200],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.035,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, 0.250],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.049,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.120, -0.140],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.024,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.020, -0.250],
                region_name='red_book_init_region',
                target_name='study_table',
                region_half_len=0.024,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.100],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.048,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, -0.080],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.038,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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



@register_mu(scene_type='study')
class ExtensionStudyScene36(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.200],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.032,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, 0.250],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.048,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.080, -0.220],
                region_name='red_book_init_region',
                target_name='study_table',
                region_half_len=0.044,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.020, 0.000],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.054,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, -0.020],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.040,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.120, -0.160],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.052,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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



@register_mu(scene_type='study')
class ExtensionStudyScene37(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.080, -0.080],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.200],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.041,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, 0.250],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.042,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, -0.020],
                region_name='green_book_init_region',
                target_name='study_table',
                region_half_len=0.032,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.120, -0.220],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.033,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.040, -0.240],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.010,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.020, 0.020],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.120, -0.200],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.010,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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



@register_mu(scene_type='study')
class ExtensionStudyScene38(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.200],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.033,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, 0.250],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.042,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.020],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.052,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.120, -0.250],
                region_name='red_book_A_init_region',
                target_name='study_table',
                region_half_len=0.053,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, -0.060],
                region_name='red_book_B_init_region',
                target_name='study_table',
                region_half_len=0.052,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.220, 0.180],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.082,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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



@register_mu(scene_type='study')
class ExtensionStudyScene39(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.200],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.033,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, 0.250],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.044,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.160, 0.180],
                region_name='green_book_init_region',
                target_name='study_table',
                region_half_len=0.052,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.120, 0.000],
                region_name='red_book_init_region',
                target_name='study_table',
                region_half_len=0.042,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.160, -0.160],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.042,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.120, -0.100],
                region_name='yellow_book_A_init_region',
                target_name='study_table',
                region_half_len=0.045,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, -0.220],
                region_name='yellow_book_B_init_region',
                target_name='study_table',
                region_half_len=0.045,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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



@register_mu(scene_type='study')
class ExtensionStudyScene40(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.120, -0.200],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.050,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.300, -0.200],
                region_name='desk_caddy_back_init_region',
                target_name='study_table',
                region_half_len=0.040,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, 0.250],
                region_name='desk_caddy_init_region',
                target_name='study_table',
                region_half_len=0.058,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.080, -0.200],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.054,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.170, 0.180],
                region_name='striped_book_A_init_region',
                target_name='study_table',
                region_half_len=0.070,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, -0.040],
                region_name='striped_book_B_init_region',
                target_name='study_table',
                region_half_len=0.054,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

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
    
        

@register_mu(scene_type='study')
class ExtensionStudyScene41(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.050],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.150],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.200],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.106,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, -0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='study_table',
                region_half_len=0.072,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, 0.200],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.066,
                yaw_rotation=(0.000, 0.000),
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



@register_mu(scene_type='study')
class ExtensionStudyScene42(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.050, 0.050],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.016,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.150],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.016,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.200],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.095,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, -0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='study_table',
                region_half_len=0.072,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, 0.200],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.085,
                yaw_rotation=(0.000, 0.000),
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



@register_mu(scene_type='study')
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.140, -0.100],
                region_name='black_book_A_init_region',
                target_name='study_table',
                region_half_len=0.084,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.020, 0.200],
                region_name='black_book_B_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.050, 0.060],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.038,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.160, -0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='study_table',
                region_half_len=0.084,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.120, 0.220],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
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



@register_mu(scene_type='study')
class ExtensionStudyScene44(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.000, 0.050],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.150, -0.200],
                region_name='green_book_init_region',
                target_name='study_table',
                region_half_len=0.106,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, 0.150],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.031,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, -0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='study_table',
                region_half_len=0.072,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.150, 0.200],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.066,
                yaw_rotation=(0.000, 0.000),
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



@register_mu(scene_type='study')
class ExtensionStudyScene45(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.020, 0.250],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.010,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.060, 0.190],
                region_name='red_book_init_region',
                target_name='study_table',
                region_half_len=0.010,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.120, 0.080],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.034,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.190, -0.050],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.034,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, -0.240],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='study_table',
                region_half_len=0.128,
                yaw_rotation=(0.000, 0.000),
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



@register_mu(scene_type='study')
class ExtensionStudyScene46(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, 0.060],
                region_name='red_book_init_region',
                target_name='study_table',
                region_half_len=0.018,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.100, -0.160],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.077,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.120, 0.160],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.018,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.200, -0.220],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='study_table',
                region_half_len=0.073,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, 0.140],
                region_name='yellow_book_init_region',
                target_name='study_table',
                region_half_len=0.110,
                yaw_rotation=(0.000, 0.000),
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



@register_mu(scene_type='study')
class ExtensionStudyScene47(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.050, 0.190],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.019,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.160, 0.230],
                region_name='red_book_A_init_region',
                target_name='study_table',
                region_half_len=0.019,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.200, 0.040],
                region_name='red_book_B_init_region',
                target_name='study_table',
                region_half_len=0.032,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.010, 0.000],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.057,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.120, 0.160],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.032,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, -0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='study_table',
                region_half_len=0.077,
                yaw_rotation=(0.000, 0.000),
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



@register_mu(scene_type='study')
class ExtensionStudyScene48(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.050, 0.190],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.019,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.160, 0.230],
                region_name='red_book_A_init_region',
                target_name='study_table',
                region_half_len=0.019,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.200, 0.040],
                region_name='red_book_B_init_region',
                target_name='study_table',
                region_half_len=0.032,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.120, 0.160],
                region_name='striped_book_init_region',
                target_name='study_table',
                region_half_len=0.032,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, -0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='study_table',
                region_half_len=0.149,
                yaw_rotation=(0.000, 0.000),
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



@register_mu(scene_type='study')
class ExtensionStudyScene49(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.180, -0.180],
                region_name='green_book_init_region',
                target_name='study_table',
                region_half_len=0.077,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.140, 0.050],
                region_name='red_book_init_region',
                target_name='study_table',
                region_half_len=0.040,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.020, 0.060],
                region_name='white_yellow_mug_init_region',
                target_name='study_table',
                region_half_len=0.030,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, -0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='study_table',
                region_half_len=0.094,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.170, 0.120],
                region_name='yellow_book_A_init_region',
                target_name='study_table',
                region_half_len=0.041,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.020, 0.200],
                region_name='yellow_book_B_init_region',
                target_name='study_table',
                region_half_len=0.030,
                yaw_rotation=(0.000, 0.000),
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



@register_mu(scene_type='study')
class ExtensionStudyScene50(InitialSceneTemplates):
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
        """Auto-generated Level-2 test scene."""
        self.regions = {}
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.050, 0.200],
                region_name='black_book_init_region',
                target_name='study_table',
                region_half_len=0.032,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.140, 0.160],
                region_name='orange_book_init_region',
                target_name='study_table',
                region_half_len=0.028,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.220, 0.300],
                region_name='red_coffee_mug_init_region',
                target_name='study_table',
                region_half_len=0.059,
                yaw_rotation=(-3.142, 3.142),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.030, 0.080],
                region_name='striped_book_A_init_region',
                target_name='study_table',
                region_half_len=0.028,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.170, -0.130],
                region_name='striped_book_B_init_region',
                target_name='study_table',
                region_half_len=0.086,
                yaw_rotation=(0.000, 0.000),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.180, -0.250],
                region_name='wooden_two_layer_shelf_init_region',
                target_name='study_table',
                region_half_len=0.105,
                yaw_rotation=(0.000, 0.000),
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



