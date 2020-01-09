""" Cisco_IOS_XR_shellutil_copy_act 

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




class Copy(_Entity_):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_copy_act.Copy.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_copy_act.Copy.Output>`
    
    

    """

    _prefix = 'shellutil-copy-act'
    _revision = '2018-05-20'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Copy, self).__init__()
        self._top_entity = None

        self.yang_name = "copy"
        self.yang_parent_name = "Cisco-IOS-XR-shellutil-copy-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = Copy.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = Copy.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-shellutil-copy-act:copy"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: sourcename
        
        	source file name to copy
        	**type**\: str
        
        .. attribute:: destinationname
        
        	destination file name
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: sourcefilesystem
        
        	source file system e.g disk0\: tftp
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: destinationfilesystem
        
        	destination file system e.g disk0\:, tftp\:
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: sourcelocation
        
        	source location
        	**type**\: str
        
        .. attribute:: destinationlocation
        
        	destination location
        	**type**\: str
        
        .. attribute:: vrf
        
        	vrf name
        	**type**\: str
        
        .. attribute:: recurse
        
        	recurse files to copy
        	**type**\: bool
        
        

        """

        _prefix = 'shellutil-copy-act'
        _revision = '2018-05-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Copy.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "copy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('sourcename', (YLeaf(YType.str, 'sourcename'), ['str'])),
                ('destinationname', (YLeaf(YType.str, 'destinationname'), ['str'])),
                ('sourcefilesystem', (YLeaf(YType.str, 'sourcefilesystem'), ['str'])),
                ('destinationfilesystem', (YLeaf(YType.str, 'destinationfilesystem'), ['str'])),
                ('sourcelocation', (YLeaf(YType.str, 'sourcelocation'), ['str'])),
                ('destinationlocation', (YLeaf(YType.str, 'destinationlocation'), ['str'])),
                ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                ('recurse', (YLeaf(YType.boolean, 'recurse'), ['bool'])),
            ])
            self.sourcename = None
            self.destinationname = None
            self.sourcefilesystem = None
            self.destinationfilesystem = None
            self.sourcelocation = None
            self.destinationlocation = None
            self.vrf = None
            self.recurse = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-shellutil-copy-act:copy/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Copy.Input, ['sourcename', 'destinationname', 'sourcefilesystem', 'destinationfilesystem', 'sourcelocation', 'destinationlocation', 'vrf', 'recurse'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_shellutil_copy_act as meta
            return meta._meta_table['Copy.Input']['meta_info']


    class Output(_Entity_):
        """
        
        
        .. attribute:: response
        
        	Status of copy operation
        	**type**\: str
        
        

        """

        _prefix = 'shellutil-copy-act'
        _revision = '2018-05-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Copy.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "copy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('response', (YLeaf(YType.str, 'response'), ['str'])),
            ])
            self.response = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-shellutil-copy-act:copy/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Copy.Output, ['response'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_shellutil_copy_act as meta
            return meta._meta_table['Copy.Output']['meta_info']

    def clone_ptr(self):
        self._top_entity = Copy()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_shellutil_copy_act as meta
        return meta._meta_table['Copy']['meta_info']


