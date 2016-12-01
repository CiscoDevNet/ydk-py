""" Cisco_IOS_XR_mpls_ldp_oper_datatypes 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-ldp\-oper\-data package operational data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class MplsLdpOperAfNameEnum(Enum):
    """
    MplsLdpOperAfNameEnum

    Mpls ldp oper af name

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    """

    ipv4 = 1

    ipv6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_oper_datatypes as meta
        return meta._meta_table['MplsLdpOperAfNameEnum']



