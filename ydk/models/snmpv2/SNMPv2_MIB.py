""" SNMPv2_MIB 


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class SnmpEnableAuthenTrapsType_Enum(Enum):
    """
    SnmpEnableAuthenTrapsType_Enum

    """

    ENABLED = 1

    DISABLED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.snmpv2._meta import _SNMPv2_MIB as meta
        return meta._meta_table['SnmpEnableAuthenTrapsType_Enum']



class SNMPv2MIB(object):
    """
    
    
    .. attribute:: snmp
    
    	
    	**type**\: :py:class:`Snmp <ydk.models.snmpv2.SNMPv2_MIB.SNMPv2MIB.Snmp>`
    
    .. attribute:: snmpset
    
    	
    	**type**\: :py:class:`SnmpSet <ydk.models.snmpv2.SNMPv2_MIB.SNMPv2MIB.SnmpSet>`
    
    .. attribute:: sysortable
    
    	
    	**type**\: :py:class:`SysORTable <ydk.models.snmpv2.SNMPv2_MIB.SNMPv2MIB.SysORTable>`
    
    .. attribute:: system
    
    	
    	**type**\: :py:class:`System <ydk.models.snmpv2.SNMPv2_MIB.SNMPv2MIB.System>`
    
    

    """

    _prefix = 'SNMPv2_MIB'
    _revision = '2002-10-16'

    def __init__(self):
        self.snmp = SNMPv2MIB.Snmp()
        self.snmp.parent = self
        self.snmpset = SNMPv2MIB.SnmpSet()
        self.snmpset.parent = self
        self.sysortable = SNMPv2MIB.SysORTable()
        self.sysortable.parent = self
        self.system = SNMPv2MIB.System()
        self.system.parent = self


    class Snmp(object):
        """
        
        
        .. attribute:: snmpenableauthentraps
        
        	
        	**type**\: :py:class:`SnmpEnableAuthenTrapsType_Enum <ydk.models.snmpv2.SNMPv2_MIB.SnmpEnableAuthenTrapsType_Enum>`
        
        .. attribute:: snmpinasnparseerrs
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadcommunitynames
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadcommunityuses
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadversions
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinpkts
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpproxydrops
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpsilentdrops
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'SNMPv2_MIB'
        _revision = '2002-10-16'

        def __init__(self):
            self.parent = None
            self.snmpenableauthentraps = None
            self.snmpinasnparseerrs = None
            self.snmpinbadcommunitynames = None
            self.snmpinbadcommunityuses = None
            self.snmpinbadversions = None
            self.snmpinpkts = None
            self.snmpproxydrops = None
            self.snmpsilentdrops = None

        @property
        def _common_path(self):

            return '/SNMPv2-MIB:SNMPv2-MIB/SNMPv2-MIB:snmp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.snmpenableauthentraps is not None:
                return True

            if self.snmpinasnparseerrs is not None:
                return True

            if self.snmpinbadcommunitynames is not None:
                return True

            if self.snmpinbadcommunityuses is not None:
                return True

            if self.snmpinbadversions is not None:
                return True

            if self.snmpinpkts is not None:
                return True

            if self.snmpproxydrops is not None:
                return True

            if self.snmpsilentdrops is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.snmpv2._meta import _SNMPv2_MIB as meta
            return meta._meta_table['SNMPv2MIB.Snmp']['meta_info']


    class SnmpSet(object):
        """
        
        
        .. attribute:: snmpsetserialno
        
        	
        	**type**\: int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'SNMPv2_MIB'
        _revision = '2002-10-16'

        def __init__(self):
            self.parent = None
            self.snmpsetserialno = None

        @property
        def _common_path(self):

            return '/SNMPv2-MIB:SNMPv2-MIB/SNMPv2-MIB:snmpSet'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.snmpsetserialno is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.snmpv2._meta import _SNMPv2_MIB as meta
            return meta._meta_table['SNMPv2MIB.SnmpSet']['meta_info']


    class SysORTable(object):
        """
        
        
        .. attribute:: sysorentry
        
        	
        	**type**\: list of :py:class:`SysOREntry <ydk.models.snmpv2.SNMPv2_MIB.SNMPv2MIB.SysORTable.SysOREntry>`
        
        

        """

        _prefix = 'SNMPv2_MIB'
        _revision = '2002-10-16'

        def __init__(self):
            self.parent = None
            self.sysorentry = YList()
            self.sysorentry.parent = self
            self.sysorentry.name = 'sysorentry'


        class SysOREntry(object):
            """
            
            
            .. attribute:: sysorindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: sysordescr
            
            	
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: sysorid
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: sysoruptime
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'SNMPv2_MIB'
            _revision = '2002-10-16'

            def __init__(self):
                self.parent = None
                self.sysorindex = None
                self.sysordescr = None
                self.sysorid = None
                self.sysoruptime = None

            @property
            def _common_path(self):
                if self.sysorindex is None:
                    raise YPYDataValidationError('Key property sysorindex is None')

                return '/SNMPv2-MIB:SNMPv2-MIB/SNMPv2-MIB:sysORTable/SNMPv2-MIB:sysOREntry[SNMPv2-MIB:sysORIndex = ' + str(self.sysorindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.sysorindex is not None:
                    return True

                if self.sysordescr is not None:
                    return True

                if self.sysorid is not None:
                    return True

                if self.sysoruptime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.snmpv2._meta import _SNMPv2_MIB as meta
                return meta._meta_table['SNMPv2MIB.SysORTable.SysOREntry']['meta_info']

        @property
        def _common_path(self):

            return '/SNMPv2-MIB:SNMPv2-MIB/SNMPv2-MIB:sysORTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sysorentry is not None:
                for child_ref in self.sysorentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.snmpv2._meta import _SNMPv2_MIB as meta
            return meta._meta_table['SNMPv2MIB.SysORTable']['meta_info']


    class System(object):
        """
        
        
        .. attribute:: syscontact
        
        	
        	**type**\: str
        
        	**pattern:** \\p{IsBasicLatin}{0,255}
        
        .. attribute:: sysdescr
        
        	
        	**type**\: str
        
        	**pattern:** \\p{IsBasicLatin}{0,255}
        
        .. attribute:: syslocation
        
        	
        	**type**\: str
        
        	**pattern:** \\p{IsBasicLatin}{0,255}
        
        .. attribute:: sysname
        
        	
        	**type**\: str
        
        	**pattern:** \\p{IsBasicLatin}{0,255}
        
        .. attribute:: sysobjectid
        
        	
        	**type**\: str
        
        	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
        
        .. attribute:: sysorlastchange
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: sysservices
        
        	
        	**type**\: int
        
        	**range:** 0..127
        
        .. attribute:: sysuptime
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'SNMPv2_MIB'
        _revision = '2002-10-16'

        def __init__(self):
            self.parent = None
            self.syscontact = None
            self.sysdescr = None
            self.syslocation = None
            self.sysname = None
            self.sysobjectid = None
            self.sysorlastchange = None
            self.sysservices = None
            self.sysuptime = None

        @property
        def _common_path(self):

            return '/SNMPv2-MIB:SNMPv2-MIB/SNMPv2-MIB:system'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.syscontact is not None:
                return True

            if self.sysdescr is not None:
                return True

            if self.syslocation is not None:
                return True

            if self.sysname is not None:
                return True

            if self.sysobjectid is not None:
                return True

            if self.sysorlastchange is not None:
                return True

            if self.sysservices is not None:
                return True

            if self.sysuptime is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.snmpv2._meta import _SNMPv2_MIB as meta
            return meta._meta_table['SNMPv2MIB.System']['meta_info']

    @property
    def _common_path(self):

        return '/SNMPv2-MIB:SNMPv2-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.snmp is not None and self.snmp._has_data():
            return True

        if self.snmp is not None and self.snmp.is_presence():
            return True

        if self.snmpset is not None and self.snmpset._has_data():
            return True

        if self.snmpset is not None and self.snmpset.is_presence():
            return True

        if self.sysortable is not None and self.sysortable._has_data():
            return True

        if self.sysortable is not None and self.sysortable.is_presence():
            return True

        if self.system is not None and self.system._has_data():
            return True

        if self.system is not None and self.system.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.snmpv2._meta import _SNMPv2_MIB as meta
        return meta._meta_table['SNMPv2MIB']['meta_info']


