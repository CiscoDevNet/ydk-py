""" Cisco_IOS_XR_cdp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR cdp package configuration.

This module contains definitions
for the following management objects\:
  cdp\: Global CDP configuration data

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Cdp(Entity):
    """
    Global CDP configuration data
    
    .. attribute:: advertise_v1_only
    
    	Enable CDPv1 only advertisements
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: enable
    
    	Enable or disable CDP globally
    	**type**\:  bool
    
    	**default value**\: true
    
    .. attribute:: hold_time
    
    	Length of time (in sec) that the receiver must keep a CDP packet
    	**type**\:  int
    
    	**range:** 10..255
    
    	**default value**\: 180
    
    .. attribute:: log_adjacency
    
    	Enable logging of adjacency changes
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: timer
    
    	Specify the rate at which CDP packets are sent
    	**type**\:  int
    
    	**range:** 5..255
    
    	**default value**\: 60
    
    

    """

    _prefix = 'cdp-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        super(Cdp, self).__init__()
        self._top_entity = None

        self.yang_name = "cdp"
        self.yang_parent_name = "Cisco-IOS-XR-cdp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

        self.advertise_v1_only = YLeaf(YType.empty, "advertise-v1-only")

        self.enable = YLeaf(YType.boolean, "enable")

        self.hold_time = YLeaf(YType.uint32, "hold-time")

        self.log_adjacency = YLeaf(YType.empty, "log-adjacency")

        self.timer = YLeaf(YType.uint32, "timer")
        self._segment_path = lambda: "Cisco-IOS-XR-cdp-cfg:cdp"

    def __setattr__(self, name, value):
        self._perform_setattr(Cdp, ['advertise_v1_only', 'enable', 'hold_time', 'log_adjacency', 'timer'], name, value)

    def clone_ptr(self):
        self._top_entity = Cdp()
        return self._top_entity

