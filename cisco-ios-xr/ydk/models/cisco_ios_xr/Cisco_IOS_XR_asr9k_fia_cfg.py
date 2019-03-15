""" Cisco_IOS_XR_asr9k_fia_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-fia package configuration.

This module contains definitions
for the following management objects\:
  fabric\-fia\-config\: Configure Global Fabric Fia Settings

This YANG module augments the
  Cisco\-IOS\-XR\-config\-mda\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class FabricFiaConfig(Entity):
    """
    Configure Global Fabric Fia Settings
    
    .. attribute:: fia_intf_policer
    
    	FIA interface rate\-limiter on 7\-Fabric LC
    	**type**\:  :py:class:`FiaIntfPolicer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fia_cfg.FabricFiaConfig.FiaIntfPolicer>`
    
    

    """

    _prefix = 'asr9k-fia-cfg'
    _revision = '2017-08-17'

    def __init__(self):
        super(FabricFiaConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "fabric-fia-config"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-fia-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("fia-intf-policer", ("fia_intf_policer", FabricFiaConfig.FiaIntfPolicer))])
        self._leafs = OrderedDict()

        self.fia_intf_policer = FabricFiaConfig.FiaIntfPolicer()
        self.fia_intf_policer.parent = self
        self._children_name_map["fia_intf_policer"] = "fia-intf-policer"
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-fia-cfg:fabric-fia-config"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(FabricFiaConfig, [], name, value)


    class FiaIntfPolicer(Entity):
        """
        FIA interface rate\-limiter on 7\-Fabric LC
        
        .. attribute:: disable
        
        	disable FIA interface policer 
        	**type**\: bool
        
        

        """

        _prefix = 'asr9k-fia-cfg'
        _revision = '2017-08-17'

        def __init__(self):
            super(FabricFiaConfig.FiaIntfPolicer, self).__init__()

            self.yang_name = "fia-intf-policer"
            self.yang_parent_name = "fabric-fia-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('disable', (YLeaf(YType.boolean, 'disable'), ['bool'])),
            ])
            self.disable = None
            self._segment_path = lambda: "fia-intf-policer"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-fia-cfg:fabric-fia-config/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FabricFiaConfig.FiaIntfPolicer, ['disable'], name, value)


    def clone_ptr(self):
        self._top_entity = FabricFiaConfig()
        return self._top_entity



