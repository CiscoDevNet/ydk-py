""" bgp_types 

This module contains general data definitions for use in BGP
policy. It can be imported by modules that make use of BGP
attributes

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class BgpOriginAttrType_Enum(Enum):
    """
    BgpOriginAttrType_Enum

    Type definition for standard BGP origin attribute

    """

    """

    Origin of the NLRI is internal

    """
    IGP = 0

    """

    Origin of the NLRI is EGP

    """
    EGP = 1

    """

    Origin of the NLRI is neither IGP or EGP

    """
    INCOMPLETE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['BgpOriginAttrType_Enum']


class BgpSessionDirection_Enum(Enum):
    """
    BgpSessionDirection_Enum

    Type to describe the direction of NLRI transmission

    """

    """

    Refers to all NLRI received from the BGP peer

    """
    INBOUND = 0

    """

    Refers to all NLRI advertised to the BGP peer

    """
    OUTBOUND = 1


    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['BgpSessionDirection_Enum']


class CommunityType_Enum(Enum):
    """
    CommunityType_Enum

    type describing variations of community attributes\:
    STANDARD\: standard BGP community [rfc1997]
    EXTENDED\: extended BGP community [rfc4360]
    BOTH\: both standard and extended community

    """

    """

    send only standard communities

    """
    STANDARD = 0

    """

    send only extended communities

    """
    EXTENDED = 1

    """

    send both standard and extended communities

    """
    BOTH = 2

    """

    do not send any community attribute

    """
    NONE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['CommunityType_Enum']


class PeerType_Enum(Enum):
    """
    PeerType_Enum

    labels a peer or peer group as explicitly internal or
    external

    """

    """

    internal (iBGP) peer

    """
    INTERNAL = 0

    """

    external (eBGP) peer

    """
    EXTERNAL = 1


    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['PeerType_Enum']


class RemovePrivateAsOption_Enum(Enum):
    """
    RemovePrivateAsOption_Enum

    set of options for configuring how private AS path numbers
    are removed from advertisements

    """

    """

    remove all private ASes in the path

    """
    ALL = 0

    """

    replace private ASes with local AS

    """
    REPLACE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['RemovePrivateAsOption_Enum']



class AfiSafiType_Identity(object):
    """
    Base identity type for AFI,SAFI tuples for BGP\-4
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['AfiSafiType_Identity']['meta_info']


class BgpCapability_Identity(object):
    """
    Base identity for a BGP capability
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['BgpCapability_Identity']['meta_info']


class BgpWellKnownStdCommunity_Identity(object):
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
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['BgpWellKnownStdCommunity_Identity']['meta_info']


class ADDPATHS_Identity(BgpCapability_Identity):
    """
    BGP add\-paths
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        BgpCapability_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['ADDPATHS_Identity']['meta_info']


class ASN32_Identity(BgpCapability_Identity):
    """
    4\-byte (32\-bit) AS number functionality
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        BgpCapability_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['ASN32_Identity']['meta_info']


class GRACEFULRESTART_Identity(BgpCapability_Identity):
    """
    Graceful restart functionality
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        BgpCapability_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['GRACEFULRESTART_Identity']['meta_info']


class INTERNET_Identity(BgpWellKnownStdCommunity_Identity):
    """
    A community used by some implementations with the value 0\:0
    which represents all possible community values.
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        BgpWellKnownStdCommunity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['INTERNET_Identity']['meta_info']


class Ipv4LabelledUnicast_Identity(AfiSafiType_Identity):
    """
    Labelled IPv4 unicast (AFI,SAFI = 1,4)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['Ipv4LabelledUnicast_Identity']['meta_info']


class Ipv4Unicast_Identity(AfiSafiType_Identity):
    """
    IPv4 unicast (AFI,SAFI = 1,1)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['Ipv4Unicast_Identity']['meta_info']


class Ipv6LabelledUnicast_Identity(AfiSafiType_Identity):
    """
    Labelled IPv6 unicast (AFI,SAFI = 2,4)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['Ipv6LabelledUnicast_Identity']['meta_info']


class Ipv6Unicast_Identity(AfiSafiType_Identity):
    """
    IPv6 unicast (AFI,SAFI = 2,1)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['Ipv6Unicast_Identity']['meta_info']


class L2vpnEvpn_Identity(AfiSafiType_Identity):
    """
    BGP MPLS Based Ethernet VPN (AFI,SAFI = 25,70)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['L2vpnEvpn_Identity']['meta_info']


class L2vpnVpls_Identity(AfiSafiType_Identity):
    """
    BGP\-signalled VPLS (AFI,SAFI = 25,65)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['L2vpnVpls_Identity']['meta_info']


class L3vpnIpv4Multicast_Identity(AfiSafiType_Identity):
    """
    Multicast IPv4 MPLS L3VPN (AFI,SAFI = 1,129)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['L3vpnIpv4Multicast_Identity']['meta_info']


class L3vpnIpv4Unicast_Identity(AfiSafiType_Identity):
    """
    Unicast IPv4 MPLS L3VPN (AFI,SAFI = 1,128)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['L3vpnIpv4Unicast_Identity']['meta_info']


class L3vpnIpv6Multicast_Identity(AfiSafiType_Identity):
    """
    Multicast IPv6 MPLS L3VPN (AFI,SAFI = 2,129)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['L3vpnIpv6Multicast_Identity']['meta_info']


class L3vpnIpv6Unicast_Identity(AfiSafiType_Identity):
    """
    Unicast IPv6 MPLS L3VPN (AFI,SAFI = 2,128)
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        AfiSafiType_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['L3vpnIpv6Unicast_Identity']['meta_info']


class MPBGP_Identity(BgpCapability_Identity):
    """
    Multi\-protocol extensions to BGP
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        BgpCapability_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['MPBGP_Identity']['meta_info']


class NOPEER_Identity(BgpWellKnownStdCommunity_Identity):
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
        BgpWellKnownStdCommunity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['NOPEER_Identity']['meta_info']


class NO_ADVERTISE_Identity(BgpWellKnownStdCommunity_Identity):
    """
    All NLRI received carrying this community must not be
    advertised to other BGP peers. This community has a value of
    0xFFFFFF02.
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        BgpWellKnownStdCommunity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['NO_ADVERTISE_Identity']['meta_info']


class NO_EXPORT_Identity(BgpWellKnownStdCommunity_Identity):
    """
    Do not export NLRI received carrying this community outside
    the bounds of this autonomous system, or this confederation if
    the local autonomous system is a confederation member AS. This
    community has a value of 0xFFFFFF01.
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        BgpWellKnownStdCommunity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['NO_EXPORT_Identity']['meta_info']


class NO_EXPORT_SUBCONFED_Identity(BgpWellKnownStdCommunity_Identity):
    """
    All NLRI received carrying this community must not be
    advertised to external BGP peers \- including over confederation
    sub\-AS boundaries. This community has a value of 0xFFFFFF03.
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        BgpWellKnownStdCommunity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['NO_EXPORT_SUBCONFED_Identity']['meta_info']


class ROUTEREFRESH_Identity(BgpCapability_Identity):
    """
    The BGP route\-refresh functionality
    
    

    """

    _prefix = 'bgp-types'
    _revision = '2015-05-15'

    def __init__(self):
        BgpCapability_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp_types as meta
        return meta._meta_table['ROUTEREFRESH_Identity']['meta_info']


