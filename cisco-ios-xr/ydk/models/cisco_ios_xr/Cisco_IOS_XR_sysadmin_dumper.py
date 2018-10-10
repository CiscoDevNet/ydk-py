""" Cisco_IOS_XR_sysadmin_dumper 

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin dumper to
configure file path options to copy the core files to.

Copyright(c) 2015\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Exception(Entity):
    """
    
    
    .. attribute:: choice
    
    	
    	**type**\: list of  		 :py:class:`Choice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_dumper.Exception.Choice>`
    
    

    """

    _prefix = 'dumper'
    _revision = '2017-05-09'

    def __init__(self):
        super(Exception, self).__init__()
        self._top_entity = None

        self.yang_name = "exception"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-dumper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("choice", ("choice", Exception.Choice))])
        self._leafs = OrderedDict()

        self.choice = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-dumper:exception"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Exception, [], name, value)


    class Choice(Entity):
        """
        
        
        .. attribute:: order  (key)
        
        	
        	**type**\: int
        
        	**range:** 1..3
        
        .. attribute:: filepath
        
        	
        	**type**\: str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'dumper'
        _revision = '2017-05-09'

        def __init__(self):
            super(Exception.Choice, self).__init__()

            self.yang_name = "choice"
            self.yang_parent_name = "exception"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['order']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('order', (YLeaf(YType.int32, 'order'), ['int'])),
                ('filepath', (YLeaf(YType.str, 'filepath'), ['str'])),
            ])
            self.order = None
            self.filepath = None
            self._segment_path = lambda: "choice" + "[order='" + str(self.order) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-dumper:exception/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Exception.Choice, ['order', 'filepath'], name, value)

    def clone_ptr(self):
        self._top_entity = Exception()
        return self._top_entity

