""" openconfig_types 

This module contains a set of general type definitions that
are used across OpenConfig models. It can be imported by modules
that make use of these types.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class ADDRESSFAMILY(Identity):
    """
    A base identity for all address families
    
    

    """

    _prefix = 'oc-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/openconfig-types", pref="openconfig-types", tag="openconfig-types:ADDRESS_FAMILY"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ADDRESSFAMILY, self).__init__(ns, pref, tag)



class IPV4(ADDRESSFAMILY):
    """
    The IPv4 address family
    
    

    """

    _prefix = 'oc-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/openconfig-types", pref="openconfig-types", tag="openconfig-types:IPV4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IPV4, self).__init__(ns, pref, tag)



class IPV6(ADDRESSFAMILY):
    """
    The IPv6 address family
    
    

    """

    _prefix = 'oc-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/openconfig-types", pref="openconfig-types", tag="openconfig-types:IPV6"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IPV6, self).__init__(ns, pref, tag)



class MPLS(ADDRESSFAMILY):
    """
    The MPLS address family
    
    

    """

    _prefix = 'oc-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/openconfig-types", pref="openconfig-types", tag="openconfig-types:MPLS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MPLS, self).__init__(ns, pref, tag)



class L2ETHERNET(ADDRESSFAMILY):
    """
    The 802.3 Ethernet address family
    
    

    """

    _prefix = 'oc-types'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/openconfig-types", pref="openconfig-types", tag="openconfig-types:L2_ETHERNET"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(L2ETHERNET, self).__init__(ns, pref, tag)



