""" Cisco_IOS_XR_segment_routing_srv6_datatypes 

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



class Srv6EncapsulationHopLimitOption(Enum):
    """
    Srv6EncapsulationHopLimitOption (Enum Class)

    Srv6 encapsulation hop limit option

    .. data:: count = 1

    	Set Value

    """

    count = Enum.YLeaf(1, "count")



