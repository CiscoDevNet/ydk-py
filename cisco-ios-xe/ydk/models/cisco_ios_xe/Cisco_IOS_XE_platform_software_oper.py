""" Cisco_IOS_XE_platform_software_oper 

This module contains a collection of YANG definitions
for monitoring platform software in a Network Element

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BFru(Enum):
    """
    BFru

    FRU type

    .. data:: platform_fru_rp = 0

    .. data:: platform_fru_fp = 1

    .. data:: platform_fru_cc = 2

    .. data:: platform_fru_max = 3

    """

    platform_fru_rp = Enum.YLeaf(0, "platform-fru-rp")

    platform_fru_fp = Enum.YLeaf(1, "platform-fru-fp")

    platform_fru_cc = Enum.YLeaf(2, "platform-fru-cc")

    platform_fru_max = Enum.YLeaf(3, "platform-fru-max")



class CiscoPlatformSoftware(Entity):
    """
    Cisco platform software information
    
    .. attribute:: control_processes
    
    	Information about control processes
    	**type**\:  :py:class:`ControlProcesses <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses>`
    
    

    """

    _prefix = 'platform-sw-ios-xe-oper'
    _revision = '2017-04-01'

    def __init__(self):
        super(CiscoPlatformSoftware, self).__init__()
        self._top_entity = None

        self.yang_name = "cisco-platform-software"
        self.yang_parent_name = "Cisco-IOS-XE-platform-software-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"control-processes" : ("control_processes", CiscoPlatformSoftware.ControlProcesses)}
        self._child_list_classes = {}

        self.control_processes = CiscoPlatformSoftware.ControlProcesses()
        self.control_processes.parent = self
        self._children_name_map["control_processes"] = "control-processes"
        self._children_yang_names.add("control-processes")
        self._segment_path = lambda: "Cisco-IOS-XE-platform-software-oper:cisco-platform-software"


    class ControlProcesses(Entity):
        """
        Information about control processes
        
        .. attribute:: control_process
        
        	The list of control processes
        	**type**\: list of  		 :py:class:`ControlProcess <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess>`
        
        

        """

        _prefix = 'platform-sw-ios-xe-oper'
        _revision = '2017-04-01'

        def __init__(self):
            super(CiscoPlatformSoftware.ControlProcesses, self).__init__()

            self.yang_name = "control-processes"
            self.yang_parent_name = "cisco-platform-software"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"control-process" : ("control_process", CiscoPlatformSoftware.ControlProcesses.ControlProcess)}

            self.control_process = YList(self)
            self._segment_path = lambda: "control-processes"
            self._absolute_path = lambda: "Cisco-IOS-XE-platform-software-oper:cisco-platform-software/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CiscoPlatformSoftware.ControlProcesses, [], name, value)


        class ControlProcess(Entity):
            """
            The list of control processes
            
            .. attribute:: fru  <key>
            
            	Field replaceable unit
            	**type**\:  :py:class:`BFru <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.BFru>`
            
            .. attribute:: slotnum  <key>
            
            	Slot number
            	**type**\: int
            
            	**range:** \-32768..32767
            
            .. attribute:: baynum  <key>
            
            	Bay number
            	**type**\: int
            
            	**range:** \-32768..32767
            
            .. attribute:: chassisnum  <key>
            
            	Chassis number
            	**type**\: int
            
            	**range:** \-32768..32767
            
            .. attribute:: control_process_status
            
            	Status of the control process
            	**type**\: str
            
            .. attribute:: updated
            
            	Number of seconds since the data has been updated
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: load_average_stats
            
            	Load average statictics
            	**type**\:  :py:class:`LoadAverageStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAverageStats>`
            
            .. attribute:: load_avg_minutes
            
            	Load average statistics calculated over a period of time
            	**type**\:  :py:class:`LoadAvgMinutes <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes>`
            
            .. attribute:: memory_stats
            
            	Memory statistics
            	**type**\:  :py:class:`MemoryStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats>`
            
            .. attribute:: per_core_stats
            
            	Processor core statistics
            	**type**\:  :py:class:`PerCoreStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats>`
            
            

            """

            _prefix = 'platform-sw-ios-xe-oper'
            _revision = '2017-04-01'

            def __init__(self):
                super(CiscoPlatformSoftware.ControlProcesses.ControlProcess, self).__init__()

                self.yang_name = "control-process"
                self.yang_parent_name = "control-processes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"load-average-stats" : ("load_average_stats", CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAverageStats), "load-avg-minutes" : ("load_avg_minutes", CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes), "memory-stats" : ("memory_stats", CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats), "per-core-stats" : ("per_core_stats", CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats)}
                self._child_list_classes = {}

                self.fru = YLeaf(YType.enumeration, "fru")

                self.slotnum = YLeaf(YType.int16, "slotnum")

                self.baynum = YLeaf(YType.int16, "baynum")

                self.chassisnum = YLeaf(YType.int16, "chassisnum")

                self.control_process_status = YLeaf(YType.str, "control-process-status")

                self.updated = YLeaf(YType.uint64, "updated")

                self.load_average_stats = CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAverageStats()
                self.load_average_stats.parent = self
                self._children_name_map["load_average_stats"] = "load-average-stats"
                self._children_yang_names.add("load-average-stats")

                self.load_avg_minutes = CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes()
                self.load_avg_minutes.parent = self
                self._children_name_map["load_avg_minutes"] = "load-avg-minutes"
                self._children_yang_names.add("load-avg-minutes")

                self.memory_stats = CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats()
                self.memory_stats.parent = self
                self._children_name_map["memory_stats"] = "memory-stats"
                self._children_yang_names.add("memory-stats")

                self.per_core_stats = CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats()
                self.per_core_stats.parent = self
                self._children_name_map["per_core_stats"] = "per-core-stats"
                self._children_yang_names.add("per-core-stats")
                self._segment_path = lambda: "control-process" + "[fru='" + self.fru.get() + "']" + "[slotnum='" + self.slotnum.get() + "']" + "[baynum='" + self.baynum.get() + "']" + "[chassisnum='" + self.chassisnum.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-platform-software-oper:cisco-platform-software/control-processes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess, ['fru', 'slotnum', 'baynum', 'chassisnum', 'control_process_status', 'updated'], name, value)


            class LoadAverageStats(Entity):
                """
                Load average statictics
                
                .. attribute:: load_average_status
                
                	Load average status
                	**type**\: str
                
                

                """

                _prefix = 'platform-sw-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAverageStats, self).__init__()

                    self.yang_name = "load-average-stats"
                    self.yang_parent_name = "control-process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.load_average_status = YLeaf(YType.str, "load-average-status")
                    self._segment_path = lambda: "load-average-stats"

                def __setattr__(self, name, value):
                    self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAverageStats, ['load_average_status'], name, value)


            class LoadAvgMinutes(Entity):
                """
                Load average statistics calculated over a period of time
                
                .. attribute:: load_avg_minute
                
                	List of Load averages based on a time frame
                	**type**\: list of  		 :py:class:`LoadAvgMinute <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute>`
                
                

                """

                _prefix = 'platform-sw-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes, self).__init__()

                    self.yang_name = "load-avg-minutes"
                    self.yang_parent_name = "control-process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"load-avg-minute" : ("load_avg_minute", CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute)}

                    self.load_avg_minute = YList(self)
                    self._segment_path = lambda: "load-avg-minutes"

                def __setattr__(self, name, value):
                    self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes, [], name, value)


                class LoadAvgMinute(Entity):
                    """
                    List of Load averages based on a time frame
                    
                    .. attribute:: number  <key>
                    
                    	The number of minutes the average was calculated on
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: average
                    
                    	Calculated average
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: status
                    
                    	Load average statistics minute status
                    	**type**\:  :py:class:`Status <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status>`
                    
                    

                    """

                    _prefix = 'platform-sw-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute, self).__init__()

                        self.yang_name = "load-avg-minute"
                        self.yang_parent_name = "load-avg-minutes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"status" : ("status", CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status)}
                        self._child_list_classes = {}

                        self.number = YLeaf(YType.uint64, "number")

                        self.average = YLeaf(YType.str, "average")

                        self.status = CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status()
                        self.status.parent = self
                        self._children_name_map["status"] = "status"
                        self._children_yang_names.add("status")
                        self._segment_path = lambda: "load-avg-minute" + "[number='" + self.number.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute, ['number', 'average'], name, value)


                    class Status(Entity):
                        """
                        Load average statistics minute status
                        
                        .. attribute:: condition
                        
                        	Load average condition
                        	**type**\: str
                        
                        .. attribute:: threshold_status
                        
                        	Load average status
                        	**type**\: str
                        
                        .. attribute:: threshold_value
                        
                        	Load average threshold
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        

                        """

                        _prefix = 'platform-sw-ios-xe-oper'
                        _revision = '2017-04-01'

                        def __init__(self):
                            super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status, self).__init__()

                            self.yang_name = "status"
                            self.yang_parent_name = "load-avg-minute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.condition = YLeaf(YType.str, "condition")

                            self.threshold_status = YLeaf(YType.str, "threshold-status")

                            self.threshold_value = YLeaf(YType.str, "threshold-value")
                            self._segment_path = lambda: "status"

                        def __setattr__(self, name, value):
                            self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status, ['condition', 'threshold_status', 'threshold_value'], name, value)


            class MemoryStats(Entity):
                """
                Memory statistics
                
                .. attribute:: memory_status
                
                	The status of the memory
                	**type**\: str
                
                .. attribute:: total
                
                	The total amount of memory in kb
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: used_number
                
                	The amount of memory being used in kb
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: used_percent
                
                	The percentage of memory being used
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: free_number
                
                	The amount of free memory in kb
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: free_percent
                
                	The percentage of free memory
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: available_number
                
                	The amount of available memory in kb
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: available_percent
                
                	The percentage of available memory
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: committed_number
                
                	The amount of committed memory in kb
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: committed_percent
                
                	The percentage of committed memory
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: status
                
                	Memory status
                	**type**\:  :py:class:`Status <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats.Status>`
                
                

                """

                _prefix = 'platform-sw-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats, self).__init__()

                    self.yang_name = "memory-stats"
                    self.yang_parent_name = "control-process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"status" : ("status", CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats.Status)}
                    self._child_list_classes = {}

                    self.memory_status = YLeaf(YType.str, "memory-status")

                    self.total = YLeaf(YType.uint64, "total")

                    self.used_number = YLeaf(YType.uint64, "used-number")

                    self.used_percent = YLeaf(YType.uint64, "used-percent")

                    self.free_number = YLeaf(YType.uint64, "free-number")

                    self.free_percent = YLeaf(YType.uint64, "free-percent")

                    self.available_number = YLeaf(YType.uint64, "available-number")

                    self.available_percent = YLeaf(YType.uint64, "available-percent")

                    self.committed_number = YLeaf(YType.uint64, "committed-number")

                    self.committed_percent = YLeaf(YType.uint8, "committed-percent")

                    self.status = CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats.Status()
                    self.status.parent = self
                    self._children_name_map["status"] = "status"
                    self._children_yang_names.add("status")
                    self._segment_path = lambda: "memory-stats"

                def __setattr__(self, name, value):
                    self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats, ['memory_status', 'total', 'used_number', 'used_percent', 'free_number', 'free_percent', 'available_number', 'available_percent', 'committed_number', 'committed_percent'], name, value)


                class Status(Entity):
                    """
                    Memory status
                    
                    .. attribute:: warning_threshold_percent
                    
                    	Memory warning threshold value percent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: critical_threshold_percent
                    
                    	Memory critical threshold value percent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'platform-sw-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats.Status, self).__init__()

                        self.yang_name = "status"
                        self.yang_parent_name = "memory-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.warning_threshold_percent = YLeaf(YType.uint32, "warning-threshold-percent")

                        self.critical_threshold_percent = YLeaf(YType.uint32, "critical-threshold-percent")
                        self._segment_path = lambda: "status"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats.Status, ['warning_threshold_percent', 'critical_threshold_percent'], name, value)


            class PerCoreStats(Entity):
                """
                Processor core statistics
                
                .. attribute:: per_core_stat
                
                	List of processor cores
                	**type**\: list of  		 :py:class:`PerCoreStat <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat>`
                
                

                """

                _prefix = 'platform-sw-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats, self).__init__()

                    self.yang_name = "per-core-stats"
                    self.yang_parent_name = "control-process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"per-core-stat" : ("per_core_stat", CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat)}

                    self.per_core_stat = YList(self)
                    self._segment_path = lambda: "per-core-stats"

                def __setattr__(self, name, value):
                    self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats, [], name, value)


                class PerCoreStat(Entity):
                    """
                    List of processor cores
                    
                    .. attribute:: name  <key>
                    
                    	The identifier of the core
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: user
                    
                    	CPU utilization in user mode
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: system
                    
                    	CPU utilization in system mode
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: nice
                    
                    	Nice level
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: idle
                    
                    	Idle percentage
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: irq
                    
                    	The percentage of utilization by irq
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: sirq
                    
                    	The percentage of utilization by sirq
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: io_wait
                    
                    	IOWait percentage
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    

                    """

                    _prefix = 'platform-sw-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat, self).__init__()

                        self.yang_name = "per-core-stat"
                        self.yang_parent_name = "per-core-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.name = YLeaf(YType.uint32, "name")

                        self.user = YLeaf(YType.str, "user")

                        self.system = YLeaf(YType.str, "system")

                        self.nice = YLeaf(YType.str, "nice")

                        self.idle = YLeaf(YType.str, "idle")

                        self.irq = YLeaf(YType.str, "irq")

                        self.sirq = YLeaf(YType.str, "sirq")

                        self.io_wait = YLeaf(YType.str, "io-wait")
                        self._segment_path = lambda: "per-core-stat" + "[name='" + self.name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat, ['name', 'user', 'system', 'nice', 'idle', 'irq', 'sirq', 'io_wait'], name, value)

    def clone_ptr(self):
        self._top_entity = CiscoPlatformSoftware()
        return self._top_entity

