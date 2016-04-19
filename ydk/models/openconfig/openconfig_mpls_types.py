""" openconfig_mpls_types 

General types for MPLS / TE data model

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



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



class LspOperStatus_Identity(object):
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
        return meta._meta_table['LspOperStatus_Identity']['meta_info']


class LspRole_Identity(object):
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
        return meta._meta_table['LspRole_Identity']['meta_info']


class NullLabelType_Identity(object):
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
        return meta._meta_table['NullLabelType_Identity']['meta_info']


class PathSetupProtocol_Identity(object):
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
        return meta._meta_table['PathSetupProtocol_Identity']['meta_info']


class ProtectionType_Identity(object):
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
        return meta._meta_table['ProtectionType_Identity']['meta_info']


class TunnelAdminStatus_Identity(object):
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
        return meta._meta_table['TunnelAdminStatus_Identity']['meta_info']


class TunnelType_Identity(object):
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
        return meta._meta_table['TunnelType_Identity']['meta_info']


class Admin_Down_Identity(TunnelAdminStatus_Identity):
    """
    LSP is administratively down
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        TunnelAdminStatus_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['Admin_Down_Identity']['meta_info']


class Admin_Up_Identity(TunnelAdminStatus_Identity):
    """
    LSP is administratively up
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        TunnelAdminStatus_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['Admin_Up_Identity']['meta_info']


class Down_Identity(LspOperStatus_Identity):
    """
    LSP is operationally down or out of service
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        LspOperStatus_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['Down_Identity']['meta_info']


class Egress_Identity(LspRole_Identity):
    """
    Label switched path is an egress (tailend)
    LSP
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        LspRole_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['Egress_Identity']['meta_info']


class Explicit_Identity(NullLabelType_Identity):
    """
    Explicit null label is used.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        NullLabelType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['Explicit_Identity']['meta_info']


class Implicit_Identity(NullLabelType_Identity):
    """
    Implicit null label is used.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        NullLabelType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['Implicit_Identity']['meta_info']


class Ingress_Identity(LspRole_Identity):
    """
    Label switched path is an ingress (headend)
    LSP
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        LspRole_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['Ingress_Identity']['meta_info']


class LinkNodeProtectionRequested_Identity(ProtectionType_Identity):
    """
    node and link protection are both desired
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        ProtectionType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['LinkNodeProtectionRequested_Identity']['meta_info']


class LinkProtectionRequested_Identity(ProtectionType_Identity):
    """
    link protection is desired
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        ProtectionType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['LinkProtectionRequested_Identity']['meta_info']


class P2Mp_Identity(TunnelType_Identity):
    """
    TE point\-to\-multipoint tunnel type.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        TunnelType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['P2Mp_Identity']['meta_info']


class P2P_Identity(TunnelType_Identity):
    """
    TE point\-to\-point tunnel type.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        TunnelType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['P2P_Identity']['meta_info']


class PathSetupLdp_Identity(PathSetupProtocol_Identity):
    """
    LDP \- RFC 5036
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        PathSetupProtocol_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['PathSetupLdp_Identity']['meta_info']


class PathSetupRsvp_Identity(PathSetupProtocol_Identity):
    """
    RSVP\-TE signaling protocol
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        PathSetupProtocol_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['PathSetupRsvp_Identity']['meta_info']


class PathSetupSr_Identity(PathSetupProtocol_Identity):
    """
    Segment routing
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        PathSetupProtocol_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['PathSetupSr_Identity']['meta_info']


class Transit_Identity(LspRole_Identity):
    """
    Label switched path is a transit LSP
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        LspRole_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['Transit_Identity']['meta_info']


class Unprotected_Identity(ProtectionType_Identity):
    """
    no protection is desired
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        ProtectionType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['Unprotected_Identity']['meta_info']


class Up_Identity(LspOperStatus_Identity):
    """
    LSP is operationally active and available
    for traffic.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        LspOperStatus_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_mpls_types as meta
        return meta._meta_table['Up_Identity']['meta_info']


