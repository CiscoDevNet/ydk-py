""" Cisco_IOS_XR_upgrade_fpd_admin_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR upgrade\-fpd package admin\-plane configuration.

This module contains definitions
for the following management objects\:
  fpd\: Configuration for fpd auto\-upgrade

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Fpd(Entity):
    """
    Configuration for fpd auto\-upgrade
    
    .. attribute:: auto_upgrade
    
    	Variable for fpd auto\-upgrade enable/disable
    	**type**\: bool
    
    .. attribute:: auto_reload
    
    	Variable for fpd auto\-reload enable/disable
    	**type**\: bool
    
    

    """

    _prefix = 'upgrade-fpd-admin-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Fpd, self).__init__()
        self._top_entity = None

        self.yang_name = "fpd"
        self.yang_parent_name = "Cisco-IOS-XR-upgrade-fpd-admin-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('auto_upgrade', (YLeaf(YType.boolean, 'auto-upgrade'), ['bool'])),
            ('auto_reload', (YLeaf(YType.boolean, 'auto-reload'), ['bool'])),
        ])
        self.auto_upgrade = None
        self.auto_reload = None
        self._segment_path = lambda: "Cisco-IOS-XR-upgrade-fpd-admin-cfg:fpd"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Fpd, ['auto_upgrade', 'auto_reload'], name, value)

    def clone_ptr(self):
        self._top_entity = Fpd()
        return self._top_entity



