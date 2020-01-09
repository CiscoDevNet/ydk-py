""" Cisco_IOS_XR_infra_statsd_act 

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




class ClearCountersController(_Entity_):
    """
    Controller name.
    
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_act.ClearCountersController.Input>`
    
    

    """

    _prefix = 'statsd-act'
    _revision = '2018-01-10'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(ClearCountersController, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-counters-controller"
        self.yang_parent_name = "Cisco-IOS-XR-infra-statsd-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearCountersController.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-statsd-act:clear-counters-controller"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: controller_name
        
        	Controller name
        	**type**\: str
        
        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'statsd-act'
        _revision = '2018-01-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ClearCountersController.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-counters-controller"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('controller_name', (YLeaf(YType.str, 'controller-name'), ['str'])),
            ])
            self.controller_name = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-statsd-act:clear-counters-controller/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClearCountersController.Input, ['controller_name'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_act as meta
            return meta._meta_table['ClearCountersController.Input']['meta_info']

    def clone_ptr(self):
        self._top_entity = ClearCountersController()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_act as meta
        return meta._meta_table['ClearCountersController']['meta_info']


class ClearCountersAll(_Entity_):
    """
    Clear counters on all interfaces.
    
    
    

    """

    _prefix = 'statsd-act'
    _revision = '2018-01-10'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(ClearCountersAll, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-counters-all"
        self.yang_parent_name = "Cisco-IOS-XR-infra-statsd-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-infra-statsd-act:clear-counters-all"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = ClearCountersAll()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_act as meta
        return meta._meta_table['ClearCountersAll']['meta_info']


class ClearCountersInterface(_Entity_):
    """
    Clear counters for interface.
    
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_act.ClearCountersInterface.Input>`
    
    

    """

    _prefix = 'statsd-act'
    _revision = '2018-01-10'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(ClearCountersInterface, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-counters-interface"
        self.yang_parent_name = "Cisco-IOS-XR-infra-statsd-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearCountersInterface.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-statsd-act:clear-counters-interface"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: interface_name
        
        	Interface name
        	**type**\: str
        
        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'statsd-act'
        _revision = '2018-01-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ClearCountersInterface.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-counters-interface"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
            ])
            self.interface_name = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-statsd-act:clear-counters-interface/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClearCountersInterface.Input, ['interface_name'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_act as meta
            return meta._meta_table['ClearCountersInterface.Input']['meta_info']

    def clone_ptr(self):
        self._top_entity = ClearCountersInterface()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_act as meta
        return meta._meta_table['ClearCountersInterface']['meta_info']


