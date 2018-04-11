""" Cisco_IOS_XR_ncs1001_ots_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1001\-ots\-act package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\-action\: NCS1k1 HW module config

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class OtsPsmManualSwitch(Enum):
    """
    OtsPsmManualSwitch (Enum Class)

    Ots psm manual switch

    .. data:: working = 1

    	Working port

    .. data:: protected = 2

    	Protected port

    """

    working = Enum.YLeaf(1, "working")

    protected = Enum.YLeaf(2, "protected")



class PsmManualSwitchTo(Entity):
    """
    Psm manual switch to port
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_act.PsmManualSwitchTo.Input>`
    
    

    """

    _prefix = 'ncs1001-ots-act'
    _revision = '2017-08-04'

    def __init__(self):
        super(PsmManualSwitchTo, self).__init__()
        self._top_entity = None

        self.yang_name = "psm-manual-switch-to"
        self.yang_parent_name = "Cisco-IOS-XR-ncs1001-ots-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = PsmManualSwitchTo.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")
        self._segment_path = lambda: "Cisco-IOS-XR-ncs1001-ots-act:psm-manual-switch-to"


    class Input(Entity):
        """
        
        
        .. attribute:: slot_id
        
        	Set Slot
        	**type**\: int
        
        	**range:** 1..3
        
        	**mandatory**\: True
        
        .. attribute:: manual_switch_to
        
        	Switch active path to selected port
        	**type**\:  :py:class:`OtsPsmManualSwitch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_act.OtsPsmManualSwitch>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ncs1001-ots-act'
        _revision = '2017-08-04'

        def __init__(self):
            super(PsmManualSwitchTo.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "psm-manual-switch-to"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('slot_id', YLeaf(YType.uint32, 'slot-id')),
                ('manual_switch_to', YLeaf(YType.enumeration, 'manual-switch-to')),
            ])
            self.slot_id = None
            self.manual_switch_to = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs1001-ots-act:psm-manual-switch-to/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PsmManualSwitchTo.Input, ['slot_id', 'manual_switch_to'], name, value)

    def clone_ptr(self):
        self._top_entity = PsmManualSwitchTo()
        return self._top_entity

