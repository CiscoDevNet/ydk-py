""" SNMP_MPD_MIB 


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class SNMPMPDMIB(object):
    """
    
    
    .. attribute:: snmpmpdstats
    
    	
    	**type**\: :py:class:`SnmpMPDStats <ydk.models.snmp.SNMP_MPD_MIB.SNMPMPDMIB.SnmpMPDStats>`
    
    

    """

    _prefix = 'SNMP_MPD_MIB'
    _revision = '2002-10-14'

    def __init__(self):
        self.snmpmpdstats = SNMPMPDMIB.SnmpMPDStats()
        self.snmpmpdstats.parent = self


    class SnmpMPDStats(object):
        """
        
        
        .. attribute:: snmpinvalidmsgs
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpunknownpduhandlers
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpunknownsecuritymodels
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'SNMP_MPD_MIB'
        _revision = '2002-10-14'

        def __init__(self):
            self.parent = None
            self.snmpinvalidmsgs = None
            self.snmpunknownpduhandlers = None
            self.snmpunknownsecuritymodels = None

        @property
        def _common_path(self):

            return '/SNMP-MPD-MIB:SNMP-MPD-MIB/SNMP-MPD-MIB:snmpMPDStats'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.snmpinvalidmsgs is not None:
                return True

            if self.snmpunknownpduhandlers is not None:
                return True

            if self.snmpunknownsecuritymodels is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.snmp._meta import _SNMP_MPD_MIB as meta
            return meta._meta_table['SNMPMPDMIB.SnmpMPDStats']['meta_info']

    @property
    def _common_path(self):

        return '/SNMP-MPD-MIB:SNMP-MPD-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.snmpmpdstats is not None and self.snmpmpdstats._has_data():
            return True

        if self.snmpmpdstats is not None and self.snmpmpdstats.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.snmp._meta import _SNMP_MPD_MIB as meta
        return meta._meta_table['SNMPMPDMIB']['meta_info']


