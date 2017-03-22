""" openconfig_if_ip 

Model for managing IP interfaces.
This model reuses most of the IETF YANG model for IP management
described by RFC 7277.  The primary differences are in the
structure of configuration and state data.

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

    OTHER = 0

    STATIC = 1

    DHCP = 2

    LINK_LAYER = 3

    RANDOM = 4


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ip as meta
        return meta._meta_table['IpAddressOriginEnum']


class NeighborOriginEnum(Enum):
    """
    NeighborOriginEnum

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

    OTHER = 0

    STATIC = 1

    DYNAMIC = 2


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_ip as meta
        return meta._meta_table['NeighborOriginEnum']



