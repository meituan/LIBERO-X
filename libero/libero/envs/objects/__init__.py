import re

from libero.libero.envs.base_object import OBJECTS_DICT, VISUAL_CHANGE_OBJECTS_DICT

from .articulated_objects import *
from .extension_objects import *
from .google_scanned_objects import *
from .hope_objects import *
from .libero_x_objects import *
from .site_object import SiteObject
from .target_zones import *
from .turbosquid_objects import *


def get_object_fn(category_name):
    return OBJECTS_DICT[category_name.lower()]


def get_object_dict():
    return OBJECTS_DICT
