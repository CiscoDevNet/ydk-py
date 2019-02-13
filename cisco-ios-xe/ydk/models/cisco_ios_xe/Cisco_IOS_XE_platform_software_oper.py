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
    
    .. attribute:: system_usages
    
    	Platform system usage information
    	**type**\:  :py:class:`SystemUsages <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.SystemUsages>`
    
    	**config**\: False
    
    .. attribute:: control_processes
    
    	Information about control processes
    	**type**\:  :py:class:`ControlProcesses <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses>`
    
    	**config**\: False
    
    .. attribute:: q_filesystem
    
    	Information about the filesystem
    	**type**\: list of  		 :py:class:`QFilesystem <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.QFilesystem>`
    
    	**config**\: False
    
    

    """

    _prefix = 'platform-sw-ios-xe-oper'
    _revision = '2018-03-09'

    def __init__(self):
        super(CiscoPlatformSoftware, self).__init__()
        self._top_entity = None

        self.yang_name = "cisco-platform-software"
        self.yang_parent_name = "Cisco-IOS-XE-platform-software-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("system-usages", ("system_usages", CiscoPlatformSoftware.SystemUsages)), ("control-processes", ("control_processes", CiscoPlatformSoftware.ControlProcesses)), ("q-filesystem", ("q_filesystem", CiscoPlatformSoftware.QFilesystem))])
        self._leafs = OrderedDict()

        self.system_usages = CiscoPlatformSoftware.SystemUsages()
        self.system_usages.parent = self
        self._children_name_map["system_usages"] = "system-usages"

        self.control_processes = CiscoPlatformSoftware.ControlProcesses()
        self.control_processes.parent = self
        self._children_name_map["control_processes"] = "control-processes"

        self.q_filesystem = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-platform-software-oper:cisco-platform-software"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CiscoPlatformSoftware, [], name, value)


    class SystemUsages(Entity):
        """
        Platform system usage information
        
        .. attribute:: system_usage
        
        	The list of process system usage
        	**type**\: list of  		 :py:class:`SystemUsage <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.SystemUsages.SystemUsage>`
        
        	**config**\: False
        
        

        """

        _prefix = 'platform-sw-ios-xe-oper'
        _revision = '2018-03-09'

        def __init__(self):
            super(CiscoPlatformSoftware.SystemUsages, self).__init__()

            self.yang_name = "system-usages"
            self.yang_parent_name = "cisco-platform-software"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("system-usage", ("system_usage", CiscoPlatformSoftware.SystemUsages.SystemUsage))])
            self._leafs = OrderedDict()

            self.system_usage = YList(self)
            self._segment_path = lambda: "system-usages"
            self._absolute_path = lambda: "Cisco-IOS-XE-platform-software-oper:cisco-platform-software/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CiscoPlatformSoftware.SystemUsages, [], name, value)


        class SystemUsage(Entity):
            """
            The list of process system usage
            
            .. attribute:: fru  (key)
            
            	Field replaceable unit
            	**type**\:  :py:class:`BFru <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.BFru>`
            
            	**config**\: False
            
            .. attribute:: slotnum  (key)
            
            	Slot number
            	**type**\: int
            
            	**range:** \-32768..32767
            
            	**config**\: False
            
            .. attribute:: baynum  (key)
            
            	Bay number
            	**type**\: int
            
            	**range:** \-32768..32767
            
            	**config**\: False
            
            .. attribute:: chassisnum  (key)
            
            	Chassis number
            	**type**\: int
            
            	**range:** \-32768..32767
            
            	**config**\: False
            
            .. attribute:: process_system_usages
            
            	List of process system usage
            	**type**\:  :py:class:`ProcessSystemUsages <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.SystemUsages.SystemUsage.ProcessSystemUsages>`
            
            	**config**\: False
            
            

            """

            _prefix = 'platform-sw-ios-xe-oper'
            _revision = '2018-03-09'

            def __init__(self):
                super(CiscoPlatformSoftware.SystemUsages.SystemUsage, self).__init__()

                self.yang_name = "system-usage"
                self.yang_parent_name = "system-usages"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['fru','slotnum','baynum','chassisnum']
                self._child_classes = OrderedDict([("process-system-usages", ("process_system_usages", CiscoPlatformSoftware.SystemUsages.SystemUsage.ProcessSystemUsages))])
                self._leafs = OrderedDict([
                    ('fru', (YLeaf(YType.enumeration, 'fru'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper', 'BFru', '')])),
                    ('slotnum', (YLeaf(YType.int16, 'slotnum'), ['int'])),
                    ('baynum', (YLeaf(YType.int16, 'baynum'), ['int'])),
                    ('chassisnum', (YLeaf(YType.int16, 'chassisnum'), ['int'])),
                ])
                self.fru = None
                self.slotnum = None
                self.baynum = None
                self.chassisnum = None

                self.process_system_usages = CiscoPlatformSoftware.SystemUsages.SystemUsage.ProcessSystemUsages()
                self.process_system_usages.parent = self
                self._children_name_map["process_system_usages"] = "process-system-usages"
                self._segment_path = lambda: "system-usage" + "[fru='" + str(self.fru) + "']" + "[slotnum='" + str(self.slotnum) + "']" + "[baynum='" + str(self.baynum) + "']" + "[chassisnum='" + str(self.chassisnum) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-platform-software-oper:cisco-platform-software/system-usages/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CiscoPlatformSoftware.SystemUsages.SystemUsage, ['fru', 'slotnum', 'baynum', 'chassisnum'], name, value)


            class ProcessSystemUsages(Entity):
                """
                List of process system usage
                
                .. attribute:: process_system_usage
                
                	Per\-process system usage
                	**type**\: list of  		 :py:class:`ProcessSystemUsage <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.SystemUsages.SystemUsage.ProcessSystemUsages.ProcessSystemUsage>`
                
                	**config**\: False
                
                

                """

                _prefix = 'platform-sw-ios-xe-oper'
                _revision = '2018-03-09'

                def __init__(self):
                    super(CiscoPlatformSoftware.SystemUsages.SystemUsage.ProcessSystemUsages, self).__init__()

                    self.yang_name = "process-system-usages"
                    self.yang_parent_name = "system-usage"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("process-system-usage", ("process_system_usage", CiscoPlatformSoftware.SystemUsages.SystemUsage.ProcessSystemUsages.ProcessSystemUsage))])
                    self._leafs = OrderedDict()

                    self.process_system_usage = YList(self)
                    self._segment_path = lambda: "process-system-usages"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(CiscoPlatformSoftware.SystemUsages.SystemUsage.ProcessSystemUsages, [], name, value)


                class ProcessSystemUsage(Entity):
                    """
                    Per\-process system usage
                    
                    .. attribute:: pid  (key)
                    
                    	The pid of the process
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: name
                    
                    	Process name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: total_run_time
                    
                    	Total run time in seconds
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: five_seconds
                    
                    	Busy percentage in last 5\-seconds
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: allocated_memory
                    
                    	Memory allocated to this process in kB
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: allocated_memory_percent
                    
                    	Percentage of memory allocated to this process
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'platform-sw-ios-xe-oper'
                    _revision = '2018-03-09'

                    def __init__(self):
                        super(CiscoPlatformSoftware.SystemUsages.SystemUsage.ProcessSystemUsages.ProcessSystemUsage, self).__init__()

                        self.yang_name = "process-system-usage"
                        self.yang_parent_name = "process-system-usages"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['pid']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('pid', (YLeaf(YType.uint32, 'pid'), ['int'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('total_run_time', (YLeaf(YType.uint64, 'total-run-time'), ['int'])),
                            ('five_seconds', (YLeaf(YType.uint64, 'five-seconds'), ['int'])),
                            ('allocated_memory', (YLeaf(YType.uint64, 'allocated-memory'), ['int'])),
                            ('allocated_memory_percent', (YLeaf(YType.uint32, 'allocated-memory-percent'), ['int'])),
                        ])
                        self.pid = None
                        self.name = None
                        self.total_run_time = None
                        self.five_seconds = None
                        self.allocated_memory = None
                        self.allocated_memory_percent = None
                        self._segment_path = lambda: "process-system-usage" + "[pid='" + str(self.pid) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(CiscoPlatformSoftware.SystemUsages.SystemUsage.ProcessSystemUsages.ProcessSystemUsage, ['pid', 'name', 'total_run_time', 'five_seconds', 'allocated_memory', 'allocated_memory_percent'], name, value)






    class ControlProcesses(Entity):
        """
        Information about control processes
        
        .. attribute:: control_process
        
        	The list of control processes
        	**type**\: list of  		 :py:class:`ControlProcess <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess>`
        
        	**config**\: False
        
        

        """

        _prefix = 'platform-sw-ios-xe-oper'
        _revision = '2018-03-09'

        def __init__(self):
            super(CiscoPlatformSoftware.ControlProcesses, self).__init__()

            self.yang_name = "control-processes"
            self.yang_parent_name = "cisco-platform-software"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("control-process", ("control_process", CiscoPlatformSoftware.ControlProcesses.ControlProcess))])
            self._leafs = OrderedDict()

            self.control_process = YList(self)
            self._segment_path = lambda: "control-processes"
            self._absolute_path = lambda: "Cisco-IOS-XE-platform-software-oper:cisco-platform-software/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CiscoPlatformSoftware.ControlProcesses, [], name, value)


        class ControlProcess(Entity):
            """
            The list of control processes
            
            .. attribute:: fru  (key)
            
            	Field replaceable unit
            	**type**\:  :py:class:`BFru <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.BFru>`
            
            	**config**\: False
            
            .. attribute:: slotnum  (key)
            
            	Slot number
            	**type**\: int
            
            	**range:** \-32768..32767
            
            	**config**\: False
            
            .. attribute:: baynum  (key)
            
            	Bay number
            	**type**\: int
            
            	**range:** \-32768..32767
            
            	**config**\: False
            
            .. attribute:: chassisnum  (key)
            
            	Chassis number
            	**type**\: int
            
            	**range:** \-32768..32767
            
            	**config**\: False
            
            .. attribute:: control_process_status
            
            	Status of the control process
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: updated
            
            	Number of seconds since the data has been updated
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: load_average_stats
            
            	Load average statictics
            	**type**\:  :py:class:`LoadAverageStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAverageStats>`
            
            	**config**\: False
            
            .. attribute:: load_avg_minutes
            
            	Load average statistics calculated over a period of time
            	**type**\:  :py:class:`LoadAvgMinutes <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes>`
            
            	**config**\: False
            
            .. attribute:: memory_stats
            
            	Memory statistics
            	**type**\:  :py:class:`MemoryStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats>`
            
            	**config**\: False
            
            .. attribute:: per_core_stats
            
            	Processor core statistics
            	**type**\:  :py:class:`PerCoreStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats>`
            
            	**config**\: False
            
            

            """

            _prefix = 'platform-sw-ios-xe-oper'
            _revision = '2018-03-09'

            def __init__(self):
                super(CiscoPlatformSoftware.ControlProcesses.ControlProcess, self).__init__()

                self.yang_name = "control-process"
                self.yang_parent_name = "control-processes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['fru','slotnum','baynum','chassisnum']
                self._child_classes = OrderedDict([("load-average-stats", ("load_average_stats", CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAverageStats)), ("load-avg-minutes", ("load_avg_minutes", CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes)), ("memory-stats", ("memory_stats", CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats)), ("per-core-stats", ("per_core_stats", CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats))])
                self._leafs = OrderedDict([
                    ('fru', (YLeaf(YType.enumeration, 'fru'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper', 'BFru', '')])),
                    ('slotnum', (YLeaf(YType.int16, 'slotnum'), ['int'])),
                    ('baynum', (YLeaf(YType.int16, 'baynum'), ['int'])),
                    ('chassisnum', (YLeaf(YType.int16, 'chassisnum'), ['int'])),
                    ('control_process_status', (YLeaf(YType.str, 'control-process-status'), ['str'])),
                    ('updated', (YLeaf(YType.uint64, 'updated'), ['int'])),
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

                self.load_avg_minutes = CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes()
                self.load_avg_minutes.parent = self
                self._children_name_map["load_avg_minutes"] = "load-avg-minutes"

                self.memory_stats = CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats()
                self.memory_stats.parent = self
                self._children_name_map["memory_stats"] = "memory-stats"

                self.per_core_stats = CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats()
                self.per_core_stats.parent = self
                self._children_name_map["per_core_stats"] = "per-core-stats"
                self._segment_path = lambda: "control-process" + "[fru='" + str(self.fru) + "']" + "[slotnum='" + str(self.slotnum) + "']" + "[baynum='" + str(self.baynum) + "']" + "[chassisnum='" + str(self.chassisnum) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-platform-software-oper:cisco-platform-software/control-processes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess, ['fru', 'slotnum', 'baynum', 'chassisnum', 'control_process_status', 'updated'], name, value)


            class LoadAverageStats(Entity):
                """
                Load average statictics
                
                .. attribute:: load_average_status
                
                	Load average status
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'platform-sw-ios-xe-oper'
                _revision = '2018-03-09'

                def __init__(self):
                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAverageStats, self).__init__()

                    self.yang_name = "load-average-stats"
                    self.yang_parent_name = "control-process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('load_average_status', (YLeaf(YType.str, 'load-average-status'), ['str'])),
                    ])
                    self.load_average_status = None
                    self._segment_path = lambda: "load-average-stats"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAverageStats, ['load_average_status'], name, value)



            class LoadAvgMinutes(Entity):
                """
                Load average statistics calculated over a period of time
                
                .. attribute:: load_avg_minute
                
                	List of Load averages based on a time frame
                	**type**\: list of  		 :py:class:`LoadAvgMinute <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute>`
                
                	**config**\: False
                
                

                """

                _prefix = 'platform-sw-ios-xe-oper'
                _revision = '2018-03-09'

                def __init__(self):
                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes, self).__init__()

                    self.yang_name = "load-avg-minutes"
                    self.yang_parent_name = "control-process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("load-avg-minute", ("load_avg_minute", CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute))])
                    self._leafs = OrderedDict()

                    self.load_avg_minute = YList(self)
                    self._segment_path = lambda: "load-avg-minutes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes, [], name, value)


                class LoadAvgMinute(Entity):
                    """
                    List of Load averages based on a time frame
                    
                    .. attribute:: number  (key)
                    
                    	The number of minutes the average was calculated on
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: average
                    
                    	Calculated average
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    .. attribute:: status
                    
                    	Load average statistics minute status
                    	**type**\:  :py:class:`Status <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'platform-sw-ios-xe-oper'
                    _revision = '2018-03-09'

                    def __init__(self):
                        super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute, self).__init__()

                        self.yang_name = "load-avg-minute"
                        self.yang_parent_name = "load-avg-minutes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['number']
                        self._child_classes = OrderedDict([("status", ("status", CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status))])
                        self._leafs = OrderedDict([
                            ('number', (YLeaf(YType.uint64, 'number'), ['int'])),
                            ('average', (YLeaf(YType.str, 'average'), ['Decimal64'])),
                        ])
                        self.number = None
                        self.average = None

                        self.status = CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status()
                        self.status.parent = self
                        self._children_name_map["status"] = "status"
                        self._segment_path = lambda: "load-avg-minute" + "[number='" + str(self.number) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute, ['number', 'average'], name, value)


                    class Status(Entity):
                        """
                        Load average statistics minute status
                        
                        .. attribute:: condition
                        
                        	Load average condition
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: threshold_status
                        
                        	Load average status
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: threshold_value
                        
                        	Load average threshold
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'platform-sw-ios-xe-oper'
                        _revision = '2018-03-09'

                        def __init__(self):
                            super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status, self).__init__()

                            self.yang_name = "status"
                            self.yang_parent_name = "load-avg-minute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('condition', (YLeaf(YType.str, 'condition'), ['str'])),
                                ('threshold_status', (YLeaf(YType.str, 'threshold-status'), ['str'])),
                                ('threshold_value', (YLeaf(YType.str, 'threshold-value'), ['Decimal64'])),
                            ])
                            self.condition = None
                            self.threshold_status = None
                            self.threshold_value = None
                            self._segment_path = lambda: "status"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status, ['condition', 'threshold_status', 'threshold_value'], name, value)





            class MemoryStats(Entity):
                """
                Memory statistics
                
                .. attribute:: memory_status
                
                	The status of the memory
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: total
                
                	The total amount of memory in kb
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: used_number
                
                	The amount of memory being used in kb
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: used_percent
                
                	The percentage of memory being used
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: free_number
                
                	The amount of free memory in kb
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: free_percent
                
                	The percentage of free memory
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: available_number
                
                	The amount of available memory in kb
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: available_percent
                
                	The percentage of available memory
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: committed_number
                
                	The amount of committed memory in kb
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: committed_percent
                
                	The percentage of committed memory
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: status
                
                	Memory status
                	**type**\:  :py:class:`Status <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats.Status>`
                
                	**config**\: False
                
                

                """

                _prefix = 'platform-sw-ios-xe-oper'
                _revision = '2018-03-09'

                def __init__(self):
                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats, self).__init__()

                    self.yang_name = "memory-stats"
                    self.yang_parent_name = "control-process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("status", ("status", CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats.Status))])
                    self._leafs = OrderedDict([
                        ('memory_status', (YLeaf(YType.str, 'memory-status'), ['str'])),
                        ('total', (YLeaf(YType.uint64, 'total'), ['int'])),
                        ('used_number', (YLeaf(YType.uint64, 'used-number'), ['int'])),
                        ('used_percent', (YLeaf(YType.uint64, 'used-percent'), ['int'])),
                        ('free_number', (YLeaf(YType.uint64, 'free-number'), ['int'])),
                        ('free_percent', (YLeaf(YType.uint64, 'free-percent'), ['int'])),
                        ('available_number', (YLeaf(YType.uint64, 'available-number'), ['int'])),
                        ('available_percent', (YLeaf(YType.uint64, 'available-percent'), ['int'])),
                        ('committed_number', (YLeaf(YType.uint64, 'committed-number'), ['int'])),
                        ('committed_percent', (YLeaf(YType.uint8, 'committed-percent'), ['int'])),
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
                    self._segment_path = lambda: "memory-stats"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats, ['memory_status', 'total', 'used_number', 'used_percent', 'free_number', 'free_percent', 'available_number', 'available_percent', 'committed_number', 'committed_percent'], name, value)


                class Status(Entity):
                    """
                    Memory status
                    
                    .. attribute:: warning_threshold_percent
                    
                    	Memory warning threshold value percent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: critical_threshold_percent
                    
                    	Memory critical threshold value percent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'platform-sw-ios-xe-oper'
                    _revision = '2018-03-09'

                    def __init__(self):
                        super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats.Status, self).__init__()

                        self.yang_name = "status"
                        self.yang_parent_name = "memory-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('warning_threshold_percent', (YLeaf(YType.uint32, 'warning-threshold-percent'), ['int'])),
                            ('critical_threshold_percent', (YLeaf(YType.uint32, 'critical-threshold-percent'), ['int'])),
                        ])
                        self.warning_threshold_percent = None
                        self.critical_threshold_percent = None
                        self._segment_path = lambda: "status"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats.Status, ['warning_threshold_percent', 'critical_threshold_percent'], name, value)




            class PerCoreStats(Entity):
                """
                Processor core statistics
                
                .. attribute:: per_core_stat
                
                	List of processor cores
                	**type**\: list of  		 :py:class:`PerCoreStat <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat>`
                
                	**config**\: False
                
                

                """

                _prefix = 'platform-sw-ios-xe-oper'
                _revision = '2018-03-09'

                def __init__(self):
                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats, self).__init__()

                    self.yang_name = "per-core-stats"
                    self.yang_parent_name = "control-process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("per-core-stat", ("per_core_stat", CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat))])
                    self._leafs = OrderedDict()

                    self.per_core_stat = YList(self)
                    self._segment_path = lambda: "per-core-stats"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats, [], name, value)


                class PerCoreStat(Entity):
                    """
                    List of processor cores
                    
                    .. attribute:: name  (key)
                    
                    	The identifier of the core
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: user
                    
                    	CPU utilization in user mode
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    .. attribute:: system
                    
                    	CPU utilization in system mode
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    .. attribute:: nice
                    
                    	Nice level
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    .. attribute:: idle
                    
                    	Idle percentage
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    .. attribute:: irq
                    
                    	The percentage of utilization by irq
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    .. attribute:: sirq
                    
                    	The percentage of utilization by sirq
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    .. attribute:: io_wait
                    
                    	IOWait percentage
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'platform-sw-ios-xe-oper'
                    _revision = '2018-03-09'

                    def __init__(self):
                        super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat, self).__init__()

                        self.yang_name = "per-core-stat"
                        self.yang_parent_name = "per-core-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.uint32, 'name'), ['int'])),
                            ('user', (YLeaf(YType.str, 'user'), ['Decimal64'])),
                            ('system', (YLeaf(YType.str, 'system'), ['Decimal64'])),
                            ('nice', (YLeaf(YType.str, 'nice'), ['Decimal64'])),
                            ('idle', (YLeaf(YType.str, 'idle'), ['Decimal64'])),
                            ('irq', (YLeaf(YType.str, 'irq'), ['Decimal64'])),
                            ('sirq', (YLeaf(YType.str, 'sirq'), ['Decimal64'])),
                            ('io_wait', (YLeaf(YType.str, 'io-wait'), ['Decimal64'])),
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
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat, ['name', 'user', 'system', 'nice', 'idle', 'irq', 'sirq', 'io_wait'], name, value)






    class QFilesystem(Entity):
        """
        Information about the filesystem
        
        .. attribute:: fru  (key)
        
        	Field replaceable unit
        	**type**\:  :py:class:`BFru <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.BFru>`
        
        	**config**\: False
        
        .. attribute:: slotnum  (key)
        
        	Slot number
        	**type**\: int
        
        	**range:** \-32768..32767
        
        	**config**\: False
        
        .. attribute:: baynum  (key)
        
        	Bay number
        	**type**\: int
        
        	**range:** \-32768..32767
        
        	**config**\: False
        
        .. attribute:: chassisnum  (key)
        
        	Chassis number
        	**type**\: int
        
        	**range:** \-32768..32767
        
        	**config**\: False
        
        .. attribute:: partitions
        
        	Information about partitions
        	**type**\: list of  		 :py:class:`Partitions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.QFilesystem.Partitions>`
        
        	**config**\: False
        
        .. attribute:: core_files
        
        	Information about core files
        	**type**\: list of  		 :py:class:`CoreFiles <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.QFilesystem.CoreFiles>`
        
        	**config**\: False
        
        

        """

        _prefix = 'platform-sw-ios-xe-oper'
        _revision = '2018-03-09'

        def __init__(self):
            super(CiscoPlatformSoftware.QFilesystem, self).__init__()

            self.yang_name = "q-filesystem"
            self.yang_parent_name = "cisco-platform-software"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['fru','slotnum','baynum','chassisnum']
            self._child_classes = OrderedDict([("partitions", ("partitions", CiscoPlatformSoftware.QFilesystem.Partitions)), ("core-files", ("core_files", CiscoPlatformSoftware.QFilesystem.CoreFiles))])
            self._leafs = OrderedDict([
                ('fru', (YLeaf(YType.enumeration, 'fru'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper', 'BFru', '')])),
                ('slotnum', (YLeaf(YType.int16, 'slotnum'), ['int'])),
                ('baynum', (YLeaf(YType.int16, 'baynum'), ['int'])),
                ('chassisnum', (YLeaf(YType.int16, 'chassisnum'), ['int'])),
            ])
            self.fru = None
            self.slotnum = None
            self.baynum = None
            self.chassisnum = None

            self.partitions = YList(self)
            self.core_files = YList(self)
            self._segment_path = lambda: "q-filesystem" + "[fru='" + str(self.fru) + "']" + "[slotnum='" + str(self.slotnum) + "']" + "[baynum='" + str(self.baynum) + "']" + "[chassisnum='" + str(self.chassisnum) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-platform-software-oper:cisco-platform-software/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CiscoPlatformSoftware.QFilesystem, ['fru', 'slotnum', 'baynum', 'chassisnum'], name, value)


        class Partitions(Entity):
            """
            Information about partitions
            
            .. attribute:: name  (key)
            
            	The name of the partition
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: total_size
            
            	Total size of the partition in Kilobytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: used_size
            
            	Size used in Kilobytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            

            """

            _prefix = 'platform-sw-ios-xe-oper'
            _revision = '2018-03-09'

            def __init__(self):
                super(CiscoPlatformSoftware.QFilesystem.Partitions, self).__init__()

                self.yang_name = "partitions"
                self.yang_parent_name = "q-filesystem"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('total_size', (YLeaf(YType.uint64, 'total-size'), ['int'])),
                    ('used_size', (YLeaf(YType.uint64, 'used-size'), ['int'])),
                ])
                self.name = None
                self.total_size = None
                self.used_size = None
                self._segment_path = lambda: "partitions" + "[name='" + str(self.name) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CiscoPlatformSoftware.QFilesystem.Partitions, ['name', 'total_size', 'used_size'], name, value)



        class CoreFiles(Entity):
            """
            Information about core files
            
            .. attribute:: filename  (key)
            
            	The core filename
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: time
            
            	The date of generation
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            	**config**\: False
            
            

            """

            _prefix = 'platform-sw-ios-xe-oper'
            _revision = '2018-03-09'

            def __init__(self):
                super(CiscoPlatformSoftware.QFilesystem.CoreFiles, self).__init__()

                self.yang_name = "core-files"
                self.yang_parent_name = "q-filesystem"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['filename']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('filename', (YLeaf(YType.str, 'filename'), ['str'])),
                    ('time', (YLeaf(YType.str, 'time'), ['str'])),
                ])
                self.filename = None
                self.time = None
                self._segment_path = lambda: "core-files" + "[filename='" + str(self.filename) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CiscoPlatformSoftware.QFilesystem.CoreFiles, ['filename', 'time'], name, value)



    def clone_ptr(self):
        self._top_entity = CiscoPlatformSoftware()
        return self._top_entity



