""" oc_mapping_acl 

This module defines mapping state data
that must be saved to implement the openconfig\-acl
model because the capabilities are not implemented
on XE devices

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AclMapping(Entity):
    """
    Top level enclosing container for ACL model config
    and operational state data
    
    .. attribute:: acl_sets
    
    	Access list entries variables enclosing container
    	**type**\:   :py:class:`AclSets <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.AclSets>`
    
    .. attribute:: interfaces
    
    	Enclosing container for the list of interfaces on which ACLs are set
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces>`
    
    

    """

    _prefix = 'oc-map-acl'
    _revision = '2017-01-17'

    def __init__(self):
        super(AclMapping, self).__init__()
        self._top_entity = None

        self.yang_name = "acl-mapping"
        self.yang_parent_name = "oc-mapping-acl"

        self.acl_sets = AclMapping.AclSets()
        self.acl_sets.parent = self
        self._children_name_map["acl_sets"] = "acl-sets"
        self._children_yang_names.add("acl-sets")

        self.interfaces = AclMapping.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")


    class AclSets(Entity):
        """
        Access list entries variables enclosing container
        
        .. attribute:: acl_set
        
        	List of ACL sets, each comprising of a list of ACL entries
        	**type**\: list of    :py:class:`AclSet <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.AclSets.AclSet>`
        
        

        """

        _prefix = 'oc-map-acl'
        _revision = '2017-01-17'

        def __init__(self):
            super(AclMapping.AclSets, self).__init__()

            self.yang_name = "acl-sets"
            self.yang_parent_name = "acl-mapping"

            self.acl_set = YList(self)

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
                        super(AclMapping.AclSets, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AclMapping.AclSets, self).__setattr__(name, value)


        class AclSet(Entity):
            """
            List of ACL sets, each comprising of a list of ACL
            entries
            
            .. attribute:: name  <key>
            
            	Reference to the name list key
            	**type**\:  str
            
            .. attribute:: config
            
            	Access list config
            	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.AclSets.AclSet.Config>`
            
            

            """

            _prefix = 'oc-map-acl'
            _revision = '2017-01-17'

            def __init__(self):
                super(AclMapping.AclSets.AclSet, self).__init__()

                self.yang_name = "acl-set"
                self.yang_parent_name = "acl-sets"

                self.name = YLeaf(YType.str, "name")

                self.config = AclMapping.AclSets.AclSet.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(AclMapping.AclSets.AclSet, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(AclMapping.AclSets.AclSet, self).__setattr__(name, value)


            class Config(Entity):
                """
                Access list config
                
                .. attribute:: acl_entries
                
                	Access list entries container
                	**type**\:   :py:class:`AclEntries <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.AclSets.AclSet.Config.AclEntries>`
                
                .. attribute:: acl_type
                
                	The type of the access\-list set
                	**type**\:   :py:class:`IpVersion <ydk.models.ietf.ietf_inet_types.IpVersion>`
                
                .. attribute:: description
                
                	Description, or comment, for the ACL set
                	**type**\:  str
                
                .. attribute:: name
                
                	The name of the access\-list set
                	**type**\:  str
                
                

                """

                _prefix = 'oc-map-acl'
                _revision = '2017-01-17'

                def __init__(self):
                    super(AclMapping.AclSets.AclSet.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "acl-set"

                    self.acl_type = YLeaf(YType.enumeration, "acl-type")

                    self.description = YLeaf(YType.str, "description")

                    self.name = YLeaf(YType.str, "name")

                    self.acl_entries = AclMapping.AclSets.AclSet.Config.AclEntries()
                    self.acl_entries.parent = self
                    self._children_name_map["acl_entries"] = "acl-entries"
                    self._children_yang_names.add("acl-entries")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("acl_type",
                                    "description",
                                    "name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(AclMapping.AclSets.AclSet.Config, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AclMapping.AclSets.AclSet.Config, self).__setattr__(name, value)


                class AclEntries(Entity):
                    """
                    Access list entries container
                    
                    .. attribute:: acl_entry
                    
                    	List of ACL entries comprising an ACL set
                    	**type**\: list of    :py:class:`AclEntry <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.AclSets.AclSet.Config.AclEntries.AclEntry>`
                    
                    

                    """

                    _prefix = 'oc-map-acl'
                    _revision = '2017-01-17'

                    def __init__(self):
                        super(AclMapping.AclSets.AclSet.Config.AclEntries, self).__init__()

                        self.yang_name = "acl-entries"
                        self.yang_parent_name = "config"

                        self.acl_entry = YList(self)

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
                                    super(AclMapping.AclSets.AclSet.Config.AclEntries, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AclMapping.AclSets.AclSet.Config.AclEntries, self).__setattr__(name, value)


                    class AclEntry(Entity):
                        """
                        List of ACL entries comprising an ACL set
                        
                        .. attribute:: sequence_id  <key>
                        
                        	The sequence id determines the order in which ACL entries are applied.  The sequence id must be unique for each entry in an ACL set.  Target devices should apply the ACL entry rules in the order determined by sequence id, rather than the relying only on order in the list
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_version
                        
                        	IP version of the header
                        	**type**\:   :py:class:`IpVersion <ydk.models.ietf.ietf_inet_types.IpVersion>`
                        
                        

                        """

                        _prefix = 'oc-map-acl'
                        _revision = '2017-01-17'

                        def __init__(self):
                            super(AclMapping.AclSets.AclSet.Config.AclEntries.AclEntry, self).__init__()

                            self.yang_name = "acl-entry"
                            self.yang_parent_name = "acl-entries"

                            self.sequence_id = YLeaf(YType.uint32, "sequence-id")

                            self.ip_version = YLeaf(YType.enumeration, "ip-version")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("sequence_id",
                                            "ip_version") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(AclMapping.AclSets.AclSet.Config.AclEntries.AclEntry, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AclMapping.AclSets.AclSet.Config.AclEntries.AclEntry, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.sequence_id.is_set or
                                self.ip_version.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.sequence_id.yfilter != YFilter.not_set or
                                self.ip_version.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "acl-entry" + "[sequence-id='" + self.sequence_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.sequence_id.is_set or self.sequence_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sequence_id.get_name_leafdata())
                            if (self.ip_version.is_set or self.ip_version.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_version.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sequence-id" or name == "ip-version"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "sequence-id"):
                                self.sequence_id = value
                                self.sequence_id.value_namespace = name_space
                                self.sequence_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-version"):
                                self.ip_version = value
                                self.ip_version.value_namespace = name_space
                                self.ip_version.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.acl_entry:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.acl_entry:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "acl-entries" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "acl-entry"):
                            for c in self.acl_entry:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = AclMapping.AclSets.AclSet.Config.AclEntries.AclEntry()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.acl_entry.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "acl-entry"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.acl_type.is_set or
                        self.description.is_set or
                        self.name.is_set or
                        (self.acl_entries is not None and self.acl_entries.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.acl_type.yfilter != YFilter.not_set or
                        self.description.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        (self.acl_entries is not None and self.acl_entries.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "config" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.acl_type.is_set or self.acl_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.acl_type.get_name_leafdata())
                    if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.description.get_name_leafdata())
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "acl-entries"):
                        if (self.acl_entries is None):
                            self.acl_entries = AclMapping.AclSets.AclSet.Config.AclEntries()
                            self.acl_entries.parent = self
                            self._children_name_map["acl_entries"] = "acl-entries"
                        return self.acl_entries

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "acl-entries" or name == "acl-type" or name == "description" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "acl-type"):
                        self.acl_type = value
                        self.acl_type.value_namespace = name_space
                        self.acl_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "description"):
                        self.description = value
                        self.description.value_namespace = name_space
                        self.description.value_namespace_prefix = name_space_prefix
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.name.is_set or
                    (self.config is not None and self.config.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    (self.config is not None and self.config.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "acl-set" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "oc-mapping-acl:acl-mapping/acl-sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "config"):
                    if (self.config is None):
                        self.config = AclMapping.AclSets.AclSet.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                    return self.config

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "config" or name == "name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.acl_set:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.acl_set:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "acl-sets" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "oc-mapping-acl:acl-mapping/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "acl-set"):
                for c in self.acl_set:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = AclMapping.AclSets.AclSet()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.acl_set.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "acl-set"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Interfaces(Entity):
        """
        Enclosing container for the list of interfaces on which
        ACLs are set
        
        .. attribute:: interface
        
        	List of interfaces on which ACLs are set
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface>`
        
        

        """

        _prefix = 'oc-map-acl'
        _revision = '2017-01-17'

        def __init__(self):
            super(AclMapping.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "acl-mapping"

            self.interface = YList(self)

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
                        super(AclMapping.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AclMapping.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            List of interfaces on which ACLs are set
            
            .. attribute:: id  <key>
            
            	Reference to the interface id list key
            	**type**\:  str
            
            .. attribute:: config
            
            	Configuration for ACL per\-interface data
            	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.Config>`
            
            .. attribute:: egress_acl_sets
            
            	Enclosing container the list of egress ACLs on the interface
            	**type**\:   :py:class:`EgressAclSets <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.EgressAclSets>`
            
            .. attribute:: ingress_acl_sets
            
            	Enclosing container the list of ingress ACLs on the interface
            	**type**\:   :py:class:`IngressAclSets <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.IngressAclSets>`
            
            .. attribute:: interface_ref
            
            	Reference to an interface or subinterface
            	**type**\:   :py:class:`InterfaceRef <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.InterfaceRef>`
            
            

            """

            _prefix = 'oc-map-acl'
            _revision = '2017-01-17'

            def __init__(self):
                super(AclMapping.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"

                self.id = YLeaf(YType.str, "id")

                self.config = AclMapping.Interfaces.Interface.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.egress_acl_sets = AclMapping.Interfaces.Interface.EgressAclSets()
                self.egress_acl_sets.parent = self
                self._children_name_map["egress_acl_sets"] = "egress-acl-sets"
                self._children_yang_names.add("egress-acl-sets")

                self.ingress_acl_sets = AclMapping.Interfaces.Interface.IngressAclSets()
                self.ingress_acl_sets.parent = self
                self._children_name_map["ingress_acl_sets"] = "ingress-acl-sets"
                self._children_yang_names.add("ingress-acl-sets")

                self.interface_ref = AclMapping.Interfaces.Interface.InterfaceRef()
                self.interface_ref.parent = self
                self._children_name_map["interface_ref"] = "interface-ref"
                self._children_yang_names.add("interface-ref")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(AclMapping.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(AclMapping.Interfaces.Interface, self).__setattr__(name, value)


            class Config(Entity):
                """
                Configuration for ACL per\-interface data
                
                .. attribute:: id
                
                	User\-defined identifier for the interface \-\- a common convention could be '<if name>.<subif index>'
                	**type**\:  str
                
                

                """

                _prefix = 'oc-map-acl'
                _revision = '2017-01-17'

                def __init__(self):
                    super(AclMapping.Interfaces.Interface.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "interface"

                    self.id = YLeaf(YType.str, "id")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(AclMapping.Interfaces.Interface.Config, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AclMapping.Interfaces.Interface.Config, self).__setattr__(name, value)

                def has_data(self):
                    return self.id.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.id.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "config" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "id"):
                        self.id = value
                        self.id.value_namespace = name_space
                        self.id.value_namespace_prefix = name_space_prefix


            class InterfaceRef(Entity):
                """
                Reference to an interface or subinterface
                
                .. attribute:: config
                
                	Configured reference to interface / subinterface
                	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.InterfaceRef.Config>`
                
                .. attribute:: state
                
                	Operational state for interface\-ref
                	**type**\:   :py:class:`State <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.InterfaceRef.State>`
                
                

                """

                _prefix = 'oc-map-acl'
                _revision = '2017-01-17'

                def __init__(self):
                    super(AclMapping.Interfaces.Interface.InterfaceRef, self).__init__()

                    self.yang_name = "interface-ref"
                    self.yang_parent_name = "interface"

                    self.config = AclMapping.Interfaces.Interface.InterfaceRef.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = AclMapping.Interfaces.Interface.InterfaceRef.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")


                class Config(Entity):
                    """
                    Configured reference to interface / subinterface
                    
                    .. attribute:: interface
                    
                    	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: subinterface
                    
                    	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                    
                    

                    """

                    _prefix = 'oc-map-acl'
                    _revision = '2017-01-17'

                    def __init__(self):
                        super(AclMapping.Interfaces.Interface.InterfaceRef.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "interface-ref"

                        self.interface = YLeaf(YType.str, "interface")

                        self.subinterface = YLeaf(YType.str, "subinterface")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface",
                                        "subinterface") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(AclMapping.Interfaces.Interface.InterfaceRef.Config, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AclMapping.Interfaces.Interface.InterfaceRef.Config, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.interface.is_set or
                            self.subinterface.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.subinterface.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "config" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.subinterface.is_set or self.subinterface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subinterface.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface" or name == "subinterface"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "subinterface"):
                            self.subinterface = value
                            self.subinterface.value_namespace = name_space
                            self.subinterface.value_namespace_prefix = name_space_prefix


                class State(Entity):
                    """
                    Operational state for interface\-ref
                    
                    .. attribute:: interface
                    
                    	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: subinterface
                    
                    	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                    
                    

                    """

                    _prefix = 'oc-map-acl'
                    _revision = '2017-01-17'

                    def __init__(self):
                        super(AclMapping.Interfaces.Interface.InterfaceRef.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "interface-ref"

                        self.interface = YLeaf(YType.str, "interface")

                        self.subinterface = YLeaf(YType.str, "subinterface")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface",
                                        "subinterface") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(AclMapping.Interfaces.Interface.InterfaceRef.State, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AclMapping.Interfaces.Interface.InterfaceRef.State, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.interface.is_set or
                            self.subinterface.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.subinterface.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "state" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.subinterface.is_set or self.subinterface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subinterface.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface" or name == "subinterface"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "subinterface"):
                            self.subinterface = value
                            self.subinterface.value_namespace = name_space
                            self.subinterface.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.config is not None and self.config.has_data()) or
                        (self.state is not None and self.state.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.config is not None and self.config.has_operation()) or
                        (self.state is not None and self.state.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface-ref" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "config"):
                        if (self.config is None):
                            self.config = AclMapping.Interfaces.Interface.InterfaceRef.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                        return self.config

                    if (child_yang_name == "state"):
                        if (self.state is None):
                            self.state = AclMapping.Interfaces.Interface.InterfaceRef.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                        return self.state

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "config" or name == "state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class IngressAclSets(Entity):
                """
                Enclosing container the list of ingress ACLs on the
                interface
                
                .. attribute:: ingress_acl_set
                
                	List of ingress ACLs on the interface
                	**type**\: list of    :py:class:`IngressAclSet <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet>`
                
                

                """

                _prefix = 'oc-map-acl'
                _revision = '2017-01-17'

                def __init__(self):
                    super(AclMapping.Interfaces.Interface.IngressAclSets, self).__init__()

                    self.yang_name = "ingress-acl-sets"
                    self.yang_parent_name = "interface"

                    self.ingress_acl_set = YList(self)

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
                                super(AclMapping.Interfaces.Interface.IngressAclSets, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AclMapping.Interfaces.Interface.IngressAclSets, self).__setattr__(name, value)


                class IngressAclSet(Entity):
                    """
                    List of ingress ACLs on the interface
                    
                    .. attribute:: set_name  <key>
                    
                    	Reference to set name list key
                    	**type**\:  str
                    
                    .. attribute:: acl_entries
                    
                    	Enclosing container for list of references to ACLs
                    	**type**\:   :py:class:`AclEntries <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries>`
                    
                    .. attribute:: config
                    
                    	Configuration data 
                    	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for interface ingress ACLs
                    	**type**\:   :py:class:`State <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.State>`
                    
                    

                    """

                    _prefix = 'oc-map-acl'
                    _revision = '2017-01-17'

                    def __init__(self):
                        super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet, self).__init__()

                        self.yang_name = "ingress-acl-set"
                        self.yang_parent_name = "ingress-acl-sets"

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.acl_entries = AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries()
                        self.acl_entries.parent = self
                        self._children_name_map["acl_entries"] = "acl-entries"
                        self._children_yang_names.add("acl-entries")

                        self.config = AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("set_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet, self).__setattr__(name, value)


                    class Config(Entity):
                        """
                        Configuration data 
                        
                        .. attribute:: set_name
                        
                        	Reference to the ACL set applied on ingress
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'oc-map-acl'
                        _revision = '2017-01-17'

                        def __init__(self):
                            super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "ingress-acl-set"

                            self.set_name = YLeaf(YType.str, "set-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("set_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.Config, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.Config, self).__setattr__(name, value)

                        def has_data(self):
                            return self.set_name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.set_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "config" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.set_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "set-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "set-name"):
                                self.set_name = value
                                self.set_name.value_namespace = name_space
                                self.set_name.value_namespace_prefix = name_space_prefix


                    class State(Entity):
                        """
                        Operational state data for interface ingress ACLs
                        
                        .. attribute:: set_name
                        
                        	Reference to the ACL set applied on ingress
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'oc-map-acl'
                        _revision = '2017-01-17'

                        def __init__(self):
                            super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "ingress-acl-set"

                            self.set_name = YLeaf(YType.str, "set-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("set_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.State, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.State, self).__setattr__(name, value)

                        def has_data(self):
                            return self.set_name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.set_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "state" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.set_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "set-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "set-name"):
                                self.set_name = value
                                self.set_name.value_namespace = name_space
                                self.set_name.value_namespace_prefix = name_space_prefix


                    class AclEntries(Entity):
                        """
                        Enclosing container for list of references to ACLs
                        
                        .. attribute:: acl_entry
                        
                        	List of ACL entries assigned to an interface
                        	**type**\: list of    :py:class:`AclEntry <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry>`
                        
                        

                        """

                        _prefix = 'oc-map-acl'
                        _revision = '2017-01-17'

                        def __init__(self):
                            super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries, self).__init__()

                            self.yang_name = "acl-entries"
                            self.yang_parent_name = "ingress-acl-set"

                            self.acl_entry = YList(self)

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
                                        super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries, self).__setattr__(name, value)


                        class AclEntry(Entity):
                            """
                            List of ACL entries assigned to an interface
                            
                            .. attribute:: sequence_id  <key>
                            
                            	Reference to per\-interface acl entry key
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'oc-map-acl'
                            _revision = '2017-01-17'

                            def __init__(self):
                                super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry, self).__init__()

                                self.yang_name = "acl-entry"
                                self.yang_parent_name = "acl-entries"

                                self.sequence_id = YLeaf(YType.str, "sequence-id")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("sequence_id") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry, self).__setattr__(name, value)

                            def has_data(self):
                                return self.sequence_id.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.sequence_id.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "acl-entry" + "[sequence-id='" + self.sequence_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.sequence_id.is_set or self.sequence_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sequence_id.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sequence-id"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "sequence-id"):
                                    self.sequence_id = value
                                    self.sequence_id.value_namespace = name_space
                                    self.sequence_id.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.acl_entry:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.acl_entry:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "acl-entries" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "acl-entry"):
                                for c in self.acl_entry:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.acl_entry.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "acl-entry"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.set_name.is_set or
                            (self.acl_entries is not None and self.acl_entries.has_data()) or
                            (self.config is not None and self.config.has_data()) or
                            (self.state is not None and self.state.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.set_name.yfilter != YFilter.not_set or
                            (self.acl_entries is not None and self.acl_entries.has_operation()) or
                            (self.config is not None and self.config.has_operation()) or
                            (self.state is not None and self.state.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ingress-acl-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.set_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "acl-entries"):
                            if (self.acl_entries is None):
                                self.acl_entries = AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries()
                                self.acl_entries.parent = self
                                self._children_name_map["acl_entries"] = "acl-entries"
                            return self.acl_entries

                        if (child_yang_name == "config"):
                            if (self.config is None):
                                self.config = AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                            return self.config

                        if (child_yang_name == "state"):
                            if (self.state is None):
                                self.state = AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                            return self.state

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "acl-entries" or name == "config" or name == "state" or name == "set-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "set-name"):
                            self.set_name = value
                            self.set_name.value_namespace = name_space
                            self.set_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ingress_acl_set:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ingress_acl_set:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ingress-acl-sets" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ingress-acl-set"):
                        for c in self.ingress_acl_set:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ingress_acl_set.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ingress-acl-set"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class EgressAclSets(Entity):
                """
                Enclosing container the list of egress ACLs on the
                interface
                
                .. attribute:: egress_acl_set
                
                	List of egress ACLs on the interface
                	**type**\: list of    :py:class:`EgressAclSet <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet>`
                
                

                """

                _prefix = 'oc-map-acl'
                _revision = '2017-01-17'

                def __init__(self):
                    super(AclMapping.Interfaces.Interface.EgressAclSets, self).__init__()

                    self.yang_name = "egress-acl-sets"
                    self.yang_parent_name = "interface"

                    self.egress_acl_set = YList(self)

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
                                super(AclMapping.Interfaces.Interface.EgressAclSets, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AclMapping.Interfaces.Interface.EgressAclSets, self).__setattr__(name, value)


                class EgressAclSet(Entity):
                    """
                    List of egress ACLs on the interface
                    
                    .. attribute:: set_name  <key>
                    
                    	Reference to set name list key
                    	**type**\:  str
                    
                    .. attribute:: acl_entries
                    
                    	Enclosing container for list of references to ACLs
                    	**type**\:   :py:class:`AclEntries <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries>`
                    
                    .. attribute:: config
                    
                    	Configuration data 
                    	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.Config>`
                    
                    

                    """

                    _prefix = 'oc-map-acl'
                    _revision = '2017-01-17'

                    def __init__(self):
                        super(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet, self).__init__()

                        self.yang_name = "egress-acl-set"
                        self.yang_parent_name = "egress-acl-sets"

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.acl_entries = AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries()
                        self.acl_entries.parent = self
                        self._children_name_map["acl_entries"] = "acl-entries"
                        self._children_yang_names.add("acl-entries")

                        self.config = AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("set_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet, self).__setattr__(name, value)


                    class Config(Entity):
                        """
                        Configuration data 
                        
                        .. attribute:: set_name
                        
                        	Reference to the ACL set applied on egress
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'oc-map-acl'
                        _revision = '2017-01-17'

                        def __init__(self):
                            super(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "egress-acl-set"

                            self.set_name = YLeaf(YType.str, "set-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("set_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.Config, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.Config, self).__setattr__(name, value)

                        def has_data(self):
                            return self.set_name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.set_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "config" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.set_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "set-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "set-name"):
                                self.set_name = value
                                self.set_name.value_namespace = name_space
                                self.set_name.value_namespace_prefix = name_space_prefix


                    class AclEntries(Entity):
                        """
                        Enclosing container for list of references to ACLs
                        
                        .. attribute:: acl_entry
                        
                        	List of ACL entries assigned to an interface
                        	**type**\: list of    :py:class:`AclEntry <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry>`
                        
                        

                        """

                        _prefix = 'oc-map-acl'
                        _revision = '2017-01-17'

                        def __init__(self):
                            super(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries, self).__init__()

                            self.yang_name = "acl-entries"
                            self.yang_parent_name = "egress-acl-set"

                            self.acl_entry = YList(self)

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
                                        super(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries, self).__setattr__(name, value)


                        class AclEntry(Entity):
                            """
                            List of ACL entries assigned to an interface
                            
                            .. attribute:: sequence_id  <key>
                            
                            	Reference to per\-interface acl entry key
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'oc-map-acl'
                            _revision = '2017-01-17'

                            def __init__(self):
                                super(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry, self).__init__()

                                self.yang_name = "acl-entry"
                                self.yang_parent_name = "acl-entries"

                                self.sequence_id = YLeaf(YType.str, "sequence-id")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("sequence_id") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry, self).__setattr__(name, value)

                            def has_data(self):
                                return self.sequence_id.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.sequence_id.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "acl-entry" + "[sequence-id='" + self.sequence_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.sequence_id.is_set or self.sequence_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sequence_id.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sequence-id"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "sequence-id"):
                                    self.sequence_id = value
                                    self.sequence_id.value_namespace = name_space
                                    self.sequence_id.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.acl_entry:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.acl_entry:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "acl-entries" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "acl-entry"):
                                for c in self.acl_entry:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.acl_entry.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "acl-entry"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.set_name.is_set or
                            (self.acl_entries is not None and self.acl_entries.has_data()) or
                            (self.config is not None and self.config.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.set_name.yfilter != YFilter.not_set or
                            (self.acl_entries is not None and self.acl_entries.has_operation()) or
                            (self.config is not None and self.config.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "egress-acl-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.set_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "acl-entries"):
                            if (self.acl_entries is None):
                                self.acl_entries = AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries()
                                self.acl_entries.parent = self
                                self._children_name_map["acl_entries"] = "acl-entries"
                            return self.acl_entries

                        if (child_yang_name == "config"):
                            if (self.config is None):
                                self.config = AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                            return self.config

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "acl-entries" or name == "config" or name == "set-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "set-name"):
                            self.set_name = value
                            self.set_name.value_namespace = name_space
                            self.set_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.egress_acl_set:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.egress_acl_set:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "egress-acl-sets" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "egress-acl-set"):
                        for c in self.egress_acl_set:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.egress_acl_set.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "egress-acl-set"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.id.is_set or
                    (self.config is not None and self.config.has_data()) or
                    (self.egress_acl_sets is not None and self.egress_acl_sets.has_data()) or
                    (self.ingress_acl_sets is not None and self.ingress_acl_sets.has_data()) or
                    (self.interface_ref is not None and self.interface_ref.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.id.yfilter != YFilter.not_set or
                    (self.config is not None and self.config.has_operation()) or
                    (self.egress_acl_sets is not None and self.egress_acl_sets.has_operation()) or
                    (self.ingress_acl_sets is not None and self.ingress_acl_sets.has_operation()) or
                    (self.interface_ref is not None and self.interface_ref.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + "[id='" + self.id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "oc-mapping-acl:acl-mapping/interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "config"):
                    if (self.config is None):
                        self.config = AclMapping.Interfaces.Interface.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                    return self.config

                if (child_yang_name == "egress-acl-sets"):
                    if (self.egress_acl_sets is None):
                        self.egress_acl_sets = AclMapping.Interfaces.Interface.EgressAclSets()
                        self.egress_acl_sets.parent = self
                        self._children_name_map["egress_acl_sets"] = "egress-acl-sets"
                    return self.egress_acl_sets

                if (child_yang_name == "ingress-acl-sets"):
                    if (self.ingress_acl_sets is None):
                        self.ingress_acl_sets = AclMapping.Interfaces.Interface.IngressAclSets()
                        self.ingress_acl_sets.parent = self
                        self._children_name_map["ingress_acl_sets"] = "ingress-acl-sets"
                    return self.ingress_acl_sets

                if (child_yang_name == "interface-ref"):
                    if (self.interface_ref is None):
                        self.interface_ref = AclMapping.Interfaces.Interface.InterfaceRef()
                        self.interface_ref.parent = self
                        self._children_name_map["interface_ref"] = "interface-ref"
                    return self.interface_ref

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "config" or name == "egress-acl-sets" or name == "ingress-acl-sets" or name == "interface-ref" or name == "id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "id"):
                    self.id = value
                    self.id.value_namespace = name_space
                    self.id.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.interface:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.interface:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "oc-mapping-acl:acl-mapping/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interface"):
                for c in self.interface:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = AclMapping.Interfaces.Interface()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.interface.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.acl_sets is not None and self.acl_sets.has_data()) or
            (self.interfaces is not None and self.interfaces.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.acl_sets is not None and self.acl_sets.has_operation()) or
            (self.interfaces is not None and self.interfaces.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "oc-mapping-acl:acl-mapping" + path_buffer

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

        if (child_yang_name == "acl-sets"):
            if (self.acl_sets is None):
                self.acl_sets = AclMapping.AclSets()
                self.acl_sets.parent = self
                self._children_name_map["acl_sets"] = "acl-sets"
            return self.acl_sets

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = AclMapping.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "acl-sets" or name == "interfaces"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = AclMapping()
        return self._top_entity

