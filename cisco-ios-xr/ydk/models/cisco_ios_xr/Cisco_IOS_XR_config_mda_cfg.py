""" Cisco_IOS_XR_config_mda_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR config\-mda package configuration.

This module contains definitions
for the following management objects\:
  active\-nodes\: Per\-node configuration for active nodes
  preconfigured\-nodes\: preconfigured nodes

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class ActiveNodes(Entity):
    """
    Per\-node configuration for active nodes
    
    .. attribute:: active_node
    
    	The configuration for an active node
    	**type**\: list of  		 :py:class:`ActiveNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode>`
    
    

    """

    _prefix = 'config-mda-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(ActiveNodes, self).__init__()
        self._top_entity = None

        self.yang_name = "active-nodes"
        self.yang_parent_name = "Cisco-IOS-XR-config-mda-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("active-node", ("active_node", ActiveNodes.ActiveNode))])
        self._leafs = OrderedDict()

        self.active_node = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-config-mda-cfg:active-nodes"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ActiveNodes, [], name, value)


    class ActiveNode(Entity):
        """
        The configuration for an active node
        
        .. attribute:: node_name  (key)
        
        	The identifier for this node
        	**type**\: str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: watchdog_node_threshold
        
        	watchdog node threshold
        	**type**\:  :py:class:`WatchdogNodeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.WatchdogNodeThreshold>`
        
        .. attribute:: ltrace
        
        	Ltrace Memory configuration
        	**type**\:  :py:class:`Ltrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.Ltrace>`
        
        .. attribute:: clock_interface
        
        	Configuration for a clock interface
        	**type**\:  :py:class:`ClockInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface>`
        
        .. attribute:: ssrp_group
        
        	Per\-node SSRP configuration data
        	**type**\:  :py:class:`SsrpGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.SsrpGroup>`
        
        .. attribute:: lpts_local
        
        	lpts node specific configuration commands
        	**type**\:  :py:class:`LptsLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal>`
        
        

        """

        _prefix = 'config-mda-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(ActiveNodes.ActiveNode, self).__init__()

            self.yang_name = "active-node"
            self.yang_parent_name = "active-nodes"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['node_name']
            self._child_classes = OrderedDict([("Cisco-IOS-XR-watchd-cfg:watchdog-node-threshold", ("watchdog_node_threshold", ActiveNodes.ActiveNode.WatchdogNodeThreshold)), ("Cisco-IOS-XR-infra-ltrace-cfg:ltrace", ("ltrace", ActiveNodes.ActiveNode.Ltrace)), ("Cisco-IOS-XR-freqsync-cfg:clock-interface", ("clock_interface", ActiveNodes.ActiveNode.ClockInterface)), ("Cisco-IOS-XR-ppp-ma-ssrp-cfg:ssrp-group", ("ssrp_group", ActiveNodes.ActiveNode.SsrpGroup)), ("Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local", ("lpts_local", ActiveNodes.ActiveNode.LptsLocal))])
            self._leafs = OrderedDict([
                ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
            ])
            self.node_name = None

            self.watchdog_node_threshold = ActiveNodes.ActiveNode.WatchdogNodeThreshold()
            self.watchdog_node_threshold.parent = self
            self._children_name_map["watchdog_node_threshold"] = "Cisco-IOS-XR-watchd-cfg:watchdog-node-threshold"

            self.ltrace = ActiveNodes.ActiveNode.Ltrace()
            self.ltrace.parent = self
            self._children_name_map["ltrace"] = "Cisco-IOS-XR-infra-ltrace-cfg:ltrace"

            self.clock_interface = ActiveNodes.ActiveNode.ClockInterface()
            self.clock_interface.parent = self
            self._children_name_map["clock_interface"] = "Cisco-IOS-XR-freqsync-cfg:clock-interface"

            self.ssrp_group = ActiveNodes.ActiveNode.SsrpGroup()
            self.ssrp_group.parent = self
            self._children_name_map["ssrp_group"] = "Cisco-IOS-XR-ppp-ma-ssrp-cfg:ssrp-group"

            self.lpts_local = ActiveNodes.ActiveNode.LptsLocal()
            self.lpts_local.parent = self
            self._children_name_map["lpts_local"] = "Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local"
            self._segment_path = lambda: "active-node" + "[node-name='" + str(self.node_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-config-mda-cfg:active-nodes/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ActiveNodes.ActiveNode, [u'node_name'], name, value)


        class WatchdogNodeThreshold(Entity):
            """
            watchdog node threshold
            
            .. attribute:: disk_threshold
            
            	Disk thresholds
            	**type**\:  :py:class:`DiskThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.WatchdogNodeThreshold.DiskThreshold>`
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\:  :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.WatchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'watchd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ActiveNodes.ActiveNode.WatchdogNodeThreshold, self).__init__()

                self.yang_name = "watchdog-node-threshold"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("disk-threshold", ("disk_threshold", ActiveNodes.ActiveNode.WatchdogNodeThreshold.DiskThreshold)), ("memory-threshold", ("memory_threshold", ActiveNodes.ActiveNode.WatchdogNodeThreshold.MemoryThreshold))])
                self._leafs = OrderedDict()

                self.disk_threshold = ActiveNodes.ActiveNode.WatchdogNodeThreshold.DiskThreshold()
                self.disk_threshold.parent = self
                self._children_name_map["disk_threshold"] = "disk-threshold"

                self.memory_threshold = ActiveNodes.ActiveNode.WatchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self
                self._children_name_map["memory_threshold"] = "memory-threshold"
                self._segment_path = lambda: "Cisco-IOS-XR-watchd-cfg:watchdog-node-threshold"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ActiveNodes.ActiveNode.WatchdogNodeThreshold, [], name, value)


            class DiskThreshold(Entity):
                """
                Disk thresholds
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\: int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\: int
                
                	**range:** 4..40
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\: int
                
                	**range:** 3..40
                
                

                """

                _prefix = 'watchd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.WatchdogNodeThreshold.DiskThreshold, self).__init__()

                    self.yang_name = "disk-threshold"
                    self.yang_parent_name = "watchdog-node-threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('minor', (YLeaf(YType.uint32, 'minor'), ['int'])),
                        ('severe', (YLeaf(YType.uint32, 'severe'), ['int'])),
                        ('critical', (YLeaf(YType.uint32, 'critical'), ['int'])),
                    ])
                    self.minor = None
                    self.severe = None
                    self.critical = None
                    self._segment_path = lambda: "disk-threshold"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.WatchdogNodeThreshold.DiskThreshold, ['minor', 'severe', 'critical'], name, value)


            class MemoryThreshold(Entity):
                """
                Memory thresholds
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\: int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\: int
                
                	**range:** 4..40
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\: int
                
                	**range:** 3..40
                
                

                """

                _prefix = 'watchd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.WatchdogNodeThreshold.MemoryThreshold, self).__init__()

                    self.yang_name = "memory-threshold"
                    self.yang_parent_name = "watchdog-node-threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('minor', (YLeaf(YType.uint32, 'minor'), ['int'])),
                        ('severe', (YLeaf(YType.uint32, 'severe'), ['int'])),
                        ('critical', (YLeaf(YType.uint32, 'critical'), ['int'])),
                    ])
                    self.minor = None
                    self.severe = None
                    self.critical = None
                    self._segment_path = lambda: "memory-threshold"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.WatchdogNodeThreshold.MemoryThreshold, ['minor', 'severe', 'critical'], name, value)


        class Ltrace(Entity):
            """
            Ltrace Memory configuration
            
            .. attribute:: allocation_params
            
            	Select Ltrace mode and scale\-factor
            	**type**\:  :py:class:`AllocationParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.Ltrace.AllocationParams>`
            
            

            """

            _prefix = 'infra-ltrace-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ActiveNodes.ActiveNode.Ltrace, self).__init__()

                self.yang_name = "ltrace"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("allocation-params", ("allocation_params", ActiveNodes.ActiveNode.Ltrace.AllocationParams))])
                self._leafs = OrderedDict()

                self.allocation_params = ActiveNodes.ActiveNode.Ltrace.AllocationParams()
                self.allocation_params.parent = self
                self._children_name_map["allocation_params"] = "allocation-params"
                self._segment_path = lambda: "Cisco-IOS-XR-infra-ltrace-cfg:ltrace"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ActiveNodes.ActiveNode.Ltrace, [], name, value)


            class AllocationParams(Entity):
                """
                Select Ltrace mode and scale\-factor
                
                .. attribute:: mode
                
                	Select an allocation mode (static\:1, dynamic \:2)
                	**type**\:  :py:class:`InfraLtraceMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceMode>`
                
                .. attribute:: scale_factor
                
                	Select a scaling down factor
                	**type**\:  :py:class:`InfraLtraceScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceScale>`
                
                

                """

                _prefix = 'infra-ltrace-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.Ltrace.AllocationParams, self).__init__()

                    self.yang_name = "allocation-params"
                    self.yang_parent_name = "ltrace"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg', 'InfraLtraceMode', '')])),
                        ('scale_factor', (YLeaf(YType.enumeration, 'scale-factor'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg', 'InfraLtraceScale', '')])),
                    ])
                    self.mode = None
                    self.scale_factor = None
                    self._segment_path = lambda: "allocation-params"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.Ltrace.AllocationParams, ['mode', 'scale_factor'], name, value)


        class ClockInterface(Entity):
            """
            Configuration for a clock interface
            
            .. attribute:: clocks
            
            	Configuration for a clock interface
            	**type**\:  :py:class:`Clocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks>`
            
            

            """

            _prefix = 'freqsync-cfg'
            _revision = '2017-09-30'

            def __init__(self):
                super(ActiveNodes.ActiveNode.ClockInterface, self).__init__()

                self.yang_name = "clock-interface"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("clocks", ("clocks", ActiveNodes.ActiveNode.ClockInterface.Clocks))])
                self._leafs = OrderedDict()

                self.clocks = ActiveNodes.ActiveNode.ClockInterface.Clocks()
                self.clocks.parent = self
                self._children_name_map["clocks"] = "clocks"
                self._segment_path = lambda: "Cisco-IOS-XR-freqsync-cfg:clock-interface"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface, [], name, value)


            class Clocks(Entity):
                """
                Configuration for a clock interface
                
                .. attribute:: clock
                
                	Configuration for a clock interface
                	**type**\: list of  		 :py:class:`Clock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock>`
                
                

                """

                _prefix = 'freqsync-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.ClockInterface.Clocks, self).__init__()

                    self.yang_name = "clocks"
                    self.yang_parent_name = "clock-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("clock", ("clock", ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock))])
                    self._leafs = OrderedDict()

                    self.clock = YList(self)
                    self._segment_path = lambda: "clocks"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks, [], name, value)


                class Clock(Entity):
                    """
                    Configuration for a clock interface
                    
                    .. attribute:: clock_type  (key)
                    
                    	Clock type
                    	**type**\:  :py:class:`FsyncClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncClock>`
                    
                    .. attribute:: port  (key)
                    
                    	Clock port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: frequency_synchronization
                    
                    	Frequency Synchronization clock configuraiton
                    	**type**\:  :py:class:`FrequencySynchronization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization>`
                    
                    .. attribute:: sync_controller
                    
                    	sync\-controller value
                    	**type**\:  :py:class:`SyncController <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController>`
                    
                    

                    """

                    _prefix = 'freqsync-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock, self).__init__()

                        self.yang_name = "clock"
                        self.yang_parent_name = "clocks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['clock_type','port']
                        self._child_classes = OrderedDict([("frequency-synchronization", ("frequency_synchronization", ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization)), ("Cisco-IOS-XR-syncc-controller-cfg:sync-controller", ("sync_controller", ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController))])
                        self._leafs = OrderedDict([
                            ('clock_type', (YLeaf(YType.enumeration, 'clock-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncClock', '')])),
                            ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                        ])
                        self.clock_type = None
                        self.port = None

                        self.frequency_synchronization = ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization()
                        self.frequency_synchronization.parent = self
                        self._children_name_map["frequency_synchronization"] = "frequency-synchronization"

                        self.sync_controller = ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController()
                        self.sync_controller.parent = self
                        self._children_name_map["sync_controller"] = "Cisco-IOS-XR-syncc-controller-cfg:sync-controller"
                        self._segment_path = lambda: "clock" + "[clock-type='" + str(self.clock_type) + "']" + "[port='" + str(self.port) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock, ['clock_type', 'port'], name, value)


                    class FrequencySynchronization(Entity):
                        """
                        Frequency Synchronization clock configuraiton
                        
                        .. attribute:: output_quality_level
                        
                        	Set the output quality level
                        	**type**\:  :py:class:`OutputQualityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel>`
                        
                        .. attribute:: input_quality_level
                        
                        	Set the input quality level
                        	**type**\:  :py:class:`InputQualityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel>`
                        
                        .. attribute:: wait_to_restore_time
                        
                        	Set the wait\-to\-restore time for this source
                        	**type**\: int
                        
                        	**range:** 0..12
                        
                        	**default value**\: 5
                        
                        .. attribute:: priority
                        
                        	Set the priority of this source
                        	**type**\: int
                        
                        	**range:** 1..254
                        
                        	**default value**\: 100
                        
                        .. attribute:: selection_input
                        
                        	Assign this source as a selection input
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: time_of_day_priority
                        
                        	Set the time\-of\-day priority of this source
                        	**type**\: int
                        
                        	**range:** 1..254
                        
                        	**default value**\: 100
                        
                        .. attribute:: ssm_disable
                        
                        	Disable SSM on this source
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'freqsync-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization, self).__init__()

                            self.yang_name = "frequency-synchronization"
                            self.yang_parent_name = "clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("output-quality-level", ("output_quality_level", ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel)), ("input-quality-level", ("input_quality_level", ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel))])
                            self._leafs = OrderedDict([
                                ('wait_to_restore_time', (YLeaf(YType.uint32, 'wait-to-restore-time'), ['int'])),
                                ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                ('selection_input', (YLeaf(YType.empty, 'selection-input'), ['Empty'])),
                                ('time_of_day_priority', (YLeaf(YType.uint32, 'time-of-day-priority'), ['int'])),
                                ('ssm_disable', (YLeaf(YType.empty, 'ssm-disable'), ['Empty'])),
                            ])
                            self.wait_to_restore_time = None
                            self.priority = None
                            self.selection_input = None
                            self.time_of_day_priority = None
                            self.ssm_disable = None

                            self.output_quality_level = ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel()
                            self.output_quality_level.parent = self
                            self._children_name_map["output_quality_level"] = "output-quality-level"

                            self.input_quality_level = ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel()
                            self.input_quality_level.parent = self
                            self._children_name_map["input_quality_level"] = "input-quality-level"
                            self._segment_path = lambda: "frequency-synchronization"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization, ['wait_to_restore_time', 'priority', 'selection_input', 'time_of_day_priority', 'ssm_disable'], name, value)


                        class OutputQualityLevel(Entity):
                            """
                            Set the output quality level
                            
                            .. attribute:: quality_level_option
                            
                            	Quality level option
                            	**type**\:  :py:class:`FsyncQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlOption>`
                            
                            .. attribute:: exact_quality_level_value
                            
                            	Exact quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: min_quality_level_value
                            
                            	Minimum quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: max_quality_level_value
                            
                            	Maximum quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            

                            """

                            _prefix = 'freqsync-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel, self).__init__()

                                self.yang_name = "output-quality-level"
                                self.yang_parent_name = "frequency-synchronization"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlOption', '')])),
                                    ('exact_quality_level_value', (YLeaf(YType.enumeration, 'exact-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                    ('min_quality_level_value', (YLeaf(YType.enumeration, 'min-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                    ('max_quality_level_value', (YLeaf(YType.enumeration, 'max-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                ])
                                self.quality_level_option = None
                                self.exact_quality_level_value = None
                                self.min_quality_level_value = None
                                self.max_quality_level_value = None
                                self._segment_path = lambda: "output-quality-level"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel, ['quality_level_option', 'exact_quality_level_value', 'min_quality_level_value', 'max_quality_level_value'], name, value)


                        class InputQualityLevel(Entity):
                            """
                            Set the input quality level
                            
                            .. attribute:: quality_level_option
                            
                            	Quality level option
                            	**type**\:  :py:class:`FsyncQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlOption>`
                            
                            .. attribute:: exact_quality_level_value
                            
                            	Exact quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: min_quality_level_value
                            
                            	Minimum quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: max_quality_level_value
                            
                            	Maximum quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            

                            """

                            _prefix = 'freqsync-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel, self).__init__()

                                self.yang_name = "input-quality-level"
                                self.yang_parent_name = "frequency-synchronization"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlOption', '')])),
                                    ('exact_quality_level_value', (YLeaf(YType.enumeration, 'exact-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                    ('min_quality_level_value', (YLeaf(YType.enumeration, 'min-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                    ('max_quality_level_value', (YLeaf(YType.enumeration, 'max-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                ])
                                self.quality_level_option = None
                                self.exact_quality_level_value = None
                                self.min_quality_level_value = None
                                self.max_quality_level_value = None
                                self._segment_path = lambda: "input-quality-level"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel, ['quality_level_option', 'exact_quality_level_value', 'min_quality_level_value', 'max_quality_level_value'], name, value)


                    class SyncController(Entity):
                        """
                        sync\-controller value
                        
                        .. attribute:: transport_mode
                        
                        	Transport mode
                        	**type**\:  :py:class:`TransportMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController.TransportMode>`
                        
                        

                        """

                        _prefix = 'syncc-controller-cfg'
                        _revision = '2017-06-22'

                        def __init__(self):
                            super(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController, self).__init__()

                            self.yang_name = "sync-controller"
                            self.yang_parent_name = "clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("transport-mode", ("transport_mode", ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController.TransportMode))])
                            self._leafs = OrderedDict()

                            self.transport_mode = ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController.TransportMode()
                            self.transport_mode.parent = self
                            self._children_name_map["transport_mode"] = "transport-mode"
                            self._segment_path = lambda: "Cisco-IOS-XR-syncc-controller-cfg:sync-controller"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController, [], name, value)


                        class TransportMode(Entity):
                            """
                            Transport mode
                            
                            .. attribute:: frequency_mode
                            
                            	Frequency Mode
                            	**type**\:  :py:class:`FrequencyMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController.TransportMode.FrequencyMode>`
                            
                            

                            """

                            _prefix = 'syncc-controller-cfg'
                            _revision = '2017-06-22'

                            def __init__(self):
                                super(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController.TransportMode, self).__init__()

                                self.yang_name = "transport-mode"
                                self.yang_parent_name = "sync-controller"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("frequency-mode", ("frequency_mode", ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController.TransportMode.FrequencyMode))])
                                self._leafs = OrderedDict()

                                self.frequency_mode = ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController.TransportMode.FrequencyMode()
                                self.frequency_mode.parent = self
                                self._children_name_map["frequency_mode"] = "frequency-mode"
                                self._segment_path = lambda: "transport-mode"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController.TransportMode, [], name, value)


                            class FrequencyMode(Entity):
                                """
                                Frequency Mode
                                
                                .. attribute:: port_mode
                                
                                	clock\-interface sync <value> location <value> port\-parameters bits\-input 2m \-> Option1=0, Option2=2, Option3=0, Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-input 2m \-> Option1=0, Option2=2, Option3=0, Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-input 64k\-input\-only \-> Option1=0, Option2=3, Option3=0, Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa4 ami \-> Option1=0, Option2=1, Option3=1, Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa4 hdb3 \-> Option1=0, Option2=1, Option3=1, Option4=0 , Option5=1 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa5 ami \-> Option1=0, Option2=1, Option3=1, Option4=0, Option5=1 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa5 hdb3 \-> Option1=0, Option2=1, Option3=1, Option4=1 , Option5=1 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa6 ami \-> Option1=0, Option2=1, Option3=1, Option4=0, Option5=2 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa6 hdb3 \-> Option1=0, Option2=1, Option3=1, Option4=1 , Option5=2 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa7 ami \-> Option1=0, Option2=1, Option3=1, Option4=0, Option5=3 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa7 hdb3 \-> Option1=0, Option2=1, Option3=1, Option4=1 , Option5=3 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa8 ami \-> Option1=0, Option2=1, Option3=1, Option4=0, Option5=4 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa8 hdb3 \-> Option1=0, Option2=1, Option3=1, Option4=1 , Option5=4 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 non\-crc\-4 ami \-> Option1=0, Option2=1, Option3=0, Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 non\-crc\-4 hdb3 \-> Option1=0, Option2=1, Option3=0, Option4=1 , Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-input t1 d4 ami \-> Option1=0, Option2=0, Option3=1, Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-input t1 d4 b8zs \-> Option1=0, Option2=0 , Option3=1, Option4=1, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-input t1 esf ami \-> Option1=0, Option2=0, Option3=0, Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-input t1 esf b8zs \-> Option1=0, Option2=0, Option3=0, Option4=1, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output 2m \-> Option1=1 , Option2=2, Option3=0, Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output 6m\-output\-only \-> Option1=1 , Option2=4, Option3=0 , Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa4 ami \-> Option1=1 , Option2=1, Option3=1 , Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa4 hdb3 \-> Option1=1 , Option2=1, Option3=1 , Option4=1, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa5 ami \-> Option1=1 , Option2=1, Option3=1 , Option4=0, Option5=1 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa5 hdb3 \-> Option1=1 , Option2=1, Option3=1 , Option4=1, Option5=1 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa6 ami \-> Option1=1 , Option2=1, Option3=1 , Option4=0, Option5=2 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa6 hdb3 \-> Option1=1 , Option2=1, Option3=1 , Option4=1, Option5=2 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa7 ami \-> Option1=1 , Option2=1, Option3=1 , Option4=0, Option5=3 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa7 hdb3 \-> Option1=1 , Option2=1, Option3=1 , Option4=1, Option5=3 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa8 ami \-> Option1=1 , Option2=1, Option3=1 , Option4=0, Option5=4 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa8 hdb3 \-> Option1=1 , Option2=1, Option3=1 , Option4=1, Option5=4 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 non\-crc\-4 ami \-> Option1=1 , Option2=1, Option3=0 , Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 non\-crc\-4 hdb3 \-> Option1=1 , Option2=1, Option3=0 , Option4=1, Option5=0clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 ami 0 \-> Option1=1 , Option2=0, Option3=1 , Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 ami 1 \-> Option1=1 , Option2=0, Option3=1 , Option4=0, Option5=1 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 ami 2 \-> Option1=1 , Option2=0, Option3=1 , Option4=0, Option5=2 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 ami 3 \-> Option1=1 , Option2=0, Option3=1 , Option4=0, Option5=3 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 ami 4 \-> Option1=1 , Option2=0, Option3=1 , Option4=0, Option5=4 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 b8zs 0 \-> Option1=1 , Option2=0, Option3=1 , Option4=1, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 b8zs 1 \-> Option1=1 , Option2=0, Option3=1 , Option4=1, Option5=1 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 b8zs 2 \-> Option1=1 , Option2=0, Option3=1 , Option4=1, Option5=2 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 b8zs 3 \-> Option1=1 , Option2=0, Option3=1 , Option4=1, Option5=3 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 b8zs 4 \-> Option1=1 , Option2=0, Option3=1 , Option4=1, Option5=4 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf ami 0 \-> Option1=1 , Option2=0, Option3=0 , Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf ami 1 \-> Option1=1 , Option2=0, Option3=0 , Option4=0, Option5=1 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf ami 2 \-> Option1=1 , Option2=0, Option3=0 , Option4=0, Option5=2 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf ami 3 \-> Option1=1 , Option2=0, Option3=0 , Option4=0, Option5=3 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf ami 4 \-> Option1=1 , Option2=0, Option3=0 , Option4=0, Option5=4 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf b8zs 0 \-> Option1=1 , Option2=0, Option3=0 , Option4=1, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf b8zs 1 \-> Option1=1 , Option2=0, Option3=0 , Option4=1, Option5=1 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf b8zs 2 \-> Option1=1 , Option2=0, Option3=0 , Option4=1, Option5=2 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf b8zs 3 \-> Option1=1 , Option2=0, Option3=0 , Option4=1, Option5=3 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf b8zs 4 \-> Option1=1 , Option2=0, Option3=0 , Option4=1, Option5=4 clock\-interface sync <value> location <value> port\-parameters port\-parameters uti \-> Option1=2 , Option2=0, Option3=0 , Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters port\-parameters gps\-input \-> Option1=3, Option2=0, Option3=0 , Option4=0, Option5=0 
                                	**type**\:  :py:class:`PortMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController.TransportMode.FrequencyMode.PortMode>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: shutdown
                                
                                	Disable the SyncE Port
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'syncc-controller-cfg'
                                _revision = '2017-06-22'

                                def __init__(self):
                                    super(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController.TransportMode.FrequencyMode, self).__init__()

                                    self.yang_name = "frequency-mode"
                                    self.yang_parent_name = "transport-mode"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("port-mode", ("port_mode", ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController.TransportMode.FrequencyMode.PortMode))])
                                    self._leafs = OrderedDict([
                                        ('shutdown', (YLeaf(YType.empty, 'shutdown'), ['Empty'])),
                                    ])
                                    self.shutdown = None

                                    self.port_mode = None
                                    self._children_name_map["port_mode"] = "port-mode"
                                    self._segment_path = lambda: "frequency-mode"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController.TransportMode.FrequencyMode, ['shutdown'], name, value)


                                class PortMode(Entity):
                                    """
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input 2m \-> Option1=0,
                                    Option2=2, Option3=0, Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input 2m \-> Option1=0,
                                    Option2=2, Option3=0, Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input 64k\-input\-only \->
                                    Option1=0, Option2=3, Option3=0, Option4=0,
                                    Option5=0 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-input
                                    e1 crc\-4 sa4 ami \-> Option1=0, Option2=1,
                                    Option3=1, Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input e1 crc\-4 sa4 hdb3
                                    \-> Option1=0, Option2=1, Option3=1, Option4=0
                                    , Option5=1 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-input
                                    e1 crc\-4 sa5 ami \-> Option1=0, Option2=1,
                                    Option3=1, Option4=0, Option5=1
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input e1 crc\-4 sa5 hdb3
                                    \-> Option1=0, Option2=1, Option3=1, Option4=1
                                    , Option5=1 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-input
                                    e1 crc\-4 sa6 ami \-> Option1=0, Option2=1,
                                    Option3=1, Option4=0, Option5=2
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input e1 crc\-4 sa6 hdb3
                                    \-> Option1=0, Option2=1, Option3=1, Option4=1
                                    , Option5=2 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-input
                                    e1 crc\-4 sa7 ami \-> Option1=0, Option2=1,
                                    Option3=1, Option4=0, Option5=3
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input e1 crc\-4 sa7 hdb3
                                    \-> Option1=0, Option2=1, Option3=1, Option4=1
                                    , Option5=3 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-input
                                    e1 crc\-4 sa8 ami \-> Option1=0, Option2=1,
                                    Option3=1, Option4=0, Option5=4
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input e1 crc\-4 sa8 hdb3
                                    \-> Option1=0, Option2=1, Option3=1, Option4=1
                                    , Option5=4 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-input
                                    e1 non\-crc\-4 ami \-> Option1=0, Option2=1,
                                    Option3=0, Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input e1 non\-crc\-4 hdb3
                                    \-> Option1=0, Option2=1, Option3=0, Option4=1
                                    , Option5=0 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-input
                                    t1 d4 ami \-> Option1=0, Option2=0, Option3=1,
                                    Option4=0, Option5=0 clock\-interface sync
                                    <value> location <value> port\-parameters
                                    bits\-input t1 d4 b8zs \-> Option1=0, Option2=0
                                    , Option3=1, Option4=1, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input t1 esf ami \->
                                    Option1=0, Option2=0, Option3=0, Option4=0,
                                    Option5=0 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-input
                                    t1 esf b8zs \-> Option1=0, Option2=0,
                                    Option3=0, Option4=1, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output 2m \-> Option1=1 ,
                                    Option2=2, Option3=0, Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output 6m\-output\-only \->
                                    Option1=1 , Option2=4, Option3=0 , Option4=0,
                                    Option5=0 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    e1 crc\-4 sa4 ami \-> Option1=1 , Option2=1,
                                    Option3=1 , Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output e1 crc\-4 sa4 hdb3
                                    \-> Option1=1 , Option2=1, Option3=1 ,
                                    Option4=1, Option5=0 clock\-interface sync
                                    <value> location <value> port\-parameters
                                    bits\-output e1 crc\-4 sa5 ami \-> Option1=1 ,
                                    Option2=1, Option3=1 , Option4=0, Option5=1
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output e1 crc\-4 sa5 hdb3
                                    \-> Option1=1 , Option2=1, Option3=1 ,
                                    Option4=1, Option5=1 clock\-interface sync
                                    <value> location <value> port\-parameters
                                    bits\-output e1 crc\-4 sa6 ami \-> Option1=1 ,
                                    Option2=1, Option3=1 , Option4=0, Option5=2
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output e1 crc\-4 sa6 hdb3
                                    \-> Option1=1 , Option2=1, Option3=1 ,
                                    Option4=1, Option5=2 clock\-interface sync
                                    <value> location <value> port\-parameters
                                    bits\-output e1 crc\-4 sa7 ami \-> Option1=1 ,
                                    Option2=1, Option3=1 , Option4=0, Option5=3
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output e1 crc\-4 sa7 hdb3
                                    \-> Option1=1 , Option2=1, Option3=1 ,
                                    Option4=1, Option5=3 clock\-interface sync
                                    <value> location <value> port\-parameters
                                    bits\-output e1 crc\-4 sa8 ami \-> Option1=1 ,
                                    Option2=1, Option3=1 , Option4=0, Option5=4
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output e1 crc\-4 sa8 hdb3
                                    \-> Option1=1 , Option2=1, Option3=1 ,
                                    Option4=1, Option5=4 clock\-interface sync
                                    <value> location <value> port\-parameters
                                    bits\-output e1 non\-crc\-4 ami \-> Option1=1 ,
                                    Option2=1, Option3=0 , Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output e1 non\-crc\-4 hdb3
                                    \-> Option1=1 , Option2=1, Option3=0 ,
                                    Option4=1, Option5=0clock\-interface sync
                                    <value> location <value> port\-parameters
                                    bits\-output t1 d4 ami 0 \-> Option1=1 ,
                                    Option2=0, Option3=1 , Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 d4 ami 1 \->
                                    Option1=1 , Option2=0, Option3=1 , Option4=0,
                                    Option5=1 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    t1 d4 ami 2 \-> Option1=1 , Option2=0,
                                    Option3=1 , Option4=0, Option5=2
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 d4 ami 3 \->
                                    Option1=1 , Option2=0, Option3=1 , Option4=0,
                                    Option5=3 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    t1 d4 ami 4 \-> Option1=1 , Option2=0,
                                    Option3=1 , Option4=0, Option5=4
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 d4 b8zs 0 \->
                                    Option1=1 , Option2=0, Option3=1 , Option4=1,
                                    Option5=0 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    t1 d4 b8zs 1 \-> Option1=1 , Option2=0,
                                    Option3=1 , Option4=1, Option5=1
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 d4 b8zs 2 \->
                                    Option1=1 , Option2=0, Option3=1 , Option4=1,
                                    Option5=2 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    t1 d4 b8zs 3 \-> Option1=1 , Option2=0,
                                    Option3=1 , Option4=1, Option5=3
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 d4 b8zs 4 \->
                                    Option1=1 , Option2=0, Option3=1 , Option4=1,
                                    Option5=4 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    t1 esf ami 0 \-> Option1=1 , Option2=0,
                                    Option3=0 , Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 esf ami 1 \->
                                    Option1=1 , Option2=0, Option3=0 , Option4=0,
                                    Option5=1 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    t1 esf ami 2 \-> Option1=1 , Option2=0,
                                    Option3=0 , Option4=0, Option5=2
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 esf ami 3 \->
                                    Option1=1 , Option2=0, Option3=0 , Option4=0,
                                    Option5=3 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    t1 esf ami 4 \-> Option1=1 , Option2=0,
                                    Option3=0 , Option4=0, Option5=4
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 esf b8zs 0 \->
                                    Option1=1 , Option2=0, Option3=0 , Option4=1,
                                    Option5=0 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    t1 esf b8zs 1 \-> Option1=1 , Option2=0,
                                    Option3=0 , Option4=1, Option5=1
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 esf b8zs 2 \->
                                    Option1=1 , Option2=0, Option3=0 , Option4=1,
                                    Option5=2 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    t1 esf b8zs 3 \-> Option1=1 , Option2=0,
                                    Option3=0 , Option4=1, Option5=3
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 esf b8zs 4 \->
                                    Option1=1 , Option2=0, Option3=0 , Option4=1,
                                    Option5=4 clock\-interface sync <value>
                                    location <value> port\-parameters
                                    port\-parameters uti \-> Option1=2 , Option2=0,
                                    Option3=0 , Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters port\-parameters gps\-input \->
                                    Option1=3, Option2=0, Option3=0 , Option4=0,
                                    Option5=0 
                                    
                                    .. attribute:: option1
                                    
                                    	Option value #1
                                    	**type**\: int
                                    
                                    	**range:** 0..3
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: option2
                                    
                                    	Option value #2
                                    	**type**\: int
                                    
                                    	**range:** 0..4
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: option3
                                    
                                    	Option value #3
                                    	**type**\: int
                                    
                                    	**range:** 0..1
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: option4
                                    
                                    	Option value #4
                                    	**type**\: int
                                    
                                    	**range:** 0..1
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: option5
                                    
                                    	Option value #5
                                    	**type**\: int
                                    
                                    	**range:** 0..4
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'syncc-controller-cfg'
                                    _revision = '2017-06-22'

                                    def __init__(self):
                                        super(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController.TransportMode.FrequencyMode.PortMode, self).__init__()

                                        self.yang_name = "port-mode"
                                        self.yang_parent_name = "frequency-mode"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('option1', (YLeaf(YType.uint32, 'option1'), ['int'])),
                                            ('option2', (YLeaf(YType.uint32, 'option2'), ['int'])),
                                            ('option3', (YLeaf(YType.uint32, 'option3'), ['int'])),
                                            ('option4', (YLeaf(YType.uint32, 'option4'), ['int'])),
                                            ('option5', (YLeaf(YType.uint32, 'option5'), ['int'])),
                                        ])
                                        self.option1 = None
                                        self.option2 = None
                                        self.option3 = None
                                        self.option4 = None
                                        self.option5 = None
                                        self._segment_path = lambda: "port-mode"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.SyncController.TransportMode.FrequencyMode.PortMode, ['option1', 'option2', 'option3', 'option4', 'option5'], name, value)


        class SsrpGroup(Entity):
            """
            Per\-node SSRP configuration data
            
            .. attribute:: groups
            
            	Table of SSRP Group configuration
            	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.SsrpGroup.Groups>`
            
            

            """

            _prefix = 'ppp-ma-ssrp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ActiveNodes.ActiveNode.SsrpGroup, self).__init__()

                self.yang_name = "ssrp-group"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("groups", ("groups", ActiveNodes.ActiveNode.SsrpGroup.Groups))])
                self._leafs = OrderedDict()

                self.groups = ActiveNodes.ActiveNode.SsrpGroup.Groups()
                self.groups.parent = self
                self._children_name_map["groups"] = "groups"
                self._segment_path = lambda: "Cisco-IOS-XR-ppp-ma-ssrp-cfg:ssrp-group"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ActiveNodes.ActiveNode.SsrpGroup, [], name, value)


            class Groups(Entity):
                """
                Table of SSRP Group configuration
                
                .. attribute:: group
                
                	SSRP Group configuration
                	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.SsrpGroup.Groups.Group>`
                
                

                """

                _prefix = 'ppp-ma-ssrp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.SsrpGroup.Groups, self).__init__()

                    self.yang_name = "groups"
                    self.yang_parent_name = "ssrp-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("group", ("group", ActiveNodes.ActiveNode.SsrpGroup.Groups.Group))])
                    self._leafs = OrderedDict()

                    self.group = YList(self)
                    self._segment_path = lambda: "groups"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.SsrpGroup.Groups, [], name, value)


                class Group(Entity):
                    """
                    SSRP Group configuration
                    
                    .. attribute:: group_id  (key)
                    
                    	The identifier for this group
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: profile
                    
                    	This specifies the SSRP profile to use for this group
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ppp-ma-ssrp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ActiveNodes.ActiveNode.SsrpGroup.Groups.Group, self).__init__()

                        self.yang_name = "group"
                        self.yang_parent_name = "groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['group_id']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('group_id', (YLeaf(YType.uint32, 'group-id'), ['int'])),
                            ('profile', (YLeaf(YType.str, 'profile'), ['str'])),
                        ])
                        self.group_id = None
                        self.profile = None
                        self._segment_path = lambda: "group" + "[group-id='" + str(self.group_id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.SsrpGroup.Groups.Group, ['group_id', 'profile'], name, value)


        class LptsLocal(Entity):
            """
            lpts node specific configuration commands
            
            .. attribute:: ipolicer_local_tables
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:  :py:class:`IpolicerLocalTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables>`
            
            .. attribute:: dynamic_flows_tables
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:  :py:class:`DynamicFlowsTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables>`
            
            .. attribute:: ipolicer_local
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:  :py:class:`IpolicerLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(ActiveNodes.ActiveNode.LptsLocal, self).__init__()

                self.yang_name = "lpts-local"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ipolicer-local-tables", ("ipolicer_local_tables", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables)), ("dynamic-flows-tables", ("dynamic_flows_tables", ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables)), ("ipolicer-local", ("ipolicer_local", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal))])
                self._leafs = OrderedDict()

                self.ipolicer_local_tables = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables()
                self.ipolicer_local_tables.parent = self
                self._children_name_map["ipolicer_local_tables"] = "ipolicer-local-tables"

                self.dynamic_flows_tables = ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables()
                self.dynamic_flows_tables.parent = self
                self._children_name_map["dynamic_flows_tables"] = "dynamic-flows-tables"

                self.ipolicer_local = None
                self._children_name_map["ipolicer_local"] = "ipolicer-local"
                self._segment_path = lambda: "Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal, [], name, value)


            class IpolicerLocalTables(Entity):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: ipolicer_local_table
                
                	Pre IFIB (Internal Forwarding Information Base) configuration table
                	**type**\: list of  		 :py:class:`IpolicerLocalTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables, self).__init__()

                    self.yang_name = "ipolicer-local-tables"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ipolicer-local-table", ("ipolicer_local_table", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable))])
                    self._leafs = OrderedDict()

                    self.ipolicer_local_table = YList(self)
                    self._segment_path = lambda: "ipolicer-local-tables"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables, [], name, value)


                class IpolicerLocalTable(Entity):
                    """
                    Pre IFIB (Internal Forwarding Information
                    Base) configuration table
                    
                    .. attribute:: id1  (key)
                    
                    	none
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: np_flows
                    
                    	NP name
                    	**type**\:  :py:class:`NpFlows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable, self).__init__()

                        self.yang_name = "ipolicer-local-table"
                        self.yang_parent_name = "ipolicer-local-tables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['id1']
                        self._child_classes = OrderedDict([("np-flows", ("np_flows", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows))])
                        self._leafs = OrderedDict([
                            ('id1', (YLeaf(YType.str, 'id1'), ['str'])),
                        ])
                        self.id1 = None

                        self.np_flows = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows()
                        self.np_flows.parent = self
                        self._children_name_map["np_flows"] = "np-flows"
                        self._segment_path = lambda: "ipolicer-local-table" + "[id1='" + str(self.id1) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable, ['id1'], name, value)


                    class NpFlows(Entity):
                        """
                        NP name
                        
                        .. attribute:: np_flow
                        
                        	Table of NP Flow names
                        	**type**\: list of  		 :py:class:`NpFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows.NpFlow>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows, self).__init__()

                            self.yang_name = "np-flows"
                            self.yang_parent_name = "ipolicer-local-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("np-flow", ("np_flow", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows.NpFlow))])
                            self._leafs = OrderedDict()

                            self.np_flow = YList(self)
                            self._segment_path = lambda: "np-flows"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows, [], name, value)


                        class NpFlow(Entity):
                            """
                            Table of NP Flow names
                            
                            .. attribute:: flow_type  (key)
                            
                            	LPTS Flow Type
                            	**type**\:  :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                            
                            .. attribute:: np_rate
                            
                            	Configured rate value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows.NpFlow, self).__init__()

                                self.yang_name = "np-flow"
                                self.yang_parent_name = "np-flows"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['flow_type']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('flow_type', (YLeaf(YType.enumeration, 'flow-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow', '')])),
                                    ('np_rate', (YLeaf(YType.uint32, 'np-rate'), ['int'])),
                                ])
                                self.flow_type = None
                                self.np_rate = None
                                self._segment_path = lambda: "np-flow" + "[flow-type='" + str(self.flow_type) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows.NpFlow, ['flow_type', 'np_rate'], name, value)


            class DynamicFlowsTables(Entity):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: dynamic_flows_table
                
                	Table for Dynamic Flows
                	**type**\: list of  		 :py:class:`DynamicFlowsTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables, self).__init__()

                    self.yang_name = "dynamic-flows-tables"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("dynamic-flows-table", ("dynamic_flows_table", ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable))])
                    self._leafs = OrderedDict()

                    self.dynamic_flows_table = YList(self)
                    self._segment_path = lambda: "dynamic-flows-tables"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables, [], name, value)


                class DynamicFlowsTable(Entity):
                    """
                    Table for Dynamic Flows
                    
                    .. attribute:: table_type  (key)
                    
                    	LPTS Dynamic Flows Table Type
                    	**type**\:  :py:class:`LptsDynamicFlowConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsDynamicFlowConfig>`
                    
                    .. attribute:: flow_type
                    
                    	Selected flow type
                    	**type**\: list of  		 :py:class:`FlowType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable, self).__init__()

                        self.yang_name = "dynamic-flows-table"
                        self.yang_parent_name = "dynamic-flows-tables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['table_type']
                        self._child_classes = OrderedDict([("flow-type", ("flow_type", ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType))])
                        self._leafs = OrderedDict([
                            ('table_type', (YLeaf(YType.enumeration, 'table-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsDynamicFlowConfig', '')])),
                        ])
                        self.table_type = None

                        self.flow_type = YList(self)
                        self._segment_path = lambda: "dynamic-flows-table" + "[table-type='" + str(self.table_type) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable, ['table_type'], name, value)


                    class FlowType(Entity):
                        """
                        Selected flow type
                        
                        .. attribute:: flow_type  (key)
                        
                        	LPTS Flow Type
                        	**type**\:  :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                        
                        .. attribute:: max
                        
                        	Configured Max TCAM value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType, self).__init__()

                            self.yang_name = "flow-type"
                            self.yang_parent_name = "dynamic-flows-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['flow_type']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('flow_type', (YLeaf(YType.enumeration, 'flow-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow', '')])),
                                ('max', (YLeaf(YType.uint32, 'max'), ['int'])),
                            ])
                            self.flow_type = None
                            self.max = None
                            self._segment_path = lambda: "flow-type" + "[flow-type='" + str(self.flow_type) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType, ['flow_type', 'max'], name, value)


            class IpolicerLocal(Entity):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: enable
                
                	Enabled
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: flows
                
                	Table for Flows
                	**type**\:  :py:class:`Flows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal, self).__init__()

                    self.yang_name = "ipolicer-local"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("flows", ("flows", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows))])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.enable = None

                    self.flows = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows()
                    self.flows.parent = self
                    self._children_name_map["flows"] = "flows"
                    self._segment_path = lambda: "ipolicer-local"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal, ['enable'], name, value)


                class Flows(Entity):
                    """
                    Table for Flows
                    
                    .. attribute:: flow
                    
                    	selected flow type
                    	**type**\: list of  		 :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows, self).__init__()

                        self.yang_name = "flows"
                        self.yang_parent_name = "ipolicer-local"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("flow", ("flow", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow))])
                        self._leafs = OrderedDict()

                        self.flow = YList(self)
                        self._segment_path = lambda: "flows"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows, [], name, value)


                    class Flow(Entity):
                        """
                        selected flow type
                        
                        .. attribute:: flow_type  (key)
                        
                        	LPTS Flow Type
                        	**type**\:  :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                        
                        .. attribute:: precedences
                        
                        	TOS Precedence value(s)
                        	**type**\:  :py:class:`Precedences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences>`
                        
                        .. attribute:: rate
                        
                        	Configured rate value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow, self).__init__()

                            self.yang_name = "flow"
                            self.yang_parent_name = "flows"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['flow_type']
                            self._child_classes = OrderedDict([("precedences", ("precedences", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences))])
                            self._leafs = OrderedDict([
                                ('flow_type', (YLeaf(YType.enumeration, 'flow-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow', '')])),
                                ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                            ])
                            self.flow_type = None
                            self.rate = None

                            self.precedences = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences()
                            self.precedences.parent = self
                            self._children_name_map["precedences"] = "precedences"
                            self._segment_path = lambda: "flow" + "[flow-type='" + str(self.flow_type) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow, ['flow_type', 'rate'], name, value)


                        class Precedences(Entity):
                            """
                            TOS Precedence value(s)
                            
                            .. attribute:: precedence
                            
                            	Precedence values
                            	**type**\: union of the below types:
                            
                            		**type**\: list of   :py:class:`LptsPreIFibPrecedenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumber>`
                            
                            		**type**\: list of int
                            
                            			**range:** 0..7
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences, self).__init__()

                                self.yang_name = "precedences"
                                self.yang_parent_name = "flow"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('precedence', (YLeafList(YType.str, 'precedence'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPreIFibPrecedenceNumber', ''),'int'])),
                                ])
                                self.precedence = []
                                self._segment_path = lambda: "precedences"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences, ['precedence'], name, value)

    def clone_ptr(self):
        self._top_entity = ActiveNodes()
        return self._top_entity

class PreconfiguredNodes(Entity):
    """
    preconfigured nodes
    
    .. attribute:: preconfigured_node
    
    	The configuration for a non\-active node
    	**type**\: list of  		 :py:class:`PreconfiguredNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode>`
    
    

    """

    _prefix = 'config-mda-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(PreconfiguredNodes, self).__init__()
        self._top_entity = None

        self.yang_name = "preconfigured-nodes"
        self.yang_parent_name = "Cisco-IOS-XR-config-mda-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("preconfigured-node", ("preconfigured_node", PreconfiguredNodes.PreconfiguredNode))])
        self._leafs = OrderedDict()

        self.preconfigured_node = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-config-mda-cfg:preconfigured-nodes"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PreconfiguredNodes, [], name, value)


    class PreconfiguredNode(Entity):
        """
        The configuration for a non\-active node
        
        .. attribute:: node_name  (key)
        
        	The identifier for this node
        	**type**\: str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: watchdog_node_threshold
        
        	watchdog node threshold
        	**type**\:  :py:class:`WatchdogNodeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.WatchdogNodeThreshold>`
        
        .. attribute:: ltrace
        
        	Ltrace Memory configuration
        	**type**\:  :py:class:`Ltrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.Ltrace>`
        
        .. attribute:: clock_interface
        
        	Configuration for a clock interface
        	**type**\:  :py:class:`ClockInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface>`
        
        .. attribute:: lpts_local
        
        	lpts node specific configuration commands
        	**type**\:  :py:class:`LptsLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal>`
        
        

        """

        _prefix = 'config-mda-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(PreconfiguredNodes.PreconfiguredNode, self).__init__()

            self.yang_name = "preconfigured-node"
            self.yang_parent_name = "preconfigured-nodes"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['node_name']
            self._child_classes = OrderedDict([("Cisco-IOS-XR-watchd-cfg:watchdog-node-threshold", ("watchdog_node_threshold", PreconfiguredNodes.PreconfiguredNode.WatchdogNodeThreshold)), ("Cisco-IOS-XR-infra-ltrace-cfg:ltrace", ("ltrace", PreconfiguredNodes.PreconfiguredNode.Ltrace)), ("Cisco-IOS-XR-freqsync-cfg:clock-interface", ("clock_interface", PreconfiguredNodes.PreconfiguredNode.ClockInterface)), ("Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local", ("lpts_local", PreconfiguredNodes.PreconfiguredNode.LptsLocal))])
            self._leafs = OrderedDict([
                ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
            ])
            self.node_name = None

            self.watchdog_node_threshold = PreconfiguredNodes.PreconfiguredNode.WatchdogNodeThreshold()
            self.watchdog_node_threshold.parent = self
            self._children_name_map["watchdog_node_threshold"] = "Cisco-IOS-XR-watchd-cfg:watchdog-node-threshold"

            self.ltrace = PreconfiguredNodes.PreconfiguredNode.Ltrace()
            self.ltrace.parent = self
            self._children_name_map["ltrace"] = "Cisco-IOS-XR-infra-ltrace-cfg:ltrace"

            self.clock_interface = PreconfiguredNodes.PreconfiguredNode.ClockInterface()
            self.clock_interface.parent = self
            self._children_name_map["clock_interface"] = "Cisco-IOS-XR-freqsync-cfg:clock-interface"

            self.lpts_local = PreconfiguredNodes.PreconfiguredNode.LptsLocal()
            self.lpts_local.parent = self
            self._children_name_map["lpts_local"] = "Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local"
            self._segment_path = lambda: "preconfigured-node" + "[node-name='" + str(self.node_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-config-mda-cfg:preconfigured-nodes/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode, [u'node_name'], name, value)


        class WatchdogNodeThreshold(Entity):
            """
            watchdog node threshold
            
            .. attribute:: disk_threshold
            
            	Disk thresholds
            	**type**\:  :py:class:`DiskThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.WatchdogNodeThreshold.DiskThreshold>`
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\:  :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.WatchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'watchd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(PreconfiguredNodes.PreconfiguredNode.WatchdogNodeThreshold, self).__init__()

                self.yang_name = "watchdog-node-threshold"
                self.yang_parent_name = "preconfigured-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("disk-threshold", ("disk_threshold", PreconfiguredNodes.PreconfiguredNode.WatchdogNodeThreshold.DiskThreshold)), ("memory-threshold", ("memory_threshold", PreconfiguredNodes.PreconfiguredNode.WatchdogNodeThreshold.MemoryThreshold))])
                self._leafs = OrderedDict()

                self.disk_threshold = PreconfiguredNodes.PreconfiguredNode.WatchdogNodeThreshold.DiskThreshold()
                self.disk_threshold.parent = self
                self._children_name_map["disk_threshold"] = "disk-threshold"

                self.memory_threshold = PreconfiguredNodes.PreconfiguredNode.WatchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self
                self._children_name_map["memory_threshold"] = "memory-threshold"
                self._segment_path = lambda: "Cisco-IOS-XR-watchd-cfg:watchdog-node-threshold"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.WatchdogNodeThreshold, [], name, value)


            class DiskThreshold(Entity):
                """
                Disk thresholds
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\: int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\: int
                
                	**range:** 4..40
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\: int
                
                	**range:** 3..40
                
                

                """

                _prefix = 'watchd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.WatchdogNodeThreshold.DiskThreshold, self).__init__()

                    self.yang_name = "disk-threshold"
                    self.yang_parent_name = "watchdog-node-threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('minor', (YLeaf(YType.uint32, 'minor'), ['int'])),
                        ('severe', (YLeaf(YType.uint32, 'severe'), ['int'])),
                        ('critical', (YLeaf(YType.uint32, 'critical'), ['int'])),
                    ])
                    self.minor = None
                    self.severe = None
                    self.critical = None
                    self._segment_path = lambda: "disk-threshold"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.WatchdogNodeThreshold.DiskThreshold, ['minor', 'severe', 'critical'], name, value)


            class MemoryThreshold(Entity):
                """
                Memory thresholds
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\: int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\: int
                
                	**range:** 4..40
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\: int
                
                	**range:** 3..40
                
                

                """

                _prefix = 'watchd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.WatchdogNodeThreshold.MemoryThreshold, self).__init__()

                    self.yang_name = "memory-threshold"
                    self.yang_parent_name = "watchdog-node-threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('minor', (YLeaf(YType.uint32, 'minor'), ['int'])),
                        ('severe', (YLeaf(YType.uint32, 'severe'), ['int'])),
                        ('critical', (YLeaf(YType.uint32, 'critical'), ['int'])),
                    ])
                    self.minor = None
                    self.severe = None
                    self.critical = None
                    self._segment_path = lambda: "memory-threshold"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.WatchdogNodeThreshold.MemoryThreshold, ['minor', 'severe', 'critical'], name, value)


        class Ltrace(Entity):
            """
            Ltrace Memory configuration
            
            .. attribute:: allocation_params
            
            	Select Ltrace mode and scale\-factor
            	**type**\:  :py:class:`AllocationParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams>`
            
            

            """

            _prefix = 'infra-ltrace-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(PreconfiguredNodes.PreconfiguredNode.Ltrace, self).__init__()

                self.yang_name = "ltrace"
                self.yang_parent_name = "preconfigured-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("allocation-params", ("allocation_params", PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams))])
                self._leafs = OrderedDict()

                self.allocation_params = PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams()
                self.allocation_params.parent = self
                self._children_name_map["allocation_params"] = "allocation-params"
                self._segment_path = lambda: "Cisco-IOS-XR-infra-ltrace-cfg:ltrace"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.Ltrace, [], name, value)


            class AllocationParams(Entity):
                """
                Select Ltrace mode and scale\-factor
                
                .. attribute:: mode
                
                	Select an allocation mode (static\:1, dynamic \:2)
                	**type**\:  :py:class:`InfraLtraceMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceMode>`
                
                .. attribute:: scale_factor
                
                	Select a scaling down factor
                	**type**\:  :py:class:`InfraLtraceScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceScale>`
                
                

                """

                _prefix = 'infra-ltrace-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams, self).__init__()

                    self.yang_name = "allocation-params"
                    self.yang_parent_name = "ltrace"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg', 'InfraLtraceMode', '')])),
                        ('scale_factor', (YLeaf(YType.enumeration, 'scale-factor'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg', 'InfraLtraceScale', '')])),
                    ])
                    self.mode = None
                    self.scale_factor = None
                    self._segment_path = lambda: "allocation-params"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams, ['mode', 'scale_factor'], name, value)


        class ClockInterface(Entity):
            """
            Configuration for a clock interface
            
            .. attribute:: clocks
            
            	Configuration for a clock interface
            	**type**\:  :py:class:`Clocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks>`
            
            

            """

            _prefix = 'freqsync-cfg'
            _revision = '2017-09-30'

            def __init__(self):
                super(PreconfiguredNodes.PreconfiguredNode.ClockInterface, self).__init__()

                self.yang_name = "clock-interface"
                self.yang_parent_name = "preconfigured-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("clocks", ("clocks", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks))])
                self._leafs = OrderedDict()

                self.clocks = PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks()
                self.clocks.parent = self
                self._children_name_map["clocks"] = "clocks"
                self._segment_path = lambda: "Cisco-IOS-XR-freqsync-cfg:clock-interface"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface, [], name, value)


            class Clocks(Entity):
                """
                Configuration for a clock interface
                
                .. attribute:: clock
                
                	Configuration for a clock interface
                	**type**\: list of  		 :py:class:`Clock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock>`
                
                

                """

                _prefix = 'freqsync-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks, self).__init__()

                    self.yang_name = "clocks"
                    self.yang_parent_name = "clock-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("clock", ("clock", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock))])
                    self._leafs = OrderedDict()

                    self.clock = YList(self)
                    self._segment_path = lambda: "clocks"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks, [], name, value)


                class Clock(Entity):
                    """
                    Configuration for a clock interface
                    
                    .. attribute:: clock_type  (key)
                    
                    	Clock type
                    	**type**\:  :py:class:`FsyncClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncClock>`
                    
                    .. attribute:: port  (key)
                    
                    	Clock port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: frequency_synchronization
                    
                    	Frequency Synchronization clock configuraiton
                    	**type**\:  :py:class:`FrequencySynchronization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization>`
                    
                    .. attribute:: sync_controller
                    
                    	sync\-controller value
                    	**type**\:  :py:class:`SyncController <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController>`
                    
                    

                    """

                    _prefix = 'freqsync-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock, self).__init__()

                        self.yang_name = "clock"
                        self.yang_parent_name = "clocks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['clock_type','port']
                        self._child_classes = OrderedDict([("frequency-synchronization", ("frequency_synchronization", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization)), ("Cisco-IOS-XR-syncc-controller-cfg:sync-controller", ("sync_controller", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController))])
                        self._leafs = OrderedDict([
                            ('clock_type', (YLeaf(YType.enumeration, 'clock-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncClock', '')])),
                            ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                        ])
                        self.clock_type = None
                        self.port = None

                        self.frequency_synchronization = PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization()
                        self.frequency_synchronization.parent = self
                        self._children_name_map["frequency_synchronization"] = "frequency-synchronization"

                        self.sync_controller = PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController()
                        self.sync_controller.parent = self
                        self._children_name_map["sync_controller"] = "Cisco-IOS-XR-syncc-controller-cfg:sync-controller"
                        self._segment_path = lambda: "clock" + "[clock-type='" + str(self.clock_type) + "']" + "[port='" + str(self.port) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock, ['clock_type', 'port'], name, value)


                    class FrequencySynchronization(Entity):
                        """
                        Frequency Synchronization clock configuraiton
                        
                        .. attribute:: output_quality_level
                        
                        	Set the output quality level
                        	**type**\:  :py:class:`OutputQualityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel>`
                        
                        .. attribute:: input_quality_level
                        
                        	Set the input quality level
                        	**type**\:  :py:class:`InputQualityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel>`
                        
                        .. attribute:: wait_to_restore_time
                        
                        	Set the wait\-to\-restore time for this source
                        	**type**\: int
                        
                        	**range:** 0..12
                        
                        	**default value**\: 5
                        
                        .. attribute:: priority
                        
                        	Set the priority of this source
                        	**type**\: int
                        
                        	**range:** 1..254
                        
                        	**default value**\: 100
                        
                        .. attribute:: selection_input
                        
                        	Assign this source as a selection input
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: time_of_day_priority
                        
                        	Set the time\-of\-day priority of this source
                        	**type**\: int
                        
                        	**range:** 1..254
                        
                        	**default value**\: 100
                        
                        .. attribute:: ssm_disable
                        
                        	Disable SSM on this source
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'freqsync-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization, self).__init__()

                            self.yang_name = "frequency-synchronization"
                            self.yang_parent_name = "clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("output-quality-level", ("output_quality_level", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel)), ("input-quality-level", ("input_quality_level", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel))])
                            self._leafs = OrderedDict([
                                ('wait_to_restore_time', (YLeaf(YType.uint32, 'wait-to-restore-time'), ['int'])),
                                ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                ('selection_input', (YLeaf(YType.empty, 'selection-input'), ['Empty'])),
                                ('time_of_day_priority', (YLeaf(YType.uint32, 'time-of-day-priority'), ['int'])),
                                ('ssm_disable', (YLeaf(YType.empty, 'ssm-disable'), ['Empty'])),
                            ])
                            self.wait_to_restore_time = None
                            self.priority = None
                            self.selection_input = None
                            self.time_of_day_priority = None
                            self.ssm_disable = None

                            self.output_quality_level = PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel()
                            self.output_quality_level.parent = self
                            self._children_name_map["output_quality_level"] = "output-quality-level"

                            self.input_quality_level = PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel()
                            self.input_quality_level.parent = self
                            self._children_name_map["input_quality_level"] = "input-quality-level"
                            self._segment_path = lambda: "frequency-synchronization"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization, ['wait_to_restore_time', 'priority', 'selection_input', 'time_of_day_priority', 'ssm_disable'], name, value)


                        class OutputQualityLevel(Entity):
                            """
                            Set the output quality level
                            
                            .. attribute:: quality_level_option
                            
                            	Quality level option
                            	**type**\:  :py:class:`FsyncQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlOption>`
                            
                            .. attribute:: exact_quality_level_value
                            
                            	Exact quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: min_quality_level_value
                            
                            	Minimum quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: max_quality_level_value
                            
                            	Maximum quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            

                            """

                            _prefix = 'freqsync-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel, self).__init__()

                                self.yang_name = "output-quality-level"
                                self.yang_parent_name = "frequency-synchronization"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlOption', '')])),
                                    ('exact_quality_level_value', (YLeaf(YType.enumeration, 'exact-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                    ('min_quality_level_value', (YLeaf(YType.enumeration, 'min-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                    ('max_quality_level_value', (YLeaf(YType.enumeration, 'max-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                ])
                                self.quality_level_option = None
                                self.exact_quality_level_value = None
                                self.min_quality_level_value = None
                                self.max_quality_level_value = None
                                self._segment_path = lambda: "output-quality-level"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel, ['quality_level_option', 'exact_quality_level_value', 'min_quality_level_value', 'max_quality_level_value'], name, value)


                        class InputQualityLevel(Entity):
                            """
                            Set the input quality level
                            
                            .. attribute:: quality_level_option
                            
                            	Quality level option
                            	**type**\:  :py:class:`FsyncQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlOption>`
                            
                            .. attribute:: exact_quality_level_value
                            
                            	Exact quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: min_quality_level_value
                            
                            	Minimum quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: max_quality_level_value
                            
                            	Maximum quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            

                            """

                            _prefix = 'freqsync-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel, self).__init__()

                                self.yang_name = "input-quality-level"
                                self.yang_parent_name = "frequency-synchronization"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlOption', '')])),
                                    ('exact_quality_level_value', (YLeaf(YType.enumeration, 'exact-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                    ('min_quality_level_value', (YLeaf(YType.enumeration, 'min-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                    ('max_quality_level_value', (YLeaf(YType.enumeration, 'max-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                ])
                                self.quality_level_option = None
                                self.exact_quality_level_value = None
                                self.min_quality_level_value = None
                                self.max_quality_level_value = None
                                self._segment_path = lambda: "input-quality-level"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel, ['quality_level_option', 'exact_quality_level_value', 'min_quality_level_value', 'max_quality_level_value'], name, value)


                    class SyncController(Entity):
                        """
                        sync\-controller value
                        
                        .. attribute:: transport_mode
                        
                        	Transport mode
                        	**type**\:  :py:class:`TransportMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController.TransportMode>`
                        
                        

                        """

                        _prefix = 'syncc-controller-cfg'
                        _revision = '2017-06-22'

                        def __init__(self):
                            super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController, self).__init__()

                            self.yang_name = "sync-controller"
                            self.yang_parent_name = "clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("transport-mode", ("transport_mode", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController.TransportMode))])
                            self._leafs = OrderedDict()

                            self.transport_mode = PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController.TransportMode()
                            self.transport_mode.parent = self
                            self._children_name_map["transport_mode"] = "transport-mode"
                            self._segment_path = lambda: "Cisco-IOS-XR-syncc-controller-cfg:sync-controller"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController, [], name, value)


                        class TransportMode(Entity):
                            """
                            Transport mode
                            
                            .. attribute:: frequency_mode
                            
                            	Frequency Mode
                            	**type**\:  :py:class:`FrequencyMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController.TransportMode.FrequencyMode>`
                            
                            

                            """

                            _prefix = 'syncc-controller-cfg'
                            _revision = '2017-06-22'

                            def __init__(self):
                                super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController.TransportMode, self).__init__()

                                self.yang_name = "transport-mode"
                                self.yang_parent_name = "sync-controller"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("frequency-mode", ("frequency_mode", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController.TransportMode.FrequencyMode))])
                                self._leafs = OrderedDict()

                                self.frequency_mode = PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController.TransportMode.FrequencyMode()
                                self.frequency_mode.parent = self
                                self._children_name_map["frequency_mode"] = "frequency-mode"
                                self._segment_path = lambda: "transport-mode"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController.TransportMode, [], name, value)


                            class FrequencyMode(Entity):
                                """
                                Frequency Mode
                                
                                .. attribute:: port_mode
                                
                                	clock\-interface sync <value> location <value> port\-parameters bits\-input 2m \-> Option1=0, Option2=2, Option3=0, Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-input 2m \-> Option1=0, Option2=2, Option3=0, Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-input 64k\-input\-only \-> Option1=0, Option2=3, Option3=0, Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa4 ami \-> Option1=0, Option2=1, Option3=1, Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa4 hdb3 \-> Option1=0, Option2=1, Option3=1, Option4=0 , Option5=1 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa5 ami \-> Option1=0, Option2=1, Option3=1, Option4=0, Option5=1 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa5 hdb3 \-> Option1=0, Option2=1, Option3=1, Option4=1 , Option5=1 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa6 ami \-> Option1=0, Option2=1, Option3=1, Option4=0, Option5=2 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa6 hdb3 \-> Option1=0, Option2=1, Option3=1, Option4=1 , Option5=2 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa7 ami \-> Option1=0, Option2=1, Option3=1, Option4=0, Option5=3 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa7 hdb3 \-> Option1=0, Option2=1, Option3=1, Option4=1 , Option5=3 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa8 ami \-> Option1=0, Option2=1, Option3=1, Option4=0, Option5=4 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 crc\-4 sa8 hdb3 \-> Option1=0, Option2=1, Option3=1, Option4=1 , Option5=4 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 non\-crc\-4 ami \-> Option1=0, Option2=1, Option3=0, Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-input e1 non\-crc\-4 hdb3 \-> Option1=0, Option2=1, Option3=0, Option4=1 , Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-input t1 d4 ami \-> Option1=0, Option2=0, Option3=1, Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-input t1 d4 b8zs \-> Option1=0, Option2=0 , Option3=1, Option4=1, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-input t1 esf ami \-> Option1=0, Option2=0, Option3=0, Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-input t1 esf b8zs \-> Option1=0, Option2=0, Option3=0, Option4=1, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output 2m \-> Option1=1 , Option2=2, Option3=0, Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output 6m\-output\-only \-> Option1=1 , Option2=4, Option3=0 , Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa4 ami \-> Option1=1 , Option2=1, Option3=1 , Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa4 hdb3 \-> Option1=1 , Option2=1, Option3=1 , Option4=1, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa5 ami \-> Option1=1 , Option2=1, Option3=1 , Option4=0, Option5=1 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa5 hdb3 \-> Option1=1 , Option2=1, Option3=1 , Option4=1, Option5=1 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa6 ami \-> Option1=1 , Option2=1, Option3=1 , Option4=0, Option5=2 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa6 hdb3 \-> Option1=1 , Option2=1, Option3=1 , Option4=1, Option5=2 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa7 ami \-> Option1=1 , Option2=1, Option3=1 , Option4=0, Option5=3 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa7 hdb3 \-> Option1=1 , Option2=1, Option3=1 , Option4=1, Option5=3 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa8 ami \-> Option1=1 , Option2=1, Option3=1 , Option4=0, Option5=4 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 crc\-4 sa8 hdb3 \-> Option1=1 , Option2=1, Option3=1 , Option4=1, Option5=4 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 non\-crc\-4 ami \-> Option1=1 , Option2=1, Option3=0 , Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output e1 non\-crc\-4 hdb3 \-> Option1=1 , Option2=1, Option3=0 , Option4=1, Option5=0clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 ami 0 \-> Option1=1 , Option2=0, Option3=1 , Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 ami 1 \-> Option1=1 , Option2=0, Option3=1 , Option4=0, Option5=1 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 ami 2 \-> Option1=1 , Option2=0, Option3=1 , Option4=0, Option5=2 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 ami 3 \-> Option1=1 , Option2=0, Option3=1 , Option4=0, Option5=3 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 ami 4 \-> Option1=1 , Option2=0, Option3=1 , Option4=0, Option5=4 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 b8zs 0 \-> Option1=1 , Option2=0, Option3=1 , Option4=1, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 b8zs 1 \-> Option1=1 , Option2=0, Option3=1 , Option4=1, Option5=1 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 b8zs 2 \-> Option1=1 , Option2=0, Option3=1 , Option4=1, Option5=2 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 b8zs 3 \-> Option1=1 , Option2=0, Option3=1 , Option4=1, Option5=3 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 d4 b8zs 4 \-> Option1=1 , Option2=0, Option3=1 , Option4=1, Option5=4 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf ami 0 \-> Option1=1 , Option2=0, Option3=0 , Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf ami 1 \-> Option1=1 , Option2=0, Option3=0 , Option4=0, Option5=1 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf ami 2 \-> Option1=1 , Option2=0, Option3=0 , Option4=0, Option5=2 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf ami 3 \-> Option1=1 , Option2=0, Option3=0 , Option4=0, Option5=3 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf ami 4 \-> Option1=1 , Option2=0, Option3=0 , Option4=0, Option5=4 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf b8zs 0 \-> Option1=1 , Option2=0, Option3=0 , Option4=1, Option5=0 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf b8zs 1 \-> Option1=1 , Option2=0, Option3=0 , Option4=1, Option5=1 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf b8zs 2 \-> Option1=1 , Option2=0, Option3=0 , Option4=1, Option5=2 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf b8zs 3 \-> Option1=1 , Option2=0, Option3=0 , Option4=1, Option5=3 clock\-interface sync <value> location <value> port\-parameters bits\-output t1 esf b8zs 4 \-> Option1=1 , Option2=0, Option3=0 , Option4=1, Option5=4 clock\-interface sync <value> location <value> port\-parameters port\-parameters uti \-> Option1=2 , Option2=0, Option3=0 , Option4=0, Option5=0 clock\-interface sync <value> location <value> port\-parameters port\-parameters gps\-input \-> Option1=3, Option2=0, Option3=0 , Option4=0, Option5=0 
                                	**type**\:  :py:class:`PortMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController.TransportMode.FrequencyMode.PortMode>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: shutdown
                                
                                	Disable the SyncE Port
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'syncc-controller-cfg'
                                _revision = '2017-06-22'

                                def __init__(self):
                                    super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController.TransportMode.FrequencyMode, self).__init__()

                                    self.yang_name = "frequency-mode"
                                    self.yang_parent_name = "transport-mode"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("port-mode", ("port_mode", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController.TransportMode.FrequencyMode.PortMode))])
                                    self._leafs = OrderedDict([
                                        ('shutdown', (YLeaf(YType.empty, 'shutdown'), ['Empty'])),
                                    ])
                                    self.shutdown = None

                                    self.port_mode = None
                                    self._children_name_map["port_mode"] = "port-mode"
                                    self._segment_path = lambda: "frequency-mode"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController.TransportMode.FrequencyMode, ['shutdown'], name, value)


                                class PortMode(Entity):
                                    """
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input 2m \-> Option1=0,
                                    Option2=2, Option3=0, Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input 2m \-> Option1=0,
                                    Option2=2, Option3=0, Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input 64k\-input\-only \->
                                    Option1=0, Option2=3, Option3=0, Option4=0,
                                    Option5=0 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-input
                                    e1 crc\-4 sa4 ami \-> Option1=0, Option2=1,
                                    Option3=1, Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input e1 crc\-4 sa4 hdb3
                                    \-> Option1=0, Option2=1, Option3=1, Option4=0
                                    , Option5=1 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-input
                                    e1 crc\-4 sa5 ami \-> Option1=0, Option2=1,
                                    Option3=1, Option4=0, Option5=1
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input e1 crc\-4 sa5 hdb3
                                    \-> Option1=0, Option2=1, Option3=1, Option4=1
                                    , Option5=1 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-input
                                    e1 crc\-4 sa6 ami \-> Option1=0, Option2=1,
                                    Option3=1, Option4=0, Option5=2
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input e1 crc\-4 sa6 hdb3
                                    \-> Option1=0, Option2=1, Option3=1, Option4=1
                                    , Option5=2 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-input
                                    e1 crc\-4 sa7 ami \-> Option1=0, Option2=1,
                                    Option3=1, Option4=0, Option5=3
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input e1 crc\-4 sa7 hdb3
                                    \-> Option1=0, Option2=1, Option3=1, Option4=1
                                    , Option5=3 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-input
                                    e1 crc\-4 sa8 ami \-> Option1=0, Option2=1,
                                    Option3=1, Option4=0, Option5=4
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input e1 crc\-4 sa8 hdb3
                                    \-> Option1=0, Option2=1, Option3=1, Option4=1
                                    , Option5=4 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-input
                                    e1 non\-crc\-4 ami \-> Option1=0, Option2=1,
                                    Option3=0, Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input e1 non\-crc\-4 hdb3
                                    \-> Option1=0, Option2=1, Option3=0, Option4=1
                                    , Option5=0 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-input
                                    t1 d4 ami \-> Option1=0, Option2=0, Option3=1,
                                    Option4=0, Option5=0 clock\-interface sync
                                    <value> location <value> port\-parameters
                                    bits\-input t1 d4 b8zs \-> Option1=0, Option2=0
                                    , Option3=1, Option4=1, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-input t1 esf ami \->
                                    Option1=0, Option2=0, Option3=0, Option4=0,
                                    Option5=0 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-input
                                    t1 esf b8zs \-> Option1=0, Option2=0,
                                    Option3=0, Option4=1, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output 2m \-> Option1=1 ,
                                    Option2=2, Option3=0, Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output 6m\-output\-only \->
                                    Option1=1 , Option2=4, Option3=0 , Option4=0,
                                    Option5=0 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    e1 crc\-4 sa4 ami \-> Option1=1 , Option2=1,
                                    Option3=1 , Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output e1 crc\-4 sa4 hdb3
                                    \-> Option1=1 , Option2=1, Option3=1 ,
                                    Option4=1, Option5=0 clock\-interface sync
                                    <value> location <value> port\-parameters
                                    bits\-output e1 crc\-4 sa5 ami \-> Option1=1 ,
                                    Option2=1, Option3=1 , Option4=0, Option5=1
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output e1 crc\-4 sa5 hdb3
                                    \-> Option1=1 , Option2=1, Option3=1 ,
                                    Option4=1, Option5=1 clock\-interface sync
                                    <value> location <value> port\-parameters
                                    bits\-output e1 crc\-4 sa6 ami \-> Option1=1 ,
                                    Option2=1, Option3=1 , Option4=0, Option5=2
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output e1 crc\-4 sa6 hdb3
                                    \-> Option1=1 , Option2=1, Option3=1 ,
                                    Option4=1, Option5=2 clock\-interface sync
                                    <value> location <value> port\-parameters
                                    bits\-output e1 crc\-4 sa7 ami \-> Option1=1 ,
                                    Option2=1, Option3=1 , Option4=0, Option5=3
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output e1 crc\-4 sa7 hdb3
                                    \-> Option1=1 , Option2=1, Option3=1 ,
                                    Option4=1, Option5=3 clock\-interface sync
                                    <value> location <value> port\-parameters
                                    bits\-output e1 crc\-4 sa8 ami \-> Option1=1 ,
                                    Option2=1, Option3=1 , Option4=0, Option5=4
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output e1 crc\-4 sa8 hdb3
                                    \-> Option1=1 , Option2=1, Option3=1 ,
                                    Option4=1, Option5=4 clock\-interface sync
                                    <value> location <value> port\-parameters
                                    bits\-output e1 non\-crc\-4 ami \-> Option1=1 ,
                                    Option2=1, Option3=0 , Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output e1 non\-crc\-4 hdb3
                                    \-> Option1=1 , Option2=1, Option3=0 ,
                                    Option4=1, Option5=0clock\-interface sync
                                    <value> location <value> port\-parameters
                                    bits\-output t1 d4 ami 0 \-> Option1=1 ,
                                    Option2=0, Option3=1 , Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 d4 ami 1 \->
                                    Option1=1 , Option2=0, Option3=1 , Option4=0,
                                    Option5=1 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    t1 d4 ami 2 \-> Option1=1 , Option2=0,
                                    Option3=1 , Option4=0, Option5=2
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 d4 ami 3 \->
                                    Option1=1 , Option2=0, Option3=1 , Option4=0,
                                    Option5=3 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    t1 d4 ami 4 \-> Option1=1 , Option2=0,
                                    Option3=1 , Option4=0, Option5=4
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 d4 b8zs 0 \->
                                    Option1=1 , Option2=0, Option3=1 , Option4=1,
                                    Option5=0 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    t1 d4 b8zs 1 \-> Option1=1 , Option2=0,
                                    Option3=1 , Option4=1, Option5=1
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 d4 b8zs 2 \->
                                    Option1=1 , Option2=0, Option3=1 , Option4=1,
                                    Option5=2 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    t1 d4 b8zs 3 \-> Option1=1 , Option2=0,
                                    Option3=1 , Option4=1, Option5=3
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 d4 b8zs 4 \->
                                    Option1=1 , Option2=0, Option3=1 , Option4=1,
                                    Option5=4 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    t1 esf ami 0 \-> Option1=1 , Option2=0,
                                    Option3=0 , Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 esf ami 1 \->
                                    Option1=1 , Option2=0, Option3=0 , Option4=0,
                                    Option5=1 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    t1 esf ami 2 \-> Option1=1 , Option2=0,
                                    Option3=0 , Option4=0, Option5=2
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 esf ami 3 \->
                                    Option1=1 , Option2=0, Option3=0 , Option4=0,
                                    Option5=3 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    t1 esf ami 4 \-> Option1=1 , Option2=0,
                                    Option3=0 , Option4=0, Option5=4
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 esf b8zs 0 \->
                                    Option1=1 , Option2=0, Option3=0 , Option4=1,
                                    Option5=0 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    t1 esf b8zs 1 \-> Option1=1 , Option2=0,
                                    Option3=0 , Option4=1, Option5=1
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 esf b8zs 2 \->
                                    Option1=1 , Option2=0, Option3=0 , Option4=1,
                                    Option5=2 clock\-interface sync <value>
                                    location <value> port\-parameters bits\-output
                                    t1 esf b8zs 3 \-> Option1=1 , Option2=0,
                                    Option3=0 , Option4=1, Option5=3
                                    clock\-interface sync <value> location <value>
                                    port\-parameters bits\-output t1 esf b8zs 4 \->
                                    Option1=1 , Option2=0, Option3=0 , Option4=1,
                                    Option5=4 clock\-interface sync <value>
                                    location <value> port\-parameters
                                    port\-parameters uti \-> Option1=2 , Option2=0,
                                    Option3=0 , Option4=0, Option5=0
                                    clock\-interface sync <value> location <value>
                                    port\-parameters port\-parameters gps\-input \->
                                    Option1=3, Option2=0, Option3=0 , Option4=0,
                                    Option5=0 
                                    
                                    .. attribute:: option1
                                    
                                    	Option value #1
                                    	**type**\: int
                                    
                                    	**range:** 0..3
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: option2
                                    
                                    	Option value #2
                                    	**type**\: int
                                    
                                    	**range:** 0..4
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: option3
                                    
                                    	Option value #3
                                    	**type**\: int
                                    
                                    	**range:** 0..1
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: option4
                                    
                                    	Option value #4
                                    	**type**\: int
                                    
                                    	**range:** 0..1
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: option5
                                    
                                    	Option value #5
                                    	**type**\: int
                                    
                                    	**range:** 0..4
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'syncc-controller-cfg'
                                    _revision = '2017-06-22'

                                    def __init__(self):
                                        super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController.TransportMode.FrequencyMode.PortMode, self).__init__()

                                        self.yang_name = "port-mode"
                                        self.yang_parent_name = "frequency-mode"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('option1', (YLeaf(YType.uint32, 'option1'), ['int'])),
                                            ('option2', (YLeaf(YType.uint32, 'option2'), ['int'])),
                                            ('option3', (YLeaf(YType.uint32, 'option3'), ['int'])),
                                            ('option4', (YLeaf(YType.uint32, 'option4'), ['int'])),
                                            ('option5', (YLeaf(YType.uint32, 'option5'), ['int'])),
                                        ])
                                        self.option1 = None
                                        self.option2 = None
                                        self.option3 = None
                                        self.option4 = None
                                        self.option5 = None
                                        self._segment_path = lambda: "port-mode"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.SyncController.TransportMode.FrequencyMode.PortMode, ['option1', 'option2', 'option3', 'option4', 'option5'], name, value)


        class LptsLocal(Entity):
            """
            lpts node specific configuration commands
            
            .. attribute:: ipolicer_local_tables
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:  :py:class:`IpolicerLocalTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables>`
            
            .. attribute:: dynamic_flows_tables
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:  :py:class:`DynamicFlowsTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables>`
            
            .. attribute:: ipolicer_local
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:  :py:class:`IpolicerLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal, self).__init__()

                self.yang_name = "lpts-local"
                self.yang_parent_name = "preconfigured-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ipolicer-local-tables", ("ipolicer_local_tables", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables)), ("dynamic-flows-tables", ("dynamic_flows_tables", PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables)), ("ipolicer-local", ("ipolicer_local", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal))])
                self._leafs = OrderedDict()

                self.ipolicer_local_tables = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables()
                self.ipolicer_local_tables.parent = self
                self._children_name_map["ipolicer_local_tables"] = "ipolicer-local-tables"

                self.dynamic_flows_tables = PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables()
                self.dynamic_flows_tables.parent = self
                self._children_name_map["dynamic_flows_tables"] = "dynamic-flows-tables"

                self.ipolicer_local = None
                self._children_name_map["ipolicer_local"] = "ipolicer-local"
                self._segment_path = lambda: "Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal, [], name, value)


            class IpolicerLocalTables(Entity):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: ipolicer_local_table
                
                	Pre IFIB (Internal Forwarding Information Base) configuration table
                	**type**\: list of  		 :py:class:`IpolicerLocalTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables, self).__init__()

                    self.yang_name = "ipolicer-local-tables"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ipolicer-local-table", ("ipolicer_local_table", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable))])
                    self._leafs = OrderedDict()

                    self.ipolicer_local_table = YList(self)
                    self._segment_path = lambda: "ipolicer-local-tables"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables, [], name, value)


                class IpolicerLocalTable(Entity):
                    """
                    Pre IFIB (Internal Forwarding Information
                    Base) configuration table
                    
                    .. attribute:: id1  (key)
                    
                    	none
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: np_flows
                    
                    	NP name
                    	**type**\:  :py:class:`NpFlows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable, self).__init__()

                        self.yang_name = "ipolicer-local-table"
                        self.yang_parent_name = "ipolicer-local-tables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['id1']
                        self._child_classes = OrderedDict([("np-flows", ("np_flows", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows))])
                        self._leafs = OrderedDict([
                            ('id1', (YLeaf(YType.str, 'id1'), ['str'])),
                        ])
                        self.id1 = None

                        self.np_flows = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows()
                        self.np_flows.parent = self
                        self._children_name_map["np_flows"] = "np-flows"
                        self._segment_path = lambda: "ipolicer-local-table" + "[id1='" + str(self.id1) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable, ['id1'], name, value)


                    class NpFlows(Entity):
                        """
                        NP name
                        
                        .. attribute:: np_flow
                        
                        	Table of NP Flow names
                        	**type**\: list of  		 :py:class:`NpFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows.NpFlow>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows, self).__init__()

                            self.yang_name = "np-flows"
                            self.yang_parent_name = "ipolicer-local-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("np-flow", ("np_flow", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows.NpFlow))])
                            self._leafs = OrderedDict()

                            self.np_flow = YList(self)
                            self._segment_path = lambda: "np-flows"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows, [], name, value)


                        class NpFlow(Entity):
                            """
                            Table of NP Flow names
                            
                            .. attribute:: flow_type  (key)
                            
                            	LPTS Flow Type
                            	**type**\:  :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                            
                            .. attribute:: np_rate
                            
                            	Configured rate value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows.NpFlow, self).__init__()

                                self.yang_name = "np-flow"
                                self.yang_parent_name = "np-flows"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['flow_type']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('flow_type', (YLeaf(YType.enumeration, 'flow-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow', '')])),
                                    ('np_rate', (YLeaf(YType.uint32, 'np-rate'), ['int'])),
                                ])
                                self.flow_type = None
                                self.np_rate = None
                                self._segment_path = lambda: "np-flow" + "[flow-type='" + str(self.flow_type) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows.NpFlow, ['flow_type', 'np_rate'], name, value)


            class DynamicFlowsTables(Entity):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: dynamic_flows_table
                
                	Table for Dynamic Flows
                	**type**\: list of  		 :py:class:`DynamicFlowsTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables, self).__init__()

                    self.yang_name = "dynamic-flows-tables"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("dynamic-flows-table", ("dynamic_flows_table", PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable))])
                    self._leafs = OrderedDict()

                    self.dynamic_flows_table = YList(self)
                    self._segment_path = lambda: "dynamic-flows-tables"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables, [], name, value)


                class DynamicFlowsTable(Entity):
                    """
                    Table for Dynamic Flows
                    
                    .. attribute:: table_type  (key)
                    
                    	LPTS Dynamic Flows Table Type
                    	**type**\:  :py:class:`LptsDynamicFlowConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsDynamicFlowConfig>`
                    
                    .. attribute:: flow_type
                    
                    	Selected flow type
                    	**type**\: list of  		 :py:class:`FlowType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable, self).__init__()

                        self.yang_name = "dynamic-flows-table"
                        self.yang_parent_name = "dynamic-flows-tables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['table_type']
                        self._child_classes = OrderedDict([("flow-type", ("flow_type", PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType))])
                        self._leafs = OrderedDict([
                            ('table_type', (YLeaf(YType.enumeration, 'table-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsDynamicFlowConfig', '')])),
                        ])
                        self.table_type = None

                        self.flow_type = YList(self)
                        self._segment_path = lambda: "dynamic-flows-table" + "[table-type='" + str(self.table_type) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable, ['table_type'], name, value)


                    class FlowType(Entity):
                        """
                        Selected flow type
                        
                        .. attribute:: flow_type  (key)
                        
                        	LPTS Flow Type
                        	**type**\:  :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                        
                        .. attribute:: max
                        
                        	Configured Max TCAM value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType, self).__init__()

                            self.yang_name = "flow-type"
                            self.yang_parent_name = "dynamic-flows-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['flow_type']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('flow_type', (YLeaf(YType.enumeration, 'flow-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow', '')])),
                                ('max', (YLeaf(YType.uint32, 'max'), ['int'])),
                            ])
                            self.flow_type = None
                            self.max = None
                            self._segment_path = lambda: "flow-type" + "[flow-type='" + str(self.flow_type) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType, ['flow_type', 'max'], name, value)


            class IpolicerLocal(Entity):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: enable
                
                	Enabled
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: flows
                
                	Table for Flows
                	**type**\:  :py:class:`Flows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal, self).__init__()

                    self.yang_name = "ipolicer-local"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("flows", ("flows", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows))])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.enable = None

                    self.flows = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows()
                    self.flows.parent = self
                    self._children_name_map["flows"] = "flows"
                    self._segment_path = lambda: "ipolicer-local"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal, ['enable'], name, value)


                class Flows(Entity):
                    """
                    Table for Flows
                    
                    .. attribute:: flow
                    
                    	selected flow type
                    	**type**\: list of  		 :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows, self).__init__()

                        self.yang_name = "flows"
                        self.yang_parent_name = "ipolicer-local"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("flow", ("flow", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow))])
                        self._leafs = OrderedDict()

                        self.flow = YList(self)
                        self._segment_path = lambda: "flows"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows, [], name, value)


                    class Flow(Entity):
                        """
                        selected flow type
                        
                        .. attribute:: flow_type  (key)
                        
                        	LPTS Flow Type
                        	**type**\:  :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                        
                        .. attribute:: precedences
                        
                        	TOS Precedence value(s)
                        	**type**\:  :py:class:`Precedences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences>`
                        
                        .. attribute:: rate
                        
                        	Configured rate value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow, self).__init__()

                            self.yang_name = "flow"
                            self.yang_parent_name = "flows"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['flow_type']
                            self._child_classes = OrderedDict([("precedences", ("precedences", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences))])
                            self._leafs = OrderedDict([
                                ('flow_type', (YLeaf(YType.enumeration, 'flow-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow', '')])),
                                ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                            ])
                            self.flow_type = None
                            self.rate = None

                            self.precedences = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences()
                            self.precedences.parent = self
                            self._children_name_map["precedences"] = "precedences"
                            self._segment_path = lambda: "flow" + "[flow-type='" + str(self.flow_type) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow, ['flow_type', 'rate'], name, value)


                        class Precedences(Entity):
                            """
                            TOS Precedence value(s)
                            
                            .. attribute:: precedence
                            
                            	Precedence values
                            	**type**\: union of the below types:
                            
                            		**type**\: list of   :py:class:`LptsPreIFibPrecedenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumber>`
                            
                            		**type**\: list of int
                            
                            			**range:** 0..7
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences, self).__init__()

                                self.yang_name = "precedences"
                                self.yang_parent_name = "flow"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('precedence', (YLeafList(YType.str, 'precedence'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPreIFibPrecedenceNumber', ''),'int'])),
                                ])
                                self.precedence = []
                                self._segment_path = lambda: "precedences"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences, ['precedence'], name, value)

    def clone_ptr(self):
        self._top_entity = PreconfiguredNodes()
        return self._top_entity

