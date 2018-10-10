""" Cisco_IOS_XR_common_acl_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AclUsageAppIdEnum(Enum):
    """
    AclUsageAppIdEnum (Enum Class)

    Acl usage app id enum

    .. data:: pfilter = 1

    	General Usage Statistics

    .. data:: bgp = 2

    	Usage staistics related to BGP Traffic

    .. data:: ospf = 3

    	Usage staistics related to OSPF Traffic

    """

    pfilter = Enum.YLeaf(1, "pfilter")

    bgp = Enum.YLeaf(2, "bgp")

    ospf = Enum.YLeaf(3, "ospf")



