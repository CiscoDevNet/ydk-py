""" Cisco_IOS_XR_snmp_ifmib_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR snmp\-ifmib package operational data.

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-oper
module with state data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class LinkUpDownStatus(Enum):
    """
    LinkUpDownStatus

    Link up down status

    .. data:: enabled = 1

    	LinkUpDown notification is enabled

    .. data:: disabled = 2

    	LinkUpDown notification is disabled

    """

    enabled = Enum.YLeaf(1, "enabled")

    disabled = Enum.YLeaf(2, "disabled")



