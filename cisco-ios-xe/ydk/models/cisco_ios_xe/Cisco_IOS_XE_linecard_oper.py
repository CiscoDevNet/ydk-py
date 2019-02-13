""" Cisco_IOS_XE_linecard_oper 

This module contains a collection of YANG definitions for
monitoring linecards in a Network Element.
Copyright (c) 2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class LinecardOperData(Entity):
    """
    Top\-level container for linecard operational data
    
    .. attribute:: linecard
    
    	List of linecard instances, keyed by slot
    	**type**\: list of  		 :py:class:`Linecard <ydk.models.cisco_ios_xe.Cisco_IOS_XE_linecard_oper.LinecardOperData.Linecard>`
    
    	**config**\: False
    
    

    """

    _prefix = 'linecard-ios-xe-oper'
    _revision = '2018-03-26'

    def __init__(self):
        super(LinecardOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "linecard-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-linecard-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("linecard", ("linecard", LinecardOperData.Linecard))])
        self._leafs = OrderedDict()

        self.linecard = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-linecard-oper:linecard-oper-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(LinecardOperData, [], name, value)


    class Linecard(Entity):
        """
        List of linecard instances, keyed by slot
        
        .. attribute:: name  (key)
        
        	Physical location description of the linecard
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: power_admin_state
        
        	Power provided to the linecard\: Enabled/Disabled
        	**type**\: bool
        
        	**config**\: False
        
        

        """

        _prefix = 'linecard-ios-xe-oper'
        _revision = '2018-03-26'

        def __init__(self):
            super(LinecardOperData.Linecard, self).__init__()

            self.yang_name = "linecard"
            self.yang_parent_name = "linecard-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('power_admin_state', (YLeaf(YType.boolean, 'power-admin-state'), ['bool'])),
            ])
            self.name = None
            self.power_admin_state = None
            self._segment_path = lambda: "linecard" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-linecard-oper:linecard-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LinecardOperData.Linecard, ['name', 'power_admin_state'], name, value)


    def clone_ptr(self):
        self._top_entity = LinecardOperData()
        return self._top_entity



