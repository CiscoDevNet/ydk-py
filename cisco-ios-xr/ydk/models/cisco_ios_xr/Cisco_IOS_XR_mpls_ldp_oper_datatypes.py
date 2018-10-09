""" Cisco_IOS_XR_mpls_ldp_oper_datatypes 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-ldp\-oper\-data package operational data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MplsLdpOperAfName(Enum):
    """
    MplsLdpOperAfName (Enum Class)

    Mpls ldp oper af name

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    .. data:: all = 65535

    	All

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")

    all = Enum.YLeaf(65535, "all")



