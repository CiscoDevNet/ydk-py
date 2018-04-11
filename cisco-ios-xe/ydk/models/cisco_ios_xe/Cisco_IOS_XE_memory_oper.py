""" Cisco_IOS_XE_memory_oper 

This module contains a collection of YANG definitions for
monitoring memory in a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MemoryStatistics(Entity):
    """
    Data nodes for All Memory Pool Statistics.
    
    .. attribute:: memory_statistic
    
    	The list of software memory pools in the system
    	**type**\: list of  		 :py:class:`MemoryStatistic <ydk.models.cisco_ios_xe.Cisco_IOS_XE_memory_oper.MemoryStatistics.MemoryStatistic>`
    
    

    """

    _prefix = 'memory-ios-xe-oper'
    _revision = '2017-04-01'

    def __init__(self):
        super(MemoryStatistics, self).__init__()
        self._top_entity = None

        self.yang_name = "memory-statistics"
        self.yang_parent_name = "Cisco-IOS-XE-memory-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("memory-statistic", ("memory_statistic", MemoryStatistics.MemoryStatistic))])
        self._leafs = OrderedDict()

        self.memory_statistic = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-memory-oper:memory-statistics"

    def __setattr__(self, name, value):
        self._perform_setattr(MemoryStatistics, [], name, value)


    class MemoryStatistic(Entity):
        """
        The list of software memory pools in the system.
        
        .. attribute:: name  (key)
        
        	The name of the memory pool
        	**type**\: str
        
        .. attribute:: total_memory
        
        	Total memory in the pool (bytes)
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: used_memory
        
        	Total used memory in the pool (bytes)
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: free_memory
        
        	Total free memory in the pool (bytes)
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: lowest_usage
        
        	Historical lowest memory usage (bytes)
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: highest_usage
        
        	Historical highest memory usage (bytes)
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        

        """

        _prefix = 'memory-ios-xe-oper'
        _revision = '2017-04-01'

        def __init__(self):
            super(MemoryStatistics.MemoryStatistic, self).__init__()

            self.yang_name = "memory-statistic"
            self.yang_parent_name = "memory-statistics"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', YLeaf(YType.str, 'name')),
                ('total_memory', YLeaf(YType.uint64, 'total-memory')),
                ('used_memory', YLeaf(YType.uint64, 'used-memory')),
                ('free_memory', YLeaf(YType.uint64, 'free-memory')),
                ('lowest_usage', YLeaf(YType.uint64, 'lowest-usage')),
                ('highest_usage', YLeaf(YType.uint64, 'highest-usage')),
            ])
            self.name = None
            self.total_memory = None
            self.used_memory = None
            self.free_memory = None
            self.lowest_usage = None
            self.highest_usage = None
            self._segment_path = lambda: "memory-statistic" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-memory-oper:memory-statistics/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MemoryStatistics.MemoryStatistic, ['name', 'total_memory', 'used_memory', 'free_memory', 'lowest_usage', 'highest_usage'], name, value)

    def clone_ptr(self):
        self._top_entity = MemoryStatistics()
        return self._top_entity

