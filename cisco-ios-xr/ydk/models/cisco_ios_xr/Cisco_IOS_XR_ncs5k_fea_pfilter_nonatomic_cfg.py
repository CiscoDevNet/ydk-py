""" Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs5k\-fea\-pfilter\-nonatomic package configuration.

This module contains definitions
for the following management objects\:
  hardware\: Hardware

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AtomicDisableDfltActn(Enum):
    """
    AtomicDisableDfltActn

    Atomic disable dflt actn

    .. data:: default_action_deny = 1

    	Drops traffic during modification

    .. data:: default_action_permit = 2

    	Forward traffic during modification

    """

    default_action_deny = Enum.YLeaf(1, "default-action-deny")

    default_action_permit = Enum.YLeaf(2, "default-action-permit")



class Hardware(Entity):
    """
    Hardware
    
    .. attribute:: access_list
    
    	Access\-list option
    	**type**\:   :py:class:`AccessList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg.Hardware.AccessList>`
    
    

    """

    _prefix = 'ncs5k-fea-pfilter-nonatomic-cfg'
    _revision = '2016-09-01'

    def __init__(self):
        super(Hardware, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware"
        self.yang_parent_name = "Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg"

        self.access_list = Hardware.AccessList()
        self.access_list.parent = self
        self._children_name_map["access_list"] = "access-list"
        self._children_yang_names.add("access-list")


    class AccessList(Entity):
        """
        Access\-list option
        
        .. attribute:: atomic_disable
        
        	Specify Option for Atomic disable
        	**type**\:   :py:class:`AtomicDisableDfltActn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg.AtomicDisableDfltActn>`
        
        

        """

        _prefix = 'ncs5k-fea-pfilter-nonatomic-cfg'
        _revision = '2016-09-01'

        def __init__(self):
            super(Hardware.AccessList, self).__init__()

            self.yang_name = "access-list"
            self.yang_parent_name = "hardware"

            self.atomic_disable = YLeaf(YType.enumeration, "atomic-disable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("atomic_disable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Hardware.AccessList, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Hardware.AccessList, self).__setattr__(name, value)

        def has_data(self):
            return self.atomic_disable.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.atomic_disable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "access-list" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg:hardware/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.atomic_disable.is_set or self.atomic_disable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.atomic_disable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "atomic-disable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "atomic-disable"):
                self.atomic_disable = value
                self.atomic_disable.value_namespace = name_space
                self.atomic_disable.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.access_list is not None and self.access_list.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.access_list is not None and self.access_list.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg:hardware" + path_buffer

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
            if (self.access_list is None):
                self.access_list = Hardware.AccessList()
                self.access_list.parent = self
                self._children_name_map["access_list"] = "access-list"
            return self.access_list

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "access-list"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Hardware()
        return self._top_entity

