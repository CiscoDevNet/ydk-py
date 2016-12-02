""" Cisco_IOS_XR_aaa_locald_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-locald package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-aaa\-lib\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AaaLocaldTaskClassEnum(Enum):
    """
    AaaLocaldTaskClassEnum

    Aaa locald task class

    .. data:: read = 0

    	Permits read operation for a Task ID

    .. data:: write = 1

    	Permits write operation for a Task ID

    .. data:: execute = 2

    	Permits execute operation for a Task ID

    .. data:: debug = 3

    	Permits debug operation for a Task ID

    """

    read = 0

    write = 1

    execute = 2

    debug = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_cfg as meta
        return meta._meta_table['AaaLocaldTaskClassEnum']



