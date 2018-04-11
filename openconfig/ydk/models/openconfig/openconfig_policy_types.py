""" openconfig_policy_types 

This module contains general data definitions for use in routing
policy.  It can be imported by modules that contain protocol\-
specific policy conditions and actions.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MatchSetOptionsRestrictedType(Enum):
    """
    MatchSetOptionsRestrictedType (Enum Class)

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
    MatchSetOptionsType (Enum Class)

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



class ATTRIBUTECOMPARISON(Identity):
    """
    base type for supported comparison operators on route
    attributes
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(ATTRIBUTECOMPARISON, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:ATTRIBUTE_COMPARISON")


class INSTALLPROTOCOLTYPE(Identity):
    """
    Base type for protocols which can install prefixes into the
    RIB
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(INSTALLPROTOCOLTYPE, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:INSTALL_PROTOCOL_TYPE")


class ATTRIBUTEEQ(Identity):
    """
    == comparison
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(ATTRIBUTEEQ, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:ATTRIBUTE_EQ")


class ATTRIBUTEGE(Identity):
    """
    >= comparison
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(ATTRIBUTEGE, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:ATTRIBUTE_GE")


class ATTRIBUTELE(Identity):
    """
    <= comparison
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(ATTRIBUTELE, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:ATTRIBUTE_LE")


class BGP(Identity):
    """
    BGP
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(BGP, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:BGP")


class ISIS(Identity):
    """
    IS\-IS
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(ISIS, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:ISIS")


class OSPF(Identity):
    """
    OSPFv2
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(OSPF, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:OSPF")


class OSPF3(Identity):
    """
    OSPFv3
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(OSPF3, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:OSPF3")


class STATIC(Identity):
    """
    Locally\-installed static route
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(STATIC, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:STATIC")


class DIRECTLYCONNECTED(Identity):
    """
    A directly connected route
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(DIRECTLYCONNECTED, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:DIRECTLY_CONNECTED")


class LOCALAGGREGATE(Identity):
    """
    Locally defined aggregate route
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2016-05-12'

    def __init__(self):
        super(LOCALAGGREGATE, self).__init__("http://openconfig.net/yang/policy-types", "openconfig-policy-types", "openconfig-policy-types:LOCAL_AGGREGATE")


