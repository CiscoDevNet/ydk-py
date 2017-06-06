""" openconfig_policy_types 

This module contains general data definitions for use in routing
policy.  It can be imported by modules that contain protocol\-
specific policy conditions and actions.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class MatchSetOptionsRestrictedTypeEnum(Enum):
    """
    MatchSetOptionsRestrictedTypeEnum

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

    ANY = 0

    INVERT = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_policy_types as meta
        return meta._meta_table['MatchSetOptionsRestrictedTypeEnum']


class MatchSetOptionsTypeEnum(Enum):
    """
    MatchSetOptionsTypeEnum

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

    ANY = 0

    ALL = 1

    INVERT = 2


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_policy_types as meta
        return meta._meta_table['MatchSetOptionsTypeEnum']



class AttributeComparisonIdentity(object):
    """
    base type for supported comparison operators on route
    attributes
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-10-09'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_policy_types as meta
        return meta._meta_table['AttributeComparisonIdentity']['meta_info']


class InstallProtocolTypeIdentity(object):
    """
    Base type for protocols which can install prefixes into the
    RIB
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-10-09'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_policy_types as meta
        return meta._meta_table['InstallProtocolTypeIdentity']['meta_info']


class AttributeLeIdentity(AttributeComparisonIdentity):
    """
    <= comparison
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-10-09'

    def __init__(self):
        AttributeComparisonIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_policy_types as meta
        return meta._meta_table['AttributeLeIdentity']['meta_info']


class DirectlyConnectedIdentity(InstallProtocolTypeIdentity):
    """
    A directly connected route
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-10-09'

    def __init__(self):
        InstallProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_policy_types as meta
        return meta._meta_table['DirectlyConnectedIdentity']['meta_info']


class AttributeEqIdentity(AttributeComparisonIdentity):
    """
    == comparison
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-10-09'

    def __init__(self):
        AttributeComparisonIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_policy_types as meta
        return meta._meta_table['AttributeEqIdentity']['meta_info']


class BgpIdentity(InstallProtocolTypeIdentity):
    """
    BGP
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-10-09'

    def __init__(self):
        InstallProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_policy_types as meta
        return meta._meta_table['BgpIdentity']['meta_info']


class AttributeGeIdentity(AttributeComparisonIdentity):
    """
    >= comparison
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-10-09'

    def __init__(self):
        AttributeComparisonIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_policy_types as meta
        return meta._meta_table['AttributeGeIdentity']['meta_info']


class OspfIdentity(InstallProtocolTypeIdentity):
    """
    OSPFv2
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-10-09'

    def __init__(self):
        InstallProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_policy_types as meta
        return meta._meta_table['OspfIdentity']['meta_info']


class LocalAggregateIdentity(InstallProtocolTypeIdentity):
    """
    Locally defined aggregate route
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-10-09'

    def __init__(self):
        InstallProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_policy_types as meta
        return meta._meta_table['LocalAggregateIdentity']['meta_info']


class IsisIdentity(InstallProtocolTypeIdentity):
    """
    IS\-IS
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-10-09'

    def __init__(self):
        InstallProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_policy_types as meta
        return meta._meta_table['IsisIdentity']['meta_info']


class Ospf3Identity(InstallProtocolTypeIdentity):
    """
    OSPFv3
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-10-09'

    def __init__(self):
        InstallProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_policy_types as meta
        return meta._meta_table['Ospf3Identity']['meta_info']


class StaticIdentity(InstallProtocolTypeIdentity):
    """
    Locally\-installed static route
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-10-09'

    def __init__(self):
        InstallProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_policy_types as meta
        return meta._meta_table['StaticIdentity']['meta_info']


