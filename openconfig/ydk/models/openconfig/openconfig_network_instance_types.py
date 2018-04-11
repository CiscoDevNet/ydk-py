""" openconfig_network_instance_types 

Types associated with a network instance

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class NETWORKINSTANCETYPE(Identity):
    """
    A base identity which can be extended to indicate different
    types of network instance supported by a device.
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(NETWORKINSTANCETYPE, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:NETWORK_INSTANCE_TYPE")


class ENDPOINTTYPE(Identity):
    """
    Specification of the type of endpoint that is being associated
    with a network instance
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(ENDPOINTTYPE, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:ENDPOINT_TYPE")


class LABELALLOCATIONMODE(Identity):
    """
    Base identity to be used to express types of label allocation
    strategies to be used within a network instance
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(LABELALLOCATIONMODE, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:LABEL_ALLOCATION_MODE")


class ENCAPSULATION(Identity):
    """
    On the wire encapsulations that can be used when
    differentiating network instances
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(ENCAPSULATION, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:ENCAPSULATION")


class SIGNALLINGPROTOCOL(Identity):
    """
    The signalling protocol that should be used to diseminate
    entries within a forwarding instance
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(SIGNALLINGPROTOCOL, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:SIGNALLING_PROTOCOL")


class DEFAULTINSTANCE(Identity):
    """
    A special routing instance which acts as the 'default' or
    'global' routing instance for a network device.
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(DEFAULTINSTANCE, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:DEFAULT_INSTANCE")


class L3VRF(Identity):
    """
    A private Layer 3 only routing instance which is formed of
    one or more RIBs
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(L3VRF, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:L3VRF")


class L2VSI(Identity):
    """
    A private Layer 2 only switch instance which is formed of
    one or more L2 forwarding tables
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(L2VSI, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:L2VSI")


class L2P2P(Identity):
    """
    A private Layer 2 only forwarding instance which acts as
    a point to point connection between two endpoints
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(L2P2P, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:L2P2P")


class L2L3(Identity):
    """
    A private Layer 2 and Layer 2 forwarding instance
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(L2L3, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:L2L3")


class LOCAL(Identity):
    """
    A local interface which is being associated with the endpoint
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(LOCAL, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:LOCAL")


class REMOTE(Identity):
    """
    A remote interface which is being associated with the
    endpoint
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(REMOTE, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:REMOTE")


class PERPREFIX(Identity):
    """
    A label is to be allocated per prefix entry in the RIB for the
    network instance
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(PERPREFIX, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:PER_PREFIX")


class PERNEXTHOP(Identity):
    """
    A label is to be allocated per nexthop entry in the RIB for
    the network instance
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(PERNEXTHOP, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:PER_NEXTHOP")


class INSTANCELABEL(Identity):
    """
    A single label is to be used for the instance
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(INSTANCELABEL, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:INSTANCE_LABEL")


class MPLS(Identity):
    """
    Use MPLS labels to distinguish network instances on the wire
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(MPLS, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:MPLS")


class VXLAN(Identity):
    """
    Use VXLAN (RFC7348) VNIs to distinguish network instances on
    the wire
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(VXLAN, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:VXLAN")


class LDP(Identity):
    """
    Use LDP\-based setup for signalling. Where the instance is
    a point\-to\-point service this refers to RFC4447 ('Martini')
    setup. Where the service is an L2VSI, or L2L3 instance it
    refers to RFC4762 LDP\-signalled VPLS instances
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(LDP, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:LDP")


class BGPVPLS(Identity):
    """
    Use BGP\-based signalling and autodiscovery for VPLS instances
    as per RFC4761
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(BGPVPLS, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:BGP_VPLS")


class BGPEVPN(Identity):
    """
    Use BGP\-based Ethernet VPN (RFC7432) based signalling for
    the network instance
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self):
        super(BGPEVPN, self).__init__("http://openconfig.net/yang/network-instance-types", "openconfig-network-instance-types", "openconfig-network-instance-types:BGP_EVPN")


