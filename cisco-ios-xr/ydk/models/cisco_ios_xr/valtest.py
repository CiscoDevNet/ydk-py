""" valtest 

This module contains definitions
for the Calvados model objects.

This module holds a sample validation.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
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




class Config(_Entity_):
    """
    
    
    .. attribute:: valtest
    
    	
    	**type**\:  :py:class:`Valtest <ydk.models.cisco_ios_xr.valtest.Config.Valtest>`
    
    

    """

    _prefix = 'valtest'
    _revision = '2012-08-20'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Config, self).__init__()
        self._top_entity = None

        self.yang_name = "config"
        self.yang_parent_name = "valtest"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("valtest", ("valtest", Config.Valtest))])
        self._leafs = OrderedDict()

        self.valtest = Config.Valtest()
        self.valtest.parent = self
        self._children_name_map["valtest"] = "valtest"
        self._segment_path = lambda: "valtest:config"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Config, [], name, value)


    class Valtest(_Entity_):
        """
        
        
        .. attribute:: a_number
        
        	
        	**type**\: int
        
        	**range:** \-9223372036854775808..9223372036854775807
        
        	**default value**\: 42
        
        .. attribute:: b_number
        
        	
        	**type**\: int
        
        	**range:** \-9223372036854775808..9223372036854775807
        
        	**default value**\: 7
        
        

        """

        _prefix = 'valtest'
        _revision = '2012-08-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Config.Valtest, self).__init__()

            self.yang_name = "valtest"
            self.yang_parent_name = "config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('a_number', (YLeaf(YType.int64, 'a_number'), ['int'])),
                ('b_number', (YLeaf(YType.int64, 'b_number'), ['int'])),
            ])
            self.a_number = None
            self.b_number = None
            self._segment_path = lambda: "valtest"
            self._absolute_path = lambda: "valtest:config/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Config.Valtest, ['a_number', 'b_number'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _valtest as meta
            return meta._meta_table['Config.Valtest']['meta_info']

    def clone_ptr(self):
        self._top_entity = Config()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _valtest as meta
        return meta._meta_table['Config']['meta_info']


