""" openconfig_if_ip 

This model defines data for managing configuration and
operational state on IP (IPv4 and IPv6) interfaces.

This model reuses data items defined in the IETF YANG model for
interfaces described by RFC 7277 with an alternate structure
(particularly for operational state data) and with
additional configuration items.

Portions of this code were derived from IETF RFC 7277.
Please reproduce this note if possible.

IETF code is subject to the following copyright and license\:
Copyright (c) IETF Trust and the persons identified as authors of
the code.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, is permitted pursuant to, and subject to the license
terms contained in, the Simplified BSD License set forth in
Section 4.c of the IETF Trust's Legal Provisions Relating
to IETF Documents (http\://trustee.ietf.org/license\-info).

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IpAddressOrigin(Enum):
    """
    IpAddressOrigin (Enum Class)

    The origin of an address.

    .. data:: OTHER = 0

    	None of the following.

    .. data:: STATIC = 1

    	Indicates that the address has been statically

    	configured - for example, using NETCONF or a Command Line

    	Interface.

    .. data:: DHCP = 2

    	Indicates an address that has been assigned to this

    	system by a DHCP server.

    .. data:: LINK_LAYER = 3

    	Indicates an address created by IPv6 stateless

    	autoconfiguration that embeds a link-layer address in its

    	interface identifier.

    .. data:: RANDOM = 4

    	Indicates an address chosen by the system at

    	random, e.g., an IPv4 address within 169.254/16, an

    	RFC 4941 temporary address, or an RFC 7217 semantically

    	opaque address.

    """

    OTHER = Enum.YLeaf(0, "OTHER")

    STATIC = Enum.YLeaf(1, "STATIC")

    DHCP = Enum.YLeaf(2, "DHCP")

    LINK_LAYER = Enum.YLeaf(3, "LINK_LAYER")

    RANDOM = Enum.YLeaf(4, "RANDOM")


class NeighborOrigin(Enum):
    """
    NeighborOrigin (Enum Class)

    The origin of a neighbor entry.

    .. data:: OTHER = 0

    	None of the following.

    .. data:: STATIC = 1

    	Indicates that the mapping has been statically

    	configured - for example, using NETCONF or a Command Line

    	Interface.

    .. data:: DYNAMIC = 2

    	Indicates that the mapping has been dynamically resolved

    	using, e.g., IPv4 ARP or the IPv6 Neighbor Discovery

    	protocol.

    """

    OTHER = Enum.YLeaf(0, "OTHER")

    STATIC = Enum.YLeaf(1, "STATIC")

    DYNAMIC = Enum.YLeaf(2, "DYNAMIC")



