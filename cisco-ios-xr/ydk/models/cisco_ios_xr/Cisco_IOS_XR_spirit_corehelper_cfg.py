""" Cisco_IOS_XR_spirit_corehelper_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR spirit\-corehelper package configuration.

This module contains definitions
for the following management objects\:
  exception\: Core dump configuration commands

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Exception(Entity):
    """
    Core dump configuration commands
    
    .. attribute:: file
    
    	Container for the order of preference
    	**type**\:   :py:class:`File <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_corehelper_cfg.Exception.File>`
    
    

    """

    _prefix = 'spirit-corehelper-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Exception, self).__init__()
        self._top_entity = None

        self.yang_name = "exception"
        self.yang_parent_name = "Cisco-IOS-XR-spirit-corehelper-cfg"

        self.file = Exception.File()
        self.file.parent = self
        self._children_name_map["file"] = "file"
        self._children_yang_names.add("file")


    class File(Entity):
        """
        Container for the order of preference
        
        .. attribute:: choice1
        
        	Preference of the dump location
        	**type**\:  str
        
        .. attribute:: choice2
        
        	Preference of the dump location
        	**type**\:  str
        
        .. attribute:: choice3
        
        	Preference of the dump location
        	**type**\:  str
        
        

        """

        _prefix = 'spirit-corehelper-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Exception.File, self).__init__()

            self.yang_name = "file"
            self.yang_parent_name = "exception"

            self.choice1 = YLeaf(YType.str, "choice1")

            self.choice2 = YLeaf(YType.str, "choice2")

            self.choice3 = YLeaf(YType.str, "choice3")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("choice1",
                            "choice2",
                            "choice3") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Exception.File, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Exception.File, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.choice1.is_set or
                self.choice2.is_set or
                self.choice3.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.choice1.yfilter != YFilter.not_set or
                self.choice2.yfilter != YFilter.not_set or
                self.choice3.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "file" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-spirit-corehelper-cfg:exception/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.choice1.is_set or self.choice1.yfilter != YFilter.not_set):
                leaf_name_data.append(self.choice1.get_name_leafdata())
            if (self.choice2.is_set or self.choice2.yfilter != YFilter.not_set):
                leaf_name_data.append(self.choice2.get_name_leafdata())
            if (self.choice3.is_set or self.choice3.yfilter != YFilter.not_set):
                leaf_name_data.append(self.choice3.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "choice1" or name == "choice2" or name == "choice3"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "choice1"):
                self.choice1 = value
                self.choice1.value_namespace = name_space
                self.choice1.value_namespace_prefix = name_space_prefix
            if(value_path == "choice2"):
                self.choice2 = value
                self.choice2.value_namespace = name_space
                self.choice2.value_namespace_prefix = name_space_prefix
            if(value_path == "choice3"):
                self.choice3 = value
                self.choice3.value_namespace = name_space
                self.choice3.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.file is not None and self.file.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.file is not None and self.file.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-spirit-corehelper-cfg:exception" + path_buffer

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

        if (child_yang_name == "file"):
            if (self.file is None):
                self.file = Exception.File()
                self.file.parent = self
                self._children_name_map["file"] = "file"
            return self.file

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "file"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Exception()
        return self._top_entity

