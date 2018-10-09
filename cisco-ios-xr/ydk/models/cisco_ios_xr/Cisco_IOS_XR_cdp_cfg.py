""" Cisco_IOS_XR_cdp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR cdp package configuration.

This module contains definitions
for the following management objects\:
  cdp\: Global CDP configuration data

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Cdp(Entity):
    """
    Global CDP configuration data
    
    .. attribute:: timer
    
    	Specify the rate at which CDP packets are sent
    	**type**\: int
    
    	**range:** 5..254
    
    	**default value**\: 60
    
    .. attribute:: advertise_v1_only
    
    	Enable CDPv1 only advertisements
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: enable
    
    	Enable or disable CDP globally
    	**type**\: bool
    
    	**default value**\: true
    
    .. attribute:: hold_time
    
    	Length of time (in sec) that the receiver must keep a CDP packet
    	**type**\: int
    
    	**range:** 10..255
    
    	**default value**\: 180
    
    .. attribute:: log_adjacency
    
    	Enable logging of adjacency changes
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'cdp-cfg'
    _revision = '2017-08-16'

    def __init__(self):
        super(Cdp, self).__init__()
        self._top_entity = None

        self.yang_name = "cdp"
        self.yang_parent_name = "Cisco-IOS-XR-cdp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('timer', (YLeaf(YType.uint32, 'timer'), ['int'])),
            ('advertise_v1_only', (YLeaf(YType.empty, 'advertise-v1-only'), ['Empty'])),
            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
            ('hold_time', (YLeaf(YType.uint32, 'hold-time'), ['int'])),
            ('log_adjacency', (YLeaf(YType.empty, 'log-adjacency'), ['Empty'])),
        ])
        self.timer = None
        self.advertise_v1_only = None
        self.enable = None
        self.hold_time = None
        self.log_adjacency = None
        self._segment_path = lambda: "Cisco-IOS-XR-cdp-cfg:cdp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Cdp, ['timer', 'advertise_v1_only', 'enable', 'hold_time', 'log_adjacency'], name, value)

    def clone_ptr(self):
        self._top_entity = Cdp()
        return self._top_entity

