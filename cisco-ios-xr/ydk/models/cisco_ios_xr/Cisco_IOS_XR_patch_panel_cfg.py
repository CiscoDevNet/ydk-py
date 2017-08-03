""" Cisco_IOS_XR_patch_panel_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR patch\-panel package configuration.

This module contains definitions
for the following management objects\:
  patch\-panel\: patch\-panel service submode

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class PatchPanel(Entity):
    """
    patch\-panel service submode
    
    .. attribute:: enable
    
    	Enable patch\-panel service
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    	**mandatory**\: True
    
    .. attribute:: ipv4
    
    	IP address for patch\-panel
    	**type**\:  str
    
    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
    
    .. attribute:: password
    
    	Password name to be used for Authentication with Patch\-Panel
    	**type**\:  str
    
    	**pattern:** (!.+)\|([^!].+)
    
    .. attribute:: user_name
    
    	User name to be used for Authentication with Patch\-Panel
    	**type**\:  str
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'patch-panel-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(PatchPanel, self).__init__()
        self._top_entity = None

        self.yang_name = "patch-panel"
        self.yang_parent_name = "Cisco-IOS-XR-patch-panel-cfg"
        self.is_presence_container = True

        self.enable = YLeaf(YType.empty, "enable")

        self.ipv4 = YLeaf(YType.str, "ipv4")

        self.password = YLeaf(YType.str, "password")

        self.user_name = YLeaf(YType.str, "user-name")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("enable",
                        "ipv4",
                        "password",
                        "user_name") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(PatchPanel, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(PatchPanel, self).__setattr__(name, value)

    def has_data(self):
        return (
            self.enable.is_set or
            self.ipv4.is_set or
            self.password.is_set or
            self.user_name.is_set)

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.enable.yfilter != YFilter.not_set or
            self.ipv4.yfilter != YFilter.not_set or
            self.password.yfilter != YFilter.not_set or
            self.user_name.yfilter != YFilter.not_set)

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-patch-panel-cfg:patch-panel" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable.get_name_leafdata())
        if (self.ipv4.is_set or self.ipv4.yfilter != YFilter.not_set):
            leaf_name_data.append(self.ipv4.get_name_leafdata())
        if (self.password.is_set or self.password.yfilter != YFilter.not_set):
            leaf_name_data.append(self.password.get_name_leafdata())
        if (self.user_name.is_set or self.user_name.yfilter != YFilter.not_set):
            leaf_name_data.append(self.user_name.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "enable" or name == "ipv4" or name == "password" or name == "user-name"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "enable"):
            self.enable = value
            self.enable.value_namespace = name_space
            self.enable.value_namespace_prefix = name_space_prefix
        if(value_path == "ipv4"):
            self.ipv4 = value
            self.ipv4.value_namespace = name_space
            self.ipv4.value_namespace_prefix = name_space_prefix
        if(value_path == "password"):
            self.password = value
            self.password.value_namespace = name_space
            self.password.value_namespace_prefix = name_space_prefix
        if(value_path == "user-name"):
            self.user_name = value
            self.user_name.value_namespace = name_space
            self.user_name.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = PatchPanel()
        return self._top_entity

