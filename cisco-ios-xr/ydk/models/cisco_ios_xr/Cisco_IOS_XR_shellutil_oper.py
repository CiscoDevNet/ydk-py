""" Cisco_IOS_XR_shellutil_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR shellutil package operational data.

This module contains definitions
for the following management objects\:
  system\-time\: System time information

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class TimeSource(Enum):
    """
    TimeSource (Enum Class)

    Time source

    .. data:: error = 0

    	Error

    .. data:: none = 1

    	Unsynchronized time

    .. data:: ntp = 2

    	Network time protocol

    .. data:: manual = 3

    	User configured

    .. data:: calendar = 4

    	Hardware calendar

    """

    error = Enum.YLeaf(0, "error")

    none = Enum.YLeaf(1, "none")

    ntp = Enum.YLeaf(2, "ntp")

    manual = Enum.YLeaf(3, "manual")

    calendar = Enum.YLeaf(4, "calendar")



class SystemTime(Entity):
    """
    System time information
    
    .. attribute:: clock
    
    	System clock information
    	**type**\:  :py:class:`Clock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper.SystemTime.Clock>`
    
    	**config**\: False
    
    .. attribute:: uptime
    
    	System uptime information
    	**type**\:  :py:class:`Uptime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper.SystemTime.Uptime>`
    
    	**config**\: False
    
    

    """

    _prefix = 'shellutil-oper'
    _revision = '2015-01-07'

    def __init__(self):
        super(SystemTime, self).__init__()
        self._top_entity = None

        self.yang_name = "system-time"
        self.yang_parent_name = "Cisco-IOS-XR-shellutil-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("clock", ("clock", SystemTime.Clock)), ("uptime", ("uptime", SystemTime.Uptime))])
        self._leafs = OrderedDict()

        self.clock = SystemTime.Clock()
        self.clock.parent = self
        self._children_name_map["clock"] = "clock"

        self.uptime = SystemTime.Uptime()
        self.uptime.parent = self
        self._children_name_map["uptime"] = "uptime"
        self._segment_path = lambda: "Cisco-IOS-XR-shellutil-oper:system-time"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SystemTime, [], name, value)


    class Clock(Entity):
        """
        System clock information
        
        .. attribute:: year
        
        	Year [0..65535]
        	**type**\: int
        
        	**range:** 0..65535
        
        	**config**\: False
        
        .. attribute:: month
        
        	Month [1..12]
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        .. attribute:: day
        
        	Day [1..31]
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        .. attribute:: hour
        
        	Hour [0..23]
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        .. attribute:: minute
        
        	Minute [0..59]
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        .. attribute:: second
        
        	Second [0..60], use 60 for leap\-second
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        .. attribute:: millisecond
        
        	Millisecond [0..999]
        	**type**\: int
        
        	**range:** 0..65535
        
        	**config**\: False
        
        .. attribute:: wday
        
        	Week Day [0..6]
        	**type**\: int
        
        	**range:** 0..65535
        
        	**config**\: False
        
        .. attribute:: time_zone
        
        	Time zone
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: time_source
        
        	Time source
        	**type**\:  :py:class:`TimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper.TimeSource>`
        
        	**config**\: False
        
        

        """

        _prefix = 'shellutil-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(SystemTime.Clock, self).__init__()

            self.yang_name = "clock"
            self.yang_parent_name = "system-time"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('year', (YLeaf(YType.uint16, 'year'), ['int'])),
                ('month', (YLeaf(YType.uint8, 'month'), ['int'])),
                ('day', (YLeaf(YType.uint8, 'day'), ['int'])),
                ('hour', (YLeaf(YType.uint8, 'hour'), ['int'])),
                ('minute', (YLeaf(YType.uint8, 'minute'), ['int'])),
                ('second', (YLeaf(YType.uint8, 'second'), ['int'])),
                ('millisecond', (YLeaf(YType.uint16, 'millisecond'), ['int'])),
                ('wday', (YLeaf(YType.uint16, 'wday'), ['int'])),
                ('time_zone', (YLeaf(YType.str, 'time-zone'), ['str'])),
                ('time_source', (YLeaf(YType.enumeration, 'time-source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper', 'TimeSource', '')])),
            ])
            self.year = None
            self.month = None
            self.day = None
            self.hour = None
            self.minute = None
            self.second = None
            self.millisecond = None
            self.wday = None
            self.time_zone = None
            self.time_source = None
            self._segment_path = lambda: "clock"
            self._absolute_path = lambda: "Cisco-IOS-XR-shellutil-oper:system-time/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SystemTime.Clock, [u'year', u'month', u'day', u'hour', u'minute', u'second', u'millisecond', u'wday', u'time_zone', u'time_source'], name, value)



    class Uptime(Entity):
        """
        System uptime information
        
        .. attribute:: host_name
        
        	Host name
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: uptime
        
        	Amount of time in seconds since this system was last initialized
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: second
        
        

        """

        _prefix = 'shellutil-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(SystemTime.Uptime, self).__init__()

            self.yang_name = "uptime"
            self.yang_parent_name = "system-time"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('host_name', (YLeaf(YType.str, 'host-name'), ['str'])),
                ('uptime', (YLeaf(YType.uint32, 'uptime'), ['int'])),
            ])
            self.host_name = None
            self.uptime = None
            self._segment_path = lambda: "uptime"
            self._absolute_path = lambda: "Cisco-IOS-XR-shellutil-oper:system-time/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SystemTime.Uptime, [u'host_name', u'uptime'], name, value)


    def clone_ptr(self):
        self._top_entity = SystemTime()
        return self._top_entity



