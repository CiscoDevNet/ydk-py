""" tailf_actions 

This module contains YANG definitions
for Cisco IOS\-XR and Tail\-F action support.

Copyright (c) 2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Action(Entity):
    """
    Support Tail\-F actions rpc format.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.tailf_actions.Action.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.tailf_actions.Action.Output>`
    
    

    """

    _prefix = 'act'
    _revision = '2017-02-28'

    def __init__(self):
        super(Action, self).__init__()
        self._top_entity = None

        self.yang_name = "action"
        self.yang_parent_name = "tailf-actions"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = Action.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = Action.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "tailf-actions:action"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: data
        
        	Data section of the YANG action hierarchy
        	**type**\: anyxml
        
        

        """

        _prefix = 'act'
        _revision = '2017-02-28'

        def __init__(self):
            super(Action.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "action"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('data', (YLeaf(YType.str, 'data'), ['str'])),
            ])
            self.data = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "tailf-actions:action/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Action.Input, ['data'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: data
        
        	Data and messages returned by the Tail\-F ConfD agent
        	**type**\: anyxml
        
        

        """

        _prefix = 'act'
        _revision = '2017-02-28'

        def __init__(self):
            super(Action.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "action"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('data', (YLeaf(YType.str, 'data'), ['str'])),
            ])
            self.data = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "tailf-actions:action/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Action.Output, ['data'], name, value)

    def clone_ptr(self):
        self._top_entity = Action()
        return self._top_entity

