""" Cisco_IOS_XR_wanphy_ui_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR wanphy\-ui package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class WanphyLanModeEnum(Enum):
    """
    WanphyLanModeEnum

    Wanphy lan mode

    .. data:: on = 1

    	LanMode

    """

    on = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wanphy_ui_cfg as meta
        return meta._meta_table['WanphyLanModeEnum']


class WanphyWanModeEnum(Enum):
    """
    WanphyWanModeEnum

    Wanphy wan mode

    .. data:: on = 1

    	WAN Mode

    """

    on = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wanphy_ui_cfg as meta
        return meta._meta_table['WanphyWanModeEnum']



