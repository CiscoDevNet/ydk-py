""" Cisco_IOS_XE_ospf 

Cisco XE Native Open Shortest Path First (OSPF) Yang model.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class RedistOspfExternalType(Enum):
    """
    RedistOspfExternalType

    .. data:: Y_1 = 0

    .. data:: Y_2 = 1

    """

    Y_1 = Enum.YLeaf(0, "1")

    Y_2 = Enum.YLeaf(1, "2")



