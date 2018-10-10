""" Cisco_IOS_XR_shellutil_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR shellutil package configuration.

This module contains definitions
for the following management objects\:
  host\-names\: Container Schema for hostname configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class HostNames(Entity):
    """
    Container Schema for hostname configuration
    
    .. attribute:: host_name
    
    	Configure system's hostname
    	**type**\: str
    
    

    """

    _prefix = 'shellutil-cfg'
    _revision = '2015-10-12'

    def __init__(self):
        super(HostNames, self).__init__()
        self._top_entity = None

        self.yang_name = "host-names"
        self.yang_parent_name = "Cisco-IOS-XR-shellutil-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('host_name', (YLeaf(YType.str, 'host-name'), ['str'])),
        ])
        self.host_name = None
        self._segment_path = lambda: "Cisco-IOS-XR-shellutil-cfg:host-names"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HostNames, ['host_name'], name, value)

    def clone_ptr(self):
        self._top_entity = HostNames()
        return self._top_entity

