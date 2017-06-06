""" Cisco_IOS_XE_process_cpu_oper 

This module contains a collection of YANG definitions for
monitoring CPU usage of processes in a Network Element.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CpuUsage(object):
    """
    
    
    .. attribute:: cpu_utilization
    
    	Data nodes for Total CPU Utilizations Statistics
    	**type**\:   :py:class:`CpuUtilization <ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_cpu_oper.CpuUsage.CpuUtilization>`
    
    

    """

    _prefix = 'process-cpu-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.cpu_utilization = CpuUsage.CpuUtilization()
        self.cpu_utilization.parent = self


    class CpuUtilization(object):
        """
        Data nodes for Total CPU Utilizations Statistics.
        
        .. attribute:: cpu_usage_processes
        
        	Data nodes for System wide Process CPU usage Statistics
        	**type**\:   :py:class:`CpuUsageProcesses <ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_cpu_oper.CpuUsage.CpuUtilization.CpuUsageProcesses>`
        
        .. attribute:: five_minutes
        
        	Busy percentage in last five minutes
        	**type**\:  int
        
        	**range:** 0..255
        
        	**units**\: percent
        
        .. attribute:: five_seconds
        
        	Busy percentage in last 5\-seconds
        	**type**\:  int
        
        	**range:** 0..255
        
        	**units**\: percent
        
        .. attribute:: five_seconds_intr
        
        	Interrupt busy percentage in last 5\-seconds
        	**type**\:  int
        
        	**range:** 0..255
        
        	**units**\: percent
        
        .. attribute:: one_minute
        
        	Busy percentage in last one minute
        	**type**\:  int
        
        	**range:** 0..255
        
        	**units**\: percent
        
        

        """

        _prefix = 'process-cpu-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.cpu_usage_processes = CpuUsage.CpuUtilization.CpuUsageProcesses()
            self.cpu_usage_processes.parent = self
            self.five_minutes = None
            self.five_seconds = None
            self.five_seconds_intr = None
            self.one_minute = None


        class CpuUsageProcesses(object):
            """
            Data nodes for System wide Process CPU usage Statistics.
            
            .. attribute:: cpu_usage_process
            
            	The list of software processes on the device
            	**type**\: list of    :py:class:`CpuUsageProcess <ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_cpu_oper.CpuUsage.CpuUtilization.CpuUsageProcesses.CpuUsageProcess>`
            
            

            """

            _prefix = 'process-cpu-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.cpu_usage_process = YList()
                self.cpu_usage_process.parent = self
                self.cpu_usage_process.name = 'cpu_usage_process'


            class CpuUsageProcess(object):
                """
                The list of software processes on the device.
                
                .. attribute:: pid  <key>
                
                	Process\-ID of the process
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: name  <key>
                
                	The name of the process
                	**type**\:  str
                
                .. attribute:: avg_run_time
                
                	Average Run\-time of this process (uSec)
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: micro-seconds
                
                .. attribute:: five_minutes
                
                	Busy percentage in last five minutes
                	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: percent
                
                .. attribute:: five_seconds
                
                	Busy percentage in last 5\-seconds
                	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: percent
                
                .. attribute:: invocation_count
                
                	Total number of invocations
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: one_minute
                
                	Busy percentage in last one minute
                	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: percent
                
                .. attribute:: total_run_time
                
                	Total Run\-time of this process (mSec)
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: milli-seconds
                
                .. attribute:: tty
                
                	TTY bound to by the process
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'process-cpu-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.pid = None
                    self.name = None
                    self.avg_run_time = None
                    self.five_minutes = None
                    self.five_seconds = None
                    self.invocation_count = None
                    self.one_minute = None
                    self.total_run_time = None
                    self.tty = None

                @property
                def _common_path(self):
                    if self.pid is None:
                        raise YPYModelError('Key property pid is None')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XE-process-cpu-oper:cpu-usage/Cisco-IOS-XE-process-cpu-oper:cpu-utilization/Cisco-IOS-XE-process-cpu-oper:cpu-usage-processes/Cisco-IOS-XE-process-cpu-oper:cpu-usage-process[Cisco-IOS-XE-process-cpu-oper:pid = ' + str(self.pid) + '][Cisco-IOS-XE-process-cpu-oper:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.pid is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.avg_run_time is not None:
                        return True

                    if self.five_minutes is not None:
                        return True

                    if self.five_seconds is not None:
                        return True

                    if self.invocation_count is not None:
                        return True

                    if self.one_minute is not None:
                        return True

                    if self.total_run_time is not None:
                        return True

                    if self.tty is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_process_cpu_oper as meta
                    return meta._meta_table['CpuUsage.CpuUtilization.CpuUsageProcesses.CpuUsageProcess']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-process-cpu-oper:cpu-usage/Cisco-IOS-XE-process-cpu-oper:cpu-utilization/Cisco-IOS-XE-process-cpu-oper:cpu-usage-processes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpu_usage_process is not None:
                    for child_ref in self.cpu_usage_process:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_process_cpu_oper as meta
                return meta._meta_table['CpuUsage.CpuUtilization.CpuUsageProcesses']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-process-cpu-oper:cpu-usage/Cisco-IOS-XE-process-cpu-oper:cpu-utilization'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpu_usage_processes is not None and self.cpu_usage_processes._has_data():
                return True

            if self.five_minutes is not None:
                return True

            if self.five_seconds is not None:
                return True

            if self.five_seconds_intr is not None:
                return True

            if self.one_minute is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_process_cpu_oper as meta
            return meta._meta_table['CpuUsage.CpuUtilization']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-process-cpu-oper:cpu-usage'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cpu_utilization is not None and self.cpu_utilization._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_process_cpu_oper as meta
        return meta._meta_table['CpuUsage']['meta_info']


