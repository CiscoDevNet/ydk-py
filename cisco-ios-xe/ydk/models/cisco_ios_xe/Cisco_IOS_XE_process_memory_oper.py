""" Cisco_IOS_XE_process_memory_oper 

This module contains a collection of YANG definitions for
monitoring memory usage of processes in a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MemoryUsageProcesses(Entity):
    """
    Data nodes for System wide Process Memory Statistics.
    
    .. attribute:: memory_usage_process
    
    	The list of software processes on the device
    	**type**\: list of  		 :py:class:`MemoryUsageProcess <ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_memory_oper.MemoryUsageProcesses.MemoryUsageProcess>`
    
    

    """

    _prefix = 'process-memory-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(MemoryUsageProcesses, self).__init__()
        self._top_entity = None

        self.yang_name = "memory-usage-processes"
        self.yang_parent_name = "Cisco-IOS-XE-process-memory-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("memory-usage-process", ("memory_usage_process", MemoryUsageProcesses.MemoryUsageProcess))])
        self._leafs = OrderedDict()

        self.memory_usage_process = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-process-memory-oper:memory-usage-processes"

    def __setattr__(self, name, value):
        self._perform_setattr(MemoryUsageProcesses, [], name, value)


    class MemoryUsageProcess(Entity):
        """
        The list of software processes on the device.
        
        .. attribute:: pid  (key)
        
        	Process\-ID of the process
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: name  (key)
        
        	The name of the process
        	**type**\: str
        
        .. attribute:: tty
        
        	TTY bound to by the process
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: allocated_memory
        
        	Total memory allocated to this process (bytes)
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: freed_memory
        
        	Total memory freed by this process (bytes)
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: holding_memory
        
        	Total memory currently held by this process (bytes)
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: get_buffers
        
        	Get Buffers of this process (bytes)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ret_buffers
        
        	Return Buffers of this process (bytes)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'process-memory-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(MemoryUsageProcesses.MemoryUsageProcess, self).__init__()

            self.yang_name = "memory-usage-process"
            self.yang_parent_name = "memory-usage-processes"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['pid','name']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('pid', YLeaf(YType.uint32, 'pid')),
                ('name', YLeaf(YType.str, 'name')),
                ('tty', YLeaf(YType.uint16, 'tty')),
                ('allocated_memory', YLeaf(YType.uint64, 'allocated-memory')),
                ('freed_memory', YLeaf(YType.uint64, 'freed-memory')),
                ('holding_memory', YLeaf(YType.uint64, 'holding-memory')),
                ('get_buffers', YLeaf(YType.uint32, 'get-buffers')),
                ('ret_buffers', YLeaf(YType.uint32, 'ret-buffers')),
            ])
            self.pid = None
            self.name = None
            self.tty = None
            self.allocated_memory = None
            self.freed_memory = None
            self.holding_memory = None
            self.get_buffers = None
            self.ret_buffers = None
            self._segment_path = lambda: "memory-usage-process" + "[pid='" + str(self.pid) + "']" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-process-memory-oper:memory-usage-processes/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MemoryUsageProcesses.MemoryUsageProcess, ['pid', 'name', 'tty', 'allocated_memory', 'freed_memory', 'holding_memory', 'get_buffers', 'ret_buffers'], name, value)

    def clone_ptr(self):
        self._top_entity = MemoryUsageProcesses()
        return self._top_entity

