""" openconfig_mpls_types 

General types for MPLS / TE data model

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class MplsLabelEnum(Enum):
    """
    MplsLabelEnum

    type for MPLS label value encoding

    .. data:: IPV4_EXPLICIT_NULL = 0

    	valid at the bottom of the label stack,

    	indicates that stack must be popped and packet forwarded

    	based on IPv4 header

    .. data:: ROUTER_ALERT = 1

    	allowed anywhere in the label stack except

    	the bottom, local router delivers packet to the local CPU

    	when this label is at the top of the stack

    .. data:: IPV6_EXPLICIT_NULL = 2

    	valid at the bottom of the label stack,

    	indicates that stack must be popped and packet forwarded

    	based on IPv6 header

    .. data:: IMPLICIT_NULL = 3

    	assigned by local LSR but not carried in

    	packets

    .. data:: ENTROPY_LABEL_INDICATOR = 7

    	Entropy label indicator, to allow an LSR

    	to distinguish between entropy label and applicaiton

    	labels RFC 6790

    """

    IPV4_EXPLICIT_NULL = 0

    ROUTER_ALERT = 1

    IPV6_EXPLICIT_NULL = 2

    IMPLICIT_NULL = 3

    ENTROPY_LABEL_INDICATOR = 7


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['MplsLabelEnum']


class TunnelTypeEnum(Enum):
    """
    TunnelTypeEnum

    defines the tunnel type for the LSP

    .. data:: P2P = 0

    	point-to-point label-switched-path

    .. data:: P2MP = 1

    	point-to-multipoint label-switched-path

    .. data:: MP2MP = 2

    	multipoint-to-multipoint label-switched-path

    """

    P2P = 0

    P2MP = 1

    MP2MP = 2


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['TunnelTypeEnum']



class TunnelAdminStatusIdentity(object):
    """
    Base identity for tunnel administrative status
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['TunnelAdminStatusIdentity']['meta_info']


class LspOperStatusIdentity(object):
    """
    Base identity for LSP operational status
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['LspOperStatusIdentity']['meta_info']


class PathSetupProtocolIdentity(object):
    """
    base identity for supported MPLS signaling
    protocols
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['PathSetupProtocolIdentity']['meta_info']


class NullLabelTypeIdentity(object):
    """
    Base identity from which specific null\-label types are
    derived.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['NullLabelTypeIdentity']['meta_info']


class LspRoleIdentity(object):
    """
    Base identity for describing the role of
    label switched path at the current node
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['LspRoleIdentity']['meta_info']


class ProtectionTypeIdentity(object):
    """
    base identity for protection type
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['ProtectionTypeIdentity']['meta_info']


class TunnelTypeIdentity(object):
    """
    Base identity from which specific tunnel types are
    derived.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['TunnelTypeIdentity']['meta_info']


class P2PIdentity(TunnelTypeIdentity):
    """
    TE point\-to\-point tunnel type.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        TunnelTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['P2PIdentity']['meta_info']


class UnprotectedIdentity(ProtectionTypeIdentity):
    """
    no protection is desired
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        ProtectionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['UnprotectedIdentity']['meta_info']


class Admin_UpIdentity(TunnelAdminStatusIdentity):
    """
    LSP is administratively up
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        TunnelAdminStatusIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['Admin_UpIdentity']['meta_info']


class DownIdentity(LspOperStatusIdentity):
    """
    LSP is operationally down or out of service
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        LspOperStatusIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['DownIdentity']['meta_info']


class PathSetupLdpIdentity(PathSetupProtocolIdentity):
    """
    LDP \- RFC 5036
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        PathSetupProtocolIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['PathSetupLdpIdentity']['meta_info']


class UpIdentity(LspOperStatusIdentity):
    """
    LSP is operationally active and available
    for traffic.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        LspOperStatusIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['UpIdentity']['meta_info']


class TransitIdentity(LspRoleIdentity):
    """
    Label switched path is a transit LSP
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        LspRoleIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['TransitIdentity']['meta_info']


class LinkNodeProtectionRequestedIdentity(ProtectionTypeIdentity):
    """
    node and link protection are both desired
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        ProtectionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['LinkNodeProtectionRequestedIdentity']['meta_info']


class EgressIdentity(LspRoleIdentity):
    """
    Label switched path is an egress (tailend)
    LSP
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        LspRoleIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['EgressIdentity']['meta_info']


class LinkProtectionRequestedIdentity(ProtectionTypeIdentity):
    """
    link protection is desired
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        ProtectionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['LinkProtectionRequestedIdentity']['meta_info']


class ExplicitIdentity(NullLabelTypeIdentity):
    """
    Explicit null label is used.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        NullLabelTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['ExplicitIdentity']['meta_info']


class PathSetupSrIdentity(PathSetupProtocolIdentity):
    """
    Segment routing
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        PathSetupProtocolIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['PathSetupSrIdentity']['meta_info']


class Admin_DownIdentity(TunnelAdminStatusIdentity):
    """
    LSP is administratively down
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        TunnelAdminStatusIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['Admin_DownIdentity']['meta_info']


class IngressIdentity(LspRoleIdentity):
    """
    Label switched path is an ingress (headend)
    LSP
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        LspRoleIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['IngressIdentity']['meta_info']


class ImplicitIdentity(NullLabelTypeIdentity):
    """
    Implicit null label is used.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        NullLabelTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['ImplicitIdentity']['meta_info']


class PathSetupRsvpIdentity(PathSetupProtocolIdentity):
    """
    RSVP\-TE signaling protocol
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        PathSetupProtocolIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['PathSetupRsvpIdentity']['meta_info']


class P2MpIdentity(TunnelTypeIdentity):
    """
    TE point\-to\-multipoint tunnel type.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        TunnelTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['P2MpIdentity']['meta_info']


