""" Cisco_IOS_XR_ipv6_io_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-io package configuration.

This module contains definitions
for the following management objects\:
  ipv6\-configuration\: IPv6 Configuration Data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ipv6Configuration(Entity):
    """
    IPv6 Configuration Data
    
    .. attribute:: ipv6_assembler
    
    	IPv6 fragmented packet assembler
    	**type**\:   :py:class:`Ipv6Assembler <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_cfg.Ipv6Configuration.Ipv6Assembler>`
    
    .. attribute:: ipv6_hop_limit
    
    	Configure IPv6 hop count limit
    	**type**\:  int
    
    	**range:** 1..255
    
    .. attribute:: ipv6_pmtu_enable
    
    	TRUE if enabled, FALSE if disabled
    	**type**\:  bool
    
    	**default value**\: false
    
    .. attribute:: ipv6_pmtu_time_out
    
    	Configure IPv6 Path MTU timeout value in minutes
    	**type**\:  int
    
    	**range:** 1..15
    
    	**units**\: minute
    
    .. attribute:: ipv6_source_route
    
    	TRUE if enabled, FALSE if disabled
    	**type**\:  bool
    
    	**default value**\: true
    
    .. attribute:: ipv6icmp
    
    	Configure IPv6 ICMP parameters
    	**type**\:   :py:class:`Ipv6Icmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_cfg.Ipv6Configuration.Ipv6Icmp>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'ipv6-io-cfg'
    _revision = '2016-05-10'

    def __init__(self):
        super(Ipv6Configuration, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6-configuration"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-io-cfg"

        self.ipv6_hop_limit = YLeaf(YType.uint32, "ipv6-hop-limit")

        self.ipv6_pmtu_enable = YLeaf(YType.boolean, "ipv6-pmtu-enable")

        self.ipv6_pmtu_time_out = YLeaf(YType.uint32, "ipv6-pmtu-time-out")

        self.ipv6_source_route = YLeaf(YType.boolean, "ipv6-source-route")

        self.ipv6_assembler = Ipv6Configuration.Ipv6Assembler()
        self.ipv6_assembler.parent = self
        self._children_name_map["ipv6_assembler"] = "ipv6-assembler"
        self._children_yang_names.add("ipv6-assembler")

        self.ipv6icmp = None
        self._children_name_map["ipv6icmp"] = "ipv6icmp"
        self._children_yang_names.add("ipv6icmp")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("ipv6_hop_limit",
                        "ipv6_pmtu_enable",
                        "ipv6_pmtu_time_out",
                        "ipv6_source_route") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Ipv6Configuration, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Ipv6Configuration, self).__setattr__(name, value)


    class Ipv6Assembler(Entity):
        """
        IPv6 fragmented packet assembler
        
        .. attribute:: max_packets
        
        	Maxinum packets allowed in assembly queues (in percent)
        	**type**\:  int
        
        	**range:** 1..50
        
        	**units**\: percentage
        
        .. attribute:: timeout
        
        	Number of seconds an assembly queue will hold before timeout
        	**type**\:  int
        
        	**range:** 1..120
        
        	**units**\: second
        
        

        """

        _prefix = 'ipv6-io-cfg'
        _revision = '2016-05-10'

        def __init__(self):
            super(Ipv6Configuration.Ipv6Assembler, self).__init__()

            self.yang_name = "ipv6-assembler"
            self.yang_parent_name = "ipv6-configuration"

            self.max_packets = YLeaf(YType.uint32, "max-packets")

            self.timeout = YLeaf(YType.uint32, "timeout")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("max_packets",
                            "timeout") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ipv6Configuration.Ipv6Assembler, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv6Configuration.Ipv6Assembler, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.max_packets.is_set or
                self.timeout.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.max_packets.yfilter != YFilter.not_set or
                self.timeout.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipv6-assembler" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv6-io-cfg:ipv6-configuration/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.max_packets.is_set or self.max_packets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_packets.get_name_leafdata())
            if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.timeout.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "max-packets" or name == "timeout"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "max-packets"):
                self.max_packets = value
                self.max_packets.value_namespace = name_space
                self.max_packets.value_namespace_prefix = name_space_prefix
            if(value_path == "timeout"):
                self.timeout = value
                self.timeout.value_namespace = name_space
                self.timeout.value_namespace_prefix = name_space_prefix


    class Ipv6Icmp(Entity):
        """
        Configure IPv6 ICMP parameters
        
        .. attribute:: bucket_size
        
        	Bucket size
        	**type**\:  int
        
        	**range:** 1..200
        
        	**default value**\: 10
        
        .. attribute:: error_interval
        
        	Interval between tokens in milliseconds
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**mandatory**\: True
        
        	**units**\: millisecond
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv6-io-cfg'
        _revision = '2016-05-10'

        def __init__(self):
            super(Ipv6Configuration.Ipv6Icmp, self).__init__()

            self.yang_name = "ipv6icmp"
            self.yang_parent_name = "ipv6-configuration"
            self.is_presence_container = True

            self.bucket_size = YLeaf(YType.uint32, "bucket-size")

            self.error_interval = YLeaf(YType.uint32, "error-interval")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("bucket_size",
                            "error_interval") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ipv6Configuration.Ipv6Icmp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv6Configuration.Ipv6Icmp, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.bucket_size.is_set or
                self.error_interval.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.bucket_size.yfilter != YFilter.not_set or
                self.error_interval.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipv6icmp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv6-io-cfg:ipv6-configuration/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.bucket_size.is_set or self.bucket_size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.bucket_size.get_name_leafdata())
            if (self.error_interval.is_set or self.error_interval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.error_interval.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bucket-size" or name == "error-interval"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "bucket-size"):
                self.bucket_size = value
                self.bucket_size.value_namespace = name_space
                self.bucket_size.value_namespace_prefix = name_space_prefix
            if(value_path == "error-interval"):
                self.error_interval = value
                self.error_interval.value_namespace = name_space
                self.error_interval.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.ipv6_hop_limit.is_set or
            self.ipv6_pmtu_enable.is_set or
            self.ipv6_pmtu_time_out.is_set or
            self.ipv6_source_route.is_set or
            (self.ipv6_assembler is not None and self.ipv6_assembler.has_data()) or
            (self.ipv6icmp is not None))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.ipv6_hop_limit.yfilter != YFilter.not_set or
            self.ipv6_pmtu_enable.yfilter != YFilter.not_set or
            self.ipv6_pmtu_time_out.yfilter != YFilter.not_set or
            self.ipv6_source_route.yfilter != YFilter.not_set or
            (self.ipv6_assembler is not None and self.ipv6_assembler.has_operation()) or
            (self.ipv6icmp is not None and self.ipv6icmp.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv6-io-cfg:ipv6-configuration" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.ipv6_hop_limit.is_set or self.ipv6_hop_limit.yfilter != YFilter.not_set):
            leaf_name_data.append(self.ipv6_hop_limit.get_name_leafdata())
        if (self.ipv6_pmtu_enable.is_set or self.ipv6_pmtu_enable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.ipv6_pmtu_enable.get_name_leafdata())
        if (self.ipv6_pmtu_time_out.is_set or self.ipv6_pmtu_time_out.yfilter != YFilter.not_set):
            leaf_name_data.append(self.ipv6_pmtu_time_out.get_name_leafdata())
        if (self.ipv6_source_route.is_set or self.ipv6_source_route.yfilter != YFilter.not_set):
            leaf_name_data.append(self.ipv6_source_route.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "ipv6-assembler"):
            if (self.ipv6_assembler is None):
                self.ipv6_assembler = Ipv6Configuration.Ipv6Assembler()
                self.ipv6_assembler.parent = self
                self._children_name_map["ipv6_assembler"] = "ipv6-assembler"
            return self.ipv6_assembler

        if (child_yang_name == "ipv6icmp"):
            if (self.ipv6icmp is None):
                self.ipv6icmp = Ipv6Configuration.Ipv6Icmp()
                self.ipv6icmp.parent = self
                self._children_name_map["ipv6icmp"] = "ipv6icmp"
            return self.ipv6icmp

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ipv6-assembler" or name == "ipv6icmp" or name == "ipv6-hop-limit" or name == "ipv6-pmtu-enable" or name == "ipv6-pmtu-time-out" or name == "ipv6-source-route"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "ipv6-hop-limit"):
            self.ipv6_hop_limit = value
            self.ipv6_hop_limit.value_namespace = name_space
            self.ipv6_hop_limit.value_namespace_prefix = name_space_prefix
        if(value_path == "ipv6-pmtu-enable"):
            self.ipv6_pmtu_enable = value
            self.ipv6_pmtu_enable.value_namespace = name_space
            self.ipv6_pmtu_enable.value_namespace_prefix = name_space_prefix
        if(value_path == "ipv6-pmtu-time-out"):
            self.ipv6_pmtu_time_out = value
            self.ipv6_pmtu_time_out.value_namespace = name_space
            self.ipv6_pmtu_time_out.value_namespace_prefix = name_space_prefix
        if(value_path == "ipv6-source-route"):
            self.ipv6_source_route = value
            self.ipv6_source_route.value_namespace = name_space
            self.ipv6_source_route.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Ipv6Configuration()
        return self._top_entity

