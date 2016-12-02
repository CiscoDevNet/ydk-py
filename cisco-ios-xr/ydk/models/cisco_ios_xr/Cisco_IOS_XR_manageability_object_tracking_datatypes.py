""" Cisco_IOS_XR_manageability_object_tracking_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class ObjectTrackingBooleanSignEnum(Enum):
    """
    ObjectTrackingBooleanSignEnum

    Object tracking boolean sign

    .. data:: without_not = 0

    	Object without not

    .. data:: with_not = 1

    	Object with not

    """

    without_not = 0

    with_not = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_datatypes as meta
        return meta._meta_table['ObjectTrackingBooleanSignEnum']



