""" openconfig_if_types 

This module contains a set of interface type definitions that
are used across OpenConfig models. These are generally physical
or logical interfaces, distinct from hardware ports (which are
described by the OpenConfig platform model).

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class INTERFACETYPE(Identity):
    """
    Base identity from which interface types are derived.
    
    

    """

    _prefix = 'oc-ift'
    _revision = '2018-01-05'

    def __init__(self, ns="http://openconfig.net/yang/openconfig-if-types", pref="openconfig-if-types", tag="openconfig-if-types:INTERFACE_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(INTERFACETYPE, self).__init__(ns, pref, tag)



class IFETHERNET(INTERFACETYPE):
    """
    Ethernet interfaces based on IEEE 802.3 standards, as well
    as FlexEthernet
    
    

    """

    _prefix = 'oc-ift'
    _revision = '2018-01-05'

    def __init__(self, ns="http://openconfig.net/yang/openconfig-if-types", pref="openconfig-if-types", tag="openconfig-if-types:IF_ETHERNET"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IFETHERNET, self).__init__(ns, pref, tag)



class IFAGGREGATE(INTERFACETYPE):
    """
    An aggregated, or bonded, interface forming a
    Link Aggregation Group (LAG), or bundle, most often based on
    the IEEE 802.1AX (or 802.3ad) standard.
    
    

    """

    _prefix = 'oc-ift'
    _revision = '2018-01-05'

    def __init__(self, ns="http://openconfig.net/yang/openconfig-if-types", pref="openconfig-if-types", tag="openconfig-if-types:IF_AGGREGATE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IFAGGREGATE, self).__init__(ns, pref, tag)



class IFLOOPBACK(INTERFACETYPE):
    """
    A virtual interface designated as a loopback used for
    various management and operations tasks.
    
    

    """

    _prefix = 'oc-ift'
    _revision = '2018-01-05'

    def __init__(self, ns="http://openconfig.net/yang/openconfig-if-types", pref="openconfig-if-types", tag="openconfig-if-types:IF_LOOPBACK"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IFLOOPBACK, self).__init__(ns, pref, tag)



class IFROUTEDVLAN(INTERFACETYPE):
    """
    A logical interface used for routing services on a VLAN.
    Such interfaces are also known as switch virtual interfaces
    (SVI) or integrated routing and bridging interfaces (IRBs).
    
    

    """

    _prefix = 'oc-ift'
    _revision = '2018-01-05'

    def __init__(self, ns="http://openconfig.net/yang/openconfig-if-types", pref="openconfig-if-types", tag="openconfig-if-types:IF_ROUTED_VLAN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IFROUTEDVLAN, self).__init__(ns, pref, tag)



class IFSONET(INTERFACETYPE):
    """
    SONET/SDH interface
    
    

    """

    _prefix = 'oc-ift'
    _revision = '2018-01-05'

    def __init__(self, ns="http://openconfig.net/yang/openconfig-if-types", pref="openconfig-if-types", tag="openconfig-if-types:IF_SONET"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IFSONET, self).__init__(ns, pref, tag)



class IFTUNNELGRE4(INTERFACETYPE):
    """
    A GRE tunnel over IPv4 transport.
    
    

    """

    _prefix = 'oc-ift'
    _revision = '2018-01-05'

    def __init__(self, ns="http://openconfig.net/yang/openconfig-if-types", pref="openconfig-if-types", tag="openconfig-if-types:IF_TUNNEL_GRE4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IFTUNNELGRE4, self).__init__(ns, pref, tag)



class IFTUNNELGRE6(INTERFACETYPE):
    """
    A GRE tunnel over IPv6 transport.
    
    

    """

    _prefix = 'oc-ift'
    _revision = '2018-01-05'

    def __init__(self, ns="http://openconfig.net/yang/openconfig-if-types", pref="openconfig-if-types", tag="openconfig-if-types:IF_TUNNEL_GRE6"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IFTUNNELGRE6, self).__init__(ns, pref, tag)



