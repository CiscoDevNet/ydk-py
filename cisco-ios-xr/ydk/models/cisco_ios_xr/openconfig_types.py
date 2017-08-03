""" openconfig_types 

This module contains a set of general type definitions that
are used across OpenConfig models. It can be imported by modules
that make use of these types.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Address_Family(Identity):
    """
    A base identity for all address families
    
    

    """

    _prefix = 'oc-types'
    _revision = '2016-05-31'

    def __init__(self):
        super(Address_Family, self).__init__("http://openconfig.net/yang/openconfig-types", "openconfig-types", "openconfig-types:ADDRESS_FAMILY")


class Ipv6(Identity):
    """
    The IPv6 address family
    
    

    """

    _prefix = 'oc-types'
    _revision = '2016-05-31'

    def __init__(self):
        super(Ipv6, self).__init__("http://openconfig.net/yang/openconfig-types", "openconfig-types", "openconfig-types:IPV6")


class Ipv4(Identity):
    """
    The IPv4 address family
    
    

    """

    _prefix = 'oc-types'
    _revision = '2016-05-31'

    def __init__(self):
        super(Ipv4, self).__init__("http://openconfig.net/yang/openconfig-types", "openconfig-types", "openconfig-types:IPV4")


