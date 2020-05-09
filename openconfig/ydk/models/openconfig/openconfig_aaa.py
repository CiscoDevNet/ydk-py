""" openconfig_aaa 

This module defines configuration and operational state data
related to authorization, authentication, and accounting (AAA)
management.

Portions of this model reuse data definitions or structure from
RFC 7317 \- A YANG Data Model for System Management

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error

from ydk.models.openconfig.openconfig_aaa_types import AAASERVERTYPE



class TACACS(AAASERVERTYPE):
    """
    Terminal Access Controller Access Control System (TACACS+)
    AAA server
    
    

    """

    _prefix = 'oc-aaa'
    _revision = '2017-09-18'

    def __init__(self, ns="http://openconfig.net/yang/aaa", pref="openconfig-aaa", tag="openconfig-aaa:TACACS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TACACS, self).__init__(ns, pref, tag)



class RADIUS(AAASERVERTYPE):
    """
    Remote Authentication Dial In User Service (RADIUS) AAA
    server
    
    

    """

    _prefix = 'oc-aaa'
    _revision = '2017-09-18'

    def __init__(self, ns="http://openconfig.net/yang/aaa", pref="openconfig-aaa", tag="openconfig-aaa:RADIUS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(RADIUS, self).__init__(ns, pref, tag)



