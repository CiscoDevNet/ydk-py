""" Cisco_IOS_XR_man_ems_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-ems package configuration.

This module contains definitions
for the following management objects\:
  grpc\: GRPC configruation

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Grpc(Entity):
    """
    GRPC configruation
    
    .. attribute:: address_family
    
    	Address family identifier type
    	**type**\:  str
    
    .. attribute:: enable
    
    	Enable GRPC
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: max_request_per_user
    
    	Maximum concurrent requests per user
    	**type**\:  int
    
    	**range:** 1..32
    
    .. attribute:: max_request_total
    
    	Maximum concurrent requests in total
    	**type**\:  int
    
    	**range:** 1..256
    
    .. attribute:: port
    
    	Server listening port
    	**type**\:  int
    
    	**range:** 10000..57999
    
    .. attribute:: service_layer
    
    	Service Layer
    	**type**\:   :py:class:`ServiceLayer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_cfg.Grpc.ServiceLayer>`
    
    .. attribute:: tls
    
    	Transport Layer Security (TLS)
    	**type**\:   :py:class:`Tls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_cfg.Grpc.Tls>`
    
    

    """

    _prefix = 'man-ems-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Grpc, self).__init__()
        self._top_entity = None

        self.yang_name = "grpc"
        self.yang_parent_name = "Cisco-IOS-XR-man-ems-cfg"

        self.address_family = YLeaf(YType.str, "address-family")

        self.enable = YLeaf(YType.empty, "enable")

        self.max_request_per_user = YLeaf(YType.uint32, "max-request-per-user")

        self.max_request_total = YLeaf(YType.uint32, "max-request-total")

        self.port = YLeaf(YType.uint32, "port")

        self.service_layer = Grpc.ServiceLayer()
        self.service_layer.parent = self
        self._children_name_map["service_layer"] = "service-layer"
        self._children_yang_names.add("service-layer")

        self.tls = Grpc.Tls()
        self.tls.parent = self
        self._children_name_map["tls"] = "tls"
        self._children_yang_names.add("tls")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("address_family",
                        "enable",
                        "max_request_per_user",
                        "max_request_total",
                        "port") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Grpc, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Grpc, self).__setattr__(name, value)


    class ServiceLayer(Entity):
        """
        Service Layer
        
        .. attribute:: enable
        
        	Enable ServiceLayer
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'man-ems-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Grpc.ServiceLayer, self).__init__()

            self.yang_name = "service-layer"
            self.yang_parent_name = "grpc"

            self.enable = YLeaf(YType.empty, "enable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("enable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Grpc.ServiceLayer, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Grpc.ServiceLayer, self).__setattr__(name, value)

        def has_data(self):
            return self.enable.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.enable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "service-layer" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-man-ems-cfg:grpc/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "enable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "enable"):
                self.enable = value
                self.enable.value_namespace = name_space
                self.enable.value_namespace_prefix = name_space_prefix


    class Tls(Entity):
        """
        Transport Layer Security (TLS)
        
        .. attribute:: enable
        
        	Enable TLS
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: trustpoint
        
        	Trustpoint Name
        	**type**\:  str
        
        

        """

        _prefix = 'man-ems-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Grpc.Tls, self).__init__()

            self.yang_name = "tls"
            self.yang_parent_name = "grpc"

            self.enable = YLeaf(YType.empty, "enable")

            self.trustpoint = YLeaf(YType.str, "trustpoint")

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
                            "trustpoint") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Grpc.Tls, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Grpc.Tls, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.enable.is_set or
                self.trustpoint.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.enable.yfilter != YFilter.not_set or
                self.trustpoint.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "tls" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-man-ems-cfg:grpc/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enable.get_name_leafdata())
            if (self.trustpoint.is_set or self.trustpoint.yfilter != YFilter.not_set):
                leaf_name_data.append(self.trustpoint.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "enable" or name == "trustpoint"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "enable"):
                self.enable = value
                self.enable.value_namespace = name_space
                self.enable.value_namespace_prefix = name_space_prefix
            if(value_path == "trustpoint"):
                self.trustpoint = value
                self.trustpoint.value_namespace = name_space
                self.trustpoint.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.address_family.is_set or
            self.enable.is_set or
            self.max_request_per_user.is_set or
            self.max_request_total.is_set or
            self.port.is_set or
            (self.service_layer is not None and self.service_layer.has_data()) or
            (self.tls is not None and self.tls.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.address_family.yfilter != YFilter.not_set or
            self.enable.yfilter != YFilter.not_set or
            self.max_request_per_user.yfilter != YFilter.not_set or
            self.max_request_total.yfilter != YFilter.not_set or
            self.port.yfilter != YFilter.not_set or
            (self.service_layer is not None and self.service_layer.has_operation()) or
            (self.tls is not None and self.tls.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-man-ems-cfg:grpc" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.address_family.is_set or self.address_family.yfilter != YFilter.not_set):
            leaf_name_data.append(self.address_family.get_name_leafdata())
        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable.get_name_leafdata())
        if (self.max_request_per_user.is_set or self.max_request_per_user.yfilter != YFilter.not_set):
            leaf_name_data.append(self.max_request_per_user.get_name_leafdata())
        if (self.max_request_total.is_set or self.max_request_total.yfilter != YFilter.not_set):
            leaf_name_data.append(self.max_request_total.get_name_leafdata())
        if (self.port.is_set or self.port.yfilter != YFilter.not_set):
            leaf_name_data.append(self.port.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "service-layer"):
            if (self.service_layer is None):
                self.service_layer = Grpc.ServiceLayer()
                self.service_layer.parent = self
                self._children_name_map["service_layer"] = "service-layer"
            return self.service_layer

        if (child_yang_name == "tls"):
            if (self.tls is None):
                self.tls = Grpc.Tls()
                self.tls.parent = self
                self._children_name_map["tls"] = "tls"
            return self.tls

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "service-layer" or name == "tls" or name == "address-family" or name == "enable" or name == "max-request-per-user" or name == "max-request-total" or name == "port"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "address-family"):
            self.address_family = value
            self.address_family.value_namespace = name_space
            self.address_family.value_namespace_prefix = name_space_prefix
        if(value_path == "enable"):
            self.enable = value
            self.enable.value_namespace = name_space
            self.enable.value_namespace_prefix = name_space_prefix
        if(value_path == "max-request-per-user"):
            self.max_request_per_user = value
            self.max_request_per_user.value_namespace = name_space
            self.max_request_per_user.value_namespace_prefix = name_space_prefix
        if(value_path == "max-request-total"):
            self.max_request_total = value
            self.max_request_total.value_namespace = name_space
            self.max_request_total.value_namespace_prefix = name_space_prefix
        if(value_path == "port"):
            self.port = value
            self.port.value_namespace = name_space
            self.port.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Grpc()
        return self._top_entity

