""" Cisco_IOS_XR_wanphy_ui_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR wanphy\-ui package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class WanphyLanMode(Enum):
    """
    WanphyLanMode

    Wanphy lan mode

    .. data:: on = 1

    	LanMode

    """

    on = Enum.YLeaf(1, "on")


class WanphyWanMode(Enum):
    """
    WanphyWanMode

    Wanphy wan mode

    .. data:: on = 1

    	WAN Mode

    """

    on = Enum.YLeaf(1, "on")



