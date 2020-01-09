""" Cisco_IOS_XR_controller_ains_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR Controller AINS configuration.

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




class ControllerAinsSoak(_Entity_):
    """
    Execute ains soak configuration operations
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_ains_act.ControllerAinsSoak.Input>`
    
    

    """

    _prefix = 'controller-ains-act'
    _revision = '2018-01-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(ControllerAinsSoak, self).__init__()
        self._top_entity = None

        self.yang_name = "controller-ains-soak"
        self.yang_parent_name = "Cisco-IOS-XR-controller-ains-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ControllerAinsSoak.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-controller-ains-act:controller-ains-soak"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: controller
        
        	Controller name in R/S/I/P format
        	**type**\: str
        
        .. attribute:: hours
        
        	Hours in range of 0\-48
        	**type**\: int
        
        	**range:** 0..48
        
        .. attribute:: minutes
        
        	Minutes in range of 0\-59
        	**type**\: int
        
        	**range:** 0..59
        
        

        """

        _prefix = 'controller-ains-act'
        _revision = '2018-01-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ControllerAinsSoak.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "controller-ains-soak"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('controller', (YLeaf(YType.str, 'controller'), ['str'])),
                ('hours', (YLeaf(YType.uint32, 'hours'), ['int'])),
                ('minutes', (YLeaf(YType.uint32, 'minutes'), ['int'])),
            ])
            self.controller = None
            self.hours = None
            self.minutes = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-controller-ains-act:controller-ains-soak/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ControllerAinsSoak.Input, ['controller', 'hours', 'minutes'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_ains_act as meta
            return meta._meta_table['ControllerAinsSoak.Input']['meta_info']

    def clone_ptr(self):
        self._top_entity = ControllerAinsSoak()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_ains_act as meta
        return meta._meta_table['ControllerAinsSoak']['meta_info']


