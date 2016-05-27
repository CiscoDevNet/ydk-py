""" Cisco_IOS_XR_snmp_ifmib_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR snmp\-ifmib package operational data.

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-oper
module with state data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class LinkUpDownStatusEnum(Enum):
    """
    LinkUpDownStatusEnum

    Link up down status

    .. data:: ENABLED = 1

    	LinkUpDown notification is enabled

    .. data:: DISABLED = 2

    	LinkUpDown notification is disabled

    """

    ENABLED = 1

    DISABLED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.snmp._meta import _Cisco_IOS_XR_snmp_ifmib_oper as meta
        return meta._meta_table['LinkUpDownStatusEnum']



