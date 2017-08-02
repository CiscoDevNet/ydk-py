""" Cisco_IOS_XE_utd 

Cisco XE Native Unified Threat Defense (UTD) Yang model.
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SyslogLevelType(Enum):
    """
    SyslogLevelType

    .. data:: alert = 0

    .. data:: crit = 1

    .. data:: debug = 2

    .. data:: emerg = 3

    .. data:: err = 4

    .. data:: info = 5

    .. data:: notice = 6

    .. data:: warning = 7

    """

    alert = Enum.YLeaf(0, "alert")

    crit = Enum.YLeaf(1, "crit")

    debug = Enum.YLeaf(2, "debug")

    emerg = Enum.YLeaf(3, "emerg")

    err = Enum.YLeaf(4, "err")

    info = Enum.YLeaf(5, "info")

    notice = Enum.YLeaf(6, "notice")

    warning = Enum.YLeaf(7, "warning")



