""" Cisco_IOS_XR_mpls_ldp_oper_datatypes 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-ldp\-oper\-data package operational data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
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

    .. data:: IPV4 = 1

    	IPv4

    .. data:: IPV6 = 2

    	IPv6

    """

    IPV4 = 1

    IPV6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_ldp_oper_datatypes as meta
        return meta._meta_table['MplsLdpOperAfNameEnum']



