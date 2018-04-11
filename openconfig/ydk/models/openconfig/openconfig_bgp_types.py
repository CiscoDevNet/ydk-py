""" openconfig_bgp_types 

This module contains general data definitions for use in BGP
policy. It can be imported by modules that make use of BGP
attributes

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BgpOriginAttrType(Enum):
    """
    BgpOriginAttrType (Enum Class)

    Type definition for standard BGP origin attribute

    .. data:: IGP = 0

    	Origin of the NLRI is internal

    .. data:: EGP = 1

    	Origin of the NLRI is EGP

    .. data:: INCOMPLETE = 2

    	Origin of the NLRI is neither IGP or EGP

    """

    IGP = Enum.YLeaf(0, "IGP")

    EGP = Enum.YLeaf(1, "EGP")

    INCOMPLETE = Enum.YLeaf(2, "INCOMPLETE")


class BgpSessionDirection(Enum):
    """
    BgpSessionDirection (Enum Class)

    Type to describe the direction of NLRI transmission

    .. data:: INBOUND = 0

    	Refers to all NLRI received from the BGP peer

    .. data:: OUTBOUND = 1

    	Refers to all NLRI advertised to the BGP peer

    """

    INBOUND = Enum.YLeaf(0, "INBOUND")

    OUTBOUND = Enum.YLeaf(1, "OUTBOUND")


class CommunityType(Enum):
    """
    CommunityType (Enum Class)

    type describing variations of community attributes\:

    STANDARD\: standard BGP community [rfc1997]

    EXTENDED\: extended BGP community [rfc4360]

    BOTH\: both standard and extended community

    .. data:: STANDARD = 0

    	send only standard communities

    .. data:: EXTENDED = 1

    	send only extended communities

    .. data:: BOTH = 2

    	send both standard and extended communities

    .. data:: NONE = 3

    	do not send any community attribute

    """

    STANDARD = Enum.YLeaf(0, "STANDARD")

    EXTENDED = Enum.YLeaf(1, "EXTENDED")

    BOTH = Enum.YLeaf(2, "BOTH")

    NONE = Enum.YLeaf(3, "NONE")


class PeerType(Enum):
    """
    PeerType (Enum Class)

    labels a peer or peer group as explicitly internal or

    external

    .. data:: INTERNAL = 0

    	internal (iBGP) peer

    .. data:: EXTERNAL = 1

    	external (eBGP) peer

    """

    INTERNAL = Enum.YLeaf(0, "INTERNAL")

    EXTERNAL = Enum.YLeaf(1, "EXTERNAL")



class BGPCAPABILITY(Identity):
    """
    Base identity for a BGP capability
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(BGPCAPABILITY, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:BGP_CAPABILITY")


class AFISAFITYPE(Identity):
    """
    Base identity type for AFI,SAFI tuples for BGP\-4
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(AFISAFITYPE, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:AFI_SAFI_TYPE")


class BGPWELLKNOWNSTDCOMMUNITY(Identity):
    """
    Reserved communities within the standard community space
    defined by RFC1997. These communities must fall within the
    range 0x00000000 to 0xFFFFFFFF
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(BGPWELLKNOWNSTDCOMMUNITY, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:BGP_WELL_KNOWN_STD_COMMUNITY")


class REMOVEPRIVATEASOPTION(Identity):
    """
    Base identity for options for removing private autonomous
    system numbers from the AS\_PATH attribute
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(REMOVEPRIVATEASOPTION, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:REMOVE_PRIVATE_AS_OPTION")


class MPBGP(Identity):
    """
    Multi\-protocol extensions to BGP
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(MPBGP, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:MPBGP")


class ROUTEREFRESH(Identity):
    """
    The BGP route\-refresh functionality
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(ROUTEREFRESH, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:ROUTE_REFRESH")


class ASN32(Identity):
    """
    4\-byte (32\-bit) AS number functionality
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(ASN32, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:ASN32")


class GRACEFULRESTART(Identity):
    """
    Graceful restart functionality
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(GRACEFULRESTART, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:GRACEFUL_RESTART")


class ADDPATHS(Identity):
    """
    BGP add\-paths
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(ADDPATHS, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:ADD_PATHS")


class IPV4UNICAST(Identity):
    """
    IPv4 unicast (AFI,SAFI = 1,1)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(IPV4UNICAST, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:IPV4_UNICAST")


class IPV6UNICAST(Identity):
    """
    IPv6 unicast (AFI,SAFI = 2,1)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(IPV6UNICAST, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:IPV6_UNICAST")


class IPV4LABELEDUNICAST(Identity):
    """
    Labeled IPv4 unicast (AFI,SAFI = 1,4)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(IPV4LABELEDUNICAST, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:IPV4_LABELED_UNICAST")


class IPV6LABELEDUNICAST(Identity):
    """
    Labeled IPv6 unicast (AFI,SAFI = 2,4)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(IPV6LABELEDUNICAST, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:IPV6_LABELED_UNICAST")


class L3VPNIPV4UNICAST(Identity):
    """
    Unicast IPv4 MPLS L3VPN (AFI,SAFI = 1,128)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(L3VPNIPV4UNICAST, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:L3VPN_IPV4_UNICAST")


class L3VPNIPV6UNICAST(Identity):
    """
    Unicast IPv6 MPLS L3VPN (AFI,SAFI = 2,128)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(L3VPNIPV6UNICAST, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:L3VPN_IPV6_UNICAST")


class L3VPNIPV4MULTICAST(Identity):
    """
    Multicast IPv4 MPLS L3VPN (AFI,SAFI = 1,129)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(L3VPNIPV4MULTICAST, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:L3VPN_IPV4_MULTICAST")


class L3VPNIPV6MULTICAST(Identity):
    """
    Multicast IPv6 MPLS L3VPN (AFI,SAFI = 2,129)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(L3VPNIPV6MULTICAST, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:L3VPN_IPV6_MULTICAST")


class L2VPNVPLS(Identity):
    """
    BGP\-signalled VPLS (AFI,SAFI = 25,65)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(L2VPNVPLS, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:L2VPN_VPLS")


class L2VPNEVPN(Identity):
    """
    BGP MPLS Based Ethernet VPN (AFI,SAFI = 25,70)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(L2VPNEVPN, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:L2VPN_EVPN")


class NOEXPORT(Identity):
    """
    Do not export NLRI received carrying this community outside
    the bounds of this autonomous system, or this confederation if
    the local autonomous system is a confederation member AS. This
    community has a value of 0xFFFFFF01.
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(NOEXPORT, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:NO_EXPORT")


class NOADVERTISE(Identity):
    """
    All NLRI received carrying this community must not be
    advertised to other BGP peers. This community has a value of
    0xFFFFFF02.
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(NOADVERTISE, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:NO_ADVERTISE")


class NOEXPORTSUBCONFED(Identity):
    """
    All NLRI received carrying this community must not be
    advertised to external BGP peers \- including over confederation
    sub\-AS boundaries. This community has a value of 0xFFFFFF03.
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(NOEXPORTSUBCONFED, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:NO_EXPORT_SUBCONFED")


class NOPEER(Identity):
    """
    An autonomous system receiving NLRI tagged with this community
    is advised not to readvertise the NLRI to external bi\-lateral
    peer autonomous systems. An AS may also filter received NLRI
    from bilateral peer sessions when they are tagged with this
    community value
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(NOPEER, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:NOPEER")


class PRIVATEASREMOVEALL(Identity):
    """
    Strip all private autonmous system numbers from the AS\_PATH.
    This action is performed regardless of the other content of the
    AS\_PATH attribute, and for all instances of private AS numbers
    within that attribute.
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(PRIVATEASREMOVEALL, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:PRIVATE_AS_REMOVE_ALL")


class PRIVATEASREPLACEALL(Identity):
    """
    Replace all instances of private autonomous system numbers in
    the AS\_PATH with the local BGP speaker's autonomous system
    number. This action is performed regardless of the other
    content of the AS\_PATH attribute, and for all instances of
    private AS number within that attribute.
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2016-06-21'

    def __init__(self):
        super(PRIVATEASREPLACEALL, self).__init__("http://openconfig.net/yang/bgp-types", "openconfig-bgp-types", "openconfig-bgp-types:PRIVATE_AS_REPLACE_ALL")


