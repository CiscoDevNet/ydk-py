""" Cisco_IOS_XR_config_cfgmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR config\-cfgmgr package operational data.

This module contains definitions
for the following management objects\:
  config\: Configuration\-related operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Config(Entity):
    """
    Configuration\-related operational data
    
    .. attribute:: global_
    
    	Global operational data
    	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_oper.Config.Global>`
    
    

    """

    _prefix = 'config-cfgmgr-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Config, self).__init__()
        self._top_entity = None

        self.yang_name = "config"
        self.yang_parent_name = "Cisco-IOS-XR-config-cfgmgr-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("global", ("global_", Config.Global))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.global_ = Config.Global()
        self.global_.parent = self
        self._children_name_map["global_"] = "global"
        self._children_yang_names.add("global")
        self._segment_path = lambda: "Cisco-IOS-XR-config-cfgmgr-oper:config"


    class Global(Entity):
        """
        Global operational data
        
        

        """

        _prefix = 'config-cfgmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Config.Global, self).__init__()

            self.yang_name = "global"
            self.yang_parent_name = "config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()
            self._segment_path = lambda: "global"
            self._absolute_path = lambda: "Cisco-IOS-XR-config-cfgmgr-oper:config/%s" % self._segment_path()

    def clone_ptr(self):
        self._top_entity = Config()
        return self._top_entity

