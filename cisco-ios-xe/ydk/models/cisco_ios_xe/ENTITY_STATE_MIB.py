""" ENTITY_STATE_MIB 

This MIB defines a state extension to the Entity MIB.

Copyright (C) The Internet Society 2005.  This version
of this MIB module is part of RFC 4268; see the RFC
itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EntityStateMib(Entity):
    """
    
    
    .. attribute:: entstatetable
    
    	A table of information about state/status of entities. This is a sparse augment of the entPhysicalTable.  Entries appear in this table for values of entPhysicalClass [RFC4133] that in this implementation are able to report any of the state or status stored in this table
    	**type**\:   :py:class:`Entstatetable <ydk.models.cisco_ios_xe.ENTITY_STATE_MIB.EntityStateMib.Entstatetable>`
    
    

    """

    _prefix = 'ENTITY-STATE-MIB'
    _revision = '2005-11-22'

    def __init__(self):
        super(EntityStateMib, self).__init__()
        self._top_entity = None

        self.yang_name = "ENTITY-STATE-MIB"
        self.yang_parent_name = "ENTITY-STATE-MIB"

        self.entstatetable = EntityStateMib.Entstatetable()
        self.entstatetable.parent = self
        self._children_name_map["entstatetable"] = "entStateTable"
        self._children_yang_names.add("entStateTable")


    class Entstatetable(Entity):
        """
        A table of information about state/status of entities.
        This is a sparse augment of the entPhysicalTable.  Entries
        appear in this table for values of
        entPhysicalClass [RFC4133] that in this implementation
        are able to report any of the state or status stored in
        this table.
        
        .. attribute:: entstateentry
        
        	State information about this physical entity
        	**type**\: list of    :py:class:`Entstateentry <ydk.models.cisco_ios_xe.ENTITY_STATE_MIB.EntityStateMib.Entstatetable.Entstateentry>`
        
        

        """

        _prefix = 'ENTITY-STATE-MIB'
        _revision = '2005-11-22'

        def __init__(self):
            super(EntityStateMib.Entstatetable, self).__init__()

            self.yang_name = "entStateTable"
            self.yang_parent_name = "ENTITY-STATE-MIB"

            self.entstateentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EntityStateMib.Entstatetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EntityStateMib.Entstatetable, self).__setattr__(name, value)


        class Entstateentry(Entity):
            """
            State information about this physical entity.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: entstateadmin
            
            	The administrative state for this entity.  This object refers to an entities administrative permission to service both other entities within its containment hierarchy as well other users of its services defined by means outside the scope of this MIB.  Setting this object to 'notSupported' will result in an 'inconsistentValue' error.  For entities that do not support administrative state, all set operations will result in an 'inconsistentValue' error.  Some physical entities exhibit only a subset of the remaining administrative state values.  Some entities cannot be locked, and hence this object exhibits only the 'unlocked' state.  Other entities cannot be shutdown gracefully, and hence this object does not exhibit the 'shuttingDown' state.  A value of 'inconsistentValue' will be returned if attempts are made to set this object to values not supported by its administrative model
            	**type**\:   :py:class:`Entityadminstate <ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB.Entityadminstate>`
            
            .. attribute:: entstatealarm
            
            	The alarm status for this entity.  It does not include the alarms raised on child components within its containment hierarchy.  A value of 'unknown' means that this entity is  unable to report alarm state.  Note that this differs from 'indeterminate', which means that alarm state is supported and there are alarms against this entity, but the severity of some of the alarms is not known.  If no bits are set, then this entity supports reporting of alarms, but there are currently no active alarms against this entity
            	**type**\:   :py:class:`Entityalarmstatus <ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB.Entityalarmstatus>`
            
            .. attribute:: entstatelastchanged
            
            	The value of this object is the date and time when the value of any of entStateAdmin, entStateOper, entStateUsage, entStateAlarm, or entStateStandby changed for this entity.  If there has been no change since the last re\-initialization of the local system, this object contains the date and time of local system initialization.  If there has been no change since the entity was added to the local system, this object contains the date and time of the insertion
            	**type**\:  str
            
            .. attribute:: entstateoper
            
            	The operational state for this entity.  Note that unlike the state model used within the Interfaces MIB [RFC2863], this object does not follow the administrative state.  An administrative state of down does not predict an operational state of disabled.  A value of 'testing' means that entity currently being tested and cannot therefore report whether it is operational or not.  A value of 'disabled' means that an entity is totally inoperable and unable to provide service both to entities within its containment hierarchy, or to other receivers of its service as defined in ways outside the scope of this MIB.  A value of 'enabled' means that an entity is fully or partially operable and able to provide service both to  entities within its containment hierarchy, or to other receivers of its service as defined in ways outside the scope of this MIB.  Note that some implementations may not be able to accurately report entStateOper while the entStateAdmin object has a value other than 'unlocked'. In these cases, this object MUST have a value of 'unknown'
            	**type**\:   :py:class:`Entityoperstate <ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB.Entityoperstate>`
            
            .. attribute:: entstatestandby
            
            	The standby status for this entity.  Some entities will exhibit only a subset of the remaining standby state values.  If this entity cannot operate in a standby role, the value of this object will always be 'providingService'
            	**type**\:   :py:class:`Entitystandbystatus <ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB.Entitystandbystatus>`
            
            .. attribute:: entstateusage
            
            	The usage state for this entity.  This object refers to an entity's ability to service more physical entities in a containment hierarchy.  A value of 'idle' means this entity is able to contain other entities but that no other entity is currently contained within this entity.  A value of 'active' means that at least one entity is contained within this entity, but that it could handle more.  A value of 'busy' means that the entity is unable to handle any additional entities being contained in it.  Some entities will exhibit only a subset of the usage state values.  Entities that are unable to ever service any entities within a containment hierarchy will always have a usage state of 'busy'.  Some entities will only ever be able to support one entity within its containment hierarchy and will therefore only exhibit values of 'idle' and 'busy'
            	**type**\:   :py:class:`Entityusagestate <ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB.Entityusagestate>`
            
            

            """

            _prefix = 'ENTITY-STATE-MIB'
            _revision = '2005-11-22'

            def __init__(self):
                super(EntityStateMib.Entstatetable.Entstateentry, self).__init__()

                self.yang_name = "entStateEntry"
                self.yang_parent_name = "entStateTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.entstateadmin = YLeaf(YType.enumeration, "entStateAdmin")

                self.entstatealarm = YLeaf(YType.bits, "entStateAlarm")

                self.entstatelastchanged = YLeaf(YType.str, "entStateLastChanged")

                self.entstateoper = YLeaf(YType.enumeration, "entStateOper")

                self.entstatestandby = YLeaf(YType.enumeration, "entStateStandby")

                self.entstateusage = YLeaf(YType.enumeration, "entStateUsage")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "entstateadmin",
                                "entstatealarm",
                                "entstatelastchanged",
                                "entstateoper",
                                "entstatestandby",
                                "entstateusage") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EntityStateMib.Entstatetable.Entstateentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EntityStateMib.Entstatetable.Entstateentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.entstateadmin.is_set or
                    self.entstatealarm.is_set or
                    self.entstatelastchanged.is_set or
                    self.entstateoper.is_set or
                    self.entstatestandby.is_set or
                    self.entstateusage.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.entstateadmin.yfilter != YFilter.not_set or
                    self.entstatealarm.yfilter != YFilter.not_set or
                    self.entstatelastchanged.yfilter != YFilter.not_set or
                    self.entstateoper.yfilter != YFilter.not_set or
                    self.entstatestandby.yfilter != YFilter.not_set or
                    self.entstateusage.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "entStateEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ENTITY-STATE-MIB:ENTITY-STATE-MIB/entStateTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.entstateadmin.is_set or self.entstateadmin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entstateadmin.get_name_leafdata())
                if (self.entstatealarm.is_set or self.entstatealarm.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entstatealarm.get_name_leafdata())
                if (self.entstatelastchanged.is_set or self.entstatelastchanged.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entstatelastchanged.get_name_leafdata())
                if (self.entstateoper.is_set or self.entstateoper.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entstateoper.get_name_leafdata())
                if (self.entstatestandby.is_set or self.entstatestandby.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entstatestandby.get_name_leafdata())
                if (self.entstateusage.is_set or self.entstateusage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entstateusage.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "entStateAdmin" or name == "entStateAlarm" or name == "entStateLastChanged" or name == "entStateOper" or name == "entStateStandby" or name == "entStateUsage"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "entStateAdmin"):
                    self.entstateadmin = value
                    self.entstateadmin.value_namespace = name_space
                    self.entstateadmin.value_namespace_prefix = name_space_prefix
                if(value_path == "entStateAlarm"):
                    self.entstatealarm[value] = True
                if(value_path == "entStateLastChanged"):
                    self.entstatelastchanged = value
                    self.entstatelastchanged.value_namespace = name_space
                    self.entstatelastchanged.value_namespace_prefix = name_space_prefix
                if(value_path == "entStateOper"):
                    self.entstateoper = value
                    self.entstateoper.value_namespace = name_space
                    self.entstateoper.value_namespace_prefix = name_space_prefix
                if(value_path == "entStateStandby"):
                    self.entstatestandby = value
                    self.entstatestandby.value_namespace = name_space
                    self.entstatestandby.value_namespace_prefix = name_space_prefix
                if(value_path == "entStateUsage"):
                    self.entstateusage = value
                    self.entstateusage.value_namespace = name_space
                    self.entstateusage.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.entstateentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.entstateentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "entStateTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ENTITY-STATE-MIB:ENTITY-STATE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "entStateEntry"):
                for c in self.entstateentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EntityStateMib.Entstatetable.Entstateentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.entstateentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "entStateEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.entstatetable is not None and self.entstatetable.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.entstatetable is not None and self.entstatetable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ENTITY-STATE-MIB:ENTITY-STATE-MIB" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "entStateTable"):
            if (self.entstatetable is None):
                self.entstatetable = EntityStateMib.Entstatetable()
                self.entstatetable.parent = self
                self._children_name_map["entstatetable"] = "entStateTable"
            return self.entstatetable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "entStateTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EntityStateMib()
        return self._top_entity

