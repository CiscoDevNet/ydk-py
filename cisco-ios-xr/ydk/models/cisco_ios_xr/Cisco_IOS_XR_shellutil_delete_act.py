""" Cisco_IOS_XR_shellutil_delete_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

Copyright (c) 2016, 2018 by Cisco Systems, Inc.
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




class Delete(_Entity_):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_delete_act.Delete.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_delete_act.Delete.Output>`
    
    

    """

    _prefix = 'shellutil-delete-act'
    _revision = '2018-01-20'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Delete, self).__init__()
        self._top_entity = None

        self.yang_name = "delete"
        self.yang_parent_name = "Cisco-IOS-XR-shellutil-delete-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = Delete.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = Delete.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-shellutil-delete-act:delete"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: name
        
        	file name
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: location
        
        	location
        	**type**\: str
        
        .. attribute:: recurse
        
        	Files in dir
        	**type**\: bool
        
        

        """

        _prefix = 'shellutil-delete-act'
        _revision = '2018-01-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Delete.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "delete"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ('recurse', (YLeaf(YType.boolean, 'recurse'), ['bool'])),
            ])
            self.name = None
            self.location = None
            self.recurse = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-shellutil-delete-act:delete/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Delete.Input, ['name', 'location', 'recurse'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_shellutil_delete_act as meta
            return meta._meta_table['Delete.Input']['meta_info']


    class Output(_Entity_):
        """
        
        
        .. attribute:: response
        
        	Status of delete operation
        	**type**\: str
        
        

        """

        _prefix = 'shellutil-delete-act'
        _revision = '2018-01-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Delete.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "delete"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('response', (YLeaf(YType.str, 'response'), ['str'])),
            ])
            self.response = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-shellutil-delete-act:delete/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Delete.Output, ['response'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_shellutil_delete_act as meta
            return meta._meta_table['Delete.Output']['meta_info']

    def clone_ptr(self):
        self._top_entity = Delete()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_shellutil_delete_act as meta
        return meta._meta_table['Delete']['meta_info']


