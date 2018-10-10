""" Cisco_IOS_XR_spirit_corehelper_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR spirit\-corehelper package configuration.

This module contains definitions
for the following management objects\:
  exception\: Core dump configuration commands

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Exception(Entity):
    """
    Core dump configuration commands
    
    .. attribute:: file
    
    	Container for the order of preference
    	**type**\:  :py:class:`File <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_corehelper_cfg.Exception.File>`
    
    

    """

    _prefix = 'spirit-corehelper-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Exception, self).__init__()
        self._top_entity = None

        self.yang_name = "exception"
        self.yang_parent_name = "Cisco-IOS-XR-spirit-corehelper-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("file", ("file", Exception.File))])
        self._leafs = OrderedDict()

        self.file = Exception.File()
        self.file.parent = self
        self._children_name_map["file"] = "file"
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-corehelper-cfg:exception"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Exception, [], name, value)


    class File(Entity):
        """
        Container for the order of preference
        
        .. attribute:: choice2
        
        	Preference of the dump location
        	**type**\: str
        
        .. attribute:: choice1
        
        	Preference of the dump location
        	**type**\: str
        
        .. attribute:: choice3
        
        	Preference of the dump location
        	**type**\: str
        
        

        """

        _prefix = 'spirit-corehelper-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Exception.File, self).__init__()

            self.yang_name = "file"
            self.yang_parent_name = "exception"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('choice2', (YLeaf(YType.str, 'choice2'), ['str'])),
                ('choice1', (YLeaf(YType.str, 'choice1'), ['str'])),
                ('choice3', (YLeaf(YType.str, 'choice3'), ['str'])),
            ])
            self.choice2 = None
            self.choice1 = None
            self.choice3 = None
            self._segment_path = lambda: "file"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-corehelper-cfg:exception/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Exception.File, ['choice2', 'choice1', 'choice3'], name, value)

    def clone_ptr(self):
        self._top_entity = Exception()
        return self._top_entity

