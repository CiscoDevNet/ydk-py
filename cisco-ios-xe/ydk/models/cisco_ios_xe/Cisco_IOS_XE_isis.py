""" Cisco_IOS_XE_isis 

Cisco XE Native Intermediate System\-to\-Intermediate System (IS\-IS) Yang model.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AuthenticationLevelType(Enum):
    """
    AuthenticationLevelType

    .. data:: level_1 = 0

    .. data:: level_2 = 1

    """

    level_1 = Enum.YLeaf(0, "level-1")

    level_2 = Enum.YLeaf(1, "level-2")


class IsisLevelType(Enum):
    """
    IsisLevelType

    .. data:: level_1 = 0

    .. data:: level_1_2 = 1

    .. data:: level_2 = 2

    """

    level_1 = Enum.YLeaf(0, "level-1")

    level_1_2 = Enum.YLeaf(1, "level-1-2")

    level_2 = Enum.YLeaf(2, "level-2")


class IsisRoutesLevelType(Enum):
    """
    IsisRoutesLevelType

    .. data:: level_1 = 0

    .. data:: level_1_2 = 1

    .. data:: level_2 = 2

    """

    level_1 = Enum.YLeaf(0, "level-1")

    level_1_2 = Enum.YLeaf(1, "level-1-2")

    level_2 = Enum.YLeaf(2, "level-2")



