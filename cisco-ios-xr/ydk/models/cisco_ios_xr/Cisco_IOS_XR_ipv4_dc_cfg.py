""" Cisco_IOS_XR_ipv4_dc_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-dc package configuration.

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



class Opt61Sub(Enum):
    """
    Opt61Sub (Enum Class)

    Opt61 sub

    .. data:: ascii = 1

    	ascii

    .. data:: sn_chassis = 3

    	sn chassis

    """

    ascii = Enum.YLeaf(1, "ascii")

    sn_chassis = Enum.YLeaf(3, "sn-chassis")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dc_cfg as meta
        return meta._meta_table['Opt61Sub']


class Option60(Enum):
    """
    Option60 (Enum Class)

    Option60

    .. data:: option60 = 60

    	OPTION60

    """

    option60 = Enum.YLeaf(60, "option60")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dc_cfg as meta
        return meta._meta_table['Option60']


class Option61(Enum):
    """
    Option61 (Enum Class)

    Option61

    .. data:: option61 = 61

    	OPTION61

    """

    option61 = Enum.YLeaf(61, "option61")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dc_cfg as meta
        return meta._meta_table['Option61']


class Option77(Enum):
    """
    Option77 (Enum Class)

    Option77

    .. data:: option77 = 77

    	OPTION77

    """

    option77 = Enum.YLeaf(77, "option77")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dc_cfg as meta
        return meta._meta_table['Option77']



