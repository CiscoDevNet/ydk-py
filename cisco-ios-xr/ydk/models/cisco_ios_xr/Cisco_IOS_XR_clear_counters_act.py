""" Cisco_IOS_XR_clear_counters_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR Controller to clear alarm counters.

Copyright (c) 2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class ClearCounters(Entity):
    """
    Execute clear counters operations
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clear_counters_act.ClearCounters.Input>`
    
    

    """

    _prefix = 'clear-counters-act'
    _revision = '2018-02-14'

    def __init__(self):
        super(ClearCounters, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-counters"
        self.yang_parent_name = "Cisco-IOS-XR-clear-counters-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearCounters.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-clear-counters-act:clear-counters"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: controller
        
        	Controller name in R/S/I/P format
        	**type**\: str
        
        

        """

        _prefix = 'clear-counters-act'
        _revision = '2018-02-14'

        def __init__(self):
            super(ClearCounters.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-counters"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('controller', (YLeaf(YType.str, 'controller'), ['str'])),
            ])
            self.controller = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-clear-counters-act:clear-counters/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClearCounters.Input, ['controller'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearCounters()
        return self._top_entity

