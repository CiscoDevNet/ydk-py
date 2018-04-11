""" Cisco_IOS_XR_sysadmin_sdm_diag 


"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Diagnostic(Entity):
    """
    
    
    .. attribute:: monitor
    
    	
    	**type**\:  :py:class:`Monitor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Monitor>`
    
    .. attribute:: schedule
    
    	
    	**type**\:  :py:class:`Schedule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Schedule>`
    
    .. attribute:: status
    
    	
    	**type**\:  :py:class:`Status <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Status>`
    
    .. attribute:: diag_start
    
    	
    	**type**\:  :py:class:`DiagStart <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.DiagStart>`
    
    .. attribute:: diag_stop
    
    	
    	**type**\:  :py:class:`DiagStop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.DiagStop>`
    
    .. attribute:: content
    
    	
    	**type**\:  :py:class:`Content <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Content>`
    
    .. attribute:: result
    
    	
    	**type**\:  :py:class:`Result <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Result>`
    
    

    """

    _prefix = 'diagnostics_actions'
    _revision = '2017-03-21'

    def __init__(self):
        super(Diagnostic, self).__init__()
        self._top_entity = None

        self.yang_name = "diagnostic"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-sdm-diag"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("monitor", ("monitor", Diagnostic.Monitor)), ("schedule", ("schedule", Diagnostic.Schedule)), ("status", ("status", Diagnostic.Status)), ("diag_start", ("diag_start", Diagnostic.DiagStart)), ("diag_stop", ("diag_stop", Diagnostic.DiagStop)), ("content", ("content", Diagnostic.Content)), ("result", ("result", Diagnostic.Result))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.monitor = Diagnostic.Monitor()
        self.monitor.parent = self
        self._children_name_map["monitor"] = "monitor"
        self._children_yang_names.add("monitor")

        self.schedule = Diagnostic.Schedule()
        self.schedule.parent = self
        self._children_name_map["schedule"] = "schedule"
        self._children_yang_names.add("schedule")

        self.status = Diagnostic.Status()
        self.status.parent = self
        self._children_name_map["status"] = "status"
        self._children_yang_names.add("status")

        self.diag_start = Diagnostic.DiagStart()
        self.diag_start.parent = self
        self._children_name_map["diag_start"] = "diag_start"
        self._children_yang_names.add("diag_start")

        self.diag_stop = Diagnostic.DiagStop()
        self.diag_stop.parent = self
        self._children_name_map["diag_stop"] = "diag_stop"
        self._children_yang_names.add("diag_stop")

        self.content = Diagnostic.Content()
        self.content.parent = self
        self._children_name_map["content"] = "content"
        self._children_yang_names.add("content")

        self.result = Diagnostic.Result()
        self.result.parent = self
        self._children_name_map["result"] = "result"
        self._children_yang_names.add("result")
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic"


    class Monitor(Entity):
        """
        
        
        .. attribute:: rejected
        
        	
        	**type**\:  :py:class:`Rejected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Monitor.Rejected>`
        
        .. attribute:: interval
        
        	
        	**type**\:  :py:class:`Interval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Monitor.Interval>`
        
        .. attribute:: threshold
        
        	
        	**type**\:  :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Monitor.Threshold>`
        
        

        """

        _prefix = 'diagnostics_actions'
        _revision = '2017-03-21'

        def __init__(self):
            super(Diagnostic.Monitor, self).__init__()

            self.yang_name = "monitor"
            self.yang_parent_name = "diagnostic"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("rejected", ("rejected", Diagnostic.Monitor.Rejected)), ("interval", ("interval", Diagnostic.Monitor.Interval)), ("threshold", ("threshold", Diagnostic.Monitor.Threshold))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.rejected = Diagnostic.Monitor.Rejected()
            self.rejected.parent = self
            self._children_name_map["rejected"] = "rejected"
            self._children_yang_names.add("rejected")

            self.interval = Diagnostic.Monitor.Interval()
            self.interval.parent = self
            self._children_name_map["interval"] = "interval"
            self._children_yang_names.add("interval")

            self.threshold = Diagnostic.Monitor.Threshold()
            self.threshold.parent = self
            self._children_name_map["threshold"] = "threshold"
            self._children_yang_names.add("threshold")
            self._segment_path = lambda: "monitor"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/%s" % self._segment_path()


        class Rejected(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Monitor.Rejected.Location>`
            
            

            """

            _prefix = 'diagnostics_actions'
            _revision = '2017-03-21'

            def __init__(self):
                super(Diagnostic.Monitor.Rejected, self).__init__()

                self.yang_name = "rejected"
                self.yang_parent_name = "monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("location", ("location", Diagnostic.Monitor.Rejected.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "rejected"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/monitor/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Diagnostic.Monitor.Rejected, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: loc  (key)
                
                	
                	**type**\: str
                
                .. attribute:: test
                
                	
                	**type**\: list of  		 :py:class:`Test <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Monitor.Rejected.Location.Test>`
                
                

                """

                _prefix = 'diagnostics_actions'
                _revision = '2017-03-21'

                def __init__(self):
                    super(Diagnostic.Monitor.Rejected.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "rejected"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['loc']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("test", ("test", Diagnostic.Monitor.Rejected.Location.Test))])
                    self._leafs = OrderedDict([
                        ('loc', YLeaf(YType.str, 'loc')),
                    ])
                    self.loc = None

                    self.test = YList(self)
                    self._segment_path = lambda: "location" + "[loc='" + str(self.loc) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/monitor/rejected/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Diagnostic.Monitor.Rejected.Location, ['loc'], name, value)


                class Test(Entity):
                    """
                    
                    
                    .. attribute:: test_id  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: run  (key)
                    
                    	
                    	**type**\:  :py:class:`Run <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Monitor.Rejected.Location.Test.Run>`
                    
                    

                    """

                    _prefix = 'diagnostics_actions'
                    _revision = '2017-03-21'

                    def __init__(self):
                        super(Diagnostic.Monitor.Rejected.Location.Test, self).__init__()

                        self.yang_name = "test"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['test_id','run']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('test_id', YLeaf(YType.str, 'test_id')),
                            ('run', YLeaf(YType.enumeration, 'run')),
                        ])
                        self.test_id = None
                        self.run = None
                        self._segment_path = lambda: "test" + "[test_id='" + str(self.test_id) + "']" + "[run='" + str(self.run) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diagnostic.Monitor.Rejected.Location.Test, ['test_id', 'run'], name, value)

                    class Run(Enum):
                        """
                        Run (Enum Class)

                        .. data:: disable = 1

                        """

                        disable = Enum.YLeaf(1, "disable")



        class Interval(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Monitor.Interval.Location>`
            
            

            """

            _prefix = 'diagnostics_actions'
            _revision = '2017-03-21'

            def __init__(self):
                super(Diagnostic.Monitor.Interval, self).__init__()

                self.yang_name = "interval"
                self.yang_parent_name = "monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("location", ("location", Diagnostic.Monitor.Interval.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "interval"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/monitor/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Diagnostic.Monitor.Interval, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: loc  (key)
                
                	
                	**type**\: str
                
                .. attribute:: test
                
                	
                	**type**\: list of  		 :py:class:`Test <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Monitor.Interval.Location.Test>`
                
                

                """

                _prefix = 'diagnostics_actions'
                _revision = '2017-03-21'

                def __init__(self):
                    super(Diagnostic.Monitor.Interval.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "interval"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['loc']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("test", ("test", Diagnostic.Monitor.Interval.Location.Test))])
                    self._leafs = OrderedDict([
                        ('loc', YLeaf(YType.str, 'loc')),
                    ])
                    self.loc = None

                    self.test = YList(self)
                    self._segment_path = lambda: "location" + "[loc='" + str(self.loc) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/monitor/interval/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Diagnostic.Monitor.Interval.Location, ['loc'], name, value)


                class Test(Entity):
                    """
                    
                    
                    .. attribute:: test_id  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: days
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..20
                    
                    	**mandatory**\: True
                    
                    .. attribute:: time
                    
                    	
                    	**type**\: str
                    
                    	**pattern:** ([01]?[0\-9]\|2[0\-3])\:[0\-5][0\-9]\:[0\-5][0\-9]
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'diagnostics_actions'
                    _revision = '2017-03-21'

                    def __init__(self):
                        super(Diagnostic.Monitor.Interval.Location.Test, self).__init__()

                        self.yang_name = "test"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['test_id']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('test_id', YLeaf(YType.str, 'test_id')),
                            ('days', YLeaf(YType.int32, 'days')),
                            ('time', YLeaf(YType.str, 'time')),
                        ])
                        self.test_id = None
                        self.days = None
                        self.time = None
                        self._segment_path = lambda: "test" + "[test_id='" + str(self.test_id) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diagnostic.Monitor.Interval.Location.Test, ['test_id', 'days', 'time'], name, value)


        class Threshold(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Monitor.Threshold.Location>`
            
            

            """

            _prefix = 'diagnostics_actions'
            _revision = '2017-03-21'

            def __init__(self):
                super(Diagnostic.Monitor.Threshold, self).__init__()

                self.yang_name = "threshold"
                self.yang_parent_name = "monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("location", ("location", Diagnostic.Monitor.Threshold.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "threshold"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/monitor/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Diagnostic.Monitor.Threshold, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: loc  (key)
                
                	
                	**type**\: str
                
                .. attribute:: test
                
                	
                	**type**\: list of  		 :py:class:`Test <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Monitor.Threshold.Location.Test>`
                
                

                """

                _prefix = 'diagnostics_actions'
                _revision = '2017-03-21'

                def __init__(self):
                    super(Diagnostic.Monitor.Threshold.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['loc']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("test", ("test", Diagnostic.Monitor.Threshold.Location.Test))])
                    self._leafs = OrderedDict([
                        ('loc', YLeaf(YType.str, 'loc')),
                    ])
                    self.loc = None

                    self.test = YList(self)
                    self._segment_path = lambda: "location" + "[loc='" + str(self.loc) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/monitor/threshold/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Diagnostic.Monitor.Threshold.Location, ['loc'], name, value)


                class Test(Entity):
                    """
                    
                    
                    .. attribute:: test_id  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: failure_count
                    
                    	
                    	**type**\: int
                    
                    	**range:** 1..99
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'diagnostics_actions'
                    _revision = '2017-03-21'

                    def __init__(self):
                        super(Diagnostic.Monitor.Threshold.Location.Test, self).__init__()

                        self.yang_name = "test"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['test_id']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('test_id', YLeaf(YType.str, 'test_id')),
                            ('failure_count', YLeaf(YType.int32, 'failure-count')),
                        ])
                        self.test_id = None
                        self.failure_count = None
                        self._segment_path = lambda: "test" + "[test_id='" + str(self.test_id) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diagnostic.Monitor.Threshold.Location.Test, ['test_id', 'failure_count'], name, value)


    class Schedule(Entity):
        """
        
        
        .. attribute:: start
        
        	
        	**type**\:  :py:class:`Start <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Schedule.Start>`
        
        

        """

        _prefix = 'diagnostics_actions'
        _revision = '2017-03-21'

        def __init__(self):
            super(Diagnostic.Schedule, self).__init__()

            self.yang_name = "schedule"
            self.yang_parent_name = "diagnostic"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("start", ("start", Diagnostic.Schedule.Start))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.start = Diagnostic.Schedule.Start()
            self.start.parent = self
            self._children_name_map["start"] = "start"
            self._children_yang_names.add("start")
            self._segment_path = lambda: "schedule"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/%s" % self._segment_path()


        class Start(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Schedule.Start.Location>`
            
            

            """

            _prefix = 'diagnostics_actions'
            _revision = '2017-03-21'

            def __init__(self):
                super(Diagnostic.Schedule.Start, self).__init__()

                self.yang_name = "start"
                self.yang_parent_name = "schedule"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("location", ("location", Diagnostic.Schedule.Start.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "start"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/schedule/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Diagnostic.Schedule.Start, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: loc  (key)
                
                	
                	**type**\: str
                
                .. attribute:: test
                
                	
                	**type**\: list of  		 :py:class:`Test <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Schedule.Start.Location.Test>`
                
                

                """

                _prefix = 'diagnostics_actions'
                _revision = '2017-03-21'

                def __init__(self):
                    super(Diagnostic.Schedule.Start.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "start"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['loc']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("test", ("test", Diagnostic.Schedule.Start.Location.Test))])
                    self._leafs = OrderedDict([
                        ('loc', YLeaf(YType.str, 'loc')),
                    ])
                    self.loc = None

                    self.test = YList(self)
                    self._segment_path = lambda: "location" + "[loc='" + str(self.loc) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/schedule/start/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Diagnostic.Schedule.Start.Location, ['loc'], name, value)


                class Test(Entity):
                    """
                    
                    
                    .. attribute:: test_id  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: daily
                    
                    	
                    	**type**\: list of  		 :py:class:`Daily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Schedule.Start.Location.Test.Daily>`
                    
                    .. attribute:: on
                    
                    	
                    	**type**\: list of  		 :py:class:`On <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Schedule.Start.Location.Test.On>`
                    
                    .. attribute:: weekly
                    
                    	
                    	**type**\: list of  		 :py:class:`Weekly <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Schedule.Start.Location.Test.Weekly>`
                    
                    

                    """

                    _prefix = 'diagnostics_actions'
                    _revision = '2017-03-21'

                    def __init__(self):
                        super(Diagnostic.Schedule.Start.Location.Test, self).__init__()

                        self.yang_name = "test"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['test_id']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("daily", ("daily", Diagnostic.Schedule.Start.Location.Test.Daily)), ("on", ("on", Diagnostic.Schedule.Start.Location.Test.On)), ("weekly", ("weekly", Diagnostic.Schedule.Start.Location.Test.Weekly))])
                        self._leafs = OrderedDict([
                            ('test_id', YLeaf(YType.str, 'test_id')),
                        ])
                        self.test_id = None

                        self.daily = YList(self)
                        self.on = YList(self)
                        self.weekly = YList(self)
                        self._segment_path = lambda: "test" + "[test_id='" + str(self.test_id) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diagnostic.Schedule.Start.Location.Test, ['test_id'], name, value)


                    class Daily(Entity):
                        """
                        
                        
                        .. attribute:: hour_min  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ([01]?[0\-9]\|2[0\-3])\:[0\-5][0\-9]
                        
                        

                        """

                        _prefix = 'diagnostics_actions'
                        _revision = '2017-03-21'

                        def __init__(self):
                            super(Diagnostic.Schedule.Start.Location.Test.Daily, self).__init__()

                            self.yang_name = "daily"
                            self.yang_parent_name = "test"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['hour_min']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('hour_min', YLeaf(YType.str, 'hour_min')),
                            ])
                            self.hour_min = None
                            self._segment_path = lambda: "daily" + "[hour_min='" + str(self.hour_min) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Diagnostic.Schedule.Start.Location.Test.Daily, ['hour_min'], name, value)


                    class On(Entity):
                        """
                        
                        
                        .. attribute:: month  (key)
                        
                        	
                        	**type**\:  :py:class:`Month <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Schedule.Start.Location.Test.On.Month>`
                        
                        .. attribute:: day_of_month  (key)
                        
                        	
                        	**type**\: int
                        
                        	**range:** 1..31
                        
                        .. attribute:: year  (key)
                        
                        	
                        	**type**\: int
                        
                        	**range:** 2013..2099
                        
                        .. attribute:: hour_min  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ([01]?[0\-9]\|2[0\-3])\:[0\-5][0\-9]
                        
                        

                        """

                        _prefix = 'diagnostics_actions'
                        _revision = '2017-03-21'

                        def __init__(self):
                            super(Diagnostic.Schedule.Start.Location.Test.On, self).__init__()

                            self.yang_name = "on"
                            self.yang_parent_name = "test"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['month','day_of_month','year','hour_min']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('month', YLeaf(YType.enumeration, 'month')),
                                ('day_of_month', YLeaf(YType.int32, 'day_of_month')),
                                ('year', YLeaf(YType.int32, 'year')),
                                ('hour_min', YLeaf(YType.str, 'hour_min')),
                            ])
                            self.month = None
                            self.day_of_month = None
                            self.year = None
                            self.hour_min = None
                            self._segment_path = lambda: "on" + "[month='" + str(self.month) + "']" + "[day_of_month='" + str(self.day_of_month) + "']" + "[year='" + str(self.year) + "']" + "[hour_min='" + str(self.hour_min) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Diagnostic.Schedule.Start.Location.Test.On, ['month', 'day_of_month', 'year', 'hour_min'], name, value)

                        class Month(Enum):
                            """
                            Month (Enum Class)

                            .. data:: JAN = 0

                            .. data:: FEB = 1

                            .. data:: MAR = 2

                            .. data:: APR = 3

                            .. data:: MAY = 4

                            .. data:: JUN = 5

                            .. data:: JUL = 6

                            .. data:: AUG = 7

                            .. data:: SEP = 8

                            .. data:: OCT = 9

                            .. data:: NOV = 10

                            .. data:: DEC = 11

                            """

                            JAN = Enum.YLeaf(0, "JAN")

                            FEB = Enum.YLeaf(1, "FEB")

                            MAR = Enum.YLeaf(2, "MAR")

                            APR = Enum.YLeaf(3, "APR")

                            MAY = Enum.YLeaf(4, "MAY")

                            JUN = Enum.YLeaf(5, "JUN")

                            JUL = Enum.YLeaf(6, "JUL")

                            AUG = Enum.YLeaf(7, "AUG")

                            SEP = Enum.YLeaf(8, "SEP")

                            OCT = Enum.YLeaf(9, "OCT")

                            NOV = Enum.YLeaf(10, "NOV")

                            DEC = Enum.YLeaf(11, "DEC")



                    class Weekly(Entity):
                        """
                        
                        
                        .. attribute:: daysofweek  (key)
                        
                        	
                        	**type**\:  :py:class:`Daysofweek <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Schedule.Start.Location.Test.Weekly.Daysofweek>`
                        
                        .. attribute:: hour_min  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ([01]?[0\-9]\|2[0\-3])\:[0\-5][0\-9]
                        
                        

                        """

                        _prefix = 'diagnostics_actions'
                        _revision = '2017-03-21'

                        def __init__(self):
                            super(Diagnostic.Schedule.Start.Location.Test.Weekly, self).__init__()

                            self.yang_name = "weekly"
                            self.yang_parent_name = "test"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['daysofweek','hour_min']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('daysofweek', YLeaf(YType.enumeration, 'daysofweek')),
                                ('hour_min', YLeaf(YType.str, 'hour_min')),
                            ])
                            self.daysofweek = None
                            self.hour_min = None
                            self._segment_path = lambda: "weekly" + "[daysofweek='" + str(self.daysofweek) + "']" + "[hour_min='" + str(self.hour_min) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Diagnostic.Schedule.Start.Location.Test.Weekly, ['daysofweek', 'hour_min'], name, value)

                        class Daysofweek(Enum):
                            """
                            Daysofweek (Enum Class)

                            .. data:: SUN = 0

                            .. data:: MON = 1

                            .. data:: TUE = 2

                            .. data:: WED = 3

                            .. data:: THR = 4

                            .. data:: FRI = 5

                            .. data:: SAT = 6

                            """

                            SUN = Enum.YLeaf(0, "SUN")

                            MON = Enum.YLeaf(1, "MON")

                            TUE = Enum.YLeaf(2, "TUE")

                            WED = Enum.YLeaf(3, "WED")

                            THR = Enum.YLeaf(4, "THR")

                            FRI = Enum.YLeaf(5, "FRI")

                            SAT = Enum.YLeaf(6, "SAT")



    class Status(Entity):
        """
        
        
        .. attribute:: location_index
        
        	
        	**type**\: list of  		 :py:class:`LocationIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Status.LocationIndex>`
        
        

        """

        _prefix = 'diagnostics_actions'
        _revision = '2017-03-21'

        def __init__(self):
            super(Diagnostic.Status, self).__init__()

            self.yang_name = "status"
            self.yang_parent_name = "diagnostic"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("location_index", ("location_index", Diagnostic.Status.LocationIndex))])
            self._leafs = OrderedDict()

            self.location_index = YList(self)
            self._segment_path = lambda: "status"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Diagnostic.Status, [], name, value)


        class LocationIndex(Entity):
            """
            
            
            .. attribute:: data_idx  (key)
            
            	
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: description
            
            	
            	**type**\: str
            
            .. attribute:: curr_running_tst_runby
            
            	
            	**type**\: str
            
            

            """

            _prefix = 'diagnostics_actions'
            _revision = '2017-03-21'

            def __init__(self):
                super(Diagnostic.Status.LocationIndex, self).__init__()

                self.yang_name = "location_index"
                self.yang_parent_name = "status"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['data_idx']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('data_idx', YLeaf(YType.int32, 'data_idx')),
                    ('description', YLeaf(YType.str, 'description')),
                    ('curr_running_tst_runby', YLeaf(YType.str, 'curr_running_tst_runby')),
                ])
                self.data_idx = None
                self.description = None
                self.curr_running_tst_runby = None
                self._segment_path = lambda: "location_index" + "[data_idx='" + str(self.data_idx) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/status/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Diagnostic.Status.LocationIndex, ['data_idx', 'description', 'curr_running_tst_runby'], name, value)


    class DiagStart(Entity):
        """
        
        
        .. attribute:: location
        
        	
        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.DiagStart.Location>`
        
        

        """

        _prefix = 'diagnostics_actions'
        _revision = '2017-03-21'

        def __init__(self):
            super(Diagnostic.DiagStart, self).__init__()

            self.yang_name = "diag_start"
            self.yang_parent_name = "diagnostic"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("location", ("location", Diagnostic.DiagStart.Location))])
            self._leafs = OrderedDict()

            self.location = YList(self)
            self._segment_path = lambda: "diag_start"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Diagnostic.DiagStart, [], name, value)


        class Location(Entity):
            """
            
            
            .. attribute:: loc  (key)
            
            	
            	**type**\: str
            
            .. attribute:: description
            
            	
            	**type**\: str
            
            	**default value**\: port.
            
            .. attribute:: test
            
            	
            	**type**\: list of  		 :py:class:`Test <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.DiagStart.Location.Test>`
            
            

            """

            _prefix = 'diagnostics_actions'
            _revision = '2017-03-21'

            def __init__(self):
                super(Diagnostic.DiagStart.Location, self).__init__()

                self.yang_name = "location"
                self.yang_parent_name = "diag_start"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['loc']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("test", ("test", Diagnostic.DiagStart.Location.Test))])
                self._leafs = OrderedDict([
                    ('loc', YLeaf(YType.str, 'loc')),
                    ('description', YLeaf(YType.str, 'description')),
                ])
                self.loc = None
                self.description = None

                self.test = YList(self)
                self._segment_path = lambda: "location" + "[loc='" + str(self.loc) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/diag_start/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Diagnostic.DiagStart.Location, ['loc', 'description'], name, value)


            class Test(Entity):
                """
                
                
                .. attribute:: test_type  (key)
                
                	
                	**type**\: str
                
                .. attribute:: description
                
                	
                	**type**\: str
                
                	**default value**\: Test.
                
                

                """

                _prefix = 'diagnostics_actions'
                _revision = '2017-03-21'

                def __init__(self):
                    super(Diagnostic.DiagStart.Location.Test, self).__init__()

                    self.yang_name = "test"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['test_type']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('test_type', YLeaf(YType.str, 'test_type')),
                        ('description', YLeaf(YType.str, 'description')),
                    ])
                    self.test_type = None
                    self.description = None
                    self._segment_path = lambda: "test" + "[test_type='" + str(self.test_type) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Diagnostic.DiagStart.Location.Test, ['test_type', 'description'], name, value)


    class DiagStop(Entity):
        """
        
        
        .. attribute:: location
        
        	
        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.DiagStop.Location>`
        
        

        """

        _prefix = 'diagnostics_actions'
        _revision = '2017-03-21'

        def __init__(self):
            super(Diagnostic.DiagStop, self).__init__()

            self.yang_name = "diag_stop"
            self.yang_parent_name = "diagnostic"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("location", ("location", Diagnostic.DiagStop.Location))])
            self._leafs = OrderedDict()

            self.location = YList(self)
            self._segment_path = lambda: "diag_stop"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Diagnostic.DiagStop, [], name, value)


        class Location(Entity):
            """
            
            
            .. attribute:: loc  (key)
            
            	
            	**type**\: str
            
            .. attribute:: description
            
            	
            	**type**\: str
            
            	**default value**\: port.
            
            .. attribute:: test
            
            	
            	**type**\: list of  		 :py:class:`Test <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.DiagStop.Location.Test>`
            
            

            """

            _prefix = 'diagnostics_actions'
            _revision = '2017-03-21'

            def __init__(self):
                super(Diagnostic.DiagStop.Location, self).__init__()

                self.yang_name = "location"
                self.yang_parent_name = "diag_stop"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['loc']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("test", ("test", Diagnostic.DiagStop.Location.Test))])
                self._leafs = OrderedDict([
                    ('loc', YLeaf(YType.str, 'loc')),
                    ('description', YLeaf(YType.str, 'description')),
                ])
                self.loc = None
                self.description = None

                self.test = YList(self)
                self._segment_path = lambda: "location" + "[loc='" + str(self.loc) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/diag_stop/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Diagnostic.DiagStop.Location, ['loc', 'description'], name, value)


            class Test(Entity):
                """
                
                
                .. attribute:: test_type  (key)
                
                	
                	**type**\: str
                
                .. attribute:: description
                
                	
                	**type**\: str
                
                	**default value**\: Test.
                
                

                """

                _prefix = 'diagnostics_actions'
                _revision = '2017-03-21'

                def __init__(self):
                    super(Diagnostic.DiagStop.Location.Test, self).__init__()

                    self.yang_name = "test"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['test_type']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('test_type', YLeaf(YType.str, 'test_type')),
                        ('description', YLeaf(YType.str, 'description')),
                    ])
                    self.test_type = None
                    self.description = None
                    self._segment_path = lambda: "test" + "[test_type='" + str(self.test_type) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Diagnostic.DiagStop.Location.Test, ['test_type', 'description'], name, value)


    class Content(Entity):
        """
        
        
        .. attribute:: location
        
        	
        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Content.Location>`
        
        

        """

        _prefix = 'diagnostics_actions'
        _revision = '2017-03-21'

        def __init__(self):
            super(Diagnostic.Content, self).__init__()

            self.yang_name = "content"
            self.yang_parent_name = "diagnostic"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("location", ("location", Diagnostic.Content.Location))])
            self._leafs = OrderedDict()

            self.location = YList(self)
            self._segment_path = lambda: "content"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Diagnostic.Content, [], name, value)


        class Location(Entity):
            """
            
            
            .. attribute:: loc  (key)
            
            	
            	**type**\: str
            
            .. attribute:: description
            
            	
            	**type**\: str
            
            	**default value**\: port.
            
            .. attribute:: data_list
            
            	
            	**type**\: list of  		 :py:class:`DataList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Content.Location.DataList>`
            
            

            """

            _prefix = 'diagnostics_actions'
            _revision = '2017-03-21'

            def __init__(self):
                super(Diagnostic.Content.Location, self).__init__()

                self.yang_name = "location"
                self.yang_parent_name = "content"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['loc']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("data_list", ("data_list", Diagnostic.Content.Location.DataList))])
                self._leafs = OrderedDict([
                    ('loc', YLeaf(YType.str, 'loc')),
                    ('description', YLeaf(YType.str, 'description')),
                ])
                self.loc = None
                self.description = None

                self.data_list = YList(self)
                self._segment_path = lambda: "location" + "[loc='" + str(self.loc) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/content/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Diagnostic.Content.Location, ['loc', 'description'], name, value)


            class DataList(Entity):
                """
                
                
                .. attribute:: data_idx  (key)
                
                	
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: id
                
                	To display the test information
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: test_name
                
                	
                	**type**\: str
                
                .. attribute:: attribute
                
                	
                	**type**\: str
                
                .. attribute:: timeinfo
                
                	
                	**type**\: str
                
                .. attribute:: threshold
                
                	
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'diagnostics_actions'
                _revision = '2017-03-21'

                def __init__(self):
                    super(Diagnostic.Content.Location.DataList, self).__init__()

                    self.yang_name = "data_list"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['data_idx']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('data_idx', YLeaf(YType.int32, 'data_idx')),
                        ('id', YLeaf(YType.int32, 'id')),
                        ('test_name', YLeaf(YType.str, 'test_name')),
                        ('attribute', YLeaf(YType.str, 'attribute')),
                        ('timeinfo', YLeaf(YType.str, 'timeinfo')),
                        ('threshold', YLeaf(YType.int32, 'threshold')),
                    ])
                    self.data_idx = None
                    self.id = None
                    self.test_name = None
                    self.attribute = None
                    self.timeinfo = None
                    self.threshold = None
                    self._segment_path = lambda: "data_list" + "[data_idx='" + str(self.data_idx) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Diagnostic.Content.Location.DataList, ['data_idx', 'id', 'test_name', 'attribute', 'timeinfo', 'threshold'], name, value)


    class Result(Entity):
        """
        
        
        .. attribute:: location
        
        	
        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Result.Location>`
        
        

        """

        _prefix = 'diagnostics_actions'
        _revision = '2017-03-21'

        def __init__(self):
            super(Diagnostic.Result, self).__init__()

            self.yang_name = "result"
            self.yang_parent_name = "diagnostic"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("location", ("location", Diagnostic.Result.Location))])
            self._leafs = OrderedDict()

            self.location = YList(self)
            self._segment_path = lambda: "result"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Diagnostic.Result, [], name, value)


        class Location(Entity):
            """
            
            
            .. attribute:: loc  (key)
            
            	
            	**type**\: str
            
            .. attribute:: description
            
            	
            	**type**\: str
            
            	**default value**\: port.
            
            .. attribute:: test
            
            	
            	**type**\: list of  		 :py:class:`Test <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Result.Location.Test>`
            
            

            """

            _prefix = 'diagnostics_actions'
            _revision = '2017-03-21'

            def __init__(self):
                super(Diagnostic.Result.Location, self).__init__()

                self.yang_name = "location"
                self.yang_parent_name = "result"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['loc']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("test", ("test", Diagnostic.Result.Location.Test))])
                self._leafs = OrderedDict([
                    ('loc', YLeaf(YType.str, 'loc')),
                    ('description', YLeaf(YType.str, 'description')),
                ])
                self.loc = None
                self.description = None

                self.test = YList(self)
                self._segment_path = lambda: "location" + "[loc='" + str(self.loc) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdm-diag:diagnostic/result/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Diagnostic.Result.Location, ['loc', 'description'], name, value)


            class Test(Entity):
                """
                
                
                .. attribute:: test_type  (key)
                
                	test name\|all
                	**type**\: str
                
                .. attribute:: description
                
                	
                	**type**\: str
                
                	**default value**\: port.
                
                .. attribute:: detail
                
                	
                	**type**\: list of  		 :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Result.Location.Test.Detail>`
                
                

                """

                _prefix = 'diagnostics_actions'
                _revision = '2017-03-21'

                def __init__(self):
                    super(Diagnostic.Result.Location.Test, self).__init__()

                    self.yang_name = "test"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['test_type']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("detail", ("detail", Diagnostic.Result.Location.Test.Detail))])
                    self._leafs = OrderedDict([
                        ('test_type', YLeaf(YType.str, 'test_type')),
                        ('description', YLeaf(YType.str, 'description')),
                    ])
                    self.test_type = None
                    self.description = None

                    self.detail = YList(self)
                    self._segment_path = lambda: "test" + "[test_type='" + str(self.test_type) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Diagnostic.Result.Location.Test, ['test_type', 'description'], name, value)


                class Detail(Entity):
                    """
                    
                    
                    .. attribute:: det  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: data_list
                    
                    	
                    	**type**\: list of  		 :py:class:`DataList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdm_diag.Diagnostic.Result.Location.Test.Detail.DataList>`
                    
                    

                    """

                    _prefix = 'diagnostics_actions'
                    _revision = '2017-03-21'

                    def __init__(self):
                        super(Diagnostic.Result.Location.Test.Detail, self).__init__()

                        self.yang_name = "detail"
                        self.yang_parent_name = "test"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['det']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("data_list", ("data_list", Diagnostic.Result.Location.Test.Detail.DataList))])
                        self._leafs = OrderedDict([
                            ('det', YLeaf(YType.str, 'det')),
                        ])
                        self.det = None

                        self.data_list = YList(self)
                        self._segment_path = lambda: "detail" + "[det='" + str(self.det) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diagnostic.Result.Location.Test.Detail, ['det'], name, value)


                    class DataList(Entity):
                        """
                        
                        
                        .. attribute:: data_idx  (key)
                        
                        	
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: detail_flag
                        
                        	
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: sl_no
                        
                        	
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: test_name
                        
                        	
                        	**type**\: str
                        
                        .. attribute:: test_result
                        
                        	
                        	**type**\: str
                        
                        .. attribute:: err_code
                        
                        	
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: err_description
                        
                        	
                        	**type**\: str
                        
                        .. attribute:: test_type
                        
                        	
                        	**type**\: str
                        
                        .. attribute:: hm_test_count
                        
                        	
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: od_test_count
                        
                        	
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: sched_test_count
                        
                        	
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: run_cnt
                        
                        	
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: lt_exe_time
                        
                        	
                        	**type**\: str
                        
                        .. attribute:: ft_fail_time
                        
                        	
                        	**type**\: str
                        
                        .. attribute:: lt_fail_time
                        
                        	
                        	**type**\: str
                        
                        .. attribute:: lt_pass_time
                        
                        	
                        	**type**\: str
                        
                        .. attribute:: total_fail_cnt
                        
                        	
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: cons_fail_cnt
                        
                        	
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: more_info
                        
                        	
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'diagnostics_actions'
                        _revision = '2017-03-21'

                        def __init__(self):
                            super(Diagnostic.Result.Location.Test.Detail.DataList, self).__init__()

                            self.yang_name = "data_list"
                            self.yang_parent_name = "detail"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['data_idx']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('data_idx', YLeaf(YType.int32, 'data_idx')),
                                ('detail_flag', YLeaf(YType.int32, 'detail_flag')),
                                ('sl_no', YLeaf(YType.int32, 'sl_no')),
                                ('test_name', YLeaf(YType.str, 'test_name')),
                                ('test_result', YLeaf(YType.str, 'test_result')),
                                ('err_code', YLeaf(YType.int32, 'err_code')),
                                ('err_description', YLeaf(YType.str, 'err_description')),
                                ('test_type', YLeaf(YType.str, 'test_type')),
                                ('hm_test_count', YLeaf(YType.int32, 'hm_test_count')),
                                ('od_test_count', YLeaf(YType.int32, 'od_test_count')),
                                ('sched_test_count', YLeaf(YType.int32, 'sched_test_count')),
                                ('run_cnt', YLeaf(YType.int32, 'run_cnt')),
                                ('lt_exe_time', YLeaf(YType.str, 'lt_exe_time')),
                                ('ft_fail_time', YLeaf(YType.str, 'ft_fail_time')),
                                ('lt_fail_time', YLeaf(YType.str, 'lt_fail_time')),
                                ('lt_pass_time', YLeaf(YType.str, 'lt_pass_time')),
                                ('total_fail_cnt', YLeaf(YType.int32, 'total_fail_cnt')),
                                ('cons_fail_cnt', YLeaf(YType.int32, 'cons_fail_cnt')),
                                ('more_info', YLeaf(YType.str, 'more_info')),
                            ])
                            self.data_idx = None
                            self.detail_flag = None
                            self.sl_no = None
                            self.test_name = None
                            self.test_result = None
                            self.err_code = None
                            self.err_description = None
                            self.test_type = None
                            self.hm_test_count = None
                            self.od_test_count = None
                            self.sched_test_count = None
                            self.run_cnt = None
                            self.lt_exe_time = None
                            self.ft_fail_time = None
                            self.lt_fail_time = None
                            self.lt_pass_time = None
                            self.total_fail_cnt = None
                            self.cons_fail_cnt = None
                            self.more_info = None
                            self._segment_path = lambda: "data_list" + "[data_idx='" + str(self.data_idx) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Diagnostic.Result.Location.Test.Detail.DataList, ['data_idx', 'detail_flag', 'sl_no', 'test_name', 'test_result', 'err_code', 'err_description', 'test_type', 'hm_test_count', 'od_test_count', 'sched_test_count', 'run_cnt', 'lt_exe_time', 'ft_fail_time', 'lt_fail_time', 'lt_pass_time', 'total_fail_cnt', 'cons_fail_cnt', 'more_info'], name, value)

    def clone_ptr(self):
        self._top_entity = Diagnostic()
        return self._top_entity

