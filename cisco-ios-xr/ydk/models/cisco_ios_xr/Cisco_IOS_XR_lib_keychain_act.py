""" Cisco_IOS_XR_lib_keychain_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

Copyright (c) 2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MasterKeyAdd(Entity):
    """
    To add a new master key
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_act.MasterKeyAdd.Input>`
    
    

    """

    _prefix = 'lib-keychain-act'
    _revision = '2017-04-17'

    def __init__(self):
        super(MasterKeyAdd, self).__init__()
        self._top_entity = None

        self.yang_name = "master-key-add"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-act"

        self.input = MasterKeyAdd.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: new_key
        
        	New master key to be added
        	**type**\:  str
        
        

        """

        _prefix = 'lib-keychain-act'
        _revision = '2017-04-17'

        def __init__(self):
            super(MasterKeyAdd.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "master-key-add"

            self.new_key = YLeaf(YType.str, "new-key")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("new_key") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MasterKeyAdd.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MasterKeyAdd.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.new_key.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.new_key.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-lib-keychain-act:master-key-add/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.new_key.is_set or self.new_key.yfilter != YFilter.not_set):
                leaf_name_data.append(self.new_key.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "new-key"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "new-key"):
                self.new_key = value
                self.new_key.value_namespace = name_space
                self.new_key.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-lib-keychain-act:master-key-add" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = MasterKeyAdd.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MasterKeyAdd()
        return self._top_entity

class MasterKeyDelete(Entity):
    """
    Remove Master key
    
    

    """

    _prefix = 'lib-keychain-act'
    _revision = '2017-04-17'

    def __init__(self):
        super(MasterKeyDelete, self).__init__()
        self._top_entity = None

        self.yang_name = "master-key-delete"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-lib-keychain-act:master-key-delete" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MasterKeyDelete()
        return self._top_entity

class MasterKeyUpdate(Entity):
    """
    To update master key
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_act.MasterKeyUpdate.Input>`
    
    

    """

    _prefix = 'lib-keychain-act'
    _revision = '2017-04-17'

    def __init__(self):
        super(MasterKeyUpdate, self).__init__()
        self._top_entity = None

        self.yang_name = "master-key-update"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-act"

        self.input = MasterKeyUpdate.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: new_key
        
        	New master key to be added 
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: old_key
        
        	key already added/key to be replaced
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'lib-keychain-act'
        _revision = '2017-04-17'

        def __init__(self):
            super(MasterKeyUpdate.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "master-key-update"

            self.new_key = YLeaf(YType.str, "new-key")

            self.old_key = YLeaf(YType.str, "old-key")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("new_key",
                            "old_key") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MasterKeyUpdate.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MasterKeyUpdate.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.new_key.is_set or
                self.old_key.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.new_key.yfilter != YFilter.not_set or
                self.old_key.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-lib-keychain-act:master-key-update/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.new_key.is_set or self.new_key.yfilter != YFilter.not_set):
                leaf_name_data.append(self.new_key.get_name_leafdata())
            if (self.old_key.is_set or self.old_key.yfilter != YFilter.not_set):
                leaf_name_data.append(self.old_key.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "new-key" or name == "old-key"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "new-key"):
                self.new_key = value
                self.new_key.value_namespace = name_space
                self.new_key.value_namespace_prefix = name_space_prefix
            if(value_path == "old-key"):
                self.old_key = value
                self.old_key.value_namespace = name_space
                self.old_key.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-lib-keychain-act:master-key-update" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = MasterKeyUpdate.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MasterKeyUpdate()
        return self._top_entity

