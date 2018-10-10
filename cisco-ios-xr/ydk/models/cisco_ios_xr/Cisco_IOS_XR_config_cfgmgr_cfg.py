""" Cisco_IOS_XR_config_cfgmgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR config\-cfgmgr package configuration.

This module contains definitions
for the following management objects\:
  cfgmgr\: Cfgmgr configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Cfgmgr(Entity):
    """
    Cfgmgr configuration
    
    .. attribute:: mode_exclusive
    
    	Enabled or Disabled
    	**type**\: bool
    
    	**default value**\: true
    
    

    """

    _prefix = 'config-cfgmgr-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Cfgmgr, self).__init__()
        self._top_entity = None

        self.yang_name = "cfgmgr"
        self.yang_parent_name = "Cisco-IOS-XR-config-cfgmgr-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('mode_exclusive', (YLeaf(YType.boolean, 'mode-exclusive'), ['bool'])),
        ])
        self.mode_exclusive = None
        self._segment_path = lambda: "Cisco-IOS-XR-config-cfgmgr-cfg:cfgmgr"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Cfgmgr, ['mode_exclusive'], name, value)

    def clone_ptr(self):
        self._top_entity = Cfgmgr()
        return self._top_entity

