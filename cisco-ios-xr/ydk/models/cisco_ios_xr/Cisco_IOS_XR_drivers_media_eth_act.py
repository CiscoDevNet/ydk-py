""" Cisco_IOS_XR_drivers_media_eth_act 

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




class ClearControllerCounters(_Entity_):
    """
    Clear Ethernet MAC ASIC statistics.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_act.ClearControllerCounters.Input>`
    
    

    """

    _prefix = 'eth-drvr-act'
    _revision = '2018-02-12'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(ClearControllerCounters, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-controller-counters"
        self.yang_parent_name = "Cisco-IOS-XR-drivers-media-eth-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearControllerCounters.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-drivers-media-eth-act:clear-controller-counters"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: controller_name
        
        	Controller name
        	**type**\: str
        
        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'eth-drvr-act'
        _revision = '2018-02-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ClearControllerCounters.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-controller-counters"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('controller_name', (YLeaf(YType.str, 'controller-name'), ['str'])),
            ])
            self.controller_name = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-drivers-media-eth-act:clear-controller-counters/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClearControllerCounters.Input, ['controller_name'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_act as meta
            return meta._meta_table['ClearControllerCounters.Input']['meta_info']

    def clone_ptr(self):
        self._top_entity = ClearControllerCounters()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_act as meta
        return meta._meta_table['ClearControllerCounters']['meta_info']


