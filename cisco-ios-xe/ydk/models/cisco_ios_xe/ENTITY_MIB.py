""" ENTITY_MIB 

The MIB module for representing multiple logical
entities supported by a single SNMP agent.

Copyright (C) The Internet Society (2005).  This
version of this MIB module is part of RFC 4133; see
the RFC itself for full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class PhysicalClass(Enum):
    """
    PhysicalClass (Enum Class)

    An enumerated value which provides an indication of the

    general hardware type of a particular physical entity.

    There are no restrictions as to the number of

    entPhysicalEntries of each entPhysicalClass, which must be

    instantiated by an agent.

    The enumeration 'other' is applicable if the physical entity

    class is known, but does not match any of the supported

    values.

    The enumeration 'unknown' is applicable if the physical

    entity class is unknown to the agent.

    The enumeration 'chassis' is applicable if the physical

    entity class is an overall container for networking

    equipment.  Any class of physical entity, except a stack,

    may be contained within a chassis; and a chassis may only

    be contained within a stack.

    The enumeration 'backplane' is applicable if the physical

    entity class is some sort of device for aggregating and

    forwarding networking traffic, such as a shared backplane in

    a modular ethernet switch.  Note that an agent may model a

    backplane as a single physical entity, which is actually

    implemented as multiple discrete physical components (within

    a chassis or stack).

    The enumeration 'container' is applicable if the physical

    entity class is capable of containing one or more removable

    physical entities, possibly of different types.  For

    example, each (empty or full) slot in a chassis will be

    modeled as a container.  Note that all removable physical

    entities should be modeled within a container entity, such

    as field\-replaceable modules, fans, or power supplies.  Note

    that all known containers should be modeled by the agent,

    including empty containers.

    The enumeration 'powerSupply' is applicable if the physical

    entity class is a power\-supplying component.

    The enumeration 'fan' is applicable if the physical entity

    class is a fan or other heat\-reduction component.

    The enumeration 'sensor' is applicable if the physical

    entity class is some sort of sensor, such as a temperature

    sensor within a router chassis.

    The enumeration 'module' is applicable if the physical

    entity class is some sort of self\-contained sub\-system.  If

    the enumeration 'module' is removable, then it should be

    modeled within a container entity, otherwise it should be

    modeled directly within another physical entity (e.g., a

    chassis or another module).

    The enumeration 'port' is applicable if the physical entity

    class is some sort of networking port, capable of receiving

    and/or transmitting networking traffic.

    The enumeration 'stack' is applicable if the physical entity

    class is some sort of super\-container (possibly virtual),

    intended to group together multiple chassis entities.  A

    stack may be realized by a 'virtual' cable, a real

    interconnect cable, attached to multiple chassis, or may in

    fact be comprised of multiple interconnect cables.  A stack

    should not be modeled within any other physical entities,

    but a stack may be contained within another stack.  Only

    chassis entities should be contained within a stack.

    The enumeration 'cpu' is applicable if the physical entity

    class is some sort of central processing unit.

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

    .. data:: cpu = 12

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

    cpu = Enum.YLeaf(12, "cpu")



class ENTITYMIB(Entity):
    """
    
    
    .. attribute:: entitygeneral
    
    	
    	**type**\:  :py:class:`Entitygeneral <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entitygeneral>`
    
    .. attribute:: entphysicaltable
    
    	This table contains one row per physical entity.  There is always at least one row for an 'overall' physical entity
    	**type**\:  :py:class:`Entphysicaltable <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable>`
    
    .. attribute:: entlogicaltable
    
    	This table contains one row per logical entity.  For agents that implement more than one naming scope, at least one entry must exist.  Agents which instantiate all MIB objects within a single naming scope are not required to implement this table
    	**type**\:  :py:class:`Entlogicaltable <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entlogicaltable>`
    
    .. attribute:: entlpmappingtable
    
    	This table contains zero or more rows of logical entity to physical equipment associations.  For each logical entity known by this agent, there are zero or more mappings to the physical resources, which are used to realize that logical entity.  An agent should limit the number and nature of entries in this table such that only meaningful and non\-redundant information is returned.  For example, in a system that contains a single power supply, mappings between logical entities and the power supply are not useful and should not be included.  Also, only the most appropriate physical component, which is closest to the root of a particular containment tree, should be identified in an entLPMapping entry.  For example, suppose a bridge is realized on a particular module, and all ports on that module are ports on this bridge.  A mapping between the bridge and the module would be useful, but additional mappings between the bridge and each of the ports on that module would be redundant (because the entPhysicalContainedIn hierarchy can provide the same information).  On the other hand, if more than one bridge were utilizing ports on this module, then mappings between each bridge and the ports it used would be appropriate.  Also, in the case of a single backplane repeater, a mapping for the backplane to the single repeater entity is not necessary
    	**type**\:  :py:class:`Entlpmappingtable <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entlpmappingtable>`
    
    .. attribute:: entaliasmappingtable
    
    	This table contains zero or more rows, representing mappings of logical entity and physical component to external MIB identifiers.  Each physical port in the system may be associated with a mapping to an external identifier, which itself is associated with a particular logical entity's naming scope.  A 'wildcard' mechanism is provided to indicate that an identifier is associated with more than one logical entity
    	**type**\:  :py:class:`Entaliasmappingtable <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entaliasmappingtable>`
    
    .. attribute:: entphysicalcontainstable
    
    	A table that exposes the container/'containee' relationships between physical entities.  This table provides all the information found by constructing the virtual containment tree for a given entPhysicalTable, but in a more direct format.  In the event a physical entity is contained by more than one other physical entity (e.g., double\-wide modules), this table should include these additional mappings, which cannot be represented in the entPhysicalTable virtual containment tree
    	**type**\:  :py:class:`Entphysicalcontainstable <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicalcontainstable>`
    
    

    """

    _prefix = 'ENTITY-MIB'
    _revision = '2005-08-10'

    def __init__(self):
        super(ENTITYMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "ENTITY-MIB"
        self.yang_parent_name = "ENTITY-MIB"
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
        self._segment_path = lambda: "ENTITY-MIB:ENTITY-MIB"


    class Entitygeneral(Entity):
        """
        
        
        .. attribute:: entlastchangetime
        
        	The value of sysUpTime at the time a conceptual row is created, modified, or deleted in any of these tables\:         \- entPhysicalTable         \- entLogicalTable         \- entLPMappingTable         \- entAliasMappingTable           \- entPhysicalContainsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'ENTITY-MIB'
        _revision = '2005-08-10'

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
            self._absolute_path = lambda: "ENTITY-MIB:ENTITY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYMIB.Entitygeneral, ['entlastchangetime'], name, value)


    class Entphysicaltable(Entity):
        """
        This table contains one row per physical entity.  There is
        always at least one row for an 'overall' physical entity.
        
        .. attribute:: entphysicalentry
        
        	Information about a particular physical entity.  Each entry provides objects (entPhysicalDescr, entPhysicalVendorType, and entPhysicalClass) to help an NMS identify and characterize the entry, and objects (entPhysicalContainedIn and entPhysicalParentRelPos) to help an NMS relate the particular entry to other entries in this table
        	**type**\: list of  		 :py:class:`Entphysicalentry <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
        
        

        """

        _prefix = 'ENTITY-MIB'
        _revision = '2005-08-10'

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
            self._absolute_path = lambda: "ENTITY-MIB:ENTITY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYMIB.Entphysicaltable, [], name, value)


        class Entphysicalentry(Entity):
            """
            Information about a particular physical entity.
            
            Each entry provides objects (entPhysicalDescr,
            entPhysicalVendorType, and entPhysicalClass) to help an NMS
            identify and characterize the entry, and objects
            (entPhysicalContainedIn and entPhysicalParentRelPos) to help
            an NMS relate the particular entry to other entries in this
            table.
            
            .. attribute:: entphysicalindex  (key)
            
            	The index for this entry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: entphysicaldescr
            
            	A textual description of physical entity.  This object should contain a string that identifies the manufacturer's name for the physical entity, and should be set to a distinct value for each version or model of the physical entity
            	**type**\: str
            
            .. attribute:: entphysicalvendortype
            
            	An indication of the vendor\-specific hardware type of the physical entity.  Note that this is different from the definition of MIB\-II's sysObjectID.  An agent should set this object to an enterprise\-specific registration identifier value indicating the specific equipment type in detail.  The associated instance of entPhysicalClass is used to indicate the general type of hardware device.  If no vendor\-specific registration identifier exists for this physical entity, or the value is unknown by this agent, then the value { 0 0 } is returned
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: entphysicalcontainedin
            
            	The value of entPhysicalIndex for the physical entity which 'contains' this physical entity.  A value of zero indicates this physical entity is not contained in any other physical entity.  Note that the set of 'containment' relationships define a strict hierarchy; that is, recursion is not allowed.  In the event that a physical entity is contained by more than one physical entity (e.g., double\-wide modules), this object should identify the containing entity with the lowest value of entPhysicalIndex
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: entphysicalclass
            
            	An indication of the general hardware type of the physical entity.  An agent should set this object to the standard enumeration value that most accurately indicates the general class of the physical entity, or the primary class if there is more than one entity.  If no appropriate standard registration identifier exists for this physical entity, then the value 'other(1)' is returned.  If the value is unknown by this agent, then the value 'unknown(2)' is returned
            	**type**\:  :py:class:`PhysicalClass <ydk.models.cisco_ios_xe.ENTITY_MIB.PhysicalClass>`
            
            .. attribute:: entphysicalparentrelpos
            
            	An indication of the relative position of this 'child' component among all its 'sibling' components.  Sibling components are defined as entPhysicalEntries that share the same instance values of each of the entPhysicalContainedIn and entPhysicalClass objects.  An NMS can use this object to identify the relative ordering for all sibling components of a particular parent (identified by the entPhysicalContainedIn instance in each sibling entry).  If possible, this value should match any external labeling of the physical component.  For example, for a container (e.g., card slot) labeled as 'slot #3', entPhysicalParentRelPos should have the value '3'.  Note that the entPhysicalEntry for the module plugged in slot 3 should have an entPhysicalParentRelPos value of '1'.  If the physical position of this component does not match any external numbering or clearly visible ordering, then user documentation or other external reference material should be used to determine the parent\-relative position. If this is not possible, then the agent should assign a consistent (but possibly arbitrary) ordering to a given set of 'sibling' components, perhaps based on internal representation of the components.   If the agent cannot determine the parent\-relative position for some reason, or if the associated value of entPhysicalContainedIn is '0', then the value '\-1' is returned.  Otherwise, a non\-negative integer is returned, indicating the parent\-relative position of this physical entity.  Parent\-relative ordering normally starts from '1' and continues to 'N', where 'N' represents the highest positioned child entity.  However, if the physical entities (e.g., slots) are labeled from a starting position of zero, then the first sibling should be associated with an entPhysicalParentRelPos value of '0'.  Note that this ordering may be sparse or dense, depending on agent implementation.  The actual values returned are not globally meaningful, as each 'parent' component may use different numbering algorithms.  The ordering is only meaningful among siblings of the same parent component.  The agent should retain parent\-relative position values across reboots, either through algorithmic assignment or use of non\-volatile storage
            	**type**\: int
            
            	**range:** \-1..2147483647
            
            .. attribute:: entphysicalname
            
            	The textual name of the physical entity.  The value of this object should be the name of the component as assigned by the local device and should be suitable for use in commands entered at the device's `console'.  This might be a text name (e.g., `console') or a simple component number (e.g., port or module number, such as `1'), depending on the physical component naming syntax of the device.  If there is no local name, or if this object is otherwise not applicable, then this object contains a zero\-length string.  Note that the value of entPhysicalName for two physical entities will be the same in the event that the console interface does not distinguish between them, e.g., slot\-1 and the card in slot\-1
            	**type**\: str
            
            .. attribute:: entphysicalhardwarerev
            
            	The vendor\-specific hardware revision string for the physical entity.  The preferred value is the hardware revision identifier actually printed on the component itself (if present).  Note that if revision information is stored internally in a non\-printable (e.g., binary) format, then the agent must convert such information to a printable format, in an implementation\-specific manner.  If no specific hardware revision string is associated with the physical component, or if this information is unknown to the agent, then this object will contain a zero\-length string
            	**type**\: str
            
            .. attribute:: entphysicalfirmwarerev
            
            	The vendor\-specific firmware revision string for the physical entity.  Note that if revision information is stored internally in a non\-printable (e.g., binary) format, then the agent must convert such information to a printable format, in an implementation\-specific manner.  If no specific firmware programs are associated with the physical component, or if this information is unknown to the agent, then this object will contain a zero\-length string
            	**type**\: str
            
            .. attribute:: entphysicalsoftwarerev
            
            	The vendor\-specific software revision string for the physical entity.  Note that if revision information is stored internally in a   non\-printable (e.g., binary) format, then the agent must convert such information to a printable format, in an implementation\-specific manner.  If no specific software programs are associated with the physical component, or if this information is unknown to the agent, then this object will contain a zero\-length string
            	**type**\: str
            
            .. attribute:: entphysicalserialnum
            
            	The vendor\-specific serial number string for the physical entity.  The preferred value is the serial number string actually printed on the component itself (if present).  On the first instantiation of an physical entity, the value of entPhysicalSerialNum associated with that entity is set to the correct vendor\-assigned serial number, if this information is available to the agent.  If a serial number is unknown or non\-existent, the entPhysicalSerialNum will be set to a zero\-length string instead.  Note that implementations that can correctly identify the serial numbers of all installed physical entities do not need to provide write access to the entPhysicalSerialNum object.  Agents which cannot provide non\-volatile storage for the entPhysicalSerialNum strings are not required to implement write access for this object.  Not every physical component will have a serial number, or even need one.  Physical entities for which the associated value of the entPhysicalIsFRU object is equal to 'false(2)' (e.g., the repeater ports within a repeater module), do not need their own unique serial number.  An agent does not have to provide write access for such entities, and may return a zero\-length string.  If write access is implemented for an instance of entPhysicalSerialNum, and a value is written into the instance, the agent must retain the supplied value in the entPhysicalSerialNum instance (associated with the same physical entity) for as long as that entity remains instantiated.  This includes instantiations across all re\-initializations/reboots of the network management system, including those resulting in a change of the physical   entity's entPhysicalIndex value
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: entphysicalmfgname
            
            	The name of the manufacturer of this physical component. The preferred value is the manufacturer name string actually printed on the component itself (if present).  Note that comparisons between instances of the entPhysicalModelName, entPhysicalFirmwareRev, entPhysicalSoftwareRev, and the entPhysicalSerialNum objects, are only meaningful amongst entPhysicalEntries with the same value of entPhysicalMfgName.  If the manufacturer name string associated with the physical component is unknown to the agent, then this object will contain a zero\-length string
            	**type**\: str
            
            .. attribute:: entphysicalmodelname
            
            	The vendor\-specific model name identifier string associated with this physical component.  The preferred value is the customer\-visible part number, which may be printed on the component itself.  If the model name string associated with the physical component is unknown to the agent, then this object will contain a zero\-length string
            	**type**\: str
            
            .. attribute:: entphysicalalias
            
            	This object is an 'alias' name for the physical entity, as specified by a network manager, and provides a non\-volatile 'handle' for the physical entity.  On the first instantiation of a physical entity, the value   of entPhysicalAlias associated with that entity is set to the zero\-length string.  However, the agent may set the value to a locally unique default value, instead of a zero\-length string.  If write access is implemented for an instance of entPhysicalAlias, and a value is written into the instance, the agent must retain the supplied value in the entPhysicalAlias instance (associated with the same physical entity) for as long as that entity remains instantiated. This includes instantiations across all re\-initializations/reboots of the network management system, including those resulting in a change of the physical entity's entPhysicalIndex value
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: entphysicalassetid
            
            	This object is a user\-assigned asset tracking identifier (as specified by a network manager) for the physical entity, and provides non\-volatile storage of this information.  On the first instantiation of a physical entity, the value of entPhysicalAssetID associated with that entity is set to the zero\-length string.  Not every physical component will have an asset tracking identifier, or even need one.  Physical entities for which the associated value of the entPhysicalIsFRU object is equal to 'false(2)' (e.g., the repeater ports within a repeater module), do not need their own unique asset tracking identifier.  An agent does not have to provide write access for such entities, and may instead return a zero\-length string.  If write access is implemented for an instance of entPhysicalAssetID, and a value is written into the instance, the agent must retain the supplied value in the entPhysicalAssetID instance (associated with the same physical entity) for as long as that entity remains instantiated.  This includes instantiations across all re\-initializations/reboots of the network management system, including those resulting in a change of the physical entity's entPhysicalIndex value.   If no asset tracking information is associated with the physical component, then this object will contain a zero\-length string
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: entphysicalisfru
            
            	This object indicates whether or not this physical entity is considered a 'field replaceable unit' by the vendor.  If this object contains the value 'true(1)' then this entPhysicalEntry identifies a field replaceable unit.  For all entPhysicalEntries that represent components permanently contained within a field replaceable unit, the value 'false(2)' should be returned for this object
            	**type**\: bool
            
            .. attribute:: entphysicalmfgdate
            
            	This object contains the date of manufacturing of the managed entity.  If the manufacturing date is unknown or not supported, the object is not instantiated.  The special value '0000000000000000'H may also be returned in this case
            	**type**\: str
            
            .. attribute:: entphysicaluris
            
            	This object contains additional identification information about the physical entity.  The object contains URIs and, therefore, the syntax of this object must conform to RFC 3986, section 2.  Multiple URIs may be present and are separated by white space characters.  Leading and trailing white space characters are ignored.  If no additional identification information is known about the physical entity or supported, the object is not instantiated.  A zero length octet string may also be   returned in this case
            	**type**\: str
            
            .. attribute:: ceentphysicalsecondserialnum
            
            	This object represents the vendor\-specific second serial number string for the physical entity.  The first serial number string of the physical entity is represented in the value of corresponding  instance of the 'entPhysicalSerialNum' object.  On the first instantiation of an physical entity, the value of this object is the correct vendor\-assigned second  serial number, if this information is available to the agent.   If the second serial number is unknown or non\-existent, then  the value of this object will be a zero\-length string instead.  Note that implementations which can correctly identify the second serial numbers of all installed physical entities do  not need to provide write access to this object.  Agents which cannot provide non\-volatile storage for the  second serial number strings are not required to implement  write access for this object.  Not every physical component will have a serial number, or even need one.  Physical entities for which the associated value of the entPhysicalIsFRU object is equal to 'false(2)' (e.g., the repeater ports within a repeater module), do not need their own unique serial number. An agent does not have to provide write access for such entities, and may return a zero\-length string.  If write access is implemented for an instance of 'ceEntPhysicalSecondSerialNum', and a value is written into  the instance, the agent must retain the supplied value in the 'ceEntPhysicalSecondSerialNum' instance associated with the  same physical entity for as long as that entity remains instantiated. This includes instantiations across all re\- initializations/reboots of the network management system, including those which result in a change of the physical entity's entPhysicalIndex value
            	**type**\: str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'ENTITY-MIB'
            _revision = '2005-08-10'

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
                    ('entphysicalisfru', YLeaf(YType.boolean, 'entPhysicalIsFRU')),
                    ('entphysicalmfgdate', YLeaf(YType.str, 'entPhysicalMfgDate')),
                    ('entphysicaluris', YLeaf(YType.str, 'entPhysicalUris')),
                    ('ceentphysicalsecondserialnum', YLeaf(YType.str, 'CISCO-ENTITY-EXT-MIB:ceEntPhysicalSecondSerialNum')),
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
                self.entphysicalmfgdate = None
                self.entphysicaluris = None
                self.ceentphysicalsecondserialnum = None
                self._segment_path = lambda: "entPhysicalEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "ENTITY-MIB:ENTITY-MIB/entPhysicalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ENTITYMIB.Entphysicaltable.Entphysicalentry, ['entphysicalindex', 'entphysicaldescr', 'entphysicalvendortype', 'entphysicalcontainedin', 'entphysicalclass', 'entphysicalparentrelpos', 'entphysicalname', 'entphysicalhardwarerev', 'entphysicalfirmwarerev', 'entphysicalsoftwarerev', 'entphysicalserialnum', 'entphysicalmfgname', 'entphysicalmodelname', 'entphysicalalias', 'entphysicalassetid', 'entphysicalisfru', 'entphysicalmfgdate', 'entphysicaluris', 'ceentphysicalsecondserialnum'], name, value)


    class Entlogicaltable(Entity):
        """
        This table contains one row per logical entity.  For agents
        that implement more than one naming scope, at least one
        entry must exist.  Agents which instantiate all MIB objects
        within a single naming scope are not required to implement
        this table.
        
        .. attribute:: entlogicalentry
        
        	Information about a particular logical entity.  Entities may be managed by this agent or other SNMP agents (possibly) in the same chassis
        	**type**\: list of  		 :py:class:`Entlogicalentry <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entlogicaltable.Entlogicalentry>`
        
        

        """

        _prefix = 'ENTITY-MIB'
        _revision = '2005-08-10'

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
            self._absolute_path = lambda: "ENTITY-MIB:ENTITY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYMIB.Entlogicaltable, [], name, value)


        class Entlogicalentry(Entity):
            """
            Information about a particular logical entity.  Entities
            may be managed by this agent or other SNMP agents (possibly)
            in the same chassis.
            
            .. attribute:: entlogicalindex  (key)
            
            	The value of this object uniquely identifies the logical entity.  The value should be a small positive integer; index values for different logical entities are not necessarily contiguous
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: entlogicaldescr
            
            	A textual description of the logical entity.  This object should contain a string that identifies the manufacturer's name for the logical entity, and should be set to a distinct value for each version of the logical entity
            	**type**\: str
            
            .. attribute:: entlogicaltype
            
            	An indication of the type of logical entity.  This will typically be the OBJECT IDENTIFIER name of the node in the SMI's naming hierarchy which represents the major MIB module, or the majority of the MIB modules, supported by the logical entity.  For example\:    a logical entity of a regular host/router \-> mib\-2    a logical entity of a 802.1d bridge \-> dot1dBridge    a logical entity of a 802.3 repeater \-> snmpDot3RptrMgmt If an appropriate node in the SMI's naming hierarchy cannot be identified, the value 'mib\-2' should be used
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: entlogicalcommunity
            
            	An SNMPv1 or SNMPv2C community\-string, which can be used to access detailed management information for this logical entity.  The agent should allow read access with this community string (to an appropriate subset of all managed objects) and may also return a community string based on the privileges of the request used to read this object.  Note that an agent may return a community string with read\-only privileges, even if this object is accessed with a read\-write community string.  However, the agent must take   care not to return a community string that allows more privileges than the community string used to access this object.  A compliant SNMP agent may wish to conserve naming scopes by representing multiple logical entities in a single 'default' naming scope.  This is possible when the logical entities, represented by the same value of entLogicalCommunity, have no object instances in common.  For example, 'bridge1' and 'repeater1' may be part of the main naming scope, but at least one additional community string is needed to represent 'bridge2' and 'repeater2'.  Logical entities 'bridge1' and 'repeater1' would be represented by sysOREntries associated with the 'default' naming scope.  For agents not accessible via SNMPv1 or SNMPv2C, the value of this object is the empty string.  This object may also contain an empty string if a community string has not yet been assigned by the agent, or if no community string with suitable access rights can be returned for a particular SNMP request.  Note that this object is deprecated.  Agents which implement SNMPv3 access should use the entLogicalContextEngineID and entLogicalContextName objects to identify the context associated with each logical entity.  SNMPv3 agents may return a zero\-length string for this object, or may continue to return a community string (e.g., tri\-lingual agent support)
            	**type**\: str
            
            	**length:** 0..255
            
            	**status**\: deprecated
            
            .. attribute:: entlogicaltaddress
            
            	The transport service address by which the logical entity receives network management traffic, formatted according to the corresponding value of entLogicalTDomain.  For snmpUDPDomain, a TAddress is 6 octets long\: the initial 4 octets contain the IP\-address in network\-byte order and the last 2 contain the UDP port in network\-byte order. Consult 'Transport Mappings for the Simple Network Management Protocol' (STD 62, RFC 3417 [RFC3417]) for further information on snmpUDPDomain
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: entlogicaltdomain
            
            	Indicates the kind of transport service by which the logical entity receives network management traffic. Possible values for this object are presently found in the Transport Mappings for Simple Network Management Protocol' (STD 62, RFC 3417 [RFC3417])
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: entlogicalcontextengineid
            
            	The authoritative contextEngineID that can be used to send an SNMP message concerning information held by this logical entity, to the address specified by the associated 'entLogicalTAddress/entLogicalTDomain' pair.  This object, together with the associated entLogicalContextName object, defines the context associated with a particular logical entity, and allows access to SNMP engines identified by a contextEngineId and contextName pair.  If no value has been configured by the agent, a zero\-length string is returned, or the agent may choose not to instantiate this object at all
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: entlogicalcontextname
            
            	The contextName that can be used to send an SNMP message concerning information held by this logical entity, to the address specified by the associated 'entLogicalTAddress/entLogicalTDomain' pair.  This object, together with the associated entLogicalContextEngineID object, defines the context associated with a particular logical entity, and allows   access to SNMP engines identified by a contextEngineId and contextName pair.  If no value has been configured by the agent, a zero\-length string is returned, or the agent may choose not to instantiate this object at all
            	**type**\: str
            
            

            """

            _prefix = 'ENTITY-MIB'
            _revision = '2005-08-10'

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
                self._absolute_path = lambda: "ENTITY-MIB:ENTITY-MIB/entLogicalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ENTITYMIB.Entlogicaltable.Entlogicalentry, ['entlogicalindex', 'entlogicaldescr', 'entlogicaltype', 'entlogicalcommunity', 'entlogicaltaddress', 'entlogicaltdomain', 'entlogicalcontextengineid', 'entlogicalcontextname'], name, value)


    class Entlpmappingtable(Entity):
        """
        This table contains zero or more rows of logical entity to
        physical equipment associations.  For each logical entity
        known by this agent, there are zero or more mappings to the
        physical resources, which are used to realize that logical
        entity.
        
        An agent should limit the number and nature of entries in
        this table such that only meaningful and non\-redundant
        information is returned.  For example, in a system that
        contains a single power supply, mappings between logical
        entities and the power supply are not useful and should not
        be included.
        
        Also, only the most appropriate physical component, which is
        closest to the root of a particular containment tree, should
        be identified in an entLPMapping entry.
        
        For example, suppose a bridge is realized on a particular
        module, and all ports on that module are ports on this
        bridge.  A mapping between the bridge and the module would
        be useful, but additional mappings between the bridge and
        each of the ports on that module would be redundant (because
        the entPhysicalContainedIn hierarchy can provide the same
        information).  On the other hand, if more than one bridge
        were utilizing ports on this module, then mappings between
        each bridge and the ports it used would be appropriate.
        
        Also, in the case of a single backplane repeater, a mapping
        for the backplane to the single repeater entity is not
        necessary.
        
        .. attribute:: entlpmappingentry
        
        	Information about a particular logical entity to physical equipment association.  Note that the nature of the association is not specifically identified in this entry. It is expected that sufficient information exists in the MIBs used to manage a particular logical entity to infer how physical component information is utilized
        	**type**\: list of  		 :py:class:`Entlpmappingentry <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entlpmappingtable.Entlpmappingentry>`
        
        

        """

        _prefix = 'ENTITY-MIB'
        _revision = '2005-08-10'

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
            self._absolute_path = lambda: "ENTITY-MIB:ENTITY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYMIB.Entlpmappingtable, [], name, value)


        class Entlpmappingentry(Entity):
            """
            Information about a particular logical entity to physical
            equipment association.  Note that the nature of the
            association is not specifically identified in this entry.
            It is expected that sufficient information exists in the
            MIBs used to manage a particular logical entity to infer how
            physical component information is utilized.
            
            .. attribute:: entlogicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entlogicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entlogicaltable.Entlogicalentry>`
            
            .. attribute:: entlpphysicalindex  (key)
            
            	The value of this object identifies the index value of a particular entPhysicalEntry associated with the indicated entLogicalEntity
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'ENTITY-MIB'
            _revision = '2005-08-10'

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
                    ('entlogicalindex', YLeaf(YType.str, 'entLogicalIndex')),
                    ('entlpphysicalindex', YLeaf(YType.int32, 'entLPPhysicalIndex')),
                ])
                self.entlogicalindex = None
                self.entlpphysicalindex = None
                self._segment_path = lambda: "entLPMappingEntry" + "[entLogicalIndex='" + str(self.entlogicalindex) + "']" + "[entLPPhysicalIndex='" + str(self.entlpphysicalindex) + "']"
                self._absolute_path = lambda: "ENTITY-MIB:ENTITY-MIB/entLPMappingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ENTITYMIB.Entlpmappingtable.Entlpmappingentry, ['entlogicalindex', 'entlpphysicalindex'], name, value)


    class Entaliasmappingtable(Entity):
        """
        This table contains zero or more rows, representing
        mappings of logical entity and physical component to
        external MIB identifiers.  Each physical port in the system
        may be associated with a mapping to an external identifier,
        which itself is associated with a particular logical
        entity's naming scope.  A 'wildcard' mechanism is provided
        to indicate that an identifier is associated with more than
        one logical entity.
        
        .. attribute:: entaliasmappingentry
        
        	Information about a particular physical equipment, logical   entity to external identifier binding.  Each logical entity/physical component pair may be associated with one alias mapping.  The logical entity index may also be used as a 'wildcard' (refer to the entAliasLogicalIndexOrZero object DESCRIPTION clause for details.)  Note that only entPhysicalIndex values that represent physical ports (i.e., associated entPhysicalClass value is 'port(10)') are permitted to exist in this table
        	**type**\: list of  		 :py:class:`Entaliasmappingentry <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entaliasmappingtable.Entaliasmappingentry>`
        
        

        """

        _prefix = 'ENTITY-MIB'
        _revision = '2005-08-10'

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
            self._absolute_path = lambda: "ENTITY-MIB:ENTITY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYMIB.Entaliasmappingtable, [], name, value)


        class Entaliasmappingentry(Entity):
            """
            Information about a particular physical equipment, logical
            
            
            entity to external identifier binding.  Each logical
            entity/physical component pair may be associated with one
            alias mapping.  The logical entity index may also be used as
            a 'wildcard' (refer to the entAliasLogicalIndexOrZero object
            DESCRIPTION clause for details.)
            
            Note that only entPhysicalIndex values that represent
            physical ports (i.e., associated entPhysicalClass value is
            'port(10)') are permitted to exist in this table.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: entaliaslogicalindexorzero  (key)
            
            	The value of this object identifies the logical entity that defines the naming scope for the associated instance of the 'entAliasMappingIdentifier' object.  If this object has a non\-zero value, then it identifies the logical entity named by the same value of entLogicalIndex.  If this object has a value of zero, then the mapping between the physical component and the alias identifier for this entAliasMapping entry is associated with all unspecified logical entities.  That is, a value of zero (the default mapping) identifies any logical entity that does not have an explicit entry in this table for a particular entPhysicalIndex/entAliasMappingIdentifier pair.  For example, to indicate that a particular interface (e.g., physical component 33) is identified by the same value of ifIndex for all logical entities, the following instance might exist\:          entAliasMappingIdentifier.33.0 = ifIndex.5  In the event an entPhysicalEntry is associated differently for some logical entities, additional entAliasMapping entries may exist, e.g.\:           entAliasMappingIdentifier.33.0 = ifIndex.6         entAliasMappingIdentifier.33.4 =  ifIndex.1         entAliasMappingIdentifier.33.5 =  ifIndex.1         entAliasMappingIdentifier.33.10 = ifIndex.12  Note that entries with non\-zero entAliasLogicalIndexOrZero index values have precedence over zero\-indexed entries.  In this example, all logical entities except 4, 5, and 10, associate physical entity 33 with ifIndex.6
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: entaliasmappingidentifier
            
            	The value of this object identifies a particular conceptual row associated with the indicated entPhysicalIndex and entLogicalIndex pair.  Because only physical ports are modeled in this table, only entries that represent interfaces or ports are allowed.  If an ifEntry exists on behalf of a particular physical port, then this object should identify the associated 'ifEntry'. For repeater ports, the appropriate row in the 'rptrPortGroupTable' should be identified instead.  For example, suppose a physical port was represented by entPhysicalEntry.3, entLogicalEntry.15 existed for a repeater, and entLogicalEntry.22 existed for a bridge.  Then there might be two related instances of entAliasMappingIdentifier\:    entAliasMappingIdentifier.3.15 == rptrPortGroupIndex.5.2    entAliasMappingIdentifier.3.22 == ifIndex.17 It is possible that other mappings (besides interfaces and repeater ports) may be defined in the future, as required.  Bridge ports are identified by examining the Bridge MIB and appropriate ifEntries associated with each 'dot1dBasePort', and are thus not represented in this table
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'ENTITY-MIB'
            _revision = '2005-08-10'

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
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('entaliaslogicalindexorzero', YLeaf(YType.int32, 'entAliasLogicalIndexOrZero')),
                    ('entaliasmappingidentifier', YLeaf(YType.str, 'entAliasMappingIdentifier')),
                ])
                self.entphysicalindex = None
                self.entaliaslogicalindexorzero = None
                self.entaliasmappingidentifier = None
                self._segment_path = lambda: "entAliasMappingEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[entAliasLogicalIndexOrZero='" + str(self.entaliaslogicalindexorzero) + "']"
                self._absolute_path = lambda: "ENTITY-MIB:ENTITY-MIB/entAliasMappingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ENTITYMIB.Entaliasmappingtable.Entaliasmappingentry, ['entphysicalindex', 'entaliaslogicalindexorzero', 'entaliasmappingidentifier'], name, value)


    class Entphysicalcontainstable(Entity):
        """
        A table that exposes the container/'containee'
        relationships between physical entities.  This table
        provides all the information found by constructing the
        virtual containment tree for a given entPhysicalTable, but
        in a more direct format.
        
        In the event a physical entity is contained by more than one
        other physical entity (e.g., double\-wide modules), this
        table should include these additional mappings, which cannot
        be represented in the entPhysicalTable virtual containment
        tree.
        
        .. attribute:: entphysicalcontainsentry
        
        	A single container/'containee' relationship
        	**type**\: list of  		 :py:class:`Entphysicalcontainsentry <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicalcontainstable.Entphysicalcontainsentry>`
        
        

        """

        _prefix = 'ENTITY-MIB'
        _revision = '2005-08-10'

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
            self._absolute_path = lambda: "ENTITY-MIB:ENTITY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYMIB.Entphysicalcontainstable, [], name, value)


        class Entphysicalcontainsentry(Entity):
            """
            A single container/'containee' relationship.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: entphysicalchildindex  (key)
            
            	The value of entPhysicalIndex for the contained physical entity
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'ENTITY-MIB'
            _revision = '2005-08-10'

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
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('entphysicalchildindex', YLeaf(YType.int32, 'entPhysicalChildIndex')),
                ])
                self.entphysicalindex = None
                self.entphysicalchildindex = None
                self._segment_path = lambda: "entPhysicalContainsEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[entPhysicalChildIndex='" + str(self.entphysicalchildindex) + "']"
                self._absolute_path = lambda: "ENTITY-MIB:ENTITY-MIB/entPhysicalContainsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ENTITYMIB.Entphysicalcontainstable.Entphysicalcontainsentry, ['entphysicalindex', 'entphysicalchildindex'], name, value)

    def clone_ptr(self):
        self._top_entity = ENTITYMIB()
        return self._top_entity

