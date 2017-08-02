""" openconfig_mpls_types 

General types for MPLS / TE data model

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MplsLabel(Enum):
    """
    MplsLabel

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

    IPV4_EXPLICIT_NULL = Enum.YLeaf(0, "IPV4_EXPLICIT_NULL")

    ROUTER_ALERT = Enum.YLeaf(1, "ROUTER_ALERT")

    IPV6_EXPLICIT_NULL = Enum.YLeaf(2, "IPV6_EXPLICIT_NULL")

    IMPLICIT_NULL = Enum.YLeaf(3, "IMPLICIT_NULL")

    ENTROPY_LABEL_INDICATOR = Enum.YLeaf(7, "ENTROPY_LABEL_INDICATOR")


class TunnelType(Enum):
    """
    TunnelType

    defines the tunnel type for the LSP

    .. data:: P2P = 0

    	point-to-point label-switched-path

    .. data:: P2MP = 1

    	point-to-multipoint label-switched-path

    .. data:: MP2MP = 2

    	multipoint-to-multipoint label-switched-path

    """

    P2P = Enum.YLeaf(0, "P2P")

    P2MP = Enum.YLeaf(1, "P2MP")

    MP2MP = Enum.YLeaf(2, "MP2MP")



class TunnelType(Identity):
    """
    Base identity from which specific tunnel types are
    derived.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(TunnelType, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:tunnel-type")


class TunnelAdminStatus(Identity):
    """
    Base identity for tunnel administrative status
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(TunnelAdminStatus, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:tunnel-admin-status")


class ProtectionType(Identity):
    """
    base identity for protection type
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(ProtectionType, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:protection-type")


class NullLabelType(Identity):
    """
    Base identity from which specific null\-label types are
    derived.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(NullLabelType, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:null-label-type")


class PathSetupProtocol(Identity):
    """
    base identity for supported MPLS signaling
    protocols
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(PathSetupProtocol, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:path-setup-protocol")


class LspRole(Identity):
    """
    Base identity for describing the role of
    label switched path at the current node
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(LspRole, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:lsp-role")


class LspOperStatus(Identity):
    """
    Base identity for LSP operational status
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(LspOperStatus, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:lsp-oper-status")


class LinkNodeProtectionRequested(Identity):
    """
    node and link protection are both desired
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(LinkNodeProtectionRequested, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:link-node-protection-requested")


class P2Mp(Identity):
    """
    TE point\-to\-multipoint tunnel type.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(P2Mp, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:P2MP")


class Explicit(Identity):
    """
    Explicit null label is used.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(Explicit, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:EXPLICIT")


class Admin_Up(Identity):
    """
    LSP is administratively up
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(Admin_Up, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:ADMIN_UP")


class PathSetupLdp(Identity):
    """
    LDP \- RFC 5036
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(PathSetupLdp, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:path-setup-ldp")


class Ingress(Identity):
    """
    Label switched path is an ingress (headend)
    LSP
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(Ingress, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:INGRESS")


class LinkProtectionRequested(Identity):
    """
    link protection is desired
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(LinkProtectionRequested, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:link-protection-requested")


class Up(Identity):
    """
    LSP is operationally active and available
    for traffic.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(Up, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:UP")


class PathSetupSr(Identity):
    """
    Segment routing
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(PathSetupSr, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:path-setup-sr")


class Down(Identity):
    """
    LSP is operationally down or out of service
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(Down, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:DOWN")


class Egress(Identity):
    """
    Label switched path is an egress (tailend)
    LSP
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(Egress, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:EGRESS")


class P2P(Identity):
    """
    TE point\-to\-point tunnel type.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(P2P, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:P2P")


class Transit(Identity):
    """
    Label switched path is a transit LSP
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(Transit, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:TRANSIT")


class Admin_Down(Identity):
    """
    LSP is administratively down
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(Admin_Down, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:ADMIN_DOWN")


class PathSetupRsvp(Identity):
    """
    RSVP\-TE signaling protocol
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(PathSetupRsvp, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:path-setup-rsvp")


class Implicit(Identity):
    """
    Implicit null label is used.
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(Implicit, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:IMPLICIT")


class Unprotected(Identity):
    """
    no protection is desired
    
    

    """

    _prefix = 'mplst'
    _revision = '2015-11-05'

    def __init__(self):
        super(Unprotected, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:unprotected")


