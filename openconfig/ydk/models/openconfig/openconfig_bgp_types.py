""" openconfig_bgp_types 

This module contains general data definitions for use in BGP
policy. It can be imported by modules that make use of BGP
attributes

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AsPathSegmentType(Enum):
    """
    AsPathSegmentType (Enum Class)

    Defines the types of BGP AS path segments.

    .. data:: AS_SEQ = 0

    	Ordered set of autonomous systems that a route in

    	the UPDATE message has traversed

    .. data:: AS_SET = 1

    	Unordered set of autonomous systems that a route in

    	the UPDATE message has traversed

    .. data:: AS_CONFED_SEQUENCE = 2

    	Ordered set of Member Autonomous

    	Systems in the local confederation that the UPDATE message

    	has traversed

    .. data:: AS_CONFED_SET = 3

    	Unordered set of Member Autonomous Systems

    	in the local confederation that the UPDATE message has

    	traversed

    """

    AS_SEQ = Enum.YLeaf(0, "AS_SEQ")

    AS_SET = Enum.YLeaf(1, "AS_SET")

    AS_CONFED_SEQUENCE = Enum.YLeaf(2, "AS_CONFED_SEQUENCE")

    AS_CONFED_SET = Enum.YLeaf(3, "AS_CONFED_SET")


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

    	Send only standard communities

    .. data:: EXTENDED = 1

    	Send only extended communities

    .. data:: BOTH = 2

    	Send both standard and extended communities

    .. data:: NONE = 3

    	Do not send any community attribute

    """

    STANDARD = Enum.YLeaf(0, "STANDARD")

    EXTENDED = Enum.YLeaf(1, "EXTENDED")

    BOTH = Enum.YLeaf(2, "BOTH")

    NONE = Enum.YLeaf(3, "NONE")


class PeerType(Enum):
    """
    PeerType (Enum Class)

    Labels a peer or peer group as explicitly internal or

    external

    .. data:: INTERNAL = 0

    	Internal (iBGP) peer

    .. data:: EXTERNAL = 1

    	External (eBGP) peer

    """

    INTERNAL = Enum.YLeaf(0, "INTERNAL")

    EXTERNAL = Enum.YLeaf(1, "EXTERNAL")



class BGPCAPABILITY(Identity):
    """
    Base identity for a BGP capability
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:BGP_CAPABILITY"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(BGPCAPABILITY, self).__init__(ns, pref, tag)



class AFISAFITYPE(Identity):
    """
    Base identity type for AFI,SAFI tuples for BGP\-4
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:AFI_SAFI_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AFISAFITYPE, self).__init__(ns, pref, tag)



class BGPWELLKNOWNSTDCOMMUNITY(Identity):
    """
    Reserved communities within the standard community space
    defined by RFC1997. These communities must fall within the
    range 0x00000000 to 0xFFFFFFFF
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:BGP_WELL_KNOWN_STD_COMMUNITY"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(BGPWELLKNOWNSTDCOMMUNITY, self).__init__(ns, pref, tag)



class REMOVEPRIVATEASOPTION(Identity):
    """
    Base identity for options for removing private autonomous
    system numbers from the AS\_PATH attribute
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:REMOVE_PRIVATE_AS_OPTION"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(REMOVEPRIVATEASOPTION, self).__init__(ns, pref, tag)



class MPBGP(BGPCAPABILITY):
    """
    Multi\-protocol extensions to BGP
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:MPBGP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MPBGP, self).__init__(ns, pref, tag)



class ROUTEREFRESH(BGPCAPABILITY):
    """
    The BGP route\-refresh functionality
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:ROUTE_REFRESH"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ROUTEREFRESH, self).__init__(ns, pref, tag)



class ASN32(BGPCAPABILITY):
    """
    4\-byte (32\-bit) AS number functionality
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:ASN32"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ASN32, self).__init__(ns, pref, tag)



class GRACEFULRESTART(BGPCAPABILITY):
    """
    Graceful restart functionality
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:GRACEFUL_RESTART"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(GRACEFULRESTART, self).__init__(ns, pref, tag)



class ADDPATHS(BGPCAPABILITY):
    """
    BGP add\-paths
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:ADD_PATHS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ADDPATHS, self).__init__(ns, pref, tag)



class IPV4UNICAST(AFISAFITYPE):
    """
    IPv4 unicast (AFI,SAFI = 1,1)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:IPV4_UNICAST"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IPV4UNICAST, self).__init__(ns, pref, tag)



class IPV6UNICAST(AFISAFITYPE):
    """
    IPv6 unicast (AFI,SAFI = 2,1)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:IPV6_UNICAST"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IPV6UNICAST, self).__init__(ns, pref, tag)



class IPV4LABELEDUNICAST(AFISAFITYPE):
    """
    Labeled IPv4 unicast (AFI,SAFI = 1,4)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:IPV4_LABELED_UNICAST"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IPV4LABELEDUNICAST, self).__init__(ns, pref, tag)



class IPV6LABELEDUNICAST(AFISAFITYPE):
    """
    Labeled IPv6 unicast (AFI,SAFI = 2,4)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:IPV6_LABELED_UNICAST"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IPV6LABELEDUNICAST, self).__init__(ns, pref, tag)



class L3VPNIPV4UNICAST(AFISAFITYPE):
    """
    Unicast IPv4 MPLS L3VPN (AFI,SAFI = 1,128)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:L3VPN_IPV4_UNICAST"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(L3VPNIPV4UNICAST, self).__init__(ns, pref, tag)



class L3VPNIPV6UNICAST(AFISAFITYPE):
    """
    Unicast IPv6 MPLS L3VPN (AFI,SAFI = 2,128)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:L3VPN_IPV6_UNICAST"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(L3VPNIPV6UNICAST, self).__init__(ns, pref, tag)



class L3VPNIPV4MULTICAST(AFISAFITYPE):
    """
    Multicast IPv4 MPLS L3VPN (AFI,SAFI = 1,129)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:L3VPN_IPV4_MULTICAST"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(L3VPNIPV4MULTICAST, self).__init__(ns, pref, tag)



class L3VPNIPV6MULTICAST(AFISAFITYPE):
    """
    Multicast IPv6 MPLS L3VPN (AFI,SAFI = 2,129)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:L3VPN_IPV6_MULTICAST"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(L3VPNIPV6MULTICAST, self).__init__(ns, pref, tag)



class L2VPNVPLS(AFISAFITYPE):
    """
    BGP\-signalled VPLS (AFI,SAFI = 25,65)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:L2VPN_VPLS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(L2VPNVPLS, self).__init__(ns, pref, tag)



class L2VPNEVPN(AFISAFITYPE):
    """
    BGP MPLS Based Ethernet VPN (AFI,SAFI = 25,70)
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:L2VPN_EVPN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(L2VPNEVPN, self).__init__(ns, pref, tag)



class NOEXPORT(BGPWELLKNOWNSTDCOMMUNITY):
    """
    Do not export NLRI received carrying this community outside
    the bounds of this autonomous system, or this confederation if
    the local autonomous system is a confederation member AS. This
    community has a value of 0xFFFFFF01.
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:NO_EXPORT"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(NOEXPORT, self).__init__(ns, pref, tag)



class NOADVERTISE(BGPWELLKNOWNSTDCOMMUNITY):
    """
    All NLRI received carrying this community must not be
    advertised to other BGP peers. This community has a value of
    0xFFFFFF02.
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:NO_ADVERTISE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(NOADVERTISE, self).__init__(ns, pref, tag)



class NOEXPORTSUBCONFED(BGPWELLKNOWNSTDCOMMUNITY):
    """
    All NLRI received carrying this community must not be
    advertised to external BGP peers \- including over confederation
    sub\-AS boundaries. This community has a value of 0xFFFFFF03.
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:NO_EXPORT_SUBCONFED"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(NOEXPORTSUBCONFED, self).__init__(ns, pref, tag)



class NOPEER(BGPWELLKNOWNSTDCOMMUNITY):
    """
    An autonomous system receiving NLRI tagged with this community
    is advised not to readvertise the NLRI to external bi\-lateral
    peer autonomous systems. An AS may also filter received NLRI
    from bilateral peer sessions when they are tagged with this
    community value
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:NOPEER"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(NOPEER, self).__init__(ns, pref, tag)



class PRIVATEASREMOVEALL(REMOVEPRIVATEASOPTION):
    """
    Strip all private autonmous system numbers from the AS\_PATH.
    This action is performed regardless of the other content of the
    AS\_PATH attribute, and for all instances of private AS numbers
    within that attribute.
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:PRIVATE_AS_REMOVE_ALL"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PRIVATEASREMOVEALL, self).__init__(ns, pref, tag)



class PRIVATEASREPLACEALL(REMOVEPRIVATEASOPTION):
    """
    Replace all instances of private autonomous system numbers in
    the AS\_PATH with the local BGP speaker's autonomous system
    number. This action is performed regardless of the other
    content of the AS\_PATH attribute, and for all instances of
    private AS number within that attribute.
    
    

    """

    _prefix = 'oc-bgp-types'
    _revision = '2017-02-02'

    def __init__(self, ns="http://openconfig.net/yang/bgp-types", pref="openconfig-bgp-types", tag="openconfig-bgp-types:PRIVATE_AS_REPLACE_ALL"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PRIVATEASREPLACEALL, self).__init__(ns, pref, tag)



