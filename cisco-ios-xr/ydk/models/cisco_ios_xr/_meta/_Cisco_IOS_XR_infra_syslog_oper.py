


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SystemMessageSeverityEnum' : _MetaInfoEnum('SystemMessageSeverityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper',
        {
            'message-severity-unknown':'message_severity_unknown',
            'message-severity-emergency':'message_severity_emergency',
            'message-severity-alert':'message_severity_alert',
            'message-severity-critical':'message_severity_critical',
            'message-severity-error':'message_severity_error',
            'message-severity-warning':'message_severity_warning',
            'message-severity-notice':'message_severity_notice',
            'message-severity-informational':'message_severity_informational',
            'message-severity-debug':'message_severity_debug',
        }, 'Cisco-IOS-XR-infra-syslog-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper']),
    'Logging.History' : {
        'meta_info' : _MetaInfoClass('Logging.History',
            False, 
            [
            _MetaInfoClassMember('message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Syslog Message
                ''',
                'message',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('properties', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Syslog Properties
                ''',
                'properties',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            ],
            'Cisco-IOS-XR-infra-syslog-oper',
            'history',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper'
        ),
    },
    'Logging' : {
        'meta_info' : _MetaInfoClass('Logging',
            False, 
            [
            _MetaInfoClassMember('history', REFERENCE_CLASS, 'History' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'Logging.History', 
                [], [], 
                '''                Syslog Info 
                ''',
                'history',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            ],
            'Cisco-IOS-XR-infra-syslog-oper',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper'
        ),
    },
    'Syslog.LoggingFiles.FileLogDetail' : {
        'meta_info' : _MetaInfoClass('Syslog.LoggingFiles.FileLogDetail',
            False, 
            [
            _MetaInfoClassMember('file-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                File name for logging messages
                ''',
                'file_name',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('file-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                File path for logging messages
                ''',
                'file_path',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            ],
            'Cisco-IOS-XR-infra-syslog-oper',
            'file-log-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper'
        ),
    },
    'Syslog.LoggingFiles' : {
        'meta_info' : _MetaInfoClass('Syslog.LoggingFiles',
            False, 
            [
            _MetaInfoClassMember('file-log-detail', REFERENCE_LIST, 'FileLogDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'Syslog.LoggingFiles.FileLogDetail', 
                [], [], 
                '''                Logging Files
                ''',
                'file_log_detail',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            ],
            'Cisco-IOS-XR-infra-syslog-oper',
            'logging-files',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper'
        ),
    },
    'Syslog.AnRemoteServers.AnRemoteLogServer' : {
        'meta_info' : _MetaInfoClass('Syslog.AnRemoteServers.AnRemoteLogServer',
            False, 
            [
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP Address
                ''',
                'ip_address',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('rh-discriminator', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote-Host Discriminator
                ''',
                'rh_discriminator',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('vrf-severity', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Severity
                ''',
                'vrf_severity',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            ],
            'Cisco-IOS-XR-infra-syslog-oper',
            'an-remote-log-server',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper'
        ),
    },
    'Syslog.AnRemoteServers' : {
        'meta_info' : _MetaInfoClass('Syslog.AnRemoteServers',
            False, 
            [
            _MetaInfoClassMember('an-remote-log-server', REFERENCE_LIST, 'AnRemoteLogServer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'Syslog.AnRemoteServers.AnRemoteLogServer', 
                [], [], 
                '''                AN Remote Log Servers
                ''',
                'an_remote_log_server',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            ],
            'Cisco-IOS-XR-infra-syslog-oper',
            'an-remote-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper'
        ),
    },
    'Syslog.Messages.Message' : {
        'meta_info' : _MetaInfoClass('Syslog.Messages.Message',
            False, 
            [
            _MetaInfoClassMember('message-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Message ID of the system message
                ''',
                'message_id',
                'Cisco-IOS-XR-infra-syslog-oper', True),
            _MetaInfoClassMember('card-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Message card location: 'RP', 'DRP', 'LC', 'SC',
                'SP' or 'UNK' 
                ''',
                'card_type',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('category', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Message category
                ''',
                'category',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Message group
                ''',
                'group',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('message-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Message name
                ''',
                'message_name',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Message source location
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Process name
                ''',
                'process_name',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'SystemMessageSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'SystemMessageSeverityEnum', 
                [], [], 
                '''                Message severity
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('text', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Additional message text
                ''',
                'text',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('time-of-day', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Time of day of event in DDD MMM DD  YYYY HH:MM
                :SS format, e.g Wed Apr 01 2009  15:50:26
                ''',
                'time_of_day',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time in milliseconds since 00:00:00 UTC, January
                11970 of when message was generated
                ''',
                'time_stamp',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('time-zone', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Time Zone in UTC+/-HH:MM format,  e.g UTC+5:30,
                UTC-6
                ''',
                'time_zone',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            ],
            'Cisco-IOS-XR-infra-syslog-oper',
            'message',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper'
        ),
    },
    'Syslog.Messages' : {
        'meta_info' : _MetaInfoClass('Syslog.Messages',
            False, 
            [
            _MetaInfoClassMember('message', REFERENCE_LIST, 'Message' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'Syslog.Messages.Message', 
                [], [], 
                '''                A system message
                ''',
                'message',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            ],
            'Cisco-IOS-XR-infra-syslog-oper',
            'messages',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper'
        ),
    },
    'Syslog.LoggingStatistics.LoggingStats' : {
        'meta_info' : _MetaInfoClass('Syslog.LoggingStatistics.LoggingStats',
            False, 
            [
            _MetaInfoClassMember('drop-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of messages dropped
                ''',
                'drop_count',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('flush-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of messages flushed
                ''',
                'flush_count',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('is-log-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is log enabled
                ''',
                'is_log_enabled',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('overrun-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of messages overrun
                ''',
                'overrun_count',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            ],
            'Cisco-IOS-XR-infra-syslog-oper',
            'logging-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper'
        ),
    },
    'Syslog.LoggingStatistics.ConsoleLoggingStats' : {
        'meta_info' : _MetaInfoClass('Syslog.LoggingStatistics.ConsoleLoggingStats',
            False, 
            [
            _MetaInfoClassMember('buffer-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Buffer size in bytes if logging buffer isenabled
                ''',
                'buffer_size',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('is-log-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is log enabled
                ''',
                'is_log_enabled',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('message-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message count
                ''',
                'message_count',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'SystemMessageSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'SystemMessageSeverityEnum', 
                [], [], 
                '''                Configured severity
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            ],
            'Cisco-IOS-XR-infra-syslog-oper',
            'console-logging-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper'
        ),
    },
    'Syslog.LoggingStatistics.MonitorLoggingStats' : {
        'meta_info' : _MetaInfoClass('Syslog.LoggingStatistics.MonitorLoggingStats',
            False, 
            [
            _MetaInfoClassMember('buffer-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Buffer size in bytes if logging buffer isenabled
                ''',
                'buffer_size',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('is-log-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is log enabled
                ''',
                'is_log_enabled',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('message-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message count
                ''',
                'message_count',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'SystemMessageSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'SystemMessageSeverityEnum', 
                [], [], 
                '''                Configured severity
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            ],
            'Cisco-IOS-XR-infra-syslog-oper',
            'monitor-logging-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper'
        ),
    },
    'Syslog.LoggingStatistics.TrapLoggingStats' : {
        'meta_info' : _MetaInfoClass('Syslog.LoggingStatistics.TrapLoggingStats',
            False, 
            [
            _MetaInfoClassMember('buffer-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Buffer size in bytes if logging buffer isenabled
                ''',
                'buffer_size',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('is-log-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is log enabled
                ''',
                'is_log_enabled',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('message-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message count
                ''',
                'message_count',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'SystemMessageSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'SystemMessageSeverityEnum', 
                [], [], 
                '''                Configured severity
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            ],
            'Cisco-IOS-XR-infra-syslog-oper',
            'trap-logging-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper'
        ),
    },
    'Syslog.LoggingStatistics.BufferLoggingStats' : {
        'meta_info' : _MetaInfoClass('Syslog.LoggingStatistics.BufferLoggingStats',
            False, 
            [
            _MetaInfoClassMember('buffer-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Buffer size in bytes if logging buffer isenabled
                ''',
                'buffer_size',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('is-log-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is log enabled
                ''',
                'is_log_enabled',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('message-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message count
                ''',
                'message_count',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'SystemMessageSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'SystemMessageSeverityEnum', 
                [], [], 
                '''                Configured severity
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            ],
            'Cisco-IOS-XR-infra-syslog-oper',
            'buffer-logging-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper'
        ),
    },
    'Syslog.LoggingStatistics.RemoteLoggingStat' : {
        'meta_info' : _MetaInfoClass('Syslog.LoggingStatistics.RemoteLoggingStat',
            False, 
            [
            _MetaInfoClassMember('message-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message count
                ''',
                'message_count',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('remote-host-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote hostname
                ''',
                'remote_host_name',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            ],
            'Cisco-IOS-XR-infra-syslog-oper',
            'remote-logging-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper'
        ),
    },
    'Syslog.LoggingStatistics.TlsRemoteLoggingStat' : {
        'meta_info' : _MetaInfoClass('Syslog.LoggingStatistics.TlsRemoteLoggingStat',
            False, 
            [
            _MetaInfoClassMember('message-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message count
                ''',
                'message_count',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('remote-host-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TLS Remote hostname
                ''',
                'remote_host_name',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            ],
            'Cisco-IOS-XR-infra-syslog-oper',
            'tls-remote-logging-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper'
        ),
    },
    'Syslog.LoggingStatistics.FileLoggingStat' : {
        'meta_info' : _MetaInfoClass('Syslog.LoggingStatistics.FileLoggingStat',
            False, 
            [
            _MetaInfoClassMember('file-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                File name for logging messages
                ''',
                'file_name',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('message-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message count
                ''',
                'message_count',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            ],
            'Cisco-IOS-XR-infra-syslog-oper',
            'file-logging-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper'
        ),
    },
    'Syslog.LoggingStatistics' : {
        'meta_info' : _MetaInfoClass('Syslog.LoggingStatistics',
            False, 
            [
            _MetaInfoClassMember('buffer-logging-stats', REFERENCE_CLASS, 'BufferLoggingStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'Syslog.LoggingStatistics.BufferLoggingStats', 
                [], [], 
                '''                Buffer logging statistics
                ''',
                'buffer_logging_stats',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('console-logging-stats', REFERENCE_CLASS, 'ConsoleLoggingStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'Syslog.LoggingStatistics.ConsoleLoggingStats', 
                [], [], 
                '''                Console logging statistics
                ''',
                'console_logging_stats',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('file-logging-stat', REFERENCE_LIST, 'FileLoggingStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'Syslog.LoggingStatistics.FileLoggingStat', 
                [], [], 
                '''                File logging statistics
                ''',
                'file_logging_stat',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('logging-stats', REFERENCE_CLASS, 'LoggingStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'Syslog.LoggingStatistics.LoggingStats', 
                [], [], 
                '''                Logging statistics
                ''',
                'logging_stats',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('monitor-logging-stats', REFERENCE_CLASS, 'MonitorLoggingStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'Syslog.LoggingStatistics.MonitorLoggingStats', 
                [], [], 
                '''                Monitor loggingstatistics
                ''',
                'monitor_logging_stats',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('remote-logging-stat', REFERENCE_LIST, 'RemoteLoggingStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'Syslog.LoggingStatistics.RemoteLoggingStat', 
                [], [], 
                '''                Remote logging statistics
                ''',
                'remote_logging_stat',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('tls-remote-logging-stat', REFERENCE_LIST, 'TlsRemoteLoggingStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'Syslog.LoggingStatistics.TlsRemoteLoggingStat', 
                [], [], 
                '''                TLS Remote logging statistics
                ''',
                'tls_remote_logging_stat',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('trap-logging-stats', REFERENCE_CLASS, 'TrapLoggingStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'Syslog.LoggingStatistics.TrapLoggingStats', 
                [], [], 
                '''                Trap logging statistics
                ''',
                'trap_logging_stats',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            ],
            'Cisco-IOS-XR-infra-syslog-oper',
            'logging-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper'
        ),
    },
    'Syslog' : {
        'meta_info' : _MetaInfoClass('Syslog',
            False, 
            [
            _MetaInfoClassMember('an-remote-servers', REFERENCE_CLASS, 'AnRemoteServers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'Syslog.AnRemoteServers', 
                [], [], 
                '''                Logging AN remote servers information
                ''',
                'an_remote_servers',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('logging-files', REFERENCE_CLASS, 'LoggingFiles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'Syslog.LoggingFiles', 
                [], [], 
                '''                Logging Files information
                ''',
                'logging_files',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('logging-statistics', REFERENCE_CLASS, 'LoggingStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'Syslog.LoggingStatistics', 
                [], [], 
                '''                Logging statistics information
                ''',
                'logging_statistics',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            _MetaInfoClassMember('messages', REFERENCE_CLASS, 'Messages' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'Syslog.Messages', 
                [], [], 
                '''                Message table information
                ''',
                'messages',
                'Cisco-IOS-XR-infra-syslog-oper', False),
            ],
            'Cisco-IOS-XR-infra-syslog-oper',
            'syslog',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper'
        ),
    },
}
_meta_table['Logging.History']['meta_info'].parent =_meta_table['Logging']['meta_info']
_meta_table['Syslog.LoggingFiles.FileLogDetail']['meta_info'].parent =_meta_table['Syslog.LoggingFiles']['meta_info']
_meta_table['Syslog.AnRemoteServers.AnRemoteLogServer']['meta_info'].parent =_meta_table['Syslog.AnRemoteServers']['meta_info']
_meta_table['Syslog.Messages.Message']['meta_info'].parent =_meta_table['Syslog.Messages']['meta_info']
_meta_table['Syslog.LoggingStatistics.LoggingStats']['meta_info'].parent =_meta_table['Syslog.LoggingStatistics']['meta_info']
_meta_table['Syslog.LoggingStatistics.ConsoleLoggingStats']['meta_info'].parent =_meta_table['Syslog.LoggingStatistics']['meta_info']
_meta_table['Syslog.LoggingStatistics.MonitorLoggingStats']['meta_info'].parent =_meta_table['Syslog.LoggingStatistics']['meta_info']
_meta_table['Syslog.LoggingStatistics.TrapLoggingStats']['meta_info'].parent =_meta_table['Syslog.LoggingStatistics']['meta_info']
_meta_table['Syslog.LoggingStatistics.BufferLoggingStats']['meta_info'].parent =_meta_table['Syslog.LoggingStatistics']['meta_info']
_meta_table['Syslog.LoggingStatistics.RemoteLoggingStat']['meta_info'].parent =_meta_table['Syslog.LoggingStatistics']['meta_info']
_meta_table['Syslog.LoggingStatistics.TlsRemoteLoggingStat']['meta_info'].parent =_meta_table['Syslog.LoggingStatistics']['meta_info']
_meta_table['Syslog.LoggingStatistics.FileLoggingStat']['meta_info'].parent =_meta_table['Syslog.LoggingStatistics']['meta_info']
_meta_table['Syslog.LoggingFiles']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.AnRemoteServers']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.Messages']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.LoggingStatistics']['meta_info'].parent =_meta_table['Syslog']['meta_info']
