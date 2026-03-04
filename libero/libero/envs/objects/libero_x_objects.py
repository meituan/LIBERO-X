import os
import pathlib
import re

import numpy as np
from robosuite.models.objects import MujocoXMLObject

from libero.libero.envs.base_object import register_object

absolute_path = pathlib.Path(__file__).parent.parent.parent.absolute()


class LiberoXObjects(MujocoXMLObject):
    def __init__(self, name, obj_name, joints=[dict(type="free", damping="0.0005")]):
        super().__init__(
            os.path.join(
                str(absolute_path),
                f"assets/libero_x_objects/{obj_name}/{obj_name}.xml",
            ),
            name=name,
            joints=joints,
            obj_type="all",
            duplicate_collision_geoms=False,
        )
        self.category_name = "_".join(
            re.sub(r"([A-Z])", r" \1", self.__class__.__name__).split()
        ).lower()
        self.rotation = (0, 0)
        self.rotation_axis = "x"
        self.object_properties = {"vis_site_names": {}}


@register_object
class PurpleBook(LiberoXObjects):
    def __init__(
        self,
        name="purple_book",
        obj_name="purple_book",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class CyanGridBook(LiberoXObjects):
    def __init__(
        self,
        name="cyan_grid_book",
        obj_name="cyan_grid_book",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class TealWavyBook(LiberoXObjects):
    def __init__(
        self,
        name="teal_wavy_book",
        obj_name="teal_wavy_book",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class NavySpeckleBook(LiberoXObjects):
    def __init__(
        self,
        name="navy_speckle_book",
        obj_name="navy_speckle_book",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class YellowGreenStripedBook(LiberoXObjects):
    def __init__(
        self,
        name="yellow_green_striped_book",
        obj_name="yellow_green_striped_book",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class PinkWavyBook(LiberoXObjects):
    def __init__(
        self,
        name="pink_wavy_book",
        obj_name="pink_wavy_book",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class BrownGridBook(LiberoXObjects):
    def __init__(
        self,
        name="brown_grid_book",
        obj_name="brown_grid_book",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class WhiteSpeckleBook(LiberoXObjects):
    def __init__(
        self,
        name="white_speckle_book",
        obj_name="white_speckle_book",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class OrangeBowl(LiberoXObjects):
    def __init__(
        self,
        name="orange_bowl",
        obj_name="orange_bowl",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class CyanBowl(LiberoXObjects):
    def __init__(
        self,
        name="cyan_bowl",
        obj_name="cyan_bowl",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class TealBowl(LiberoXObjects):
    def __init__(
        self,
        name="teal_bowl",
        obj_name="teal_bowl",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class PinkBowl(LiberoXObjects):
    def __init__(
        self,
        name="pink_bowl",
        obj_name="pink_bowl",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class BlackBookInterferenceDarkGreySmall(LiberoXObjects):
    def __init__(
        self,
        name="black_book_interference_dark_grey_small",
        obj_name="black_book_interference_dark_grey_small",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class BlackBookInterferenceDarkGrey(LiberoXObjects):
    def __init__(
        self,
        name="black_book_interference_dark_grey",
        obj_name="black_book_interference_dark_grey",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class GreenBookInterferenceLightGreenSmall(LiberoXObjects):
    def __init__(
        self,
        name="green_book_interference_light_green_small",
        obj_name="green_book_interference_light_green_small",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class GreenBookInterferenceLightGreen(LiberoXObjects):
    def __init__(
        self,
        name="green_book_interference_light_green",
        obj_name="green_book_interference_light_green",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class OrangeBookInterferenceDarkOrangeSmall(LiberoXObjects):
    def __init__(
        self,
        name="orange_book_interference_dark_orange_small",
        obj_name="orange_book_interference_dark_orange_small",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class OrangeBookInterferenceDarkOrange(LiberoXObjects):
    def __init__(
        self,
        name="orange_book_interference_dark_orange",
        obj_name="orange_book_interference_dark_orange",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class RedBookInterferenceLightRedSmall(LiberoXObjects):
    def __init__(
        self,
        name="red_book_interference_light_red_small",
        obj_name="red_book_interference_light_red_small",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class RedBookInterferenceLightRed(LiberoXObjects):
    def __init__(
        self,
        name="red_book_interference_light_red",
        obj_name="red_book_interference_light_red",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class StripedBookInterferenceDarkStripesSmall(LiberoXObjects):
    def __init__(
        self,
        name="striped_book_interference_dark_stripes_small",
        obj_name="striped_book_interference_dark_stripes_small",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class StripedBookInterferenceDarkStripes(LiberoXObjects):
    def __init__(
        self,
        name="striped_book_interference_dark_stripes",
        obj_name="striped_book_interference_dark_stripes",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class YellowBookInterferenceLightYellowSmall(LiberoXObjects):
    def __init__(
        self,
        name="yellow_book_interference_light_yellow_small",
        obj_name="yellow_book_interference_light_yellow_small",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class YellowBookInterferenceLightYellow(LiberoXObjects):
    def __init__(
        self,
        name="yellow_book_interference_light_yellow",
        obj_name="yellow_book_interference_light_yellow",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = (-np.pi / 2, -np.pi / 4)


@register_object
class AkitaBlueBowlInterferenceDarkBlueLarge(LiberoXObjects):
    def __init__(
        self,
        name="akita_blue_bowl_interference_dark_blue_large",
        obj_name="akita_blue_bowl_interference_dark_blue_large",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class AkitaGreenBowlInterferenceLightGreenSmall(LiberoXObjects):
    def __init__(
        self,
        name="akita_green_bowl_interference_light_green_small",
        obj_name="akita_green_bowl_interference_light_green_small",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class AkitaPurpleBowlInterferenceDarkPurpleSmall(LiberoXObjects):
    def __init__(
        self,
        name="akita_purple_bowl_interference_dark_purple_small",
        obj_name="akita_purple_bowl_interference_dark_purple_small",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class AkitaRedBowlInterferenceLightRedLarge(LiberoXObjects):
    def __init__(
        self,
        name="akita_red_bowl_interference_light_red_large",
        obj_name="akita_red_bowl_interference_light_red_large",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class AkitaYellowBowlInterferenceDarkYellowSmall(LiberoXObjects):
    def __init__(
        self,
        name="akita_yellow_bowl_interference_dark_yellow_small",
        obj_name="akita_yellow_bowl_interference_dark_yellow_small",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class AkitaBlackBowlInterferenceLightGreyLarge(LiberoXObjects):
    def __init__(
        self,
        name="akita_black_bowl_interference_light_grey_large",
        obj_name="akita_black_bowl_interference_light_grey_large",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class RedBowlInterferenceDarkRedSmall(LiberoXObjects):
    def __init__(
        self,
        name="red_bowl_interference_dark_red_small",
        obj_name="red_bowl_interference_dark_red_small",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None


@register_object
class WhiteBowlInterferenceOffWhiteLarge(LiberoXObjects):
    def __init__(
        self,
        name="white_bowl_interference_off_white_large",
        obj_name="white_bowl_interference_off_white_large",
        joints=[dict(type="free", damping="0.0005")],
    ):
        super().__init__(name, obj_name, joints)
        self.rotation = {
            "x": (-np.pi / 2, -np.pi / 2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None
