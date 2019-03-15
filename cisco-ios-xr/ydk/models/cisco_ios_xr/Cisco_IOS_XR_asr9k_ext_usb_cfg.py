""" Cisco_IOS_XR_asr9k_ext_usb_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-ext\-usb package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\-ext\-usb\: External USB configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class HardwareModuleExtUsb(Entity):
    """
    External USB configuration
    
    .. attribute:: disable
    
    	External USB disable
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'asr9k-ext-usb-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(HardwareModuleExtUsb, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module-ext-usb"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-ext-usb-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('disable', (YLeaf(YType.empty, 'disable'), ['Empty'])),
        ])
        self.disable = None
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-ext-usb-cfg:hardware-module-ext-usb"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HardwareModuleExtUsb, ['disable'], name, value)

    def clone_ptr(self):
        self._top_entity = HardwareModuleExtUsb()
        return self._top_entity



