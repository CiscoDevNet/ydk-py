""" Cisco_IOS_XR_upgrade_fpd_ng_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR upgrade\-fpd package action data.

This module contains definitions
for the following management objects\:
  fpd\: Field programmable device (FPD) operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class UpgradeFpd(Entity):
    """
    Execute FPD upgrade
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_ng_act.UpgradeFpd.Input>`
    
    

    """

    _prefix = 'upgrade-fpd-act'
    _revision = '2017-04-04'

    def __init__(self):
        super(UpgradeFpd, self).__init__()
        self._top_entity = None

        self.yang_name = "upgrade-fpd"
        self.yang_parent_name = "Cisco-IOS-XR-upgrade-fpd-ng-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = UpgradeFpd.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-upgrade-fpd-ng-act:upgrade-fpd"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: location
        
        	Location of the FPD to be upgraded
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: fpd
        
        	name of the fpd to be upgraded
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: force
        
        	Force the upgrade process
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'upgrade-fpd-act'
        _revision = '2017-04-04'

        def __init__(self):
            super(UpgradeFpd.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "upgrade-fpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ('fpd', (YLeaf(YType.str, 'fpd'), ['str'])),
                ('force', (YLeaf(YType.empty, 'force'), ['Empty'])),
            ])
            self.location = None
            self.fpd = None
            self.force = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-upgrade-fpd-ng-act:upgrade-fpd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(UpgradeFpd.Input, ['location', 'fpd', 'force'], name, value)

    def clone_ptr(self):
        self._top_entity = UpgradeFpd()
        return self._top_entity

