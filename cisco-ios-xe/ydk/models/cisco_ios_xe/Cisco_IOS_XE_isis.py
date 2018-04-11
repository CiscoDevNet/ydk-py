""" Cisco_IOS_XE_isis 

Cisco XE Native Intermediate System\-to\-Intermediate System (IS\-IS) Yang model.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AuthenticationLevelType(Enum):
    """
    AuthenticationLevelType (Enum Class)

    .. data:: level_1 = 0

    .. data:: level_2 = 1

    """

    level_1 = Enum.YLeaf(0, "level-1")

    level_2 = Enum.YLeaf(1, "level-2")


class IsisLevelType(Enum):
    """
    IsisLevelType (Enum Class)

    .. data:: level_1 = 0

    .. data:: level_1_2 = 1

    .. data:: level_2 = 2

    """

    level_1 = Enum.YLeaf(0, "level-1")

    level_1_2 = Enum.YLeaf(1, "level-1-2")

    level_2 = Enum.YLeaf(2, "level-2")


class IsisRoutesLevelType(Enum):
    """
    IsisRoutesLevelType (Enum Class)

    .. data:: level_1 = 0

    .. data:: level_1_2 = 1

    .. data:: level_2 = 2

    """

    level_1 = Enum.YLeaf(0, "level-1")

    level_1_2 = Enum.YLeaf(1, "level-1-2")

    level_2 = Enum.YLeaf(2, "level-2")



