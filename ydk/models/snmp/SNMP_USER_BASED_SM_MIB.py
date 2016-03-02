""" SNMP_USER_BASED_SM_MIB 


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum


class SNMPUSERBASEDSMMIB(object):
    """
    
    
    .. attribute:: usmstats
    
    	
    	**type**\: :py:class:`UsmStats <ydk.models.snmp.SNMP_USER_BASED_SM_MIB.SNMPUSERBASEDSMMIB.UsmStats>`
    
    .. attribute:: usmusertable
    
    	
    	**type**\: :py:class:`UsmUserTable <ydk.models.snmp.SNMP_USER_BASED_SM_MIB.SNMPUSERBASEDSMMIB.UsmUserTable>`
    
    

    """

    _prefix = 'SNMP_USER_BASED_SM_MIB'
    _revision = '2002-10-16'

    def __init__(self):
        self.usmstats = SNMPUSERBASEDSMMIB.UsmStats()
        self.usmstats.parent = self
        self.usmusertable = SNMPUSERBASEDSMMIB.UsmUserTable()
        self.usmusertable.parent = self


    class UsmStats(object):
        """
        
        
        .. attribute:: usmstatsdecryptionerrors
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: usmstatsnotintimewindows
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: usmstatsunknownengineids
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: usmstatsunknownusernames
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: usmstatsunsupportedseclevels
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: usmstatswrongdigests
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'SNMP_USER_BASED_SM_MIB'
        _revision = '2002-10-16'

        def __init__(self):
            self.parent = None
            self.usmstatsdecryptionerrors = None
            self.usmstatsnotintimewindows = None
            self.usmstatsunknownengineids = None
            self.usmstatsunknownusernames = None
            self.usmstatsunsupportedseclevels = None
            self.usmstatswrongdigests = None

        @property
        def _common_path(self):

            return '/SNMP-USER-BASED-SM-MIB:SNMP-USER-BASED-SM-MIB/SNMP-USER-BASED-SM-MIB:usmStats'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.usmstatsdecryptionerrors is not None:
                return True

            if self.usmstatsnotintimewindows is not None:
                return True

            if self.usmstatsunknownengineids is not None:
                return True

            if self.usmstatsunknownusernames is not None:
                return True

            if self.usmstatsunsupportedseclevels is not None:
                return True

            if self.usmstatswrongdigests is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.snmp._meta import _SNMP_USER_BASED_SM_MIB as meta
            return meta._meta_table['SNMPUSERBASEDSMMIB.UsmStats']['meta_info']


    class UsmUserTable(object):
        """
        
        
        .. attribute:: usmuserentry
        
        	
        	**type**\: list of :py:class:`UsmUserEntry <ydk.models.snmp.SNMP_USER_BASED_SM_MIB.SNMPUSERBASEDSMMIB.UsmUserTable.UsmUserEntry>`
        
        

        """

        _prefix = 'SNMP_USER_BASED_SM_MIB'
        _revision = '2002-10-16'

        def __init__(self):
            self.parent = None
            self.usmuserentry = YList()
            self.usmuserentry.parent = self
            self.usmuserentry.name = 'usmuserentry'


        class UsmUserEntry(object):
            """
            
            
            .. attribute:: usmuserengineid
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: usmusername
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: usmuserauthkey
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: usmuserauthkeychange
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: usmuserauthprotocol
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: usmuserclonefrom
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: usmuserownauthkeychange
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: usmuserownprivkeychange
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: usmuserprivkey
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: usmuserprivkeychange
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: usmuserprivprotocol
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: usmuserpublic
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: usmusersecurityname
            
            	
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: usmuserstoragetype
            
            	
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'SNMP_USER_BASED_SM_MIB'
            _revision = '2002-10-16'

            def __init__(self):
                self.parent = None
                self.usmuserengineid = None
                self.usmusername = None
                self.usmuserauthkey = None
                self.usmuserauthkeychange = None
                self.usmuserauthprotocol = None
                self.usmuserclonefrom = None
                self.usmuserownauthkeychange = None
                self.usmuserownprivkeychange = None
                self.usmuserprivkey = None
                self.usmuserprivkeychange = None
                self.usmuserprivprotocol = None
                self.usmuserpublic = None
                self.usmusersecurityname = None
                self.usmuserstoragetype = None

            @property
            def _common_path(self):
                if self.usmuserengineid is None:
                    raise YPYDataValidationError('Key property usmuserengineid is None')
                if self.usmusername is None:
                    raise YPYDataValidationError('Key property usmusername is None')

                return '/SNMP-USER-BASED-SM-MIB:SNMP-USER-BASED-SM-MIB/SNMP-USER-BASED-SM-MIB:usmUserTable/SNMP-USER-BASED-SM-MIB:usmUserEntry[SNMP-USER-BASED-SM-MIB:usmUserEngineID = ' + str(self.usmuserengineid) + '][SNMP-USER-BASED-SM-MIB:usmUserName = ' + str(self.usmusername) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.usmuserengineid is not None:
                    return True

                if self.usmusername is not None:
                    return True

                if self.usmuserauthkey is not None:
                    return True

                if self.usmuserauthkeychange is not None:
                    return True

                if self.usmuserauthprotocol is not None:
                    return True

                if self.usmuserclonefrom is not None:
                    return True

                if self.usmuserownauthkeychange is not None:
                    return True

                if self.usmuserownprivkeychange is not None:
                    return True

                if self.usmuserprivkey is not None:
                    return True

                if self.usmuserprivkeychange is not None:
                    return True

                if self.usmuserprivprotocol is not None:
                    return True

                if self.usmuserpublic is not None:
                    return True

                if self.usmusersecurityname is not None:
                    return True

                if self.usmuserstoragetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.snmp._meta import _SNMP_USER_BASED_SM_MIB as meta
                return meta._meta_table['SNMPUSERBASEDSMMIB.UsmUserTable.UsmUserEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SNMP-USER-BASED-SM-MIB:SNMP-USER-BASED-SM-MIB/SNMP-USER-BASED-SM-MIB:usmUserTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.usmuserentry is not None:
                for child_ref in self.usmuserentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.snmp._meta import _SNMP_USER_BASED_SM_MIB as meta
            return meta._meta_table['SNMPUSERBASEDSMMIB.UsmUserTable']['meta_info']

    @property
    def _common_path(self):

        return '/SNMP-USER-BASED-SM-MIB:SNMP-USER-BASED-SM-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.usmstats is not None and self.usmstats._has_data():
            return True

        if self.usmstats is not None and self.usmstats.is_presence():
            return True

        if self.usmusertable is not None and self.usmusertable._has_data():
            return True

        if self.usmusertable is not None and self.usmusertable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.snmp._meta import _SNMP_USER_BASED_SM_MIB as meta
        return meta._meta_table['SNMPUSERBASEDSMMIB']['meta_info']


