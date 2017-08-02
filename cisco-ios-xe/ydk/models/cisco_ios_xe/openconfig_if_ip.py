""" openconfig_if_ip 

Model for managing IP interfaces.

This model reuses most of the IETF YANG model for IP management
described by RFC 7277.  The primary differences are in the
structure of configuration and state data.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class IpAddressOrigin(Enum):
    """
    IpAddressOrigin

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

    	[adapted from RFC 7277]

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
    NeighborOrigin

    The origin of a neighbor entry.

    .. data:: OTHER = 0

    	None of the following.

    .. data:: STATIC = 1

    	Indicates that the mapping has been statically

    	configured - for example, using NETCONF or a Command Line

    	Interface.

    .. data:: DYNAMIC = 2

    	[adapted from RFC 7277]

    	Indicates that the mapping has been dynamically resolved

    	using, e.g., IPv4 ARP or the IPv6 Neighbor Discovery

    	protocol.

    """

    OTHER = Enum.YLeaf(0, "OTHER")

    STATIC = Enum.YLeaf(1, "STATIC")

    DYNAMIC = Enum.YLeaf(2, "DYNAMIC")



