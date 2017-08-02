""" Cisco_IOS_XE_process_memory_oper 

This module contains a collection of YANG definitions for
monitoring memory usage of processes in a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MemoryUsageProcesses(Entity):
    """
    Data nodes for System wide Process Memory Statistics.
    
    .. attribute:: memory_usage_process
    
    	The list of software processes on the device
    	**type**\: list of    :py:class:`MemoryUsageProcess <ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_memory_oper.MemoryUsageProcesses.MemoryUsageProcess>`
    
    

    """

    _prefix = 'process-memory-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(MemoryUsageProcesses, self).__init__()
        self._top_entity = None

        self.yang_name = "memory-usage-processes"
        self.yang_parent_name = "Cisco-IOS-XE-process-memory-oper"

        self.memory_usage_process = YList(self)

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
                    super(MemoryUsageProcesses, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(MemoryUsageProcesses, self).__setattr__(name, value)


    class MemoryUsageProcess(Entity):
        """
        The list of software processes on the device.
        
        .. attribute:: pid  <key>
        
        	Process\-ID of the process
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: name  <key>
        
        	The name of the process
        	**type**\:  str
        
        .. attribute:: allocated_memory
        
        	Total memory allocated to this process (bytes)
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: freed_memory
        
        	Total memory freed by this process (bytes)
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: get_buffers
        
        	Get Buffers of this process (bytes)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: holding_memory
        
        	Total memory currently held by this process (bytes)
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: ret_buffers
        
        	Return Buffers of this process (bytes)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tty
        
        	TTY bound to by the process
        	**type**\:  int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'process-memory-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(MemoryUsageProcesses.MemoryUsageProcess, self).__init__()

            self.yang_name = "memory-usage-process"
            self.yang_parent_name = "memory-usage-processes"

            self.pid = YLeaf(YType.uint32, "pid")

            self.name = YLeaf(YType.str, "name")

            self.allocated_memory = YLeaf(YType.uint64, "allocated-memory")

            self.freed_memory = YLeaf(YType.uint64, "freed-memory")

            self.get_buffers = YLeaf(YType.uint32, "get-buffers")

            self.holding_memory = YLeaf(YType.uint64, "holding-memory")

            self.ret_buffers = YLeaf(YType.uint32, "ret-buffers")

            self.tty = YLeaf(YType.uint16, "tty")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("pid",
                            "name",
                            "allocated_memory",
                            "freed_memory",
                            "get_buffers",
                            "holding_memory",
                            "ret_buffers",
                            "tty") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MemoryUsageProcesses.MemoryUsageProcess, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MemoryUsageProcesses.MemoryUsageProcess, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.pid.is_set or
                self.name.is_set or
                self.allocated_memory.is_set or
                self.freed_memory.is_set or
                self.get_buffers.is_set or
                self.holding_memory.is_set or
                self.ret_buffers.is_set or
                self.tty.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.pid.yfilter != YFilter.not_set or
                self.name.yfilter != YFilter.not_set or
                self.allocated_memory.yfilter != YFilter.not_set or
                self.freed_memory.yfilter != YFilter.not_set or
                self.get_buffers.yfilter != YFilter.not_set or
                self.holding_memory.yfilter != YFilter.not_set or
                self.ret_buffers.yfilter != YFilter.not_set or
                self.tty.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "memory-usage-process" + "[pid='" + self.pid.get() + "']" + "[name='" + self.name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-process-memory-oper:memory-usage-processes/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.pid.is_set or self.pid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.pid.get_name_leafdata())
            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.name.get_name_leafdata())
            if (self.allocated_memory.is_set or self.allocated_memory.yfilter != YFilter.not_set):
                leaf_name_data.append(self.allocated_memory.get_name_leafdata())
            if (self.freed_memory.is_set or self.freed_memory.yfilter != YFilter.not_set):
                leaf_name_data.append(self.freed_memory.get_name_leafdata())
            if (self.get_buffers.is_set or self.get_buffers.yfilter != YFilter.not_set):
                leaf_name_data.append(self.get_buffers.get_name_leafdata())
            if (self.holding_memory.is_set or self.holding_memory.yfilter != YFilter.not_set):
                leaf_name_data.append(self.holding_memory.get_name_leafdata())
            if (self.ret_buffers.is_set or self.ret_buffers.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ret_buffers.get_name_leafdata())
            if (self.tty.is_set or self.tty.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tty.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "pid" or name == "name" or name == "allocated-memory" or name == "freed-memory" or name == "get-buffers" or name == "holding-memory" or name == "ret-buffers" or name == "tty"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "pid"):
                self.pid = value
                self.pid.value_namespace = name_space
                self.pid.value_namespace_prefix = name_space_prefix
            if(value_path == "name"):
                self.name = value
                self.name.value_namespace = name_space
                self.name.value_namespace_prefix = name_space_prefix
            if(value_path == "allocated-memory"):
                self.allocated_memory = value
                self.allocated_memory.value_namespace = name_space
                self.allocated_memory.value_namespace_prefix = name_space_prefix
            if(value_path == "freed-memory"):
                self.freed_memory = value
                self.freed_memory.value_namespace = name_space
                self.freed_memory.value_namespace_prefix = name_space_prefix
            if(value_path == "get-buffers"):
                self.get_buffers = value
                self.get_buffers.value_namespace = name_space
                self.get_buffers.value_namespace_prefix = name_space_prefix
            if(value_path == "holding-memory"):
                self.holding_memory = value
                self.holding_memory.value_namespace = name_space
                self.holding_memory.value_namespace_prefix = name_space_prefix
            if(value_path == "ret-buffers"):
                self.ret_buffers = value
                self.ret_buffers.value_namespace = name_space
                self.ret_buffers.value_namespace_prefix = name_space_prefix
            if(value_path == "tty"):
                self.tty = value
                self.tty.value_namespace = name_space
                self.tty.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.memory_usage_process:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.memory_usage_process:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-process-memory-oper:memory-usage-processes" + path_buffer

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

        if (child_yang_name == "memory-usage-process"):
            for c in self.memory_usage_process:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = MemoryUsageProcesses.MemoryUsageProcess()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.memory_usage_process.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "memory-usage-process"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MemoryUsageProcesses()
        return self._top_entity

