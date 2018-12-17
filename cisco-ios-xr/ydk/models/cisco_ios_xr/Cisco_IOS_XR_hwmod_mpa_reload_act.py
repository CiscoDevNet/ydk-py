""" Cisco_IOS_XR_hwmod_mpa_reload_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR MPA reload action package configuration.

Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class HwModuleSubslot(Entity):
    """
    Execute subslot h/w module operations
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_hwmod_mpa_reload_act.HwModuleSubslot.Input>`
    
    

    """

    _prefix = 'hwmod-mpa-reload-act'
    _revision = '2016-06-30'

    def __init__(self):
        super(HwModuleSubslot, self).__init__()
        self._top_entity = None

        self.yang_name = "hw-module-subslot"
        self.yang_parent_name = "Cisco-IOS-XR-hwmod-mpa-reload-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = HwModuleSubslot.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-hwmod-mpa-reload-act:hw-module-subslot"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: subslot
        
        	Fully qualified location specification
        	**type**\: str
        
        .. attribute:: reload
        
        	Cycle subslot h/w reset
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'hwmod-mpa-reload-act'
        _revision = '2016-06-30'

        def __init__(self):
            super(HwModuleSubslot.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "hw-module-subslot"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('subslot', (YLeaf(YType.str, 'subslot'), ['str'])),
                ('reload', (YLeaf(YType.empty, 'reload'), ['Empty'])),
            ])
            self.subslot = None
            self.reload = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-hwmod-mpa-reload-act:hw-module-subslot/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HwModuleSubslot.Input, ['subslot', 'reload'], name, value)

    def clone_ptr(self):
        self._top_entity = HwModuleSubslot()
        return self._top_entity

