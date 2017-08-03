""" Cisco_IOS_XR_ip_udp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-udp package configuration.

This module contains definitions
for the following management objects\:
  ip\-udp\: Global IP UDP configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ip\-tcp\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IpUdp(Entity):
    """
    Global IP UDP configuration
    
    .. attribute:: directory
    
    	UDP directory details
    	**type**\:   :py:class:`Directory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_cfg.IpUdp.Directory>`
    
    	**presence node**\: True
    
    .. attribute:: num_thread
    
    	UDP InQueue and OutQueue threads
    	**type**\:   :py:class:`NumThread <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_cfg.IpUdp.NumThread>`
    
    	**presence node**\: True
    
    .. attribute:: receive_q
    
    	UDP receive Queue Size
    	**type**\:  int
    
    	**range:** 40..800
    
    

    """

    _prefix = 'ip-udp-cfg'
    _revision = '2016-02-26'

    def __init__(self):
        super(IpUdp, self).__init__()
        self._top_entity = None

        self.yang_name = "ip-udp"
        self.yang_parent_name = "Cisco-IOS-XR-ip-udp-cfg"

        self.receive_q = YLeaf(YType.uint32, "receive-q")

        self.directory = None
        self._children_name_map["directory"] = "directory"
        self._children_yang_names.add("directory")

        self.num_thread = None
        self._children_name_map["num_thread"] = "num-thread"
        self._children_yang_names.add("num-thread")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("receive_q") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(IpUdp, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(IpUdp, self).__setattr__(name, value)


    class NumThread(Entity):
        """
        UDP InQueue and OutQueue threads
        
        .. attribute:: udp_in_q_threads
        
        	InQ Threads
        	**type**\:  int
        
        	**range:** 1..16
        
        	**mandatory**\: True
        
        .. attribute:: udp_out_q_threads
        
        	OutQ Threads
        	**type**\:  int
        
        	**range:** 1..16
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-udp-cfg'
        _revision = '2016-02-26'

        def __init__(self):
            super(IpUdp.NumThread, self).__init__()

            self.yang_name = "num-thread"
            self.yang_parent_name = "ip-udp"
            self.is_presence_container = True

            self.udp_in_q_threads = YLeaf(YType.uint32, "udp-in-q-threads")

            self.udp_out_q_threads = YLeaf(YType.uint32, "udp-out-q-threads")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("udp_in_q_threads",
                            "udp_out_q_threads") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IpUdp.NumThread, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpUdp.NumThread, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.udp_in_q_threads.is_set or
                self.udp_out_q_threads.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.udp_in_q_threads.yfilter != YFilter.not_set or
                self.udp_out_q_threads.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "num-thread" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-udp-cfg:ip-udp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.udp_in_q_threads.is_set or self.udp_in_q_threads.yfilter != YFilter.not_set):
                leaf_name_data.append(self.udp_in_q_threads.get_name_leafdata())
            if (self.udp_out_q_threads.is_set or self.udp_out_q_threads.yfilter != YFilter.not_set):
                leaf_name_data.append(self.udp_out_q_threads.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "udp-in-q-threads" or name == "udp-out-q-threads"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "udp-in-q-threads"):
                self.udp_in_q_threads = value
                self.udp_in_q_threads.value_namespace = name_space
                self.udp_in_q_threads.value_namespace_prefix = name_space_prefix
            if(value_path == "udp-out-q-threads"):
                self.udp_out_q_threads = value
                self.udp_out_q_threads.value_namespace = name_space
                self.udp_out_q_threads.value_namespace_prefix = name_space_prefix


    class Directory(Entity):
        """
        UDP directory details
        
        .. attribute:: directoryname
        
        	Directory name
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: max_file_size_files
        
        	Set size of debug files in bytes
        	**type**\:  int
        
        	**range:** 1024..4294967295
        
        	**mandatory**\: True
        
        	**units**\: byte
        
        .. attribute:: max_udp_debug_files
        
        	Set number of Debug files
        	**type**\:  int
        
        	**range:** 1..5000
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-udp-cfg'
        _revision = '2016-02-26'

        def __init__(self):
            super(IpUdp.Directory, self).__init__()

            self.yang_name = "directory"
            self.yang_parent_name = "ip-udp"
            self.is_presence_container = True

            self.directoryname = YLeaf(YType.str, "directoryname")

            self.max_file_size_files = YLeaf(YType.uint32, "max-file-size-files")

            self.max_udp_debug_files = YLeaf(YType.uint32, "max-udp-debug-files")

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
                            "max_file_size_files",
                            "max_udp_debug_files") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IpUdp.Directory, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpUdp.Directory, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.directoryname.is_set or
                self.max_file_size_files.is_set or
                self.max_udp_debug_files.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.directoryname.yfilter != YFilter.not_set or
                self.max_file_size_files.yfilter != YFilter.not_set or
                self.max_udp_debug_files.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "directory" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-udp-cfg:ip-udp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.directoryname.is_set or self.directoryname.yfilter != YFilter.not_set):
                leaf_name_data.append(self.directoryname.get_name_leafdata())
            if (self.max_file_size_files.is_set or self.max_file_size_files.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_file_size_files.get_name_leafdata())
            if (self.max_udp_debug_files.is_set or self.max_udp_debug_files.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_udp_debug_files.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "directoryname" or name == "max-file-size-files" or name == "max-udp-debug-files"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "directoryname"):
                self.directoryname = value
                self.directoryname.value_namespace = name_space
                self.directoryname.value_namespace_prefix = name_space_prefix
            if(value_path == "max-file-size-files"):
                self.max_file_size_files = value
                self.max_file_size_files.value_namespace = name_space
                self.max_file_size_files.value_namespace_prefix = name_space_prefix
            if(value_path == "max-udp-debug-files"):
                self.max_udp_debug_files = value
                self.max_udp_debug_files.value_namespace = name_space
                self.max_udp_debug_files.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.receive_q.is_set or
            (self.directory is not None) or
            (self.num_thread is not None))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.receive_q.yfilter != YFilter.not_set or
            (self.directory is not None and self.directory.has_operation()) or
            (self.num_thread is not None and self.num_thread.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-udp-cfg:ip-udp" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.receive_q.is_set or self.receive_q.yfilter != YFilter.not_set):
            leaf_name_data.append(self.receive_q.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "directory"):
            if (self.directory is None):
                self.directory = IpUdp.Directory()
                self.directory.parent = self
                self._children_name_map["directory"] = "directory"
            return self.directory

        if (child_yang_name == "num-thread"):
            if (self.num_thread is None):
                self.num_thread = IpUdp.NumThread()
                self.num_thread.parent = self
                self._children_name_map["num_thread"] = "num-thread"
            return self.num_thread

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "directory" or name == "num-thread" or name == "receive-q"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "receive-q"):
            self.receive_q = value
            self.receive_q.value_namespace = name_space
            self.receive_q.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = IpUdp()
        return self._top_entity

