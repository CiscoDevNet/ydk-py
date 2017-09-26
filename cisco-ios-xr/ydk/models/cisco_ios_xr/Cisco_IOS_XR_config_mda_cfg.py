""" Cisco_IOS_XR_config_mda_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR config\-mda package configuration.

This module contains definitions
for the following management objects\:
  active\-nodes\: Per\-node configuration for active nodes
  preconfigured\-nodes\: preconfigured nodes

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ActiveNodes(Entity):
    """
    Per\-node configuration for active nodes
    
    .. attribute:: active_node
    
    	The configuration for an active node
    	**type**\: list of    :py:class:`ActiveNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode>`
    
    

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
        self._child_container_classes = {}
        self._child_list_classes = {"active-node" : ("active_node", ActiveNodes.ActiveNode)}

        self.active_node = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-config-mda-cfg:active-nodes"

    def __setattr__(self, name, value):
        self._perform_setattr(ActiveNodes, [], name, value)


    class ActiveNode(Entity):
        """
        The configuration for an active node
        
        .. attribute:: node_name  <key>
        
        	The identifier for this node
        	**type**\:  str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: cisco_ios_xr_watchd_cfg_watchdog_node_threshold
        
        	watchdog node threshold
        	**type**\:   :py:class:`CiscoIOSXRWatchdCfgWatchdogNodeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold>`
        
        .. attribute:: cisco_ios_xr_wd_cfg_watchdog_node_threshold
        
        	Watchdog threshold configuration
        	**type**\:   :py:class:`CiscoIOSXRWdCfgWatchdogNodeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold>`
        
        .. attribute:: clock_interface
        
        	Configuration for a clock interface
        	**type**\:   :py:class:`ClockInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface>`
        
        .. attribute:: lpts_local
        
        	lpts node specific configuration commands
        	**type**\:   :py:class:`LptsLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal>`
        
        .. attribute:: ltrace
        
        	Ltrace Memory configuration
        	**type**\:   :py:class:`Ltrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.Ltrace>`
        
        .. attribute:: ssrp_group
        
        	Per\-node SSRP configuration data
        	**type**\:   :py:class:`SsrpGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.SsrpGroup>`
        
        

        """

        _prefix = 'config-mda-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(ActiveNodes.ActiveNode, self).__init__()

            self.yang_name = "active-node"
            self.yang_parent_name = "active-nodes"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold" : ("cisco_ios_xr_watchd_cfg_watchdog_node_threshold", ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold), "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold" : ("cisco_ios_xr_wd_cfg_watchdog_node_threshold", ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold), "clock-interface" : ("clock_interface", ActiveNodes.ActiveNode.ClockInterface), "lpts-local" : ("lpts_local", ActiveNodes.ActiveNode.LptsLocal), "ltrace" : ("ltrace", ActiveNodes.ActiveNode.Ltrace), "ssrp-group" : ("ssrp_group", ActiveNodes.ActiveNode.SsrpGroup)}
            self._child_list_classes = {}

            self.node_name = YLeaf(YType.str, "node-name")

            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold = ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold()
            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold.parent = self
            self._children_name_map["cisco_ios_xr_watchd_cfg_watchdog_node_threshold"] = "Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold"
            self._children_yang_names.add("Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold")

            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold = ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold()
            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold.parent = self
            self._children_name_map["cisco_ios_xr_wd_cfg_watchdog_node_threshold"] = "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold"
            self._children_yang_names.add("Cisco-IOS-XR-wd-cfg_watchdog-node-threshold")

            self.clock_interface = ActiveNodes.ActiveNode.ClockInterface()
            self.clock_interface.parent = self
            self._children_name_map["clock_interface"] = "clock-interface"
            self._children_yang_names.add("clock-interface")

            self.lpts_local = ActiveNodes.ActiveNode.LptsLocal()
            self.lpts_local.parent = self
            self._children_name_map["lpts_local"] = "lpts-local"
            self._children_yang_names.add("lpts-local")

            self.ltrace = ActiveNodes.ActiveNode.Ltrace()
            self.ltrace.parent = self
            self._children_name_map["ltrace"] = "ltrace"
            self._children_yang_names.add("ltrace")

            self.ssrp_group = ActiveNodes.ActiveNode.SsrpGroup()
            self.ssrp_group.parent = self
            self._children_name_map["ssrp_group"] = "ssrp-group"
            self._children_yang_names.add("ssrp-group")
            self._segment_path = lambda: "active-node" + "[node-name='" + self.node_name.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-config-mda-cfg:active-nodes/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ActiveNodes.ActiveNode, ['node_name'], name, value)


        class CiscoIOSXRWatchdCfgWatchdogNodeThreshold(Entity):
            """
            watchdog node threshold
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\:   :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'watchd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold, self).__init__()

                self.yang_name = "Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"memory-threshold" : ("memory_threshold", ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold)}
                self._child_list_classes = {}

                self.memory_threshold = ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self
                self._children_name_map["memory_threshold"] = "memory-threshold"
                self._children_yang_names.add("memory-threshold")
                self._segment_path = lambda: "Cisco-IOS-XR-watchd-cfg:Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold"


            class MemoryThreshold(Entity):
                """
                Memory thresholds
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\:  int
                
                	**range:** 3..40
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\:  int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\:  int
                
                	**range:** 4..40
                
                

                """

                _prefix = 'watchd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold, self).__init__()

                    self.yang_name = "memory-threshold"
                    self.yang_parent_name = "Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.critical = YLeaf(YType.uint32, "critical")

                    self.minor = YLeaf(YType.uint32, "minor")

                    self.severe = YLeaf(YType.uint32, "severe")
                    self._segment_path = lambda: "memory-threshold"

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold, ['critical', 'minor', 'severe'], name, value)


        class CiscoIOSXRWdCfgWatchdogNodeThreshold(Entity):
            """
            Watchdog threshold configuration
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\:   :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'wd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold, self).__init__()

                self.yang_name = "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"memory-threshold" : ("memory_threshold", ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold)}
                self._child_list_classes = {}

                self.memory_threshold = ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self
                self._children_name_map["memory_threshold"] = "memory-threshold"
                self._children_yang_names.add("memory-threshold")
                self._segment_path = lambda: "Cisco-IOS-XR-wd-cfg:Cisco-IOS-XR-wd-cfg_watchdog-node-threshold"


            class MemoryThreshold(Entity):
                """
                Memory thresholds
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\:  int
                
                	**range:** 3..40
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\:  int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\:  int
                
                	**range:** 4..40
                
                

                """

                _prefix = 'wd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold, self).__init__()

                    self.yang_name = "memory-threshold"
                    self.yang_parent_name = "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.critical = YLeaf(YType.uint32, "critical")

                    self.minor = YLeaf(YType.uint32, "minor")

                    self.severe = YLeaf(YType.uint32, "severe")
                    self._segment_path = lambda: "memory-threshold"

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold, ['critical', 'minor', 'severe'], name, value)


        class ClockInterface(Entity):
            """
            Configuration for a clock interface
            
            .. attribute:: clocks
            
            	Configuration for a clock interface
            	**type**\:   :py:class:`Clocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks>`
            
            

            """

            _prefix = 'freqsync-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ActiveNodes.ActiveNode.ClockInterface, self).__init__()

                self.yang_name = "clock-interface"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"clocks" : ("clocks", ActiveNodes.ActiveNode.ClockInterface.Clocks)}
                self._child_list_classes = {}

                self.clocks = ActiveNodes.ActiveNode.ClockInterface.Clocks()
                self.clocks.parent = self
                self._children_name_map["clocks"] = "clocks"
                self._children_yang_names.add("clocks")
                self._segment_path = lambda: "Cisco-IOS-XR-freqsync-cfg:clock-interface"


            class Clocks(Entity):
                """
                Configuration for a clock interface
                
                .. attribute:: clock
                
                	Configuration for a clock interface
                	**type**\: list of    :py:class:`Clock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock>`
                
                

                """

                _prefix = 'freqsync-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.ClockInterface.Clocks, self).__init__()

                    self.yang_name = "clocks"
                    self.yang_parent_name = "clock-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"clock" : ("clock", ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock)}

                    self.clock = YList(self)
                    self._segment_path = lambda: "clocks"

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks, [], name, value)


                class Clock(Entity):
                    """
                    Configuration for a clock interface
                    
                    .. attribute:: clock_type  <key>
                    
                    	Clock type
                    	**type**\:   :py:class:`FsyncClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncClock>`
                    
                    .. attribute:: port  <key>
                    
                    	Clock port
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: frequency_synchronization
                    
                    	Frequency Synchronization clock configuraiton
                    	**type**\:   :py:class:`FrequencySynchronization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization>`
                    
                    

                    """

                    _prefix = 'freqsync-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock, self).__init__()

                        self.yang_name = "clock"
                        self.yang_parent_name = "clocks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"frequency-synchronization" : ("frequency_synchronization", ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization)}
                        self._child_list_classes = {}

                        self.clock_type = YLeaf(YType.enumeration, "clock-type")

                        self.port = YLeaf(YType.int32, "port")

                        self.frequency_synchronization = ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization()
                        self.frequency_synchronization.parent = self
                        self._children_name_map["frequency_synchronization"] = "frequency-synchronization"
                        self._children_yang_names.add("frequency-synchronization")
                        self._segment_path = lambda: "clock" + "[clock-type='" + self.clock_type.get() + "']" + "[port='" + self.port.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock, ['clock_type', 'port'], name, value)


                    class FrequencySynchronization(Entity):
                        """
                        Frequency Synchronization clock configuraiton
                        
                        .. attribute:: input_quality_level
                        
                        	Set the input quality level
                        	**type**\:   :py:class:`InputQualityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel>`
                        
                        .. attribute:: output_quality_level
                        
                        	Set the output quality level
                        	**type**\:   :py:class:`OutputQualityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel>`
                        
                        .. attribute:: priority
                        
                        	Set the priority of this source
                        	**type**\:  int
                        
                        	**range:** 1..254
                        
                        	**default value**\: 100
                        
                        .. attribute:: selection_input
                        
                        	Assign this source as a selection input
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: ssm_disable
                        
                        	Disable SSM on this source
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: time_of_day_priority
                        
                        	Set the time\-of\-day priority of this source
                        	**type**\:  int
                        
                        	**range:** 1..254
                        
                        	**default value**\: 100
                        
                        .. attribute:: wait_to_restore_time
                        
                        	Set the wait\-to\-restore time for this source
                        	**type**\:  int
                        
                        	**range:** 0..12
                        
                        	**default value**\: 5
                        
                        

                        """

                        _prefix = 'freqsync-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization, self).__init__()

                            self.yang_name = "frequency-synchronization"
                            self.yang_parent_name = "clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"input-quality-level" : ("input_quality_level", ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel), "output-quality-level" : ("output_quality_level", ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel)}
                            self._child_list_classes = {}

                            self.priority = YLeaf(YType.uint32, "priority")

                            self.selection_input = YLeaf(YType.empty, "selection-input")

                            self.ssm_disable = YLeaf(YType.empty, "ssm-disable")

                            self.time_of_day_priority = YLeaf(YType.uint32, "time-of-day-priority")

                            self.wait_to_restore_time = YLeaf(YType.uint32, "wait-to-restore-time")

                            self.input_quality_level = ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel()
                            self.input_quality_level.parent = self
                            self._children_name_map["input_quality_level"] = "input-quality-level"
                            self._children_yang_names.add("input-quality-level")

                            self.output_quality_level = ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel()
                            self.output_quality_level.parent = self
                            self._children_name_map["output_quality_level"] = "output-quality-level"
                            self._children_yang_names.add("output-quality-level")
                            self._segment_path = lambda: "frequency-synchronization"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization, ['priority', 'selection_input', 'ssm_disable', 'time_of_day_priority', 'wait_to_restore_time'], name, value)


                        class InputQualityLevel(Entity):
                            """
                            Set the input quality level
                            
                            .. attribute:: exact_quality_level_value
                            
                            	Exact quality level value
                            	**type**\:   :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: max_quality_level_value
                            
                            	Maximum quality level value
                            	**type**\:   :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: min_quality_level_value
                            
                            	Minimum quality level value
                            	**type**\:   :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: quality_level_option
                            
                            	Quality level option
                            	**type**\:   :py:class:`FsyncQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlOption>`
                            
                            

                            """

                            _prefix = 'freqsync-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel, self).__init__()

                                self.yang_name = "input-quality-level"
                                self.yang_parent_name = "frequency-synchronization"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.exact_quality_level_value = YLeaf(YType.enumeration, "exact-quality-level-value")

                                self.max_quality_level_value = YLeaf(YType.enumeration, "max-quality-level-value")

                                self.min_quality_level_value = YLeaf(YType.enumeration, "min-quality-level-value")

                                self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")
                                self._segment_path = lambda: "input-quality-level"

                            def __setattr__(self, name, value):
                                self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel, ['exact_quality_level_value', 'max_quality_level_value', 'min_quality_level_value', 'quality_level_option'], name, value)


                        class OutputQualityLevel(Entity):
                            """
                            Set the output quality level
                            
                            .. attribute:: exact_quality_level_value
                            
                            	Exact quality level value
                            	**type**\:   :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: max_quality_level_value
                            
                            	Maximum quality level value
                            	**type**\:   :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: min_quality_level_value
                            
                            	Minimum quality level value
                            	**type**\:   :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: quality_level_option
                            
                            	Quality level option
                            	**type**\:   :py:class:`FsyncQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlOption>`
                            
                            

                            """

                            _prefix = 'freqsync-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel, self).__init__()

                                self.yang_name = "output-quality-level"
                                self.yang_parent_name = "frequency-synchronization"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.exact_quality_level_value = YLeaf(YType.enumeration, "exact-quality-level-value")

                                self.max_quality_level_value = YLeaf(YType.enumeration, "max-quality-level-value")

                                self.min_quality_level_value = YLeaf(YType.enumeration, "min-quality-level-value")

                                self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")
                                self._segment_path = lambda: "output-quality-level"

                            def __setattr__(self, name, value):
                                self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel, ['exact_quality_level_value', 'max_quality_level_value', 'min_quality_level_value', 'quality_level_option'], name, value)


        class LptsLocal(Entity):
            """
            lpts node specific configuration commands
            
            .. attribute:: dynamic_flows_tables
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:   :py:class:`DynamicFlowsTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables>`
            
            .. attribute:: ipolicer_local
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:   :py:class:`IpolicerLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal>`
            
            	**presence node**\: True
            
            .. attribute:: ipolicer_local_tables
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:   :py:class:`IpolicerLocalTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ActiveNodes.ActiveNode.LptsLocal, self).__init__()

                self.yang_name = "lpts-local"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"dynamic-flows-tables" : ("dynamic_flows_tables", ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables), "ipolicer-local" : ("ipolicer_local", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal), "ipolicer-local-tables" : ("ipolicer_local_tables", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables)}
                self._child_list_classes = {}

                self.dynamic_flows_tables = ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables()
                self.dynamic_flows_tables.parent = self
                self._children_name_map["dynamic_flows_tables"] = "dynamic-flows-tables"
                self._children_yang_names.add("dynamic-flows-tables")

                self.ipolicer_local = None
                self._children_name_map["ipolicer_local"] = "ipolicer-local"
                self._children_yang_names.add("ipolicer-local")

                self.ipolicer_local_tables = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables()
                self.ipolicer_local_tables.parent = self
                self._children_name_map["ipolicer_local_tables"] = "ipolicer-local-tables"
                self._children_yang_names.add("ipolicer-local-tables")
                self._segment_path = lambda: "Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local"


            class DynamicFlowsTables(Entity):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: dynamic_flows_table
                
                	Table for Dynamic Flows
                	**type**\: list of    :py:class:`DynamicFlowsTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables, self).__init__()

                    self.yang_name = "dynamic-flows-tables"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"dynamic-flows-table" : ("dynamic_flows_table", ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable)}

                    self.dynamic_flows_table = YList(self)
                    self._segment_path = lambda: "dynamic-flows-tables"

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables, [], name, value)


                class DynamicFlowsTable(Entity):
                    """
                    Table for Dynamic Flows
                    
                    .. attribute:: table_type  <key>
                    
                    	LPTS Dynamic Flows Table Type
                    	**type**\:   :py:class:`LptsDynamicFlowConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsDynamicFlowConfig>`
                    
                    .. attribute:: flow_type
                    
                    	Selected flow type
                    	**type**\: list of    :py:class:`FlowType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable, self).__init__()

                        self.yang_name = "dynamic-flows-table"
                        self.yang_parent_name = "dynamic-flows-tables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"flow-type" : ("flow_type", ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType)}

                        self.table_type = YLeaf(YType.enumeration, "table-type")

                        self.flow_type = YList(self)
                        self._segment_path = lambda: "dynamic-flows-table" + "[table-type='" + self.table_type.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable, ['table_type'], name, value)


                    class FlowType(Entity):
                        """
                        Selected flow type
                        
                        .. attribute:: flow_type  <key>
                        
                        	LPTS Flow Type
                        	**type**\:   :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                        
                        .. attribute:: max
                        
                        	Configured Max TCAM value
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType, self).__init__()

                            self.yang_name = "flow-type"
                            self.yang_parent_name = "dynamic-flows-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.flow_type = YLeaf(YType.enumeration, "flow-type")

                            self.max = YLeaf(YType.int32, "max")
                            self._segment_path = lambda: "flow-type" + "[flow-type='" + self.flow_type.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType, ['flow_type', 'max'], name, value)


            class IpolicerLocal(Entity):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: enable
                
                	Enabled
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: flows
                
                	Table for Flows
                	**type**\:   :py:class:`Flows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal, self).__init__()

                    self.yang_name = "ipolicer-local"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"flows" : ("flows", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows)}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.enable = YLeaf(YType.empty, "enable")

                    self.flows = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows()
                    self.flows.parent = self
                    self._children_name_map["flows"] = "flows"
                    self._children_yang_names.add("flows")
                    self._segment_path = lambda: "ipolicer-local"

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal, ['enable'], name, value)


                class Flows(Entity):
                    """
                    Table for Flows
                    
                    .. attribute:: flow
                    
                    	selected flow type
                    	**type**\: list of    :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows, self).__init__()

                        self.yang_name = "flows"
                        self.yang_parent_name = "ipolicer-local"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"flow" : ("flow", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow)}

                        self.flow = YList(self)
                        self._segment_path = lambda: "flows"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows, [], name, value)


                    class Flow(Entity):
                        """
                        selected flow type
                        
                        .. attribute:: flow_type  <key>
                        
                        	LPTS Flow Type
                        	**type**\:   :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                        
                        .. attribute:: precedences
                        
                        	TOS Precedence value(s)
                        	**type**\:   :py:class:`Precedences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences>`
                        
                        .. attribute:: rate
                        
                        	Configured rate value
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow, self).__init__()

                            self.yang_name = "flow"
                            self.yang_parent_name = "flows"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"precedences" : ("precedences", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences)}
                            self._child_list_classes = {}

                            self.flow_type = YLeaf(YType.enumeration, "flow-type")

                            self.rate = YLeaf(YType.int32, "rate")

                            self.precedences = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences()
                            self.precedences.parent = self
                            self._children_name_map["precedences"] = "precedences"
                            self._children_yang_names.add("precedences")
                            self._segment_path = lambda: "flow" + "[flow-type='" + self.flow_type.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow, ['flow_type', 'rate'], name, value)


                        class Precedences(Entity):
                            """
                            TOS Precedence value(s)
                            
                            .. attribute:: precedence
                            
                            	Precedence values
                            	**type**\: one of the below types:
                            
                            	**type**\:  list of   :py:class:`LptsPreIFibPrecedenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumber>`
                            
                            
                            ----
                            	**type**\:  list of int
                            
                            	**range:** 0..7
                            
                            
                            ----
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences, self).__init__()

                                self.yang_name = "precedences"
                                self.yang_parent_name = "flow"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.precedence = YLeafList(YType.str, "precedence")
                                self._segment_path = lambda: "precedences"

                            def __setattr__(self, name, value):
                                self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences, ['precedence'], name, value)


            class IpolicerLocalTables(Entity):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: ipolicer_local_table
                
                	Pre IFIB (Internal Forwarding Information Base) configuration table
                	**type**\: list of    :py:class:`IpolicerLocalTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables, self).__init__()

                    self.yang_name = "ipolicer-local-tables"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"ipolicer-local-table" : ("ipolicer_local_table", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable)}

                    self.ipolicer_local_table = YList(self)
                    self._segment_path = lambda: "ipolicer-local-tables"

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables, [], name, value)


                class IpolicerLocalTable(Entity):
                    """
                    Pre IFIB (Internal Forwarding Information
                    Base) configuration table
                    
                    .. attribute:: id1  <key>
                    
                    	none
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: nps
                    
                    	NP name
                    	**type**\:   :py:class:`Nps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable, self).__init__()

                        self.yang_name = "ipolicer-local-table"
                        self.yang_parent_name = "ipolicer-local-tables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"nps" : ("nps", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps)}
                        self._child_list_classes = {}

                        self.id1 = YLeaf(YType.str, "id1")

                        self.nps = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps()
                        self.nps.parent = self
                        self._children_name_map["nps"] = "nps"
                        self._children_yang_names.add("nps")
                        self._segment_path = lambda: "ipolicer-local-table" + "[id1='" + self.id1.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable, ['id1'], name, value)


                    class Nps(Entity):
                        """
                        NP name
                        
                        .. attribute:: np
                        
                        	Table of NP names
                        	**type**\: list of    :py:class:`Np <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps, self).__init__()

                            self.yang_name = "nps"
                            self.yang_parent_name = "ipolicer-local-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"np" : ("np", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np)}

                            self.np = YList(self)
                            self._segment_path = lambda: "nps"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps, [], name, value)


                        class Np(Entity):
                            """
                            Table of NP names
                            
                            .. attribute:: id1  <key>
                            
                            	none
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: rate
                            
                            	Packets per second
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**units**\: packet/s
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np, self).__init__()

                                self.yang_name = "np"
                                self.yang_parent_name = "nps"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.id1 = YLeaf(YType.int32, "id1")

                                self.rate = YLeaf(YType.int32, "rate")
                                self._segment_path = lambda: "np" + "[id1='" + self.id1.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np, ['id1', 'rate'], name, value)


        class Ltrace(Entity):
            """
            Ltrace Memory configuration
            
            .. attribute:: allocation_params
            
            	Select Ltrace mode and scale\-factor
            	**type**\:   :py:class:`AllocationParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.Ltrace.AllocationParams>`
            
            

            """

            _prefix = 'infra-ltrace-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ActiveNodes.ActiveNode.Ltrace, self).__init__()

                self.yang_name = "ltrace"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"allocation-params" : ("allocation_params", ActiveNodes.ActiveNode.Ltrace.AllocationParams)}
                self._child_list_classes = {}

                self.allocation_params = ActiveNodes.ActiveNode.Ltrace.AllocationParams()
                self.allocation_params.parent = self
                self._children_name_map["allocation_params"] = "allocation-params"
                self._children_yang_names.add("allocation-params")
                self._segment_path = lambda: "Cisco-IOS-XR-infra-ltrace-cfg:ltrace"


            class AllocationParams(Entity):
                """
                Select Ltrace mode and scale\-factor
                
                .. attribute:: mode
                
                	Select an allocation mode (static\:1, dynamic \:2)
                	**type**\:   :py:class:`InfraLtraceMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceMode>`
                
                .. attribute:: scale_factor
                
                	Select a scaling down factor
                	**type**\:   :py:class:`InfraLtraceScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceScale>`
                
                

                """

                _prefix = 'infra-ltrace-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.Ltrace.AllocationParams, self).__init__()

                    self.yang_name = "allocation-params"
                    self.yang_parent_name = "ltrace"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.mode = YLeaf(YType.enumeration, "mode")

                    self.scale_factor = YLeaf(YType.enumeration, "scale-factor")
                    self._segment_path = lambda: "allocation-params"

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.Ltrace.AllocationParams, ['mode', 'scale_factor'], name, value)


        class SsrpGroup(Entity):
            """
            Per\-node SSRP configuration data
            
            .. attribute:: groups
            
            	Table of SSRP Group configuration
            	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.SsrpGroup.Groups>`
            
            

            """

            _prefix = 'ppp-ma-ssrp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ActiveNodes.ActiveNode.SsrpGroup, self).__init__()

                self.yang_name = "ssrp-group"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"groups" : ("groups", ActiveNodes.ActiveNode.SsrpGroup.Groups)}
                self._child_list_classes = {}

                self.groups = ActiveNodes.ActiveNode.SsrpGroup.Groups()
                self.groups.parent = self
                self._children_name_map["groups"] = "groups"
                self._children_yang_names.add("groups")
                self._segment_path = lambda: "Cisco-IOS-XR-ppp-ma-ssrp-cfg:ssrp-group"


            class Groups(Entity):
                """
                Table of SSRP Group configuration
                
                .. attribute:: group
                
                	SSRP Group configuration
                	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.SsrpGroup.Groups.Group>`
                
                

                """

                _prefix = 'ppp-ma-ssrp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ActiveNodes.ActiveNode.SsrpGroup.Groups, self).__init__()

                    self.yang_name = "groups"
                    self.yang_parent_name = "ssrp-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"group" : ("group", ActiveNodes.ActiveNode.SsrpGroup.Groups.Group)}

                    self.group = YList(self)
                    self._segment_path = lambda: "groups"

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.SsrpGroup.Groups, [], name, value)


                class Group(Entity):
                    """
                    SSRP Group configuration
                    
                    .. attribute:: group_id  <key>
                    
                    	The identifier for this group
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: profile
                    
                    	This specifies the SSRP profile to use for this group
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ppp-ma-ssrp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ActiveNodes.ActiveNode.SsrpGroup.Groups.Group, self).__init__()

                        self.yang_name = "group"
                        self.yang_parent_name = "groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.group_id = YLeaf(YType.uint32, "group-id")

                        self.profile = YLeaf(YType.str, "profile")
                        self._segment_path = lambda: "group" + "[group-id='" + self.group_id.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.SsrpGroup.Groups.Group, ['group_id', 'profile'], name, value)

    def clone_ptr(self):
        self._top_entity = ActiveNodes()
        return self._top_entity

class PreconfiguredNodes(Entity):
    """
    preconfigured nodes
    
    .. attribute:: preconfigured_node
    
    	The configuration for a non\-active node
    	**type**\: list of    :py:class:`PreconfiguredNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode>`
    
    

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
        self._child_container_classes = {}
        self._child_list_classes = {"preconfigured-node" : ("preconfigured_node", PreconfiguredNodes.PreconfiguredNode)}

        self.preconfigured_node = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-config-mda-cfg:preconfigured-nodes"

    def __setattr__(self, name, value):
        self._perform_setattr(PreconfiguredNodes, [], name, value)


    class PreconfiguredNode(Entity):
        """
        The configuration for a non\-active node
        
        .. attribute:: node_name  <key>
        
        	The identifier for this node
        	**type**\:  str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: cisco_ios_xr_watchd_cfg_watchdog_node_threshold
        
        	watchdog node threshold
        	**type**\:   :py:class:`CiscoIOSXRWatchdCfgWatchdogNodeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold>`
        
        .. attribute:: cisco_ios_xr_wd_cfg_watchdog_node_threshold
        
        	Watchdog threshold configuration
        	**type**\:   :py:class:`CiscoIOSXRWdCfgWatchdogNodeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold>`
        
        .. attribute:: clock_interface
        
        	Configuration for a clock interface
        	**type**\:   :py:class:`ClockInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface>`
        
        .. attribute:: lpts_local
        
        	lpts node specific configuration commands
        	**type**\:   :py:class:`LptsLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal>`
        
        .. attribute:: ltrace
        
        	Ltrace Memory configuration
        	**type**\:   :py:class:`Ltrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.Ltrace>`
        
        

        """

        _prefix = 'config-mda-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(PreconfiguredNodes.PreconfiguredNode, self).__init__()

            self.yang_name = "preconfigured-node"
            self.yang_parent_name = "preconfigured-nodes"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold" : ("cisco_ios_xr_watchd_cfg_watchdog_node_threshold", PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold), "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold" : ("cisco_ios_xr_wd_cfg_watchdog_node_threshold", PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold), "clock-interface" : ("clock_interface", PreconfiguredNodes.PreconfiguredNode.ClockInterface), "lpts-local" : ("lpts_local", PreconfiguredNodes.PreconfiguredNode.LptsLocal), "ltrace" : ("ltrace", PreconfiguredNodes.PreconfiguredNode.Ltrace)}
            self._child_list_classes = {}

            self.node_name = YLeaf(YType.str, "node-name")

            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold()
            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold.parent = self
            self._children_name_map["cisco_ios_xr_watchd_cfg_watchdog_node_threshold"] = "Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold"
            self._children_yang_names.add("Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold")

            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold()
            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold.parent = self
            self._children_name_map["cisco_ios_xr_wd_cfg_watchdog_node_threshold"] = "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold"
            self._children_yang_names.add("Cisco-IOS-XR-wd-cfg_watchdog-node-threshold")

            self.clock_interface = PreconfiguredNodes.PreconfiguredNode.ClockInterface()
            self.clock_interface.parent = self
            self._children_name_map["clock_interface"] = "clock-interface"
            self._children_yang_names.add("clock-interface")

            self.lpts_local = PreconfiguredNodes.PreconfiguredNode.LptsLocal()
            self.lpts_local.parent = self
            self._children_name_map["lpts_local"] = "lpts-local"
            self._children_yang_names.add("lpts-local")

            self.ltrace = PreconfiguredNodes.PreconfiguredNode.Ltrace()
            self.ltrace.parent = self
            self._children_name_map["ltrace"] = "ltrace"
            self._children_yang_names.add("ltrace")
            self._segment_path = lambda: "preconfigured-node" + "[node-name='" + self.node_name.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-config-mda-cfg:preconfigured-nodes/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode, ['node_name'], name, value)


        class CiscoIOSXRWatchdCfgWatchdogNodeThreshold(Entity):
            """
            watchdog node threshold
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\:   :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'watchd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold, self).__init__()

                self.yang_name = "Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold"
                self.yang_parent_name = "preconfigured-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"memory-threshold" : ("memory_threshold", PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold)}
                self._child_list_classes = {}

                self.memory_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self
                self._children_name_map["memory_threshold"] = "memory-threshold"
                self._children_yang_names.add("memory-threshold")
                self._segment_path = lambda: "Cisco-IOS-XR-watchd-cfg:Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold"


            class MemoryThreshold(Entity):
                """
                Memory thresholds
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\:  int
                
                	**range:** 3..40
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\:  int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\:  int
                
                	**range:** 4..40
                
                

                """

                _prefix = 'watchd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold, self).__init__()

                    self.yang_name = "memory-threshold"
                    self.yang_parent_name = "Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.critical = YLeaf(YType.uint32, "critical")

                    self.minor = YLeaf(YType.uint32, "minor")

                    self.severe = YLeaf(YType.uint32, "severe")
                    self._segment_path = lambda: "memory-threshold"

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold, ['critical', 'minor', 'severe'], name, value)


        class CiscoIOSXRWdCfgWatchdogNodeThreshold(Entity):
            """
            Watchdog threshold configuration
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\:   :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'wd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold, self).__init__()

                self.yang_name = "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold"
                self.yang_parent_name = "preconfigured-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"memory-threshold" : ("memory_threshold", PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold)}
                self._child_list_classes = {}

                self.memory_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self
                self._children_name_map["memory_threshold"] = "memory-threshold"
                self._children_yang_names.add("memory-threshold")
                self._segment_path = lambda: "Cisco-IOS-XR-wd-cfg:Cisco-IOS-XR-wd-cfg_watchdog-node-threshold"


            class MemoryThreshold(Entity):
                """
                Memory thresholds
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\:  int
                
                	**range:** 3..40
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\:  int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\:  int
                
                	**range:** 4..40
                
                

                """

                _prefix = 'wd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold, self).__init__()

                    self.yang_name = "memory-threshold"
                    self.yang_parent_name = "Cisco-IOS-XR-wd-cfg_watchdog-node-threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.critical = YLeaf(YType.uint32, "critical")

                    self.minor = YLeaf(YType.uint32, "minor")

                    self.severe = YLeaf(YType.uint32, "severe")
                    self._segment_path = lambda: "memory-threshold"

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold, ['critical', 'minor', 'severe'], name, value)


        class ClockInterface(Entity):
            """
            Configuration for a clock interface
            
            .. attribute:: clocks
            
            	Configuration for a clock interface
            	**type**\:   :py:class:`Clocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks>`
            
            

            """

            _prefix = 'freqsync-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(PreconfiguredNodes.PreconfiguredNode.ClockInterface, self).__init__()

                self.yang_name = "clock-interface"
                self.yang_parent_name = "preconfigured-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"clocks" : ("clocks", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks)}
                self._child_list_classes = {}

                self.clocks = PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks()
                self.clocks.parent = self
                self._children_name_map["clocks"] = "clocks"
                self._children_yang_names.add("clocks")
                self._segment_path = lambda: "Cisco-IOS-XR-freqsync-cfg:clock-interface"


            class Clocks(Entity):
                """
                Configuration for a clock interface
                
                .. attribute:: clock
                
                	Configuration for a clock interface
                	**type**\: list of    :py:class:`Clock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock>`
                
                

                """

                _prefix = 'freqsync-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks, self).__init__()

                    self.yang_name = "clocks"
                    self.yang_parent_name = "clock-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"clock" : ("clock", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock)}

                    self.clock = YList(self)
                    self._segment_path = lambda: "clocks"

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks, [], name, value)


                class Clock(Entity):
                    """
                    Configuration for a clock interface
                    
                    .. attribute:: clock_type  <key>
                    
                    	Clock type
                    	**type**\:   :py:class:`FsyncClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncClock>`
                    
                    .. attribute:: port  <key>
                    
                    	Clock port
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: frequency_synchronization
                    
                    	Frequency Synchronization clock configuraiton
                    	**type**\:   :py:class:`FrequencySynchronization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization>`
                    
                    

                    """

                    _prefix = 'freqsync-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock, self).__init__()

                        self.yang_name = "clock"
                        self.yang_parent_name = "clocks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"frequency-synchronization" : ("frequency_synchronization", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization)}
                        self._child_list_classes = {}

                        self.clock_type = YLeaf(YType.enumeration, "clock-type")

                        self.port = YLeaf(YType.int32, "port")

                        self.frequency_synchronization = PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization()
                        self.frequency_synchronization.parent = self
                        self._children_name_map["frequency_synchronization"] = "frequency-synchronization"
                        self._children_yang_names.add("frequency-synchronization")
                        self._segment_path = lambda: "clock" + "[clock-type='" + self.clock_type.get() + "']" + "[port='" + self.port.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock, ['clock_type', 'port'], name, value)


                    class FrequencySynchronization(Entity):
                        """
                        Frequency Synchronization clock configuraiton
                        
                        .. attribute:: input_quality_level
                        
                        	Set the input quality level
                        	**type**\:   :py:class:`InputQualityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel>`
                        
                        .. attribute:: output_quality_level
                        
                        	Set the output quality level
                        	**type**\:   :py:class:`OutputQualityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel>`
                        
                        .. attribute:: priority
                        
                        	Set the priority of this source
                        	**type**\:  int
                        
                        	**range:** 1..254
                        
                        	**default value**\: 100
                        
                        .. attribute:: selection_input
                        
                        	Assign this source as a selection input
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: ssm_disable
                        
                        	Disable SSM on this source
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: time_of_day_priority
                        
                        	Set the time\-of\-day priority of this source
                        	**type**\:  int
                        
                        	**range:** 1..254
                        
                        	**default value**\: 100
                        
                        .. attribute:: wait_to_restore_time
                        
                        	Set the wait\-to\-restore time for this source
                        	**type**\:  int
                        
                        	**range:** 0..12
                        
                        	**default value**\: 5
                        
                        

                        """

                        _prefix = 'freqsync-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization, self).__init__()

                            self.yang_name = "frequency-synchronization"
                            self.yang_parent_name = "clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"input-quality-level" : ("input_quality_level", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel), "output-quality-level" : ("output_quality_level", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel)}
                            self._child_list_classes = {}

                            self.priority = YLeaf(YType.uint32, "priority")

                            self.selection_input = YLeaf(YType.empty, "selection-input")

                            self.ssm_disable = YLeaf(YType.empty, "ssm-disable")

                            self.time_of_day_priority = YLeaf(YType.uint32, "time-of-day-priority")

                            self.wait_to_restore_time = YLeaf(YType.uint32, "wait-to-restore-time")

                            self.input_quality_level = PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel()
                            self.input_quality_level.parent = self
                            self._children_name_map["input_quality_level"] = "input-quality-level"
                            self._children_yang_names.add("input-quality-level")

                            self.output_quality_level = PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel()
                            self.output_quality_level.parent = self
                            self._children_name_map["output_quality_level"] = "output-quality-level"
                            self._children_yang_names.add("output-quality-level")
                            self._segment_path = lambda: "frequency-synchronization"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization, ['priority', 'selection_input', 'ssm_disable', 'time_of_day_priority', 'wait_to_restore_time'], name, value)


                        class InputQualityLevel(Entity):
                            """
                            Set the input quality level
                            
                            .. attribute:: exact_quality_level_value
                            
                            	Exact quality level value
                            	**type**\:   :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: max_quality_level_value
                            
                            	Maximum quality level value
                            	**type**\:   :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: min_quality_level_value
                            
                            	Minimum quality level value
                            	**type**\:   :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: quality_level_option
                            
                            	Quality level option
                            	**type**\:   :py:class:`FsyncQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlOption>`
                            
                            

                            """

                            _prefix = 'freqsync-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel, self).__init__()

                                self.yang_name = "input-quality-level"
                                self.yang_parent_name = "frequency-synchronization"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.exact_quality_level_value = YLeaf(YType.enumeration, "exact-quality-level-value")

                                self.max_quality_level_value = YLeaf(YType.enumeration, "max-quality-level-value")

                                self.min_quality_level_value = YLeaf(YType.enumeration, "min-quality-level-value")

                                self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")
                                self._segment_path = lambda: "input-quality-level"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel, ['exact_quality_level_value', 'max_quality_level_value', 'min_quality_level_value', 'quality_level_option'], name, value)


                        class OutputQualityLevel(Entity):
                            """
                            Set the output quality level
                            
                            .. attribute:: exact_quality_level_value
                            
                            	Exact quality level value
                            	**type**\:   :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: max_quality_level_value
                            
                            	Maximum quality level value
                            	**type**\:   :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: min_quality_level_value
                            
                            	Minimum quality level value
                            	**type**\:   :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: quality_level_option
                            
                            	Quality level option
                            	**type**\:   :py:class:`FsyncQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlOption>`
                            
                            

                            """

                            _prefix = 'freqsync-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel, self).__init__()

                                self.yang_name = "output-quality-level"
                                self.yang_parent_name = "frequency-synchronization"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.exact_quality_level_value = YLeaf(YType.enumeration, "exact-quality-level-value")

                                self.max_quality_level_value = YLeaf(YType.enumeration, "max-quality-level-value")

                                self.min_quality_level_value = YLeaf(YType.enumeration, "min-quality-level-value")

                                self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")
                                self._segment_path = lambda: "output-quality-level"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel, ['exact_quality_level_value', 'max_quality_level_value', 'min_quality_level_value', 'quality_level_option'], name, value)


        class LptsLocal(Entity):
            """
            lpts node specific configuration commands
            
            .. attribute:: dynamic_flows_tables
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:   :py:class:`DynamicFlowsTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables>`
            
            .. attribute:: ipolicer_local
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:   :py:class:`IpolicerLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal>`
            
            	**presence node**\: True
            
            .. attribute:: ipolicer_local_tables
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:   :py:class:`IpolicerLocalTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal, self).__init__()

                self.yang_name = "lpts-local"
                self.yang_parent_name = "preconfigured-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"dynamic-flows-tables" : ("dynamic_flows_tables", PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables), "ipolicer-local" : ("ipolicer_local", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal), "ipolicer-local-tables" : ("ipolicer_local_tables", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables)}
                self._child_list_classes = {}

                self.dynamic_flows_tables = PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables()
                self.dynamic_flows_tables.parent = self
                self._children_name_map["dynamic_flows_tables"] = "dynamic-flows-tables"
                self._children_yang_names.add("dynamic-flows-tables")

                self.ipolicer_local = None
                self._children_name_map["ipolicer_local"] = "ipolicer-local"
                self._children_yang_names.add("ipolicer-local")

                self.ipolicer_local_tables = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables()
                self.ipolicer_local_tables.parent = self
                self._children_name_map["ipolicer_local_tables"] = "ipolicer-local-tables"
                self._children_yang_names.add("ipolicer-local-tables")
                self._segment_path = lambda: "Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local"


            class DynamicFlowsTables(Entity):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: dynamic_flows_table
                
                	Table for Dynamic Flows
                	**type**\: list of    :py:class:`DynamicFlowsTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables, self).__init__()

                    self.yang_name = "dynamic-flows-tables"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"dynamic-flows-table" : ("dynamic_flows_table", PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable)}

                    self.dynamic_flows_table = YList(self)
                    self._segment_path = lambda: "dynamic-flows-tables"

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables, [], name, value)


                class DynamicFlowsTable(Entity):
                    """
                    Table for Dynamic Flows
                    
                    .. attribute:: table_type  <key>
                    
                    	LPTS Dynamic Flows Table Type
                    	**type**\:   :py:class:`LptsDynamicFlowConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsDynamicFlowConfig>`
                    
                    .. attribute:: flow_type
                    
                    	Selected flow type
                    	**type**\: list of    :py:class:`FlowType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable, self).__init__()

                        self.yang_name = "dynamic-flows-table"
                        self.yang_parent_name = "dynamic-flows-tables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"flow-type" : ("flow_type", PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType)}

                        self.table_type = YLeaf(YType.enumeration, "table-type")

                        self.flow_type = YList(self)
                        self._segment_path = lambda: "dynamic-flows-table" + "[table-type='" + self.table_type.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable, ['table_type'], name, value)


                    class FlowType(Entity):
                        """
                        Selected flow type
                        
                        .. attribute:: flow_type  <key>
                        
                        	LPTS Flow Type
                        	**type**\:   :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                        
                        .. attribute:: max
                        
                        	Configured Max TCAM value
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType, self).__init__()

                            self.yang_name = "flow-type"
                            self.yang_parent_name = "dynamic-flows-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.flow_type = YLeaf(YType.enumeration, "flow-type")

                            self.max = YLeaf(YType.int32, "max")
                            self._segment_path = lambda: "flow-type" + "[flow-type='" + self.flow_type.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType, ['flow_type', 'max'], name, value)


            class IpolicerLocal(Entity):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: enable
                
                	Enabled
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: flows
                
                	Table for Flows
                	**type**\:   :py:class:`Flows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal, self).__init__()

                    self.yang_name = "ipolicer-local"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"flows" : ("flows", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows)}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.enable = YLeaf(YType.empty, "enable")

                    self.flows = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows()
                    self.flows.parent = self
                    self._children_name_map["flows"] = "flows"
                    self._children_yang_names.add("flows")
                    self._segment_path = lambda: "ipolicer-local"

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal, ['enable'], name, value)


                class Flows(Entity):
                    """
                    Table for Flows
                    
                    .. attribute:: flow
                    
                    	selected flow type
                    	**type**\: list of    :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows, self).__init__()

                        self.yang_name = "flows"
                        self.yang_parent_name = "ipolicer-local"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"flow" : ("flow", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow)}

                        self.flow = YList(self)
                        self._segment_path = lambda: "flows"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows, [], name, value)


                    class Flow(Entity):
                        """
                        selected flow type
                        
                        .. attribute:: flow_type  <key>
                        
                        	LPTS Flow Type
                        	**type**\:   :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                        
                        .. attribute:: precedences
                        
                        	TOS Precedence value(s)
                        	**type**\:   :py:class:`Precedences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences>`
                        
                        .. attribute:: rate
                        
                        	Configured rate value
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow, self).__init__()

                            self.yang_name = "flow"
                            self.yang_parent_name = "flows"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"precedences" : ("precedences", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences)}
                            self._child_list_classes = {}

                            self.flow_type = YLeaf(YType.enumeration, "flow-type")

                            self.rate = YLeaf(YType.int32, "rate")

                            self.precedences = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences()
                            self.precedences.parent = self
                            self._children_name_map["precedences"] = "precedences"
                            self._children_yang_names.add("precedences")
                            self._segment_path = lambda: "flow" + "[flow-type='" + self.flow_type.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow, ['flow_type', 'rate'], name, value)


                        class Precedences(Entity):
                            """
                            TOS Precedence value(s)
                            
                            .. attribute:: precedence
                            
                            	Precedence values
                            	**type**\: one of the below types:
                            
                            	**type**\:  list of   :py:class:`LptsPreIFibPrecedenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumber>`
                            
                            
                            ----
                            	**type**\:  list of int
                            
                            	**range:** 0..7
                            
                            
                            ----
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences, self).__init__()

                                self.yang_name = "precedences"
                                self.yang_parent_name = "flow"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.precedence = YLeafList(YType.str, "precedence")
                                self._segment_path = lambda: "precedences"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences, ['precedence'], name, value)


            class IpolicerLocalTables(Entity):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: ipolicer_local_table
                
                	Pre IFIB (Internal Forwarding Information Base) configuration table
                	**type**\: list of    :py:class:`IpolicerLocalTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables, self).__init__()

                    self.yang_name = "ipolicer-local-tables"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"ipolicer-local-table" : ("ipolicer_local_table", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable)}

                    self.ipolicer_local_table = YList(self)
                    self._segment_path = lambda: "ipolicer-local-tables"

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables, [], name, value)


                class IpolicerLocalTable(Entity):
                    """
                    Pre IFIB (Internal Forwarding Information
                    Base) configuration table
                    
                    .. attribute:: id1  <key>
                    
                    	none
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: nps
                    
                    	NP name
                    	**type**\:   :py:class:`Nps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable, self).__init__()

                        self.yang_name = "ipolicer-local-table"
                        self.yang_parent_name = "ipolicer-local-tables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"nps" : ("nps", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps)}
                        self._child_list_classes = {}

                        self.id1 = YLeaf(YType.str, "id1")

                        self.nps = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps()
                        self.nps.parent = self
                        self._children_name_map["nps"] = "nps"
                        self._children_yang_names.add("nps")
                        self._segment_path = lambda: "ipolicer-local-table" + "[id1='" + self.id1.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable, ['id1'], name, value)


                    class Nps(Entity):
                        """
                        NP name
                        
                        .. attribute:: np
                        
                        	Table of NP names
                        	**type**\: list of    :py:class:`Np <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps, self).__init__()

                            self.yang_name = "nps"
                            self.yang_parent_name = "ipolicer-local-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"np" : ("np", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np)}

                            self.np = YList(self)
                            self._segment_path = lambda: "nps"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps, [], name, value)


                        class Np(Entity):
                            """
                            Table of NP names
                            
                            .. attribute:: id1  <key>
                            
                            	none
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: rate
                            
                            	Packets per second
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**units**\: packet/s
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np, self).__init__()

                                self.yang_name = "np"
                                self.yang_parent_name = "nps"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.id1 = YLeaf(YType.int32, "id1")

                                self.rate = YLeaf(YType.int32, "rate")
                                self._segment_path = lambda: "np" + "[id1='" + self.id1.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np, ['id1', 'rate'], name, value)


        class Ltrace(Entity):
            """
            Ltrace Memory configuration
            
            .. attribute:: allocation_params
            
            	Select Ltrace mode and scale\-factor
            	**type**\:   :py:class:`AllocationParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams>`
            
            

            """

            _prefix = 'infra-ltrace-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(PreconfiguredNodes.PreconfiguredNode.Ltrace, self).__init__()

                self.yang_name = "ltrace"
                self.yang_parent_name = "preconfigured-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"allocation-params" : ("allocation_params", PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams)}
                self._child_list_classes = {}

                self.allocation_params = PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams()
                self.allocation_params.parent = self
                self._children_name_map["allocation_params"] = "allocation-params"
                self._children_yang_names.add("allocation-params")
                self._segment_path = lambda: "Cisco-IOS-XR-infra-ltrace-cfg:ltrace"


            class AllocationParams(Entity):
                """
                Select Ltrace mode and scale\-factor
                
                .. attribute:: mode
                
                	Select an allocation mode (static\:1, dynamic \:2)
                	**type**\:   :py:class:`InfraLtraceMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceMode>`
                
                .. attribute:: scale_factor
                
                	Select a scaling down factor
                	**type**\:   :py:class:`InfraLtraceScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceScale>`
                
                

                """

                _prefix = 'infra-ltrace-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams, self).__init__()

                    self.yang_name = "allocation-params"
                    self.yang_parent_name = "ltrace"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.mode = YLeaf(YType.enumeration, "mode")

                    self.scale_factor = YLeaf(YType.enumeration, "scale-factor")
                    self._segment_path = lambda: "allocation-params"

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams, ['mode', 'scale_factor'], name, value)

    def clone_ptr(self):
        self._top_entity = PreconfiguredNodes()
        return self._top_entity

