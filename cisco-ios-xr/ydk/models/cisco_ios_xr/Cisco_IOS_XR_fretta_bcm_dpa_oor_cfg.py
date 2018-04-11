""" Cisco_IOS_XR_fretta_bcm_dpa_oor_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fretta\-bcm\-dpa\-oor package configuration.

This module contains definitions
for the following management objects\:
  oor\-hw\-config\: Out\-Of\-Resource (OOR) configuration

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class OorHwConfig(Entity):
    """
    Out\-Of\-Resource (OOR) configuration
    
    .. attribute:: hw
    
    	Hardware OOR configuration
    	**type**\:  :py:class:`Hw <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_oor_cfg.OorHwConfig.Hw>`
    
    

    """

    _prefix = 'fretta-bcm-dpa-oor-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(OorHwConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "oor-hw-config"
        self.yang_parent_name = "Cisco-IOS-XR-fretta-bcm-dpa-oor-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("hw", ("hw", OorHwConfig.Hw))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.hw = OorHwConfig.Hw()
        self.hw.parent = self
        self._children_name_map["hw"] = "hw"
        self._children_yang_names.add("hw")
        self._segment_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-oor-cfg:oor-hw-config"


    class Hw(Entity):
        """
        Hardware OOR configuration
        
        .. attribute:: thresholds
        
        	Configure OOR hardware thresholds
        	**type**\:  :py:class:`Thresholds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_oor_cfg.OorHwConfig.Hw.Thresholds>`
        
        .. attribute:: dampening
        
        	Configure OOR hardware dampening timeouts
        	**type**\: int
        
        	**range:** 0..600
        
        	**units**\: second
        
        

        """

        _prefix = 'fretta-bcm-dpa-oor-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(OorHwConfig.Hw, self).__init__()

            self.yang_name = "hw"
            self.yang_parent_name = "oor-hw-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("thresholds", ("thresholds", OorHwConfig.Hw.Thresholds))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('dampening', YLeaf(YType.uint32, 'dampening')),
            ])
            self.dampening = None

            self.thresholds = OorHwConfig.Hw.Thresholds()
            self.thresholds.parent = self
            self._children_name_map["thresholds"] = "thresholds"
            self._children_yang_names.add("thresholds")
            self._segment_path = lambda: "hw"
            self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-oor-cfg:oor-hw-config/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OorHwConfig.Hw, ['dampening'], name, value)


        class Thresholds(Entity):
            """
            Configure OOR hardware thresholds
            
            .. attribute:: threshold
            
            	none
            	**type**\: list of  		 :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_oor_cfg.OorHwConfig.Hw.Thresholds.Threshold>`
            
            

            """

            _prefix = 'fretta-bcm-dpa-oor-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(OorHwConfig.Hw.Thresholds, self).__init__()

                self.yang_name = "thresholds"
                self.yang_parent_name = "hw"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("threshold", ("threshold", OorHwConfig.Hw.Thresholds.Threshold))])
                self._leafs = OrderedDict()

                self.threshold = YList(self)
                self._segment_path = lambda: "thresholds"
                self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-oor-cfg:oor-hw-config/hw/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OorHwConfig.Hw.Thresholds, [], name, value)


            class Threshold(Entity):
                """
                none
                
                .. attribute:: color  (key)
                
                	none
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: percent
                
                	value in percent
                	**type**\: int
                
                	**range:** 0..100
                
                	**mandatory**\: True
                
                	**units**\: percentage
                
                

                """

                _prefix = 'fretta-bcm-dpa-oor-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(OorHwConfig.Hw.Thresholds.Threshold, self).__init__()

                    self.yang_name = "threshold"
                    self.yang_parent_name = "thresholds"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['color']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('color', YLeaf(YType.str, 'color')),
                        ('percent', YLeaf(YType.uint32, 'percent')),
                    ])
                    self.color = None
                    self.percent = None
                    self._segment_path = lambda: "threshold" + "[color='" + str(self.color) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-oor-cfg:oor-hw-config/hw/thresholds/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(OorHwConfig.Hw.Thresholds.Threshold, ['color', 'percent'], name, value)

    def clone_ptr(self):
        self._top_entity = OorHwConfig()
        return self._top_entity

