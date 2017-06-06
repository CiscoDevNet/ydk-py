""" Cisco_IOS_XE_memory_oper 

This module contains a collection of YANG definitions for
monitoring memory in a Network Element.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class MemoryStats(object):
    """
    Data nodes for All Memory Pool Statistics.
    
    .. attribute:: memory_stat
    
    	The list of software memory pools in the system
    	**type**\: list of    :py:class:`MemoryStat <ydk.models.cisco_ios_xe.Cisco_IOS_XE_memory_oper.MemoryStats.MemoryStat>`
    
    

    """

    _prefix = 'memory-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.memory_stat = YList()
        self.memory_stat.parent = self
        self.memory_stat.name = 'memory_stat'


    class MemoryStat(object):
        """
        The list of software memory pools in the system.
        
        .. attribute:: name  <key>
        
        	The name of the memory pool
        	**type**\:  str
        
        .. attribute:: free_memory
        
        	Total free memory in the pool (bytes)
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: highest_usage
        
        	Historical highest memory usage (bytes)
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: lowest_usage
        
        	Historical lowest memory usage (bytes)
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: total_memory
        
        	Total memory in the pool (bytes)
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: used_memory
        
        	Total used memory in the pool (bytes)
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        

        """

        _prefix = 'memory-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.name = None
            self.free_memory = None
            self.highest_usage = None
            self.lowest_usage = None
            self.total_memory = None
            self.used_memory = None

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/Cisco-IOS-XE-memory-oper:memory-stats/Cisco-IOS-XE-memory-oper:memory-stat[Cisco-IOS-XE-memory-oper:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.name is not None:
                return True

            if self.free_memory is not None:
                return True

            if self.highest_usage is not None:
                return True

            if self.lowest_usage is not None:
                return True

            if self.total_memory is not None:
                return True

            if self.used_memory is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_memory_oper as meta
            return meta._meta_table['MemoryStats.MemoryStat']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-memory-oper:memory-stats'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.memory_stat is not None:
            for child_ref in self.memory_stat:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_memory_oper as meta
        return meta._meta_table['MemoryStats']['meta_info']


