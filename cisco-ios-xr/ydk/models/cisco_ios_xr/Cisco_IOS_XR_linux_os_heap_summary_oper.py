""" Cisco_IOS_XR_linux_os_heap_summary_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR linux\-os\-heap\-summary package operational data.

This module contains definitions
for the following management objects\:
  heap\-summary\: Heap Summary

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
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




class HeapSummary(_Entity_):
    """
    Heap Summary
    
    .. attribute:: location_descriptions
    
    	Location
    	**type**\:  :py:class:`LocationDescriptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_heap_summary_oper.HeapSummary.LocationDescriptions>`
    
    	**config**\: False
    
    .. attribute:: all
    
    	All locations
    	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_heap_summary_oper.HeapSummary.All>`
    
    	**config**\: False
    
    

    """

    _prefix = 'linux-os-heap-summary-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(HeapSummary, self).__init__()
        self._top_entity = None

        self.yang_name = "heap-summary"
        self.yang_parent_name = "Cisco-IOS-XR-linux-os-heap-summary-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("location-descriptions", ("location_descriptions", HeapSummary.LocationDescriptions)), ("all", ("all", HeapSummary.All))])
        self._leafs = OrderedDict()

        self.location_descriptions = HeapSummary.LocationDescriptions()
        self.location_descriptions.parent = self
        self._children_name_map["location_descriptions"] = "location-descriptions"

        self.all = HeapSummary.All()
        self.all.parent = self
        self._children_name_map["all"] = "all"
        self._segment_path = lambda: "Cisco-IOS-XR-linux-os-heap-summary-oper:heap-summary"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HeapSummary, [], name, value)


    class LocationDescriptions(_Entity_):
        """
        Location
        
        .. attribute:: location_description
        
        	Location specified in location
        	**type**\: list of  		 :py:class:`LocationDescription <ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_heap_summary_oper.HeapSummary.LocationDescriptions.LocationDescription>`
        
        	**config**\: False
        
        

        """

        _prefix = 'linux-os-heap-summary-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(HeapSummary.LocationDescriptions, self).__init__()

            self.yang_name = "location-descriptions"
            self.yang_parent_name = "heap-summary"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("location-description", ("location_description", HeapSummary.LocationDescriptions.LocationDescription))])
            self._leafs = OrderedDict()

            self.location_description = YList(self)
            self._segment_path = lambda: "location-descriptions"
            self._absolute_path = lambda: "Cisco-IOS-XR-linux-os-heap-summary-oper:heap-summary/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HeapSummary.LocationDescriptions, [], name, value)


        class LocationDescription(_Entity_):
            """
            Location specified in location
            
            .. attribute:: node  (key)
            
            	Node location
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: show_output
            
            	string output
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'linux-os-heap-summary-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(HeapSummary.LocationDescriptions.LocationDescription, self).__init__()

                self.yang_name = "location-description"
                self.yang_parent_name = "location-descriptions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                    ('show_output', (YLeaf(YType.str, 'show-output'), ['str'])),
                ])
                self.node = None
                self.show_output = None
                self._segment_path = lambda: "location-description" + "[node='" + str(self.node) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-linux-os-heap-summary-oper:heap-summary/location-descriptions/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HeapSummary.LocationDescriptions.LocationDescription, ['node', 'show_output'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_linux_os_heap_summary_oper as meta
                return meta._meta_table['HeapSummary.LocationDescriptions.LocationDescription']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_linux_os_heap_summary_oper as meta
            return meta._meta_table['HeapSummary.LocationDescriptions']['meta_info']


    class All(_Entity_):
        """
        All locations
        
        .. attribute:: show_output
        
        	string output
        	**type**\: str
        
        	**config**\: False
        
        

        """

        _prefix = 'linux-os-heap-summary-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(HeapSummary.All, self).__init__()

            self.yang_name = "all"
            self.yang_parent_name = "heap-summary"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('show_output', (YLeaf(YType.str, 'show-output'), ['str'])),
            ])
            self.show_output = None
            self._segment_path = lambda: "all"
            self._absolute_path = lambda: "Cisco-IOS-XR-linux-os-heap-summary-oper:heap-summary/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HeapSummary.All, ['show_output'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_linux_os_heap_summary_oper as meta
            return meta._meta_table['HeapSummary.All']['meta_info']

    def clone_ptr(self):
        self._top_entity = HeapSummary()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_linux_os_heap_summary_oper as meta
        return meta._meta_table['HeapSummary']['meta_info']


