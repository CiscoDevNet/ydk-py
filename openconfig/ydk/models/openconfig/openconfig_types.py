""" openconfig_types 

This module contains a set of general type definitions that
are used across OpenConfig models. It can be imported by modules
that make use of these types.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Address_FamilyIdentity(object):
    """
    A base identity for all address families
    
    

    """

    _prefix = 'oc-types'
    _revision = '2016-05-31'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_types as meta
        return meta._meta_table['Address_FamilyIdentity']['meta_info']


class Ipv6Identity(Address_FamilyIdentity):
    """
    The IPv6 address family
    
    

    """

    _prefix = 'oc-types'
    _revision = '2016-05-31'

    def __init__(self):
        Address_FamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_types as meta
        return meta._meta_table['Ipv6Identity']['meta_info']


class Ipv4Identity(Address_FamilyIdentity):
    """
    The IPv4 address family
    
    

    """

    _prefix = 'oc-types'
    _revision = '2016-05-31'

    def __init__(self):
        Address_FamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_types as meta
        return meta._meta_table['Ipv4Identity']['meta_info']


