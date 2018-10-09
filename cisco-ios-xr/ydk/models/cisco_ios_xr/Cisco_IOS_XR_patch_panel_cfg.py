""" Cisco_IOS_XR_patch_panel_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR patch\-panel package configuration.

This module contains definitions
for the following management objects\:
  patch\-panel\: patch\-panel service submode

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class PatchPanel(Entity):
    """
    patch\-panel service submode
    
    .. attribute:: enable
    
    	Enable patch\-panel service
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    	**mandatory**\: True
    
    .. attribute:: user_name
    
    	User name to be used for Authentication with Patch\-Panel
    	**type**\: str
    
    .. attribute:: password
    
    	Password name to be used for Authentication with Patch\-Panel
    	**type**\: str
    
    	**pattern:** (!.+)\|([^!].+)
    
    .. attribute:: ipv4
    
    	IP address for patch\-panel
    	**type**\: str
    
    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'patch-panel-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(PatchPanel, self).__init__()
        self._top_entity = None

        self.yang_name = "patch-panel"
        self.yang_parent_name = "Cisco-IOS-XR-patch-panel-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self.is_presence_container = True
        self._leafs = OrderedDict([
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ('user_name', (YLeaf(YType.str, 'user-name'), ['str'])),
            ('password', (YLeaf(YType.str, 'password'), ['str'])),
            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
        ])
        self.enable = None
        self.user_name = None
        self.password = None
        self.ipv4 = None
        self._segment_path = lambda: "Cisco-IOS-XR-patch-panel-cfg:patch-panel"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PatchPanel, ['enable', 'user_name', 'password', 'ipv4'], name, value)

    def clone_ptr(self):
        self._top_entity = PatchPanel()
        return self._top_entity

