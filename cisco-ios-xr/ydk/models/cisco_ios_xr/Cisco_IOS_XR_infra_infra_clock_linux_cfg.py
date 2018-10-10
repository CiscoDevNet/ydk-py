""" Cisco_IOS_XR_infra_infra_clock_linux_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-infra\-clock\-linux package configuration.

This module contains definitions
for the following management objects\:
  clock\: Configure time\-of\-day clock

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Clock(Entity):
    """
    Configure time\-of\-day clock
    
    .. attribute:: time_zone
    
    	Configure time zone
    	**type**\:  :py:class:`TimeZone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_linux_cfg.Clock.TimeZone>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'infra-infra-clock-linux-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Clock, self).__init__()
        self._top_entity = None

        self.yang_name = "clock"
        self.yang_parent_name = "Cisco-IOS-XR-infra-infra-clock-linux-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("time-zone", ("time_zone", Clock.TimeZone))])
        self._leafs = OrderedDict()

        self.time_zone = None
        self._children_name_map["time_zone"] = "time-zone"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-infra-clock-linux-cfg:clock"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Clock, [], name, value)


    class TimeZone(Entity):
        """
        Configure time zone
        
        .. attribute:: time_zone_name
        
        	Name of time zone
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: area_name
        
        	Area File in zoneinfo package
        	**type**\: str
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-infra-clock-linux-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Clock.TimeZone, self).__init__()

            self.yang_name = "time-zone"
            self.yang_parent_name = "clock"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('time_zone_name', (YLeaf(YType.str, 'time-zone-name'), ['str'])),
                ('area_name', (YLeaf(YType.str, 'area-name'), ['str'])),
            ])
            self.time_zone_name = None
            self.area_name = None
            self._segment_path = lambda: "time-zone"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-infra-clock-linux-cfg:clock/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Clock.TimeZone, ['time_zone_name', 'area_name'], name, value)

    def clone_ptr(self):
        self._top_entity = Clock()
        return self._top_entity

