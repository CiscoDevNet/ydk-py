""" Cisco_IOS_XR_fib_cef_lba_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fib\-cef\-lba package configuration.

This module contains definitions
for the following management objects\:
  fiblb\: FIB load\-balancing

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Fiblb(Entity):
    """
    FIB load\-balancing
    
    .. attribute:: fields
    
    	Specify number of fields used for the load balancing
    	**type**\: int
    
    	**range:** 0..1
    
    	**mandatory**\: True
    
    .. attribute:: payload
    
    	Payload Load\-Balancing
    	**type**\: bool
    
    	**mandatory**\: True
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'fib-cef-lba-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Fiblb, self).__init__()
        self._top_entity = None

        self.yang_name = "fiblb"
        self.yang_parent_name = "Cisco-IOS-XR-fib-cef-lba-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self.is_presence_container = True
        self._leafs = OrderedDict([
            ('fields', (YLeaf(YType.uint32, 'fields'), ['int'])),
            ('payload', (YLeaf(YType.boolean, 'payload'), ['bool'])),
        ])
        self.fields = None
        self.payload = None
        self._segment_path = lambda: "Cisco-IOS-XR-fib-cef-lba-cfg:fiblb"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Fiblb, ['fields', 'payload'], name, value)

    def clone_ptr(self):
        self._top_entity = Fiblb()
        return self._top_entity



