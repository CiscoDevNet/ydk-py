""" SNMP_TARGET_MIB 


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmp.SNMP_FRAMEWORK_MIB import SnmpSecurityLevel_Enum
from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum


class SNMPTARGETMIB(object):
    """
    
    
    .. attribute:: snmptargetaddrtable
    
    	
    	**type**\: :py:class:`SnmpTargetAddrTable <ydk.models.snmp.SNMP_TARGET_MIB.SNMPTARGETMIB.SnmpTargetAddrTable>`
    
    .. attribute:: snmptargetobjects
    
    	
    	**type**\: :py:class:`SnmpTargetObjects <ydk.models.snmp.SNMP_TARGET_MIB.SNMPTARGETMIB.SnmpTargetObjects>`
    
    .. attribute:: snmptargetparamstable
    
    	
    	**type**\: :py:class:`SnmpTargetParamsTable <ydk.models.snmp.SNMP_TARGET_MIB.SNMPTARGETMIB.SnmpTargetParamsTable>`
    
    

    """

    _prefix = 'SNMP_TARGET_MIB'
    _revision = '2002-10-14'

    def __init__(self):
        self.snmptargetaddrtable = SNMPTARGETMIB.SnmpTargetAddrTable()
        self.snmptargetaddrtable.parent = self
        self.snmptargetobjects = SNMPTARGETMIB.SnmpTargetObjects()
        self.snmptargetobjects.parent = self
        self.snmptargetparamstable = SNMPTARGETMIB.SnmpTargetParamsTable()
        self.snmptargetparamstable.parent = self


    class SnmpTargetAddrTable(object):
        """
        
        
        .. attribute:: snmptargetaddrentry
        
        	
        	**type**\: list of :py:class:`SnmpTargetAddrEntry <ydk.models.snmp.SNMP_TARGET_MIB.SNMPTARGETMIB.SnmpTargetAddrTable.SnmpTargetAddrEntry>`
        
        

        """

        _prefix = 'SNMP_TARGET_MIB'
        _revision = '2002-10-14'

        def __init__(self):
            self.parent = None
            self.snmptargetaddrentry = YList()
            self.snmptargetaddrentry.parent = self
            self.snmptargetaddrentry.name = 'snmptargetaddrentry'


        class SnmpTargetAddrEntry(object):
            """
            
            
            .. attribute:: snmptargetaddrname
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: enabled
            
            	
            	**type**\: bool
            
            .. attribute:: snmptargetaddrengineid
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: snmptargetaddrmms
            
            	
            	**type**\: int
            
            	**range:** 0 \| 484..2147483647
            
            .. attribute:: snmptargetaddrparams
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: snmptargetaddrretrycount
            
            	
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: snmptargetaddrstoragetype
            
            	
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: snmptargetaddrtaddress
            
            	
            	**type**\: one of { str | str }
            
            .. attribute:: snmptargetaddrtaglist
            
            	
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: snmptargetaddrtdomain
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: snmptargetaddrtimeout
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: snmptargetaddrtmask
            
            	
            	**type**\: one of { one of { str | str } | str }
            
            

            """

            _prefix = 'SNMP_TARGET_MIB'
            _revision = '2002-10-14'

            def __init__(self):
                self.parent = None
                self.snmptargetaddrname = None
                self.enabled = None
                self.snmptargetaddrengineid = None
                self.snmptargetaddrmms = None
                self.snmptargetaddrparams = None
                self.snmptargetaddrretrycount = None
                self.snmptargetaddrstoragetype = None
                self.snmptargetaddrtaddress = None
                self.snmptargetaddrtaglist = None
                self.snmptargetaddrtdomain = None
                self.snmptargetaddrtimeout = None
                self.snmptargetaddrtmask = None

            @property
            def _common_path(self):
                if self.snmptargetaddrname is None:
                    raise YPYDataValidationError('Key property snmptargetaddrname is None')

                return '/SNMP-TARGET-MIB:SNMP-TARGET-MIB/SNMP-TARGET-MIB:snmpTargetAddrTable/SNMP-TARGET-MIB:snmpTargetAddrEntry[SNMP-TARGET-MIB:snmpTargetAddrName = ' + str(self.snmptargetaddrname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.snmptargetaddrname is not None:
                    return True

                if self.enabled is not None:
                    return True

                if self.snmptargetaddrengineid is not None:
                    return True

                if self.snmptargetaddrmms is not None:
                    return True

                if self.snmptargetaddrparams is not None:
                    return True

                if self.snmptargetaddrretrycount is not None:
                    return True

                if self.snmptargetaddrstoragetype is not None:
                    return True

                if self.snmptargetaddrtaddress is not None:
                    return True

                if self.snmptargetaddrtaglist is not None:
                    return True

                if self.snmptargetaddrtdomain is not None:
                    return True

                if self.snmptargetaddrtimeout is not None:
                    return True

                if self.snmptargetaddrtmask is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.snmp._meta import _SNMP_TARGET_MIB as meta
                return meta._meta_table['SNMPTARGETMIB.SnmpTargetAddrTable.SnmpTargetAddrEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SNMP-TARGET-MIB:SNMP-TARGET-MIB/SNMP-TARGET-MIB:snmpTargetAddrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.snmptargetaddrentry is not None:
                for child_ref in self.snmptargetaddrentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.snmp._meta import _SNMP_TARGET_MIB as meta
            return meta._meta_table['SNMPTARGETMIB.SnmpTargetAddrTable']['meta_info']


    class SnmpTargetObjects(object):
        """
        
        
        .. attribute:: snmpunavailablecontexts
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpunknowncontexts
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'SNMP_TARGET_MIB'
        _revision = '2002-10-14'

        def __init__(self):
            self.parent = None
            self.snmpunavailablecontexts = None
            self.snmpunknowncontexts = None

        @property
        def _common_path(self):

            return '/SNMP-TARGET-MIB:SNMP-TARGET-MIB/SNMP-TARGET-MIB:snmpTargetObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.snmpunavailablecontexts is not None:
                return True

            if self.snmpunknowncontexts is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.snmp._meta import _SNMP_TARGET_MIB as meta
            return meta._meta_table['SNMPTARGETMIB.SnmpTargetObjects']['meta_info']


    class SnmpTargetParamsTable(object):
        """
        
        
        .. attribute:: snmptargetparamsentry
        
        	
        	**type**\: list of :py:class:`SnmpTargetParamsEntry <ydk.models.snmp.SNMP_TARGET_MIB.SNMPTARGETMIB.SnmpTargetParamsTable.SnmpTargetParamsEntry>`
        
        

        """

        _prefix = 'SNMP_TARGET_MIB'
        _revision = '2002-10-14'

        def __init__(self):
            self.parent = None
            self.snmptargetparamsentry = YList()
            self.snmptargetparamsentry.parent = self
            self.snmptargetparamsentry.name = 'snmptargetparamsentry'


        class SnmpTargetParamsEntry(object):
            """
            
            
            .. attribute:: snmptargetparamsname
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: snmptargetparamsmpmodel
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: snmptargetparamssecuritylevel
            
            	
            	**type**\: :py:class:`SnmpSecurityLevel_Enum <ydk.models.snmp.SNMP_FRAMEWORK_MIB.SnmpSecurityLevel_Enum>`
            
            .. attribute:: snmptargetparamssecuritymodel
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: snmptargetparamssecurityname
            
            	
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: snmptargetparamsstoragetype
            
            	
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'SNMP_TARGET_MIB'
            _revision = '2002-10-14'

            def __init__(self):
                self.parent = None
                self.snmptargetparamsname = None
                self.snmptargetparamsmpmodel = None
                self.snmptargetparamssecuritylevel = None
                self.snmptargetparamssecuritymodel = None
                self.snmptargetparamssecurityname = None
                self.snmptargetparamsstoragetype = None

            @property
            def _common_path(self):
                if self.snmptargetparamsname is None:
                    raise YPYDataValidationError('Key property snmptargetparamsname is None')

                return '/SNMP-TARGET-MIB:SNMP-TARGET-MIB/SNMP-TARGET-MIB:snmpTargetParamsTable/SNMP-TARGET-MIB:snmpTargetParamsEntry[SNMP-TARGET-MIB:snmpTargetParamsName = ' + str(self.snmptargetparamsname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.snmptargetparamsname is not None:
                    return True

                if self.snmptargetparamsmpmodel is not None:
                    return True

                if self.snmptargetparamssecuritylevel is not None:
                    return True

                if self.snmptargetparamssecuritymodel is not None:
                    return True

                if self.snmptargetparamssecurityname is not None:
                    return True

                if self.snmptargetparamsstoragetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.snmp._meta import _SNMP_TARGET_MIB as meta
                return meta._meta_table['SNMPTARGETMIB.SnmpTargetParamsTable.SnmpTargetParamsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SNMP-TARGET-MIB:SNMP-TARGET-MIB/SNMP-TARGET-MIB:snmpTargetParamsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.snmptargetparamsentry is not None:
                for child_ref in self.snmptargetparamsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.snmp._meta import _SNMP_TARGET_MIB as meta
            return meta._meta_table['SNMPTARGETMIB.SnmpTargetParamsTable']['meta_info']

    @property
    def _common_path(self):

        return '/SNMP-TARGET-MIB:SNMP-TARGET-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.snmptargetaddrtable is not None and self.snmptargetaddrtable._has_data():
            return True

        if self.snmptargetaddrtable is not None and self.snmptargetaddrtable.is_presence():
            return True

        if self.snmptargetobjects is not None and self.snmptargetobjects._has_data():
            return True

        if self.snmptargetobjects is not None and self.snmptargetobjects.is_presence():
            return True

        if self.snmptargetparamstable is not None and self.snmptargetparamstable._has_data():
            return True

        if self.snmptargetparamstable is not None and self.snmptargetparamstable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.snmp._meta import _SNMP_TARGET_MIB as meta
        return meta._meta_table['SNMPTARGETMIB']['meta_info']


