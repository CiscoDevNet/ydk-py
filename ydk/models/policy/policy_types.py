""" policy_types 

This module contains general data definitions for use in routing
policy.  It can be imported by modules that contain protocol\-
specific policy conditions and actions.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



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
        from ydk.models.policy._meta import _policy_types as meta
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
        from ydk.models.policy._meta import _policy_types as meta
        return meta._meta_table['MatchSetOptionsTypeEnum']



class AttributeComparison_Identity(object):
    """
    base type for supported comparison operators on route
    attributes
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-05-15'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.policy._meta import _policy_types as meta
        return meta._meta_table['AttributeComparison_Identity']['meta_info']


class InstallProtocolType_Identity(object):
    """
    Base type for protocols which can install prefixes into the
    RIB
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-05-15'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.policy._meta import _policy_types as meta
        return meta._meta_table['InstallProtocolType_Identity']['meta_info']


class AttributeEq_Identity(AttributeComparison_Identity):
    """
    == comparison
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-05-15'

    def __init__(self):
        AttributeComparison_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.policy._meta import _policy_types as meta
        return meta._meta_table['AttributeEq_Identity']['meta_info']


class AttributeGe_Identity(AttributeComparison_Identity):
    """
    >= comparison
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-05-15'

    def __init__(self):
        AttributeComparison_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.policy._meta import _policy_types as meta
        return meta._meta_table['AttributeGe_Identity']['meta_info']


class AttributeLe_Identity(AttributeComparison_Identity):
    """
    <= comparison
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-05-15'

    def __init__(self):
        AttributeComparison_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.policy._meta import _policy_types as meta
        return meta._meta_table['AttributeLe_Identity']['meta_info']


class Bgp_Identity(InstallProtocolType_Identity):
    """
    BGP
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-05-15'

    def __init__(self):
        InstallProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.policy._meta import _policy_types as meta
        return meta._meta_table['Bgp_Identity']['meta_info']


class DirectlyConnected_Identity(InstallProtocolType_Identity):
    """
    A directly connected route
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-05-15'

    def __init__(self):
        InstallProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.policy._meta import _policy_types as meta
        return meta._meta_table['DirectlyConnected_Identity']['meta_info']


class Isis_Identity(InstallProtocolType_Identity):
    """
    IS\-IS
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-05-15'

    def __init__(self):
        InstallProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.policy._meta import _policy_types as meta
        return meta._meta_table['Isis_Identity']['meta_info']


class LocalAggregate_Identity(InstallProtocolType_Identity):
    """
    Locally defined aggregate route
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-05-15'

    def __init__(self):
        InstallProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.policy._meta import _policy_types as meta
        return meta._meta_table['LocalAggregate_Identity']['meta_info']


class Ospf3_Identity(InstallProtocolType_Identity):
    """
    OSPFv3
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-05-15'

    def __init__(self):
        InstallProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.policy._meta import _policy_types as meta
        return meta._meta_table['Ospf3_Identity']['meta_info']


class Ospf_Identity(InstallProtocolType_Identity):
    """
    OSPFv2
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-05-15'

    def __init__(self):
        InstallProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.policy._meta import _policy_types as meta
        return meta._meta_table['Ospf_Identity']['meta_info']


class Static_Identity(InstallProtocolType_Identity):
    """
    Locally\-installed static route
    
    

    """

    _prefix = 'ptypes'
    _revision = '2015-05-15'

    def __init__(self):
        InstallProtocolType_Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.policy._meta import _policy_types as meta
        return meta._meta_table['Static_Identity']['meta_info']


