""" openconfig_types 

This module contains a set of general type definitions that
are used across OpenConfig models. It can be imported by modules
that make use of these types.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ADDRESSFAMILY(Identity):
    """
    A base identity for all address families
    
    

    """

    _prefix = 'oc-types'
    _revision = '2017-01-13'

    def __init__(self):
        super(ADDRESSFAMILY, self).__init__("http://openconfig.net/yang/openconfig-types", "openconfig-types", "openconfig-types:ADDRESS_FAMILY")


class IPV4(Identity):
    """
    The IPv4 address family
    
    

    """

    _prefix = 'oc-types'
    _revision = '2017-01-13'

    def __init__(self):
        super(IPV4, self).__init__("http://openconfig.net/yang/openconfig-types", "openconfig-types", "openconfig-types:IPV4")


class IPV6(Identity):
    """
    The IPv6 address family
    
    

    """

    _prefix = 'oc-types'
    _revision = '2017-01-13'

    def __init__(self):
        super(IPV6, self).__init__("http://openconfig.net/yang/openconfig-types", "openconfig-types", "openconfig-types:IPV6")


class MPLS(Identity):
    """
    The MPLS address family
    
    

    """

    _prefix = 'oc-types'
    _revision = '2017-01-13'

    def __init__(self):
        super(MPLS, self).__init__("http://openconfig.net/yang/openconfig-types", "openconfig-types", "openconfig-types:MPLS")


class L2ETHERNET(Identity):
    """
    The 802.3 Ethernet address family
    
    

    """

    _prefix = 'oc-types'
    _revision = '2017-01-13'

    def __init__(self):
        super(L2ETHERNET, self).__init__("http://openconfig.net/yang/openconfig-types", "openconfig-types", "openconfig-types:L2_ETHERNET")


