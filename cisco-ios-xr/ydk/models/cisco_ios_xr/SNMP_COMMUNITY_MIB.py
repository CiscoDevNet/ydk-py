""" SNMP_COMMUNITY_MIB 


"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class SNMPCOMMUNITYMIB(_Entity_):
    """
    
    
    .. attribute:: snmpcommunitytable
    
    	
    	**type**\:  :py:class:`SnmpCommunityTable <ydk.models.cisco_ios_xr.SNMP_COMMUNITY_MIB.SNMPCOMMUNITYMIB.SnmpCommunityTable>`
    
    

    """

    _prefix = 'SNMP_COMMUNITY_MIB'
    _revision = '2003-08-06'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(SNMPCOMMUNITYMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "SNMP-COMMUNITY-MIB"
        self.yang_parent_name = "SNMP-COMMUNITY-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("snmpCommunityTable", ("snmpcommunitytable", SNMPCOMMUNITYMIB.SnmpCommunityTable))])
        self._leafs = OrderedDict()

        self.snmpcommunitytable = SNMPCOMMUNITYMIB.SnmpCommunityTable()
        self.snmpcommunitytable.parent = self
        self._children_name_map["snmpcommunitytable"] = "snmpCommunityTable"
        self._segment_path = lambda: "SNMP-COMMUNITY-MIB:SNMP-COMMUNITY-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SNMPCOMMUNITYMIB, [], name, value)


    class SnmpCommunityTable(_Entity_):
        """
        
        
        .. attribute:: snmpcommunityentry
        
        	
        	**type**\: list of  		 :py:class:`SnmpCommunityEntry <ydk.models.cisco_ios_xr.SNMP_COMMUNITY_MIB.SNMPCOMMUNITYMIB.SnmpCommunityTable.SnmpCommunityEntry>`
        
        

        """

        _prefix = 'SNMP_COMMUNITY_MIB'
        _revision = '2003-08-06'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SNMPCOMMUNITYMIB.SnmpCommunityTable, self).__init__()

            self.yang_name = "snmpCommunityTable"
            self.yang_parent_name = "SNMP-COMMUNITY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("snmpCommunityEntry", ("snmpcommunityentry", SNMPCOMMUNITYMIB.SnmpCommunityTable.SnmpCommunityEntry))])
            self._leafs = OrderedDict()

            self.snmpcommunityentry = YList(self)
            self._segment_path = lambda: "snmpCommunityTable"
            self._absolute_path = lambda: "SNMP-COMMUNITY-MIB:SNMP-COMMUNITY-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPCOMMUNITYMIB.SnmpCommunityTable, [], name, value)


        class SnmpCommunityEntry(_Entity_):
            """
            
            
            .. attribute:: snmpcommunityindex  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: snmpcommunityname
            
            	
            	**type**\: str
            
            	**mandatory**\: True
            
            .. attribute:: snmpcommunitysecurityname
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**mandatory**\: True
            
            .. attribute:: snmpcommunitycontextengineid
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            	**mandatory**\: True
            
            .. attribute:: snmpcommunitycontextname
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: snmpcommunitytransporttag
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: snmpcommunitystoragetype
            
            	
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xr.SNMPv2_TC.StorageType>`
            
            	**default value**\: permanent
            
            

            """

            _prefix = 'SNMP_COMMUNITY_MIB'
            _revision = '2003-08-06'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(SNMPCOMMUNITYMIB.SnmpCommunityTable.SnmpCommunityEntry, self).__init__()

                self.yang_name = "snmpCommunityEntry"
                self.yang_parent_name = "snmpCommunityTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['snmpcommunityindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('snmpcommunityindex', (YLeaf(YType.str, 'snmpCommunityIndex'), ['str'])),
                    ('snmpcommunityname', (YLeaf(YType.str, 'snmpCommunityName'), ['str'])),
                    ('snmpcommunitysecurityname', (YLeaf(YType.str, 'snmpCommunitySecurityName'), ['str'])),
                    ('snmpcommunitycontextengineid', (YLeaf(YType.str, 'snmpCommunityContextEngineID'), ['str'])),
                    ('snmpcommunitycontextname', (YLeaf(YType.str, 'snmpCommunityContextName'), ['str'])),
                    ('snmpcommunitytransporttag', (YLeaf(YType.str, 'snmpCommunityTransportTag'), ['str'])),
                    ('snmpcommunitystoragetype', (YLeaf(YType.enumeration, 'snmpCommunityStorageType'), [('ydk.models.cisco_ios_xr.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.snmpcommunityindex = None
                self.snmpcommunityname = None
                self.snmpcommunitysecurityname = None
                self.snmpcommunitycontextengineid = None
                self.snmpcommunitycontextname = None
                self.snmpcommunitytransporttag = None
                self.snmpcommunitystoragetype = None
                self._segment_path = lambda: "snmpCommunityEntry" + "[snmpCommunityIndex='" + str(self.snmpcommunityindex) + "']"
                self._absolute_path = lambda: "SNMP-COMMUNITY-MIB:SNMP-COMMUNITY-MIB/snmpCommunityTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SNMPCOMMUNITYMIB.SnmpCommunityTable.SnmpCommunityEntry, ['snmpcommunityindex', 'snmpcommunityname', 'snmpcommunitysecurityname', 'snmpcommunitycontextengineid', 'snmpcommunitycontextname', 'snmpcommunitytransporttag', 'snmpcommunitystoragetype'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _SNMP_COMMUNITY_MIB as meta
                return meta._meta_table['SNMPCOMMUNITYMIB.SnmpCommunityTable.SnmpCommunityEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _SNMP_COMMUNITY_MIB as meta
            return meta._meta_table['SNMPCOMMUNITYMIB.SnmpCommunityTable']['meta_info']

    def clone_ptr(self):
        self._top_entity = SNMPCOMMUNITYMIB()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _SNMP_COMMUNITY_MIB as meta
        return meta._meta_table['SNMPCOMMUNITYMIB']['meta_info']


