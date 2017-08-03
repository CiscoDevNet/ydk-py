""" openconfig_policy_types 

This module contains general data definitions for use in routing
policy.  It can be imported by modules that contain protocol\-
specific policy conditions and actions.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MatchSetOptionsRestrictedType(Enum):
    """
    MatchSetOptionsRestrictedType

    Options that govern the behavior of a match statement.  The

    default behavior is ANY, i.e., the given value matches any

    of the members of the defined set.  Note this type is a

    restricted version of the match\-set\-options\-type.

    .. data:: ANY = 0

    	match is true if given value matches any member

    	of the defined set

    .. data:: INVERT = 1

    	match is true if given value does not match any

    	member of the defined set

    """

    ANY = Enum.YLeaf(0, "ANY")

    INVERT = Enum.YLeaf(1, "INVERT")


class MatchSetOptionsType(Enum):
    """
    MatchSetOptionsType

    Options that govern the behavior of a match statement.  The

    default behavior is ANY, i.e., the given value matches any

    of the members of the defined set

    .. data:: ANY = 0

    	match is true if given value matches any member

    	of the defined set

    .. data:: ALL = 1

    	match is true if given value matches all

    	members of the defined set

    .. data:: INVERT = 2

    	match is true if given value does not match any

    	member of the defined set

    """

    ANY = Enum.YLeaf(0, "ANY")

    ALL = Enum.YLeaf(1, "ALL")

    INVERT = Enum.YLeaf(2, "INVERT")



class Attribute_Comparison(Identity):
    """
    base type for supported comparison operators on route
    attributes
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(Attribute_Comparison, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:ATTRIBUTE_COMPARISON")


class Install_Protocol_Type(Identity):
    """
    Base type for protocols which can install prefixes into the
    RIB
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(Install_Protocol_Type, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:INSTALL_PROTOCOL_TYPE")


class Attribute_Le(Identity):
    """
    <= comparison
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(Attribute_Le, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:ATTRIBUTE_LE")


class Local_Aggregate(Identity):
    """
    Locally defined aggregate route
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(Local_Aggregate, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:LOCAL_AGGREGATE")


class Attribute_Eq(Identity):
    """
    == comparison
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(Attribute_Eq, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:ATTRIBUTE_EQ")


class Directly_Connected(Identity):
    """
    A directly connected route
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(Directly_Connected, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:DIRECTLY_CONNECTED")


class Ospf(Identity):
    """
    OSPFv2
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(Ospf, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:OSPF")


class Attribute_Ge(Identity):
    """
    >= comparison
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(Attribute_Ge, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:ATTRIBUTE_GE")


class Isis(Identity):
    """
    IS\-IS
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(Isis, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:ISIS")


class Ospf3(Identity):
    """
    OSPFv3
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(Ospf3, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:OSPF3")


class Static(Identity):
    """
    Locally\-installed static route
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(Static, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:STATIC")


class Bgp(Identity):
    """
    BGP
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(Bgp, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:BGP")


