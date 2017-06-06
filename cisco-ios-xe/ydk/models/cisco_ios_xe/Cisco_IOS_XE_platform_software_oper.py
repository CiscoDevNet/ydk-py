""" Cisco_IOS_XE_platform_software_oper 

This module contains a collection of YANG definitions for
monitoring the platform software in a Network Element.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoPlatformSoftware(object):
    """
    
    
    .. attribute:: platform_software_interface_rp_active_brief_forwarding
    
    	DESCRIPTION NEEDED
    	**type**\:   :py:class:`PlatformSoftwareInterfaceRpActiveBriefForwarding <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding>`
    
    .. attribute:: platform_software_status_control_processes
    
    	Contents of the show platform software status control process cli
    	**type**\:   :py:class:`PlatformSoftwareStatusControlProcesses <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses>`
    
    

    """

    _prefix = 'platform-sw-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.platform_software_interface_rp_active_brief_forwarding = CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding()
        self.platform_software_interface_rp_active_brief_forwarding.parent = self
        self.platform_software_status_control_processes = CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses()
        self.platform_software_status_control_processes.parent = self


    class PlatformSoftwareStatusControlProcesses(object):
        """
        Contents of the show platform software status control process cli.
        
        .. attribute:: control_processes
        
        	
        	**type**\:   :py:class:`ControlProcesses <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses>`
        
        

        """

        _prefix = 'platform-sw-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.control_processes = CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses()
            self.control_processes.parent = self


        class ControlProcesses(object):
            """
            
            
            .. attribute:: control_process
            
            	Control process
            	**type**\: list of    :py:class:`ControlProcess <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess>`
            
            

            """

            _prefix = 'platform-sw-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.control_process = YList()
                self.control_process.parent = self
                self.control_process.name = 'control_process'


            class ControlProcess(object):
                """
                Control process
                
                .. attribute:: name  <key>
                
                	Name of the control process
                	**type**\:  str
                
                .. attribute:: load_average_stats
                
                	Statistics on the load average
                	**type**\:   :py:class:`LoadAverageStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAverageStats>`
                
                .. attribute:: load_avg_minutes
                
                	
                	**type**\:   :py:class:`LoadAvgMinutes <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes>`
                
                .. attribute:: memory_stats
                
                	The statistics on the memory
                	**type**\:   :py:class:`MemoryStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.MemoryStats>`
                
                .. attribute:: per_core_stats
                
                	Statistics on each core
                	**type**\:   :py:class:`PerCoreStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.PerCoreStats>`
                
                .. attribute:: status
                
                	Status of the control processer
                	**type**\:  str
                
                .. attribute:: updated
                
                	Number of seconds since the data has been updated
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'platform-sw-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.load_average_stats = CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAverageStats()
                    self.load_average_stats.parent = self
                    self.load_avg_minutes = CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes()
                    self.load_avg_minutes.parent = self
                    self.memory_stats = CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.MemoryStats()
                    self.memory_stats.parent = self
                    self.per_core_stats = CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.PerCoreStats()
                    self.per_core_stats.parent = self
                    self.status = None
                    self.updated = None


                class LoadAverageStats(object):
                    """
                    Statistics on the load average.
                    
                    .. attribute:: load_average_status
                    
                    	
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'platform-sw-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.load_average_status = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-platform-software-oper:load-average-stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.load_average_status is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_platform_software_oper as meta
                        return meta._meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAverageStats']['meta_info']


                class LoadAvgMinutes(object):
                    """
                    
                    
                    .. attribute:: load_avg_minute
                    
                    	Load average statistics based on a time frame
                    	**type**\: list of    :py:class:`LoadAvgMinute <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute>`
                    
                    

                    """

                    _prefix = 'platform-sw-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.load_avg_minute = YList()
                        self.load_avg_minute.parent = self
                        self.load_avg_minute.name = 'load_avg_minute'


                    class LoadAvgMinute(object):
                        """
                        Load average statistics based on a time frame
                        
                        .. attribute:: number  <key>
                        
                        	The number of minutes the average was calculated on
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: average
                        
                        	Format\: Decimal with 2 fraction digits
                        	**type**\:  str
                        
                        .. attribute:: status
                        
                        	
                        	**type**\:   :py:class:`Status <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status>`
                        
                        

                        """

                        _prefix = 'platform-sw-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            self.parent = None
                            self.number = None
                            self.average = None
                            self.status = CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status()
                            self.status.parent = self


                        class Status(object):
                            """
                            
                            
                            .. attribute:: condition
                            
                            	Need description
                            	**type**\:  str
                            
                            .. attribute:: threshold_status
                            
                            	Need description
                            	**type**\:  str
                            
                            .. attribute:: threshold_value
                            
                            	Format\: Decimal with 2 fraction digits
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'platform-sw-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                self.parent = None
                                self.condition = None
                                self.threshold_status = None
                                self.threshold_value = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XE-platform-software-oper:status'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.condition is not None:
                                    return True

                                if self.threshold_status is not None:
                                    return True

                                if self.threshold_value is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_platform_software_oper as meta
                                return meta._meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.number is None:
                                raise YPYModelError('Key property number is None')

                            return self.parent._common_path +'/Cisco-IOS-XE-platform-software-oper:load-avg-minute[Cisco-IOS-XE-platform-software-oper:number = ' + str(self.number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.number is not None:
                                return True

                            if self.average is not None:
                                return True

                            if self.status is not None and self.status._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_platform_software_oper as meta
                            return meta._meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-platform-software-oper:load-avg-minutes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.load_avg_minute is not None:
                            for child_ref in self.load_avg_minute:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_platform_software_oper as meta
                        return meta._meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes']['meta_info']


                class MemoryStats(object):
                    """
                    The statistics on the memory
                    
                    .. attribute:: available_number
                    
                    	The number of available memory in kb
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: available_percent
                    
                    	The percentage of available memory
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: committed_number
                    
                    	The number of committed memory in kb
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: committed_percent
                    
                    	The percentage of comitted memory
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: free_number
                    
                    	The number of free memory in kb
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: free_percent
                    
                    	The percentage of free memory
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: memory_status
                    
                    	The status of the memory
                    	**type**\:  str
                    
                    .. attribute:: status
                    
                    	
                    	**type**\:   :py:class:`Status <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.MemoryStats.Status>`
                    
                    .. attribute:: total
                    
                    	The total number of memory in kb
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: used_number
                    
                    	The number of memory being used in kb
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: used_percent
                    
                    	The percentage of memory being used
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'platform-sw-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.available_number = None
                        self.available_percent = None
                        self.committed_number = None
                        self.committed_percent = None
                        self.free_number = None
                        self.free_percent = None
                        self.memory_status = None
                        self.status = CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.MemoryStats.Status()
                        self.status.parent = self
                        self.total = None
                        self.used_number = None
                        self.used_percent = None


                    class Status(object):
                        """
                        
                        
                        .. attribute:: condition
                        
                        	Need description
                        	**type**\:  str
                        
                        .. attribute:: threshold_status
                        
                        	Need description
                        	**type**\:  str
                        
                        .. attribute:: threshold_value_percent
                        
                        	Need description
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'platform-sw-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            self.parent = None
                            self.condition = None
                            self.threshold_status = None
                            self.threshold_value_percent = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XE-platform-software-oper:status'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.condition is not None:
                                return True

                            if self.threshold_status is not None:
                                return True

                            if self.threshold_value_percent is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_platform_software_oper as meta
                            return meta._meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.MemoryStats.Status']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-platform-software-oper:memory-stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.available_number is not None:
                            return True

                        if self.available_percent is not None:
                            return True

                        if self.committed_number is not None:
                            return True

                        if self.committed_percent is not None:
                            return True

                        if self.free_number is not None:
                            return True

                        if self.free_percent is not None:
                            return True

                        if self.memory_status is not None:
                            return True

                        if self.status is not None and self.status._has_data():
                            return True

                        if self.total is not None:
                            return True

                        if self.used_number is not None:
                            return True

                        if self.used_percent is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_platform_software_oper as meta
                        return meta._meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.MemoryStats']['meta_info']


                class PerCoreStats(object):
                    """
                    Statistics on each core
                    
                    .. attribute:: per_core_stat
                    
                    	A Core
                    	**type**\: list of    :py:class:`PerCoreStat <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat>`
                    
                    

                    """

                    _prefix = 'platform-sw-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.per_core_stat = YList()
                        self.per_core_stat.parent = self
                        self.per_core_stat.name = 'per_core_stat'


                    class PerCoreStat(object):
                        """
                        A Core
                        
                        .. attribute:: name  <key>
                        
                        	The name of the core
                        	**type**\:  str
                        
                        .. attribute:: idle
                        
                        	The percentage that is idle                 Format\: Decimal with 2 fraction digits
                        	**type**\:  str
                        
                        .. attribute:: io_wait
                        
                        	The percentage of utilization by IOwait                 Format\: Decimal with 2 fraction digits
                        	**type**\:  str
                        
                        .. attribute:: irq
                        
                        	The percentage of utilizaion by irq                 Format\: Decimal with 2 fraction digits
                        	**type**\:  str
                        
                        .. attribute:: nice
                        
                        	The percentage of utilization by nice                 Format\: Decimal with 2 fraction digits
                        	**type**\:  str
                        
                        .. attribute:: sirq
                        
                        	The percentage of utilizaion by sirq                 Format\: Decimal with 2 fraction digits
                        	**type**\:  str
                        
                        .. attribute:: system
                        
                        	The percentage of utilization by the system                 Format\: Decimal with 2 fraction digits
                        	**type**\:  str
                        
                        .. attribute:: user
                        
                        	The percentage of utilization by user                 Format\: Decimal with 2 fraction digits
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'platform-sw-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.idle = None
                            self.io_wait = None
                            self.irq = None
                            self.nice = None
                            self.sirq = None
                            self.system = None
                            self.user = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYModelError('Key property name is None')

                            return self.parent._common_path +'/Cisco-IOS-XE-platform-software-oper:per-core-stat[Cisco-IOS-XE-platform-software-oper:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.name is not None:
                                return True

                            if self.idle is not None:
                                return True

                            if self.io_wait is not None:
                                return True

                            if self.irq is not None:
                                return True

                            if self.nice is not None:
                                return True

                            if self.sirq is not None:
                                return True

                            if self.system is not None:
                                return True

                            if self.user is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_platform_software_oper as meta
                            return meta._meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-platform-software-oper:per-core-stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.per_core_stat is not None:
                            for child_ref in self.per_core_stat:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_platform_software_oper as meta
                        return meta._meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.PerCoreStats']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XE-platform-software-oper:cisco-platform-software/Cisco-IOS-XE-platform-software-oper:platform-software-status-control-processes/Cisco-IOS-XE-platform-software-oper:control-processes/Cisco-IOS-XE-platform-software-oper:control-process[Cisco-IOS-XE-platform-software-oper:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.load_average_stats is not None and self.load_average_stats._has_data():
                        return True

                    if self.load_avg_minutes is not None and self.load_avg_minutes._has_data():
                        return True

                    if self.memory_stats is not None and self.memory_stats._has_data():
                        return True

                    if self.per_core_stats is not None and self.per_core_stats._has_data():
                        return True

                    if self.status is not None:
                        return True

                    if self.updated is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_platform_software_oper as meta
                    return meta._meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-platform-software-oper:cisco-platform-software/Cisco-IOS-XE-platform-software-oper:platform-software-status-control-processes/Cisco-IOS-XE-platform-software-oper:control-processes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.control_process is not None:
                    for child_ref in self.control_process:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_platform_software_oper as meta
                return meta._meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-platform-software-oper:cisco-platform-software/Cisco-IOS-XE-platform-software-oper:platform-software-status-control-processes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.control_processes is not None and self.control_processes._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_platform_software_oper as meta
            return meta._meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses']['meta_info']


    class PlatformSoftwareInterfaceRpActiveBriefForwarding(object):
        """
        DESCRIPTION NEEDED
        
        .. attribute:: xos_interfaces
        
        	
        	**type**\:   :py:class:`XosInterfaces <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding.XosInterfaces>`
        
        

        """

        _prefix = 'platform-sw-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.xos_interfaces = CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding.XosInterfaces()
            self.xos_interfaces.parent = self


        class XosInterfaces(object):
            """
            
            
            .. attribute:: xos_interface
            
            	DESCRIPTION NEEDED
            	**type**\: list of    :py:class:`XosInterface <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding.XosInterfaces.XosInterface>`
            
            

            """

            _prefix = 'platform-sw-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.xos_interface = YList()
                self.xos_interface.parent = self
                self.xos_interface.name = 'xos_interface'


            class XosInterface(object):
                """
                DESCRIPTION NEEDED
                
                .. attribute:: name  <key>
                
                	DESCRPITION NEEDED
                	**type**\:  str
                
                .. attribute:: id
                
                	DESCRPITION NEEDED
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: qfp_id
                
                	DESCRPITION NEEDED
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'platform-sw-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.id = None
                    self.qfp_id = None

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XE-platform-software-oper:cisco-platform-software/Cisco-IOS-XE-platform-software-oper:platform-software-interface-rp-active-brief-forwarding/Cisco-IOS-XE-platform-software-oper:xos-interfaces/Cisco-IOS-XE-platform-software-oper:xos-interface[Cisco-IOS-XE-platform-software-oper:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.id is not None:
                        return True

                    if self.qfp_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_platform_software_oper as meta
                    return meta._meta_table['CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding.XosInterfaces.XosInterface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-platform-software-oper:cisco-platform-software/Cisco-IOS-XE-platform-software-oper:platform-software-interface-rp-active-brief-forwarding/Cisco-IOS-XE-platform-software-oper:xos-interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.xos_interface is not None:
                    for child_ref in self.xos_interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_platform_software_oper as meta
                return meta._meta_table['CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding.XosInterfaces']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-platform-software-oper:cisco-platform-software/Cisco-IOS-XE-platform-software-oper:platform-software-interface-rp-active-brief-forwarding'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.xos_interfaces is not None and self.xos_interfaces._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_platform_software_oper as meta
            return meta._meta_table['CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-platform-software-oper:cisco-platform-software'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.platform_software_interface_rp_active_brief_forwarding is not None and self.platform_software_interface_rp_active_brief_forwarding._has_data():
            return True

        if self.platform_software_status_control_processes is not None and self.platform_software_status_control_processes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_platform_software_oper as meta
        return meta._meta_table['CiscoPlatformSoftware']['meta_info']


