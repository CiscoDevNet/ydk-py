""" Cisco_IOS_XR_manageability_object_tracking_datatypes 

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



class ObjectTrackingBooleanSign(Enum):
    """
    ObjectTrackingBooleanSign (Enum Class)

    Object tracking boolean sign

    .. data:: without_not = 0

    	Object without not

    .. data:: with_not = 1

    	Object with not

    """

    without_not = Enum.YLeaf(0, "without-not")

    with_not = Enum.YLeaf(1, "with-not")



