""" openconfig_network_instance_types 

Types associated with a network instance

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
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

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:NETWORK_INSTANCE_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(NETWORKINSTANCETYPE, self).__init__(ns, pref, tag)



class ENDPOINTTYPE(Identity):
    """
    Specification of the type of endpoint that is being associated
    with a network instance
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:ENDPOINT_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ENDPOINTTYPE, self).__init__(ns, pref, tag)



class LABELALLOCATIONMODE(Identity):
    """
    Base identity to be used to express types of label allocation
    strategies to be used within a network instance
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:LABEL_ALLOCATION_MODE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LABELALLOCATIONMODE, self).__init__(ns, pref, tag)



class ENCAPSULATION(Identity):
    """
    On the wire encapsulations that can be used when
    differentiating network instances
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:ENCAPSULATION"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ENCAPSULATION, self).__init__(ns, pref, tag)



class SIGNALLINGPROTOCOL(Identity):
    """
    The signalling protocol that should be used to diseminate
    entries within a forwarding instance
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:SIGNALLING_PROTOCOL"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SIGNALLINGPROTOCOL, self).__init__(ns, pref, tag)



class DEFAULTINSTANCE(NETWORKINSTANCETYPE):
    """
    A special routing instance which acts as the 'default' or
    'global' routing instance for a network device.
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:DEFAULT_INSTANCE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DEFAULTINSTANCE, self).__init__(ns, pref, tag)



class L3VRF(NETWORKINSTANCETYPE):
    """
    A private Layer 3 only routing instance which is formed of
    one or more RIBs
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:L3VRF"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(L3VRF, self).__init__(ns, pref, tag)



class L2VSI(NETWORKINSTANCETYPE):
    """
    A private Layer 2 only switch instance which is formed of
    one or more L2 forwarding tables
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:L2VSI"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(L2VSI, self).__init__(ns, pref, tag)



class L2P2P(NETWORKINSTANCETYPE):
    """
    A private Layer 2 only forwarding instance which acts as
    a point to point connection between two endpoints
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:L2P2P"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(L2P2P, self).__init__(ns, pref, tag)



class L2L3(NETWORKINSTANCETYPE):
    """
    A private Layer 2 and Layer 2 forwarding instance
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:L2L3"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(L2L3, self).__init__(ns, pref, tag)



class LOCAL(ENDPOINTTYPE):
    """
    A local interface which is being associated with the endpoint
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:LOCAL"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LOCAL, self).__init__(ns, pref, tag)



class REMOTE(ENDPOINTTYPE):
    """
    A remote interface which is being associated with the
    endpoint
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:REMOTE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(REMOTE, self).__init__(ns, pref, tag)



class PERPREFIX(LABELALLOCATIONMODE):
    """
    A label is to be allocated per prefix entry in the RIB for the
    network instance
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:PER_PREFIX"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PERPREFIX, self).__init__(ns, pref, tag)



class PERNEXTHOP(LABELALLOCATIONMODE):
    """
    A label is to be allocated per nexthop entry in the RIB for
    the network instance
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:PER_NEXTHOP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PERNEXTHOP, self).__init__(ns, pref, tag)



class INSTANCELABEL(LABELALLOCATIONMODE):
    """
    A single label is to be used for the instance
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:INSTANCE_LABEL"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(INSTANCELABEL, self).__init__(ns, pref, tag)



class MPLS(ENCAPSULATION):
    """
    Use MPLS labels to distinguish network instances on the wire
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:MPLS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MPLS, self).__init__(ns, pref, tag)



class VXLAN(ENCAPSULATION):
    """
    Use VXLAN (RFC7348) VNIs to distinguish network instances on
    the wire
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:VXLAN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VXLAN, self).__init__(ns, pref, tag)



class LDP(SIGNALLINGPROTOCOL):
    """
    Use LDP\-based setup for signalling. Where the instance is
    a point\-to\-point service this refers to RFC4447 ('Martini')
    setup. Where the service is an L2VSI, or L2L3 instance it
    refers to RFC4762 LDP\-signalled VPLS instances
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:LDP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LDP, self).__init__(ns, pref, tag)



class BGPVPLS(SIGNALLINGPROTOCOL):
    """
    Use BGP\-based signalling and autodiscovery for VPLS instances
    as per RFC4761
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:BGP_VPLS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(BGPVPLS, self).__init__(ns, pref, tag)



class BGPEVPN(SIGNALLINGPROTOCOL):
    """
    Use BGP\-based Ethernet VPN (RFC7432) based signalling for
    the network instance
    
    

    """

    _prefix = 'oc-ni-types'
    _revision = '2016-12-15'

    def __init__(self, ns="http://openconfig.net/yang/network-instance-types", pref="openconfig-network-instance-types", tag="openconfig-network-instance-types:BGP_EVPN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(BGPEVPN, self).__init__(ns, pref, tag)



