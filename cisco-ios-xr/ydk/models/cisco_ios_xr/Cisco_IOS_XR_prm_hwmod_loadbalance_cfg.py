""" Cisco_IOS_XR_prm_hwmod_loadbalance_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR prm\-hwmod\-loadbalance package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\: HardwareModule

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class HardwareModule(Entity):
    """
    HardwareModule
    
    .. attribute:: loadbalancing
    
    	Loadbalance option
    	**type**\:  :py:class:`Loadbalancing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_loadbalance_cfg.HardwareModule.Loadbalancing>`
    
    

    """

    _prefix = 'prm-hwmod-loadbalance-cfg'
    _revision = '2017-04-12'

    def __init__(self):
        super(HardwareModule, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module"
        self.yang_parent_name = "Cisco-IOS-XR-prm-hwmod-loadbalance-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("loadbalancing", ("loadbalancing", HardwareModule.Loadbalancing))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.loadbalancing = HardwareModule.Loadbalancing()
        self.loadbalancing.parent = self
        self._children_name_map["loadbalancing"] = "loadbalancing"
        self._children_yang_names.add("loadbalancing")
        self._segment_path = lambda: "Cisco-IOS-XR-prm-hwmod-loadbalance-cfg:hardware-module"


    class Loadbalancing(Entity):
        """
        Loadbalance option
        
        .. attribute:: bgp3107
        
        	BGP LU
        	**type**\:  :py:class:`Bgp3107 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_loadbalance_cfg.HardwareModule.Loadbalancing.Bgp3107>`
        
        

        """

        _prefix = 'prm-hwmod-loadbalance-cfg'
        _revision = '2017-04-12'

        def __init__(self):
            super(HardwareModule.Loadbalancing, self).__init__()

            self.yang_name = "loadbalancing"
            self.yang_parent_name = "hardware-module"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("bgp3107", ("bgp3107", HardwareModule.Loadbalancing.Bgp3107))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.bgp3107 = HardwareModule.Loadbalancing.Bgp3107()
            self.bgp3107.parent = self
            self._children_name_map["bgp3107"] = "bgp3107"
            self._children_yang_names.add("bgp3107")
            self._segment_path = lambda: "loadbalancing"
            self._absolute_path = lambda: "Cisco-IOS-XR-prm-hwmod-loadbalance-cfg:hardware-module/%s" % self._segment_path()


        class Bgp3107(Entity):
            """
            BGP LU
            
            .. attribute:: ecmp
            
            	ECMP 
            	**type**\:  :py:class:`Ecmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_loadbalance_cfg.HardwareModule.Loadbalancing.Bgp3107.Ecmp>`
            
            

            """

            _prefix = 'prm-hwmod-loadbalance-cfg'
            _revision = '2017-04-12'

            def __init__(self):
                super(HardwareModule.Loadbalancing.Bgp3107, self).__init__()

                self.yang_name = "bgp3107"
                self.yang_parent_name = "loadbalancing"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("ecmp", ("ecmp", HardwareModule.Loadbalancing.Bgp3107.Ecmp))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.ecmp = HardwareModule.Loadbalancing.Bgp3107.Ecmp()
                self.ecmp.parent = self
                self._children_name_map["ecmp"] = "ecmp"
                self._children_yang_names.add("ecmp")
                self._segment_path = lambda: "bgp3107"
                self._absolute_path = lambda: "Cisco-IOS-XR-prm-hwmod-loadbalance-cfg:hardware-module/loadbalancing/%s" % self._segment_path()


            class Ecmp(Entity):
                """
                ECMP 
                
                .. attribute:: enable
                
                	Enable Option
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'prm-hwmod-loadbalance-cfg'
                _revision = '2017-04-12'

                def __init__(self):
                    super(HardwareModule.Loadbalancing.Bgp3107.Ecmp, self).__init__()

                    self.yang_name = "ecmp"
                    self.yang_parent_name = "bgp3107"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enable', YLeaf(YType.empty, 'enable')),
                    ])
                    self.enable = None
                    self._segment_path = lambda: "ecmp"
                    self._absolute_path = lambda: "Cisco-IOS-XR-prm-hwmod-loadbalance-cfg:hardware-module/loadbalancing/bgp3107/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModule.Loadbalancing.Bgp3107.Ecmp, ['enable'], name, value)

    def clone_ptr(self):
        self._top_entity = HardwareModule()
        return self._top_entity

