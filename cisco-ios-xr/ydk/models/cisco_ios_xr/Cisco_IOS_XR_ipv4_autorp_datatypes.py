""" Cisco_IOS_XR_ipv4_autorp_datatypes 

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



class AutoRpProtocolModeEnum(Enum):
    """
    AutoRpProtocolModeEnum

    Auto rp protocol mode

    .. data:: SPARSE = 0

    	Sparse Mode

    .. data:: BIDIRECTIONAL = 1

    	Bidirectional Mode

    """

    SPARSE = 0

    BIDIRECTIONAL = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_datatypes as meta
        return meta._meta_table['AutoRpProtocolModeEnum']



