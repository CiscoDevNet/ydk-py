""" Cisco_IOS_XR_ha_eem_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ha\-eem package operational data.

This module contains definitions
for the following management objects\:
  system\-monitoring\: Processes operational data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class SystemMonitoring(object):
    """
    Processes operational data
    
    .. attribute:: cpu_utilization
    
    	Processes CPU utilization information
    	**type**\: list of :py:class:`CpuUtilization <ydk.models.ha.Cisco_IOS_XR_ha_eem_oper.SystemMonitoring.CpuUtilization>`
    
    

    """

    _prefix = 'ha-eem-oper'
    _revision = '2015-01-07'

    def __init__(self):
        self.cpu_utilization = YList()
        self.cpu_utilization.parent = self
        self.cpu_utilization.name = 'cpu_utilization'


    class CpuUtilization(object):
        """
        Processes CPU utilization information
        
        .. attribute:: node_name
        
        	Node name
        	**type**\: str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: process_cpu
        
        	Per process CPU utilization
        	**type**\: list of :py:class:`ProcessCpu <ydk.models.ha.Cisco_IOS_XR_ha_eem_oper.SystemMonitoring.CpuUtilization.ProcessCpu>`
        
        .. attribute:: total_cpu_fifteen_minute
        
        	Total CPU utilization in past 15 minute
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: total_cpu_five_minute
        
        	Total CPU utilization in past 5 minute
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: total_cpu_one_minute
        
        	Total CPU utilization in past 1 minute
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'ha-eem-oper'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.node_name = None
            self.process_cpu = YList()
            self.process_cpu.parent = self
            self.process_cpu.name = 'process_cpu'
            self.total_cpu_fifteen_minute = None
            self.total_cpu_five_minute = None
            self.total_cpu_one_minute = None


        class ProcessCpu(object):
            """
            Per process CPU utilization
            
            .. attribute:: process_cpu_fifteen_minute
            
            	Process CPU utilization in percent for past 15 minute
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: process_cpu_five_minute
            
            	Process CPU utilization in percent for past 5 minute
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: process_cpu_one_minute
            
            	Process CPU utilization in percent for past 1 minute
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: process_id
            
            	Process ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: process_name
            
            	Process name
            	**type**\: str
            
            

            """

            _prefix = 'ha-eem-oper'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.process_cpu_fifteen_minute = None
                self.process_cpu_five_minute = None
                self.process_cpu_one_minute = None
                self.process_id = None
                self.process_name = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-ha-eem-oper:process-cpu'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.process_cpu_fifteen_minute is not None:
                    return True

                if self.process_cpu_five_minute is not None:
                    return True

                if self.process_cpu_one_minute is not None:
                    return True

                if self.process_id is not None:
                    return True

                if self.process_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ha._meta import _Cisco_IOS_XR_ha_eem_oper as meta
                return meta._meta_table['SystemMonitoring.CpuUtilization.ProcessCpu']['meta_info']

        @property
        def _common_path(self):
            if self.node_name is None:
                raise YPYDataValidationError('Key property node_name is None')

            return '/Cisco-IOS-XR-ha-eem-oper:system-monitoring/Cisco-IOS-XR-ha-eem-oper:cpu-utilization[Cisco-IOS-XR-ha-eem-oper:node-name = ' + str(self.node_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.node_name is not None:
                return True

            if self.process_cpu is not None:
                for child_ref in self.process_cpu:
                    if child_ref._has_data():
                        return True

            if self.total_cpu_fifteen_minute is not None:
                return True

            if self.total_cpu_five_minute is not None:
                return True

            if self.total_cpu_one_minute is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ha._meta import _Cisco_IOS_XR_ha_eem_oper as meta
            return meta._meta_table['SystemMonitoring.CpuUtilization']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ha-eem-oper:system-monitoring'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.cpu_utilization is not None:
            for child_ref in self.cpu_utilization:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ha._meta import _Cisco_IOS_XR_ha_eem_oper as meta
        return meta._meta_table['SystemMonitoring']['meta_info']


