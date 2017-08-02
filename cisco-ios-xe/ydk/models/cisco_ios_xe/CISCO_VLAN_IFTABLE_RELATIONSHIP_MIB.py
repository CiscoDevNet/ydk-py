""" CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB 

Cisco VLAN ifTable Relationship MIB lists VLAN\-id and ifIndex
information for routed VLAN interfaces.  

A routed VLAN interface is the router interface or sub\-interface 
to which the router's IP address on the VLAN is attached.  
For example, an ISL, SDE, or 802.1Q encapsulated
subinterface, or Switched Virtual Interface (SVI).

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoVlanIftableRelationshipMib(Entity):
    """
    
    
    .. attribute:: cvivlaninterfaceindextable
    
    	The cviVlanInterfaceIndexTable provides a way to translate a VLAN\-id in to an ifIndex, so that  the routed VLAN interface's routing configuration  can be obtained from interface entry in ipRouteTable.  Note that some routers can have interfaces to multiple VLAN management domains, and therefore can have multiple  routed VLAN interfaces which connect to different VLANs  having the same VLAN\-id.  Thus, it is possible to have  multiple rows in this table for the same VLAN\-id.  The cviVlanInterfaceIndexTable also provides a way to find the VLAN\-id from an ifTable VLAN's ifIndex
    	**type**\:   :py:class:`Cvivlaninterfaceindextable <ydk.models.cisco_ios_xe.CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB.CiscoVlanIftableRelationshipMib.Cvivlaninterfaceindextable>`
    
    

    """

    _prefix = 'CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB'
    _revision = '2013-07-15'

    def __init__(self):
        super(CiscoVlanIftableRelationshipMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB"
        self.yang_parent_name = "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB"

        self.cvivlaninterfaceindextable = CiscoVlanIftableRelationshipMib.Cvivlaninterfaceindextable()
        self.cvivlaninterfaceindextable.parent = self
        self._children_name_map["cvivlaninterfaceindextable"] = "cviVlanInterfaceIndexTable"
        self._children_yang_names.add("cviVlanInterfaceIndexTable")


    class Cvivlaninterfaceindextable(Entity):
        """
        The cviVlanInterfaceIndexTable provides a way to
        translate a VLAN\-id in to an ifIndex, so that 
        the routed VLAN interface's routing configuration 
        can be obtained from interface entry in ipRouteTable.
        
        Note that some routers can have interfaces to multiple
        VLAN management domains, and therefore can have multiple 
        routed VLAN interfaces which connect to different VLANs 
        having the same VLAN\-id.  Thus, it is possible to have 
        multiple rows in this table for the same VLAN\-id.
        
        The cviVlanInterfaceIndexTable also provides a way
        to find the VLAN\-id from an ifTable VLAN's ifIndex.
        
        .. attribute:: cvivlaninterfaceindexentry
        
        	Each entry represents a routed VLAN interface, its corresponding physical port if any, and the ifTable entry for the routed VLAN interface.  Entries are created by the agent when the routed VLAN interface is created.  Operational status of routing does not affect the entries listed here.  For routing configuration please refer to ipRouteTable.  Entries are deleted by the agent when the routed VLAN interface is removed from the system configuration
        	**type**\: list of    :py:class:`Cvivlaninterfaceindexentry <ydk.models.cisco_ios_xe.CISCO_VLAN_IFTABLE_RELATIONSHIP_MIB.CiscoVlanIftableRelationshipMib.Cvivlaninterfaceindextable.Cvivlaninterfaceindexentry>`
        
        

        """

        _prefix = 'CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB'
        _revision = '2013-07-15'

        def __init__(self):
            super(CiscoVlanIftableRelationshipMib.Cvivlaninterfaceindextable, self).__init__()

            self.yang_name = "cviVlanInterfaceIndexTable"
            self.yang_parent_name = "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB"

            self.cvivlaninterfaceindexentry = YList(self)

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
                        super(CiscoVlanIftableRelationshipMib.Cvivlaninterfaceindextable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVlanIftableRelationshipMib.Cvivlaninterfaceindextable, self).__setattr__(name, value)


        class Cvivlaninterfaceindexentry(Entity):
            """
            Each entry represents a routed VLAN interface, its
            corresponding physical port if any, and the ifTable entry
            for the routed VLAN interface.
            
            Entries are created by the agent when the routed VLAN interface
            is created.  Operational status of routing does not affect
            the entries listed here.  For routing configuration please refer
            to ipRouteTable.
            
            Entries are deleted by the agent when the routed VLAN interface
            is removed from the system configuration.
            
            .. attribute:: cvivlanid  <key>
            
            	The VLAN\-id number of the routed VLAN interface
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: cviphysicalifindex  <key>
            
            	For subinterfaces, this object is the ifIndex of the physical interface for the subinterface.  For Switch Virtual Interfaces (SVIs), this object is zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cviroutedvlanifindex
            
            	The index for the ifTable entry associated with this routed VLAN interface
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB'
            _revision = '2013-07-15'

            def __init__(self):
                super(CiscoVlanIftableRelationshipMib.Cvivlaninterfaceindextable.Cvivlaninterfaceindexentry, self).__init__()

                self.yang_name = "cviVlanInterfaceIndexEntry"
                self.yang_parent_name = "cviVlanInterfaceIndexTable"

                self.cvivlanid = YLeaf(YType.int32, "cviVlanId")

                self.cviphysicalifindex = YLeaf(YType.int32, "cviPhysicalIfIndex")

                self.cviroutedvlanifindex = YLeaf(YType.int32, "cviRoutedVlanIfIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvivlanid",
                                "cviphysicalifindex",
                                "cviroutedvlanifindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVlanIftableRelationshipMib.Cvivlaninterfaceindextable.Cvivlaninterfaceindexentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVlanIftableRelationshipMib.Cvivlaninterfaceindextable.Cvivlaninterfaceindexentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cvivlanid.is_set or
                    self.cviphysicalifindex.is_set or
                    self.cviroutedvlanifindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvivlanid.yfilter != YFilter.not_set or
                    self.cviphysicalifindex.yfilter != YFilter.not_set or
                    self.cviroutedvlanifindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cviVlanInterfaceIndexEntry" + "[cviVlanId='" + self.cvivlanid.get() + "']" + "[cviPhysicalIfIndex='" + self.cviphysicalifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB/cviVlanInterfaceIndexTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvivlanid.is_set or self.cvivlanid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvivlanid.get_name_leafdata())
                if (self.cviphysicalifindex.is_set or self.cviphysicalifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cviphysicalifindex.get_name_leafdata())
                if (self.cviroutedvlanifindex.is_set or self.cviroutedvlanifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cviroutedvlanifindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cviVlanId" or name == "cviPhysicalIfIndex" or name == "cviRoutedVlanIfIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cviVlanId"):
                    self.cvivlanid = value
                    self.cvivlanid.value_namespace = name_space
                    self.cvivlanid.value_namespace_prefix = name_space_prefix
                if(value_path == "cviPhysicalIfIndex"):
                    self.cviphysicalifindex = value
                    self.cviphysicalifindex.value_namespace = name_space
                    self.cviphysicalifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cviRoutedVlanIfIndex"):
                    self.cviroutedvlanifindex = value
                    self.cviroutedvlanifindex.value_namespace = name_space
                    self.cviroutedvlanifindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvivlaninterfaceindexentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvivlaninterfaceindexentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cviVlanInterfaceIndexTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cviVlanInterfaceIndexEntry"):
                for c in self.cvivlaninterfaceindexentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVlanIftableRelationshipMib.Cvivlaninterfaceindextable.Cvivlaninterfaceindexentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvivlaninterfaceindexentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cviVlanInterfaceIndexEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.cvivlaninterfaceindextable is not None and self.cvivlaninterfaceindextable.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cvivlaninterfaceindextable is not None and self.cvivlaninterfaceindextable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB:CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB" + path_buffer

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

        if (child_yang_name == "cviVlanInterfaceIndexTable"):
            if (self.cvivlaninterfaceindextable is None):
                self.cvivlaninterfaceindextable = CiscoVlanIftableRelationshipMib.Cvivlaninterfaceindextable()
                self.cvivlaninterfaceindextable.parent = self
                self._children_name_map["cvivlaninterfaceindextable"] = "cviVlanInterfaceIndexTable"
            return self.cvivlaninterfaceindextable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cviVlanInterfaceIndexTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoVlanIftableRelationshipMib()
        return self._top_entity

