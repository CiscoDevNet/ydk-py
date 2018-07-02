""" openconfig_mpls_types 

General types for MPLS / TE data model

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MplsLabel(Enum):
    """
    MplsLabel (Enum Class)

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

    .. data:: NO_LABEL = 8

    	This value is utilised to indicate that the packet that

    	is forwarded by the local system does not have an MPLS

    	header applied to it. Typically, this is used at the

    	egress of an LSP

    """

    IPV4_EXPLICIT_NULL = Enum.YLeaf(0, "IPV4_EXPLICIT_NULL")

    ROUTER_ALERT = Enum.YLeaf(1, "ROUTER_ALERT")

    IPV6_EXPLICIT_NULL = Enum.YLeaf(2, "IPV6_EXPLICIT_NULL")

    IMPLICIT_NULL = Enum.YLeaf(3, "IMPLICIT_NULL")

    ENTROPY_LABEL_INDICATOR = Enum.YLeaf(7, "ENTROPY_LABEL_INDICATOR")

    NO_LABEL = Enum.YLeaf(8, "NO_LABEL")


class TunnelType(Enum):
    """
    TunnelType (Enum Class)

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



class PROTECTIONTYPE(Identity):
    """
    base identity for protection type
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(PROTECTIONTYPE, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:PROTECTION_TYPE")


class PATHSETUPPROTOCOL(Identity):
    """
    base identity for supported MPLS signaling
    protocols
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(PATHSETUPPROTOCOL, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:PATH_SETUP_PROTOCOL")


class PATHCOMPUTATIONMETHOD(Identity):
    """
    base identity for supported path computation
    mechanisms
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(PATHCOMPUTATIONMETHOD, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:PATH_COMPUTATION_METHOD")


class TUNNELADMINSTATUS(Identity):
    """
    Base identity for tunnel administrative status
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(TUNNELADMINSTATUS, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:TUNNEL_ADMIN_STATUS")


class TUNNELTYPE(Identity):
    """
    Base identity from which specific tunnel types are
    derived.
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(TUNNELTYPE, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:TUNNEL_TYPE")


class NULLLABELTYPE(Identity):
    """
    Base identity from which specific null\-label types are
    derived.
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(NULLLABELTYPE, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:NULL_LABEL_TYPE")


class LSPOPERSTATUS(Identity):
    """
    Base identity for LSP operational status
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(LSPOPERSTATUS, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:LSP_OPER_STATUS")


class LSPMETRICTYPE(Identity):
    """
    Base identity for types of LSP metric specification
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(LSPMETRICTYPE, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:LSP_METRIC_TYPE")


class LSPROLE(Identity):
    """
    Base identity for describing the role of
    label switched path at the current node
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(LSPROLE, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:LSP_ROLE")


class LSPMETRICINHERITED(Identity):
    """
    The metric for for the LSPs to which this identity refers is
    not specified explicitly \- but rather inherited from the IGP
    cost directly
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(LSPMETRICINHERITED, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:LSP_METRIC_INHERITED")


class DOWN(Identity):
    """
    LSP is operationally down or out of service
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(DOWN, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:DOWN")


class LOCALLYCOMPUTED(Identity):
    """
    indicates a constrained\-path LSP in which the
    path is computed by the local LER
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(LOCALLYCOMPUTED, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:LOCALLY_COMPUTED")


class P2P(Identity):
    """
    TE point\-to\-point tunnel type.
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(P2P, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:P2P")


class PATHSETUPSR(Identity):
    """
    Segment routing
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(PATHSETUPSR, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:PATH_SETUP_SR")


class INGRESS(Identity):
    """
    Label switched path is an ingress (headend)
    LSP
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(INGRESS, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:INGRESS")


class PATHSETUPRSVP(Identity):
    """
    RSVP\-TE signaling protocol
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(PATHSETUPRSVP, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:PATH_SETUP_RSVP")


class PATHSETUPLDP(Identity):
    """
    LDP \- RFC 5036
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(PATHSETUPLDP, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:PATH_SETUP_LDP")


class EXPLICIT(Identity):
    """
    Explicit null label is used.
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(EXPLICIT, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:EXPLICIT")


class ADMINUP(Identity):
    """
    LSP is administratively up
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(ADMINUP, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:ADMIN_UP")


class P2MP(Identity):
    """
    TE point\-to\-multipoint tunnel type.
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(P2MP, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:P2MP")


class LINKPROTECTIONREQUIRED(Identity):
    """
    link protection is desired
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(LINKPROTECTIONREQUIRED, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:LINK_PROTECTION_REQUIRED")


class EGRESS(Identity):
    """
    Label switched path is an egress (tailend)
    LSP
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(EGRESS, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:EGRESS")


class IMPLICIT(Identity):
    """
    Implicit null label is used.
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(IMPLICIT, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:IMPLICIT")


class LINKNODEPROTECTIONREQUESTED(Identity):
    """
    node and link protection are both desired
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(LINKNODEPROTECTIONREQUESTED, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:LINK_NODE_PROTECTION_REQUESTED")


class LSPMETRICABSOLUTE(Identity):
    """
    The metric specified for the LSPs to which this identity refers
    is specified as an absolute value
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(LSPMETRICABSOLUTE, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:LSP_METRIC_ABSOLUTE")


class EXTERNALLYQUERIED(Identity):
    """
    Constrained\-path LSP in which the path is
    obtained by querying an external source, such as a PCE server.
    In the case that an LSP is defined to be externally queried, it may
    also have associated explicit definitions (which are provided to the
    external source to aid computation); and the path that is returned by
    the external source is not required to provide a wholly resolved
    path back to the originating system \- that is to say, some local
    computation may also be required
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(EXTERNALLYQUERIED, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:EXTERNALLY_QUERIED")


class ADMINDOWN(Identity):
    """
    LSP is administratively down
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(ADMINDOWN, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:ADMIN_DOWN")


class EXPLICITLYDEFINED(Identity):
    """
    constrained\-path LSP in which the path is
    explicitly specified as a collection of strict or/and loose
    hops
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(EXPLICITLYDEFINED, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:EXPLICITLY_DEFINED")


class TRANSIT(Identity):
    """
    Label switched path is a transit LSP
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(TRANSIT, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:TRANSIT")


class UP(Identity):
    """
    LSP is operationally active and available
    for traffic.
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(UP, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:UP")


class LSPMETRICRELATIVE(Identity):
    """
    The metric specified for the LSPs to which this identity refers
    is specified as a relative value to the IGP metric cost to the
    LSP's tail\-end.
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(LSPMETRICRELATIVE, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:LSP_METRIC_RELATIVE")


class UNPROTECTED(Identity):
    """
    no protection is desired
    
    

    """

    _prefix = 'oc-mpls-types'
    _revision = '2017-06-21'

    def __init__(self):
        super(UNPROTECTED, self).__init__("http://openconfig.net/yang/mpls-types", "openconfig-mpls-types", "openconfig-mpls-types:UNPROTECTED")


