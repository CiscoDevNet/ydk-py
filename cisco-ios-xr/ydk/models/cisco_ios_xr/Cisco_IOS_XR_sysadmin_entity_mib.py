""" Cisco_IOS_XR_sysadmin_entity_mib 

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

Copyright(c) 2015\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

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



class ENTITYMIB(Entity):
    """
    
    
    .. attribute:: entitygeneral
    
    	
    	**type**\:  :py:class:`Entitygeneral <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.Entitygeneral>`
    
    .. attribute:: entphysicaltable
    
    	
    	**type**\:  :py:class:`Entphysicaltable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.Entphysicaltable>`
    
    .. attribute:: entlogicaltable
    
    	
    	**type**\:  :py:class:`Entlogicaltable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.Entlogicaltable>`
    
    .. attribute:: entlpmappingtable
    
    	
    	**type**\:  :py:class:`Entlpmappingtable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.Entlpmappingtable>`
    
    .. attribute:: entaliasmappingtable
    
    	
    	**type**\:  :py:class:`Entaliasmappingtable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.Entaliasmappingtable>`
    
    .. attribute:: entphysicalcontainstable
    
    	
    	**type**\:  :py:class:`Entphysicalcontainstable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.Entphysicalcontainstable>`
    
    

    """

    _prefix = 'ENTITY_MIB'
    _revision = '2017-04-12'

    def __init__(self):
        super(ENTITYMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "ENTITY-MIB"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-entity-mib"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("entityGeneral", ("entitygeneral", ENTITYMIB.Entitygeneral)), ("entPhysicalTable", ("entphysicaltable", ENTITYMIB.Entphysicaltable)), ("entLogicalTable", ("entlogicaltable", ENTITYMIB.Entlogicaltable)), ("entLPMappingTable", ("entlpmappingtable", ENTITYMIB.Entlpmappingtable)), ("entAliasMappingTable", ("entaliasmappingtable", ENTITYMIB.Entaliasmappingtable)), ("entPhysicalContainsTable", ("entphysicalcontainstable", ENTITYMIB.Entphysicalcontainstable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.entitygeneral = ENTITYMIB.Entitygeneral()
        self.entitygeneral.parent = self
        self._children_name_map["entitygeneral"] = "entityGeneral"
        self._children_yang_names.add("entityGeneral")

        self.entphysicaltable = ENTITYMIB.Entphysicaltable()
        self.entphysicaltable.parent = self
        self._children_name_map["entphysicaltable"] = "entPhysicalTable"
        self._children_yang_names.add("entPhysicalTable")

        self.entlogicaltable = ENTITYMIB.Entlogicaltable()
        self.entlogicaltable.parent = self
        self._children_name_map["entlogicaltable"] = "entLogicalTable"
        self._children_yang_names.add("entLogicalTable")

        self.entlpmappingtable = ENTITYMIB.Entlpmappingtable()
        self.entlpmappingtable.parent = self
        self._children_name_map["entlpmappingtable"] = "entLPMappingTable"
        self._children_yang_names.add("entLPMappingTable")

        self.entaliasmappingtable = ENTITYMIB.Entaliasmappingtable()
        self.entaliasmappingtable.parent = self
        self._children_name_map["entaliasmappingtable"] = "entAliasMappingTable"
        self._children_yang_names.add("entAliasMappingTable")

        self.entphysicalcontainstable = ENTITYMIB.Entphysicalcontainstable()
        self.entphysicalcontainstable.parent = self
        self._children_name_map["entphysicalcontainstable"] = "entPhysicalContainsTable"
        self._children_yang_names.add("entPhysicalContainsTable")
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB"


    class Entitygeneral(Entity):
        """
        
        
        .. attribute:: entlastchangetime
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'ENTITY_MIB'
        _revision = '2017-04-12'

        def __init__(self):
            super(ENTITYMIB.Entitygeneral, self).__init__()

            self.yang_name = "entityGeneral"
            self.yang_parent_name = "ENTITY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('entlastchangetime', YLeaf(YType.uint32, 'entLastChangeTime')),
            ])
            self.entlastchangetime = None
            self._segment_path = lambda: "entityGeneral"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYMIB.Entitygeneral, ['entlastchangetime'], name, value)


    class Entphysicaltable(Entity):
        """
        
        
        .. attribute:: entphysicalentry
        
        	
        	**type**\: list of  		 :py:class:`Entphysicalentry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
        
        

        """

        _prefix = 'ENTITY_MIB'
        _revision = '2017-04-12'

        def __init__(self):
            super(ENTITYMIB.Entphysicaltable, self).__init__()

            self.yang_name = "entPhysicalTable"
            self.yang_parent_name = "ENTITY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("entPhysicalEntry", ("entphysicalentry", ENTITYMIB.Entphysicaltable.Entphysicalentry))])
            self._leafs = OrderedDict()

            self.entphysicalentry = YList(self)
            self._segment_path = lambda: "entPhysicalTable"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYMIB.Entphysicaltable, [], name, value)


        class Entphysicalentry(Entity):
            """
            
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: entphysicaldescr
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: entphysicalvendortype
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: entphysicalcontainedin
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: entphysicalclass
            
            	
            	**type**\:  :py:class:`PhysicalClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.PhysicalClass>`
            
            .. attribute:: entphysicalparentrelpos
            
            	
            	**type**\: int
            
            	**range:** \-1..2147483647
            
            .. attribute:: entphysicalname
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: entphysicalhardwarerev
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: entphysicalfirmwarerev
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: entphysicalsoftwarerev
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: entphysicalserialnum
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: entphysicalmfgname
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: entphysicalmodelname
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: entphysicalalias
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: entphysicalassetid
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: entphysicalisfru
            
            	
            	**type**\:  :py:class:`TruthValue <ydk.models.cisco_ios_xr.SNMPv2_TC.TruthValue>`
            
            

            """

            _prefix = 'ENTITY_MIB'
            _revision = '2017-04-12'

            def __init__(self):
                super(ENTITYMIB.Entphysicaltable.Entphysicalentry, self).__init__()

                self.yang_name = "entPhysicalEntry"
                self.yang_parent_name = "entPhysicalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.int32, 'entPhysicalIndex')),
                    ('entphysicaldescr', YLeaf(YType.str, 'entPhysicalDescr')),
                    ('entphysicalvendortype', YLeaf(YType.str, 'entPhysicalVendorType')),
                    ('entphysicalcontainedin', YLeaf(YType.int32, 'entPhysicalContainedIn')),
                    ('entphysicalclass', YLeaf(YType.enumeration, 'entPhysicalClass')),
                    ('entphysicalparentrelpos', YLeaf(YType.int32, 'entPhysicalParentRelPos')),
                    ('entphysicalname', YLeaf(YType.str, 'entPhysicalName')),
                    ('entphysicalhardwarerev', YLeaf(YType.str, 'entPhysicalHardwareRev')),
                    ('entphysicalfirmwarerev', YLeaf(YType.str, 'entPhysicalFirmwareRev')),
                    ('entphysicalsoftwarerev', YLeaf(YType.str, 'entPhysicalSoftwareRev')),
                    ('entphysicalserialnum', YLeaf(YType.str, 'entPhysicalSerialNum')),
                    ('entphysicalmfgname', YLeaf(YType.str, 'entPhysicalMfgName')),
                    ('entphysicalmodelname', YLeaf(YType.str, 'entPhysicalModelName')),
                    ('entphysicalalias', YLeaf(YType.str, 'entPhysicalAlias')),
                    ('entphysicalassetid', YLeaf(YType.str, 'entPhysicalAssetID')),
                    ('entphysicalisfru', YLeaf(YType.enumeration, 'entPhysicalIsFRU')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(ENTITYMIB.Entphysicaltable.Entphysicalentry, ['entphysicalindex', 'entphysicaldescr', 'entphysicalvendortype', 'entphysicalcontainedin', 'entphysicalclass', 'entphysicalparentrelpos', 'entphysicalname', 'entphysicalhardwarerev', 'entphysicalfirmwarerev', 'entphysicalsoftwarerev', 'entphysicalserialnum', 'entphysicalmfgname', 'entphysicalmodelname', 'entphysicalalias', 'entphysicalassetid', 'entphysicalisfru'], name, value)


    class Entlogicaltable(Entity):
        """
        
        
        .. attribute:: entlogicalentry
        
        	
        	**type**\: list of  		 :py:class:`Entlogicalentry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.Entlogicaltable.Entlogicalentry>`
        
        

        """

        _prefix = 'ENTITY_MIB'
        _revision = '2017-04-12'

        def __init__(self):
            super(ENTITYMIB.Entlogicaltable, self).__init__()

            self.yang_name = "entLogicalTable"
            self.yang_parent_name = "ENTITY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("entLogicalEntry", ("entlogicalentry", ENTITYMIB.Entlogicaltable.Entlogicalentry))])
            self._leafs = OrderedDict()

            self.entlogicalentry = YList(self)
            self._segment_path = lambda: "entLogicalTable"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYMIB.Entlogicaltable, [], name, value)


        class Entlogicalentry(Entity):
            """
            
            
            .. attribute:: entlogicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: entlogicaldescr
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: entlogicaltype
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: entlogicalcommunity
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: entlogicaltaddress
            
            	
            	**type**\: str
            
            	**pattern:** (\\d\*(.\\d\*)\*)?
            
            .. attribute:: entlogicaltdomain
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: entlogicalcontextengineid
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: entlogicalcontextname
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'ENTITY_MIB'
            _revision = '2017-04-12'

            def __init__(self):
                super(ENTITYMIB.Entlogicaltable.Entlogicalentry, self).__init__()

                self.yang_name = "entLogicalEntry"
                self.yang_parent_name = "entLogicalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entlogicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entlogicalindex', YLeaf(YType.int32, 'entLogicalIndex')),
                    ('entlogicaldescr', YLeaf(YType.str, 'entLogicalDescr')),
                    ('entlogicaltype', YLeaf(YType.str, 'entLogicalType')),
                    ('entlogicalcommunity', YLeaf(YType.str, 'entLogicalCommunity')),
                    ('entlogicaltaddress', YLeaf(YType.str, 'entLogicalTAddress')),
                    ('entlogicaltdomain', YLeaf(YType.str, 'entLogicalTDomain')),
                    ('entlogicalcontextengineid', YLeaf(YType.str, 'entLogicalContextEngineID')),
                    ('entlogicalcontextname', YLeaf(YType.str, 'entLogicalContextName')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(ENTITYMIB.Entlogicaltable.Entlogicalentry, ['entlogicalindex', 'entlogicaldescr', 'entlogicaltype', 'entlogicalcommunity', 'entlogicaltaddress', 'entlogicaltdomain', 'entlogicalcontextengineid', 'entlogicalcontextname'], name, value)


    class Entlpmappingtable(Entity):
        """
        
        
        .. attribute:: entlpmappingentry
        
        	
        	**type**\: list of  		 :py:class:`Entlpmappingentry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.Entlpmappingtable.Entlpmappingentry>`
        
        

        """

        _prefix = 'ENTITY_MIB'
        _revision = '2017-04-12'

        def __init__(self):
            super(ENTITYMIB.Entlpmappingtable, self).__init__()

            self.yang_name = "entLPMappingTable"
            self.yang_parent_name = "ENTITY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("entLPMappingEntry", ("entlpmappingentry", ENTITYMIB.Entlpmappingtable.Entlpmappingentry))])
            self._leafs = OrderedDict()

            self.entlpmappingentry = YList(self)
            self._segment_path = lambda: "entLPMappingTable"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYMIB.Entlpmappingtable, [], name, value)


        class Entlpmappingentry(Entity):
            """
            
            
            .. attribute:: entlogicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: entlpphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'ENTITY_MIB'
            _revision = '2017-04-12'

            def __init__(self):
                super(ENTITYMIB.Entlpmappingtable.Entlpmappingentry, self).__init__()

                self.yang_name = "entLPMappingEntry"
                self.yang_parent_name = "entLPMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entlogicalindex','entlpphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entlogicalindex', YLeaf(YType.int32, 'entLogicalIndex')),
                    ('entlpphysicalindex', YLeaf(YType.int32, 'entLPPhysicalIndex')),
                ])
                self.entlogicalindex = None
                self.entlpphysicalindex = None
                self._segment_path = lambda: "entLPMappingEntry" + "[entLogicalIndex='" + str(self.entlogicalindex) + "']" + "[entLPPhysicalIndex='" + str(self.entlpphysicalindex) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/entLPMappingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ENTITYMIB.Entlpmappingtable.Entlpmappingentry, ['entlogicalindex', 'entlpphysicalindex'], name, value)


    class Entaliasmappingtable(Entity):
        """
        
        
        .. attribute:: entaliasmappingentry
        
        	
        	**type**\: list of  		 :py:class:`Entaliasmappingentry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.Entaliasmappingtable.Entaliasmappingentry>`
        
        

        """

        _prefix = 'ENTITY_MIB'
        _revision = '2017-04-12'

        def __init__(self):
            super(ENTITYMIB.Entaliasmappingtable, self).__init__()

            self.yang_name = "entAliasMappingTable"
            self.yang_parent_name = "ENTITY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("entAliasMappingEntry", ("entaliasmappingentry", ENTITYMIB.Entaliasmappingtable.Entaliasmappingentry))])
            self._leafs = OrderedDict()

            self.entaliasmappingentry = YList(self)
            self._segment_path = lambda: "entAliasMappingTable"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYMIB.Entaliasmappingtable, [], name, value)


        class Entaliasmappingentry(Entity):
            """
            
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: entaliaslogicalindexorzero  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: entaliasmappingidentifier
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'ENTITY_MIB'
            _revision = '2017-04-12'

            def __init__(self):
                super(ENTITYMIB.Entaliasmappingtable.Entaliasmappingentry, self).__init__()

                self.yang_name = "entAliasMappingEntry"
                self.yang_parent_name = "entAliasMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','entaliaslogicalindexorzero']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.int32, 'entPhysicalIndex')),
                    ('entaliaslogicalindexorzero', YLeaf(YType.int32, 'entAliasLogicalIndexOrZero')),
                    ('entaliasmappingidentifier', YLeaf(YType.str, 'entAliasMappingIdentifier')),
                ])
                self.entphysicalindex = None
                self.entaliaslogicalindexorzero = None
                self.entaliasmappingidentifier = None
                self._segment_path = lambda: "entAliasMappingEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[entAliasLogicalIndexOrZero='" + str(self.entaliaslogicalindexorzero) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/entAliasMappingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ENTITYMIB.Entaliasmappingtable.Entaliasmappingentry, ['entphysicalindex', 'entaliaslogicalindexorzero', 'entaliasmappingidentifier'], name, value)


    class Entphysicalcontainstable(Entity):
        """
        
        
        .. attribute:: entphysicalcontainsentry
        
        	
        	**type**\: list of  		 :py:class:`Entphysicalcontainsentry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_mib.ENTITYMIB.Entphysicalcontainstable.Entphysicalcontainsentry>`
        
        

        """

        _prefix = 'ENTITY_MIB'
        _revision = '2017-04-12'

        def __init__(self):
            super(ENTITYMIB.Entphysicalcontainstable, self).__init__()

            self.yang_name = "entPhysicalContainsTable"
            self.yang_parent_name = "ENTITY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("entPhysicalContainsEntry", ("entphysicalcontainsentry", ENTITYMIB.Entphysicalcontainstable.Entphysicalcontainsentry))])
            self._leafs = OrderedDict()

            self.entphysicalcontainsentry = YList(self)
            self._segment_path = lambda: "entPhysicalContainsTable"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYMIB.Entphysicalcontainstable, [], name, value)


        class Entphysicalcontainsentry(Entity):
            """
            
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: entphysicalchildindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'ENTITY_MIB'
            _revision = '2017-04-12'

            def __init__(self):
                super(ENTITYMIB.Entphysicalcontainstable.Entphysicalcontainsentry, self).__init__()

                self.yang_name = "entPhysicalContainsEntry"
                self.yang_parent_name = "entPhysicalContainsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','entphysicalchildindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.int32, 'entPhysicalIndex')),
                    ('entphysicalchildindex', YLeaf(YType.int32, 'entPhysicalChildIndex')),
                ])
                self.entphysicalindex = None
                self.entphysicalchildindex = None
                self._segment_path = lambda: "entPhysicalContainsEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[entPhysicalChildIndex='" + str(self.entphysicalchildindex) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-mib:ENTITY-MIB/entPhysicalContainsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ENTITYMIB.Entphysicalcontainstable.Entphysicalcontainsentry, ['entphysicalindex', 'entphysicalchildindex'], name, value)

    def clone_ptr(self):
        self._top_entity = ENTITYMIB()
        return self._top_entity

