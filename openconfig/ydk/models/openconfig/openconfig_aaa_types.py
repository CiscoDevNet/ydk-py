""" openconfig_aaa_types 

This module defines shared types for data related to AAA
(authentication, authorization, accounting).

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class AAASERVERTYPE(Identity):
    """
    Base identity for types of AAA servers
    
    

    """

    _prefix = 'oc-aaa-types'
    _revision = '2018-04-12'

    def __init__(self, ns="http://openconfig.net/yang/aaa/types", pref="openconfig-aaa-types", tag="openconfig-aaa-types:AAA_SERVER_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AAASERVERTYPE, self).__init__(ns, pref, tag)



class SYSTEMDEFINEDROLES(Identity):
    """
    Base identity for system\_defined roles that can be assigned
    to users.
    
    

    """

    _prefix = 'oc-aaa-types'
    _revision = '2018-04-12'

    def __init__(self, ns="http://openconfig.net/yang/aaa/types", pref="openconfig-aaa-types", tag="openconfig-aaa-types:SYSTEM_DEFINED_ROLES"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SYSTEMDEFINEDROLES, self).__init__(ns, pref, tag)



class AAAACCOUNTINGEVENTTYPE(Identity):
    """
    Base identity for specifying events types that should be
    sent to AAA server for accounting
    
    

    """

    _prefix = 'oc-aaa-types'
    _revision = '2018-04-12'

    def __init__(self, ns="http://openconfig.net/yang/aaa/types", pref="openconfig-aaa-types", tag="openconfig-aaa-types:AAA_ACCOUNTING_EVENT_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AAAACCOUNTINGEVENTTYPE, self).__init__(ns, pref, tag)



class AAAAUTHORIZATIONEVENTTYPE(Identity):
    """
    Base identity for specifying activities that should be
    sent to AAA server for authorization
    
    

    """

    _prefix = 'oc-aaa-types'
    _revision = '2018-04-12'

    def __init__(self, ns="http://openconfig.net/yang/aaa/types", pref="openconfig-aaa-types", tag="openconfig-aaa-types:AAA_AUTHORIZATION_EVENT_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AAAAUTHORIZATIONEVENTTYPE, self).__init__(ns, pref, tag)



class AAAMETHODTYPE(Identity):
    """
    Base identity to define well\-known methods for AAA
    operations
    
    

    """

    _prefix = 'oc-aaa-types'
    _revision = '2018-04-12'

    def __init__(self, ns="http://openconfig.net/yang/aaa/types", pref="openconfig-aaa-types", tag="openconfig-aaa-types:AAA_METHOD_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AAAMETHODTYPE, self).__init__(ns, pref, tag)



class SYSTEMROLEADMIN(SYSTEMDEFINEDROLES):
    """
    Built\-in role that allows the equivalent of superuser
    permission for all configuration and operational commands
    on the device.
    
    

    """

    _prefix = 'oc-aaa-types'
    _revision = '2018-04-12'

    def __init__(self, ns="http://openconfig.net/yang/aaa/types", pref="openconfig-aaa-types", tag="openconfig-aaa-types:SYSTEM_ROLE_ADMIN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SYSTEMROLEADMIN, self).__init__(ns, pref, tag)



class AAAACCOUNTINGEVENTCOMMAND(AAAACCOUNTINGEVENTTYPE):
    """
    Specifies interactive command events for AAA accounting
    
    

    """

    _prefix = 'oc-aaa-types'
    _revision = '2018-04-12'

    def __init__(self, ns="http://openconfig.net/yang/aaa/types", pref="openconfig-aaa-types", tag="openconfig-aaa-types:AAA_ACCOUNTING_EVENT_COMMAND"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AAAACCOUNTINGEVENTCOMMAND, self).__init__(ns, pref, tag)



class AAAACCOUNTINGEVENTLOGIN(AAAACCOUNTINGEVENTTYPE):
    """
    Specifies login events for AAA accounting
    
    

    """

    _prefix = 'oc-aaa-types'
    _revision = '2018-04-12'

    def __init__(self, ns="http://openconfig.net/yang/aaa/types", pref="openconfig-aaa-types", tag="openconfig-aaa-types:AAA_ACCOUNTING_EVENT_LOGIN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AAAACCOUNTINGEVENTLOGIN, self).__init__(ns, pref, tag)



class AAAAUTHORIZATIONEVENTCOMMAND(AAAAUTHORIZATIONEVENTTYPE):
    """
    Specifies interactive command events for AAA authorization
    
    

    """

    _prefix = 'oc-aaa-types'
    _revision = '2018-04-12'

    def __init__(self, ns="http://openconfig.net/yang/aaa/types", pref="openconfig-aaa-types", tag="openconfig-aaa-types:AAA_AUTHORIZATION_EVENT_COMMAND"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AAAAUTHORIZATIONEVENTCOMMAND, self).__init__(ns, pref, tag)



class AAAAUTHORIZATIONEVENTCONFIG(AAAAUTHORIZATIONEVENTTYPE):
    """
    Specifies configuration (e.g., EXEC) events for AAA
    authorization
    
    

    """

    _prefix = 'oc-aaa-types'
    _revision = '2018-04-12'

    def __init__(self, ns="http://openconfig.net/yang/aaa/types", pref="openconfig-aaa-types", tag="openconfig-aaa-types:AAA_AUTHORIZATION_EVENT_CONFIG"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AAAAUTHORIZATIONEVENTCONFIG, self).__init__(ns, pref, tag)



class TACACSALL(AAAMETHODTYPE):
    """
    The group of all TACACS+ servers.
    
    

    """

    _prefix = 'oc-aaa-types'
    _revision = '2018-04-12'

    def __init__(self, ns="http://openconfig.net/yang/aaa/types", pref="openconfig-aaa-types", tag="openconfig-aaa-types:TACACS_ALL"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TACACSALL, self).__init__(ns, pref, tag)



class RADIUSALL(AAAMETHODTYPE):
    """
    The group of all RADIUS servers.
    
    

    """

    _prefix = 'oc-aaa-types'
    _revision = '2018-04-12'

    def __init__(self, ns="http://openconfig.net/yang/aaa/types", pref="openconfig-aaa-types", tag="openconfig-aaa-types:RADIUS_ALL"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(RADIUSALL, self).__init__(ns, pref, tag)



class LOCAL(AAAMETHODTYPE):
    """
    Locally configured method for AAA operations.
    
    

    """

    _prefix = 'oc-aaa-types'
    _revision = '2018-04-12'

    def __init__(self, ns="http://openconfig.net/yang/aaa/types", pref="openconfig-aaa-types", tag="openconfig-aaa-types:LOCAL"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LOCAL, self).__init__(ns, pref, tag)



