""" Cisco_IOS_XR_infra_placed_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

Copyright (c) 2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class PlacementReoptimize(_Entity_):
    """
    Migrate the processes, if placement is not optimal.
    
    
    

    """

    _prefix = 'placed-act'
    _revision = '2018-01-10'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(PlacementReoptimize, self).__init__()
        self._top_entity = None

        self.yang_name = "placement-reoptimize"
        self.yang_parent_name = "Cisco-IOS-XR-infra-placed-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-infra-placed-act:placement-reoptimize"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = PlacementReoptimize()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_placed_act as meta
        return meta._meta_table['PlacementReoptimize']['meta_info']


