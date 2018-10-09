""" Cisco_IOS_XR_sysadmin_usb 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

This module defines the top level container for
all 'usb' commands for Sysadmin.

Copyright(c) 2018\-2019 by Cisco Systems, Inc.
All rights reserved.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Usb(Entity):
    """
    
    
    

    """

    _prefix = 'usb'
    _revision = '2018-05-23'

    def __init__(self):
        super(Usb, self).__init__()
        self._top_entity = None

        self.yang_name = "usb"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-usb"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-usb:usb"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = Usb()
        return self._top_entity

