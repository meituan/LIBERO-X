import os
import pathlib
import re

import numpy as np
from robosuite.models.objects import MujocoXMLObject
from robosuite.utils.mjcf_utils import array_to_string

absolute_path = pathlib.Path(__file__).parent.parent.parent.absolute()
from libero.libero.envs.base_object import register_object
from libero.libero.envs.objects.turbosquid_objects import TurbosquidObjects


class ExtensionObjects(MujocoXMLObject):
    def __init__(self, asset_path, name, joints=[dict(type="free", damping="0.0005")]):
        assert os.path.isabs(asset_path), "Asset path must be an absolute path"
        assert asset_path.endswith(".xml"), "Asset path must be an xml file"
        super().__init__(
            asset_path, name=name, joints=joints, obj_type="all", duplicate_collision_geoms=False
        )
        self.category_name = "_".join(
            re.sub(r"([A-Z])", r" \1", self.__class__.__name__).split()
        ).lower()
        self.object_properties = {"vis_site_names": {}}


@register_object
class SmallPorcelainMug(TurbosquidObjects):
    def __init__(
        self,
        name="small_porcelain_mug",
        obj_name="small_porcelain_mug",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 2)

@register_object
class SmallPorcelainMugInverted(TurbosquidObjects):
    def __init__(
        self,
        name="small_porcelain_mug_inverted",
        obj_name="small_porcelain_mug",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (np.pi / 2, np.pi / 2)
        

@register_object
class LiberoMug(ExtensionObjects):
    def __init__(self, name="libero_mug", class_name="libero_mug", obj_name="libero_mug"):
        libero_mug_path = os.path.join(
            absolute_path, f"assets/extension_objects/{class_name}/{obj_name}.xml"
        )
        # print(f"Libero Mug asset path: {libero_mug_path}")
        super().__init__(asset_path=libero_mug_path, name=name)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class LiberoYellowMug(ExtensionObjects):
    def __init__(self, name="libero_mug", category_name="libero_mug", obj_name="libero_white_yellow_mug"):
        libero_mug_path = os.path.join(
            absolute_path, f"assets/extension_objects/{category_name}/{obj_name}.xml"
        )
        # print(f"Libero Mug asset path: {libero_mug_path}")
        super().__init__(asset_path=libero_mug_path, name=name)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class AkitaBlueBowl(ExtensionObjects):
    def __init__(
        self,
        name="akita_blue_bowl",
        category_name: str = "akita_bowl",
        obj_name: str = "akita_blue_bowl",
    ):
        akita_blue_bowl = os.path.join(
            absolute_path, f"assets/extension_objects/{category_name}/{obj_name}.xml"
        )
        super().__init__(asset_path=akita_blue_bowl, name=name)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class AkitaRedBowl(ExtensionObjects):
    def __init__(
        self,
        name="akita_red_bowl",
        category_name: str = "akita_bowl",
        obj_name: str = "akita_red_bowl",
    ):
        akita_red_bowl = os.path.join(
            absolute_path, f"assets/extension_objects/{category_name}/{obj_name}.xml"
        )
        super().__init__(asset_path=akita_red_bowl, name=name)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class AkitaGreenBowl(ExtensionObjects):
    def __init__(
        self,
        name="akita_green_bowl",
        category_name: str = "akita_bowl",
        obj_name: str = "akita_green_bowl",
    ):
        akita_red_bowl = os.path.join(
            absolute_path, f"assets/extension_objects/{category_name}/{obj_name}.xml"
        )
        super().__init__(asset_path=akita_red_bowl, name=name)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class AkitaYellowBowl(ExtensionObjects):
    def __init__(
        self,
        name="akita_yellow_bowl",
        category_name: str = "akita_bowl",
        obj_name: str = "akita_yellow_bowl",
    ):
        akita_red_bowl = os.path.join(
            absolute_path, f"assets/extension_objects/{category_name}/{obj_name}.xml"
        )
        super().__init__(asset_path=akita_red_bowl, name=name)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class AkitaPurpleBowl(ExtensionObjects):
    def __init__(
        self,
        name="akita_purple_bowl",
        category_name: str = "akita_bowl",
        obj_name: str = "akita_purple_bowl",
    ):
        akita_red_bowl = os.path.join(
            absolute_path, f"assets/extension_objects/{category_name}/{obj_name}.xml"
        )
        super().__init__(asset_path=akita_red_bowl, name=name)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class SmallAkitaRedBowl(ExtensionObjects):
    def __init__(
        self,
        name="small_akita_red_bowl",
        category_name: str = "akita_bowl",
        obj_name: str = "small_akita_red_bowl",
    ):
        akita_red_bowl = os.path.join(
            absolute_path, f"assets/extension_objects/{category_name}/{obj_name}.xml"
        )
        super().__init__(asset_path=akita_red_bowl, name=name)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class LargeAkitaRedBowl(ExtensionObjects):
    def __init__(
        self,
        name="large_akita_red_bowl",
        category_name: str = "akita_bowl",
        obj_name: str = "large_akita_red_bowl",
    ):
        akita_red_bowl = os.path.join(
            absolute_path, f"assets/extension_objects/{category_name}/{obj_name}.xml"
        )
        super().__init__(asset_path=akita_red_bowl, name=name)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object
class SmallAkitaBlackBowl(ExtensionObjects):
    def __init__(
        self,
        name="small_akita_black_bowl",
        category_name: str = "akita_bowl",
        obj_name: str = "small_akita_black_bowl",
    ):
        akita_black_bowl = os.path.join(
            absolute_path, f"assets/extension_objects/{category_name}/{obj_name}.xml"
        )
        super().__init__(asset_path=akita_black_bowl, name=name)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class LargeAkitaBlackBowl(ExtensionObjects):
    def __init__(
        self,
        name="large_akita_black_bowl",
        category_name: str = "akita_bowl",
        obj_name: str = "large_akita_black_bowl",
    ):
        akita_black_bowl = os.path.join(
            absolute_path, f"assets/extension_objects/{category_name}/{obj_name}.xml"
        )
        super().__init__(asset_path=akita_black_bowl, name=name)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

