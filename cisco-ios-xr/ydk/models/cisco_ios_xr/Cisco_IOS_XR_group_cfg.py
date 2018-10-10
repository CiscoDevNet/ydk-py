""" Cisco_IOS_XR_group_cfg 

This module contains IOS\-XR group YANG data 
for flexible cli groups 
    
Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Groups(Entity):
    """
    config groups
    
    .. attribute:: group
    
    	Group config definition
    	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_group_cfg.Groups.Group>`
    
    

    """

    _prefix = 'group-cfg'
    _revision = '2016-04-29'

    def __init__(self):
        super(Groups, self).__init__()
        self._top_entity = None

        self.yang_name = "groups"
        self.yang_parent_name = "Cisco-IOS-XR-group-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("group", ("group", Groups.Group))])
        self._leafs = OrderedDict()

        self.group = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-group-cfg:groups"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Groups, [], name, value)


    class Group(Entity):
        """
        Group config definition
        
        .. attribute:: group_name  (key)
        
        	Group name
        	**type**\: str
        
        	**length:** 0..32
        
        

        """

        _prefix = 'group-cfg'
        _revision = '2016-04-29'

        def __init__(self):
            super(Groups.Group, self).__init__()

            self.yang_name = "group"
            self.yang_parent_name = "groups"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['group_name']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('group_name', (YLeaf(YType.str, 'group-name'), ['str'])),
            ])
            self.group_name = None
            self._segment_path = lambda: "group" + "[group-name='" + str(self.group_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-group-cfg:groups/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Groups.Group, ['group_name'], name, value)

    def clone_ptr(self):
        self._top_entity = Groups()
        return self._top_entity

class ApplyGroups(Entity):
    """
    apply groups
    
    .. attribute:: apply_group
    
    	apply\-group name
    	**type**\: str
    
    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
    
    

    """

    _prefix = 'group-cfg'
    _revision = '2016-04-29'

    def __init__(self):
        super(ApplyGroups, self).__init__()
        self._top_entity = None

        self.yang_name = "apply-groups"
        self.yang_parent_name = "Cisco-IOS-XR-group-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('apply_group', (YLeaf(YType.str, 'apply-group'), ['str'])),
        ])
        self.apply_group = None
        self._segment_path = lambda: "Cisco-IOS-XR-group-cfg:apply-groups"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ApplyGroups, ['apply_group'], name, value)

    def clone_ptr(self):
        self._top_entity = ApplyGroups()
        return self._top_entity

