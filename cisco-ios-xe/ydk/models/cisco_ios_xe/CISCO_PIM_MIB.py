""" CISCO_PIM_MIB 

This MIB module defines the cisco specific variables
for Protocol Independent Multicast (PIM) management. 
These definitions are an extension of those defined in
the IETF PIM MIB (RFC 2934).

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoPimMib(Entity):
    """
    
    
    .. attribute:: ciscopimmibnotificationobjects
    
    	
    	**type**\:   :py:class:`Ciscopimmibnotificationobjects <ydk.models.cisco_ios_xe.CISCO_PIM_MIB.CiscoPimMib.Ciscopimmibnotificationobjects>`
    
    .. attribute:: cpim
    
    	
    	**type**\:   :py:class:`Cpim <ydk.models.cisco_ios_xe.CISCO_PIM_MIB.CiscoPimMib.Cpim>`
    
    

    """

    _prefix = 'CISCO-PIM-MIB'
    _revision = '2000-11-02'

    def __init__(self):
        super(CiscoPimMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-PIM-MIB"
        self.yang_parent_name = "CISCO-PIM-MIB"

        self.ciscopimmibnotificationobjects = CiscoPimMib.Ciscopimmibnotificationobjects()
        self.ciscopimmibnotificationobjects.parent = self
        self._children_name_map["ciscopimmibnotificationobjects"] = "ciscoPimMIBNotificationObjects"
        self._children_yang_names.add("ciscoPimMIBNotificationObjects")

        self.cpim = CiscoPimMib.Cpim()
        self.cpim.parent = self
        self._children_name_map["cpim"] = "cpim"
        self._children_yang_names.add("cpim")


    class Cpim(Entity):
        """
        
        
        .. attribute:: cpiminvalidjoinprunemsgsrcvd
        
        	A count of the number of invalid PIM Join/Prune messages received by this device. A PIM Join/Prune message is termed invalid if  o the RP specified in the packet is not the RP for   the group in question
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpiminvalidregistermsgsrcvd
        
        	A count of the number of invalid PIM Register messages received by this device. A PIM Register message is termed invalid if  o the encapsulated IP header is malformed, o the destination of the PIM Register message is not the   RP (Rendezvous Point) for the group in question, o the source/DR (Designated Router) address is not a valid   unicast address
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpimlasterrorgroup
        
        	The IP multicast group address to which the last invalid packet was addressed. The type of address stored depends on the value in cpimLastErrorGroupType.   The value of this object is a zero\-length InetAddress if there is a problem in the packet received from the DR, for eg. a malformed encapsulated IP header.   The value of this object is irrelevant if the value of cpimLastErrorType is none(1)
        	**type**\:  str
        
        	**length:** 0..255
        
        .. attribute:: cpimlasterrorgrouptype
        
        	Represents the type of address stored in cpimLastErrorGroup. The value of this object is unknown(0) if there is a problem in the packet received from the DR.  The value of this object is irrelevant if the value of cpimLastErrorType is none(1)
        	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
        
        .. attribute:: cpimlasterrororigin
        
        	This object represents the Network Layer Address of the source that originated the last invalid packet. The type of address stored depends on the value in cpimLastErrorOriginType.   The value of this object represents the Network Layer Address of the Designated Router (DR) whenever the value of cpimLastErrorGroup is a zero\-length address,  for eg. when encapsulated IP header is malformed.  The value of this object is irrelevant if the value of cpimLastErrorType is none(1)
        	**type**\:  str
        
        	**length:** 0..255
        
        .. attribute:: cpimlasterrororigintype
        
        	Represents the type of address stored in cpimLastErrorOrigin. The value of this object is irrelevant if the value of cpimLastErrorType is none(1)
        	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
        
        .. attribute:: cpimlasterrorrp
        
        	The address of the RP, as per the last invalid packet. The type of address stored depends on the value in cpimLastErrorRPType.   The value of this object is irrelevant if the value of cpimLastErrorType is none(1)
        	**type**\:  str
        
        	**length:** 0..255
        
        .. attribute:: cpimlasterrorrptype
        
        	Represents the type of address stored in cpimLastErrorRP. The value of this object is irrelevant if the value of cpimLastErrorType is none(1)
        	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
        
        .. attribute:: cpimlasterrortype
        
        	The type of the last invalid message that was received by this device
        	**type**\:   :py:class:`Cpimlasterrortype <ydk.models.cisco_ios_xe.CISCO_PIM_MIB.CiscoPimMib.Cpim.Cpimlasterrortype>`
        
        

        """

        _prefix = 'CISCO-PIM-MIB'
        _revision = '2000-11-02'

        def __init__(self):
            super(CiscoPimMib.Cpim, self).__init__()

            self.yang_name = "cpim"
            self.yang_parent_name = "CISCO-PIM-MIB"

            self.cpiminvalidjoinprunemsgsrcvd = YLeaf(YType.uint32, "cpimInvalidJoinPruneMsgsRcvd")

            self.cpiminvalidregistermsgsrcvd = YLeaf(YType.uint32, "cpimInvalidRegisterMsgsRcvd")

            self.cpimlasterrorgroup = YLeaf(YType.str, "cpimLastErrorGroup")

            self.cpimlasterrorgrouptype = YLeaf(YType.enumeration, "cpimLastErrorGroupType")

            self.cpimlasterrororigin = YLeaf(YType.str, "cpimLastErrorOrigin")

            self.cpimlasterrororigintype = YLeaf(YType.enumeration, "cpimLastErrorOriginType")

            self.cpimlasterrorrp = YLeaf(YType.str, "cpimLastErrorRP")

            self.cpimlasterrorrptype = YLeaf(YType.enumeration, "cpimLastErrorRPType")

            self.cpimlasterrortype = YLeaf(YType.enumeration, "cpimLastErrorType")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cpiminvalidjoinprunemsgsrcvd",
                            "cpiminvalidregistermsgsrcvd",
                            "cpimlasterrorgroup",
                            "cpimlasterrorgrouptype",
                            "cpimlasterrororigin",
                            "cpimlasterrororigintype",
                            "cpimlasterrorrp",
                            "cpimlasterrorrptype",
                            "cpimlasterrortype") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoPimMib.Cpim, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPimMib.Cpim, self).__setattr__(name, value)

        class Cpimlasterrortype(Enum):
            """
            Cpimlasterrortype

            The type of the last invalid message that was received by

            this device.

            .. data:: none = 1

            .. data:: invalidRegister = 2

            .. data:: invalidJoinPrune = 3

            """

            none = Enum.YLeaf(1, "none")

            invalidRegister = Enum.YLeaf(2, "invalidRegister")

            invalidJoinPrune = Enum.YLeaf(3, "invalidJoinPrune")


        def has_data(self):
            return (
                self.cpiminvalidjoinprunemsgsrcvd.is_set or
                self.cpiminvalidregistermsgsrcvd.is_set or
                self.cpimlasterrorgroup.is_set or
                self.cpimlasterrorgrouptype.is_set or
                self.cpimlasterrororigin.is_set or
                self.cpimlasterrororigintype.is_set or
                self.cpimlasterrorrp.is_set or
                self.cpimlasterrorrptype.is_set or
                self.cpimlasterrortype.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cpiminvalidjoinprunemsgsrcvd.yfilter != YFilter.not_set or
                self.cpiminvalidregistermsgsrcvd.yfilter != YFilter.not_set or
                self.cpimlasterrorgroup.yfilter != YFilter.not_set or
                self.cpimlasterrorgrouptype.yfilter != YFilter.not_set or
                self.cpimlasterrororigin.yfilter != YFilter.not_set or
                self.cpimlasterrororigintype.yfilter != YFilter.not_set or
                self.cpimlasterrorrp.yfilter != YFilter.not_set or
                self.cpimlasterrorrptype.yfilter != YFilter.not_set or
                self.cpimlasterrortype.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpim" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PIM-MIB:CISCO-PIM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cpiminvalidjoinprunemsgsrcvd.is_set or self.cpiminvalidjoinprunemsgsrcvd.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpiminvalidjoinprunemsgsrcvd.get_name_leafdata())
            if (self.cpiminvalidregistermsgsrcvd.is_set or self.cpiminvalidregistermsgsrcvd.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpiminvalidregistermsgsrcvd.get_name_leafdata())
            if (self.cpimlasterrorgroup.is_set or self.cpimlasterrorgroup.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpimlasterrorgroup.get_name_leafdata())
            if (self.cpimlasterrorgrouptype.is_set or self.cpimlasterrorgrouptype.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpimlasterrorgrouptype.get_name_leafdata())
            if (self.cpimlasterrororigin.is_set or self.cpimlasterrororigin.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpimlasterrororigin.get_name_leafdata())
            if (self.cpimlasterrororigintype.is_set or self.cpimlasterrororigintype.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpimlasterrororigintype.get_name_leafdata())
            if (self.cpimlasterrorrp.is_set or self.cpimlasterrorrp.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpimlasterrorrp.get_name_leafdata())
            if (self.cpimlasterrorrptype.is_set or self.cpimlasterrorrptype.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpimlasterrorrptype.get_name_leafdata())
            if (self.cpimlasterrortype.is_set or self.cpimlasterrortype.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpimlasterrortype.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpimInvalidJoinPruneMsgsRcvd" or name == "cpimInvalidRegisterMsgsRcvd" or name == "cpimLastErrorGroup" or name == "cpimLastErrorGroupType" or name == "cpimLastErrorOrigin" or name == "cpimLastErrorOriginType" or name == "cpimLastErrorRP" or name == "cpimLastErrorRPType" or name == "cpimLastErrorType"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cpimInvalidJoinPruneMsgsRcvd"):
                self.cpiminvalidjoinprunemsgsrcvd = value
                self.cpiminvalidjoinprunemsgsrcvd.value_namespace = name_space
                self.cpiminvalidjoinprunemsgsrcvd.value_namespace_prefix = name_space_prefix
            if(value_path == "cpimInvalidRegisterMsgsRcvd"):
                self.cpiminvalidregistermsgsrcvd = value
                self.cpiminvalidregistermsgsrcvd.value_namespace = name_space
                self.cpiminvalidregistermsgsrcvd.value_namespace_prefix = name_space_prefix
            if(value_path == "cpimLastErrorGroup"):
                self.cpimlasterrorgroup = value
                self.cpimlasterrorgroup.value_namespace = name_space
                self.cpimlasterrorgroup.value_namespace_prefix = name_space_prefix
            if(value_path == "cpimLastErrorGroupType"):
                self.cpimlasterrorgrouptype = value
                self.cpimlasterrorgrouptype.value_namespace = name_space
                self.cpimlasterrorgrouptype.value_namespace_prefix = name_space_prefix
            if(value_path == "cpimLastErrorOrigin"):
                self.cpimlasterrororigin = value
                self.cpimlasterrororigin.value_namespace = name_space
                self.cpimlasterrororigin.value_namespace_prefix = name_space_prefix
            if(value_path == "cpimLastErrorOriginType"):
                self.cpimlasterrororigintype = value
                self.cpimlasterrororigintype.value_namespace = name_space
                self.cpimlasterrororigintype.value_namespace_prefix = name_space_prefix
            if(value_path == "cpimLastErrorRP"):
                self.cpimlasterrorrp = value
                self.cpimlasterrorrp.value_namespace = name_space
                self.cpimlasterrorrp.value_namespace_prefix = name_space_prefix
            if(value_path == "cpimLastErrorRPType"):
                self.cpimlasterrorrptype = value
                self.cpimlasterrorrptype.value_namespace = name_space
                self.cpimlasterrorrptype.value_namespace_prefix = name_space_prefix
            if(value_path == "cpimLastErrorType"):
                self.cpimlasterrortype = value
                self.cpimlasterrortype.value_namespace = name_space
                self.cpimlasterrortype.value_namespace_prefix = name_space_prefix


    class Ciscopimmibnotificationobjects(Entity):
        """
        
        
        .. attribute:: cpimrpmappingchangetype
        
        	Describes the operation that resulted in generation of cpimRPMappingChange notification.  o newMapping, as the name suggests indicates that a new   mapping has been added into the pimRPSetTable,  o deletedMapping indicates that a mapping has been    deleted from the pimRPSetTable, and, o modifiedXXXMapping indicates that an RP mapping (which   already existed in the table) has been modified.   The two modifications types i.e. modifiedOldMapping   and modifiedNewMapping, are defined to differentiate   the notification generated before modification from   that generated after modification
        	**type**\:   :py:class:`Cpimrpmappingchangetype <ydk.models.cisco_ios_xe.CISCO_PIM_MIB.CiscoPimMib.Ciscopimmibnotificationobjects.Cpimrpmappingchangetype>`
        
        

        """

        _prefix = 'CISCO-PIM-MIB'
        _revision = '2000-11-02'

        def __init__(self):
            super(CiscoPimMib.Ciscopimmibnotificationobjects, self).__init__()

            self.yang_name = "ciscoPimMIBNotificationObjects"
            self.yang_parent_name = "CISCO-PIM-MIB"

            self.cpimrpmappingchangetype = YLeaf(YType.enumeration, "cpimRPMappingChangeType")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cpimrpmappingchangetype") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoPimMib.Ciscopimmibnotificationobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPimMib.Ciscopimmibnotificationobjects, self).__setattr__(name, value)

        class Cpimrpmappingchangetype(Enum):
            """
            Cpimrpmappingchangetype

            Describes the operation that resulted in generation

            of cpimRPMappingChange notification.

            o newMapping, as the name suggests indicates that a new

              mapping has been added into the pimRPSetTable, 

            o deletedMapping indicates that a mapping has been 

              deleted from the pimRPSetTable, and,

            o modifiedXXXMapping indicates that an RP mapping (which

              already existed in the table) has been modified.

              The two modifications types i.e. modifiedOldMapping

              and modifiedNewMapping, are defined to differentiate

              the notification generated before modification from

              that generated after modification.

            .. data:: newMapping = 1

            .. data:: deletedMapping = 2

            .. data:: modifiedOldMapping = 3

            .. data:: modifiedNewMapping = 4

            """

            newMapping = Enum.YLeaf(1, "newMapping")

            deletedMapping = Enum.YLeaf(2, "deletedMapping")

            modifiedOldMapping = Enum.YLeaf(3, "modifiedOldMapping")

            modifiedNewMapping = Enum.YLeaf(4, "modifiedNewMapping")


        def has_data(self):
            return self.cpimrpmappingchangetype.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cpimrpmappingchangetype.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoPimMIBNotificationObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PIM-MIB:CISCO-PIM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cpimrpmappingchangetype.is_set or self.cpimrpmappingchangetype.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpimrpmappingchangetype.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpimRPMappingChangeType"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cpimRPMappingChangeType"):
                self.cpimrpmappingchangetype = value
                self.cpimrpmappingchangetype.value_namespace = name_space
                self.cpimrpmappingchangetype.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.ciscopimmibnotificationobjects is not None and self.ciscopimmibnotificationobjects.has_data()) or
            (self.cpim is not None and self.cpim.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ciscopimmibnotificationobjects is not None and self.ciscopimmibnotificationobjects.has_operation()) or
            (self.cpim is not None and self.cpim.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-PIM-MIB:CISCO-PIM-MIB" + path_buffer

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

        if (child_yang_name == "ciscoPimMIBNotificationObjects"):
            if (self.ciscopimmibnotificationobjects is None):
                self.ciscopimmibnotificationobjects = CiscoPimMib.Ciscopimmibnotificationobjects()
                self.ciscopimmibnotificationobjects.parent = self
                self._children_name_map["ciscopimmibnotificationobjects"] = "ciscoPimMIBNotificationObjects"
            return self.ciscopimmibnotificationobjects

        if (child_yang_name == "cpim"):
            if (self.cpim is None):
                self.cpim = CiscoPimMib.Cpim()
                self.cpim.parent = self
                self._children_name_map["cpim"] = "cpim"
            return self.cpim

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ciscoPimMIBNotificationObjects" or name == "cpim"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoPimMib()
        return self._top_entity

