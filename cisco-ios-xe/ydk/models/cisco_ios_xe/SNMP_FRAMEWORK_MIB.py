""" SNMP_FRAMEWORK_MIB 

The SNMP Management Architecture MIB

Copyright (C) The Internet Society (2002). This
version of this MIB module is part of RFC 3411;
see the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.ietf.ietf_yang_smiv2 import ObjectIdentityIdentity

class SnmpsecuritylevelEnum(Enum):
    """
    SnmpsecuritylevelEnum

    A Level of Security at which SNMP messages can be

    sent or with which operations are being processed;

    in particular, one of\:

      noAuthNoPriv \- without authentication and

                     without privacy,

      authNoPriv   \- with authentication but

                     without privacy,

      authPriv     \- with authentication and

                     with privacy.

    These three values are ordered such that

    noAuthNoPriv is less than authNoPriv and

    authNoPriv is less than authPriv.

    .. data:: noAuthNoPriv = 1

    .. data:: authNoPriv = 2

    .. data:: authPriv = 3

    """

    noAuthNoPriv = 1

    authNoPriv = 2

    authPriv = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _SNMP_FRAMEWORK_MIB as meta
        return meta._meta_table['SnmpsecuritylevelEnum']



class SnmpauthprotocolsIdentity(ObjectIdentityIdentity):
    """
    Registration point for standards\-track
    authentication protocols used in SNMP Management
    Frameworks.
    
    

    """

    _prefix = 'SNMP-FRAMEWORK-MIB'
    _revision = '2002-10-14'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _SNMP_FRAMEWORK_MIB as meta
        return meta._meta_table['SnmpauthprotocolsIdentity']['meta_info']


class SnmpprivprotocolsIdentity(ObjectIdentityIdentity):
    """
    Registration point for standards\-track privacy
    protocols used in SNMP Management Frameworks.
    
    

    """

    _prefix = 'SNMP-FRAMEWORK-MIB'
    _revision = '2002-10-14'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _SNMP_FRAMEWORK_MIB as meta
        return meta._meta_table['SnmpprivprotocolsIdentity']['meta_info']


class SnmpFrameworkMib(object):
    """
    
    
    .. attribute:: snmpengine
    
    	
    	**type**\:   :py:class:`Snmpengine <ydk.models.cisco_ios_xe.SNMP_FRAMEWORK_MIB.SnmpFrameworkMib.Snmpengine>`
    
    

    """

    _prefix = 'SNMP-FRAMEWORK-MIB'
    _revision = '2002-10-14'

    def __init__(self):
        self.snmpengine = SnmpFrameworkMib.Snmpengine()
        self.snmpengine.parent = self


    class Snmpengine(object):
        """
        
        
        .. attribute:: snmpengineboots
        
        	The number of times that the SNMP engine has (re\-)initialized itself since snmpEngineID was last configured
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        .. attribute:: snmpengineid
        
        	An SNMP engine's administratively\-unique identifier.  This information SHOULD be stored in non\-volatile storage so that it remains constant across re\-initializations of the SNMP engine
        	**type**\:  str
        
        	**length:** 5..32
        
        .. attribute:: snmpenginemaxmessagesize
        
        	The maximum length in octets of an SNMP message which this SNMP engine can send or receive and process, determined as the minimum of the maximum message size values supported among all of the transports available to and supported by the engine
        	**type**\:  int
        
        	**range:** 484..2147483647
        
        .. attribute:: snmpenginetime
        
        	The number of seconds since the value of the snmpEngineBoots object last changed. When incrementing this object's value would cause it to exceed its maximum, snmpEngineBoots is incremented as if a re\-initialization had occurred, and this object's value consequently reverts to zero
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**units**\: seconds
        
        

        """

        _prefix = 'SNMP-FRAMEWORK-MIB'
        _revision = '2002-10-14'

        def __init__(self):
            self.parent = None
            self.snmpengineboots = None
            self.snmpengineid = None
            self.snmpenginemaxmessagesize = None
            self.snmpenginetime = None

        @property
        def _common_path(self):

            return '/SNMP-FRAMEWORK-MIB:SNMP-FRAMEWORK-MIB/SNMP-FRAMEWORK-MIB:snmpEngine'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.snmpengineboots is not None:
                return True

            if self.snmpengineid is not None:
                return True

            if self.snmpenginemaxmessagesize is not None:
                return True

            if self.snmpenginetime is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _SNMP_FRAMEWORK_MIB as meta
            return meta._meta_table['SnmpFrameworkMib.Snmpengine']['meta_info']

    @property
    def _common_path(self):

        return '/SNMP-FRAMEWORK-MIB:SNMP-FRAMEWORK-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.snmpengine is not None and self.snmpengine._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _SNMP_FRAMEWORK_MIB as meta
        return meta._meta_table['SnmpFrameworkMib']['meta_info']


