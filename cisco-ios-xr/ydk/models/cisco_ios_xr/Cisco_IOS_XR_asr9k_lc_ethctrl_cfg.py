""" Cisco_IOS_XR_asr9k_lc_ethctrl_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-lc\-ethctrl package configuration.

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


class EtherCtrlTransportMode(Enum):
    """
    EtherCtrlTransportMode

    Ether ctrl transport mode

    .. data:: wan = 1

    	WAN

    .. data:: otnopu1e = 2

    	OTNOPUle

    .. data:: otnopu2e = 3

    	OTNOPU2e

    """

    wan = Enum.YLeaf(1, "wan")

    otnopu1e = Enum.YLeaf(2, "otnopu1e")

    otnopu2e = Enum.YLeaf(3, "otnopu2e")


class PermitPluggable(Enum):
    """
    PermitPluggable

    Permit pluggable

    .. data:: all = 1

    	ALL types

    """

    all = Enum.YLeaf(1, "all")


class PermitPluggablePid(Enum):
    """
    PermitPluggablePid

    Permit pluggable pid

    .. data:: all = 1

    	ALL PIDs

    """

    all = Enum.YLeaf(1, "all")



