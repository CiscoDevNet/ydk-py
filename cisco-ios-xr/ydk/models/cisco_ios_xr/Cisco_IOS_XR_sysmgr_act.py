""" Cisco_IOS_XR_sysmgr_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR sysmgr action package configuration.

Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class SysmgrProcessRestart(Entity):
    """
    Restart an XR process
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysmgr_act.SysmgrProcessRestart.Input>`
    
    

    """

    _prefix = 'sysmgr-act'
    _revision = '2017-03-03'

    def __init__(self):
        super(SysmgrProcessRestart, self).__init__()
        self._top_entity = None

        self.yang_name = "sysmgr-process-restart"
        self.yang_parent_name = "Cisco-IOS-XR-sysmgr-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = SysmgrProcessRestart.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-sysmgr-act:sysmgr-process-restart"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: process_name
        
        	XR process name or Job Id e.g. bgp, ospf
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: location
        
        	XR node identifier e.g. 0/RP0/CPU0, 0/0/CPU0
        	**type**\: str
        
        

        """

        _prefix = 'sysmgr-act'
        _revision = '2017-03-03'

        def __init__(self):
            super(SysmgrProcessRestart.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "sysmgr-process-restart"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                ('location', (YLeaf(YType.str, 'location'), ['str'])),
            ])
            self.process_name = None
            self.location = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysmgr-act:sysmgr-process-restart/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SysmgrProcessRestart.Input, ['process_name', 'location'], name, value)

    def clone_ptr(self):
        self._top_entity = SysmgrProcessRestart()
        return self._top_entity

