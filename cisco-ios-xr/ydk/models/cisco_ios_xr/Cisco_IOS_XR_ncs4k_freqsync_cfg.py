""" Cisco_IOS_XR_ncs4k_freqsync_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs4k\-freqsync package configuration.

This module contains definitions
for the following management objects\:
  clock\-interface\: Configuration for a clock interface
  frequency\-synchronization\: frequency synchronization

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg,
  Cisco\-IOS\-XR\-ifmgr\-cfg
modules with configuration data.

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class FsyncClockSource(Enum):
    """
    FsyncClockSource

    Fsync clock source

    .. data:: system = 1

    	System

    .. data:: independent = 3

    	Independent

    """

    system = Enum.YLeaf(1, "system")

    independent = Enum.YLeaf(3, "independent")


class FsyncSourceSelectionLogging(Enum):
    """
    FsyncSourceSelectionLogging

    Fsync source selection logging

    .. data:: changes = 1

    	Log selection changes

    .. data:: errors = 2

    	Log selection errors

    """

    changes = Enum.YLeaf(1, "changes")

    errors = Enum.YLeaf(2, "errors")


class FsyncSystemTimingMode(Enum):
    """
    FsyncSystemTimingMode

    Fsync system timing mode

    .. data:: line_only = 2

    	Line-interfaces only

    .. data:: clock_only = 3

    	Clock-interfaces only

    """

    line_only = Enum.YLeaf(2, "line-only")

    clock_only = Enum.YLeaf(3, "clock-only")



class ClockInterface(Entity):
    """
    Configuration for a clock interface
    
    .. attribute:: clocks
    
    	Configuration for a clock interface
    	**type**\:   :py:class:`Clocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs4k_freqsync_cfg.ClockInterface.Clocks>`
    
    

    """

    _prefix = 'ncs4k-freqsync-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(ClockInterface, self).__init__()
        self._top_entity = None

        self.yang_name = "clock-interface"
        self.yang_parent_name = "Cisco-IOS-XR-ncs4k-freqsync-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"clocks" : ("clocks", ClockInterface.Clocks)}
        self._child_list_classes = {}

        self.clocks = ClockInterface.Clocks()
        self.clocks.parent = self
        self._children_name_map["clocks"] = "clocks"
        self._children_yang_names.add("clocks")
        self._segment_path = lambda: "Cisco-IOS-XR-ncs4k-freqsync-cfg:clock-interface"


    class Clocks(Entity):
        """
        Configuration for a clock interface
        
        .. attribute:: clock
        
        	Configuration for a clock interface
        	**type**\: list of    :py:class:`Clock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs4k_freqsync_cfg.ClockInterface.Clocks.Clock>`
        
        

        """

        _prefix = 'ncs4k-freqsync-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(ClockInterface.Clocks, self).__init__()

            self.yang_name = "clocks"
            self.yang_parent_name = "clock-interface"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"clock" : ("clock", ClockInterface.Clocks.Clock)}

            self.clock = YList(self)
            self._segment_path = lambda: "clocks"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs4k-freqsync-cfg:clock-interface/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ClockInterface.Clocks, [], name, value)


        class Clock(Entity):
            """
            Configuration for a clock interface
            
            .. attribute:: clock_name  <key>
            
            	Clock Name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: frequency_synchronization
            
            	Frequency Synchronization clock configuraiton
            	**type**\:   :py:class:`FrequencySynchronization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs4k_freqsync_cfg.ClockInterface.Clocks.Clock.FrequencySynchronization>`
            
            

            """

            _prefix = 'ncs4k-freqsync-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ClockInterface.Clocks.Clock, self).__init__()

                self.yang_name = "clock"
                self.yang_parent_name = "clocks"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"frequency-synchronization" : ("frequency_synchronization", ClockInterface.Clocks.Clock.FrequencySynchronization)}
                self._child_list_classes = {}

                self.clock_name = YLeaf(YType.str, "clock-name")

                self.frequency_synchronization = ClockInterface.Clocks.Clock.FrequencySynchronization()
                self.frequency_synchronization.parent = self
                self._children_name_map["frequency_synchronization"] = "frequency-synchronization"
                self._children_yang_names.add("frequency-synchronization")
                self._segment_path = lambda: "clock" + "[clock-name='" + self.clock_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ncs4k-freqsync-cfg:clock-interface/clocks/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ClockInterface.Clocks.Clock, ['clock_name'], name, value)


            class FrequencySynchronization(Entity):
                """
                Frequency Synchronization clock configuraiton
                
                .. attribute:: input_quality_level
                
                	Set the input quality level
                	**type**\:   :py:class:`InputQualityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs4k_freqsync_cfg.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel>`
                
                .. attribute:: output_quality_level
                
                	Set the output quality level
                	**type**\:   :py:class:`OutputQualityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs4k_freqsync_cfg.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel>`
                
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

                _prefix = 'ncs4k-freqsync-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ClockInterface.Clocks.Clock.FrequencySynchronization, self).__init__()

                    self.yang_name = "frequency-synchronization"
                    self.yang_parent_name = "clock"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"input-quality-level" : ("input_quality_level", ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel), "output-quality-level" : ("output_quality_level", ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel)}
                    self._child_list_classes = {}

                    self.priority = YLeaf(YType.uint32, "priority")

                    self.selection_input = YLeaf(YType.empty, "selection-input")

                    self.ssm_disable = YLeaf(YType.empty, "ssm-disable")

                    self.time_of_day_priority = YLeaf(YType.uint32, "time-of-day-priority")

                    self.wait_to_restore_time = YLeaf(YType.uint32, "wait-to-restore-time")

                    self.input_quality_level = ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel()
                    self.input_quality_level.parent = self
                    self._children_name_map["input_quality_level"] = "input-quality-level"
                    self._children_yang_names.add("input-quality-level")

                    self.output_quality_level = ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel()
                    self.output_quality_level.parent = self
                    self._children_name_map["output_quality_level"] = "output-quality-level"
                    self._children_yang_names.add("output-quality-level")
                    self._segment_path = lambda: "frequency-synchronization"

                def __setattr__(self, name, value):
                    self._perform_setattr(ClockInterface.Clocks.Clock.FrequencySynchronization, ['priority', 'selection_input', 'ssm_disable', 'time_of_day_priority', 'wait_to_restore_time'], name, value)


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

                    _prefix = 'ncs4k-freqsync-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel, self).__init__()

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
                        self._perform_setattr(ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel, ['exact_quality_level_value', 'max_quality_level_value', 'min_quality_level_value', 'quality_level_option'], name, value)


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

                    _prefix = 'ncs4k-freqsync-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel, self).__init__()

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
                        self._perform_setattr(ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel, ['exact_quality_level_value', 'max_quality_level_value', 'min_quality_level_value', 'quality_level_option'], name, value)

    def clone_ptr(self):
        self._top_entity = ClockInterface()
        return self._top_entity

class FrequencySynchronization(Entity):
    """
    frequency synchronization
    
    .. attribute:: clock_interface_source_type
    
    	Clock interface source type
    	**type**\:   :py:class:`FsyncClockSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs4k_freqsync_cfg.FsyncClockSource>`
    
    .. attribute:: enable
    
    	Enable Frequency Synchronization
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: quality_level_option
    
    	Quality level option
    	**type**\:   :py:class:`FsyncQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlOption>`
    
    	**default value**\: option-1
    
    .. attribute:: source_selection_logging
    
    	Source selection logging option
    	**type**\:   :py:class:`FsyncSourceSelectionLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs4k_freqsync_cfg.FsyncSourceSelectionLogging>`
    
    .. attribute:: system_timing_mode
    
    	System timing mode
    	**type**\:   :py:class:`FsyncSystemTimingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs4k_freqsync_cfg.FsyncSystemTimingMode>`
    
    

    """

    _prefix = 'ncs4k-freqsync-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(FrequencySynchronization, self).__init__()
        self._top_entity = None

        self.yang_name = "frequency-synchronization"
        self.yang_parent_name = "Cisco-IOS-XR-ncs4k-freqsync-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

        self.clock_interface_source_type = YLeaf(YType.enumeration, "clock-interface-source-type")

        self.enable = YLeaf(YType.empty, "enable")

        self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

        self.source_selection_logging = YLeaf(YType.enumeration, "source-selection-logging")

        self.system_timing_mode = YLeaf(YType.enumeration, "system-timing-mode")
        self._segment_path = lambda: "Cisco-IOS-XR-ncs4k-freqsync-cfg:frequency-synchronization"

    def __setattr__(self, name, value):
        self._perform_setattr(FrequencySynchronization, ['clock_interface_source_type', 'enable', 'quality_level_option', 'source_selection_logging', 'system_timing_mode'], name, value)

    def clone_ptr(self):
        self._top_entity = FrequencySynchronization()
        return self._top_entity

