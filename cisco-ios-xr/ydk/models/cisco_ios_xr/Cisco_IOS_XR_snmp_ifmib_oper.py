""" Cisco_IOS_XR_snmp_ifmib_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR snmp\-ifmib package operational data.

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-oper
module with state data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class LinkUpDownStatusEnum(Enum):
    """
    LinkUpDownStatusEnum

    Link up down status

    .. data:: enabled = 1

    	LinkUpDown notification is enabled

    .. data:: disabled = 2

    	LinkUpDown notification is disabled

    """

    enabled = 1

    disabled = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_ifmib_oper as meta
        return meta._meta_table['LinkUpDownStatusEnum']



