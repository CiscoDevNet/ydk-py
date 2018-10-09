""" Cisco_IOS_XE_rip 

Cisco XE Native Routing Information Protocol (RIP) Yang model.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class OffsetListInOutType(Enum):
    """
    OffsetListInOutType (Enum Class)

    .. data:: in_ = 0

    .. data:: out = 1

    """

    in_ = Enum.YLeaf(0, "in")

    out = Enum.YLeaf(1, "out")



