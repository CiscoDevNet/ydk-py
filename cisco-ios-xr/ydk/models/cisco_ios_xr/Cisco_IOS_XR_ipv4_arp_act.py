""" Cisco_IOS_XR_ipv4_arp_act 

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




class ClearArpApiStatsApi(_Entity_):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_act.ClearArpApiStatsApi.Input>`
    
    

    """

    _prefix = 'arp-act'
    _revision = '2018-10-08'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(ClearArpApiStatsApi, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-arp-api-stats-api"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-arp-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearArpApiStatsApi.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-arp-act:clear-arp-api-stats-api"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: name
        
        	
        	**type**\: str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'arp-act'
        _revision = '2018-10-08'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ClearArpApiStatsApi.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-arp-api-stats-api"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
            ])
            self.name = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-arp-act:clear-arp-api-stats-api/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClearArpApiStatsApi.Input, ['name'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_act as meta
            return meta._meta_table['ClearArpApiStatsApi.Input']['meta_info']

    def clone_ptr(self):
        self._top_entity = ClearArpApiStatsApi()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_act as meta
        return meta._meta_table['ClearArpApiStatsApi']['meta_info']


class ClearArpApiStatsLocation(_Entity_):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_act.ClearArpApiStatsLocation.Input>`
    
    

    """

    _prefix = 'arp-act'
    _revision = '2018-10-08'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(ClearArpApiStatsLocation, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-arp-api-stats-location"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-arp-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearArpApiStatsLocation.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-arp-act:clear-arp-api-stats-location"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: node_location
        
        	
        	**type**\: str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'arp-act'
        _revision = '2018-10-08'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ClearArpApiStatsLocation.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-arp-api-stats-location"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('node_location', (YLeaf(YType.str, 'node-location'), ['str'])),
            ])
            self.node_location = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-arp-act:clear-arp-api-stats-location/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClearArpApiStatsLocation.Input, ['node_location'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_act as meta
            return meta._meta_table['ClearArpApiStatsLocation.Input']['meta_info']

    def clone_ptr(self):
        self._top_entity = ClearArpApiStatsLocation()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_act as meta
        return meta._meta_table['ClearArpApiStatsLocation']['meta_info']


