""" Cisco_IOS_XE_mpls 

Cisco XE Native Multiprotocol Label Switching (MPLS) Yang model.
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class LdpDiscoveryAddressTypeEnum(Enum):
    """
    LdpDiscoveryAddressTypeEnum

    .. data:: interface = 0

    """

    interface = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls as meta
        return meta._meta_table['LdpDiscoveryAddressTypeEnum']



