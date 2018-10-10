""" Cisco_IOS_XR_freqsync_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR freqsync package configuration.

This module contains definitions
for the following management objects\:
  frequency\-synchronization\: frequency synchronization

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg,
  Cisco\-IOS\-XR\-ifmgr\-cfg
  Cisco\-IOS\-XR\-config\-mda\-cfg
modules with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FsyncClockSource(Enum):
    """
    FsyncClockSource (Enum Class)

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
    FsyncSourceSelectionLogging (Enum Class)

    Fsync source selection logging

    .. data:: changes = 1

    	Log both selection changes and errors

    .. data:: errors = 2

    	Log selection errors

    """

    changes = Enum.YLeaf(1, "changes")

    errors = Enum.YLeaf(2, "errors")


class FsyncSystemTimingMode(Enum):
    """
    FsyncSystemTimingMode (Enum Class)

    Fsync system timing mode

    .. data:: line_only = 2

    	Line-interfaces only

    .. data:: clock_only = 3

    	Clock-interfaces only

    """

    line_only = Enum.YLeaf(2, "line-only")

    clock_only = Enum.YLeaf(3, "clock-only")



class FrequencySynchronization(Entity):
    """
    frequency synchronization
    
    .. attribute:: quality_level_option
    
    	Quality level option
    	**type**\:  :py:class:`FsyncQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlOption>`
    
    	**default value**\: option-1
    
    .. attribute:: enable
    
    	Enable Frequency Synchronization
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: source_selection_logging
    
    	Source selection logging option
    	**type**\:  :py:class:`FsyncSourceSelectionLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_cfg.FsyncSourceSelectionLogging>`
    
    .. attribute:: clock_interface_source_type
    
    	Clock interface source type
    	**type**\:  :py:class:`FsyncClockSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_cfg.FsyncClockSource>`
    
    .. attribute:: system_timing_mode
    
    	System timing mode
    	**type**\:  :py:class:`FsyncSystemTimingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_cfg.FsyncSystemTimingMode>`
    
    

    """

    _prefix = 'freqsync-cfg'
    _revision = '2017-09-30'

    def __init__(self):
        super(FrequencySynchronization, self).__init__()
        self._top_entity = None

        self.yang_name = "frequency-synchronization"
        self.yang_parent_name = "Cisco-IOS-XR-freqsync-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlOption', '')])),
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ('source_selection_logging', (YLeaf(YType.enumeration, 'source-selection-logging'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_cfg', 'FsyncSourceSelectionLogging', '')])),
            ('clock_interface_source_type', (YLeaf(YType.enumeration, 'clock-interface-source-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_cfg', 'FsyncClockSource', '')])),
            ('system_timing_mode', (YLeaf(YType.enumeration, 'system-timing-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_cfg', 'FsyncSystemTimingMode', '')])),
        ])
        self.quality_level_option = None
        self.enable = None
        self.source_selection_logging = None
        self.clock_interface_source_type = None
        self.system_timing_mode = None
        self._segment_path = lambda: "Cisco-IOS-XR-freqsync-cfg:frequency-synchronization"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(FrequencySynchronization, ['quality_level_option', 'enable', 'source_selection_logging', 'clock_interface_source_type', 'system_timing_mode'], name, value)

    def clone_ptr(self):
        self._top_entity = FrequencySynchronization()
        return self._top_entity

