""" Cisco_IOS_XE_process_memory_oper 

This module contains a collection of YANG definitions for
monitoring memory usage of processes in a Network Element.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class MemoryUsageProcesses(object):
    """
    Data nodes for System wide Process Memory Statistics.
    
    .. attribute:: memory_usage_process
    
    	The list of software processes on the device
    	**type**\: list of    :py:class:`MemoryUsageProcess <ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_memory_oper.MemoryUsageProcesses.MemoryUsageProcess>`
    
    

    """

    _prefix = 'process-memory-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.memory_usage_process = YList()
        self.memory_usage_process.parent = self
        self.memory_usage_process.name = 'memory_usage_process'


    class MemoryUsageProcess(object):
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
            self.parent = None
            self.pid = None
            self.name = None
            self.allocated_memory = None
            self.freed_memory = None
            self.get_buffers = None
            self.holding_memory = None
            self.ret_buffers = None
            self.tty = None

        @property
        def _common_path(self):
            if self.pid is None:
                raise YPYModelError('Key property pid is None')
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/Cisco-IOS-XE-process-memory-oper:memory-usage-processes/Cisco-IOS-XE-process-memory-oper:memory-usage-process[Cisco-IOS-XE-process-memory-oper:pid = ' + str(self.pid) + '][Cisco-IOS-XE-process-memory-oper:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.pid is not None:
                return True

            if self.name is not None:
                return True

            if self.allocated_memory is not None:
                return True

            if self.freed_memory is not None:
                return True

            if self.get_buffers is not None:
                return True

            if self.holding_memory is not None:
                return True

            if self.ret_buffers is not None:
                return True

            if self.tty is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_process_memory_oper as meta
            return meta._meta_table['MemoryUsageProcesses.MemoryUsageProcess']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-process-memory-oper:memory-usage-processes'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.memory_usage_process is not None:
            for child_ref in self.memory_usage_process:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_process_memory_oper as meta
        return meta._meta_table['MemoryUsageProcesses']['meta_info']


