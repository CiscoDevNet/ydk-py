""" openconfig_bgp_types 

This module contains general data definitions for use in BGP
policy. It can be imported by modules that make use of BGP
attributes

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BgpOriginAttrTypeEnum(Enum):
    """
    BgpOriginAttrTypeEnum

    Type definition for standard BGP origin attribute

    .. data:: IGP = 0

    	Origin of the NLRI is internal

    .. data:: EGP = 1

    	Origin of the NLRI is EGP

    .. data:: INCOMPLETE = 2

    	Origin of the NLRI is neither IGP or EGP

    """

    IGP = 0

    EGP = 1

    INCOMPLETE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['BgpOriginAttrTypeEnum']


class BgpSessionDirectionEnum(Enum):
    """
    BgpSessionDirectionEnum

    Type to describe the direction of NLRI transmission

    .. data:: INBOUND = 0

    	Refers to all NLRI received from the BGP peer

    .. data:: OUTBOUND = 1

    	Refers to all NLRI advertised to the BGP peer

    """

    INBOUND = 0

    OUTBOUND = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['BgpSessionDirectionEnum']


class CommunityTypeEnum(Enum):
    """
    CommunityTypeEnum

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

    STANDARD = 0

    EXTENDED = 1

    BOTH = 2

    NONE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['CommunityTypeEnum']


class PeerTypeEnum(Enum):
    """
    PeerTypeEnum

    labels a peer or peer group as explicitly internal or

    external

    .. data:: INTERNAL = 0

    	internal (iBGP) peer

    .. data:: EXTERNAL = 1

    	external (eBGP) peer

    """

    INTERNAL = 0

    EXTERNAL = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['PeerTypeEnum']


class RemovePrivateAsOptionEnum(Enum):
    """
    RemovePrivateAsOptionEnum

    set of options for configuring how private AS path numbers

    are removed from advertisements

    .. data:: ALL = 0

    	remove all private ASes in the path

    .. data:: REPLACE = 1

    	replace private ASes with local AS

    """

    ALL = 0

    REPLACE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['RemovePrivateAsOptionEnum']



class BgpCapabilityIdentity(object):
    """
    Base identity for a BGP capability
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['BgpCapabilityIdentity']['meta_info']


class AfiSafiTypeIdentity(object):
    """
    Base identity type for AFI,SAFI tuples for BGP\-4
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['AfiSafiTypeIdentity']['meta_info']


class BgpWellKnownStdCommunityIdentity(object):
    """
    Reserved communities within the standard community space
    defined by RFC1997. These communities must fall within the
    range 0x00000000 to 0xFFFFFFFF
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['BgpWellKnownStdCommunityIdentity']['meta_info']


class RouteRefreshIdentity(BgpCapabilityIdentity):
    """
    The BGP route\-refresh functionality
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        BgpCapabilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['RouteRefreshIdentity']['meta_info']


class No_ExportIdentity(BgpWellKnownStdCommunityIdentity):
    """
    Do not export NLRI received carrying this community outside
    the bounds of this autonomous system, or this confederation if
    the local autonomous system is a confederation member AS. This
    community has a value of 0xFFFFFF01.
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        BgpWellKnownStdCommunityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['No_ExportIdentity']['meta_info']


class No_Export_SubconfedIdentity(BgpWellKnownStdCommunityIdentity):
    """
    All NLRI received carrying this community must not be
    advertised to external BGP peers \- including over confederation
    sub\-AS boundaries. This community has a value of 0xFFFFFF03.
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        BgpWellKnownStdCommunityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['No_Export_SubconfedIdentity']['meta_info']


class L3VpnIpv4MulticastIdentity(AfiSafiTypeIdentity):
    """
    Multicast IPv4 MPLS L3VPN (AFI,SAFI = 1,129)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['L3VpnIpv4MulticastIdentity']['meta_info']


class L2VpnVplsIdentity(AfiSafiTypeIdentity):
    """
    BGP\-signalled VPLS (AFI,SAFI = 25,65)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['L2VpnVplsIdentity']['meta_info']


class NopeerIdentity(BgpWellKnownStdCommunityIdentity):
    """
    An autonomous system receiving NLRI tagged with this community
    is advised not to readvertise the NLRI to external bi\-lateral
    peer autonomous systems. An AS may also filter received NLRI
    from bilateral peer sessions when they are tagged with this
    community value
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        BgpWellKnownStdCommunityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['NopeerIdentity']['meta_info']


class Ipv6LabelledUnicastIdentity(AfiSafiTypeIdentity):
    """
    Labelled IPv6 unicast (AFI,SAFI = 2,4)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['Ipv6LabelledUnicastIdentity']['meta_info']


class GracefulRestartIdentity(BgpCapabilityIdentity):
    """
    Graceful restart functionality
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        BgpCapabilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['GracefulRestartIdentity']['meta_info']


class MpbgpIdentity(BgpCapabilityIdentity):
    """
    Multi\-protocol extensions to BGP
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        BgpCapabilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['MpbgpIdentity']['meta_info']


class Ipv4UnicastIdentity(AfiSafiTypeIdentity):
    """
    IPv4 unicast (AFI,SAFI = 1,1)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['Ipv4UnicastIdentity']['meta_info']


class L3VpnIpv6UnicastIdentity(AfiSafiTypeIdentity):
    """
    Unicast IPv6 MPLS L3VPN (AFI,SAFI = 2,128)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['L3VpnIpv6UnicastIdentity']['meta_info']


class Asn32Identity(BgpCapabilityIdentity):
    """
    4\-byte (32\-bit) AS number functionality
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        BgpCapabilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['Asn32Identity']['meta_info']


class L3VpnIpv4UnicastIdentity(AfiSafiTypeIdentity):
    """
    Unicast IPv4 MPLS L3VPN (AFI,SAFI = 1,128)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['L3VpnIpv4UnicastIdentity']['meta_info']


class Ipv4LabelledUnicastIdentity(AfiSafiTypeIdentity):
    """
    Labelled IPv4 unicast (AFI,SAFI = 1,4)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['Ipv4LabelledUnicastIdentity']['meta_info']


class L3VpnIpv6MulticastIdentity(AfiSafiTypeIdentity):
    """
    Multicast IPv6 MPLS L3VPN (AFI,SAFI = 2,129)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['L3VpnIpv6MulticastIdentity']['meta_info']


class No_AdvertiseIdentity(BgpWellKnownStdCommunityIdentity):
    """
    All NLRI received carrying this community must not be
    advertised to other BGP peers. This community has a value of
    0xFFFFFF02.
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        BgpWellKnownStdCommunityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['No_AdvertiseIdentity']['meta_info']


class AddPathsIdentity(BgpCapabilityIdentity):
    """
    BGP add\-paths
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        BgpCapabilityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['AddPathsIdentity']['meta_info']


class Ipv6UnicastIdentity(AfiSafiTypeIdentity):
    """
    IPv6 unicast (AFI,SAFI = 2,1)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['Ipv6UnicastIdentity']['meta_info']


class L2VpnEvpnIdentity(AfiSafiTypeIdentity):
    """
    BGP MPLS Based Ethernet VPN (AFI,SAFI = 25,70)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_types as meta
        return meta._meta_table['L2VpnEvpnIdentity']['meta_info']


