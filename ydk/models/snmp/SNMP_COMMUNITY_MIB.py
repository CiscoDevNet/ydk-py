""" SNMP_COMMUNITY_MIB 


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum


class SNMPCOMMUNITYMIB(object):
    """
    
    
    .. attribute:: snmpcommunitytable
    
    	
    	**type**\: :py:class:`SnmpCommunityTable <ydk.models.snmp.SNMP_COMMUNITY_MIB.SNMPCOMMUNITYMIB.SnmpCommunityTable>`
    
    

    """

    _prefix = 'SNMP_COMMUNITY_MIB'
    _revision = '2003-08-06'

    def __init__(self):
        self.snmpcommunitytable = SNMPCOMMUNITYMIB.SnmpCommunityTable()
        self.snmpcommunitytable.parent = self


    class SnmpCommunityTable(object):
        """
        
        
        .. attribute:: snmpcommunityentry
        
        	
        	**type**\: list of :py:class:`SnmpCommunityEntry <ydk.models.snmp.SNMP_COMMUNITY_MIB.SNMPCOMMUNITYMIB.SnmpCommunityTable.SnmpCommunityEntry>`
        
        

        """

        _prefix = 'SNMP_COMMUNITY_MIB'
        _revision = '2003-08-06'

        def __init__(self):
            self.parent = None
            self.snmpcommunityentry = YList()
            self.snmpcommunityentry.parent = self
            self.snmpcommunityentry.name = 'snmpcommunityentry'


        class SnmpCommunityEntry(object):
            """
            
            
            .. attribute:: snmpcommunityindex
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: snmpcommunitycontextengineid
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: snmpcommunitycontextname
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: snmpcommunityname
            
            	
            	**type**\: str
            
            .. attribute:: snmpcommunitysecurityname
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: snmpcommunitystoragetype
            
            	
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: snmpcommunitytransporttag
            
            	
            	**type**\: str
            
            	**range:** 0..255
            
            

            """

            _prefix = 'SNMP_COMMUNITY_MIB'
            _revision = '2003-08-06'

            def __init__(self):
                self.parent = None
                self.snmpcommunityindex = None
                self.snmpcommunitycontextengineid = None
                self.snmpcommunitycontextname = None
                self.snmpcommunityname = None
                self.snmpcommunitysecurityname = None
                self.snmpcommunitystoragetype = None
                self.snmpcommunitytransporttag = None

            @property
            def _common_path(self):
                if self.snmpcommunityindex is None:
                    raise YPYDataValidationError('Key property snmpcommunityindex is None')

                return '/SNMP-COMMUNITY-MIB:SNMP-COMMUNITY-MIB/SNMP-COMMUNITY-MIB:snmpCommunityTable/SNMP-COMMUNITY-MIB:snmpCommunityEntry[SNMP-COMMUNITY-MIB:snmpCommunityIndex = ' + str(self.snmpcommunityindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.snmpcommunityindex is not None:
                    return True

                if self.snmpcommunitycontextengineid is not None:
                    return True

                if self.snmpcommunitycontextname is not None:
                    return True

                if self.snmpcommunityname is not None:
                    return True

                if self.snmpcommunitysecurityname is not None:
                    return True

                if self.snmpcommunitystoragetype is not None:
                    return True

                if self.snmpcommunitytransporttag is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.snmp._meta import _SNMP_COMMUNITY_MIB as meta
                return meta._meta_table['SNMPCOMMUNITYMIB.SnmpCommunityTable.SnmpCommunityEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SNMP-COMMUNITY-MIB:SNMP-COMMUNITY-MIB/SNMP-COMMUNITY-MIB:snmpCommunityTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.snmpcommunityentry is not None:
                for child_ref in self.snmpcommunityentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.snmp._meta import _SNMP_COMMUNITY_MIB as meta
            return meta._meta_table['SNMPCOMMUNITYMIB.SnmpCommunityTable']['meta_info']

    @property
    def _common_path(self):

        return '/SNMP-COMMUNITY-MIB:SNMP-COMMUNITY-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.snmpcommunitytable is not None and self.snmpcommunitytable._has_data():
            return True

        if self.snmpcommunitytable is not None and self.snmpcommunitytable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.snmp._meta import _SNMP_COMMUNITY_MIB as meta
        return meta._meta_table['SNMPCOMMUNITYMIB']['meta_info']


