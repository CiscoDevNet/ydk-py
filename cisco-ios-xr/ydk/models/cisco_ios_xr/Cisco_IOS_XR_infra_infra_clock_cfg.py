""" Cisco_IOS_XR_infra_infra_clock_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-infra\-clock package configuration.

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



class ClockMonth(Enum):
    """
    ClockMonth (Enum Class)

    Clock month

    .. data:: january = 0

    	January

    .. data:: february = 1

    	February

    .. data:: march = 2

    	March

    .. data:: april = 3

    	April

    .. data:: may = 4

    	May

    .. data:: june = 5

    	June

    .. data:: july = 6

    	July

    .. data:: august = 7

    	August

    .. data:: september = 8

    	September

    .. data:: october = 9

    	October

    .. data:: november = 10

    	November

    .. data:: december = 11

    	December

    """

    january = Enum.YLeaf(0, "january")

    february = Enum.YLeaf(1, "february")

    march = Enum.YLeaf(2, "march")

    april = Enum.YLeaf(3, "april")

    may = Enum.YLeaf(4, "may")

    june = Enum.YLeaf(5, "june")

    july = Enum.YLeaf(6, "july")

    august = Enum.YLeaf(7, "august")

    september = Enum.YLeaf(8, "september")

    october = Enum.YLeaf(9, "october")

    november = Enum.YLeaf(10, "november")

    december = Enum.YLeaf(11, "december")


class ClockSummerTimeMode(Enum):
    """
    ClockSummerTimeMode (Enum Class)

    Clock summer time mode

    .. data:: recurring = 0

    	Recurring summer time

    .. data:: date = 1

    	Absolute summer time

    """

    recurring = Enum.YLeaf(0, "recurring")

    date = Enum.YLeaf(1, "date")



class Clock(Entity):
    """
    Configure time\-of\-day clock
    
    .. attribute:: summer_time
    
    	Configure summer (daylight savings) time
    	**type**\:  :py:class:`SummerTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg.Clock.SummerTime>`
    
    	**presence node**\: True
    
    .. attribute:: time_zone
    
    	Configure time zone
    	**type**\:  :py:class:`TimeZone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg.Clock.TimeZone>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'infra-infra-clock-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Clock, self).__init__()
        self._top_entity = None

        self.yang_name = "clock"
        self.yang_parent_name = "Cisco-IOS-XR-infra-infra-clock-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("summer-time", ("summer_time", Clock.SummerTime)), ("time-zone", ("time_zone", Clock.TimeZone))])
        self._leafs = OrderedDict()

        self.summer_time = None
        self._children_name_map["summer_time"] = "summer-time"

        self.time_zone = None
        self._children_name_map["time_zone"] = "time-zone"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-infra-clock-cfg:clock"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Clock, [], name, value)


    class SummerTime(Entity):
        """
        Configure summer (daylight savings) time
        
        .. attribute:: time_zone_name
        
        	Name of time zone in summer
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: mode
        
        	Summer time mode
        	**type**\:  :py:class:`ClockSummerTimeMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg.ClockSummerTimeMode>`
        
        	**mandatory**\: True
        
        .. attribute:: start_week_number_or_start_date
        
        	 If Mode is set to 'Recurring' specify Week number of the Month to start (first and last strings are not allowed as they are in CLI) , if Mode is set to 'Date' specify Date to start 
        	**type**\: int
        
        	**range:** 1..31
        
        .. attribute:: start_weekday_or_start_year
        
        	 If Mode is set to 'Recurring' specify Weekday to start , if Mode is set to 'Date' specify Year to start 
        	**type**\: int
        
        	**range:** 0..2035
        
        .. attribute:: start_month
        
        	 Month to start 
        	**type**\:  :py:class:`ClockMonth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg.ClockMonth>`
        
        .. attribute:: start_hour
        
        	Hour to start 
        	**type**\: int
        
        	**range:** 0..23
        
        .. attribute:: start_minute
        
        	Minute to start 
        	**type**\: int
        
        	**range:** 0..59
        
        .. attribute:: end_week_number_or_end_date
        
        	If Mode is set to 'Recurring' specify Week number of the Month to end (first and last strings are not allowed as they are in CLI), if Mode is set to 'Date' specify Date to End
        	**type**\: int
        
        	**range:** 1..31
        
        .. attribute:: end_weekday_or_end_year
        
        	If Mode is set to 'Recurring' specify Weekday to end , if Mode is set to 'Date' specify Year to end
        	**type**\: int
        
        	**range:** 0..2035
        
        .. attribute:: end_month
        
        	 Month to end 
        	**type**\:  :py:class:`ClockMonth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg.ClockMonth>`
        
        .. attribute:: end_hour
        
        	Hour to end 
        	**type**\: int
        
        	**range:** 0..23
        
        .. attribute:: end_minute
        
        	Minute to end 
        	**type**\: int
        
        	**range:** 0..59
        
        .. attribute:: offset
        
        	Offset to add in minutes 
        	**type**\: int
        
        	**range:** 1..1440
        
        	**units**\: minute
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-infra-clock-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Clock.SummerTime, self).__init__()

            self.yang_name = "summer-time"
            self.yang_parent_name = "clock"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('time_zone_name', (YLeaf(YType.str, 'time-zone-name'), ['str'])),
                ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg', 'ClockSummerTimeMode', '')])),
                ('start_week_number_or_start_date', (YLeaf(YType.uint32, 'start-week-number-or-start-date'), ['int'])),
                ('start_weekday_or_start_year', (YLeaf(YType.uint32, 'start-weekday-or-start-year'), ['int'])),
                ('start_month', (YLeaf(YType.enumeration, 'start-month'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg', 'ClockMonth', '')])),
                ('start_hour', (YLeaf(YType.uint32, 'start-hour'), ['int'])),
                ('start_minute', (YLeaf(YType.uint32, 'start-minute'), ['int'])),
                ('end_week_number_or_end_date', (YLeaf(YType.uint32, 'end-week-number-or-end-date'), ['int'])),
                ('end_weekday_or_end_year', (YLeaf(YType.uint32, 'end-weekday-or-end-year'), ['int'])),
                ('end_month', (YLeaf(YType.enumeration, 'end-month'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg', 'ClockMonth', '')])),
                ('end_hour', (YLeaf(YType.uint32, 'end-hour'), ['int'])),
                ('end_minute', (YLeaf(YType.uint32, 'end-minute'), ['int'])),
                ('offset', (YLeaf(YType.uint32, 'offset'), ['int'])),
            ])
            self.time_zone_name = None
            self.mode = None
            self.start_week_number_or_start_date = None
            self.start_weekday_or_start_year = None
            self.start_month = None
            self.start_hour = None
            self.start_minute = None
            self.end_week_number_or_end_date = None
            self.end_weekday_or_end_year = None
            self.end_month = None
            self.end_hour = None
            self.end_minute = None
            self.offset = None
            self._segment_path = lambda: "summer-time"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-infra-clock-cfg:clock/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Clock.SummerTime, ['time_zone_name', 'mode', 'start_week_number_or_start_date', 'start_weekday_or_start_year', 'start_month', 'start_hour', 'start_minute', 'end_week_number_or_end_date', 'end_weekday_or_end_year', 'end_month', 'end_hour', 'end_minute', 'offset'], name, value)



    class TimeZone(Entity):
        """
        Configure time zone
        
        .. attribute:: time_zone_name
        
        	Name of time zone
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: hour_offset
        
        	Hours offset from UTC
        	**type**\: int
        
        	**range:** \-23..23
        
        	**mandatory**\: True
        
        	**units**\: hour
        
        .. attribute:: minute_offset
        
        	Minutes offset from UTC
        	**type**\: int
        
        	**range:** 0..59
        
        	**units**\: minute
        
        	**default value**\: 0
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-infra-clock-cfg'
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
                ('hour_offset', (YLeaf(YType.int32, 'hour-offset'), ['int'])),
                ('minute_offset', (YLeaf(YType.uint32, 'minute-offset'), ['int'])),
            ])
            self.time_zone_name = None
            self.hour_offset = None
            self.minute_offset = None
            self._segment_path = lambda: "time-zone"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-infra-clock-cfg:clock/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Clock.TimeZone, ['time_zone_name', 'hour_offset', 'minute_offset'], name, value)


    def clone_ptr(self):
        self._top_entity = Clock()
        return self._top_entity



