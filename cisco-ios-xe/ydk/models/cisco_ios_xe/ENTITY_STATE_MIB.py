""" ENTITY_STATE_MIB 

This MIB defines a state extension to the Entity MIB.

Copyright (C) The Internet Society 2005.  This version
of this MIB module is part of RFC 4268; see the RFC
itself for full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class ENTITYSTATEMIB(Entity):
    """
    
    
    .. attribute:: entstatetable
    
    	A table of information about state/status of entities. This is a sparse augment of the entPhysicalTable.  Entries appear in this table for values of entPhysicalClass [RFC4133] that in this implementation are able to report any of the state or status stored in this table
    	**type**\:  :py:class:`EntStateTable <ydk.models.cisco_ios_xe.ENTITY_STATE_MIB.ENTITYSTATEMIB.EntStateTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'ENTITY-STATE-MIB'
    _revision = '2005-11-22'

    def __init__(self):
        super(ENTITYSTATEMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "ENTITY-STATE-MIB"
        self.yang_parent_name = "ENTITY-STATE-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("entStateTable", ("entstatetable", ENTITYSTATEMIB.EntStateTable))])
        self._leafs = OrderedDict()

        self.entstatetable = ENTITYSTATEMIB.EntStateTable()
        self.entstatetable.parent = self
        self._children_name_map["entstatetable"] = "entStateTable"
        self._segment_path = lambda: "ENTITY-STATE-MIB:ENTITY-STATE-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ENTITYSTATEMIB, [], name, value)


    class EntStateTable(Entity):
        """
        A table of information about state/status of entities.
        This is a sparse augment of the entPhysicalTable.  Entries
        appear in this table for values of
        entPhysicalClass [RFC4133] that in this implementation
        are able to report any of the state or status stored in
        this table.
        
        .. attribute:: entstateentry
        
        	State information about this physical entity
        	**type**\: list of  		 :py:class:`EntStateEntry <ydk.models.cisco_ios_xe.ENTITY_STATE_MIB.ENTITYSTATEMIB.EntStateTable.EntStateEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ENTITY-STATE-MIB'
        _revision = '2005-11-22'

        def __init__(self):
            super(ENTITYSTATEMIB.EntStateTable, self).__init__()

            self.yang_name = "entStateTable"
            self.yang_parent_name = "ENTITY-STATE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("entStateEntry", ("entstateentry", ENTITYSTATEMIB.EntStateTable.EntStateEntry))])
            self._leafs = OrderedDict()

            self.entstateentry = YList(self)
            self._segment_path = lambda: "entStateTable"
            self._absolute_path = lambda: "ENTITY-STATE-MIB:ENTITY-STATE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYSTATEMIB.EntStateTable, [], name, value)


        class EntStateEntry(Entity):
            """
            State information about this physical entity.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: entstatelastchanged
            
            	The value of this object is the date and time when the value of any of entStateAdmin, entStateOper, entStateUsage, entStateAlarm, or entStateStandby changed for this entity.  If there has been no change since the last re\-initialization of the local system, this object contains the date and time of local system initialization.  If there has been no change since the entity was added to the local system, this object contains the date and time of the insertion
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: entstateadmin
            
            	The administrative state for this entity.  This object refers to an entities administrative permission to service both other entities within its containment hierarchy as well other users of its services defined by means outside the scope of this MIB.  Setting this object to 'notSupported' will result in an 'inconsistentValue' error.  For entities that do not support administrative state, all set operations will result in an 'inconsistentValue' error.  Some physical entities exhibit only a subset of the remaining administrative state values.  Some entities cannot be locked, and hence this object exhibits only the 'unlocked' state.  Other entities cannot be shutdown gracefully, and hence this object does not exhibit the 'shuttingDown' state.  A value of 'inconsistentValue' will be returned if attempts are made to set this object to values not supported by its administrative model
            	**type**\:  :py:class:`EntityAdminState <ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB.EntityAdminState>`
            
            	**config**\: False
            
            .. attribute:: entstateoper
            
            	The operational state for this entity.  Note that unlike the state model used within the Interfaces MIB [RFC2863], this object does not follow the administrative state.  An administrative state of down does not predict an operational state of disabled.  A value of 'testing' means that entity currently being tested and cannot therefore report whether it is operational or not.  A value of 'disabled' means that an entity is totally inoperable and unable to provide service both to entities within its containment hierarchy, or to other receivers of its service as defined in ways outside the scope of this MIB.  A value of 'enabled' means that an entity is fully or partially operable and able to provide service both to  entities within its containment hierarchy, or to other receivers of its service as defined in ways outside the scope of this MIB.  Note that some implementations may not be able to accurately report entStateOper while the entStateAdmin object has a value other than 'unlocked'. In these cases, this object MUST have a value of 'unknown'
            	**type**\:  :py:class:`EntityOperState <ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB.EntityOperState>`
            
            	**config**\: False
            
            .. attribute:: entstateusage
            
            	The usage state for this entity.  This object refers to an entity's ability to service more physical entities in a containment hierarchy.  A value of 'idle' means this entity is able to contain other entities but that no other entity is currently contained within this entity.  A value of 'active' means that at least one entity is contained within this entity, but that it could handle more.  A value of 'busy' means that the entity is unable to handle any additional entities being contained in it.  Some entities will exhibit only a subset of the usage state values.  Entities that are unable to ever service any entities within a containment hierarchy will always have a usage state of 'busy'.  Some entities will only ever be able to support one entity within its containment hierarchy and will therefore only exhibit values of 'idle' and 'busy'
            	**type**\:  :py:class:`EntityUsageState <ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB.EntityUsageState>`
            
            	**config**\: False
            
            .. attribute:: entstatealarm
            
            	The alarm status for this entity.  It does not include the alarms raised on child components within its containment hierarchy.  A value of 'unknown' means that this entity is  unable to report alarm state.  Note that this differs from 'indeterminate', which means that alarm state is supported and there are alarms against this entity, but the severity of some of the alarms is not known.  If no bits are set, then this entity supports reporting of alarms, but there are currently no active alarms against this entity
            	**type**\:  :py:class:`EntityAlarmStatus <ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB.EntityAlarmStatus>`
            
            	**config**\: False
            
            .. attribute:: entstatestandby
            
            	The standby status for this entity.  Some entities will exhibit only a subset of the remaining standby state values.  If this entity cannot operate in a standby role, the value of this object will always be 'providingService'
            	**type**\:  :py:class:`EntityStandbyStatus <ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB.EntityStandbyStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ENTITY-STATE-MIB'
            _revision = '2005-11-22'

            def __init__(self):
                super(ENTITYSTATEMIB.EntStateTable.EntStateEntry, self).__init__()

                self.yang_name = "entStateEntry"
                self.yang_parent_name = "entStateTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('entstatelastchanged', (YLeaf(YType.str, 'entStateLastChanged'), ['str'])),
                    ('entstateadmin', (YLeaf(YType.enumeration, 'entStateAdmin'), [('ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB', 'EntityAdminState', '')])),
                    ('entstateoper', (YLeaf(YType.enumeration, 'entStateOper'), [('ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB', 'EntityOperState', '')])),
                    ('entstateusage', (YLeaf(YType.enumeration, 'entStateUsage'), [('ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB', 'EntityUsageState', '')])),
                    ('entstatealarm', (YLeaf(YType.bits, 'entStateAlarm'), ['Bits'])),
                    ('entstatestandby', (YLeaf(YType.enumeration, 'entStateStandby'), [('ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB', 'EntityStandbyStatus', '')])),
                ])
                self.entphysicalindex = None
                self.entstatelastchanged = None
                self.entstateadmin = None
                self.entstateoper = None
                self.entstateusage = None
                self.entstatealarm = Bits()
                self.entstatestandby = None
                self._segment_path = lambda: "entStateEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "ENTITY-STATE-MIB:ENTITY-STATE-MIB/entStateTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ENTITYSTATEMIB.EntStateTable.EntStateEntry, ['entphysicalindex', 'entstatelastchanged', 'entstateadmin', 'entstateoper', 'entstateusage', 'entstatealarm', 'entstatestandby'], name, value)



    def clone_ptr(self):
        self._top_entity = ENTITYSTATEMIB()
        return self._top_entity



