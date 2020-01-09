""" Cisco_IOS_XR_mediasvr_linux_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mediasvr\-linux package operational data.

This module contains definitions
for the following management objects\:
  media\-svr\: Media server CLI operations

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




class MediaSvr(_Entity_):
    """
    Media server CLI operations
    
    .. attribute:: all
    
    	Show Media bag
    	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mediasvr_linux_oper.MediaSvr.All>`
    
    	**config**\: False
    
    .. attribute:: location_descriptions
    
    	Show Media
    	**type**\:  :py:class:`LocationDescriptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mediasvr_linux_oper.MediaSvr.LocationDescriptions>`
    
    	**config**\: False
    
    

    """

    _prefix = 'mediasvr-linux-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(MediaSvr, self).__init__()
        self._top_entity = None

        self.yang_name = "media-svr"
        self.yang_parent_name = "Cisco-IOS-XR-mediasvr-linux-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("all", ("all", MediaSvr.All)), ("location-descriptions", ("location_descriptions", MediaSvr.LocationDescriptions))])
        self._leafs = OrderedDict()

        self.all = MediaSvr.All()
        self.all.parent = self
        self._children_name_map["all"] = "all"

        self.location_descriptions = MediaSvr.LocationDescriptions()
        self.location_descriptions.parent = self
        self._children_name_map["location_descriptions"] = "location-descriptions"
        self._segment_path = lambda: "Cisco-IOS-XR-mediasvr-linux-oper:media-svr"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(MediaSvr, [], name, value)


    class All(_Entity_):
        """
        Show Media bag
        
        .. attribute:: show_output
        
        	string output
        	**type**\: str
        
        	**config**\: False
        
        

        """

        _prefix = 'mediasvr-linux-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(MediaSvr.All, self).__init__()

            self.yang_name = "all"
            self.yang_parent_name = "media-svr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('show_output', (YLeaf(YType.str, 'show-output'), ['str'])),
            ])
            self.show_output = None
            self._segment_path = lambda: "all"
            self._absolute_path = lambda: "Cisco-IOS-XR-mediasvr-linux-oper:media-svr/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MediaSvr.All, ['show_output'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mediasvr_linux_oper as meta
            return meta._meta_table['MediaSvr.All']['meta_info']


    class LocationDescriptions(_Entity_):
        """
        Show Media
        
        .. attribute:: location_description
        
        	Location specified in location
        	**type**\: list of  		 :py:class:`LocationDescription <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mediasvr_linux_oper.MediaSvr.LocationDescriptions.LocationDescription>`
        
        	**config**\: False
        
        

        """

        _prefix = 'mediasvr-linux-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(MediaSvr.LocationDescriptions, self).__init__()

            self.yang_name = "location-descriptions"
            self.yang_parent_name = "media-svr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("location-description", ("location_description", MediaSvr.LocationDescriptions.LocationDescription))])
            self._leafs = OrderedDict()

            self.location_description = YList(self)
            self._segment_path = lambda: "location-descriptions"
            self._absolute_path = lambda: "Cisco-IOS-XR-mediasvr-linux-oper:media-svr/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MediaSvr.LocationDescriptions, [], name, value)


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

            _prefix = 'mediasvr-linux-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(MediaSvr.LocationDescriptions.LocationDescription, self).__init__()

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
                self._absolute_path = lambda: "Cisco-IOS-XR-mediasvr-linux-oper:media-svr/location-descriptions/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MediaSvr.LocationDescriptions.LocationDescription, ['node', 'show_output'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mediasvr_linux_oper as meta
                return meta._meta_table['MediaSvr.LocationDescriptions.LocationDescription']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mediasvr_linux_oper as meta
            return meta._meta_table['MediaSvr.LocationDescriptions']['meta_info']

    def clone_ptr(self):
        self._top_entity = MediaSvr()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mediasvr_linux_oper as meta
        return meta._meta_table['MediaSvr']['meta_info']


