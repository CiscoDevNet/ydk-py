""" Cisco_IOS_XR_ip_rib_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-rib package configuration.

This module contains definitions
for the following management objects\:
  rib\: RIB configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-infra\-rsi\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Rib(Entity):
    """
    RIB configuration.
    
    .. attribute:: af
    
    	RIB address family configuration
    	**type**\:   :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af>`
    
    .. attribute:: max_recursion_depth
    
    	Set maximum depth for route recursion check
    	**type**\:  int
    
    	**range:** 5..16
    
    

    """

    _prefix = 'ip-rib-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Rib, self).__init__()
        self._top_entity = None

        self.yang_name = "rib"
        self.yang_parent_name = "Cisco-IOS-XR-ip-rib-cfg"

        self.max_recursion_depth = YLeaf(YType.uint32, "max-recursion-depth")

        self.af = Rib.Af()
        self.af.parent = self
        self._children_name_map["af"] = "af"
        self._children_yang_names.add("af")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("max_recursion_depth") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Rib, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Rib, self).__setattr__(name, value)


    class Af(Entity):
        """
        RIB address family configuration
        
        .. attribute:: ipv4
        
        	IPv4 configuration
        	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af.Ipv4>`
        
        .. attribute:: ipv6
        
        	IPv6 configuration
        	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af.Ipv6>`
        
        

        """

        _prefix = 'ip-rib-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rib.Af, self).__init__()

            self.yang_name = "af"
            self.yang_parent_name = "rib"

            self.ipv4 = Rib.Af.Ipv4()
            self.ipv4.parent = self
            self._children_name_map["ipv4"] = "ipv4"
            self._children_yang_names.add("ipv4")

            self.ipv6 = Rib.Af.Ipv6()
            self.ipv6.parent = self
            self._children_name_map["ipv6"] = "ipv6"
            self._children_yang_names.add("ipv6")


        class Ipv4(Entity):
            """
            IPv4 configuration
            
            .. attribute:: next_hop_dampening_disable
            
            	Disable next\-hop dampening
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: redistribution_history
            
            	Redistribution history related configs
            	**type**\:   :py:class:`RedistributionHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af.Ipv4.RedistributionHistory>`
            
            

            """

            _prefix = 'ip-rib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rib.Af.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "af"

                self.next_hop_dampening_disable = YLeaf(YType.empty, "next-hop-dampening-disable")

                self.redistribution_history = Rib.Af.Ipv4.RedistributionHistory()
                self.redistribution_history.parent = self
                self._children_name_map["redistribution_history"] = "redistribution-history"
                self._children_yang_names.add("redistribution-history")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("next_hop_dampening_disable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rib.Af.Ipv4, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rib.Af.Ipv4, self).__setattr__(name, value)


            class RedistributionHistory(Entity):
                """
                Redistribution history related configs
                
                .. attribute:: bcdl_client
                
                	Maximum BCDL redistribution history size
                	**type**\:  int
                
                	**range:** 10..2000000
                
                .. attribute:: keep
                
                	Retain redistribution history after disconnect
                	**type**\:   :py:class:`Keep <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af.Ipv4.RedistributionHistory.Keep>`
                
                .. attribute:: protocol_client
                
                	Maximum protocol redistribution history size
                	**type**\:  int
                
                	**range:** 10..250000
                
                

                """

                _prefix = 'ip-rib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rib.Af.Ipv4.RedistributionHistory, self).__init__()

                    self.yang_name = "redistribution-history"
                    self.yang_parent_name = "ipv4"

                    self.bcdl_client = YLeaf(YType.uint32, "bcdl-client")

                    self.protocol_client = YLeaf(YType.uint32, "protocol-client")

                    self.keep = Rib.Af.Ipv4.RedistributionHistory.Keep()
                    self.keep.parent = self
                    self._children_name_map["keep"] = "keep"
                    self._children_yang_names.add("keep")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bcdl_client",
                                    "protocol_client") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rib.Af.Ipv4.RedistributionHistory, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rib.Af.Ipv4.RedistributionHistory, self).__setattr__(name, value)


                class Keep(Entity):
                    """
                    Retain redistribution history after disconnect.
                    
                    .. attribute:: bcdl
                    
                    	Enable retain BCDL history
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-rib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rib.Af.Ipv4.RedistributionHistory.Keep, self).__init__()

                        self.yang_name = "keep"
                        self.yang_parent_name = "redistribution-history"

                        self.bcdl = YLeaf(YType.empty, "bcdl")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("bcdl") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rib.Af.Ipv4.RedistributionHistory.Keep, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rib.Af.Ipv4.RedistributionHistory.Keep, self).__setattr__(name, value)

                    def has_data(self):
                        return self.bcdl.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.bcdl.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "keep" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-rib-cfg:rib/af/ipv4/redistribution-history/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.bcdl.is_set or self.bcdl.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bcdl.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bcdl"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "bcdl"):
                            self.bcdl = value
                            self.bcdl.value_namespace = name_space
                            self.bcdl.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.bcdl_client.is_set or
                        self.protocol_client.is_set or
                        (self.keep is not None and self.keep.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bcdl_client.yfilter != YFilter.not_set or
                        self.protocol_client.yfilter != YFilter.not_set or
                        (self.keep is not None and self.keep.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "redistribution-history" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rib-cfg:rib/af/ipv4/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bcdl_client.is_set or self.bcdl_client.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bcdl_client.get_name_leafdata())
                    if (self.protocol_client.is_set or self.protocol_client.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.protocol_client.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "keep"):
                        if (self.keep is None):
                            self.keep = Rib.Af.Ipv4.RedistributionHistory.Keep()
                            self.keep.parent = self
                            self._children_name_map["keep"] = "keep"
                        return self.keep

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "keep" or name == "bcdl-client" or name == "protocol-client"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bcdl-client"):
                        self.bcdl_client = value
                        self.bcdl_client.value_namespace = name_space
                        self.bcdl_client.value_namespace_prefix = name_space_prefix
                    if(value_path == "protocol-client"):
                        self.protocol_client = value
                        self.protocol_client.value_namespace = name_space
                        self.protocol_client.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.next_hop_dampening_disable.is_set or
                    (self.redistribution_history is not None and self.redistribution_history.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.next_hop_dampening_disable.yfilter != YFilter.not_set or
                    (self.redistribution_history is not None and self.redistribution_history.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv4" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rib-cfg:rib/af/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.next_hop_dampening_disable.is_set or self.next_hop_dampening_disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.next_hop_dampening_disable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "redistribution-history"):
                    if (self.redistribution_history is None):
                        self.redistribution_history = Rib.Af.Ipv4.RedistributionHistory()
                        self.redistribution_history.parent = self
                        self._children_name_map["redistribution_history"] = "redistribution-history"
                    return self.redistribution_history

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "redistribution-history" or name == "next-hop-dampening-disable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "next-hop-dampening-disable"):
                    self.next_hop_dampening_disable = value
                    self.next_hop_dampening_disable.value_namespace = name_space
                    self.next_hop_dampening_disable.value_namespace_prefix = name_space_prefix


        class Ipv6(Entity):
            """
            IPv6 configuration
            
            .. attribute:: next_hop_dampening_disable
            
            	Disable next\-hop dampening
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: redistribution_history
            
            	Redistribution history related configs
            	**type**\:   :py:class:`RedistributionHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af.Ipv6.RedistributionHistory>`
            
            

            """

            _prefix = 'ip-rib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rib.Af.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "af"

                self.next_hop_dampening_disable = YLeaf(YType.empty, "next-hop-dampening-disable")

                self.redistribution_history = Rib.Af.Ipv6.RedistributionHistory()
                self.redistribution_history.parent = self
                self._children_name_map["redistribution_history"] = "redistribution-history"
                self._children_yang_names.add("redistribution-history")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("next_hop_dampening_disable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rib.Af.Ipv6, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rib.Af.Ipv6, self).__setattr__(name, value)


            class RedistributionHistory(Entity):
                """
                Redistribution history related configs
                
                .. attribute:: bcdl_client
                
                	Maximum BCDL redistribution history size
                	**type**\:  int
                
                	**range:** 10..2000000
                
                .. attribute:: keep
                
                	Retain redistribution history after disconnect
                	**type**\:   :py:class:`Keep <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af.Ipv6.RedistributionHistory.Keep>`
                
                .. attribute:: protocol_client
                
                	Maximum protocol redistribution history size
                	**type**\:  int
                
                	**range:** 10..250000
                
                

                """

                _prefix = 'ip-rib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rib.Af.Ipv6.RedistributionHistory, self).__init__()

                    self.yang_name = "redistribution-history"
                    self.yang_parent_name = "ipv6"

                    self.bcdl_client = YLeaf(YType.uint32, "bcdl-client")

                    self.protocol_client = YLeaf(YType.uint32, "protocol-client")

                    self.keep = Rib.Af.Ipv6.RedistributionHistory.Keep()
                    self.keep.parent = self
                    self._children_name_map["keep"] = "keep"
                    self._children_yang_names.add("keep")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bcdl_client",
                                    "protocol_client") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rib.Af.Ipv6.RedistributionHistory, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rib.Af.Ipv6.RedistributionHistory, self).__setattr__(name, value)


                class Keep(Entity):
                    """
                    Retain redistribution history after disconnect.
                    
                    .. attribute:: bcdl
                    
                    	Enable retain BCDL history
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-rib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rib.Af.Ipv6.RedistributionHistory.Keep, self).__init__()

                        self.yang_name = "keep"
                        self.yang_parent_name = "redistribution-history"

                        self.bcdl = YLeaf(YType.empty, "bcdl")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("bcdl") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rib.Af.Ipv6.RedistributionHistory.Keep, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rib.Af.Ipv6.RedistributionHistory.Keep, self).__setattr__(name, value)

                    def has_data(self):
                        return self.bcdl.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.bcdl.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "keep" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-rib-cfg:rib/af/ipv6/redistribution-history/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.bcdl.is_set or self.bcdl.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bcdl.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bcdl"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "bcdl"):
                            self.bcdl = value
                            self.bcdl.value_namespace = name_space
                            self.bcdl.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.bcdl_client.is_set or
                        self.protocol_client.is_set or
                        (self.keep is not None and self.keep.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bcdl_client.yfilter != YFilter.not_set or
                        self.protocol_client.yfilter != YFilter.not_set or
                        (self.keep is not None and self.keep.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "redistribution-history" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rib-cfg:rib/af/ipv6/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bcdl_client.is_set or self.bcdl_client.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bcdl_client.get_name_leafdata())
                    if (self.protocol_client.is_set or self.protocol_client.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.protocol_client.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "keep"):
                        if (self.keep is None):
                            self.keep = Rib.Af.Ipv6.RedistributionHistory.Keep()
                            self.keep.parent = self
                            self._children_name_map["keep"] = "keep"
                        return self.keep

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "keep" or name == "bcdl-client" or name == "protocol-client"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bcdl-client"):
                        self.bcdl_client = value
                        self.bcdl_client.value_namespace = name_space
                        self.bcdl_client.value_namespace_prefix = name_space_prefix
                    if(value_path == "protocol-client"):
                        self.protocol_client = value
                        self.protocol_client.value_namespace = name_space
                        self.protocol_client.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.next_hop_dampening_disable.is_set or
                    (self.redistribution_history is not None and self.redistribution_history.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.next_hop_dampening_disable.yfilter != YFilter.not_set or
                    (self.redistribution_history is not None and self.redistribution_history.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv6" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rib-cfg:rib/af/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.next_hop_dampening_disable.is_set or self.next_hop_dampening_disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.next_hop_dampening_disable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "redistribution-history"):
                    if (self.redistribution_history is None):
                        self.redistribution_history = Rib.Af.Ipv6.RedistributionHistory()
                        self.redistribution_history.parent = self
                        self._children_name_map["redistribution_history"] = "redistribution-history"
                    return self.redistribution_history

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "redistribution-history" or name == "next-hop-dampening-disable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "next-hop-dampening-disable"):
                    self.next_hop_dampening_disable = value
                    self.next_hop_dampening_disable.value_namespace = name_space
                    self.next_hop_dampening_disable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                (self.ipv4 is not None and self.ipv4.has_data()) or
                (self.ipv6 is not None and self.ipv6.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.ipv4 is not None and self.ipv4.has_operation()) or
                (self.ipv6 is not None and self.ipv6.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "af" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-rib-cfg:rib/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipv4"):
                if (self.ipv4 is None):
                    self.ipv4 = Rib.Af.Ipv4()
                    self.ipv4.parent = self
                    self._children_name_map["ipv4"] = "ipv4"
                return self.ipv4

            if (child_yang_name == "ipv6"):
                if (self.ipv6 is None):
                    self.ipv6 = Rib.Af.Ipv6()
                    self.ipv6.parent = self
                    self._children_name_map["ipv6"] = "ipv6"
                return self.ipv6

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipv4" or name == "ipv6"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            self.max_recursion_depth.is_set or
            (self.af is not None and self.af.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.max_recursion_depth.yfilter != YFilter.not_set or
            (self.af is not None and self.af.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-rib-cfg:rib" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.max_recursion_depth.is_set or self.max_recursion_depth.yfilter != YFilter.not_set):
            leaf_name_data.append(self.max_recursion_depth.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "af"):
            if (self.af is None):
                self.af = Rib.Af()
                self.af.parent = self
                self._children_name_map["af"] = "af"
            return self.af

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "af" or name == "max-recursion-depth"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "max-recursion-depth"):
            self.max_recursion_depth = value
            self.max_recursion_depth.value_namespace = name_space
            self.max_recursion_depth.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Rib()
        return self._top_entity

