""" SNMP_FRAMEWORK_MIB 


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class SnmpSecurityLevel_Enum(Enum):
    """
    SnmpSecurityLevel_Enum

    """

    NOAUTHNOPRIV = 1

    AUTHNOPRIV = 2

    AUTHPRIV = 3


    @staticmethod
    def _meta_info():
        from ydk.models.snmp._meta import _SNMP_FRAMEWORK_MIB as meta
        return meta._meta_table['SnmpSecurityLevel_Enum']



class SNMPFRAMEWORKMIB(object):
    """
    
    
    .. attribute:: snmpengine
    
    	
    	**type**\: :py:class:`SnmpEngine <ydk.models.snmp.SNMP_FRAMEWORK_MIB.SNMPFRAMEWORKMIB.SnmpEngine>`
    
    

    """

    _prefix = 'SNMP_FRAMEWORK_MIB'
    _revision = '2002-10-14'

    def __init__(self):
        self.snmpengine = SNMPFRAMEWORKMIB.SnmpEngine()
        self.snmpengine.parent = self


    class SnmpEngine(object):
        """
        
        
        .. attribute:: snmpengineboots
        
        	
        	**type**\: int
        
        	**range:** 1..2147483647
        
        .. attribute:: snmpengineid
        
        	
        	**type**\: str
        
        	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
        
        .. attribute:: snmpenginemaxmessagesize
        
        	
        	**type**\: int
        
        	**range:** 484..2147483647
        
        .. attribute:: snmpenginetime
        
        	
        	**type**\: int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'SNMP_FRAMEWORK_MIB'
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
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.snmpengineboots is not None:
                return True

            if self.snmpengineid is not None:
                return True

            if self.snmpenginemaxmessagesize is not None:
                return True

            if self.snmpenginetime is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.snmp._meta import _SNMP_FRAMEWORK_MIB as meta
            return meta._meta_table['SNMPFRAMEWORKMIB.SnmpEngine']['meta_info']

    @property
    def _common_path(self):

        return '/SNMP-FRAMEWORK-MIB:SNMP-FRAMEWORK-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.snmpengine is not None and self.snmpengine._has_data():
            return True

        if self.snmpengine is not None and self.snmpengine.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.snmp._meta import _SNMP_FRAMEWORK_MIB as meta
        return meta._meta_table['SNMPFRAMEWORKMIB']['meta_info']


