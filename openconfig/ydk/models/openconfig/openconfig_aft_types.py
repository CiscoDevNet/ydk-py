""" openconfig_aft_types 

Types related to the OpenConfig Abstract Forwarding
Table (AFT) model

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class EncapsulationHeaderType(Enum):
    """
    EncapsulationHeaderType (Enum Class)

    Types of tunnel encapsulation that are supported by systems as either

    head\- or tail\-end.

    .. data:: GRE = 0

    	The encapsulation header is a Generic Routing Encapsulation

    	header.

    .. data:: IPV4 = 1

    	The encapsulation header is an IPv4 packet header

    .. data:: IPV6 = 2

    	The encapsulation header is an IPv6 packet header

    .. data:: MPLS = 3

    	The encapsulation header is one or more MPLS labels indicated

    	by the pushed and popped label stack lists.

    """

    GRE = Enum.YLeaf(0, "GRE")

    IPV4 = Enum.YLeaf(1, "IPV4")

    IPV6 = Enum.YLeaf(2, "IPV6")

    MPLS = Enum.YLeaf(3, "MPLS")



class AFTADDRESSFAMILY(Identity):
    """
    A base identity that is used for address families that have
    distinct Abstract Forwarding Tables (AFTs).
    
    

    """

    _prefix = 'oc-aftt'
    _revision = '2017-01-13'

    def __init__(self):
        super(AFTADDRESSFAMILY, self).__init__("http://openconfig.net/yang/fib-types", "openconfig-aft-types", "openconfig-aft-types:AFT_ADDRESS_FAMILY")


class IPV4UNICAST(Identity):
    """
    The AFT entries within the corresponding table relate to unicast
    IPv4 forwarding entries.
    
    

    """

    _prefix = 'oc-aftt'
    _revision = '2017-01-13'

    def __init__(self):
        super(IPV4UNICAST, self).__init__("http://openconfig.net/yang/fib-types", "openconfig-aft-types", "openconfig-aft-types:IPV4_UNICAST")


class IPV6UNICAST(Identity):
    """
    The AFT entries within the corresponding table relate to unicast
    IPv6 forwarding entries.
    
    

    """

    _prefix = 'oc-aftt'
    _revision = '2017-01-13'

    def __init__(self):
        super(IPV6UNICAST, self).__init__("http://openconfig.net/yang/fib-types", "openconfig-aft-types", "openconfig-aft-types:IPV6_UNICAST")


class MPLS(Identity):
    """
    The AFT entries within the corresponding table relate to labelled
    forwarding entries using MPLS labels.
    
    

    """

    _prefix = 'oc-aftt'
    _revision = '2017-01-13'

    def __init__(self):
        super(MPLS, self).__init__("http://openconfig.net/yang/fib-types", "openconfig-aft-types", "openconfig-aft-types:MPLS")


class L2ETHERNET(Identity):
    """
    The AFT entries within the corresponding table relate to Ethernet
    switched forwarding entries.
    
    

    """

    _prefix = 'oc-aftt'
    _revision = '2017-01-13'

    def __init__(self):
        super(L2ETHERNET, self).__init__("http://openconfig.net/yang/fib-types", "openconfig-aft-types", "openconfig-aft-types:L2_ETHERNET")


