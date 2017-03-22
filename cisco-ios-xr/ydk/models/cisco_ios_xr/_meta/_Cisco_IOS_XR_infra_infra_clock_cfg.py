


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'ClockMonthEnum' : _MetaInfoEnum('ClockMonthEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg',
        {
            'january':'january',
            'february':'february',
            'march':'march',
            'april':'april',
            'may':'may',
            'june':'june',
            'july':'july',
            'august':'august',
            'september':'september',
            'october':'october',
            'november':'november',
            'december':'december',
        }, 'Cisco-IOS-XR-infra-infra-clock-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-infra-clock-cfg']),
    'ClockSummerTimeModeEnum' : _MetaInfoEnum('ClockSummerTimeModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg',
        {
            'recurring':'recurring',
            'date':'date',
        }, 'Cisco-IOS-XR-infra-infra-clock-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-infra-clock-cfg']),
    'Clock.SummerTime' : {
        'meta_info' : _MetaInfoClass('Clock.SummerTime',
            False, 
            [
            _MetaInfoClassMember('end-hour', ATTRIBUTE, 'int' , None, None, 
                [('0', '23')], [], 
                '''                Hour to end 
                ''',
                'end_hour',
                'Cisco-IOS-XR-infra-infra-clock-cfg', False),
            _MetaInfoClassMember('end-minute', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                Minute to end 
                ''',
                'end_minute',
                'Cisco-IOS-XR-infra-infra-clock-cfg', False),
            _MetaInfoClassMember('end-month', REFERENCE_ENUM_CLASS, 'ClockMonthEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg', 'ClockMonthEnum', 
                [], [], 
                '''                 Month to end 
                ''',
                'end_month',
                'Cisco-IOS-XR-infra-infra-clock-cfg', False),
            _MetaInfoClassMember('end-week-number-or-end-date', ATTRIBUTE, 'int' , None, None, 
                [('1', '31')], [], 
                '''                If Mode is set to 'Recurring' specify Week
                number of the Month to end (first and last
                strings are not allowed as they are in CLI), if
                Mode is set to 'Date' specify Date to End
                ''',
                'end_week_number_or_end_date',
                'Cisco-IOS-XR-infra-infra-clock-cfg', False),
            _MetaInfoClassMember('end-weekday-or-end-year', ATTRIBUTE, 'int' , None, None, 
                [('0', '2035')], [], 
                '''                If Mode is set to 'Recurring' specify Weekday
                to end , if Mode is set to 'Date' specify Year
                to end
                ''',
                'end_weekday_or_end_year',
                'Cisco-IOS-XR-infra-infra-clock-cfg', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'ClockSummerTimeModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg', 'ClockSummerTimeModeEnum', 
                [], [], 
                '''                Summer time mode
                ''',
                'mode',
                'Cisco-IOS-XR-infra-infra-clock-cfg', False),
            _MetaInfoClassMember('offset', ATTRIBUTE, 'int' , None, None, 
                [('1', '1440')], [], 
                '''                Offset to add in minutes 
                ''',
                'offset',
                'Cisco-IOS-XR-infra-infra-clock-cfg', False),
            _MetaInfoClassMember('start-hour', ATTRIBUTE, 'int' , None, None, 
                [('0', '23')], [], 
                '''                Hour to start 
                ''',
                'start_hour',
                'Cisco-IOS-XR-infra-infra-clock-cfg', False),
            _MetaInfoClassMember('start-minute', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                Minute to start 
                ''',
                'start_minute',
                'Cisco-IOS-XR-infra-infra-clock-cfg', False),
            _MetaInfoClassMember('start-month', REFERENCE_ENUM_CLASS, 'ClockMonthEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg', 'ClockMonthEnum', 
                [], [], 
                '''                 Month to start 
                ''',
                'start_month',
                'Cisco-IOS-XR-infra-infra-clock-cfg', False),
            _MetaInfoClassMember('start-week-number-or-start-date', ATTRIBUTE, 'int' , None, None, 
                [('1', '31')], [], 
                '''                 If Mode is set to 'Recurring' specify Week
                number of the Month to start (first and last
                strings are not allowed as they are in CLI) ,
                if Mode is set to 'Date' specify Date to start 
                ''',
                'start_week_number_or_start_date',
                'Cisco-IOS-XR-infra-infra-clock-cfg', False),
            _MetaInfoClassMember('start-weekday-or-start-year', ATTRIBUTE, 'int' , None, None, 
                [('0', '2035')], [], 
                '''                 If Mode is set to 'Recurring' specify Weekday
                to start , if Mode is set to 'Date' specify
                Year to start 
                ''',
                'start_weekday_or_start_year',
                'Cisco-IOS-XR-infra-infra-clock-cfg', False),
            _MetaInfoClassMember('time-zone-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of time zone in summer
                ''',
                'time_zone_name',
                'Cisco-IOS-XR-infra-infra-clock-cfg', False),
            ],
            'Cisco-IOS-XR-infra-infra-clock-cfg',
            'summer-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-infra-clock-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg'
        ),
    },
    'Clock.TimeZone' : {
        'meta_info' : _MetaInfoClass('Clock.TimeZone',
            False, 
            [
            _MetaInfoClassMember('hour-offset', ATTRIBUTE, 'int' , None, None, 
                [('-23', '23')], [], 
                '''                Hours offset from UTC
                ''',
                'hour_offset',
                'Cisco-IOS-XR-infra-infra-clock-cfg', False),
            _MetaInfoClassMember('minute-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                Minutes offset from UTC
                ''',
                'minute_offset',
                'Cisco-IOS-XR-infra-infra-clock-cfg', False),
            _MetaInfoClassMember('time-zone-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of time zone
                ''',
                'time_zone_name',
                'Cisco-IOS-XR-infra-infra-clock-cfg', False),
            ],
            'Cisco-IOS-XR-infra-infra-clock-cfg',
            'time-zone',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-infra-clock-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg'
        ),
    },
    'Clock' : {
        'meta_info' : _MetaInfoClass('Clock',
            False, 
            [
            _MetaInfoClassMember('summer-time', REFERENCE_CLASS, 'SummerTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg', 'Clock.SummerTime', 
                [], [], 
                '''                Configure summer (daylight savings) time
                ''',
                'summer_time',
                'Cisco-IOS-XR-infra-infra-clock-cfg', False),
            _MetaInfoClassMember('time-zone', REFERENCE_CLASS, 'TimeZone' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg', 'Clock.TimeZone', 
                [], [], 
                '''                Configure time zone
                ''',
                'time_zone',
                'Cisco-IOS-XR-infra-infra-clock-cfg', False),
            ],
            'Cisco-IOS-XR-infra-infra-clock-cfg',
            'clock',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-infra-clock-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg'
        ),
    },
}
_meta_table['Clock.SummerTime']['meta_info'].parent =_meta_table['Clock']['meta_info']
_meta_table['Clock.TimeZone']['meta_info'].parent =_meta_table['Clock']['meta_info']
