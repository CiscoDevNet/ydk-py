""" Cisco_IOS_XE_acl_oper 

This module contains a collection of YANG definitions
for ACL statistical data.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AccessLists(Entity):
    """
    This is top level container for Access Control Lists. It can have one
    or more Access Control List.
    
    .. attribute:: access_list
    
    	An access list (acl) is an ordered list of access list entries (ACE). Each access control entries has a list of match criteria, and a list of actions. Since there are several kinds of access control lists implemented with different attributes for each and different for each vendor, this model accommodates customizing access control lists for each kind and for each vendor
    	**type**\: list of    :py:class:`AccessList <ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper.AccessLists.AccessList>`
    
    

    """

    _prefix = 'acl-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(AccessLists, self).__init__()
        self._top_entity = None

        self.yang_name = "access-lists"
        self.yang_parent_name = "Cisco-IOS-XE-acl-oper"

        self.access_list = YList(self)

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
                    super(AccessLists, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(AccessLists, self).__setattr__(name, value)


    class AccessList(Entity):
        """
        An access list (acl) is an ordered list of
        access list entries (ACE). Each access control entries has a
        list of match criteria, and a list of actions.
        Since there are several kinds of access control lists
        implemented with different attributes for
        each and different for each vendor, this
        model accommodates customizing access control lists for
        each kind and for each vendor.
        
        .. attribute:: access_control_list_name  <key>
        
        	The name of access\-list. A device MAY restrict the length and value of this name, possibly space and special characters are not allowed
        	**type**\:  str
        
        .. attribute:: access_list_entries
        
        	access\-list\-entry(ACE) information
        	**type**\:   :py:class:`AccessListEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper.AccessLists.AccessList.AccessListEntries>`
        
        

        """

        _prefix = 'acl-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(AccessLists.AccessList, self).__init__()

            self.yang_name = "access-list"
            self.yang_parent_name = "access-lists"

            self.access_control_list_name = YLeaf(YType.str, "access-control-list-name")

            self.access_list_entries = AccessLists.AccessList.AccessListEntries()
            self.access_list_entries.parent = self
            self._children_name_map["access_list_entries"] = "access-list-entries"
            self._children_yang_names.add("access-list-entries")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("access_control_list_name") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(AccessLists.AccessList, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AccessLists.AccessList, self).__setattr__(name, value)


        class AccessListEntries(Entity):
            """
            access\-list\-entry(ACE) information
            
            .. attribute:: access_list_entry
            
            	A list of ACEs
            	**type**\: list of    :py:class:`AccessListEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper.AccessLists.AccessList.AccessListEntries.AccessListEntry>`
            
            

            """

            _prefix = 'acl-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(AccessLists.AccessList.AccessListEntries, self).__init__()

                self.yang_name = "access-list-entries"
                self.yang_parent_name = "access-list"

                self.access_list_entry = YList(self)

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
                            super(AccessLists.AccessList.AccessListEntries, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(AccessLists.AccessList.AccessListEntries, self).__setattr__(name, value)


            class AccessListEntry(Entity):
                """
                A list of ACEs
                
                .. attribute:: rule_name  <key>
                
                	Entry number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_list_entries_oper_data
                
                	Per access list entries operational data
                	**type**\:   :py:class:`AccessListEntriesOperData <ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper.AccessLists.AccessList.AccessListEntries.AccessListEntry.AccessListEntriesOperData>`
                
                

                """

                _prefix = 'acl-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(AccessLists.AccessList.AccessListEntries.AccessListEntry, self).__init__()

                    self.yang_name = "access-list-entry"
                    self.yang_parent_name = "access-list-entries"

                    self.rule_name = YLeaf(YType.uint32, "rule-name")

                    self.access_list_entries_oper_data = AccessLists.AccessList.AccessListEntries.AccessListEntry.AccessListEntriesOperData()
                    self.access_list_entries_oper_data.parent = self
                    self._children_name_map["access_list_entries_oper_data"] = "access-list-entries-oper-data"
                    self._children_yang_names.add("access-list-entries-oper-data")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("rule_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(AccessLists.AccessList.AccessListEntries.AccessListEntry, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AccessLists.AccessList.AccessListEntries.AccessListEntry, self).__setattr__(name, value)


                class AccessListEntriesOperData(Entity):
                    """
                    Per access list entries operational data
                    
                    .. attribute:: match_counter
                    
                    	Number of matches for an access list entry
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'acl-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(AccessLists.AccessList.AccessListEntries.AccessListEntry.AccessListEntriesOperData, self).__init__()

                        self.yang_name = "access-list-entries-oper-data"
                        self.yang_parent_name = "access-list-entry"

                        self.match_counter = YLeaf(YType.uint64, "match-counter")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("match_counter") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(AccessLists.AccessList.AccessListEntries.AccessListEntry.AccessListEntriesOperData, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AccessLists.AccessList.AccessListEntries.AccessListEntry.AccessListEntriesOperData, self).__setattr__(name, value)

                    def has_data(self):
                        return self.match_counter.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.match_counter.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "access-list-entries-oper-data" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.match_counter.is_set or self.match_counter.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.match_counter.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "match-counter"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "match-counter"):
                            self.match_counter = value
                            self.match_counter.value_namespace = name_space
                            self.match_counter.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.rule_name.is_set or
                        (self.access_list_entries_oper_data is not None and self.access_list_entries_oper_data.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.rule_name.yfilter != YFilter.not_set or
                        (self.access_list_entries_oper_data is not None and self.access_list_entries_oper_data.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "access-list-entry" + "[rule-name='" + self.rule_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.rule_name.is_set or self.rule_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rule_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "access-list-entries-oper-data"):
                        if (self.access_list_entries_oper_data is None):
                            self.access_list_entries_oper_data = AccessLists.AccessList.AccessListEntries.AccessListEntry.AccessListEntriesOperData()
                            self.access_list_entries_oper_data.parent = self
                            self._children_name_map["access_list_entries_oper_data"] = "access-list-entries-oper-data"
                        return self.access_list_entries_oper_data

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "access-list-entries-oper-data" or name == "rule-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "rule-name"):
                        self.rule_name = value
                        self.rule_name.value_namespace = name_space
                        self.rule_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.access_list_entry:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.access_list_entry:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "access-list-entries" + path_buffer

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

                if (child_yang_name == "access-list-entry"):
                    for c in self.access_list_entry:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = AccessLists.AccessList.AccessListEntries.AccessListEntry()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.access_list_entry.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "access-list-entry"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.access_control_list_name.is_set or
                (self.access_list_entries is not None and self.access_list_entries.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.access_control_list_name.yfilter != YFilter.not_set or
                (self.access_list_entries is not None and self.access_list_entries.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "access-list" + "[access-control-list-name='" + self.access_control_list_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-acl-oper:access-lists/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.access_control_list_name.is_set or self.access_control_list_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.access_control_list_name.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "access-list-entries"):
                if (self.access_list_entries is None):
                    self.access_list_entries = AccessLists.AccessList.AccessListEntries()
                    self.access_list_entries.parent = self
                    self._children_name_map["access_list_entries"] = "access-list-entries"
                return self.access_list_entries

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "access-list-entries" or name == "access-control-list-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "access-control-list-name"):
                self.access_control_list_name = value
                self.access_control_list_name.value_namespace = name_space
                self.access_control_list_name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.access_list:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.access_list:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-acl-oper:access-lists" + path_buffer

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

        if (child_yang_name == "access-list"):
            for c in self.access_list:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = AccessLists.AccessList()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.access_list.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "access-list"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = AccessLists()
        return self._top_entity

