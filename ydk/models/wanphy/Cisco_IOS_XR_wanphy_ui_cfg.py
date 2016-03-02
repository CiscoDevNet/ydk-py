""" Cisco_IOS_XR_wanphy_ui_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR wanphy\-ui package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class WanphyLanMode_Enum(Enum):
    """
    WanphyLanMode_Enum

    Wanphy lan mode

    """

    """

    LanMode

    """
    ON = 1


    @staticmethod
    def _meta_info():
        from ydk.models.wanphy._meta import _Cisco_IOS_XR_wanphy_ui_cfg as meta
        return meta._meta_table['WanphyLanMode_Enum']


class WanphyWanMode_Enum(Enum):
    """
    WanphyWanMode_Enum

    Wanphy wan mode

    """

    """

    WAN Mode

    """
    ON = 1


    @staticmethod
    def _meta_info():
        from ydk.models.wanphy._meta import _Cisco_IOS_XR_wanphy_ui_cfg as meta
        return meta._meta_table['WanphyWanMode_Enum']



