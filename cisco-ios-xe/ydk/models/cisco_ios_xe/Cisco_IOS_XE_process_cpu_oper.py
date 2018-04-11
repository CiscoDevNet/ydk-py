""" Cisco_IOS_XE_process_cpu_oper 

This module contains a collection of YANG definitions for
monitoring CPU usage of processes in a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CpuUsage(Entity):
    """
    CPU Utilization data
    
    .. attribute:: cpu_utilization
    
    	Data nodes for Total CPU Utilization Statistics
    	**type**\:  :py:class:`CpuUtilization <ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_cpu_oper.CpuUsage.CpuUtilization>`
    
    

    """

    _prefix = 'process-cpu-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(CpuUsage, self).__init__()
        self._top_entity = None

        self.yang_name = "cpu-usage"
        self.yang_parent_name = "Cisco-IOS-XE-process-cpu-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cpu-utilization", ("cpu_utilization", CpuUsage.CpuUtilization))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cpu_utilization = CpuUsage.CpuUtilization()
        self.cpu_utilization.parent = self
        self._children_name_map["cpu_utilization"] = "cpu-utilization"
        self._children_yang_names.add("cpu-utilization")
        self._segment_path = lambda: "Cisco-IOS-XE-process-cpu-oper:cpu-usage"


    class CpuUtilization(Entity):
        """
        Data nodes for Total CPU Utilization Statistics.
        
        .. attribute:: five_seconds
        
        	Busy percentage in last 5\-seconds
        	**type**\: int
        
        	**range:** 0..255
        
        	**units**\: percent
        
        .. attribute:: five_seconds_intr
        
        	Interrupt busy percentage in last 5\-seconds
        	**type**\: int
        
        	**range:** 0..255
        
        	**units**\: percent
        
        .. attribute:: one_minute
        
        	Busy percentage in last one minute
        	**type**\: int
        
        	**range:** 0..255
        
        	**units**\: percent
        
        .. attribute:: five_minutes
        
        	Busy percentage in last five minutes
        	**type**\: int
        
        	**range:** 0..255
        
        	**units**\: percent
        
        .. attribute:: cpu_usage_processes
        
        	Data nodes for System wide Process CPU usage Statistics
        	**type**\:  :py:class:`CpuUsageProcesses <ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_cpu_oper.CpuUsage.CpuUtilization.CpuUsageProcesses>`
        
        

        """

        _prefix = 'process-cpu-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(CpuUsage.CpuUtilization, self).__init__()

            self.yang_name = "cpu-utilization"
            self.yang_parent_name = "cpu-usage"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("cpu-usage-processes", ("cpu_usage_processes", CpuUsage.CpuUtilization.CpuUsageProcesses))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('five_seconds', YLeaf(YType.uint8, 'five-seconds')),
                ('five_seconds_intr', YLeaf(YType.uint8, 'five-seconds-intr')),
                ('one_minute', YLeaf(YType.uint8, 'one-minute')),
                ('five_minutes', YLeaf(YType.uint8, 'five-minutes')),
            ])
            self.five_seconds = None
            self.five_seconds_intr = None
            self.one_minute = None
            self.five_minutes = None

            self.cpu_usage_processes = CpuUsage.CpuUtilization.CpuUsageProcesses()
            self.cpu_usage_processes.parent = self
            self._children_name_map["cpu_usage_processes"] = "cpu-usage-processes"
            self._children_yang_names.add("cpu-usage-processes")
            self._segment_path = lambda: "cpu-utilization"
            self._absolute_path = lambda: "Cisco-IOS-XE-process-cpu-oper:cpu-usage/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CpuUsage.CpuUtilization, ['five_seconds', 'five_seconds_intr', 'one_minute', 'five_minutes'], name, value)


        class CpuUsageProcesses(Entity):
            """
            Data nodes for System wide Process CPU usage Statistics.
            
            .. attribute:: cpu_usage_process
            
            	The list of software processes on the device
            	**type**\: list of  		 :py:class:`CpuUsageProcess <ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_cpu_oper.CpuUsage.CpuUtilization.CpuUsageProcesses.CpuUsageProcess>`
            
            

            """

            _prefix = 'process-cpu-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(CpuUsage.CpuUtilization.CpuUsageProcesses, self).__init__()

                self.yang_name = "cpu-usage-processes"
                self.yang_parent_name = "cpu-utilization"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("cpu-usage-process", ("cpu_usage_process", CpuUsage.CpuUtilization.CpuUsageProcesses.CpuUsageProcess))])
                self._leafs = OrderedDict()

                self.cpu_usage_process = YList(self)
                self._segment_path = lambda: "cpu-usage-processes"
                self._absolute_path = lambda: "Cisco-IOS-XE-process-cpu-oper:cpu-usage/cpu-utilization/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CpuUsage.CpuUtilization.CpuUsageProcesses, [], name, value)


            class CpuUsageProcess(Entity):
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
                
                .. attribute:: total_run_time
                
                	Total Run\-time of this process (mSec)
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: milli-seconds
                
                .. attribute:: invocation_count
                
                	Total number of invocations
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: avg_run_time
                
                	Average Run\-time of this process (uSec)
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: micro-seconds
                
                .. attribute:: five_seconds
                
                	Busy percentage in last 5\-seconds
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: percent
                
                .. attribute:: one_minute
                
                	Busy percentage in last one minute
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: percent
                
                .. attribute:: five_minutes
                
                	Busy percentage in last five minutes
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: percent
                
                

                """

                _prefix = 'process-cpu-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(CpuUsage.CpuUtilization.CpuUsageProcesses.CpuUsageProcess, self).__init__()

                    self.yang_name = "cpu-usage-process"
                    self.yang_parent_name = "cpu-usage-processes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['pid','name']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('pid', YLeaf(YType.uint32, 'pid')),
                        ('name', YLeaf(YType.str, 'name')),
                        ('tty', YLeaf(YType.uint16, 'tty')),
                        ('total_run_time', YLeaf(YType.uint64, 'total-run-time')),
                        ('invocation_count', YLeaf(YType.uint32, 'invocation-count')),
                        ('avg_run_time', YLeaf(YType.uint64, 'avg-run-time')),
                        ('five_seconds', YLeaf(YType.str, 'five-seconds')),
                        ('one_minute', YLeaf(YType.str, 'one-minute')),
                        ('five_minutes', YLeaf(YType.str, 'five-minutes')),
                    ])
                    self.pid = None
                    self.name = None
                    self.tty = None
                    self.total_run_time = None
                    self.invocation_count = None
                    self.avg_run_time = None
                    self.five_seconds = None
                    self.one_minute = None
                    self.five_minutes = None
                    self._segment_path = lambda: "cpu-usage-process" + "[pid='" + str(self.pid) + "']" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XE-process-cpu-oper:cpu-usage/cpu-utilization/cpu-usage-processes/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(CpuUsage.CpuUtilization.CpuUsageProcesses.CpuUsageProcess, ['pid', 'name', 'tty', 'total_run_time', 'invocation_count', 'avg_run_time', 'five_seconds', 'one_minute', 'five_minutes'], name, value)

    def clone_ptr(self):
        self._top_entity = CpuUsage()
        return self._top_entity

