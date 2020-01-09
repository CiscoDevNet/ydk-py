""" Cisco_IOS_XR_wdsysmon_fd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR wdsysmon\-fd package operational data.

This module contains definitions
for the following management objects\:
  system\-monitoring\: Processes operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class SystemMonitoring(_Entity_):
    """
    Processes operational data
    
    .. attribute:: cpu_utilization
    
    	Processes CPU utilization information
    	**type**\: list of  		 :py:class:`CpuUtilization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wdsysmon_fd_oper.SystemMonitoring.CpuUtilization>`
    
    	**config**\: False
    
    

    """

    _prefix = 'wdsysmon-fd-oper'
    _revision = '2019-07-05'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(SystemMonitoring, self).__init__()
        self._top_entity = None

        self.yang_name = "system-monitoring"
        self.yang_parent_name = "Cisco-IOS-XR-wdsysmon-fd-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cpu-utilization", ("cpu_utilization", SystemMonitoring.CpuUtilization))])
        self._leafs = OrderedDict()

        self.cpu_utilization = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-wdsysmon-fd-oper:system-monitoring"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SystemMonitoring, [], name, value)


    class CpuUtilization(_Entity_):
        """
        Processes CPU utilization information
        
        .. attribute:: node_name  (key)
        
        	Node name
        	**type**\: str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        	**config**\: False
        
        .. attribute:: total_cpu_one_minute
        
        	Total CPU utilization in past 1 minute
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: total_cpu_five_minute
        
        	Total CPU utilization in past 5 minute
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: total_cpu_fifteen_minute
        
        	Total CPU utilization in past 15 minute
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: process_cpu
        
        	Per process CPU utilization
        	**type**\: list of  		 :py:class:`ProcessCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wdsysmon_fd_oper.SystemMonitoring.CpuUtilization.ProcessCpu>`
        
        	**config**\: False
        
        

        """

        _prefix = 'wdsysmon-fd-oper'
        _revision = '2019-07-05'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SystemMonitoring.CpuUtilization, self).__init__()

            self.yang_name = "cpu-utilization"
            self.yang_parent_name = "system-monitoring"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['node_name']
            self._child_classes = OrderedDict([("process-cpu", ("process_cpu", SystemMonitoring.CpuUtilization.ProcessCpu))])
            self._leafs = OrderedDict([
                ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ('total_cpu_one_minute', (YLeaf(YType.uint32, 'total-cpu-one-minute'), ['int'])),
                ('total_cpu_five_minute', (YLeaf(YType.uint32, 'total-cpu-five-minute'), ['int'])),
                ('total_cpu_fifteen_minute', (YLeaf(YType.uint32, 'total-cpu-fifteen-minute'), ['int'])),
            ])
            self.node_name = None
            self.total_cpu_one_minute = None
            self.total_cpu_five_minute = None
            self.total_cpu_fifteen_minute = None

            self.process_cpu = YList(self)
            self._segment_path = lambda: "cpu-utilization" + "[node-name='" + str(self.node_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-wdsysmon-fd-oper:system-monitoring/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SystemMonitoring.CpuUtilization, ['node_name', 'total_cpu_one_minute', 'total_cpu_five_minute', 'total_cpu_fifteen_minute'], name, value)


        class ProcessCpu(_Entity_):
            """
            Per process CPU utilization
            
            .. attribute:: process_name
            
            	Process name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: process_id
            
            	Process ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: process_cpu_one_minute
            
            	Process CPU utilization in percent for past 1 minute
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: percentage
            
            .. attribute:: process_cpu_five_minute
            
            	Process CPU utilization in percent for past 5 minute
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: percentage
            
            .. attribute:: process_cpu_fifteen_minute
            
            	Process CPU utilization in percent for past 15 minute
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: percentage
            
            

            """

            _prefix = 'wdsysmon-fd-oper'
            _revision = '2019-07-05'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(SystemMonitoring.CpuUtilization.ProcessCpu, self).__init__()

                self.yang_name = "process-cpu"
                self.yang_parent_name = "cpu-utilization"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                    ('process_id', (YLeaf(YType.uint32, 'process-id'), ['int'])),
                    ('process_cpu_one_minute', (YLeaf(YType.uint32, 'process-cpu-one-minute'), ['int'])),
                    ('process_cpu_five_minute', (YLeaf(YType.uint32, 'process-cpu-five-minute'), ['int'])),
                    ('process_cpu_fifteen_minute', (YLeaf(YType.uint32, 'process-cpu-fifteen-minute'), ['int'])),
                ])
                self.process_name = None
                self.process_id = None
                self.process_cpu_one_minute = None
                self.process_cpu_five_minute = None
                self.process_cpu_fifteen_minute = None
                self._segment_path = lambda: "process-cpu"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SystemMonitoring.CpuUtilization.ProcessCpu, ['process_name', 'process_id', 'process_cpu_one_minute', 'process_cpu_five_minute', 'process_cpu_fifteen_minute'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wdsysmon_fd_oper as meta
                return meta._meta_table['SystemMonitoring.CpuUtilization.ProcessCpu']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wdsysmon_fd_oper as meta
            return meta._meta_table['SystemMonitoring.CpuUtilization']['meta_info']

    def clone_ptr(self):
        self._top_entity = SystemMonitoring()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wdsysmon_fd_oper as meta
        return meta._meta_table['SystemMonitoring']['meta_info']


