""" openconfig_policy_types 

This module contains general data definitions for use in routing
policy.  It can be imported by modules that contain protocol\-
specific policy conditions and actions.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
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
    _revision = '2017-07-14'

    def __init__(self, ns="http://openconfig.net/yang/policy-types", pref="openconfig-policy-types", tag="openconfig-policy-types:ATTRIBUTE_COMPARISON"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ATTRIBUTECOMPARISON, self).__init__(ns, pref, tag)



class INSTALLPROTOCOLTYPE(Identity):
    """
    Base type for protocols which can install prefixes into the
    RIB
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2017-07-14'

    def __init__(self, ns="http://openconfig.net/yang/policy-types", pref="openconfig-policy-types", tag="openconfig-policy-types:INSTALL_PROTOCOL_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(INSTALLPROTOCOLTYPE, self).__init__(ns, pref, tag)



class ATTRIBUTEEQ(ATTRIBUTECOMPARISON):
    """
    == comparison
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2017-07-14'

    def __init__(self, ns="http://openconfig.net/yang/policy-types", pref="openconfig-policy-types", tag="openconfig-policy-types:ATTRIBUTE_EQ"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ATTRIBUTEEQ, self).__init__(ns, pref, tag)



class ATTRIBUTEGE(ATTRIBUTECOMPARISON):
    """
    >= comparison
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2017-07-14'

    def __init__(self, ns="http://openconfig.net/yang/policy-types", pref="openconfig-policy-types", tag="openconfig-policy-types:ATTRIBUTE_GE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ATTRIBUTEGE, self).__init__(ns, pref, tag)



class ATTRIBUTELE(ATTRIBUTECOMPARISON):
    """
    <= comparison
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2017-07-14'

    def __init__(self, ns="http://openconfig.net/yang/policy-types", pref="openconfig-policy-types", tag="openconfig-policy-types:ATTRIBUTE_LE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ATTRIBUTELE, self).__init__(ns, pref, tag)



class BGP(INSTALLPROTOCOLTYPE):
    """
    BGP
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2017-07-14'

    def __init__(self, ns="http://openconfig.net/yang/policy-types", pref="openconfig-policy-types", tag="openconfig-policy-types:BGP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(BGP, self).__init__(ns, pref, tag)



class ISIS(INSTALLPROTOCOLTYPE):
    """
    IS\-IS
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2017-07-14'

    def __init__(self, ns="http://openconfig.net/yang/policy-types", pref="openconfig-policy-types", tag="openconfig-policy-types:ISIS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ISIS, self).__init__(ns, pref, tag)



class OSPF(INSTALLPROTOCOLTYPE):
    """
    OSPFv2
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2017-07-14'

    def __init__(self, ns="http://openconfig.net/yang/policy-types", pref="openconfig-policy-types", tag="openconfig-policy-types:OSPF"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OSPF, self).__init__(ns, pref, tag)



class OSPF3(INSTALLPROTOCOLTYPE):
    """
    OSPFv3
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2017-07-14'

    def __init__(self, ns="http://openconfig.net/yang/policy-types", pref="openconfig-policy-types", tag="openconfig-policy-types:OSPF3"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(OSPF3, self).__init__(ns, pref, tag)



class STATIC(INSTALLPROTOCOLTYPE):
    """
    Locally\-installed static route
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2017-07-14'

    def __init__(self, ns="http://openconfig.net/yang/policy-types", pref="openconfig-policy-types", tag="openconfig-policy-types:STATIC"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(STATIC, self).__init__(ns, pref, tag)



class DIRECTLYCONNECTED(INSTALLPROTOCOLTYPE):
    """
    A directly connected route
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2017-07-14'

    def __init__(self, ns="http://openconfig.net/yang/policy-types", pref="openconfig-policy-types", tag="openconfig-policy-types:DIRECTLY_CONNECTED"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DIRECTLYCONNECTED, self).__init__(ns, pref, tag)



class LOCALAGGREGATE(INSTALLPROTOCOLTYPE):
    """
    Locally defined aggregate route
    
    

    """

    _prefix = 'oc-pol-types'
    _revision = '2017-07-14'

    def __init__(self, ns="http://openconfig.net/yang/policy-types", pref="openconfig-policy-types", tag="openconfig-policy-types:LOCAL_AGGREGATE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LOCALAGGREGATE, self).__init__(ns, pref, tag)



