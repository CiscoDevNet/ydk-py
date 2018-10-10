""" Cisco_IOS_XR_prm_hwmod_sr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR prm\-hwmod\-sr package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\: HardwareModule

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
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
    
    .. attribute:: segment_routing
    
    	Segment Routing
    	**type**\:  :py:class:`SegmentRouting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_sr_cfg.HardwareModule.SegmentRouting>`
    
    

    """

    _prefix = 'prm-hwmod-sr-cfg'
    _revision = '2017-04-12'

    def __init__(self):
        super(HardwareModule, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module"
        self.yang_parent_name = "Cisco-IOS-XR-prm-hwmod-sr-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("segment-routing", ("segment_routing", HardwareModule.SegmentRouting))])
        self._leafs = OrderedDict()

        self.segment_routing = HardwareModule.SegmentRouting()
        self.segment_routing.parent = self
        self._children_name_map["segment_routing"] = "segment-routing"
        self._segment_path = lambda: "Cisco-IOS-XR-prm-hwmod-sr-cfg:hardware-module"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HardwareModule, [], name, value)


    class SegmentRouting(Entity):
        """
        Segment Routing
        
        .. attribute:: reserve
        
        	Reserve
        	**type**\:  :py:class:`Reserve <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_sr_cfg.HardwareModule.SegmentRouting.Reserve>`
        
        

        """

        _prefix = 'prm-hwmod-sr-cfg'
        _revision = '2017-04-12'

        def __init__(self):
            super(HardwareModule.SegmentRouting, self).__init__()

            self.yang_name = "segment-routing"
            self.yang_parent_name = "hardware-module"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("reserve", ("reserve", HardwareModule.SegmentRouting.Reserve))])
            self._leafs = OrderedDict()

            self.reserve = HardwareModule.SegmentRouting.Reserve()
            self.reserve.parent = self
            self._children_name_map["reserve"] = "reserve"
            self._segment_path = lambda: "segment-routing"
            self._absolute_path = lambda: "Cisco-IOS-XR-prm-hwmod-sr-cfg:hardware-module/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HardwareModule.SegmentRouting, [], name, value)


        class Reserve(Entity):
            """
            Reserve
            
            .. attribute:: service_label
            
            	Service Label
            	**type**\:  :py:class:`ServiceLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_sr_cfg.HardwareModule.SegmentRouting.Reserve.ServiceLabel>`
            
            

            """

            _prefix = 'prm-hwmod-sr-cfg'
            _revision = '2017-04-12'

            def __init__(self):
                super(HardwareModule.SegmentRouting.Reserve, self).__init__()

                self.yang_name = "reserve"
                self.yang_parent_name = "segment-routing"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("service-label", ("service_label", HardwareModule.SegmentRouting.Reserve.ServiceLabel))])
                self._leafs = OrderedDict()

                self.service_label = HardwareModule.SegmentRouting.Reserve.ServiceLabel()
                self.service_label.parent = self
                self._children_name_map["service_label"] = "service-label"
                self._segment_path = lambda: "reserve"
                self._absolute_path = lambda: "Cisco-IOS-XR-prm-hwmod-sr-cfg:hardware-module/segment-routing/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModule.SegmentRouting.Reserve, [], name, value)


            class ServiceLabel(Entity):
                """
                Service Label
                
                .. attribute:: enable
                
                	Enable
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'prm-hwmod-sr-cfg'
                _revision = '2017-04-12'

                def __init__(self):
                    super(HardwareModule.SegmentRouting.Reserve.ServiceLabel, self).__init__()

                    self.yang_name = "service-label"
                    self.yang_parent_name = "reserve"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.enable = None
                    self._segment_path = lambda: "service-label"
                    self._absolute_path = lambda: "Cisco-IOS-XR-prm-hwmod-sr-cfg:hardware-module/segment-routing/reserve/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModule.SegmentRouting.Reserve.ServiceLabel, ['enable'], name, value)

    def clone_ptr(self):
        self._top_entity = HardwareModule()
        return self._top_entity

