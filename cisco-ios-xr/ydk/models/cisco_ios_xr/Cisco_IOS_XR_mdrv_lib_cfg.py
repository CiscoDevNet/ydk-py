""" Cisco_IOS_XR_mdrv_lib_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mdrv\-lib package configuration.

This module contains definitions
for the following management objects\:
  fast\-shutdown\: Fast Shutdown configuration

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




class FastShutdown(Entity):
    """
    Fast Shutdown configuration
    
    .. attribute:: ethernet
    
    	Enable Fast Shutdown for all Ethernet interfaces
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'mdrv-lib-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(FastShutdown, self).__init__()
        self._top_entity = None

        self.yang_name = "fast-shutdown"
        self.yang_parent_name = "Cisco-IOS-XR-mdrv-lib-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('ethernet', (YLeaf(YType.empty, 'ethernet'), ['Empty'])),
        ])
        self.ethernet = None
        self._segment_path = lambda: "Cisco-IOS-XR-mdrv-lib-cfg:fast-shutdown"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(FastShutdown, ['ethernet'], name, value)

    def clone_ptr(self):
        self._top_entity = FastShutdown()
        return self._top_entity

