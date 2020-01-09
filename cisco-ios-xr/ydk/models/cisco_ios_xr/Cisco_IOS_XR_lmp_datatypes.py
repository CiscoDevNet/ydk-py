""" Cisco_IOS_XR_lmp_datatypes 

This module contains a collection of generally useful
derived YANG data types.

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



class OlmAddr(Enum):
    """
    OlmAddr (Enum Class)

    Olm addr

    .. data:: ipv4 = 101

    	IPv4 address

    .. data:: ipv6 = 102

    	IPv6 address

    .. data:: unnumbered = 103

    	Unnumbered address

    .. data:: nsap = 104

    	NSAP address

    """

    ipv4 = Enum.YLeaf(101, "ipv4")

    ipv6 = Enum.YLeaf(102, "ipv6")

    unnumbered = Enum.YLeaf(103, "unnumbered")

    nsap = Enum.YLeaf(104, "nsap")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lmp_datatypes as meta
        return meta._meta_table['OlmAddr']


class OlmSwitchingCap(Enum):
    """
    OlmSwitchingCap (Enum Class)

    Olm switching cap

    .. data:: lsc = 150

    	Lambda switch capable

    .. data:: fsc = 200

    	Fiber switch capable

    """

    lsc = Enum.YLeaf(150, "lsc")

    fsc = Enum.YLeaf(200, "fsc")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lmp_datatypes as meta
        return meta._meta_table['OlmSwitchingCap']



