""" Cisco_IOS_XR_sysadmin_entity_mib 

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

Copyright(c) 2015\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class PhysicalClass(Enum):
    """
    PhysicalClass (Enum Class)

    .. data:: other = 1

    .. data:: unknown = 2

    .. data:: chassis = 3

    .. data:: backplane = 4

    .. data:: container = 5

    .. data:: powerSupply = 6

    .. data:: fan = 7

    .. data:: sensor = 8

    .. data:: module = 9

    .. data:: port = 10

    .. data:: stack = 11

    """

    other = Enum.YLeaf(1, "other")

    unknown = Enum.YLeaf(2, "unknown")

    chassis = Enum.YLeaf(3, "chassis")

    backplane = Enum.YLeaf(4, "backplane")

    container = Enum.YLeaf(5, "container")

    powerSupply = Enum.YLeaf(6, "powerSupply")

    fan = Enum.YLeaf(7, "fan")

    sensor = Enum.YLeaf(8, "sensor")

    module = Enum.YLeaf(9, "module")

    port = Enum.YLeaf(10, "port")

    stack = Enum.YLeaf(11, "stack")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_mib as meta
        return meta._meta_table['PhysicalClass']



class ENTITYMIB(_Entity_):
    """
    
    
    .. attribute:: entitygeneral
    
    	
    	**type**\:  :py:class:`EntityGeneral <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.EntityGeneral>`
    
    	**config**\: False
    
    .. attribute:: entphysicaltable
    
    	
    	**type**\:  :py:class:`EntPhysicalTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.EntPhysicalTable>`
    
    	**config**\: False
    
    .. attribute:: entlogicaltable
    
    	
    	**type**\:  :py:class:`EntLogicalTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.EntLogicalTable>`
    
    	**config**\: False
    
    .. attribute:: entlpmappingtable
    
    	
    	**type**\:  :py:class:`EntLPMappingTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.EntLPMappingTable>`
    
    	**config**\: False
    
    .. attribute:: entaliasmappingtable
    
    	
    	**type**\:  :py:class:`EntAliasMappingTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.EntAliasMappingTable>`
    
    	**config**\: False
    
    .. attribute:: entphysicalcontainstable
    
    	
    	**type**\:  :py:class:`EntPhysicalContainsTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.EntPhysicalContainsTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'ENTITY_MIB'
    _revision = '2017-04-12'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(ENTITYMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "ENTITY-MIB"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-entity-mib"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("entityGeneral", ("entitygeneral", ENTITYMIB.EntityGeneral)), ("entPhysicalTable", ("entphysicaltable", ENTITYMIB.EntPhysicalTable)), ("entLogicalTable", ("entlogicaltable", ENTITYMIB.EntLogicalTable)), ("entLPMappingTable", ("entlpmappingtable", ENTITYMIB.EntLPMappingTable)), ("entAliasMappingTable", ("entaliasmappingtable", ENTITYMIB.EntAliasMappingTable)), ("entPhysicalContainsTable", ("entphysicalcontainstable", ENTITYMIB.EntPhysicalContainsTable))])
        self._leafs = OrderedDict()

        self.entitygeneral = ENTITYMIB.EntityGeneral()
        self.entitygeneral.parent = self
        self._children_name_map["entitygeneral"] = "entityGeneral"

        self.entphysicaltable = ENTITYMIB.EntPhysicalTable()
        self.entphysicaltable.parent = self
        self._children_name_map["entphysicaltable"] = "entPhysicalTable"

        self.entlogicaltable = ENTITYMIB.EntLogicalTable()
        self.entlogicaltable.parent = self
        self._children_name_map["entlogicaltable"] = "entLogicalTable"

        self.entlpmappingtable = ENTITYMIB.EntLPMappingTable()
        self.entlpmappingtable.parent = self
        self._children_name_map["entlpmappingtable"] = "entLPMappingTable"

        self.entaliasmappingtable = ENTITYMIB.EntAliasMappingTable()
        self.entaliasmappingtable.parent = self
        self._children_name_map["entaliasmappingtable"] = "entAliasMappingTable"

        self.entphysicalcontainstable = ENTITYMIB.EntPhysicalContainsTable()
        self.entphysicalcontainstable.parent = self
        self._children_name_map["entphysicalcontainstable"] = "entPhysicalContainsTable"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ENTITYMIB, [], name, value)


    class EntityGeneral(_Entity_):
        """
        
        
        .. attribute:: entlastchangetime
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'ENTITY_MIB'
        _revision = '2017-04-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ENTITYMIB.EntityGeneral, self).__init__()

            self.yang_name = "entityGeneral"
            self.yang_parent_name = "ENTITY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('entlastchangetime', (YLeaf(YType.uint32, 'entLastChangeTime'), ['int'])),
            ])
            self.entlastchangetime = None
            self._segment_path = lambda: "entityGeneral"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYMIB.EntityGeneral, ['entlastchangetime'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_mib as meta
            return meta._meta_table['ENTITYMIB.EntityGeneral']['meta_info']


    class EntPhysicalTable(_Entity_):
        """
        
        
        .. attribute:: entphysicalentry
        
        	
        	**type**\: list of  		 :py:class:`EntPhysicalEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ENTITY_MIB'
        _revision = '2017-04-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ENTITYMIB.EntPhysicalTable, self).__init__()

            self.yang_name = "entPhysicalTable"
            self.yang_parent_name = "ENTITY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("entPhysicalEntry", ("entphysicalentry", ENTITYMIB.EntPhysicalTable.EntPhysicalEntry))])
            self._leafs = OrderedDict()

            self.entphysicalentry = YList(self)
            self._segment_path = lambda: "entPhysicalTable"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYMIB.EntPhysicalTable, [], name, value)


        class EntPhysicalEntry(_Entity_):
            """
            
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: entphysicaldescr
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: entphysicalvendortype
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: entphysicalcontainedin
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: entphysicalclass
            
            	
            	**type**\:  :py:class:`PhysicalClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.PhysicalClass>`
            
            	**config**\: False
            
            .. attribute:: entphysicalparentrelpos
            
            	
            	**type**\: int
            
            	**range:** \-1..2147483647
            
            	**config**\: False
            
            .. attribute:: entphysicalname
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: entphysicalhardwarerev
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: entphysicalfirmwarerev
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: entphysicalsoftwarerev
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: entphysicalserialnum
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: entphysicalmfgname
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: entphysicalmodelname
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: entphysicalalias
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: entphysicalassetid
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: entphysicalisfru
            
            	
            	**type**\:  :py:class:`TruthValue <ydk.models.cisco_ios_xr.SNMPv2_TC.TruthValue>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ENTITY_MIB'
            _revision = '2017-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ENTITYMIB.EntPhysicalTable.EntPhysicalEntry, self).__init__()

                self.yang_name = "entPhysicalEntry"
                self.yang_parent_name = "entPhysicalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.int32, 'entPhysicalIndex'), ['int'])),
                    ('entphysicaldescr', (YLeaf(YType.str, 'entPhysicalDescr'), ['str'])),
                    ('entphysicalvendortype', (YLeaf(YType.str, 'entPhysicalVendorType'), ['str'])),
                    ('entphysicalcontainedin', (YLeaf(YType.int32, 'entPhysicalContainedIn'), ['int'])),
                    ('entphysicalclass', (YLeaf(YType.enumeration, 'entPhysicalClass'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib', 'PhysicalClass', '')])),
                    ('entphysicalparentrelpos', (YLeaf(YType.int32, 'entPhysicalParentRelPos'), ['int'])),
                    ('entphysicalname', (YLeaf(YType.str, 'entPhysicalName'), ['str'])),
                    ('entphysicalhardwarerev', (YLeaf(YType.str, 'entPhysicalHardwareRev'), ['str'])),
                    ('entphysicalfirmwarerev', (YLeaf(YType.str, 'entPhysicalFirmwareRev'), ['str'])),
                    ('entphysicalsoftwarerev', (YLeaf(YType.str, 'entPhysicalSoftwareRev'), ['str'])),
                    ('entphysicalserialnum', (YLeaf(YType.str, 'entPhysicalSerialNum'), ['str'])),
                    ('entphysicalmfgname', (YLeaf(YType.str, 'entPhysicalMfgName'), ['str'])),
                    ('entphysicalmodelname', (YLeaf(YType.str, 'entPhysicalModelName'), ['str'])),
                    ('entphysicalalias', (YLeaf(YType.str, 'entPhysicalAlias'), ['str'])),
                    ('entphysicalassetid', (YLeaf(YType.str, 'entPhysicalAssetID'), ['str'])),
                    ('entphysicalisfru', (YLeaf(YType.enumeration, 'entPhysicalIsFRU'), [('ydk.models.cisco_ios_xr.SNMPv2_TC', 'TruthValue', '')])),
                ])
                self.entphysicalindex = None
                self.entphysicaldescr = None
                self.entphysicalvendortype = None
                self.entphysicalcontainedin = None
                self.entphysicalclass = None
                self.entphysicalparentrelpos = None
                self.entphysicalname = None
                self.entphysicalhardwarerev = None
                self.entphysicalfirmwarerev = None
                self.entphysicalsoftwarerev = None
                self.entphysicalserialnum = None
                self.entphysicalmfgname = None
                self.entphysicalmodelname = None
                self.entphysicalalias = None
                self.entphysicalassetid = None
                self.entphysicalisfru = None
                self._segment_path = lambda: "entPhysicalEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/entPhysicalTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ENTITYMIB.EntPhysicalTable.EntPhysicalEntry, ['entphysicalindex', 'entphysicaldescr', 'entphysicalvendortype', 'entphysicalcontainedin', 'entphysicalclass', 'entphysicalparentrelpos', 'entphysicalname', 'entphysicalhardwarerev', 'entphysicalfirmwarerev', 'entphysicalsoftwarerev', 'entphysicalserialnum', 'entphysicalmfgname', 'entphysicalmodelname', 'entphysicalalias', 'entphysicalassetid', 'entphysicalisfru'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_mib as meta
                return meta._meta_table['ENTITYMIB.EntPhysicalTable.EntPhysicalEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_mib as meta
            return meta._meta_table['ENTITYMIB.EntPhysicalTable']['meta_info']


    class EntLogicalTable(_Entity_):
        """
        
        
        .. attribute:: entlogicalentry
        
        	
        	**type**\: list of  		 :py:class:`EntLogicalEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.EntLogicalTable.EntLogicalEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ENTITY_MIB'
        _revision = '2017-04-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ENTITYMIB.EntLogicalTable, self).__init__()

            self.yang_name = "entLogicalTable"
            self.yang_parent_name = "ENTITY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("entLogicalEntry", ("entlogicalentry", ENTITYMIB.EntLogicalTable.EntLogicalEntry))])
            self._leafs = OrderedDict()

            self.entlogicalentry = YList(self)
            self._segment_path = lambda: "entLogicalTable"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYMIB.EntLogicalTable, [], name, value)


        class EntLogicalEntry(_Entity_):
            """
            
            
            .. attribute:: entlogicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: entlogicaldescr
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: entlogicaltype
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: entlogicalcommunity
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            	**config**\: False
            
            .. attribute:: entlogicaltaddress
            
            	
            	**type**\: str
            
            	**pattern:** (\\d\*(.\\d\*)\*)?
            
            	**config**\: False
            
            .. attribute:: entlogicaltdomain
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: entlogicalcontextengineid
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            	**config**\: False
            
            .. attribute:: entlogicalcontextname
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'ENTITY_MIB'
            _revision = '2017-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ENTITYMIB.EntLogicalTable.EntLogicalEntry, self).__init__()

                self.yang_name = "entLogicalEntry"
                self.yang_parent_name = "entLogicalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entlogicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entlogicalindex', (YLeaf(YType.int32, 'entLogicalIndex'), ['int'])),
                    ('entlogicaldescr', (YLeaf(YType.str, 'entLogicalDescr'), ['str'])),
                    ('entlogicaltype', (YLeaf(YType.str, 'entLogicalType'), ['str'])),
                    ('entlogicalcommunity', (YLeaf(YType.str, 'entLogicalCommunity'), ['str'])),
                    ('entlogicaltaddress', (YLeaf(YType.str, 'entLogicalTAddress'), ['str'])),
                    ('entlogicaltdomain', (YLeaf(YType.str, 'entLogicalTDomain'), ['str'])),
                    ('entlogicalcontextengineid', (YLeaf(YType.str, 'entLogicalContextEngineID'), ['str'])),
                    ('entlogicalcontextname', (YLeaf(YType.str, 'entLogicalContextName'), ['str'])),
                ])
                self.entlogicalindex = None
                self.entlogicaldescr = None
                self.entlogicaltype = None
                self.entlogicalcommunity = None
                self.entlogicaltaddress = None
                self.entlogicaltdomain = None
                self.entlogicalcontextengineid = None
                self.entlogicalcontextname = None
                self._segment_path = lambda: "entLogicalEntry" + "[entLogicalIndex='" + str(self.entlogicalindex) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/entLogicalTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ENTITYMIB.EntLogicalTable.EntLogicalEntry, ['entlogicalindex', 'entlogicaldescr', 'entlogicaltype', 'entlogicalcommunity', 'entlogicaltaddress', 'entlogicaltdomain', 'entlogicalcontextengineid', 'entlogicalcontextname'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_mib as meta
                return meta._meta_table['ENTITYMIB.EntLogicalTable.EntLogicalEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_mib as meta
            return meta._meta_table['ENTITYMIB.EntLogicalTable']['meta_info']


    class EntLPMappingTable(_Entity_):
        """
        
        
        .. attribute:: entlpmappingentry
        
        	
        	**type**\: list of  		 :py:class:`EntLPMappingEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.EntLPMappingTable.EntLPMappingEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ENTITY_MIB'
        _revision = '2017-04-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ENTITYMIB.EntLPMappingTable, self).__init__()

            self.yang_name = "entLPMappingTable"
            self.yang_parent_name = "ENTITY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("entLPMappingEntry", ("entlpmappingentry", ENTITYMIB.EntLPMappingTable.EntLPMappingEntry))])
            self._leafs = OrderedDict()

            self.entlpmappingentry = YList(self)
            self._segment_path = lambda: "entLPMappingTable"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYMIB.EntLPMappingTable, [], name, value)


        class EntLPMappingEntry(_Entity_):
            """
            
            
            .. attribute:: entlogicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: entlpphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'ENTITY_MIB'
            _revision = '2017-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ENTITYMIB.EntLPMappingTable.EntLPMappingEntry, self).__init__()

                self.yang_name = "entLPMappingEntry"
                self.yang_parent_name = "entLPMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entlogicalindex','entlpphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entlogicalindex', (YLeaf(YType.int32, 'entLogicalIndex'), ['int'])),
                    ('entlpphysicalindex', (YLeaf(YType.int32, 'entLPPhysicalIndex'), ['int'])),
                ])
                self.entlogicalindex = None
                self.entlpphysicalindex = None
                self._segment_path = lambda: "entLPMappingEntry" + "[entLogicalIndex='" + str(self.entlogicalindex) + "']" + "[entLPPhysicalIndex='" + str(self.entlpphysicalindex) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/entLPMappingTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ENTITYMIB.EntLPMappingTable.EntLPMappingEntry, ['entlogicalindex', 'entlpphysicalindex'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_mib as meta
                return meta._meta_table['ENTITYMIB.EntLPMappingTable.EntLPMappingEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_mib as meta
            return meta._meta_table['ENTITYMIB.EntLPMappingTable']['meta_info']


    class EntAliasMappingTable(_Entity_):
        """
        
        
        .. attribute:: entaliasmappingentry
        
        	
        	**type**\: list of  		 :py:class:`EntAliasMappingEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.EntAliasMappingTable.EntAliasMappingEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ENTITY_MIB'
        _revision = '2017-04-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ENTITYMIB.EntAliasMappingTable, self).__init__()

            self.yang_name = "entAliasMappingTable"
            self.yang_parent_name = "ENTITY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("entAliasMappingEntry", ("entaliasmappingentry", ENTITYMIB.EntAliasMappingTable.EntAliasMappingEntry))])
            self._leafs = OrderedDict()

            self.entaliasmappingentry = YList(self)
            self._segment_path = lambda: "entAliasMappingTable"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYMIB.EntAliasMappingTable, [], name, value)


        class EntAliasMappingEntry(_Entity_):
            """
            
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: entaliaslogicalindexorzero  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: entaliasmappingidentifier
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            

            """

            _prefix = 'ENTITY_MIB'
            _revision = '2017-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ENTITYMIB.EntAliasMappingTable.EntAliasMappingEntry, self).__init__()

                self.yang_name = "entAliasMappingEntry"
                self.yang_parent_name = "entAliasMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','entaliaslogicalindexorzero']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.int32, 'entPhysicalIndex'), ['int'])),
                    ('entaliaslogicalindexorzero', (YLeaf(YType.int32, 'entAliasLogicalIndexOrZero'), ['int'])),
                    ('entaliasmappingidentifier', (YLeaf(YType.str, 'entAliasMappingIdentifier'), ['str'])),
                ])
                self.entphysicalindex = None
                self.entaliaslogicalindexorzero = None
                self.entaliasmappingidentifier = None
                self._segment_path = lambda: "entAliasMappingEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[entAliasLogicalIndexOrZero='" + str(self.entaliaslogicalindexorzero) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/entAliasMappingTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ENTITYMIB.EntAliasMappingTable.EntAliasMappingEntry, ['entphysicalindex', 'entaliaslogicalindexorzero', 'entaliasmappingidentifier'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_mib as meta
                return meta._meta_table['ENTITYMIB.EntAliasMappingTable.EntAliasMappingEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_mib as meta
            return meta._meta_table['ENTITYMIB.EntAliasMappingTable']['meta_info']


    class EntPhysicalContainsTable(_Entity_):
        """
        
        
        .. attribute:: entphysicalcontainsentry
        
        	
        	**type**\: list of  		 :py:class:`EntPhysicalContainsEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.EntPhysicalContainsTable.EntPhysicalContainsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ENTITY_MIB'
        _revision = '2017-04-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ENTITYMIB.EntPhysicalContainsTable, self).__init__()

            self.yang_name = "entPhysicalContainsTable"
            self.yang_parent_name = "ENTITY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("entPhysicalContainsEntry", ("entphysicalcontainsentry", ENTITYMIB.EntPhysicalContainsTable.EntPhysicalContainsEntry))])
            self._leafs = OrderedDict()

            self.entphysicalcontainsentry = YList(self)
            self._segment_path = lambda: "entPhysicalContainsTable"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYMIB.EntPhysicalContainsTable, [], name, value)


        class EntPhysicalContainsEntry(_Entity_):
            """
            
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: entphysicalchildindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'ENTITY_MIB'
            _revision = '2017-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ENTITYMIB.EntPhysicalContainsTable.EntPhysicalContainsEntry, self).__init__()

                self.yang_name = "entPhysicalContainsEntry"
                self.yang_parent_name = "entPhysicalContainsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','entphysicalchildindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.int32, 'entPhysicalIndex'), ['int'])),
                    ('entphysicalchildindex', (YLeaf(YType.int32, 'entPhysicalChildIndex'), ['int'])),
                ])
                self.entphysicalindex = None
                self.entphysicalchildindex = None
                self._segment_path = lambda: "entPhysicalContainsEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[entPhysicalChildIndex='" + str(self.entphysicalchildindex) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/entPhysicalContainsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ENTITYMIB.EntPhysicalContainsTable.EntPhysicalContainsEntry, ['entphysicalindex', 'entphysicalchildindex'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_mib as meta
                return meta._meta_table['ENTITYMIB.EntPhysicalContainsTable.EntPhysicalContainsEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_mib as meta
            return meta._meta_table['ENTITYMIB.EntPhysicalContainsTable']['meta_info']

    def clone_ptr(self):
        self._top_entity = ENTITYMIB()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_mib as meta
        return meta._meta_table['ENTITYMIB']['meta_info']


