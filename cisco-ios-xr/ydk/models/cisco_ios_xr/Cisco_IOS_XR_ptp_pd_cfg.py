""" Cisco_IOS_XR_ptp_pd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ptp\-pd package configuration.

This module contains definitions
for the following management objects\:
  log\-servo\-root\: Servo Log for Platform

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class LogServoRoot(Entity):
    """
    Servo Log for Platform
    
    .. attribute:: servo_event_enable
    
    	Enable Servo change log events
    	**type**\: bool
    
    

    """

    _prefix = 'ptp-pd-cfg'
    _revision = '2018-05-08'

    def __init__(self):
        super(LogServoRoot, self).__init__()
        self._top_entity = None

        self.yang_name = "log-servo-root"
        self.yang_parent_name = "Cisco-IOS-XR-ptp-pd-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('servo_event_enable', (YLeaf(YType.boolean, 'servo-event-enable'), ['bool'])),
        ])
        self.servo_event_enable = None
        self._segment_path = lambda: "Cisco-IOS-XR-ptp-pd-cfg:log-servo-root"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(LogServoRoot, ['servo_event_enable'], name, value)

    def clone_ptr(self):
        self._top_entity = LogServoRoot()
        return self._top_entity

