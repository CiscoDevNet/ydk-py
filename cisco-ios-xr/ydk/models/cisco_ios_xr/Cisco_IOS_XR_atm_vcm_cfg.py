""" Cisco_IOS_XR_atm_vcm_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR atm\-vcm package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-l2vpn\-cfg
modules with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AtmPvcTestMode(Enum):
    """
    AtmPvcTestMode

    Atm pvc test mode

    .. data:: loop = 1

    	Loop mode applicable to L2/L3 PVC

    .. data:: reserved = 2

    	Reserved mode applicable to L2 PVC

    """

    loop = Enum.YLeaf(1, "loop")

    reserved = Enum.YLeaf(2, "reserved")


class AtmPvpTestMode(Enum):
    """
    AtmPvpTestMode

    Atm pvp test mode

    .. data:: loop = 1

    	Loop mode

    """

    loop = Enum.YLeaf(1, "loop")


class AtmVpiBitsMode(Enum):
    """
    AtmVpiBitsMode

    Atm vpi bits mode

    .. data:: twelve = 12

    	12-bits VPI cell format

    """

    twelve = Enum.YLeaf(12, "twelve")



