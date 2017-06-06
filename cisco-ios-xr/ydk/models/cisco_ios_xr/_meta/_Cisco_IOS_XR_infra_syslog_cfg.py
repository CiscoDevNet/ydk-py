


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'LoggingDscpValueEnum' : _MetaInfoEnum('LoggingDscpValueEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'default':'default',
            'af11':'af11',
            'af12':'af12',
            'af13':'af13',
            'af21':'af21',
            'af22':'af22',
            'af23':'af23',
            'af31':'af31',
            'af32':'af32',
            'af33':'af33',
            'af41':'af41',
            'af42':'af42',
            'af43':'af43',
            'ef':'ef',
            'cs1':'cs1',
            'cs2':'cs2',
            'cs3':'cs3',
            'cs4':'cs4',
            'cs5':'cs5',
            'cs6':'cs6',
            'cs7':'cs7',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'LoggingDscpEnum' : _MetaInfoEnum('LoggingDscpEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'dscp':'dscp',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'LogMessageSeverityEnum' : _MetaInfoEnum('LogMessageSeverityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'emergency':'emergency',
            'alert':'alert',
            'critical':'critical',
            'error':'error',
            'warning':'warning',
            'notice':'notice',
            'informational':'informational',
            'debug':'debug',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'TimeInfoEnum' : _MetaInfoEnum('TimeInfoEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'LoggingPrecedenceValueEnum' : _MetaInfoEnum('LoggingPrecedenceValueEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'routine':'routine',
            'priority':'priority',
            'immediate':'immediate',
            'flash':'flash',
            'flash-override':'flash_override',
            'critical':'critical',
            'internet':'internet',
            'network':'network',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'LoggingPrecedenceEnum' : _MetaInfoEnum('LoggingPrecedenceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'precedence':'precedence',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'LoggingLevelsEnum' : _MetaInfoEnum('LoggingLevelsEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'emergency':'emergency',
            'alert':'alert',
            'critical':'critical',
            'error':'error',
            'warning':'warning',
            'notice':'notice',
            'info':'info',
            'debug':'debug',
            'disable':'disable',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'LoggingTosEnum' : _MetaInfoEnum('LoggingTosEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'precedence':'precedence',
            'dscp':'dscp',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'FacilityEnum' : _MetaInfoEnum('FacilityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'kern':'kern',
            'user':'user',
            'mail':'mail',
            'daemon':'daemon',
            'auth':'auth',
            'syslog':'syslog',
            'lpr':'lpr',
            'news':'news',
            'uucp':'uucp',
            'cron':'cron',
            'authpriv':'authpriv',
            'ftp':'ftp',
            'local0':'local0',
            'local1':'local1',
            'local2':'local2',
            'local3':'local3',
            'local4':'local4',
            'local5':'local5',
            'local6':'local6',
            'local7':'local7',
            'sys9':'sys9',
            'sys10':'sys10',
            'sys11':'sys11',
            'sys12':'sys12',
            'sys13':'sys13',
            'sys14':'sys14',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'LogCollectFrequencyEnum' : _MetaInfoEnum('LogCollectFrequencyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'weekly':'weekly',
            'daily':'daily',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'LogSeverityEnum' : _MetaInfoEnum('LogSeverityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'emergency':'emergency',
            'alert':'alert',
            'critical':'critical',
            'error':'error',
            'warning':'warning',
            'notice':'notice',
            'informational':'informational',
            'debug':'debug',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue' : {
        'meta_info' : _MetaInfoClass('SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue',
            False, 
            [
            _MetaInfoClassMember('msec', REFERENCE_ENUM_CLASS, 'TimeInfoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfoEnum', 
                [], [], 
                '''                Seconds
                ''',
                'msec',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('time-stamp-value', REFERENCE_ENUM_CLASS, 'TimeInfoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfoEnum', 
                [], [], 
                '''                Time
                ''',
                'time_stamp_value',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('time-zone', REFERENCE_ENUM_CLASS, 'TimeInfoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfoEnum', 
                [], [], 
                '''                Timezone
                ''',
                'time_zone',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('year', REFERENCE_ENUM_CLASS, 'TimeInfoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfoEnum', 
                [], [], 
                '''                Year
                ''',
                'year',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'log-datetime-value',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'SyslogService.Timestamps.Log.LogDatetime' : {
        'meta_info' : _MetaInfoClass('SyslogService.Timestamps.Log.LogDatetime',
            False, 
            [
            _MetaInfoClassMember('log-datetime-value', REFERENCE_CLASS, 'LogDatetimeValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue', 
                [], [], 
                '''                Set timestamp for log message
                ''',
                'log_datetime_value',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'log-datetime',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'SyslogService.Timestamps.Log' : {
        'meta_info' : _MetaInfoClass('SyslogService.Timestamps.Log',
            False, 
            [
            _MetaInfoClassMember('log-datetime', REFERENCE_CLASS, 'LogDatetime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'SyslogService.Timestamps.Log.LogDatetime', 
                [], [], 
                '''                Timestamp with date and time
                ''',
                'log_datetime',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('log-timestamp-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable timestamp log messages
                ''',
                'log_timestamp_disable',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('log-uptime', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Timestamp with systime uptime
                ''',
                'log_uptime',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'log',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue' : {
        'meta_info' : _MetaInfoClass('SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue',
            False, 
            [
            _MetaInfoClassMember('msec', REFERENCE_ENUM_CLASS, 'TimeInfoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfoEnum', 
                [], [], 
                '''                Seconds
                ''',
                'msec',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('time-stamp-value', REFERENCE_ENUM_CLASS, 'TimeInfoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfoEnum', 
                [], [], 
                '''                Time
                ''',
                'time_stamp_value',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('time-zone', REFERENCE_ENUM_CLASS, 'TimeInfoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfoEnum', 
                [], [], 
                '''                Timezone
                ''',
                'time_zone',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('year', REFERENCE_ENUM_CLASS, 'TimeInfoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfoEnum', 
                [], [], 
                '''                Year
                ''',
                'year',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'datetime-value',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'SyslogService.Timestamps.Debug.DebugDatetime' : {
        'meta_info' : _MetaInfoClass('SyslogService.Timestamps.Debug.DebugDatetime',
            False, 
            [
            _MetaInfoClassMember('datetime-value', REFERENCE_CLASS, 'DatetimeValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue', 
                [], [], 
                '''                Set time format for debug msg
                ''',
                'datetime_value',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'debug-datetime',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'SyslogService.Timestamps.Debug' : {
        'meta_info' : _MetaInfoClass('SyslogService.Timestamps.Debug',
            False, 
            [
            _MetaInfoClassMember('debug-datetime', REFERENCE_CLASS, 'DebugDatetime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'SyslogService.Timestamps.Debug.DebugDatetime', 
                [], [], 
                '''                Timestamp with date and time
                ''',
                'debug_datetime',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('debug-timestamp-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable timestamp debug messages
                ''',
                'debug_timestamp_disable',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('debug-uptime', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Timestamp with systime uptime
                ''',
                'debug_uptime',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'debug',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'SyslogService.Timestamps' : {
        'meta_info' : _MetaInfoClass('SyslogService.Timestamps',
            False, 
            [
            _MetaInfoClassMember('debug', REFERENCE_CLASS, 'Debug' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'SyslogService.Timestamps.Debug', 
                [], [], 
                '''                Timestamp debug messages
                ''',
                'debug',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable timestamp debug/log messages
                ''',
                'enable',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('log', REFERENCE_CLASS, 'Log' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'SyslogService.Timestamps.Log', 
                [], [], 
                '''                Timestamp log messages
                ''',
                'log',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'timestamps',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'SyslogService' : {
        'meta_info' : _MetaInfoClass('SyslogService',
            False, 
            [
            _MetaInfoClassMember('timestamps', REFERENCE_CLASS, 'Timestamps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'SyslogService.Timestamps', 
                [], [], 
                '''                Timestamp debug/log messages configuration
                ''',
                'timestamps',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'syslog-service',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.MonitorLogging.MonitorDiscriminator' : {
        'meta_info' : _MetaInfoClass('Syslog.MonitorLogging.MonitorDiscriminator',
            False, 
            [
            _MetaInfoClassMember('match1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set monitor logging match1 discriminator
                ''',
                'match1',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('match2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set monitor logging match2 discriminator
                ''',
                'match2',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('match3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set monitor logging match3 discriminator
                ''',
                'match3',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set monitor logging no-match1 discriminator
                ''',
                'nomatch1',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set monitor logging no-match2 discriminator
                ''',
                'nomatch2',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set monitor logging no-match3 discriminator
                ''',
                'nomatch3',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'monitor-discriminator',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.MonitorLogging' : {
        'meta_info' : _MetaInfoClass('Syslog.MonitorLogging',
            False, 
            [
            _MetaInfoClassMember('logging-level', REFERENCE_ENUM_CLASS, 'LoggingLevelsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingLevelsEnum', 
                [], [], 
                '''                Monitor Logging Level
                ''',
                'logging_level',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('monitor-discriminator', REFERENCE_CLASS, 'MonitorDiscriminator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.MonitorLogging.MonitorDiscriminator', 
                [], [], 
                '''                Set monitor logging discriminators
                ''',
                'monitor_discriminator',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'monitor-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HistoryLogging' : {
        'meta_info' : _MetaInfoClass('Syslog.HistoryLogging',
            False, 
            [
            _MetaInfoClassMember('history-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '500')], [], 
                '''                Logging history size
                ''',
                'history_size',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('logging-level', REFERENCE_ENUM_CLASS, 'LoggingLevelsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingLevelsEnum', 
                [], [], 
                '''                History logging level
                ''',
                'logging_level',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'history-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.LoggingFacilities' : {
        'meta_info' : _MetaInfoClass('Syslog.LoggingFacilities',
            False, 
            [
            _MetaInfoClassMember('facility-level', REFERENCE_ENUM_CLASS, 'FacilityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'FacilityEnum', 
                [], [], 
                '''                Facility from which logging is done
                ''',
                'facility_level',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'logging-facilities',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.TrapLogging' : {
        'meta_info' : _MetaInfoClass('Syslog.TrapLogging',
            False, 
            [
            _MetaInfoClassMember('logging-level', REFERENCE_ENUM_CLASS, 'LoggingLevelsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingLevelsEnum', 
                [], [], 
                '''                Trap logging level
                ''',
                'logging_level',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'trap-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.BufferedLogging.BufferedDiscriminator' : {
        'meta_info' : _MetaInfoClass('Syslog.BufferedLogging.BufferedDiscriminator',
            False, 
            [
            _MetaInfoClassMember('match1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set buffered logging match1 discriminator
                ''',
                'match1',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('match2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set buffered logging match2 discriminator
                ''',
                'match2',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('match3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set buffered logging match3 discriminator
                ''',
                'match3',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set buffered logging no-match1 discriminator
                ''',
                'nomatch1',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set buffered logging no-match2 discriminator
                ''',
                'nomatch2',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set buffered logging no-match3 discriminator
                ''',
                'nomatch3',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'buffered-discriminator',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.BufferedLogging' : {
        'meta_info' : _MetaInfoClass('Syslog.BufferedLogging',
            False, 
            [
            _MetaInfoClassMember('buffer-size', ATTRIBUTE, 'int' , None, None, 
                [('4096', '4294967295')], [], 
                '''                Logging buffered size
                ''',
                'buffer_size',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('buffered-discriminator', REFERENCE_CLASS, 'BufferedDiscriminator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.BufferedLogging.BufferedDiscriminator', 
                [], [], 
                '''                Set buffered logging discriminators
                ''',
                'buffered_discriminator',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('logging-level', REFERENCE_ENUM_CLASS, 'LoggingLevelsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingLevelsEnum', 
                [], [], 
                '''                Logging level for Buffered logging
                ''',
                'logging_level',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'buffered-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityPort' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityPort',
            False, 
            [
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Port for the logging host
                ''',
                'port',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('severity', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Severity for the logging host
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv6-severity-port',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6Discriminator' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6Discriminator',
            False, 
            [
            _MetaInfoClassMember('match1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set IPv6 logging match1 discriminator
                ''',
                'match1',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('match2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set IPv6 logging match2 discriminator
                ''',
                'match2',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('match3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set IPv6 logging match3 discriminator
                ''',
                'match3',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set IPv6 logging no-match1 discriminator
                ''',
                'nomatch1',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set IPv6 logging no-match2 discriminator
                ''',
                'nomatch2',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set IPv6 logging no-match3 discriminator
                ''',
                'nomatch3',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv6-discriminator',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel',
            False, 
            [
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'LogSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LogSeverityEnum', 
                [], [], 
                '''                Severity for the logging host
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv6-severity-level',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels',
            False, 
            [
            _MetaInfoClassMember('ipv6-severity-level', REFERENCE_LIST, 'Ipv6SeverityLevel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel', 
                [], [], 
                '''                Severity for the logging host
                ''',
                'ipv6_severity_level',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv6-severity-levels',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address of the logging host
                ''',
                'address',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            _MetaInfoClassMember('ipv6-discriminator', REFERENCE_CLASS, 'Ipv6Discriminator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6Discriminator', 
                [], [], 
                '''                Set IPv6 logging discriminators
                ''',
                'ipv6_discriminator',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('ipv6-severity-levels', REFERENCE_CLASS, 'Ipv6SeverityLevels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels', 
                [], [], 
                '''                Severity container of the logging host
                ''',
                'ipv6_severity_levels',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('ipv6-severity-port', REFERENCE_CLASS, 'Ipv6SeverityPort' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityPort', 
                [], [], 
                '''                Severity/Port for the logging host
                ''',
                'ipv6_severity_port',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv6S' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv6S',
            False, 
            [
            _MetaInfoClassMember('ipv6', REFERENCE_LIST, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6', 
                [], [], 
                '''                IPv6 address of the logging host
                ''',
                'ipv6',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv6s',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity',
            False, 
            [
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'LogSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LogSeverityEnum', 
                [], [], 
                '''                Severity for the logging host
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'host-name-severity',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities',
            False, 
            [
            _MetaInfoClassMember('host-name-severity', REFERENCE_LIST, 'HostNameSeverity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity', 
                [], [], 
                '''                Severity for the logging host
                ''',
                'host_name_severity',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'host-name-severities',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameDiscriminator' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameDiscriminator',
            False, 
            [
            _MetaInfoClassMember('match1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set hostname logging match1 discriminator
                ''',
                'match1',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('match2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set hostname logging match2 discriminator
                ''',
                'match2',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('match3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set hostname logging match3 discriminator
                ''',
                'match3',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set hostname logging no-match1
                discriminator
                ''',
                'nomatch1',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set hostname logging no-match2
                discriminator
                ''',
                'nomatch2',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set hostname logging no-match3
                discriminator
                ''',
                'nomatch3',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'host-name-discriminator',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort',
            False, 
            [
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Port for the logging host
                ''',
                'port',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('severity', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Severity for the logging host
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'host-severity-port',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Hosts.Host' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Hosts.Host',
            False, 
            [
            _MetaInfoClassMember('host-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the logging host
                ''',
                'host_name',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            _MetaInfoClassMember('host-name-discriminator', REFERENCE_CLASS, 'HostNameDiscriminator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameDiscriminator', 
                [], [], 
                '''                Set Hostname logging discriminators
                ''',
                'host_name_discriminator',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('host-name-severities', REFERENCE_CLASS, 'HostNameSeverities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities', 
                [], [], 
                '''                Severity container of the logging host
                ''',
                'host_name_severities',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('host-severity-port', REFERENCE_CLASS, 'HostSeverityPort' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort', 
                [], [], 
                '''                Severity/Port for the logging host
                ''',
                'host_severity_port',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'host',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Hosts' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Hosts',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Hosts.Host', 
                [], [], 
                '''                Name of the logging host
                ''',
                'host',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel',
            False, 
            [
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'LogSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LogSeverityEnum', 
                [], [], 
                '''                Severity for the logging host
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv4-severity-level',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels',
            False, 
            [
            _MetaInfoClassMember('ipv4-severity-level', REFERENCE_LIST, 'Ipv4SeverityLevel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel', 
                [], [], 
                '''                Severity for the logging host
                ''',
                'ipv4_severity_level',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv4-severity-levels',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityPort' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityPort',
            False, 
            [
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Port for the logging host
                ''',
                'port',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('severity', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Severity for the logging host
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv4-severity-port',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4Discriminator' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4Discriminator',
            False, 
            [
            _MetaInfoClassMember('match1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set IPv4 logging match1 discriminator
                ''',
                'match1',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('match2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set IPv4 logging match2 discriminator
                ''',
                'match2',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('match3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set IPv4 logging match3 discriminator
                ''',
                'match3',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set IPv4 logging no-match1 discriminator
                ''',
                'nomatch1',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set IPv4 logging no-match2 discriminator
                ''',
                'nomatch2',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set IPv4 logging no-match3 discriminator
                ''',
                'nomatch3',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv4-discriminator',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address of the logging host
                ''',
                'address',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            _MetaInfoClassMember('ipv4-discriminator', REFERENCE_CLASS, 'Ipv4Discriminator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4Discriminator', 
                [], [], 
                '''                Set IPv4 logging discriminators
                ''',
                'ipv4_discriminator',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('ipv4-severity-levels', REFERENCE_CLASS, 'Ipv4SeverityLevels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels', 
                [], [], 
                '''                Severity container of the logging host
                ''',
                'ipv4_severity_levels',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('ipv4-severity-port', REFERENCE_CLASS, 'Ipv4SeverityPort' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityPort', 
                [], [], 
                '''                Severity/Port for the logging host
                ''',
                'ipv4_severity_port',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv4S' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv4S',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_LIST, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4', 
                [], [], 
                '''                IPv4 address of the logging host
                ''',
                'ipv4',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv4s',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the VRF instance
                ''',
                'vrf_name',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Hosts', 
                [], [], 
                '''                List of the logging host
                ''',
                'hosts',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('ipv4s', REFERENCE_CLASS, 'Ipv4S' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv4S', 
                [], [], 
                '''                List of the IPv4 logging host
                ''',
                'ipv4s',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('ipv6s', REFERENCE_CLASS, 'Ipv6S' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv6S', 
                [], [], 
                '''                List of the IPv6 logging host
                ''',
                'ipv6s',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf', 
                [], [], 
                '''                VRF specific data
                ''',
                'vrf',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer',
            False, 
            [
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs', 
                [], [], 
                '''                VRF table
                ''',
                'vrfs',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'host-server',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.ConsoleLogging.ConsoleDiscriminator' : {
        'meta_info' : _MetaInfoClass('Syslog.ConsoleLogging.ConsoleDiscriminator',
            False, 
            [
            _MetaInfoClassMember('match1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set console logging match1 discriminator
                ''',
                'match1',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('match2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set console logging match2 discriminator
                ''',
                'match2',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('match3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set console logging match3 discriminator
                ''',
                'match3',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set console logging no-match1 discriminator
                ''',
                'nomatch1',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set console logging no-match2 discriminator
                ''',
                'nomatch2',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set console logging no-match3 discriminator
                ''',
                'nomatch3',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'console-discriminator',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.ConsoleLogging' : {
        'meta_info' : _MetaInfoClass('Syslog.ConsoleLogging',
            False, 
            [
            _MetaInfoClassMember('console-discriminator', REFERENCE_CLASS, 'ConsoleDiscriminator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.ConsoleLogging.ConsoleDiscriminator', 
                [], [], 
                '''                Set console logging discriminators
                ''',
                'console_discriminator',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('logging-level', REFERENCE_ENUM_CLASS, 'LoggingLevelsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingLevelsEnum', 
                [], [], 
                '''                Console logging level
                ''',
                'logging_level',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'console-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Files.File.FileSpecification' : {
        'meta_info' : _MetaInfoClass('Syslog.Files.File.FileSpecification',
            False, 
            [
            _MetaInfoClassMember('max-file-size', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Maximum file size (in KB)
                ''',
                'max_file_size',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                File path
                ''',
                'path',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('severity', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Severity of messages
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'file-specification',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Files.File.FileLogAttributes' : {
        'meta_info' : _MetaInfoClass('Syslog.Files.File.FileLogAttributes',
            False, 
            [
            _MetaInfoClassMember('max-file-size', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Maximum file size (in KB)
                ''',
                'max_file_size',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('severity', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Severity of messages
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'file-log-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Files.File.FileLogDiscriminator' : {
        'meta_info' : _MetaInfoClass('Syslog.Files.File.FileLogDiscriminator',
            False, 
            [
            _MetaInfoClassMember('match1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set file logging match discriminator 1
                ''',
                'match1',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('match2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set file logging match discriminator 2
                ''',
                'match2',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('match3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set file logging match discriminator 3
                ''',
                'match3',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set file logging no match discriminator 1
                ''',
                'nomatch1',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set file logging no match discriminator 2
                ''',
                'nomatch2',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('nomatch3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set file logging no match discriminator 3
                ''',
                'nomatch3',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'file-log-discriminator',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Files.File' : {
        'meta_info' : _MetaInfoClass('Syslog.Files.File',
            False, 
            [
            _MetaInfoClassMember('file-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the file
                ''',
                'file_name',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            _MetaInfoClassMember('file-log-attributes', REFERENCE_CLASS, 'FileLogAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Files.File.FileLogAttributes', 
                [], [], 
                '''                Attributes of the logging file destination
                ''',
                'file_log_attributes',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('file-log-discriminator', REFERENCE_CLASS, 'FileLogDiscriminator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Files.File.FileLogDiscriminator', 
                [], [], 
                '''                Set File logging discriminators
                ''',
                'file_log_discriminator',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('file-specification', REFERENCE_CLASS, 'FileSpecification' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Files.File.FileSpecification', 
                [], [], 
                '''                Specifications of the logging file destination
                ''',
                'file_specification',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'file',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Files' : {
        'meta_info' : _MetaInfoClass('Syslog.Files',
            False, 
            [
            _MetaInfoClassMember('file', REFERENCE_LIST, 'File' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Files.File', 
                [], [], 
                '''                Specify File Name
                ''',
                'file',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'files',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Ipv4.Dscp' : {
        'meta_info' : _MetaInfoClass('Syslog.Ipv4.Dscp',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'LoggingDscpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpEnum', 
                [], [], 
                '''                Logging TOS type DSCP
                ''',
                'type',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('unused', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Unused
                ''',
                'unused',
                'Cisco-IOS-XR-infra-syslog-cfg', False, [
                    _MetaInfoClassMember('unused', REFERENCE_ENUM_CLASS, 'LoggingPrecedenceValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceValueEnum', 
                        [], [], 
                        '''                        Unused
                        ''',
                        'unused',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('unused', ATTRIBUTE, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Unused
                        ''',
                        'unused',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                ]),
            _MetaInfoClassMember('value', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Logging DSCP value
                ''',
                'value',
                'Cisco-IOS-XR-infra-syslog-cfg', False, [
                    _MetaInfoClassMember('value', REFERENCE_ENUM_CLASS, 'LoggingDscpValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpValueEnum', 
                        [], [], 
                        '''                        Logging DSCP value
                        ''',
                        'value',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        Logging DSCP value
                        ''',
                        'value',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'dscp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Ipv4.Tos' : {
        'meta_info' : _MetaInfoClass('Syslog.Ipv4.Tos',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Logging DSCP value
                ''',
                'dscp',
                'Cisco-IOS-XR-infra-syslog-cfg', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_ENUM_CLASS, 'LoggingDscpValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpValueEnum', 
                        [], [], 
                        '''                        Logging DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        Logging DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                ]),
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Logging precedence value
                ''',
                'precedence',
                'Cisco-IOS-XR-infra-syslog-cfg', False, [
                    _MetaInfoClassMember('precedence', REFERENCE_ENUM_CLASS, 'LoggingPrecedenceValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceValueEnum', 
                        [], [], 
                        '''                        Logging precedence value
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('precedence', ATTRIBUTE, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Logging precedence value
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                ]),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'LoggingTosEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingTosEnum', 
                [], [], 
                '''                Logging TOS type DSCP or precedence
                ''',
                'type',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'tos',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Ipv4.Precedence' : {
        'meta_info' : _MetaInfoClass('Syslog.Ipv4.Precedence',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'LoggingPrecedenceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceEnum', 
                [], [], 
                '''                Logging TOS type precedence
                ''',
                'type',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('unused', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Unused
                ''',
                'unused',
                'Cisco-IOS-XR-infra-syslog-cfg', False, [
                    _MetaInfoClassMember('unused', REFERENCE_ENUM_CLASS, 'LoggingDscpValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpValueEnum', 
                        [], [], 
                        '''                        Unused
                        ''',
                        'unused',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('unused', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        Unused
                        ''',
                        'unused',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                ]),
            _MetaInfoClassMember('value', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Logging precedence value
                ''',
                'value',
                'Cisco-IOS-XR-infra-syslog-cfg', False, [
                    _MetaInfoClassMember('value', REFERENCE_ENUM_CLASS, 'LoggingPrecedenceValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceValueEnum', 
                        [], [], 
                        '''                        Logging precedence value
                        ''',
                        'value',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Logging precedence value
                        ''',
                        'value',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'precedence',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Ipv4' : {
        'meta_info' : _MetaInfoClass('Syslog.Ipv4',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_CLASS, 'Dscp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Ipv4.Dscp', 
                [], [], 
                '''                DSCP value
                ''',
                'dscp',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('precedence', REFERENCE_CLASS, 'Precedence' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Ipv4.Precedence', 
                [], [], 
                '''                Precedence value
                ''',
                'precedence',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('tos', REFERENCE_CLASS, 'Tos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Ipv4.Tos', 
                [], [], 
                '''                Type of service
                ''',
                'tos',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Archive' : {
        'meta_info' : _MetaInfoClass('Syslog.Archive',
            False, 
            [
            _MetaInfoClassMember('device', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                '/disk0:' or '/disk1:' or '/harddisk:'
                ''',
                'device',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('file-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '2047')], [], 
                '''                The maximum file size for a single log file.
                ''',
                'file_size',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('frequency', REFERENCE_ENUM_CLASS, 'LogCollectFrequencyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LogCollectFrequencyEnum', 
                [], [], 
                '''                The collection interval for logs
                ''',
                'frequency',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('1', '256')], [], 
                '''                The maximum number of weeks of log to maintain
                ''',
                'length',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'LogMessageSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LogMessageSeverityEnum', 
                [], [], 
                '''                The minimum severity of log messages to archive
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('1', '2047')], [], 
                '''                The total size of the archive
                ''',
                'size',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                The size threshold at which a syslog is
                generated
                ''',
                'threshold',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'archive',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Ipv6.Dscp' : {
        'meta_info' : _MetaInfoClass('Syslog.Ipv6.Dscp',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'LoggingDscpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpEnum', 
                [], [], 
                '''                Logging TOS type DSCP
                ''',
                'type',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('unused', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Unused
                ''',
                'unused',
                'Cisco-IOS-XR-infra-syslog-cfg', False, [
                    _MetaInfoClassMember('unused', REFERENCE_ENUM_CLASS, 'LoggingPrecedenceValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceValueEnum', 
                        [], [], 
                        '''                        Unused
                        ''',
                        'unused',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('unused', ATTRIBUTE, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Unused
                        ''',
                        'unused',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                ]),
            _MetaInfoClassMember('value', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Logging DSCP value
                ''',
                'value',
                'Cisco-IOS-XR-infra-syslog-cfg', False, [
                    _MetaInfoClassMember('value', REFERENCE_ENUM_CLASS, 'LoggingDscpValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpValueEnum', 
                        [], [], 
                        '''                        Logging DSCP value
                        ''',
                        'value',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        Logging DSCP value
                        ''',
                        'value',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'dscp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Ipv6.TrafficClass' : {
        'meta_info' : _MetaInfoClass('Syslog.Ipv6.TrafficClass',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Logging DSCP value
                ''',
                'dscp',
                'Cisco-IOS-XR-infra-syslog-cfg', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_ENUM_CLASS, 'LoggingDscpValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpValueEnum', 
                        [], [], 
                        '''                        Logging DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        Logging DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                ]),
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Logging precedence value
                ''',
                'precedence',
                'Cisco-IOS-XR-infra-syslog-cfg', False, [
                    _MetaInfoClassMember('precedence', REFERENCE_ENUM_CLASS, 'LoggingPrecedenceValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceValueEnum', 
                        [], [], 
                        '''                        Logging precedence value
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('precedence', ATTRIBUTE, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Logging precedence value
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                ]),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'LoggingTosEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingTosEnum', 
                [], [], 
                '''                Logging TOS type DSCP or precedence
                ''',
                'type',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'traffic-class',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Ipv6.Precedence' : {
        'meta_info' : _MetaInfoClass('Syslog.Ipv6.Precedence',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'LoggingPrecedenceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceEnum', 
                [], [], 
                '''                Logging TOS type precedence
                ''',
                'type',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('unused', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Unused
                ''',
                'unused',
                'Cisco-IOS-XR-infra-syslog-cfg', False, [
                    _MetaInfoClassMember('unused', REFERENCE_ENUM_CLASS, 'LoggingDscpValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpValueEnum', 
                        [], [], 
                        '''                        Unused
                        ''',
                        'unused',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('unused', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        Unused
                        ''',
                        'unused',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                ]),
            _MetaInfoClassMember('value', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Logging precedence value
                ''',
                'value',
                'Cisco-IOS-XR-infra-syslog-cfg', False, [
                    _MetaInfoClassMember('value', REFERENCE_ENUM_CLASS, 'LoggingPrecedenceValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceValueEnum', 
                        [], [], 
                        '''                        Logging precedence value
                        ''',
                        'value',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Logging precedence value
                        ''',
                        'value',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'precedence',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Ipv6' : {
        'meta_info' : _MetaInfoClass('Syslog.Ipv6',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_CLASS, 'Dscp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Ipv6.Dscp', 
                [], [], 
                '''                DSCP value
                ''',
                'dscp',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('precedence', REFERENCE_CLASS, 'Precedence' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Ipv6.Precedence', 
                [], [], 
                '''                Precedence value
                ''',
                'precedence',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('traffic-class', REFERENCE_CLASS, 'TrafficClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Ipv6.TrafficClass', 
                [], [], 
                '''                Type of traffic class
                ''',
                'traffic_class',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf' : {
        'meta_info' : _MetaInfoClass('Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the VRF instance
                ''',
                'vrf_name',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'source-interface-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs' : {
        'meta_info' : _MetaInfoClass('Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs',
            False, 
            [
            _MetaInfoClassMember('source-interface-vrf', REFERENCE_LIST, 'SourceInterfaceVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf', 
                [], [], 
                '''                Specify VRF for source interface
                ''',
                'source_interface_vrf',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'source-interface-vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue' : {
        'meta_info' : _MetaInfoClass('Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue',
            False, 
            [
            _MetaInfoClassMember('src-interface-name-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Which Interface
                ''',
                'src_interface_name_value',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            _MetaInfoClassMember('source-interface-vrfs', REFERENCE_CLASS, 'SourceInterfaceVrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs', 
                [], [], 
                '''                Configure source interface VRF
                ''',
                'source_interface_vrfs',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'source-interface-value',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.SourceInterfaceTable.SourceInterfaceValues' : {
        'meta_info' : _MetaInfoClass('Syslog.SourceInterfaceTable.SourceInterfaceValues',
            False, 
            [
            _MetaInfoClassMember('source-interface-value', REFERENCE_LIST, 'SourceInterfaceValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue', 
                [], [], 
                '''                Source interface
                ''',
                'source_interface_value',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'source-interface-values',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.SourceInterfaceTable' : {
        'meta_info' : _MetaInfoClass('Syslog.SourceInterfaceTable',
            False, 
            [
            _MetaInfoClassMember('source-interface-values', REFERENCE_CLASS, 'SourceInterfaceValues' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.SourceInterfaceTable.SourceInterfaceValues', 
                [], [], 
                '''                Specify interface for source address in logging
                transactions
                ''',
                'source_interface_values',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'source-interface-table',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.AlarmLogger.AlarmFilterStrings.AlarmFilterString' : {
        'meta_info' : _MetaInfoClass('Syslog.AlarmLogger.AlarmFilterStrings.AlarmFilterString',
            False, 
            [
            _MetaInfoClassMember('filter-string', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Filter String
                ''',
                'filter_string',
                'Cisco-IOS-XR-infra-alarm-logger-cfg', True),
            ],
            'Cisco-IOS-XR-infra-alarm-logger-cfg',
            'alarm-filter-string',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-alarm-logger-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.AlarmLogger.AlarmFilterStrings' : {
        'meta_info' : _MetaInfoClass('Syslog.AlarmLogger.AlarmFilterStrings',
            False, 
            [
            _MetaInfoClassMember('alarm-filter-string', REFERENCE_LIST, 'AlarmFilterString' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.AlarmLogger.AlarmFilterStrings.AlarmFilterString', 
                [], [], 
                '''                Match string to filter alarms
                ''',
                'alarm_filter_string',
                'Cisco-IOS-XR-infra-alarm-logger-cfg', False),
            ],
            'Cisco-IOS-XR-infra-alarm-logger-cfg',
            'alarm-filter-strings',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-alarm-logger-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.AlarmLogger' : {
        'meta_info' : _MetaInfoClass('Syslog.AlarmLogger',
            False, 
            [
            _MetaInfoClassMember('alarm-filter-strings', REFERENCE_CLASS, 'AlarmFilterStrings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.AlarmLogger.AlarmFilterStrings', 
                [], [], 
                '''                List of filter strings
                ''',
                'alarm_filter_strings',
                'Cisco-IOS-XR-infra-alarm-logger-cfg', False),
            _MetaInfoClassMember('buffer-size', ATTRIBUTE, 'int' , None, None, 
                [('1024', '1024000')], [], 
                '''                Set size of the local event buffer
                ''',
                'buffer_size',
                'Cisco-IOS-XR-infra-alarm-logger-cfg', False),
            _MetaInfoClassMember('severity-level', REFERENCE_ENUM_CLASS, 'AlarmLoggerSeverityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_datatypes', 'AlarmLoggerSeverityLevelEnum', 
                [], [], 
                '''                Log all events with equal or higher (lower
                level) severity than this
                ''',
                'severity_level',
                'Cisco-IOS-XR-infra-alarm-logger-cfg', False),
            _MetaInfoClassMember('source-location', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable alarm source location in message text
                ''',
                'source_location',
                'Cisco-IOS-XR-infra-alarm-logger-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('10', '100')], [], 
                '''                Configure threshold (%) for capacity alarm
                ''',
                'threshold',
                'Cisco-IOS-XR-infra-alarm-logger-cfg', False),
            ],
            'Cisco-IOS-XR-infra-alarm-logger-cfg',
            'alarm-logger',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-alarm-logger-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules.Rule.Definition' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules.Rule.Definition',
            False, 
            [
            _MetaInfoClassMember('category-name-entry1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Root message category name
                ''',
                'category_name_entry1',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('category-name-entry10', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message category name
                ''',
                'category_name_entry10',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('category-name-entry2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message category name
                ''',
                'category_name_entry2',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('category-name-entry3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message category name
                ''',
                'category_name_entry3',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('category-name-entry4', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message category name
                ''',
                'category_name_entry4',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('category-name-entry5', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message category name
                ''',
                'category_name_entry5',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('category-name-entry6', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message category name
                ''',
                'category_name_entry6',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('category-name-entry7', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message category name
                ''',
                'category_name_entry7',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('category-name-entry8', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message category name
                ''',
                'category_name_entry8',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('category-name-entry9', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message category name
                ''',
                'category_name_entry9',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('group-name-entry1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Root message group name
                ''',
                'group_name_entry1',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('group-name-entry10', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message group name
                ''',
                'group_name_entry10',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('group-name-entry2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message group name
                ''',
                'group_name_entry2',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('group-name-entry3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message group name
                ''',
                'group_name_entry3',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('group-name-entry4', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message group name
                ''',
                'group_name_entry4',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('group-name-entry5', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message group name
                ''',
                'group_name_entry5',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('group-name-entry6', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message group name
                ''',
                'group_name_entry6',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('group-name-entry7', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message group name
                ''',
                'group_name_entry7',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('group-name-entry8', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message group name
                ''',
                'group_name_entry8',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('group-name-entry9', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message group name
                ''',
                'group_name_entry9',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('message-code-entry1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Root message code
                ''',
                'message_code_entry1',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('message-code-entry10', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message code
                ''',
                'message_code_entry10',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('message-code-entry2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message code
                ''',
                'message_code_entry2',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('message-code-entry3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message code
                ''',
                'message_code_entry3',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('message-code-entry4', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message code
                ''',
                'message_code_entry4',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('message-code-entry5', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message code
                ''',
                'message_code_entry5',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('message-code-entry6', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message code
                ''',
                'message_code_entry6',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('message-code-entry7', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message code
                ''',
                'message_code_entry7',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('message-code-entry8', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message code
                ''',
                'message_code_entry8',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('message-code-entry9', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message code
                ''',
                'message_code_entry9',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '7200000')], [], 
                '''                Timeout (time the rule is to be active) in
                milliseconds
                ''',
                'timeout',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'definition',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause',
            False, 
            [
            _MetaInfoClassMember('category', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message category
                ''',
                'category',
                'Cisco-IOS-XR-infra-correlator-cfg', True),
            _MetaInfoClassMember('group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message group
                ''',
                'group',
                'Cisco-IOS-XR-infra-correlator-cfg', True),
            _MetaInfoClassMember('message-code', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message code
                ''',
                'message_code',
                'Cisco-IOS-XR-infra-correlator-cfg', True),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'non-root-cause',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses',
            False, 
            [
            _MetaInfoClassMember('non-root-cause', REFERENCE_LIST, 'NonRootCause' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause', 
                [], [], 
                '''                A non-rootcause
                ''',
                'non_root_cause',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'non-root-causes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules.Rule.NonStateful.RootCause' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules.Rule.NonStateful.RootCause',
            False, 
            [
            _MetaInfoClassMember('category', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Root message category
                ''',
                'category',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Root message group
                ''',
                'group',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('message-code', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Root message code
                ''',
                'message_code',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'root-cause',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules.Rule.NonStateful' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules.Rule.NonStateful',
            False, 
            [
            _MetaInfoClassMember('context-correlation', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable correlation on alarm context
                ''',
                'context_correlation',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('non-root-causes', REFERENCE_CLASS, 'NonRootCauses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses', 
                [], [], 
                '''                Table of configured non-rootcause
                ''',
                'non_root_causes',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('root-cause', REFERENCE_CLASS, 'RootCause' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules.Rule.NonStateful.RootCause', 
                [], [], 
                '''                The root cause
                ''',
                'root_cause',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '7200000')], [], 
                '''                Timeout (time to wait for active correlation) in
                milliseconds
                ''',
                'timeout',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('timeout-root-cause', ATTRIBUTE, 'int' , None, None, 
                [('1', '7200000')], [], 
                '''                Rootcause Timeout (time to wait for rootcause)
                in milliseconds
                ''',
                'timeout_root_cause',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'non-stateful',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses.NonRootCause' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses.NonRootCause',
            False, 
            [
            _MetaInfoClassMember('category', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message category
                ''',
                'category',
                'Cisco-IOS-XR-infra-correlator-cfg', True),
            _MetaInfoClassMember('group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message group
                ''',
                'group',
                'Cisco-IOS-XR-infra-correlator-cfg', True),
            _MetaInfoClassMember('message-code', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlated message code
                ''',
                'message_code',
                'Cisco-IOS-XR-infra-correlator-cfg', True),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'non-root-cause',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses',
            False, 
            [
            _MetaInfoClassMember('non-root-cause', REFERENCE_LIST, 'NonRootCause' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses.NonRootCause', 
                [], [], 
                '''                A non-rootcause
                ''',
                'non_root_cause',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'non-root-causes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules.Rule.Stateful.RootCause' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules.Rule.Stateful.RootCause',
            False, 
            [
            _MetaInfoClassMember('category', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Root message category
                ''',
                'category',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Root message group
                ''',
                'group',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('message-code', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Root message code
                ''',
                'message_code',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'root-cause',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules.Rule.Stateful' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules.Rule.Stateful',
            False, 
            [
            _MetaInfoClassMember('context-correlation', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable correlation on alarm context
                ''',
                'context_correlation',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('non-root-causes', REFERENCE_CLASS, 'NonRootCauses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses', 
                [], [], 
                '''                Table of configured non-rootcause
                ''',
                'non_root_causes',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('reissue', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable reissue of non-bistate alarms on
                rootcause alarm clear
                ''',
                'reissue',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('reparent', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable reparent of alarm on rootcause alarm
                clear
                ''',
                'reparent',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('root-cause', REFERENCE_CLASS, 'RootCause' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules.Rule.Stateful.RootCause', 
                [], [], 
                '''                The root cause
                ''',
                'root_cause',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '7200000')], [], 
                '''                Timeout (time to wait for active correlation) in
                milliseconds
                ''',
                'timeout',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('timeout-root-cause', ATTRIBUTE, 'int' , None, None, 
                [('1', '7200000')], [], 
                '''                Rootcause Timeout (time to wait for rootcause)
                in milliseconds
                ''',
                'timeout_root_cause',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'stateful',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules.Rule.ApplyTo.Contexts' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules.Rule.ApplyTo.Contexts',
            False, 
            [
            _MetaInfoClassMember('context', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                One or more context names
                ''',
                'context',
                'Cisco-IOS-XR-infra-correlator-cfg', False, max_elements=32),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'contexts',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules.Rule.ApplyTo.Locations' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules.Rule.ApplyTo.Locations',
            False, 
            [
            _MetaInfoClassMember('location', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                One or more Locations
                ''',
                'location',
                'Cisco-IOS-XR-infra-correlator-cfg', False, max_elements=32),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'locations',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules.Rule.ApplyTo' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules.Rule.ApplyTo',
            False, 
            [
            _MetaInfoClassMember('all-of-router', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Apply the rule to all of the router
                ''',
                'all_of_router',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('contexts', REFERENCE_CLASS, 'Contexts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules.Rule.ApplyTo.Contexts', 
                [], [], 
                '''                Apply rule to a specified list of contexts,
                e.g. interfaces
                ''',
                'contexts',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('locations', REFERENCE_CLASS, 'Locations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules.Rule.ApplyTo.Locations', 
                [], [], 
                '''                Apply rule to a specified list of Locations
                ''',
                'locations',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'apply-to',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules.Rule.AppliedTo.Contexts.Context' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules.Rule.AppliedTo.Contexts.Context',
            False, 
            [
            _MetaInfoClassMember('context', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Context
                ''',
                'context',
                'Cisco-IOS-XR-infra-correlator-cfg', True),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'context',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules.Rule.AppliedTo.Contexts' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules.Rule.AppliedTo.Contexts',
            False, 
            [
            _MetaInfoClassMember('context', REFERENCE_LIST, 'Context' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules.Rule.AppliedTo.Contexts.Context', 
                [], [], 
                '''                A context
                ''',
                'context',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'contexts',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules.Rule.AppliedTo.Locations.Location' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules.Rule.AppliedTo.Locations.Location',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-infra-correlator-cfg', True),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'location',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules.Rule.AppliedTo.Locations' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules.Rule.AppliedTo.Locations',
            False, 
            [
            _MetaInfoClassMember('location', REFERENCE_LIST, 'Location' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules.Rule.AppliedTo.Locations.Location', 
                [], [], 
                '''                A location
                ''',
                'location',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'locations',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules.Rule.AppliedTo' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules.Rule.AppliedTo',
            False, 
            [
            _MetaInfoClassMember('all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Apply to all of the router
                ''',
                'all',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('contexts', REFERENCE_CLASS, 'Contexts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules.Rule.AppliedTo.Contexts', 
                [], [], 
                '''                Table of configured contexts to apply
                ''',
                'contexts',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('locations', REFERENCE_CLASS, 'Locations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules.Rule.AppliedTo.Locations', 
                [], [], 
                '''                Table of configured locations to apply
                ''',
                'locations',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'applied-to',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules.Rule' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules.Rule',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Rule name
                ''',
                'name',
                'Cisco-IOS-XR-infra-correlator-cfg', True),
            _MetaInfoClassMember('applied-to', REFERENCE_CLASS, 'AppliedTo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules.Rule.AppliedTo', 
                [], [], 
                '''                Applied to the Rule or Ruleset
                ''',
                'applied_to',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('apply-to', REFERENCE_CLASS, 'ApplyTo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules.Rule.ApplyTo', 
                [], [], 
                '''                Apply the Rules
                ''',
                'apply_to',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('definition', REFERENCE_CLASS, 'Definition' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules.Rule.Definition', 
                [], [], 
                '''                Configure a specified correlation rule
                ''',
                'definition',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('non-stateful', REFERENCE_CLASS, 'NonStateful' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules.Rule.NonStateful', 
                [], [], 
                '''                The Non-Stateful Rule Type
                ''',
                'non_stateful',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('stateful', REFERENCE_CLASS, 'Stateful' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules.Rule.Stateful', 
                [], [], 
                '''                The Stateful Rule Type
                ''',
                'stateful',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'rule',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.Rules' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.Rules',
            False, 
            [
            _MetaInfoClassMember('rule', REFERENCE_LIST, 'Rule' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules.Rule', 
                [], [], 
                '''                Rule name
                ''',
                'rule',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'rules',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.RuleSets.RuleSet.Rulenames.Rulename' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.RuleSets.RuleSet.Rulenames.Rulename',
            False, 
            [
            _MetaInfoClassMember('rulename', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Rule name
                ''',
                'rulename',
                'Cisco-IOS-XR-infra-correlator-cfg', True),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'rulename',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.RuleSets.RuleSet.Rulenames' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.RuleSets.RuleSet.Rulenames',
            False, 
            [
            _MetaInfoClassMember('rulename', REFERENCE_LIST, 'Rulename' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.RuleSets.RuleSet.Rulenames.Rulename', 
                [], [], 
                '''                A rulename
                ''',
                'rulename',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'rulenames',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts.Context' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts.Context',
            False, 
            [
            _MetaInfoClassMember('context', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Context
                ''',
                'context',
                'Cisco-IOS-XR-infra-correlator-cfg', True),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'context',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts',
            False, 
            [
            _MetaInfoClassMember('context', REFERENCE_LIST, 'Context' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts.Context', 
                [], [], 
                '''                A context
                ''',
                'context',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'contexts',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations.Location' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations.Location',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-infra-correlator-cfg', True),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'location',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations',
            False, 
            [
            _MetaInfoClassMember('location', REFERENCE_LIST, 'Location' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations.Location', 
                [], [], 
                '''                A location
                ''',
                'location',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'locations',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.RuleSets.RuleSet.AppliedTo' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.RuleSets.RuleSet.AppliedTo',
            False, 
            [
            _MetaInfoClassMember('all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Apply to all of the router
                ''',
                'all',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('contexts', REFERENCE_CLASS, 'Contexts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts', 
                [], [], 
                '''                Table of configured contexts to apply
                ''',
                'contexts',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('locations', REFERENCE_CLASS, 'Locations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations', 
                [], [], 
                '''                Table of configured locations to apply
                ''',
                'locations',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'applied-to',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.RuleSets.RuleSet' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.RuleSets.RuleSet',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Ruleset name
                ''',
                'name',
                'Cisco-IOS-XR-infra-correlator-cfg', True),
            _MetaInfoClassMember('applied-to', REFERENCE_CLASS, 'AppliedTo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.RuleSets.RuleSet.AppliedTo', 
                [], [], 
                '''                Applied to the Rule or Ruleset
                ''',
                'applied_to',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('rulenames', REFERENCE_CLASS, 'Rulenames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.RuleSets.RuleSet.Rulenames', 
                [], [], 
                '''                Table of configured rulenames
                ''',
                'rulenames',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'rule-set',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator.RuleSets' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator.RuleSets',
            False, 
            [
            _MetaInfoClassMember('rule-set', REFERENCE_LIST, 'RuleSet' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.RuleSets.RuleSet', 
                [], [], 
                '''                Ruleset name
                ''',
                'rule_set',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'rule-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Correlator' : {
        'meta_info' : _MetaInfoClass('Syslog.Correlator',
            False, 
            [
            _MetaInfoClassMember('buffer-size', ATTRIBUTE, 'int' , None, None, 
                [('1024', '52428800')], [], 
                '''                Configure size of the correlator buffer
                ''',
                'buffer_size',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('rule-sets', REFERENCE_CLASS, 'RuleSets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.RuleSets', 
                [], [], 
                '''                Table of configured rulesets
                ''',
                'rule_sets',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('rules', REFERENCE_CLASS, 'Rules' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator.Rules', 
                [], [], 
                '''                Table of configured rules
                ''',
                'rules',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'correlator',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Suppression.Rules.Rule.AppliedTo.Sources.Source' : {
        'meta_info' : _MetaInfoClass('Syslog.Suppression.Rules.Rule.AppliedTo.Sources.Source',
            False, 
            [
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Source
                ''',
                'source',
                'Cisco-IOS-XR-infra-correlator-cfg', True),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'source',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Suppression.Rules.Rule.AppliedTo.Sources' : {
        'meta_info' : _MetaInfoClass('Syslog.Suppression.Rules.Rule.AppliedTo.Sources',
            False, 
            [
            _MetaInfoClassMember('source', REFERENCE_LIST, 'Source' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Suppression.Rules.Rule.AppliedTo.Sources.Source', 
                [], [], 
                '''                An alarm source
                ''',
                'source',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'sources',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Suppression.Rules.Rule.AppliedTo' : {
        'meta_info' : _MetaInfoClass('Syslog.Suppression.Rules.Rule.AppliedTo',
            False, 
            [
            _MetaInfoClassMember('all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Apply to all of the router
                ''',
                'all',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('sources', REFERENCE_CLASS, 'Sources' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Suppression.Rules.Rule.AppliedTo.Sources', 
                [], [], 
                '''                Table of configured sources to apply
                ''',
                'sources',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'applied-to',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Suppression.Rules.Rule.AlarmCauses.AlarmCause' : {
        'meta_info' : _MetaInfoClass('Syslog.Suppression.Rules.Rule.AlarmCauses.AlarmCause',
            False, 
            [
            _MetaInfoClassMember('category', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Category
                ''',
                'category',
                'Cisco-IOS-XR-infra-correlator-cfg', True),
            _MetaInfoClassMember('group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Group
                ''',
                'group',
                'Cisco-IOS-XR-infra-correlator-cfg', True),
            _MetaInfoClassMember('code', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Code
                ''',
                'code',
                'Cisco-IOS-XR-infra-correlator-cfg', True),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'alarm-cause',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Suppression.Rules.Rule.AlarmCauses' : {
        'meta_info' : _MetaInfoClass('Syslog.Suppression.Rules.Rule.AlarmCauses',
            False, 
            [
            _MetaInfoClassMember('alarm-cause', REFERENCE_LIST, 'AlarmCause' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Suppression.Rules.Rule.AlarmCauses.AlarmCause', 
                [], [], 
                '''                Category, Group and Code of alarm/syslog to
                be suppressed
                ''',
                'alarm_cause',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'alarm-causes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Suppression.Rules.Rule' : {
        'meta_info' : _MetaInfoClass('Syslog.Suppression.Rules.Rule',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Rule name
                ''',
                'name',
                'Cisco-IOS-XR-infra-correlator-cfg', True),
            _MetaInfoClassMember('alarm-causes', REFERENCE_CLASS, 'AlarmCauses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Suppression.Rules.Rule.AlarmCauses', 
                [], [], 
                '''                Causes of alarms to be suppressed
                ''',
                'alarm_causes',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('all-alarms', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Suppress all alarms
                ''',
                'all_alarms',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('applied-to', REFERENCE_CLASS, 'AppliedTo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Suppression.Rules.Rule.AppliedTo', 
                [], [], 
                '''                Applied to the Rule
                ''',
                'applied_to',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'rule',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Suppression.Rules' : {
        'meta_info' : _MetaInfoClass('Syslog.Suppression.Rules',
            False, 
            [
            _MetaInfoClassMember('rule', REFERENCE_LIST, 'Rule' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Suppression.Rules.Rule', 
                [], [], 
                '''                Rule name
                ''',
                'rule',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'rules',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Suppression' : {
        'meta_info' : _MetaInfoClass('Syslog.Suppression',
            False, 
            [
            _MetaInfoClassMember('rules', REFERENCE_CLASS, 'Rules' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Suppression.Rules', 
                [], [], 
                '''                Table of configured rules
                ''',
                'rules',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            ],
            'Cisco-IOS-XR-infra-correlator-cfg',
            'suppression',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog' : {
        'meta_info' : _MetaInfoClass('Syslog',
            False, 
            [
            _MetaInfoClassMember('alarm-logger', REFERENCE_CLASS, 'AlarmLogger' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.AlarmLogger', 
                [], [], 
                '''                Alarm Logger Properties
                ''',
                'alarm_logger',
                'Cisco-IOS-XR-infra-alarm-logger-cfg', False),
            _MetaInfoClassMember('archive', REFERENCE_CLASS, 'Archive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Archive', 
                [], [], 
                '''                Archive attributes configuration
                ''',
                'archive',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('buffered-logging', REFERENCE_CLASS, 'BufferedLogging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.BufferedLogging', 
                [], [], 
                '''                Set buffered logging parameters
                ''',
                'buffered_logging',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('console-logging', REFERENCE_CLASS, 'ConsoleLogging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.ConsoleLogging', 
                [], [], 
                '''                Set console logging
                ''',
                'console_logging',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('correlator', REFERENCE_CLASS, 'Correlator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Correlator', 
                [], [], 
                '''                Configure properties of the event correlator
                ''',
                'correlator',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('enable-console-logging', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled
                ''',
                'enable_console_logging',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('files', REFERENCE_CLASS, 'Files' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Files', 
                [], [], 
                '''                Configure logging file destination
                ''',
                'files',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('history-logging', REFERENCE_CLASS, 'HistoryLogging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HistoryLogging', 
                [], [], 
                '''                Set history logging
                ''',
                'history_logging',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('host-name-prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Hostname prefix to add on msgs to servers
                ''',
                'host_name_prefix',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('host-server', REFERENCE_CLASS, 'HostServer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer', 
                [], [], 
                '''                Configure logging host
                ''',
                'host_server',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Ipv4', 
                [], [], 
                '''                Syslog TOS bit for outgoing messages
                ''',
                'ipv4',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Ipv6', 
                [], [], 
                '''                Syslog traffic class bit for outgoing messages
                ''',
                'ipv6',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('local-log-file-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Set size of the local log file
                ''',
                'local_log_file_size',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('logging-facilities', REFERENCE_CLASS, 'LoggingFacilities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.LoggingFacilities', 
                [], [], 
                '''                Modify message logging facilities
                ''',
                'logging_facilities',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('monitor-logging', REFERENCE_CLASS, 'MonitorLogging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.MonitorLogging', 
                [], [], 
                '''                Set monitor logging
                ''',
                'monitor_logging',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('source-interface-table', REFERENCE_CLASS, 'SourceInterfaceTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.SourceInterfaceTable', 
                [], [], 
                '''                Configure source interface
                ''',
                'source_interface_table',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('suppress-duplicates', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Suppress consecutive duplicate messages
                ''',
                'suppress_duplicates',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('suppression', REFERENCE_CLASS, 'Suppression' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Suppression', 
                [], [], 
                '''                Configure properties of the syslog/alarm
                suppression
                ''',
                'suppression',
                'Cisco-IOS-XR-infra-correlator-cfg', False),
            _MetaInfoClassMember('trap-logging', REFERENCE_CLASS, 'TrapLogging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.TrapLogging', 
                [], [], 
                '''                Set trap logging
                ''',
                'trap_logging',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'syslog',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
}
_meta_table['SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue']['meta_info'].parent =_meta_table['SyslogService.Timestamps.Log.LogDatetime']['meta_info']
_meta_table['SyslogService.Timestamps.Log.LogDatetime']['meta_info'].parent =_meta_table['SyslogService.Timestamps.Log']['meta_info']
_meta_table['SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue']['meta_info'].parent =_meta_table['SyslogService.Timestamps.Debug.DebugDatetime']['meta_info']
_meta_table['SyslogService.Timestamps.Debug.DebugDatetime']['meta_info'].parent =_meta_table['SyslogService.Timestamps.Debug']['meta_info']
_meta_table['SyslogService.Timestamps.Log']['meta_info'].parent =_meta_table['SyslogService.Timestamps']['meta_info']
_meta_table['SyslogService.Timestamps.Debug']['meta_info'].parent =_meta_table['SyslogService.Timestamps']['meta_info']
_meta_table['SyslogService.Timestamps']['meta_info'].parent =_meta_table['SyslogService']['meta_info']
_meta_table['Syslog.MonitorLogging.MonitorDiscriminator']['meta_info'].parent =_meta_table['Syslog.MonitorLogging']['meta_info']
_meta_table['Syslog.BufferedLogging.BufferedDiscriminator']['meta_info'].parent =_meta_table['Syslog.BufferedLogging']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityPort']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6Discriminator']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameDiscriminator']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityPort']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4Discriminator']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs']['meta_info']
_meta_table['Syslog.HostServer.Vrfs']['meta_info'].parent =_meta_table['Syslog.HostServer']['meta_info']
_meta_table['Syslog.ConsoleLogging.ConsoleDiscriminator']['meta_info'].parent =_meta_table['Syslog.ConsoleLogging']['meta_info']
_meta_table['Syslog.Files.File.FileSpecification']['meta_info'].parent =_meta_table['Syslog.Files.File']['meta_info']
_meta_table['Syslog.Files.File.FileLogAttributes']['meta_info'].parent =_meta_table['Syslog.Files.File']['meta_info']
_meta_table['Syslog.Files.File.FileLogDiscriminator']['meta_info'].parent =_meta_table['Syslog.Files.File']['meta_info']
_meta_table['Syslog.Files.File']['meta_info'].parent =_meta_table['Syslog.Files']['meta_info']
_meta_table['Syslog.Ipv4.Dscp']['meta_info'].parent =_meta_table['Syslog.Ipv4']['meta_info']
_meta_table['Syslog.Ipv4.Tos']['meta_info'].parent =_meta_table['Syslog.Ipv4']['meta_info']
_meta_table['Syslog.Ipv4.Precedence']['meta_info'].parent =_meta_table['Syslog.Ipv4']['meta_info']
_meta_table['Syslog.Ipv6.Dscp']['meta_info'].parent =_meta_table['Syslog.Ipv6']['meta_info']
_meta_table['Syslog.Ipv6.TrafficClass']['meta_info'].parent =_meta_table['Syslog.Ipv6']['meta_info']
_meta_table['Syslog.Ipv6.Precedence']['meta_info'].parent =_meta_table['Syslog.Ipv6']['meta_info']
_meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf']['meta_info'].parent =_meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs']['meta_info']
_meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs']['meta_info'].parent =_meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue']['meta_info']
_meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue']['meta_info'].parent =_meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues']['meta_info']
_meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues']['meta_info'].parent =_meta_table['Syslog.SourceInterfaceTable']['meta_info']
_meta_table['Syslog.AlarmLogger.AlarmFilterStrings.AlarmFilterString']['meta_info'].parent =_meta_table['Syslog.AlarmLogger.AlarmFilterStrings']['meta_info']
_meta_table['Syslog.AlarmLogger.AlarmFilterStrings']['meta_info'].parent =_meta_table['Syslog.AlarmLogger']['meta_info']
_meta_table['Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause']['meta_info'].parent =_meta_table['Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses']['meta_info']
_meta_table['Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses']['meta_info'].parent =_meta_table['Syslog.Correlator.Rules.Rule.NonStateful']['meta_info']
_meta_table['Syslog.Correlator.Rules.Rule.NonStateful.RootCause']['meta_info'].parent =_meta_table['Syslog.Correlator.Rules.Rule.NonStateful']['meta_info']
_meta_table['Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses.NonRootCause']['meta_info'].parent =_meta_table['Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses']['meta_info']
_meta_table['Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses']['meta_info'].parent =_meta_table['Syslog.Correlator.Rules.Rule.Stateful']['meta_info']
_meta_table['Syslog.Correlator.Rules.Rule.Stateful.RootCause']['meta_info'].parent =_meta_table['Syslog.Correlator.Rules.Rule.Stateful']['meta_info']
_meta_table['Syslog.Correlator.Rules.Rule.ApplyTo.Contexts']['meta_info'].parent =_meta_table['Syslog.Correlator.Rules.Rule.ApplyTo']['meta_info']
_meta_table['Syslog.Correlator.Rules.Rule.ApplyTo.Locations']['meta_info'].parent =_meta_table['Syslog.Correlator.Rules.Rule.ApplyTo']['meta_info']
_meta_table['Syslog.Correlator.Rules.Rule.AppliedTo.Contexts.Context']['meta_info'].parent =_meta_table['Syslog.Correlator.Rules.Rule.AppliedTo.Contexts']['meta_info']
_meta_table['Syslog.Correlator.Rules.Rule.AppliedTo.Locations.Location']['meta_info'].parent =_meta_table['Syslog.Correlator.Rules.Rule.AppliedTo.Locations']['meta_info']
_meta_table['Syslog.Correlator.Rules.Rule.AppliedTo.Contexts']['meta_info'].parent =_meta_table['Syslog.Correlator.Rules.Rule.AppliedTo']['meta_info']
_meta_table['Syslog.Correlator.Rules.Rule.AppliedTo.Locations']['meta_info'].parent =_meta_table['Syslog.Correlator.Rules.Rule.AppliedTo']['meta_info']
_meta_table['Syslog.Correlator.Rules.Rule.Definition']['meta_info'].parent =_meta_table['Syslog.Correlator.Rules.Rule']['meta_info']
_meta_table['Syslog.Correlator.Rules.Rule.NonStateful']['meta_info'].parent =_meta_table['Syslog.Correlator.Rules.Rule']['meta_info']
_meta_table['Syslog.Correlator.Rules.Rule.Stateful']['meta_info'].parent =_meta_table['Syslog.Correlator.Rules.Rule']['meta_info']
_meta_table['Syslog.Correlator.Rules.Rule.ApplyTo']['meta_info'].parent =_meta_table['Syslog.Correlator.Rules.Rule']['meta_info']
_meta_table['Syslog.Correlator.Rules.Rule.AppliedTo']['meta_info'].parent =_meta_table['Syslog.Correlator.Rules.Rule']['meta_info']
_meta_table['Syslog.Correlator.Rules.Rule']['meta_info'].parent =_meta_table['Syslog.Correlator.Rules']['meta_info']
_meta_table['Syslog.Correlator.RuleSets.RuleSet.Rulenames.Rulename']['meta_info'].parent =_meta_table['Syslog.Correlator.RuleSets.RuleSet.Rulenames']['meta_info']
_meta_table['Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts.Context']['meta_info'].parent =_meta_table['Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts']['meta_info']
_meta_table['Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations.Location']['meta_info'].parent =_meta_table['Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations']['meta_info']
_meta_table['Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts']['meta_info'].parent =_meta_table['Syslog.Correlator.RuleSets.RuleSet.AppliedTo']['meta_info']
_meta_table['Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations']['meta_info'].parent =_meta_table['Syslog.Correlator.RuleSets.RuleSet.AppliedTo']['meta_info']
_meta_table['Syslog.Correlator.RuleSets.RuleSet.Rulenames']['meta_info'].parent =_meta_table['Syslog.Correlator.RuleSets.RuleSet']['meta_info']
_meta_table['Syslog.Correlator.RuleSets.RuleSet.AppliedTo']['meta_info'].parent =_meta_table['Syslog.Correlator.RuleSets.RuleSet']['meta_info']
_meta_table['Syslog.Correlator.RuleSets.RuleSet']['meta_info'].parent =_meta_table['Syslog.Correlator.RuleSets']['meta_info']
_meta_table['Syslog.Correlator.Rules']['meta_info'].parent =_meta_table['Syslog.Correlator']['meta_info']
_meta_table['Syslog.Correlator.RuleSets']['meta_info'].parent =_meta_table['Syslog.Correlator']['meta_info']
_meta_table['Syslog.Suppression.Rules.Rule.AppliedTo.Sources.Source']['meta_info'].parent =_meta_table['Syslog.Suppression.Rules.Rule.AppliedTo.Sources']['meta_info']
_meta_table['Syslog.Suppression.Rules.Rule.AppliedTo.Sources']['meta_info'].parent =_meta_table['Syslog.Suppression.Rules.Rule.AppliedTo']['meta_info']
_meta_table['Syslog.Suppression.Rules.Rule.AlarmCauses.AlarmCause']['meta_info'].parent =_meta_table['Syslog.Suppression.Rules.Rule.AlarmCauses']['meta_info']
_meta_table['Syslog.Suppression.Rules.Rule.AppliedTo']['meta_info'].parent =_meta_table['Syslog.Suppression.Rules.Rule']['meta_info']
_meta_table['Syslog.Suppression.Rules.Rule.AlarmCauses']['meta_info'].parent =_meta_table['Syslog.Suppression.Rules.Rule']['meta_info']
_meta_table['Syslog.Suppression.Rules.Rule']['meta_info'].parent =_meta_table['Syslog.Suppression.Rules']['meta_info']
_meta_table['Syslog.Suppression.Rules']['meta_info'].parent =_meta_table['Syslog.Suppression']['meta_info']
_meta_table['Syslog.MonitorLogging']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.HistoryLogging']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.LoggingFacilities']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.TrapLogging']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.BufferedLogging']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.HostServer']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.ConsoleLogging']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.Files']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.Ipv4']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.Archive']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.Ipv6']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.SourceInterfaceTable']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.AlarmLogger']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.Correlator']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.Suppression']['meta_info'].parent =_meta_table['Syslog']['meta_info']
