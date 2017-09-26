""" Cisco_IOS_XR_wdsysmon_fd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR wdsysmon\-fd package operational data.

This module contains definitions
for the following management objects\:
  system\-monitoring\: Processes operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SystemMonitoring(Entity):
    """
    Processes operational data
    
    .. attribute:: cpu_utilization
    
    	Processes CPU utilization information
    	**type**\: list of    :py:class:`CpuUtilization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wdsysmon_fd_oper.SystemMonitoring.CpuUtilization>`
    
    

    """

    _prefix = 'wdsysmon-fd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SystemMonitoring, self).__init__()
        self._top_entity = None

        self.yang_name = "system-monitoring"
        self.yang_parent_name = "Cisco-IOS-XR-wdsysmon-fd-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"cpu-utilization" : ("cpu_utilization", SystemMonitoring.CpuUtilization)}

        self.cpu_utilization = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-wdsysmon-fd-oper:system-monitoring"

    def __setattr__(self, name, value):
        self._perform_setattr(SystemMonitoring, [], name, value)


    class CpuUtilization(Entity):
        """
        Processes CPU utilization information
        
        .. attribute:: node_name  <key>
        
        	Node name
        	**type**\:  str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: process_cpu
        
        	Per process CPU utilization
        	**type**\: list of    :py:class:`ProcessCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wdsysmon_fd_oper.SystemMonitoring.CpuUtilization.ProcessCpu>`
        
        .. attribute:: total_cpu_fifteen_minute
        
        	Total CPU utilization in past 15 minute
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: total_cpu_five_minute
        
        	Total CPU utilization in past 5 minute
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: total_cpu_one_minute
        
        	Total CPU utilization in past 1 minute
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'wdsysmon-fd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SystemMonitoring.CpuUtilization, self).__init__()

            self.yang_name = "cpu-utilization"
            self.yang_parent_name = "system-monitoring"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"process-cpu" : ("process_cpu", SystemMonitoring.CpuUtilization.ProcessCpu)}

            self.node_name = YLeaf(YType.str, "node-name")

            self.total_cpu_fifteen_minute = YLeaf(YType.uint32, "total-cpu-fifteen-minute")

            self.total_cpu_five_minute = YLeaf(YType.uint32, "total-cpu-five-minute")

            self.total_cpu_one_minute = YLeaf(YType.uint32, "total-cpu-one-minute")

            self.process_cpu = YList(self)
            self._segment_path = lambda: "cpu-utilization" + "[node-name='" + self.node_name.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-wdsysmon-fd-oper:system-monitoring/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SystemMonitoring.CpuUtilization, ['node_name', 'total_cpu_fifteen_minute', 'total_cpu_five_minute', 'total_cpu_one_minute'], name, value)


        class ProcessCpu(Entity):
            """
            Per process CPU utilization
            
            .. attribute:: process_cpu_fifteen_minute
            
            	Process CPU utilization in percent for past 15 minute
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: percentage
            
            .. attribute:: process_cpu_five_minute
            
            	Process CPU utilization in percent for past 5 minute
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: percentage
            
            .. attribute:: process_cpu_one_minute
            
            	Process CPU utilization in percent for past 1 minute
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: percentage
            
            .. attribute:: process_id
            
            	Process ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: process_name
            
            	Process name
            	**type**\:  str
            
            

            """

            _prefix = 'wdsysmon-fd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SystemMonitoring.CpuUtilization.ProcessCpu, self).__init__()

                self.yang_name = "process-cpu"
                self.yang_parent_name = "cpu-utilization"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.process_cpu_fifteen_minute = YLeaf(YType.uint32, "process-cpu-fifteen-minute")

                self.process_cpu_five_minute = YLeaf(YType.uint32, "process-cpu-five-minute")

                self.process_cpu_one_minute = YLeaf(YType.uint32, "process-cpu-one-minute")

                self.process_id = YLeaf(YType.uint32, "process-id")

                self.process_name = YLeaf(YType.str, "process-name")
                self._segment_path = lambda: "process-cpu"

            def __setattr__(self, name, value):
                self._perform_setattr(SystemMonitoring.CpuUtilization.ProcessCpu, ['process_cpu_fifteen_minute', 'process_cpu_five_minute', 'process_cpu_one_minute', 'process_id', 'process_name'], name, value)

    def clone_ptr(self):
        self._top_entity = SystemMonitoring()
        return self._top_entity

