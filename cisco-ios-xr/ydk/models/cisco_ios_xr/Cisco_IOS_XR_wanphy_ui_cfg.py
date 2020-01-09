""" Cisco_IOS_XR_wanphy_ui_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR wanphy\-ui package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class WanphyLanMode(Enum):
    """
    WanphyLanMode (Enum Class)

    Wanphy lan mode

    .. data:: on = 1

    	LanMode

    """

    on = Enum.YLeaf(1, "on")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wanphy_ui_cfg as meta
        return meta._meta_table['WanphyLanMode']


class WanphyWanMode(Enum):
    """
    WanphyWanMode (Enum Class)

    Wanphy wan mode

    .. data:: on = 1

    	WAN Mode

    """

    on = Enum.YLeaf(1, "on")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wanphy_ui_cfg as meta
        return meta._meta_table['WanphyWanMode']



