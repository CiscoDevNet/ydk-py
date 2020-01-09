""" Cisco_IOS_XR_atm_vcm_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR atm\-vcm package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-l2vpn\-cfg
modules with configuration data.

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



class AtmPvcTestMode(Enum):
    """
    AtmPvcTestMode (Enum Class)

    Atm pvc test mode

    .. data:: loop = 1

    	Loop mode applicable to L2/L3 PVC

    .. data:: reserved = 2

    	Reserved mode applicable to L2 PVC

    """

    loop = Enum.YLeaf(1, "loop")

    reserved = Enum.YLeaf(2, "reserved")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_cfg as meta
        return meta._meta_table['AtmPvcTestMode']


class AtmPvpTestMode(Enum):
    """
    AtmPvpTestMode (Enum Class)

    Atm pvp test mode

    .. data:: loop = 1

    	Loop mode

    """

    loop = Enum.YLeaf(1, "loop")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_cfg as meta
        return meta._meta_table['AtmPvpTestMode']


class AtmVpiBitsMode(Enum):
    """
    AtmVpiBitsMode (Enum Class)

    Atm vpi bits mode

    .. data:: twelve = 12

    	12-bits VPI cell format

    """

    twelve = Enum.YLeaf(12, "twelve")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_cfg as meta
        return meta._meta_table['AtmVpiBitsMode']



