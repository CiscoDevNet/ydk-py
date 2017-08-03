""" Cisco_IOS_XR_ip_tcp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-tcp package configuration.

This module contains definitions
for the following management objects\:
  ip\-tcp\: Global IP TCP configuration
  ip\: ip

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IpTcp(Entity):
    """
    Global IP TCP configuration
    
    .. attribute:: accept_rate
    
    	TCP connection accept rate
    	**type**\:  int
    
    	**range:** 1..1000
    
    	**default value**\: 500
    
    .. attribute:: directory
    
    	TCP directory details
    	**type**\:   :py:class:`Directory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.IpTcp.Directory>`
    
    	**presence node**\: True
    
    .. attribute:: maximum_segment_size
    
    	TCP initial maximum segment size
    	**type**\:  int
    
    	**range:** 68..10000
    
    .. attribute:: num_thread
    
    	TCP InQueue and OutQueue threads
    	**type**\:   :py:class:`NumThread <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.IpTcp.NumThread>`
    
    	**presence node**\: True
    
    .. attribute:: path_mtu_discovery
    
    	Aging time; 0 for infinite, and range be (10,30)
    	**type**\:  int
    
    	**range:** \-2147483648..2147483647
    
    	**units**\: minute
    
    	**default value**\: 10
    
    .. attribute:: receive_q
    
    	TCP receive Queue Size
    	**type**\:  int
    
    	**range:** 40..800
    
    .. attribute:: selective_ack
    
    	Enable TCP selective\-ACK
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: syn_wait_time
    
    	Time to wait on new TCP connections in seconds
    	**type**\:  int
    
    	**range:** 5..30
    
    	**units**\: second
    
    .. attribute:: throttle
    
    	Throttle TCP receive buffer (in percentage)
    	**type**\:   :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.IpTcp.Throttle>`
    
    	**presence node**\: True
    
    .. attribute:: timestamp
    
    	Enable TCP timestamp option
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: window_size
    
    	TCP receive window size (bytes)
    	**type**\:  int
    
    	**range:** 2048..65535
    
    	**units**\: byte
    
    

    """

    _prefix = 'ip-tcp-cfg'
    _revision = '2016-02-26'

    def __init__(self):
        super(IpTcp, self).__init__()
        self._top_entity = None

        self.yang_name = "ip-tcp"
        self.yang_parent_name = "Cisco-IOS-XR-ip-tcp-cfg"

        self.accept_rate = YLeaf(YType.uint32, "accept-rate")

        self.maximum_segment_size = YLeaf(YType.uint32, "maximum-segment-size")

        self.path_mtu_discovery = YLeaf(YType.int32, "path-mtu-discovery")

        self.receive_q = YLeaf(YType.uint32, "receive-q")

        self.selective_ack = YLeaf(YType.empty, "selective-ack")

        self.syn_wait_time = YLeaf(YType.uint32, "syn-wait-time")

        self.timestamp = YLeaf(YType.empty, "timestamp")

        self.window_size = YLeaf(YType.uint32, "window-size")

        self.directory = None
        self._children_name_map["directory"] = "directory"
        self._children_yang_names.add("directory")

        self.num_thread = None
        self._children_name_map["num_thread"] = "num-thread"
        self._children_yang_names.add("num-thread")

        self.throttle = None
        self._children_name_map["throttle"] = "throttle"
        self._children_yang_names.add("throttle")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("accept_rate",
                        "maximum_segment_size",
                        "path_mtu_discovery",
                        "receive_q",
                        "selective_ack",
                        "syn_wait_time",
                        "timestamp",
                        "window_size") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(IpTcp, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(IpTcp, self).__setattr__(name, value)


    class Directory(Entity):
        """
        TCP directory details
        
        .. attribute:: directoryname
        
        	Directory name 
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: max_debug_files
        
        	Set number of Debug files
        	**type**\:  int
        
        	**range:** 1..10000
        
        	**mandatory**\: True
        
        .. attribute:: max_file_size_files
        
        	Set size of debug files in bytes
        	**type**\:  int
        
        	**range:** 1024..4294967295
        
        	**mandatory**\: True
        
        	**units**\: byte
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-tcp-cfg'
        _revision = '2016-02-26'

        def __init__(self):
            super(IpTcp.Directory, self).__init__()

            self.yang_name = "directory"
            self.yang_parent_name = "ip-tcp"
            self.is_presence_container = True

            self.directoryname = YLeaf(YType.str, "directoryname")

            self.max_debug_files = YLeaf(YType.uint32, "max-debug-files")

            self.max_file_size_files = YLeaf(YType.uint32, "max-file-size-files")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("directoryname",
                            "max_debug_files",
                            "max_file_size_files") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IpTcp.Directory, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpTcp.Directory, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.directoryname.is_set or
                self.max_debug_files.is_set or
                self.max_file_size_files.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.directoryname.yfilter != YFilter.not_set or
                self.max_debug_files.yfilter != YFilter.not_set or
                self.max_file_size_files.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "directory" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip-tcp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.directoryname.is_set or self.directoryname.yfilter != YFilter.not_set):
                leaf_name_data.append(self.directoryname.get_name_leafdata())
            if (self.max_debug_files.is_set or self.max_debug_files.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_debug_files.get_name_leafdata())
            if (self.max_file_size_files.is_set or self.max_file_size_files.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_file_size_files.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "directoryname" or name == "max-debug-files" or name == "max-file-size-files"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "directoryname"):
                self.directoryname = value
                self.directoryname.value_namespace = name_space
                self.directoryname.value_namespace_prefix = name_space_prefix
            if(value_path == "max-debug-files"):
                self.max_debug_files = value
                self.max_debug_files.value_namespace = name_space
                self.max_debug_files.value_namespace_prefix = name_space_prefix
            if(value_path == "max-file-size-files"):
                self.max_file_size_files = value
                self.max_file_size_files.value_namespace = name_space
                self.max_file_size_files.value_namespace_prefix = name_space_prefix


    class Throttle(Entity):
        """
        Throttle TCP receive buffer (in percentage)
        
        .. attribute:: tcpmaxthrottle
        
        	Max throttle
        	**type**\:  int
        
        	**range:** 0..100
        
        	**mandatory**\: True
        
        .. attribute:: tcpmin_throttle
        
        	Min throttle
        	**type**\:  int
        
        	**range:** 0..100
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-tcp-cfg'
        _revision = '2016-02-26'

        def __init__(self):
            super(IpTcp.Throttle, self).__init__()

            self.yang_name = "throttle"
            self.yang_parent_name = "ip-tcp"
            self.is_presence_container = True

            self.tcpmaxthrottle = YLeaf(YType.uint32, "tcpmaxthrottle")

            self.tcpmin_throttle = YLeaf(YType.uint32, "tcpmin-throttle")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("tcpmaxthrottle",
                            "tcpmin_throttle") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IpTcp.Throttle, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpTcp.Throttle, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.tcpmaxthrottle.is_set or
                self.tcpmin_throttle.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.tcpmaxthrottle.yfilter != YFilter.not_set or
                self.tcpmin_throttle.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "throttle" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip-tcp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.tcpmaxthrottle.is_set or self.tcpmaxthrottle.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcpmaxthrottle.get_name_leafdata())
            if (self.tcpmin_throttle.is_set or self.tcpmin_throttle.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcpmin_throttle.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "tcpmaxthrottle" or name == "tcpmin-throttle"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "tcpmaxthrottle"):
                self.tcpmaxthrottle = value
                self.tcpmaxthrottle.value_namespace = name_space
                self.tcpmaxthrottle.value_namespace_prefix = name_space_prefix
            if(value_path == "tcpmin-throttle"):
                self.tcpmin_throttle = value
                self.tcpmin_throttle.value_namespace = name_space
                self.tcpmin_throttle.value_namespace_prefix = name_space_prefix


    class NumThread(Entity):
        """
        TCP InQueue and OutQueue threads
        
        .. attribute:: tcp_in_q_threads
        
        	InQ Threads
        	**type**\:  int
        
        	**range:** 1..16
        
        	**mandatory**\: True
        
        .. attribute:: tcp_out_q_threads
        
        	OutQ Threads
        	**type**\:  int
        
        	**range:** 1..16
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-tcp-cfg'
        _revision = '2016-02-26'

        def __init__(self):
            super(IpTcp.NumThread, self).__init__()

            self.yang_name = "num-thread"
            self.yang_parent_name = "ip-tcp"
            self.is_presence_container = True

            self.tcp_in_q_threads = YLeaf(YType.uint32, "tcp-in-q-threads")

            self.tcp_out_q_threads = YLeaf(YType.uint32, "tcp-out-q-threads")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("tcp_in_q_threads",
                            "tcp_out_q_threads") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IpTcp.NumThread, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpTcp.NumThread, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.tcp_in_q_threads.is_set or
                self.tcp_out_q_threads.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.tcp_in_q_threads.yfilter != YFilter.not_set or
                self.tcp_out_q_threads.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "num-thread" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip-tcp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.tcp_in_q_threads.is_set or self.tcp_in_q_threads.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcp_in_q_threads.get_name_leafdata())
            if (self.tcp_out_q_threads.is_set or self.tcp_out_q_threads.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcp_out_q_threads.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "tcp-in-q-threads" or name == "tcp-out-q-threads"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "tcp-in-q-threads"):
                self.tcp_in_q_threads = value
                self.tcp_in_q_threads.value_namespace = name_space
                self.tcp_in_q_threads.value_namespace_prefix = name_space_prefix
            if(value_path == "tcp-out-q-threads"):
                self.tcp_out_q_threads = value
                self.tcp_out_q_threads.value_namespace = name_space
                self.tcp_out_q_threads.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.accept_rate.is_set or
            self.maximum_segment_size.is_set or
            self.path_mtu_discovery.is_set or
            self.receive_q.is_set or
            self.selective_ack.is_set or
            self.syn_wait_time.is_set or
            self.timestamp.is_set or
            self.window_size.is_set or
            (self.directory is not None) or
            (self.num_thread is not None) or
            (self.throttle is not None))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.accept_rate.yfilter != YFilter.not_set or
            self.maximum_segment_size.yfilter != YFilter.not_set or
            self.path_mtu_discovery.yfilter != YFilter.not_set or
            self.receive_q.yfilter != YFilter.not_set or
            self.selective_ack.yfilter != YFilter.not_set or
            self.syn_wait_time.yfilter != YFilter.not_set or
            self.timestamp.yfilter != YFilter.not_set or
            self.window_size.yfilter != YFilter.not_set or
            (self.directory is not None and self.directory.has_operation()) or
            (self.num_thread is not None and self.num_thread.has_operation()) or
            (self.throttle is not None and self.throttle.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip-tcp" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.accept_rate.is_set or self.accept_rate.yfilter != YFilter.not_set):
            leaf_name_data.append(self.accept_rate.get_name_leafdata())
        if (self.maximum_segment_size.is_set or self.maximum_segment_size.yfilter != YFilter.not_set):
            leaf_name_data.append(self.maximum_segment_size.get_name_leafdata())
        if (self.path_mtu_discovery.is_set or self.path_mtu_discovery.yfilter != YFilter.not_set):
            leaf_name_data.append(self.path_mtu_discovery.get_name_leafdata())
        if (self.receive_q.is_set or self.receive_q.yfilter != YFilter.not_set):
            leaf_name_data.append(self.receive_q.get_name_leafdata())
        if (self.selective_ack.is_set or self.selective_ack.yfilter != YFilter.not_set):
            leaf_name_data.append(self.selective_ack.get_name_leafdata())
        if (self.syn_wait_time.is_set or self.syn_wait_time.yfilter != YFilter.not_set):
            leaf_name_data.append(self.syn_wait_time.get_name_leafdata())
        if (self.timestamp.is_set or self.timestamp.yfilter != YFilter.not_set):
            leaf_name_data.append(self.timestamp.get_name_leafdata())
        if (self.window_size.is_set or self.window_size.yfilter != YFilter.not_set):
            leaf_name_data.append(self.window_size.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "directory"):
            if (self.directory is None):
                self.directory = IpTcp.Directory()
                self.directory.parent = self
                self._children_name_map["directory"] = "directory"
            return self.directory

        if (child_yang_name == "num-thread"):
            if (self.num_thread is None):
                self.num_thread = IpTcp.NumThread()
                self.num_thread.parent = self
                self._children_name_map["num_thread"] = "num-thread"
            return self.num_thread

        if (child_yang_name == "throttle"):
            if (self.throttle is None):
                self.throttle = IpTcp.Throttle()
                self.throttle.parent = self
                self._children_name_map["throttle"] = "throttle"
            return self.throttle

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "directory" or name == "num-thread" or name == "throttle" or name == "accept-rate" or name == "maximum-segment-size" or name == "path-mtu-discovery" or name == "receive-q" or name == "selective-ack" or name == "syn-wait-time" or name == "timestamp" or name == "window-size"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "accept-rate"):
            self.accept_rate = value
            self.accept_rate.value_namespace = name_space
            self.accept_rate.value_namespace_prefix = name_space_prefix
        if(value_path == "maximum-segment-size"):
            self.maximum_segment_size = value
            self.maximum_segment_size.value_namespace = name_space
            self.maximum_segment_size.value_namespace_prefix = name_space_prefix
        if(value_path == "path-mtu-discovery"):
            self.path_mtu_discovery = value
            self.path_mtu_discovery.value_namespace = name_space
            self.path_mtu_discovery.value_namespace_prefix = name_space_prefix
        if(value_path == "receive-q"):
            self.receive_q = value
            self.receive_q.value_namespace = name_space
            self.receive_q.value_namespace_prefix = name_space_prefix
        if(value_path == "selective-ack"):
            self.selective_ack = value
            self.selective_ack.value_namespace = name_space
            self.selective_ack.value_namespace_prefix = name_space_prefix
        if(value_path == "syn-wait-time"):
            self.syn_wait_time = value
            self.syn_wait_time.value_namespace = name_space
            self.syn_wait_time.value_namespace_prefix = name_space_prefix
        if(value_path == "timestamp"):
            self.timestamp = value
            self.timestamp.value_namespace = name_space
            self.timestamp.value_namespace_prefix = name_space_prefix
        if(value_path == "window-size"):
            self.window_size = value
            self.window_size.value_namespace = name_space
            self.window_size.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = IpTcp()
        return self._top_entity

class Ip(Entity):
    """
    ip
    
    .. attribute:: cinetd
    
    	Cinetd configuration data
    	**type**\:   :py:class:`Cinetd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd>`
    
    .. attribute:: forward_protocol
    
    	Controls forwarding of physical and directed IP broadcasts
    	**type**\:   :py:class:`ForwardProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.ForwardProtocol>`
    
    

    """

    _prefix = 'ip-tcp-cfg'
    _revision = '2016-02-26'

    def __init__(self):
        super(Ip, self).__init__()
        self._top_entity = None

        self.yang_name = "ip"
        self.yang_parent_name = "Cisco-IOS-XR-ip-tcp-cfg"

        self.cinetd = Ip.Cinetd()
        self.cinetd.parent = self
        self._children_name_map["cinetd"] = "cinetd"
        self._children_yang_names.add("cinetd")

        self.forward_protocol = Ip.ForwardProtocol()
        self.forward_protocol.parent = self
        self._children_name_map["forward_protocol"] = "forward-protocol"
        self._children_yang_names.add("forward-protocol")


    class Cinetd(Entity):
        """
        Cinetd configuration data
        
        .. attribute:: services
        
        	Describing services of cinetd
        	**type**\:   :py:class:`Services <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services>`
        
        

        """

        _prefix = 'ip-tcp-cfg'
        _revision = '2016-02-26'

        def __init__(self):
            super(Ip.Cinetd, self).__init__()

            self.yang_name = "cinetd"
            self.yang_parent_name = "ip"

            self.services = Ip.Cinetd.Services()
            self.services.parent = self
            self._children_name_map["services"] = "services"
            self._children_yang_names.add("services")


        class Services(Entity):
            """
            Describing services of cinetd
            
            .. attribute:: ipv4
            
            	IPV4 related services
            	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv4>`
            
            .. attribute:: ipv6
            
            	IPV6 related services
            	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv6>`
            
            .. attribute:: vrfs
            
            	VRF table
            	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs>`
            
            

            """

            _prefix = 'ip-tcp-cfg'
            _revision = '2016-02-26'

            def __init__(self):
                super(Ip.Cinetd.Services, self).__init__()

                self.yang_name = "services"
                self.yang_parent_name = "cinetd"

                self.ipv4 = Ip.Cinetd.Services.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
                self._children_yang_names.add("ipv4")

                self.ipv6 = Ip.Cinetd.Services.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
                self._children_yang_names.add("ipv6")

                self.vrfs = Ip.Cinetd.Services.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
                self._children_yang_names.add("vrfs")


            class Ipv4(Entity):
                """
                IPV4 related services
                
                .. attribute:: small_servers
                
                	Describing IPV4 and IPV6 small servers
                	**type**\:   :py:class:`SmallServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv4.SmallServers>`
                
                

                """

                _prefix = 'ip-tcp-cfg'
                _revision = '2016-02-26'

                def __init__(self):
                    super(Ip.Cinetd.Services.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "services"

                    self.small_servers = Ip.Cinetd.Services.Ipv4.SmallServers()
                    self.small_servers.parent = self
                    self._children_name_map["small_servers"] = "small-servers"
                    self._children_yang_names.add("small-servers")


                class SmallServers(Entity):
                    """
                    Describing IPV4 and IPV6 small servers
                    
                    .. attribute:: tcp_small_servers
                    
                    	Describing TCP related IPV4 and IPV6 small servers
                    	**type**\:   :py:class:`TcpSmallServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: udp_small_servers
                    
                    	UDP small servers configuration
                    	**type**\:   :py:class:`UdpSmallServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'ip-tcp-cfg'
                    _revision = '2016-02-26'

                    def __init__(self):
                        super(Ip.Cinetd.Services.Ipv4.SmallServers, self).__init__()

                        self.yang_name = "small-servers"
                        self.yang_parent_name = "ipv4"

                        self.tcp_small_servers = None
                        self._children_name_map["tcp_small_servers"] = "tcp-small-servers"
                        self._children_yang_names.add("tcp-small-servers")

                        self.udp_small_servers = None
                        self._children_name_map["udp_small_servers"] = "udp-small-servers"
                        self._children_yang_names.add("udp-small-servers")


                    class TcpSmallServers(Entity):
                        """
                        Describing TCP related IPV4 and IPV6 small
                        servers
                        
                        .. attribute:: access_control_list_name
                        
                        	Access list
                        	**type**\:  str
                        
                        .. attribute:: small_server
                        
                        	Set number of allowable TCP small servers, specify 0 for no\-limit
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ip-tcp-cfg'
                        _revision = '2016-02-26'

                        def __init__(self):
                            super(Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers, self).__init__()

                            self.yang_name = "tcp-small-servers"
                            self.yang_parent_name = "small-servers"
                            self.is_presence_container = True

                            self.access_control_list_name = YLeaf(YType.str, "access-control-list-name")

                            self.small_server = YLeaf(YType.int32, "small-server")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("access_control_list_name",
                                            "small_server") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.access_control_list_name.is_set or
                                self.small_server.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.access_control_list_name.yfilter != YFilter.not_set or
                                self.small_server.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "tcp-small-servers" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/ipv4/small-servers/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.access_control_list_name.is_set or self.access_control_list_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.access_control_list_name.get_name_leafdata())
                            if (self.small_server.is_set or self.small_server.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.small_server.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "access-control-list-name" or name == "small-server"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "access-control-list-name"):
                                self.access_control_list_name = value
                                self.access_control_list_name.value_namespace = name_space
                                self.access_control_list_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "small-server"):
                                self.small_server = value
                                self.small_server.value_namespace = name_space
                                self.small_server.value_namespace_prefix = name_space_prefix


                    class UdpSmallServers(Entity):
                        """
                        UDP small servers configuration
                        
                        .. attribute:: access_control_list_name
                        
                        	Specify the access list
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: small_server
                        
                        	Set number of allowable small servers, specify 0 for no\-limit
                        	**type**\:  int
                        
                        	**range:** 0..2147483647
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ip-udp-cfg'
                        _revision = '2016-02-26'

                        def __init__(self):
                            super(Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers, self).__init__()

                            self.yang_name = "udp-small-servers"
                            self.yang_parent_name = "small-servers"
                            self.is_presence_container = True

                            self.access_control_list_name = YLeaf(YType.str, "access-control-list-name")

                            self.small_server = YLeaf(YType.uint32, "small-server")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("access_control_list_name",
                                            "small_server") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.access_control_list_name.is_set or
                                self.small_server.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.access_control_list_name.yfilter != YFilter.not_set or
                                self.small_server.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "Cisco-IOS-XR-ip-udp-cfg:udp-small-servers" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/ipv4/small-servers/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.access_control_list_name.is_set or self.access_control_list_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.access_control_list_name.get_name_leafdata())
                            if (self.small_server.is_set or self.small_server.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.small_server.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "access-control-list-name" or name == "small-server"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "access-control-list-name"):
                                self.access_control_list_name = value
                                self.access_control_list_name.value_namespace = name_space
                                self.access_control_list_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "small-server"):
                                self.small_server = value
                                self.small_server.value_namespace = name_space
                                self.small_server.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.tcp_small_servers is not None) or
                            (self.udp_small_servers is not None))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.tcp_small_servers is not None and self.tcp_small_servers.has_operation()) or
                            (self.udp_small_servers is not None and self.udp_small_servers.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "small-servers" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/ipv4/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "tcp-small-servers"):
                            if (self.tcp_small_servers is None):
                                self.tcp_small_servers = Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers()
                                self.tcp_small_servers.parent = self
                                self._children_name_map["tcp_small_servers"] = "tcp-small-servers"
                            return self.tcp_small_servers

                        if (child_yang_name == "udp-small-servers"):
                            if (self.udp_small_servers is None):
                                self.udp_small_servers = Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers()
                                self.udp_small_servers.parent = self
                                self._children_name_map["udp_small_servers"] = "udp-small-servers"
                            return self.udp_small_servers

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "tcp-small-servers" or name == "udp-small-servers"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.small_servers is not None and self.small_servers.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.small_servers is not None and self.small_servers.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv4" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "small-servers"):
                        if (self.small_servers is None):
                            self.small_servers = Ip.Cinetd.Services.Ipv4.SmallServers()
                            self.small_servers.parent = self
                            self._children_name_map["small_servers"] = "small-servers"
                        return self.small_servers

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "small-servers"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Vrfs(Entity):
                """
                VRF table
                
                .. attribute:: vrf
                
                	VRF specific data
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf>`
                
                

                """

                _prefix = 'ip-tcp-cfg'
                _revision = '2016-02-26'

                def __init__(self):
                    super(Ip.Cinetd.Services.Vrfs, self).__init__()

                    self.yang_name = "vrfs"
                    self.yang_parent_name = "services"

                    self.vrf = YList(self)

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
                                super(Ip.Cinetd.Services.Vrfs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ip.Cinetd.Services.Vrfs, self).__setattr__(name, value)


                class Vrf(Entity):
                    """
                    VRF specific data
                    
                    .. attribute:: vrf_name  <key>
                    
                    	Name of the VRF instance
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: ipv4
                    
                    	IPV4 related services
                    	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv4>`
                    
                    .. attribute:: ipv6
                    
                    	IPV6 related services
                    	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv6>`
                    
                    

                    """

                    _prefix = 'ip-tcp-cfg'
                    _revision = '2016-02-26'

                    def __init__(self):
                        super(Ip.Cinetd.Services.Vrfs.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "vrfs"

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.ipv4 = Ip.Cinetd.Services.Vrfs.Vrf.Ipv4()
                        self.ipv4.parent = self
                        self._children_name_map["ipv4"] = "ipv4"
                        self._children_yang_names.add("ipv4")

                        self.ipv6 = Ip.Cinetd.Services.Vrfs.Vrf.Ipv6()
                        self.ipv6.parent = self
                        self._children_name_map["ipv6"] = "ipv6"
                        self._children_yang_names.add("ipv6")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("vrf_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ip.Cinetd.Services.Vrfs.Vrf, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ip.Cinetd.Services.Vrfs.Vrf, self).__setattr__(name, value)


                    class Ipv6(Entity):
                        """
                        IPV6 related services
                        
                        .. attribute:: telnet
                        
                        	TELNET server configuration commands
                        	**type**\:   :py:class:`Telnet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet>`
                        
                        .. attribute:: tftp
                        
                        	TFTP server configuration commands
                        	**type**\:   :py:class:`Tftp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp>`
                        
                        

                        """

                        _prefix = 'ip-tcp-cfg'
                        _revision = '2016-02-26'

                        def __init__(self):
                            super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6, self).__init__()

                            self.yang_name = "ipv6"
                            self.yang_parent_name = "vrf"

                            self.telnet = Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet()
                            self.telnet.parent = self
                            self._children_name_map["telnet"] = "telnet"
                            self._children_yang_names.add("telnet")

                            self.tftp = Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp()
                            self.tftp.parent = self
                            self._children_name_map["tftp"] = "tftp"
                            self._children_yang_names.add("tftp")


                        class Telnet(Entity):
                            """
                            TELNET server configuration commands
                            
                            .. attribute:: tcp
                            
                            	TCP details
                            	**type**\:   :py:class:`Tcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp>`
                            
                            	**presence node**\: True
                            
                            

                            """

                            _prefix = 'ip-tcp-cfg'
                            _revision = '2016-02-26'

                            def __init__(self):
                                super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet, self).__init__()

                                self.yang_name = "telnet"
                                self.yang_parent_name = "ipv6"

                                self.tcp = None
                                self._children_name_map["tcp"] = "tcp"
                                self._children_yang_names.add("tcp")


                            class Tcp(Entity):
                                """
                                TCP details
                                
                                .. attribute:: access_list_name
                                
                                	Access list
                                	**type**\:  str
                                
                                .. attribute:: maximum_server
                                
                                	Set number of allowable servers
                                	**type**\:  int
                                
                                	**range:** 1..100
                                
                                	**mandatory**\: True
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ip-tcp-cfg'
                                _revision = '2016-02-26'

                                def __init__(self):
                                    super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp, self).__init__()

                                    self.yang_name = "tcp"
                                    self.yang_parent_name = "telnet"
                                    self.is_presence_container = True

                                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                                    self.maximum_server = YLeaf(YType.uint32, "maximum-server")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("access_list_name",
                                                    "maximum_server") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.access_list_name.is_set or
                                        self.maximum_server.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.access_list_name.yfilter != YFilter.not_set or
                                        self.maximum_server.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tcp" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.access_list_name.get_name_leafdata())
                                    if (self.maximum_server.is_set or self.maximum_server.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.maximum_server.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "access-list-name" or name == "maximum-server"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "access-list-name"):
                                        self.access_list_name = value
                                        self.access_list_name.value_namespace = name_space
                                        self.access_list_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "maximum-server"):
                                        self.maximum_server = value
                                        self.maximum_server.value_namespace = name_space
                                        self.maximum_server.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (self.tcp is not None)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.tcp is not None and self.tcp.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "telnet" + path_buffer

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

                                if (child_yang_name == "tcp"):
                                    if (self.tcp is None):
                                        self.tcp = Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp()
                                        self.tcp.parent = self
                                        self._children_name_map["tcp"] = "tcp"
                                    return self.tcp

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "tcp"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Tftp(Entity):
                            """
                            TFTP server configuration commands
                            
                            .. attribute:: udp
                            
                            	UDP details
                            	**type**\:   :py:class:`Udp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp>`
                            
                            	**presence node**\: True
                            
                            

                            """

                            _prefix = 'ip-tcp-cfg'
                            _revision = '2016-02-26'

                            def __init__(self):
                                super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp, self).__init__()

                                self.yang_name = "tftp"
                                self.yang_parent_name = "ipv6"

                                self.udp = None
                                self._children_name_map["udp"] = "udp"
                                self._children_yang_names.add("udp")


                            class Udp(Entity):
                                """
                                UDP details
                                
                                .. attribute:: access_list_name
                                
                                	Access list
                                	**type**\:  str
                                
                                .. attribute:: dscp_value
                                
                                	Set IP DSCP (DiffServ CodePoint) for TFTP Server Packets
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: home_directory
                                
                                	Specify device name where file is read from (e .g. flash\:)
                                	**type**\:  str
                                
                                	**mandatory**\: True
                                
                                .. attribute:: maximum_server
                                
                                	Set number of allowable servers, 0 for no\-limit
                                	**type**\:  int
                                
                                	**range:** 0..2147483647
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ip-tcp-cfg'
                                _revision = '2016-02-26'

                                def __init__(self):
                                    super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp, self).__init__()

                                    self.yang_name = "udp"
                                    self.yang_parent_name = "tftp"
                                    self.is_presence_container = True

                                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                                    self.dscp_value = YLeaf(YType.int32, "dscp-value")

                                    self.home_directory = YLeaf(YType.str, "home-directory")

                                    self.maximum_server = YLeaf(YType.uint32, "maximum-server")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("access_list_name",
                                                    "dscp_value",
                                                    "home_directory",
                                                    "maximum_server") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.access_list_name.is_set or
                                        self.dscp_value.is_set or
                                        self.home_directory.is_set or
                                        self.maximum_server.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.access_list_name.yfilter != YFilter.not_set or
                                        self.dscp_value.yfilter != YFilter.not_set or
                                        self.home_directory.yfilter != YFilter.not_set or
                                        self.maximum_server.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "udp" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.access_list_name.get_name_leafdata())
                                    if (self.dscp_value.is_set or self.dscp_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dscp_value.get_name_leafdata())
                                    if (self.home_directory.is_set or self.home_directory.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.home_directory.get_name_leafdata())
                                    if (self.maximum_server.is_set or self.maximum_server.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.maximum_server.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "access-list-name" or name == "dscp-value" or name == "home-directory" or name == "maximum-server"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "access-list-name"):
                                        self.access_list_name = value
                                        self.access_list_name.value_namespace = name_space
                                        self.access_list_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dscp-value"):
                                        self.dscp_value = value
                                        self.dscp_value.value_namespace = name_space
                                        self.dscp_value.value_namespace_prefix = name_space_prefix
                                    if(value_path == "home-directory"):
                                        self.home_directory = value
                                        self.home_directory.value_namespace = name_space
                                        self.home_directory.value_namespace_prefix = name_space_prefix
                                    if(value_path == "maximum-server"):
                                        self.maximum_server = value
                                        self.maximum_server.value_namespace = name_space
                                        self.maximum_server.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (self.udp is not None)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.udp is not None and self.udp.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "tftp" + path_buffer

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

                                if (child_yang_name == "udp"):
                                    if (self.udp is None):
                                        self.udp = Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp()
                                        self.udp.parent = self
                                        self._children_name_map["udp"] = "udp"
                                    return self.udp

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "udp"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                (self.telnet is not None and self.telnet.has_data()) or
                                (self.tftp is not None and self.tftp.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.telnet is not None and self.telnet.has_operation()) or
                                (self.tftp is not None and self.tftp.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv6" + path_buffer

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

                            if (child_yang_name == "telnet"):
                                if (self.telnet is None):
                                    self.telnet = Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet()
                                    self.telnet.parent = self
                                    self._children_name_map["telnet"] = "telnet"
                                return self.telnet

                            if (child_yang_name == "tftp"):
                                if (self.tftp is None):
                                    self.tftp = Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp()
                                    self.tftp.parent = self
                                    self._children_name_map["tftp"] = "tftp"
                                return self.tftp

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "telnet" or name == "tftp"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Ipv4(Entity):
                        """
                        IPV4 related services
                        
                        .. attribute:: telnet
                        
                        	TELNET server configuration commands
                        	**type**\:   :py:class:`Telnet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet>`
                        
                        .. attribute:: tftp
                        
                        	TFTP server configuration commands
                        	**type**\:   :py:class:`Tftp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp>`
                        
                        

                        """

                        _prefix = 'ip-tcp-cfg'
                        _revision = '2016-02-26'

                        def __init__(self):
                            super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4, self).__init__()

                            self.yang_name = "ipv4"
                            self.yang_parent_name = "vrf"

                            self.telnet = Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet()
                            self.telnet.parent = self
                            self._children_name_map["telnet"] = "telnet"
                            self._children_yang_names.add("telnet")

                            self.tftp = Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp()
                            self.tftp.parent = self
                            self._children_name_map["tftp"] = "tftp"
                            self._children_yang_names.add("tftp")


                        class Telnet(Entity):
                            """
                            TELNET server configuration commands
                            
                            .. attribute:: tcp
                            
                            	TCP details
                            	**type**\:   :py:class:`Tcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp>`
                            
                            	**presence node**\: True
                            
                            

                            """

                            _prefix = 'ip-tcp-cfg'
                            _revision = '2016-02-26'

                            def __init__(self):
                                super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet, self).__init__()

                                self.yang_name = "telnet"
                                self.yang_parent_name = "ipv4"

                                self.tcp = None
                                self._children_name_map["tcp"] = "tcp"
                                self._children_yang_names.add("tcp")


                            class Tcp(Entity):
                                """
                                TCP details
                                
                                .. attribute:: access_list_name
                                
                                	Access list
                                	**type**\:  str
                                
                                .. attribute:: maximum_server
                                
                                	Set number of allowable servers
                                	**type**\:  int
                                
                                	**range:** 1..100
                                
                                	**mandatory**\: True
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ip-tcp-cfg'
                                _revision = '2016-02-26'

                                def __init__(self):
                                    super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp, self).__init__()

                                    self.yang_name = "tcp"
                                    self.yang_parent_name = "telnet"
                                    self.is_presence_container = True

                                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                                    self.maximum_server = YLeaf(YType.uint32, "maximum-server")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("access_list_name",
                                                    "maximum_server") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.access_list_name.is_set or
                                        self.maximum_server.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.access_list_name.yfilter != YFilter.not_set or
                                        self.maximum_server.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tcp" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.access_list_name.get_name_leafdata())
                                    if (self.maximum_server.is_set or self.maximum_server.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.maximum_server.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "access-list-name" or name == "maximum-server"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "access-list-name"):
                                        self.access_list_name = value
                                        self.access_list_name.value_namespace = name_space
                                        self.access_list_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "maximum-server"):
                                        self.maximum_server = value
                                        self.maximum_server.value_namespace = name_space
                                        self.maximum_server.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (self.tcp is not None)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.tcp is not None and self.tcp.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "telnet" + path_buffer

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

                                if (child_yang_name == "tcp"):
                                    if (self.tcp is None):
                                        self.tcp = Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp()
                                        self.tcp.parent = self
                                        self._children_name_map["tcp"] = "tcp"
                                    return self.tcp

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "tcp"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Tftp(Entity):
                            """
                            TFTP server configuration commands
                            
                            .. attribute:: udp
                            
                            	UDP details
                            	**type**\:   :py:class:`Udp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp>`
                            
                            	**presence node**\: True
                            
                            

                            """

                            _prefix = 'ip-tcp-cfg'
                            _revision = '2016-02-26'

                            def __init__(self):
                                super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp, self).__init__()

                                self.yang_name = "tftp"
                                self.yang_parent_name = "ipv4"

                                self.udp = None
                                self._children_name_map["udp"] = "udp"
                                self._children_yang_names.add("udp")


                            class Udp(Entity):
                                """
                                UDP details
                                
                                .. attribute:: access_list_name
                                
                                	Access list
                                	**type**\:  str
                                
                                .. attribute:: dscp_value
                                
                                	Set IP DSCP (DiffServ CodePoint) for TFTP Server Packets
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: home_directory
                                
                                	Specify device name where file is read from (e .g. flash\:)
                                	**type**\:  str
                                
                                	**mandatory**\: True
                                
                                .. attribute:: maximum_server
                                
                                	Set number of allowable servers, 0 for no\-limit
                                	**type**\:  int
                                
                                	**range:** 0..2147483647
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ip-tcp-cfg'
                                _revision = '2016-02-26'

                                def __init__(self):
                                    super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp, self).__init__()

                                    self.yang_name = "udp"
                                    self.yang_parent_name = "tftp"
                                    self.is_presence_container = True

                                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                                    self.dscp_value = YLeaf(YType.int32, "dscp-value")

                                    self.home_directory = YLeaf(YType.str, "home-directory")

                                    self.maximum_server = YLeaf(YType.uint32, "maximum-server")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("access_list_name",
                                                    "dscp_value",
                                                    "home_directory",
                                                    "maximum_server") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.access_list_name.is_set or
                                        self.dscp_value.is_set or
                                        self.home_directory.is_set or
                                        self.maximum_server.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.access_list_name.yfilter != YFilter.not_set or
                                        self.dscp_value.yfilter != YFilter.not_set or
                                        self.home_directory.yfilter != YFilter.not_set or
                                        self.maximum_server.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "udp" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.access_list_name.get_name_leafdata())
                                    if (self.dscp_value.is_set or self.dscp_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dscp_value.get_name_leafdata())
                                    if (self.home_directory.is_set or self.home_directory.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.home_directory.get_name_leafdata())
                                    if (self.maximum_server.is_set or self.maximum_server.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.maximum_server.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "access-list-name" or name == "dscp-value" or name == "home-directory" or name == "maximum-server"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "access-list-name"):
                                        self.access_list_name = value
                                        self.access_list_name.value_namespace = name_space
                                        self.access_list_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dscp-value"):
                                        self.dscp_value = value
                                        self.dscp_value.value_namespace = name_space
                                        self.dscp_value.value_namespace_prefix = name_space_prefix
                                    if(value_path == "home-directory"):
                                        self.home_directory = value
                                        self.home_directory.value_namespace = name_space
                                        self.home_directory.value_namespace_prefix = name_space_prefix
                                    if(value_path == "maximum-server"):
                                        self.maximum_server = value
                                        self.maximum_server.value_namespace = name_space
                                        self.maximum_server.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (self.udp is not None)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.udp is not None and self.udp.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "tftp" + path_buffer

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

                                if (child_yang_name == "udp"):
                                    if (self.udp is None):
                                        self.udp = Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp()
                                        self.udp.parent = self
                                        self._children_name_map["udp"] = "udp"
                                    return self.udp

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "udp"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                (self.telnet is not None and self.telnet.has_data()) or
                                (self.tftp is not None and self.tftp.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.telnet is not None and self.telnet.has_operation()) or
                                (self.tftp is not None and self.tftp.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv4" + path_buffer

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

                            if (child_yang_name == "telnet"):
                                if (self.telnet is None):
                                    self.telnet = Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet()
                                    self.telnet.parent = self
                                    self._children_name_map["telnet"] = "telnet"
                                return self.telnet

                            if (child_yang_name == "tftp"):
                                if (self.tftp is None):
                                    self.tftp = Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp()
                                    self.tftp.parent = self
                                    self._children_name_map["tftp"] = "tftp"
                                return self.tftp

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "telnet" or name == "tftp"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.vrf_name.is_set or
                            (self.ipv4 is not None and self.ipv4.has_data()) or
                            (self.ipv6 is not None and self.ipv6.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set or
                            (self.ipv4 is not None and self.ipv4.has_operation()) or
                            (self.ipv6 is not None and self.ipv6.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/vrfs/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "ipv4"):
                            if (self.ipv4 is None):
                                self.ipv4 = Ip.Cinetd.Services.Vrfs.Vrf.Ipv4()
                                self.ipv4.parent = self
                                self._children_name_map["ipv4"] = "ipv4"
                            return self.ipv4

                        if (child_yang_name == "ipv6"):
                            if (self.ipv6 is None):
                                self.ipv6 = Ip.Cinetd.Services.Vrfs.Vrf.Ipv6()
                                self.ipv6.parent = self
                                self._children_name_map["ipv6"] = "ipv6"
                            return self.ipv6

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipv4" or name == "ipv6" or name == "vrf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.vrf:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.vrf:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vrfs" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "vrf"):
                        for c in self.vrf:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ip.Cinetd.Services.Vrfs.Vrf()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.vrf.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "vrf"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Ipv6(Entity):
                """
                IPV6 related services
                
                .. attribute:: small_servers
                
                	Describing IPV4 and IPV6 small servers
                	**type**\:   :py:class:`SmallServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv6.SmallServers>`
                
                

                """

                _prefix = 'ip-tcp-cfg'
                _revision = '2016-02-26'

                def __init__(self):
                    super(Ip.Cinetd.Services.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "services"

                    self.small_servers = Ip.Cinetd.Services.Ipv6.SmallServers()
                    self.small_servers.parent = self
                    self._children_name_map["small_servers"] = "small-servers"
                    self._children_yang_names.add("small-servers")


                class SmallServers(Entity):
                    """
                    Describing IPV4 and IPV6 small servers
                    
                    .. attribute:: tcp_small_servers
                    
                    	Describing TCP related IPV4 and IPV6 small servers
                    	**type**\:   :py:class:`TcpSmallServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'ip-tcp-cfg'
                    _revision = '2016-02-26'

                    def __init__(self):
                        super(Ip.Cinetd.Services.Ipv6.SmallServers, self).__init__()

                        self.yang_name = "small-servers"
                        self.yang_parent_name = "ipv6"

                        self.tcp_small_servers = None
                        self._children_name_map["tcp_small_servers"] = "tcp-small-servers"
                        self._children_yang_names.add("tcp-small-servers")


                    class TcpSmallServers(Entity):
                        """
                        Describing TCP related IPV4 and IPV6 small
                        servers
                        
                        .. attribute:: access_control_list_name
                        
                        	Access list
                        	**type**\:  str
                        
                        .. attribute:: small_server
                        
                        	Set number of allowable TCP small servers, specify 0 for no\-limit
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ip-tcp-cfg'
                        _revision = '2016-02-26'

                        def __init__(self):
                            super(Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers, self).__init__()

                            self.yang_name = "tcp-small-servers"
                            self.yang_parent_name = "small-servers"
                            self.is_presence_container = True

                            self.access_control_list_name = YLeaf(YType.str, "access-control-list-name")

                            self.small_server = YLeaf(YType.int32, "small-server")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("access_control_list_name",
                                            "small_server") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.access_control_list_name.is_set or
                                self.small_server.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.access_control_list_name.yfilter != YFilter.not_set or
                                self.small_server.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "tcp-small-servers" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/ipv6/small-servers/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.access_control_list_name.is_set or self.access_control_list_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.access_control_list_name.get_name_leafdata())
                            if (self.small_server.is_set or self.small_server.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.small_server.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "access-control-list-name" or name == "small-server"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "access-control-list-name"):
                                self.access_control_list_name = value
                                self.access_control_list_name.value_namespace = name_space
                                self.access_control_list_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "small-server"):
                                self.small_server = value
                                self.small_server.value_namespace = name_space
                                self.small_server.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.tcp_small_servers is not None)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.tcp_small_servers is not None and self.tcp_small_servers.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "small-servers" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/ipv6/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "tcp-small-servers"):
                            if (self.tcp_small_servers is None):
                                self.tcp_small_servers = Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers()
                                self.tcp_small_servers.parent = self
                                self._children_name_map["tcp_small_servers"] = "tcp-small-servers"
                            return self.tcp_small_servers

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "tcp-small-servers"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.small_servers is not None and self.small_servers.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.small_servers is not None and self.small_servers.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv6" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "small-servers"):
                        if (self.small_servers is None):
                            self.small_servers = Ip.Cinetd.Services.Ipv6.SmallServers()
                            self.small_servers.parent = self
                            self._children_name_map["small_servers"] = "small-servers"
                        return self.small_servers

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "small-servers"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.ipv4 is not None and self.ipv4.has_data()) or
                    (self.ipv6 is not None and self.ipv6.has_data()) or
                    (self.vrfs is not None and self.vrfs.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.ipv4 is not None and self.ipv4.has_operation()) or
                    (self.ipv6 is not None and self.ipv6.has_operation()) or
                    (self.vrfs is not None and self.vrfs.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "services" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/%s" % self.get_segment_path()
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
                        self.ipv4 = Ip.Cinetd.Services.Ipv4()
                        self.ipv4.parent = self
                        self._children_name_map["ipv4"] = "ipv4"
                    return self.ipv4

                if (child_yang_name == "ipv6"):
                    if (self.ipv6 is None):
                        self.ipv6 = Ip.Cinetd.Services.Ipv6()
                        self.ipv6.parent = self
                        self._children_name_map["ipv6"] = "ipv6"
                    return self.ipv6

                if (child_yang_name == "vrfs"):
                    if (self.vrfs is None):
                        self.vrfs = Ip.Cinetd.Services.Vrfs()
                        self.vrfs.parent = self
                        self._children_name_map["vrfs"] = "vrfs"
                    return self.vrfs

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv4" or name == "ipv6" or name == "vrfs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.services is not None and self.services.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.services is not None and self.services.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cinetd" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "services"):
                if (self.services is None):
                    self.services = Ip.Cinetd.Services()
                    self.services.parent = self
                    self._children_name_map["services"] = "services"
                return self.services

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "services"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class ForwardProtocol(Entity):
        """
        Controls forwarding of physical and directed IP
        broadcasts
        
        .. attribute:: udp
        
        	Packets to a specific UDP port
        	**type**\:   :py:class:`Udp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.ForwardProtocol.Udp>`
        
        

        """

        _prefix = 'ip-udp-cfg'
        _revision = '2016-02-26'

        def __init__(self):
            super(Ip.ForwardProtocol, self).__init__()

            self.yang_name = "forward-protocol"
            self.yang_parent_name = "ip"

            self.udp = Ip.ForwardProtocol.Udp()
            self.udp.parent = self
            self._children_name_map["udp"] = "udp"
            self._children_yang_names.add("udp")


        class Udp(Entity):
            """
            Packets to a specific UDP port
            
            .. attribute:: disable
            
            	Disable IP Forward Protocol UDP
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: ports
            
            	Port configuration
            	**type**\:   :py:class:`Ports <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.ForwardProtocol.Udp.Ports>`
            
            

            """

            _prefix = 'ip-udp-cfg'
            _revision = '2016-02-26'

            def __init__(self):
                super(Ip.ForwardProtocol.Udp, self).__init__()

                self.yang_name = "udp"
                self.yang_parent_name = "forward-protocol"

                self.disable = YLeaf(YType.empty, "disable")

                self.ports = Ip.ForwardProtocol.Udp.Ports()
                self.ports.parent = self
                self._children_name_map["ports"] = "ports"
                self._children_yang_names.add("ports")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("disable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ip.ForwardProtocol.Udp, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ip.ForwardProtocol.Udp, self).__setattr__(name, value)


            class Ports(Entity):
                """
                Port configuration
                
                .. attribute:: port
                
                	Well\-known ports are enabled by default and non well\-known ports are disabled by default. It is not allowed to configure the default
                	**type**\: list of    :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.ForwardProtocol.Udp.Ports.Port>`
                
                

                """

                _prefix = 'ip-udp-cfg'
                _revision = '2016-02-26'

                def __init__(self):
                    super(Ip.ForwardProtocol.Udp.Ports, self).__init__()

                    self.yang_name = "ports"
                    self.yang_parent_name = "udp"

                    self.port = YList(self)

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
                                super(Ip.ForwardProtocol.Udp.Ports, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ip.ForwardProtocol.Udp.Ports, self).__setattr__(name, value)


                class Port(Entity):
                    """
                    Well\-known ports are enabled by default and
                    non well\-known ports are disabled by default.
                    It is not allowed to configure the default.
                    
                    .. attribute:: port_id  <key>
                    
                    	Port number
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: enable
                    
                    	Specify 'false' to disable well\-known ports Domain (53), TFTP (69), NameServer (42), TACACS (49), NetBiosNameService (137), or NetBiosDatagramService (138).  Specify 'true' to enable non well\-known ports
                    	**type**\:  bool
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ip-udp-cfg'
                    _revision = '2016-02-26'

                    def __init__(self):
                        super(Ip.ForwardProtocol.Udp.Ports.Port, self).__init__()

                        self.yang_name = "port"
                        self.yang_parent_name = "ports"

                        self.port_id = YLeaf(YType.uint16, "port-id")

                        self.enable = YLeaf(YType.boolean, "enable")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("port_id",
                                        "enable") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ip.ForwardProtocol.Udp.Ports.Port, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ip.ForwardProtocol.Udp.Ports.Port, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.port_id.is_set or
                            self.enable.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.port_id.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "port" + "[port-id='" + self.port_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-udp-cfg:forward-protocol/udp/ports/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.port_id.is_set or self.port_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port_id.get_name_leafdata())
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
                        if(name == "port-id" or name == "enable"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "port-id"):
                            self.port_id = value
                            self.port_id.value_namespace = name_space
                            self.port_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.port:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.port:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ports" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-udp-cfg:forward-protocol/udp/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "port"):
                        for c in self.port:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ip.ForwardProtocol.Udp.Ports.Port()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.port.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "port"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.disable.is_set or
                    (self.ports is not None and self.ports.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.disable.yfilter != YFilter.not_set or
                    (self.ports is not None and self.ports.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "udp" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-udp-cfg:forward-protocol/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ports"):
                    if (self.ports is None):
                        self.ports = Ip.ForwardProtocol.Udp.Ports()
                        self.ports.parent = self
                        self._children_name_map["ports"] = "ports"
                    return self.ports

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ports" or name == "disable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "disable"):
                    self.disable = value
                    self.disable.value_namespace = name_space
                    self.disable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.udp is not None and self.udp.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.udp is not None and self.udp.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-ip-udp-cfg:forward-protocol" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "udp"):
                if (self.udp is None):
                    self.udp = Ip.ForwardProtocol.Udp()
                    self.udp.parent = self
                    self._children_name_map["udp"] = "udp"
                return self.udp

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "udp"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cinetd is not None and self.cinetd.has_data()) or
            (self.forward_protocol is not None and self.forward_protocol.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cinetd is not None and self.cinetd.has_operation()) or
            (self.forward_protocol is not None and self.forward_protocol.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-tcp-cfg:ip" + path_buffer

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

        if (child_yang_name == "cinetd"):
            if (self.cinetd is None):
                self.cinetd = Ip.Cinetd()
                self.cinetd.parent = self
                self._children_name_map["cinetd"] = "cinetd"
            return self.cinetd

        if (child_yang_name == "forward-protocol"):
            if (self.forward_protocol is None):
                self.forward_protocol = Ip.ForwardProtocol()
                self.forward_protocol.parent = self
                self._children_name_map["forward_protocol"] = "forward-protocol"
            return self.forward_protocol

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cinetd" or name == "forward-protocol"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Ip()
        return self._top_entity

