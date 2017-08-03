""" Cisco_IOS_XR_qos_ma_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR qos package configuration.

This module contains definitions
for the following management objects\:
  qos\: Global QOS configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-l2vpn\-cfg,
modules with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class QosFieldNotSupported(Enum):
    """
    QosFieldNotSupported

    Qos field not supported

    .. data:: not_supported = 0

    	Dummy data type leave unspecified

    """

    not_supported = Enum.YLeaf(0, "not-supported")


class QosPolicyAccount(Enum):
    """
    QosPolicyAccount

    Qos policy account

    .. data:: layer1 = 8

    	Turn on Layer 1 accounting

    .. data:: layer2 = 1

    	Turn on Layer 2 accounting

    .. data:: nolayer2 = 2

    	Turn on Layer 2 accounting

    .. data:: user_defined = 4

    	User defined accounting

    """

    layer1 = Enum.YLeaf(8, "layer1")

    layer2 = Enum.YLeaf(1, "layer2")

    nolayer2 = Enum.YLeaf(2, "nolayer2")

    user_defined = Enum.YLeaf(4, "user-defined")



class Qos(Entity):
    """
    Global QOS configuration.
    
    .. attribute:: fabric_service_policy
    
    	Name of the fabric service policy
    	**type**\:  str
    
    	**length:** 0..63
    
    

    """

    _prefix = 'qos-ma-cfg'
    _revision = '2016-12-23'

    def __init__(self):
        super(Qos, self).__init__()
        self._top_entity = None

        self.yang_name = "qos"
        self.yang_parent_name = "Cisco-IOS-XR-qos-ma-cfg"

        self.fabric_service_policy = YLeaf(YType.str, "fabric-service-policy")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("fabric_service_policy") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Qos, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Qos, self).__setattr__(name, value)

    def has_data(self):
        return self.fabric_service_policy.is_set

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.fabric_service_policy.yfilter != YFilter.not_set)

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-qos-ma-cfg:qos" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.fabric_service_policy.is_set or self.fabric_service_policy.yfilter != YFilter.not_set):
            leaf_name_data.append(self.fabric_service_policy.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "fabric-service-policy"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "fabric-service-policy"):
            self.fabric_service_policy = value
            self.fabric_service_policy.value_namespace = name_space
            self.fabric_service_policy.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Qos()
        return self._top_entity

