""" ietf_routing_types 

This module contains a collection of YANG data types
considered generally useful for routing protocols.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class Ipv4MulticastSourceAddressEnum(Enum):
    """
    Ipv4MulticastSourceAddressEnum

    Multicast source IPv4 address type.

    .. data:: Y__STAR__ = 0

    	Any source address.

    """

    Y__STAR__ = 0


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['Ipv4MulticastSourceAddressEnum']


class Ipv6MulticastSourceAddressEnum(Enum):
    """
    Ipv6MulticastSourceAddressEnum

    Multicast source IPv6 address type.

    .. data:: Y__STAR__ = 0

    	Any source address.

    """

    Y__STAR__ = 0


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['Ipv6MulticastSourceAddressEnum']


class LinkAccessTypeEnum(Enum):
    """
    LinkAccessTypeEnum

    Link access type.

    .. data:: broadcast = 0

    	Specify broadcast multi-access network.

    .. data:: non_broadcast_multiaccess = 1

    	Specify Non-Broadcast Multi-Access (NBMA) network.

    .. data:: point_to_multipoint = 2

    	Specify point-to-multipoint network.

    .. data:: point_to_point = 3

    	Specify point-to-point network.

    """

    broadcast = 0

    non_broadcast_multiaccess = 1

    point_to_multipoint = 2

    point_to_point = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['LinkAccessTypeEnum']


class RouteTargetTypeEnum(Enum):
    """
    RouteTargetTypeEnum

    Indicates the role a route target takes

    in route filtering.

    .. data:: import_ = 0

    	The route target applies to route import.

    .. data:: export = 1

    	The route target applies to route export.

    .. data:: both = 2

    	The route target applies to both route import and

    	route export.

    """

    import_ = 0

    export = 1

    both = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['RouteTargetTypeEnum']


class TimerValueMillisecondsEnum(Enum):
    """
    TimerValueMillisecondsEnum

    Timer value type, in milliseconds.

    .. data:: infinity = 0

    	The timer is set to infinity.

    .. data:: not_set = 1

    	The timer is not set.

    """

    infinity = 0

    not_set = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['TimerValueMillisecondsEnum']


class TimerValueSeconds16Enum(Enum):
    """
    TimerValueSeconds16Enum

    Timer value type, in seconds (16 bit range).

    .. data:: infinity = 0

    	The timer is set to infinity.

    .. data:: not_set = 1

    	The timer is not set.

    """

    infinity = 0

    not_set = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['TimerValueSeconds16Enum']


class TimerValueSeconds32Enum(Enum):
    """
    TimerValueSeconds32Enum

    Timer value type, in seconds (32 bit range).

    .. data:: infinity = 0

    	The timer is set to infinity.

    .. data:: not_set = 1

    	The timer is not set.

    """

    infinity = 0

    not_set = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['TimerValueSeconds32Enum']



class MplsLabelSpecialPurposeValueIdentity(object):
    """
    Base identity for deriving identities describing
    special\-purpose Multiprotocol Label Switching (MPLS) label
    values.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['MplsLabelSpecialPurposeValueIdentity']['meta_info']


class AddressFamilyIdentity(object):
    """
    Base identity from which identities describing address
    families are derived.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['AddressFamilyIdentity']['meta_info']


class MplsTpSectionEidIdentity(AddressFamilyIdentity):
    """
    MPLS\-TP Section Endpoint Identifier
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['MplsTpSectionEidIdentity']['meta_info']


class MtV6Identity(AddressFamilyIdentity):
    """
    Multi\-Topology IPv6.
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['MtV6Identity']['meta_info']


class HdlcIdentity(AddressFamilyIdentity):
    """
    (8\-bit multidrop)
     Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['HdlcIdentity']['meta_info']


class Ieee802Identity(AddressFamilyIdentity):
    """
    (includes all 802 media plus Ethernet canonical format)
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['Ieee802Identity']['meta_info']


class MtV4Identity(AddressFamilyIdentity):
    """
    Multi\-Topology IPv4.
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['MtV4Identity']['meta_info']


class IpxIdentity(AddressFamilyIdentity):
    """
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['IpxIdentity']['meta_info']


class GalLabelIdentity(MplsLabelSpecialPurposeValueIdentity):
    """
    This identity represents the Generic Associated Channel Label
    (GAL).
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        MplsLabelSpecialPurposeValueIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['GalLabelIdentity']['meta_info']


class OamAlertLabelIdentity(MplsLabelSpecialPurposeValueIdentity):
    """
    This identity represents the OAM Alert Label.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        MplsLabelSpecialPurposeValueIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['OamAlertLabelIdentity']['meta_info']


class X121Identity(AddressFamilyIdentity):
    """
    (X.25, Frame Relay)
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['X121Identity']['meta_info']


class ExtensionLabelIdentity(MplsLabelSpecialPurposeValueIdentity):
    """
    This identity represents the Extension Label.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        MplsLabelSpecialPurposeValueIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['ExtensionLabelIdentity']['meta_info']


class MplsTpPweEidIdentity(AddressFamilyIdentity):
    """
    MPLS\-TP Pseudowire Endpoint Identifier
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['MplsTpPweEidIdentity']['meta_info']


class E164NsapIdentity(AddressFamilyIdentity):
    """
    E.164 with NSAP format subaddress
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['E164NsapIdentity']['meta_info']


class L2VpnIdentity(AddressFamilyIdentity):
    """
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['L2VpnIdentity']['meta_info']


class DecnetIvIdentity(AddressFamilyIdentity):
    """
    Decnet IV
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['DecnetIvIdentity']['meta_info']


class XtpIdentity(AddressFamilyIdentity):
    """
    XTP native mode XTP
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['XtpIdentity']['meta_info']


class Ipv4ExplicitNullLabelIdentity(MplsLabelSpecialPurposeValueIdentity):
    """
    This identity represents the IPv4 Explicit NULL Label.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        MplsLabelSpecialPurposeValueIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['Ipv4ExplicitNullLabelIdentity']['meta_info']


class XtpV4Identity(AddressFamilyIdentity):
    """
    XTP over IPv4
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['XtpV4Identity']['meta_info']


class XtpV6Identity(AddressFamilyIdentity):
    """
    XTP over IPv6
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['XtpV6Identity']['meta_info']


class FcPortIdentity(AddressFamilyIdentity):
    """
    Fibre Channel World\-Wide Port Name
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['FcPortIdentity']['meta_info']


class E163Identity(AddressFamilyIdentity):
    """
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['E163Identity']['meta_info']


class E164Identity(AddressFamilyIdentity):
    """
    SMDS, Frame Relay, ATM
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['E164Identity']['meta_info']


class Ipv4Identity(AddressFamilyIdentity):
    """
    This identity represents IPv4 address family.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['Ipv4Identity']['meta_info']


class DnsIdentity(AddressFamilyIdentity):
    """
    Domain Name System
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['DnsIdentity']['meta_info']


class Ipv6Identity(AddressFamilyIdentity):
    """
    This identity represents IPv6 address family.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['Ipv6Identity']['meta_info']


class MplsTpLspEidIdentity(AddressFamilyIdentity):
    """
    MPLS\-TP LSP Endpoint Identifier
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['MplsTpLspEidIdentity']['meta_info']


class ImplicitNullLabelIdentity(MplsLabelSpecialPurposeValueIdentity):
    """
    This identity represents the Implicit NULL Label.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        MplsLabelSpecialPurposeValueIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['ImplicitNullLabelIdentity']['meta_info']


class DnIdentity(AddressFamilyIdentity):
    """
    Distinguished Name
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['DnIdentity']['meta_info']


class F69Identity(AddressFamilyIdentity):
    """
    (Telex)
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['F69Identity']['meta_info']


class FcNodeIdentity(AddressFamilyIdentity):
    """
    Fibre Channel World\-Wide Node Name
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['FcNodeIdentity']['meta_info']


class Ipv6ExplicitNullLabelIdentity(MplsLabelSpecialPurposeValueIdentity):
    """
    This identity represents the IPv6 Explicit NULL Label.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        MplsLabelSpecialPurposeValueIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['Ipv6ExplicitNullLabelIdentity']['meta_info']


class EntropyLabelIndicatorIdentity(MplsLabelSpecialPurposeValueIdentity):
    """
    This identity represents the Entropy Label Indicator.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        MplsLabelSpecialPurposeValueIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['EntropyLabelIndicatorIdentity']['meta_info']


class NsapIdentity(AddressFamilyIdentity):
    """
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['NsapIdentity']['meta_info']


class GwidIdentity(AddressFamilyIdentity):
    """
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['GwidIdentity']['meta_info']


class VinesIdentity(AddressFamilyIdentity):
    """
    Banyan Vines
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['VinesIdentity']['meta_info']


class AsNumIdentity(AddressFamilyIdentity):
    """
    AS Number
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['AsNumIdentity']['meta_info']


class AppletalkIdentity(AddressFamilyIdentity):
    """
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['AppletalkIdentity']['meta_info']


class RouterAlertLabelIdentity(MplsLabelSpecialPurposeValueIdentity):
    """
    This identity represents the Router Alert Label.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        MplsLabelSpecialPurposeValueIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['RouterAlertLabelIdentity']['meta_info']


class Bbn1822Identity(AddressFamilyIdentity):
    """
    AHIP (BBN report #1822)
    Address family from IANA registry.
    
    

    """

    _prefix = 'rt-types'
    _revision = '2017-02-27'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing_types as meta
        return meta._meta_table['Bbn1822Identity']['meta_info']


