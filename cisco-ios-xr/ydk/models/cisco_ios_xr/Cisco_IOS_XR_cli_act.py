""" Cisco_IOS_XR_cli_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CliCommand(Entity):
    """
    Actions on certificate revocation lists
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cli_act.CliCommand.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cli_act.CliCommand.Output>`
    
    

    """

    _prefix = 'cli-act'
    _revision = '2016-09-22'

    def __init__(self):
        super(CliCommand, self).__init__()
        self._top_entity = None

        self.yang_name = "cli-command"
        self.yang_parent_name = "Cisco-IOS-XR-cli-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = CliCommand.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = CliCommand.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-cli-act:cli-command"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: command
        
        	CLI command string
        	**type**\: str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'cli-act'
        _revision = '2016-09-22'

        def __init__(self):
            super(CliCommand.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "cli-command"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('command', (YLeaf(YType.str, 'command'), ['str'])),
            ])
            self.command = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-cli-act:cli-command/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CliCommand.Input, ['command'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: response
        
        	CLI command output string
        	**type**\: str
        
        

        """

        _prefix = 'cli-act'
        _revision = '2016-09-22'

        def __init__(self):
            super(CliCommand.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "cli-command"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('response', (YLeaf(YType.str, 'response'), ['str'])),
            ])
            self.response = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-cli-act:cli-command/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CliCommand.Output, ['response'], name, value)

    def clone_ptr(self):
        self._top_entity = CliCommand()
        return self._top_entity

