""" Cisco_IOS_XE_platform_software_oper 

This module contains a collection of YANG definitions
for monitoring platform software in a Network Element

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BFru(Enum):
    """
    BFru (Enum Class)

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
    
    .. attribute:: q_filesystem
    
    	Information about the filesystem
    	**type**\: list of  		 :py:class:`QFilesystem <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.QFilesystem>`
    
    

    """

    _prefix = 'platform-sw-ios-xe-oper'
    _revision = '2017-10-10'

    def __init__(self):
        super(CiscoPlatformSoftware, self).__init__()
        self._top_entity = None

        self.yang_name = "cisco-platform-software"
        self.yang_parent_name = "Cisco-IOS-XE-platform-software-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("control-processes", ("control_processes", CiscoPlatformSoftware.ControlProcesses))])
        self._child_list_classes = OrderedDict([("q-filesystem", ("q_filesystem", CiscoPlatformSoftware.QFilesystem))])
        self._leafs = OrderedDict()

        self.control_processes = CiscoPlatformSoftware.ControlProcesses()
        self.control_processes.parent = self
        self._children_name_map["control_processes"] = "control-processes"
        self._children_yang_names.add("control-processes")

        self.q_filesystem = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-platform-software-oper:cisco-platform-software"

    def __setattr__(self, name, value):
        self._perform_setattr(CiscoPlatformSoftware, [], name, value)


    class ControlProcesses(Entity):
        """
        Information about control processes
        
        .. attribute:: control_process
        
        	The list of control processes
        	**type**\: list of  		 :py:class:`ControlProcess <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess>`
        
        

        """

        _prefix = 'platform-sw-ios-xe-oper'
        _revision = '2017-10-10'

        def __init__(self):
            super(CiscoPlatformSoftware.ControlProcesses, self).__init__()

            self.yang_name = "control-processes"
            self.yang_parent_name = "cisco-platform-software"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("control-process", ("control_process", CiscoPlatformSoftware.ControlProcesses.ControlProcess))])
            self._leafs = OrderedDict()

            self.control_process = YList(self)
            self._segment_path = lambda: "control-processes"
            self._absolute_path = lambda: "Cisco-IOS-XE-platform-software-oper:cisco-platform-software/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CiscoPlatformSoftware.ControlProcesses, [], name, value)


        class ControlProcess(Entity):
            """
            The list of control processes
            
            .. attribute:: fru  (key)
            
            	Field replaceable unit
            	**type**\:  :py:class:`BFru <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.BFru>`
            
            .. attribute:: slotnum  (key)
            
            	Slot number
            	**type**\: int
            
            	**range:** \-32768..32767
            
            .. attribute:: baynum  (key)
            
            	Bay number
            	**type**\: int
            
            	**range:** \-32768..32767
            
            .. attribute:: chassisnum  (key)
            
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
            _revision = '2017-10-10'

            def __init__(self):
                super(CiscoPlatformSoftware.ControlProcesses.ControlProcess, self).__init__()

                self.yang_name = "control-process"
                self.yang_parent_name = "control-processes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['fru','slotnum','baynum','chassisnum']
                self._child_container_classes = OrderedDict([("load-average-stats", ("load_average_stats", CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAverageStats)), ("load-avg-minutes", ("load_avg_minutes", CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes)), ("memory-stats", ("memory_stats", CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats)), ("per-core-stats", ("per_core_stats", CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('fru', YLeaf(YType.enumeration, 'fru')),
                    ('slotnum', YLeaf(YType.int16, 'slotnum')),
                    ('baynum', YLeaf(YType.int16, 'baynum')),
                    ('chassisnum', YLeaf(YType.int16, 'chassisnum')),
                    ('control_process_status', YLeaf(YType.str, 'control-process-status')),
                    ('updated', YLeaf(YType.uint64, 'updated')),
                ])
                self.fru = None
                self.slotnum = None
                self.baynum = None
                self.chassisnum = None
                self.control_process_status = None
                self.updated = None

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
                self._segment_path = lambda: "control-process" + "[fru='" + str(self.fru) + "']" + "[slotnum='" + str(self.slotnum) + "']" + "[baynum='" + str(self.baynum) + "']" + "[chassisnum='" + str(self.chassisnum) + "']"
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
                _revision = '2017-10-10'

                def __init__(self):
                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAverageStats, self).__init__()

                    self.yang_name = "load-average-stats"
                    self.yang_parent_name = "control-process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('load_average_status', YLeaf(YType.str, 'load-average-status')),
                    ])
                    self.load_average_status = None
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
                _revision = '2017-10-10'

                def __init__(self):
                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes, self).__init__()

                    self.yang_name = "load-avg-minutes"
                    self.yang_parent_name = "control-process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("load-avg-minute", ("load_avg_minute", CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute))])
                    self._leafs = OrderedDict()

                    self.load_avg_minute = YList(self)
                    self._segment_path = lambda: "load-avg-minutes"

                def __setattr__(self, name, value):
                    self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes, [], name, value)


                class LoadAvgMinute(Entity):
                    """
                    List of Load averages based on a time frame
                    
                    .. attribute:: number  (key)
                    
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
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute, self).__init__()

                        self.yang_name = "load-avg-minute"
                        self.yang_parent_name = "load-avg-minutes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['number']
                        self._child_container_classes = OrderedDict([("status", ("status", CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('number', YLeaf(YType.uint64, 'number')),
                            ('average', YLeaf(YType.str, 'average')),
                        ])
                        self.number = None
                        self.average = None

                        self.status = CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status()
                        self.status.parent = self
                        self._children_name_map["status"] = "status"
                        self._children_yang_names.add("status")
                        self._segment_path = lambda: "load-avg-minute" + "[number='" + str(self.number) + "']"

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
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status, self).__init__()

                            self.yang_name = "status"
                            self.yang_parent_name = "load-avg-minute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('condition', YLeaf(YType.str, 'condition')),
                                ('threshold_status', YLeaf(YType.str, 'threshold-status')),
                                ('threshold_value', YLeaf(YType.str, 'threshold-value')),
                            ])
                            self.condition = None
                            self.threshold_status = None
                            self.threshold_value = None
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
                _revision = '2017-10-10'

                def __init__(self):
                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats, self).__init__()

                    self.yang_name = "memory-stats"
                    self.yang_parent_name = "control-process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("status", ("status", CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats.Status))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('memory_status', YLeaf(YType.str, 'memory-status')),
                        ('total', YLeaf(YType.uint64, 'total')),
                        ('used_number', YLeaf(YType.uint64, 'used-number')),
                        ('used_percent', YLeaf(YType.uint64, 'used-percent')),
                        ('free_number', YLeaf(YType.uint64, 'free-number')),
                        ('free_percent', YLeaf(YType.uint64, 'free-percent')),
                        ('available_number', YLeaf(YType.uint64, 'available-number')),
                        ('available_percent', YLeaf(YType.uint64, 'available-percent')),
                        ('committed_number', YLeaf(YType.uint64, 'committed-number')),
                        ('committed_percent', YLeaf(YType.uint8, 'committed-percent')),
                    ])
                    self.memory_status = None
                    self.total = None
                    self.used_number = None
                    self.used_percent = None
                    self.free_number = None
                    self.free_percent = None
                    self.available_number = None
                    self.available_percent = None
                    self.committed_number = None
                    self.committed_percent = None

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
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats.Status, self).__init__()

                        self.yang_name = "status"
                        self.yang_parent_name = "memory-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('warning_threshold_percent', YLeaf(YType.uint32, 'warning-threshold-percent')),
                            ('critical_threshold_percent', YLeaf(YType.uint32, 'critical-threshold-percent')),
                        ])
                        self.warning_threshold_percent = None
                        self.critical_threshold_percent = None
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
                _revision = '2017-10-10'

                def __init__(self):
                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats, self).__init__()

                    self.yang_name = "per-core-stats"
                    self.yang_parent_name = "control-process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("per-core-stat", ("per_core_stat", CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat))])
                    self._leafs = OrderedDict()

                    self.per_core_stat = YList(self)
                    self._segment_path = lambda: "per-core-stats"

                def __setattr__(self, name, value):
                    self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats, [], name, value)


                class PerCoreStat(Entity):
                    """
                    List of processor cores
                    
                    .. attribute:: name  (key)
                    
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
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat, self).__init__()

                        self.yang_name = "per-core-stat"
                        self.yang_parent_name = "per-core-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', YLeaf(YType.uint32, 'name')),
                            ('user', YLeaf(YType.str, 'user')),
                            ('system', YLeaf(YType.str, 'system')),
                            ('nice', YLeaf(YType.str, 'nice')),
                            ('idle', YLeaf(YType.str, 'idle')),
                            ('irq', YLeaf(YType.str, 'irq')),
                            ('sirq', YLeaf(YType.str, 'sirq')),
                            ('io_wait', YLeaf(YType.str, 'io-wait')),
                        ])
                        self.name = None
                        self.user = None
                        self.system = None
                        self.nice = None
                        self.idle = None
                        self.irq = None
                        self.sirq = None
                        self.io_wait = None
                        self._segment_path = lambda: "per-core-stat" + "[name='" + str(self.name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat, ['name', 'user', 'system', 'nice', 'idle', 'irq', 'sirq', 'io_wait'], name, value)


    class QFilesystem(Entity):
        """
        Information about the filesystem
        
        .. attribute:: fru  (key)
        
        	Field replaceable unit
        	**type**\:  :py:class:`BFru <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.BFru>`
        
        .. attribute:: slotnum  (key)
        
        	Slot number
        	**type**\: int
        
        	**range:** \-32768..32767
        
        .. attribute:: baynum  (key)
        
        	Bay number
        	**type**\: int
        
        	**range:** \-32768..32767
        
        .. attribute:: chassisnum  (key)
        
        	Chassis number
        	**type**\: int
        
        	**range:** \-32768..32767
        
        .. attribute:: partitions
        
        	Information about partitions
        	**type**\: list of  		 :py:class:`Partitions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.QFilesystem.Partitions>`
        
        .. attribute:: core_files
        
        	Information about core files
        	**type**\: list of  		 :py:class:`CoreFiles <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.QFilesystem.CoreFiles>`
        
        

        """

        _prefix = 'platform-sw-ios-xe-oper'
        _revision = '2017-10-10'

        def __init__(self):
            super(CiscoPlatformSoftware.QFilesystem, self).__init__()

            self.yang_name = "q-filesystem"
            self.yang_parent_name = "cisco-platform-software"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['fru','slotnum','baynum','chassisnum']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("partitions", ("partitions", CiscoPlatformSoftware.QFilesystem.Partitions)), ("core-files", ("core_files", CiscoPlatformSoftware.QFilesystem.CoreFiles))])
            self._leafs = OrderedDict([
                ('fru', YLeaf(YType.enumeration, 'fru')),
                ('slotnum', YLeaf(YType.int16, 'slotnum')),
                ('baynum', YLeaf(YType.int16, 'baynum')),
                ('chassisnum', YLeaf(YType.int16, 'chassisnum')),
            ])
            self.fru = None
            self.slotnum = None
            self.baynum = None
            self.chassisnum = None

            self.partitions = YList(self)
            self.core_files = YList(self)
            self._segment_path = lambda: "q-filesystem" + "[fru='" + str(self.fru) + "']" + "[slotnum='" + str(self.slotnum) + "']" + "[baynum='" + str(self.baynum) + "']" + "[chassisnum='" + str(self.chassisnum) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-platform-software-oper:cisco-platform-software/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CiscoPlatformSoftware.QFilesystem, ['fru', 'slotnum', 'baynum', 'chassisnum'], name, value)


        class Partitions(Entity):
            """
            Information about partitions
            
            .. attribute:: name  (key)
            
            	The name of the partition
            	**type**\: str
            
            .. attribute:: total_size
            
            	Total size of the partition in Kilobytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: used_size
            
            	Size used in Kilobytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'platform-sw-ios-xe-oper'
            _revision = '2017-10-10'

            def __init__(self):
                super(CiscoPlatformSoftware.QFilesystem.Partitions, self).__init__()

                self.yang_name = "partitions"
                self.yang_parent_name = "q-filesystem"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['name']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                    ('total_size', YLeaf(YType.uint64, 'total-size')),
                    ('used_size', YLeaf(YType.uint64, 'used-size')),
                ])
                self.name = None
                self.total_size = None
                self.used_size = None
                self._segment_path = lambda: "partitions" + "[name='" + str(self.name) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(CiscoPlatformSoftware.QFilesystem.Partitions, ['name', 'total_size', 'used_size'], name, value)


        class CoreFiles(Entity):
            """
            Information about core files
            
            .. attribute:: filename  (key)
            
            	The core filename
            	**type**\: str
            
            .. attribute:: time
            
            	The date of generation
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            

            """

            _prefix = 'platform-sw-ios-xe-oper'
            _revision = '2017-10-10'

            def __init__(self):
                super(CiscoPlatformSoftware.QFilesystem.CoreFiles, self).__init__()

                self.yang_name = "core-files"
                self.yang_parent_name = "q-filesystem"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['filename']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('filename', YLeaf(YType.str, 'filename')),
                    ('time', YLeaf(YType.str, 'time')),
                ])
                self.filename = None
                self.time = None
                self._segment_path = lambda: "core-files" + "[filename='" + str(self.filename) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(CiscoPlatformSoftware.QFilesystem.CoreFiles, ['filename', 'time'], name, value)

    def clone_ptr(self):
        self._top_entity = CiscoPlatformSoftware()
        return self._top_entity

