""" ietf_ip 

This module contains a collection of YANG definitions for
configuring IP implementations.
Copyright (c) 2014 IETF Trust and the persons identified as
authors of the code.  All rights reserved.
Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).
This version of this YANG module is part of RFC 7277; see
the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class IpAddressOriginEnum(Enum):
    """
    IpAddressOriginEnum

    The origin of an address.

    .. data:: other = 0

    	None of the following.

    .. data:: static = 1

    	Indicates that the address has been statically

    	configured - for example, using NETCONF or a Command Line

    	Interface.

    .. data:: dhcp = 2

    	Indicates an address that has been assigned to this

    	system by a DHCP server.

    .. data:: link_layer = 3

    	Indicates an address created by IPv6 stateless

    	autoconfiguration that embeds a link-layer address in its

    	interface identifier.

    .. data:: random = 4

    	Indicates an address chosen by the system at

    	random, e.g., an IPv4 address within 169.254/16, an

    	RFC 4941 temporary address, or an RFC 7217 semantically

    	opaque address.

    """

    other = 0

    static = 1

    dhcp = 2

    link_layer = 3

    random = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ip as meta
        return meta._meta_table['IpAddressOriginEnum']


class NeighborOriginEnum(Enum):
    """
    NeighborOriginEnum

    The origin of a neighbor entry.

    .. data:: other = 0

    	None of the following.

    .. data:: static = 1

    	Indicates that the mapping has been statically

    	configured - for example, using NETCONF or a Command Line

    	Interface.

    .. data:: dynamic = 2

    	Indicates that the mapping has been dynamically resolved

    	using, e.g., IPv4 ARP or the IPv6 Neighbor Discovery

    	protocol.

    """

    other = 0

    static = 1

    dynamic = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ip as meta
        return meta._meta_table['NeighborOriginEnum']



