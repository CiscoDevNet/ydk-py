""" Cisco_IOS_XR_segment_routing_ms_common_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR segment\-routing\-ms\-common package configuration.

This module contains definitions
for the following management objects\:
  sr\: Segment Routing

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Sr(Entity):
    """
    Segment Routing
    
    

    """

    _prefix = 'segment-routing-ms-common-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Sr, self).__init__()
        self._top_entity = None

        self.yang_name = "sr"
        self.yang_parent_name = "Cisco-IOS-XR-segment-routing-ms-common-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-segment-routing-ms-common-cfg:sr"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = Sr()
        return self._top_entity



