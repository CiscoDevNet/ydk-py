""" Cisco_IOS_XR_group_cfg 

This module contains IOS\-XR group YANG data 
for flexible cli groups 
    
Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Groups(Entity):
    """
    config groups
    
    .. attribute:: group
    
    	Group config definition
    	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_group_cfg.Groups.Group>`
    
    

    """

    _prefix = 'group-cfg'
    _revision = '2016-04-29'

    def __init__(self):
        super(Groups, self).__init__()
        self._top_entity = None

        self.yang_name = "groups"
        self.yang_parent_name = "Cisco-IOS-XR-group-cfg"

        self.group = YList(self)

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
                    super(Groups, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Groups, self).__setattr__(name, value)


    class Group(Entity):
        """
        Group config definition
        
        .. attribute:: group_name  <key>
        
        	Group name
        	**type**\:  str
        
        	**length:** 0..32
        
        

        """

        _prefix = 'group-cfg'
        _revision = '2016-04-29'

        def __init__(self):
            super(Groups.Group, self).__init__()

            self.yang_name = "group"
            self.yang_parent_name = "groups"

            self.group_name = YLeaf(YType.str, "group-name")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("group_name") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Groups.Group, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Groups.Group, self).__setattr__(name, value)

        def has_data(self):
            return self.group_name.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.group_name.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "group" + "[group-name='" + self.group_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-group-cfg:groups/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.group_name.is_set or self.group_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.group_name.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "group-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "group-name"):
                self.group_name = value
                self.group_name.value_namespace = name_space
                self.group_name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.group:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.group:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-group-cfg:groups" + path_buffer

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

        if (child_yang_name == "group"):
            for c in self.group:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = Groups.Group()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.group.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "group"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Groups()
        return self._top_entity

class ApplyGroups(Entity):
    """
    apply groups
    
    .. attribute:: apply_group
    
    	apply\-group name
    	**type**\:  str
    
    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
    
    

    """

    _prefix = 'group-cfg'
    _revision = '2016-04-29'

    def __init__(self):
        super(ApplyGroups, self).__init__()
        self._top_entity = None

        self.yang_name = "apply-groups"
        self.yang_parent_name = "Cisco-IOS-XR-group-cfg"

        self.apply_group = YLeaf(YType.str, "apply-group")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("apply_group") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(ApplyGroups, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(ApplyGroups, self).__setattr__(name, value)

    def has_data(self):
        return self.apply_group.is_set

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.apply_group.yfilter != YFilter.not_set)

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-group-cfg:apply-groups" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.apply_group.is_set or self.apply_group.yfilter != YFilter.not_set):
            leaf_name_data.append(self.apply_group.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "apply-group"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "apply-group"):
            self.apply_group = value
            self.apply_group.value_namespace = name_space
            self.apply_group.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = ApplyGroups()
        return self._top_entity

