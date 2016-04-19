


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'LogSeverityEnum' : _MetaInfoEnum('LogSeverityEnum', 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'emergency':'EMERGENCY',
            'alert':'ALERT',
            'critical':'CRITICAL',
            'error':'ERROR',
            'warning':'WARNING',
            'notice':'NOTICE',
            'informational':'INFORMATIONAL',
            'debug':'DEBUG',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'FacilityEnum' : _MetaInfoEnum('FacilityEnum', 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'kern':'KERN',
            'user':'USER',
            'mail':'MAIL',
            'daemon':'DAEMON',
            'auth':'AUTH',
            'syslog':'SYSLOG',
            'lpr':'LPR',
            'news':'NEWS',
            'uucp':'UUCP',
            'cron':'CRON',
            'authpriv':'AUTHPRIV',
            'ftp':'FTP',
            'local0':'LOCAL0',
            'local1':'LOCAL1',
            'local2':'LOCAL2',
            'local3':'LOCAL3',
            'local4':'LOCAL4',
            'local5':'LOCAL5',
            'local6':'LOCAL6',
            'local7':'LOCAL7',
            'sys9':'SYS9',
            'sys10':'SYS10',
            'sys11':'SYS11',
            'sys12':'SYS12',
            'sys13':'SYS13',
            'sys14':'SYS14',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'LogCollectFrequencyEnum' : _MetaInfoEnum('LogCollectFrequencyEnum', 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'weekly':'WEEKLY',
            'daily':'DAILY',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'LoggingPrecedenceValueEnum' : _MetaInfoEnum('LoggingPrecedenceValueEnum', 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'routine':'ROUTINE',
            'priority':'PRIORITY',
            'immediate':'IMMEDIATE',
            'flash':'FLASH',
            'flash-override':'FLASH_OVERRIDE',
            'critical':'CRITICAL',
            'internet':'INTERNET',
            'network':'NETWORK',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'LoggingTosEnum' : _MetaInfoEnum('LoggingTosEnum', 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'precedence':'PRECEDENCE',
            'dscp':'DSCP',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'LoggingLevelsEnum' : _MetaInfoEnum('LoggingLevelsEnum', 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'emergency':'EMERGENCY',
            'alert':'ALERT',
            'critical':'CRITICAL',
            'error':'ERROR',
            'warning':'WARNING',
            'notice':'NOTICE',
            'info':'INFO',
            'debug':'DEBUG',
            'disable':'DISABLE',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'LoggingPrecedenceEnum' : _MetaInfoEnum('LoggingPrecedenceEnum', 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'precedence':'PRECEDENCE',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'LoggingDscpValueEnum' : _MetaInfoEnum('LoggingDscpValueEnum', 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'default':'DEFAULT',
            'af11':'AF11',
            'af12':'AF12',
            'af13':'AF13',
            'af21':'AF21',
            'af22':'AF22',
            'af23':'AF23',
            'af31':'AF31',
            'af32':'AF32',
            'af33':'AF33',
            'af41':'AF41',
            'af42':'AF42',
            'af43':'AF43',
            'ef':'EF',
            'cs1':'CS1',
            'cs2':'CS2',
            'cs3':'CS3',
            'cs4':'CS4',
            'cs5':'CS5',
            'cs6':'CS6',
            'cs7':'CS7',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'LogMessageSeverityEnum' : _MetaInfoEnum('LogMessageSeverityEnum', 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'emergency':'EMERGENCY',
            'alert':'ALERT',
            'critical':'CRITICAL',
            'error':'ERROR',
            'warning':'WARNING',
            'notice':'NOTICE',
            'informational':'INFORMATIONAL',
            'debug':'DEBUG',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'TimeInfoEnum' : _MetaInfoEnum('TimeInfoEnum', 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'disable':'DISABLE',
            'enable':'ENABLE',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'LoggingDscpEnum' : _MetaInfoEnum('LoggingDscpEnum', 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg',
        {
            'dscp':'DSCP',
        }, 'Cisco-IOS-XR-infra-syslog-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg']),
    'Syslog.AlarmLogger' : {
        'meta_info' : _MetaInfoClass('Syslog.AlarmLogger',
            False, 
            [
            _MetaInfoClassMember('buffer-size', ATTRIBUTE, 'int' , None, None, 
                [(1024, 1024000)], [], 
                '''                Set size of the local event buffer
                ''',
                'buffer_size',
                'Cisco-IOS-XR-infra-alarm-logger-cfg', False),
            _MetaInfoClassMember('severity-level', REFERENCE_ENUM_CLASS, 'AlarmLoggerSeverityLevelEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_alarm_logger_datatypes', 'AlarmLoggerSeverityLevelEnum', 
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
                [(10, 100)], [], 
                '''                Configure threshold (%) for capacity alarm
                ''',
                'threshold',
                'Cisco-IOS-XR-infra-alarm-logger-cfg', False),
            ],
            'Cisco-IOS-XR-infra-alarm-logger-cfg',
            'alarm-logger',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-alarm-logger-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
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
                [(1, 2047)], [], 
                '''                The maximum file size for a single log file.
                ''',
                'file_size',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('frequency', REFERENCE_ENUM_CLASS, 'LogCollectFrequencyEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LogCollectFrequencyEnum', 
                [], [], 
                '''                The collection interval for logs
                ''',
                'frequency',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [(1, 256)], [], 
                '''                The maximum number of weeks of log to maintain
                ''',
                'length',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'LogMessageSeverityEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LogMessageSeverityEnum', 
                [], [], 
                '''                The minimum severity of log messages to archive
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [(1, 2047)], [], 
                '''                The total size of the archive
                ''',
                'size',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 99)], [], 
                '''                The size threshold at which a syslog is
                generated
                ''',
                'threshold',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'archive',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
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
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.BufferedLogging' : {
        'meta_info' : _MetaInfoClass('Syslog.BufferedLogging',
            False, 
            [
            _MetaInfoClassMember('buffer-size', ATTRIBUTE, 'int' , None, None, 
                [(4096, 4294967295)], [], 
                '''                Logging buffered size
                ''',
                'buffer_size',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('buffered-discriminator', REFERENCE_CLASS, 'BufferedDiscriminator' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.BufferedLogging.BufferedDiscriminator', 
                [], [], 
                '''                Set buffered logging discriminators
                ''',
                'buffered_discriminator',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('logging-level', REFERENCE_ENUM_CLASS, 'LoggingLevelsEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingLevelsEnum', 
                [], [], 
                '''                Logging level for Buffered logging
                ''',
                'logging_level',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'buffered-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
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
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.ConsoleLogging' : {
        'meta_info' : _MetaInfoClass('Syslog.ConsoleLogging',
            False, 
            [
            _MetaInfoClassMember('console-discriminator', REFERENCE_CLASS, 'ConsoleDiscriminator' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.ConsoleLogging.ConsoleDiscriminator', 
                [], [], 
                '''                Set console logging discriminators
                ''',
                'console_discriminator',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('logging-level', REFERENCE_ENUM_CLASS, 'LoggingLevelsEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingLevelsEnum', 
                [], [], 
                '''                Console logging level
                ''',
                'logging_level',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'console-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
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
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Files.File.FileSpecification' : {
        'meta_info' : _MetaInfoClass('Syslog.Files.File.FileSpecification',
            False, 
            [
            _MetaInfoClassMember('max-file-size', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
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
                [(-2147483648, 2147483647)], [], 
                '''                Severity of messages
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'file-specification',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Files.File' : {
        'meta_info' : _MetaInfoClass('Syslog.Files.File',
            False, 
            [
            _MetaInfoClassMember('file-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the file
                ''',
                'file_name',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            _MetaInfoClassMember('file-log-discriminator', REFERENCE_CLASS, 'FileLogDiscriminator' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Files.File.FileLogDiscriminator', 
                [], [], 
                '''                Set File logging discriminators
                ''',
                'file_log_discriminator',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('file-specification', REFERENCE_CLASS, 'FileSpecification' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Files.File.FileSpecification', 
                [], [], 
                '''                Specifications of the logging file destination
                ''',
                'file_specification',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'file',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Files' : {
        'meta_info' : _MetaInfoClass('Syslog.Files',
            False, 
            [
            _MetaInfoClassMember('file', REFERENCE_LIST, 'File' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Files.File', 
                [], [], 
                '''                Specify File Name
                ''',
                'file',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'files',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HistoryLogging' : {
        'meta_info' : _MetaInfoClass('Syslog.HistoryLogging',
            False, 
            [
            _MetaInfoClassMember('history-size', ATTRIBUTE, 'int' , None, None, 
                [(1, 500)], [], 
                '''                Logging history size
                ''',
                'history_size',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('logging-level', REFERENCE_ENUM_CLASS, 'LoggingLevelsEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingLevelsEnum', 
                [], [], 
                '''                History logging level
                ''',
                'logging_level',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'history-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
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
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity',
            False, 
            [
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'LogSeverityEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LogSeverityEnum', 
                [], [], 
                '''                Severity for the logging host
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'host-name-severity',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities',
            False, 
            [
            _MetaInfoClassMember('host-name-severity', REFERENCE_LIST, 'HostNameSeverity' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity', 
                [], [], 
                '''                Severity for the logging host
                ''',
                'host_name_severity',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'host-name-severities',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort',
            False, 
            [
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Port for the logging host
                ''',
                'port',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('severity', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Severity for the logging host
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'host-severity-port',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
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
            _MetaInfoClassMember('host-name-discriminator', REFERENCE_CLASS, 'HostNameDiscriminator' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameDiscriminator', 
                [], [], 
                '''                Set Hostname logging discriminators
                ''',
                'host_name_discriminator',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('host-name-severities', REFERENCE_CLASS, 'HostNameSeverities' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities', 
                [], [], 
                '''                Severity container of the logging host
                ''',
                'host_name_severities',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('host-severity-port', REFERENCE_CLASS, 'HostSeverityPort' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort', 
                [], [], 
                '''                Severity/Port for the logging host
                ''',
                'host_severity_port',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'host',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Hosts' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Hosts',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Hosts.Host', 
                [], [], 
                '''                Name of the logging host
                ''',
                'host',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
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
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel',
            False, 
            [
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'LogSeverityEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LogSeverityEnum', 
                [], [], 
                '''                Severity for the logging host
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv4-severity-level',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels',
            False, 
            [
            _MetaInfoClassMember('ipv4-severity-level', REFERENCE_LIST, 'Ipv4SeverityLevel' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel', 
                [], [], 
                '''                Severity for the logging host
                ''',
                'ipv4_severity_level',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv4-severity-levels',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityPort' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityPort',
            False, 
            [
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Port for the logging host
                ''',
                'port',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('severity', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Severity for the logging host
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv4-severity-port',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address of the logging host
                ''',
                'address',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            _MetaInfoClassMember('ipv4-discriminator', REFERENCE_CLASS, 'Ipv4Discriminator' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4Discriminator', 
                [], [], 
                '''                Set IPv4 logging discriminators
                ''',
                'ipv4_discriminator',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('ipv4-severity-levels', REFERENCE_CLASS, 'Ipv4SeverityLevels' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels', 
                [], [], 
                '''                Severity container of the logging host
                ''',
                'ipv4_severity_levels',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('ipv4-severity-port', REFERENCE_CLASS, 'Ipv4SeverityPort' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityPort', 
                [], [], 
                '''                Severity/Port for the logging host
                ''',
                'ipv4_severity_port',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv4S' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv4S',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_LIST, 'Ipv4' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4', 
                [], [], 
                '''                IPv4 address of the logging host
                ''',
                'ipv4',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv4s',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
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
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel',
            False, 
            [
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'LogSeverityEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LogSeverityEnum', 
                [], [], 
                '''                Severity for the logging host
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv6-severity-level',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels',
            False, 
            [
            _MetaInfoClassMember('ipv6-severity-level', REFERENCE_LIST, 'Ipv6SeverityLevel' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel', 
                [], [], 
                '''                Severity for the logging host
                ''',
                'ipv6_severity_level',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv6-severity-levels',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityPort' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityPort',
            False, 
            [
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Port for the logging host
                ''',
                'port',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('severity', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Severity for the logging host
                ''',
                'severity',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv6-severity-port',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address of the logging host
                ''',
                'address',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            _MetaInfoClassMember('ipv6-discriminator', REFERENCE_CLASS, 'Ipv6Discriminator' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6Discriminator', 
                [], [], 
                '''                Set IPv6 logging discriminators
                ''',
                'ipv6_discriminator',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('ipv6-severity-levels', REFERENCE_CLASS, 'Ipv6SeverityLevels' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels', 
                [], [], 
                '''                Severity container of the logging host
                ''',
                'ipv6_severity_levels',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('ipv6-severity-port', REFERENCE_CLASS, 'Ipv6SeverityPort' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityPort', 
                [], [], 
                '''                Severity/Port for the logging host
                ''',
                'ipv6_severity_port',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf.Ipv6S' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf.Ipv6S',
            False, 
            [
            _MetaInfoClassMember('ipv6', REFERENCE_LIST, 'Ipv6' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6', 
                [], [], 
                '''                IPv6 address of the logging host
                ''',
                'ipv6',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv6s',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the VRF instance
                ''',
                'vrf_name',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Hosts', 
                [], [], 
                '''                List of the logging host
                ''',
                'hosts',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('ipv4s', REFERENCE_CLASS, 'Ipv4S' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv4S', 
                [], [], 
                '''                List of the IPv4 logging host
                ''',
                'ipv4s',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('ipv6s', REFERENCE_CLASS, 'Ipv6S' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf.Ipv6S', 
                [], [], 
                '''                List of the IPv6 logging host
                ''',
                'ipv6s',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer.Vrfs' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs.Vrf', 
                [], [], 
                '''                VRF specific data
                ''',
                'vrf',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.HostServer' : {
        'meta_info' : _MetaInfoClass('Syslog.HostServer',
            False, 
            [
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer.Vrfs', 
                [], [], 
                '''                VRF table
                ''',
                'vrfs',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'host-server',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Ipv4.Dscp' : {
        'meta_info' : _MetaInfoClass('Syslog.Ipv4.Dscp',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'LoggingDscpEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpEnum', 
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
                    _MetaInfoClassMember('unused', REFERENCE_ENUM_CLASS, 'LoggingPrecedenceValueEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceValueEnum', 
                        [], [], 
                        '''                        Unused
                        ''',
                        'unused',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('unused', ATTRIBUTE, 'int' , None, None, 
                        [(0, 7)], [], 
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
                    _MetaInfoClassMember('value', REFERENCE_ENUM_CLASS, 'LoggingDscpValueEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpValueEnum', 
                        [], [], 
                        '''                        Logging DSCP value
                        ''',
                        'value',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [(0, 63)], [], 
                        '''                        Logging DSCP value
                        ''',
                        'value',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'dscp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Ipv4.Precedence' : {
        'meta_info' : _MetaInfoClass('Syslog.Ipv4.Precedence',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'LoggingPrecedenceEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceEnum', 
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
                    _MetaInfoClassMember('unused', REFERENCE_ENUM_CLASS, 'LoggingDscpValueEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpValueEnum', 
                        [], [], 
                        '''                        Unused
                        ''',
                        'unused',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('unused', ATTRIBUTE, 'int' , None, None, 
                        [(0, 63)], [], 
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
                    _MetaInfoClassMember('value', REFERENCE_ENUM_CLASS, 'LoggingPrecedenceValueEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceValueEnum', 
                        [], [], 
                        '''                        Logging precedence value
                        ''',
                        'value',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [(0, 7)], [], 
                        '''                        Logging precedence value
                        ''',
                        'value',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'precedence',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
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
                    _MetaInfoClassMember('dscp', REFERENCE_ENUM_CLASS, 'LoggingDscpValueEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpValueEnum', 
                        [], [], 
                        '''                        Logging DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                        [(0, 63)], [], 
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
                    _MetaInfoClassMember('precedence', REFERENCE_ENUM_CLASS, 'LoggingPrecedenceValueEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceValueEnum', 
                        [], [], 
                        '''                        Logging precedence value
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('precedence', ATTRIBUTE, 'int' , None, None, 
                        [(0, 7)], [], 
                        '''                        Logging precedence value
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                ]),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'LoggingTosEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingTosEnum', 
                [], [], 
                '''                Logging TOS type DSCP or precedence
                ''',
                'type',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'tos',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Ipv4' : {
        'meta_info' : _MetaInfoClass('Syslog.Ipv4',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_CLASS, 'Dscp' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Ipv4.Dscp', 
                [], [], 
                '''                DSCP value
                ''',
                'dscp',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('precedence', REFERENCE_CLASS, 'Precedence' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Ipv4.Precedence', 
                [], [], 
                '''                Precedence value
                ''',
                'precedence',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('tos', REFERENCE_CLASS, 'Tos' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Ipv4.Tos', 
                [], [], 
                '''                Type of service
                ''',
                'tos',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Ipv6.Dscp' : {
        'meta_info' : _MetaInfoClass('Syslog.Ipv6.Dscp',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'LoggingDscpEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpEnum', 
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
                    _MetaInfoClassMember('unused', REFERENCE_ENUM_CLASS, 'LoggingPrecedenceValueEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceValueEnum', 
                        [], [], 
                        '''                        Unused
                        ''',
                        'unused',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('unused', ATTRIBUTE, 'int' , None, None, 
                        [(0, 7)], [], 
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
                    _MetaInfoClassMember('value', REFERENCE_ENUM_CLASS, 'LoggingDscpValueEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpValueEnum', 
                        [], [], 
                        '''                        Logging DSCP value
                        ''',
                        'value',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [(0, 63)], [], 
                        '''                        Logging DSCP value
                        ''',
                        'value',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'dscp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Ipv6.Precedence' : {
        'meta_info' : _MetaInfoClass('Syslog.Ipv6.Precedence',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'LoggingPrecedenceEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceEnum', 
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
                    _MetaInfoClassMember('unused', REFERENCE_ENUM_CLASS, 'LoggingDscpValueEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpValueEnum', 
                        [], [], 
                        '''                        Unused
                        ''',
                        'unused',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('unused', ATTRIBUTE, 'int' , None, None, 
                        [(0, 63)], [], 
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
                    _MetaInfoClassMember('value', REFERENCE_ENUM_CLASS, 'LoggingPrecedenceValueEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceValueEnum', 
                        [], [], 
                        '''                        Logging precedence value
                        ''',
                        'value',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [(0, 7)], [], 
                        '''                        Logging precedence value
                        ''',
                        'value',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'precedence',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
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
                    _MetaInfoClassMember('dscp', REFERENCE_ENUM_CLASS, 'LoggingDscpValueEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpValueEnum', 
                        [], [], 
                        '''                        Logging DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                        [(0, 63)], [], 
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
                    _MetaInfoClassMember('precedence', REFERENCE_ENUM_CLASS, 'LoggingPrecedenceValueEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceValueEnum', 
                        [], [], 
                        '''                        Logging precedence value
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                    _MetaInfoClassMember('precedence', ATTRIBUTE, 'int' , None, None, 
                        [(0, 7)], [], 
                        '''                        Logging precedence value
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-syslog-cfg', False),
                ]),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'LoggingTosEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingTosEnum', 
                [], [], 
                '''                Logging TOS type DSCP or precedence
                ''',
                'type',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'traffic-class',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.Ipv6' : {
        'meta_info' : _MetaInfoClass('Syslog.Ipv6',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_CLASS, 'Dscp' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Ipv6.Dscp', 
                [], [], 
                '''                DSCP value
                ''',
                'dscp',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('precedence', REFERENCE_CLASS, 'Precedence' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Ipv6.Precedence', 
                [], [], 
                '''                Precedence value
                ''',
                'precedence',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('traffic-class', REFERENCE_CLASS, 'TrafficClass' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Ipv6.TrafficClass', 
                [], [], 
                '''                Type of traffic class
                ''',
                'traffic_class',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.LoggingFacilities' : {
        'meta_info' : _MetaInfoClass('Syslog.LoggingFacilities',
            False, 
            [
            _MetaInfoClassMember('facility-level', REFERENCE_ENUM_CLASS, 'FacilityEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'FacilityEnum', 
                [], [], 
                '''                Facility from which logging is done
                ''',
                'facility_level',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'logging-facilities',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
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
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.MonitorLogging' : {
        'meta_info' : _MetaInfoClass('Syslog.MonitorLogging',
            False, 
            [
            _MetaInfoClassMember('logging-level', REFERENCE_ENUM_CLASS, 'LoggingLevelsEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingLevelsEnum', 
                [], [], 
                '''                Monitor Logging Level
                ''',
                'logging_level',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('monitor-discriminator', REFERENCE_CLASS, 'MonitorDiscriminator' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.MonitorLogging.MonitorDiscriminator', 
                [], [], 
                '''                Set monitor logging discriminators
                ''',
                'monitor_discriminator',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'monitor-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf' : {
        'meta_info' : _MetaInfoClass('Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the VRF instance
                ''',
                'vrf_name',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'source-interface-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs' : {
        'meta_info' : _MetaInfoClass('Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs',
            False, 
            [
            _MetaInfoClassMember('source-interface-vrf', REFERENCE_LIST, 'SourceInterfaceVrf' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf', 
                [], [], 
                '''                Specify VRF for source interface
                ''',
                'source_interface_vrf',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'source-interface-vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue' : {
        'meta_info' : _MetaInfoClass('Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue',
            False, 
            [
            _MetaInfoClassMember('src-interface-name-value', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Which Interface
                ''',
                'src_interface_name_value',
                'Cisco-IOS-XR-infra-syslog-cfg', True),
            _MetaInfoClassMember('source-interface-vrfs', REFERENCE_CLASS, 'SourceInterfaceVrfs' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs', 
                [], [], 
                '''                Configure source interface VRF
                ''',
                'source_interface_vrfs',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'source-interface-value',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.SourceInterfaceTable.SourceInterfaceValues' : {
        'meta_info' : _MetaInfoClass('Syslog.SourceInterfaceTable.SourceInterfaceValues',
            False, 
            [
            _MetaInfoClassMember('source-interface-value', REFERENCE_LIST, 'SourceInterfaceValue' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue', 
                [], [], 
                '''                Source interface
                ''',
                'source_interface_value',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'source-interface-values',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.SourceInterfaceTable' : {
        'meta_info' : _MetaInfoClass('Syslog.SourceInterfaceTable',
            False, 
            [
            _MetaInfoClassMember('source-interface-values', REFERENCE_CLASS, 'SourceInterfaceValues' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.SourceInterfaceTable.SourceInterfaceValues', 
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
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog.TrapLogging' : {
        'meta_info' : _MetaInfoClass('Syslog.TrapLogging',
            False, 
            [
            _MetaInfoClassMember('logging-level', REFERENCE_ENUM_CLASS, 'LoggingLevelsEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingLevelsEnum', 
                [], [], 
                '''                Trap logging level
                ''',
                'logging_level',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'trap-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'Syslog' : {
        'meta_info' : _MetaInfoClass('Syslog',
            False, 
            [
            _MetaInfoClassMember('alarm-logger', REFERENCE_CLASS, 'AlarmLogger' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.AlarmLogger', 
                [], [], 
                '''                Alarm Logger Properties
                ''',
                'alarm_logger',
                'Cisco-IOS-XR-infra-alarm-logger-cfg', False),
            _MetaInfoClassMember('archive', REFERENCE_CLASS, 'Archive' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Archive', 
                [], [], 
                '''                Archive attributes configuration
                ''',
                'archive',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('buffered-logging', REFERENCE_CLASS, 'BufferedLogging' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.BufferedLogging', 
                [], [], 
                '''                Set buffered logging parameters
                ''',
                'buffered_logging',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('console-logging', REFERENCE_CLASS, 'ConsoleLogging' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.ConsoleLogging', 
                [], [], 
                '''                Set console logging
                ''',
                'console_logging',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('enable-console-logging', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled
                ''',
                'enable_console_logging',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('files', REFERENCE_CLASS, 'Files' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Files', 
                [], [], 
                '''                Configure logging file destination
                ''',
                'files',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('history-logging', REFERENCE_CLASS, 'HistoryLogging' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HistoryLogging', 
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
            _MetaInfoClassMember('host-server', REFERENCE_CLASS, 'HostServer' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.HostServer', 
                [], [], 
                '''                Configure logging host
                ''',
                'host_server',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Ipv4', 
                [], [], 
                '''                Syslog TOS bit for outgoing messages
                ''',
                'ipv4',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.Ipv6', 
                [], [], 
                '''                Syslog traffic class bit for outgoing messages
                ''',
                'ipv6',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('local-log-file-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Set size of the local log file
                ''',
                'local_log_file_size',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('logging-facilities', REFERENCE_CLASS, 'LoggingFacilities' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.LoggingFacilities', 
                [], [], 
                '''                Modify message logging facilities
                ''',
                'logging_facilities',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('monitor-logging', REFERENCE_CLASS, 'MonitorLogging' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.MonitorLogging', 
                [], [], 
                '''                Set monitor logging
                ''',
                'monitor_logging',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('source-interface-table', REFERENCE_CLASS, 'SourceInterfaceTable' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.SourceInterfaceTable', 
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
            _MetaInfoClassMember('trap-logging', REFERENCE_CLASS, 'TrapLogging' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'Syslog.TrapLogging', 
                [], [], 
                '''                Set trap logging
                ''',
                'trap_logging',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'syslog',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue' : {
        'meta_info' : _MetaInfoClass('SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue',
            False, 
            [
            _MetaInfoClassMember('msec', REFERENCE_ENUM_CLASS, 'TimeInfoEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfoEnum', 
                [], [], 
                '''                Seconds
                ''',
                'msec',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('time-stamp-value', REFERENCE_ENUM_CLASS, 'TimeInfoEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfoEnum', 
                [], [], 
                '''                Time
                ''',
                'time_stamp_value',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('time-zone', REFERENCE_ENUM_CLASS, 'TimeInfoEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfoEnum', 
                [], [], 
                '''                Timezone
                ''',
                'time_zone',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('year', REFERENCE_ENUM_CLASS, 'TimeInfoEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfoEnum', 
                [], [], 
                '''                Year
                ''',
                'year',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'datetime-value',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'SyslogService.Timestamps.Debug.DebugDatetime' : {
        'meta_info' : _MetaInfoClass('SyslogService.Timestamps.Debug.DebugDatetime',
            False, 
            [
            _MetaInfoClassMember('datetime-value', REFERENCE_CLASS, 'DatetimeValue' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue', 
                [], [], 
                '''                Set time format for debug msg
                ''',
                'datetime_value',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'debug-datetime',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'SyslogService.Timestamps.Debug' : {
        'meta_info' : _MetaInfoClass('SyslogService.Timestamps.Debug',
            False, 
            [
            _MetaInfoClassMember('debug-datetime', REFERENCE_CLASS, 'DebugDatetime' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'SyslogService.Timestamps.Debug.DebugDatetime', 
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
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue' : {
        'meta_info' : _MetaInfoClass('SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue',
            False, 
            [
            _MetaInfoClassMember('msec', REFERENCE_ENUM_CLASS, 'TimeInfoEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfoEnum', 
                [], [], 
                '''                Seconds
                ''',
                'msec',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('time-stamp-value', REFERENCE_ENUM_CLASS, 'TimeInfoEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfoEnum', 
                [], [], 
                '''                Time
                ''',
                'time_stamp_value',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('time-zone', REFERENCE_ENUM_CLASS, 'TimeInfoEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfoEnum', 
                [], [], 
                '''                Timezone
                ''',
                'time_zone',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            _MetaInfoClassMember('year', REFERENCE_ENUM_CLASS, 'TimeInfoEnum' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfoEnum', 
                [], [], 
                '''                Year
                ''',
                'year',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'log-datetime-value',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'SyslogService.Timestamps.Log.LogDatetime' : {
        'meta_info' : _MetaInfoClass('SyslogService.Timestamps.Log.LogDatetime',
            False, 
            [
            _MetaInfoClassMember('log-datetime-value', REFERENCE_CLASS, 'LogDatetimeValue' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue', 
                [], [], 
                '''                Set timestamp for log message
                ''',
                'log_datetime_value',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'log-datetime',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'SyslogService.Timestamps.Log' : {
        'meta_info' : _MetaInfoClass('SyslogService.Timestamps.Log',
            False, 
            [
            _MetaInfoClassMember('log-datetime', REFERENCE_CLASS, 'LogDatetime' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'SyslogService.Timestamps.Log.LogDatetime', 
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
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'SyslogService.Timestamps' : {
        'meta_info' : _MetaInfoClass('SyslogService.Timestamps',
            False, 
            [
            _MetaInfoClassMember('debug', REFERENCE_CLASS, 'Debug' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'SyslogService.Timestamps.Debug', 
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
            _MetaInfoClassMember('log', REFERENCE_CLASS, 'Log' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'SyslogService.Timestamps.Log', 
                [], [], 
                '''                Timestamp log messages
                ''',
                'log',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'timestamps',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
    'SyslogService' : {
        'meta_info' : _MetaInfoClass('SyslogService',
            False, 
            [
            _MetaInfoClassMember('timestamps', REFERENCE_CLASS, 'Timestamps' , 'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg', 'SyslogService.Timestamps', 
                [], [], 
                '''                Timestamp debug/log messages configuration
                ''',
                'timestamps',
                'Cisco-IOS-XR-infra-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-infra-syslog-cfg',
            'syslog-service',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-syslog-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg'
        ),
    },
}
_meta_table['Syslog.BufferedLogging.BufferedDiscriminator']['meta_info'].parent =_meta_table['Syslog.BufferedLogging']['meta_info']
_meta_table['Syslog.ConsoleLogging.ConsoleDiscriminator']['meta_info'].parent =_meta_table['Syslog.ConsoleLogging']['meta_info']
_meta_table['Syslog.Files.File.FileLogDiscriminator']['meta_info'].parent =_meta_table['Syslog.Files.File']['meta_info']
_meta_table['Syslog.Files.File.FileSpecification']['meta_info'].parent =_meta_table['Syslog.Files.File']['meta_info']
_meta_table['Syslog.Files.File']['meta_info'].parent =_meta_table['Syslog.Files']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameDiscriminator']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4Discriminator']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityPort']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6Discriminator']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityPort']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs.Vrf']['meta_info']
_meta_table['Syslog.HostServer.Vrfs.Vrf']['meta_info'].parent =_meta_table['Syslog.HostServer.Vrfs']['meta_info']
_meta_table['Syslog.HostServer.Vrfs']['meta_info'].parent =_meta_table['Syslog.HostServer']['meta_info']
_meta_table['Syslog.Ipv4.Dscp']['meta_info'].parent =_meta_table['Syslog.Ipv4']['meta_info']
_meta_table['Syslog.Ipv4.Precedence']['meta_info'].parent =_meta_table['Syslog.Ipv4']['meta_info']
_meta_table['Syslog.Ipv4.Tos']['meta_info'].parent =_meta_table['Syslog.Ipv4']['meta_info']
_meta_table['Syslog.Ipv6.Dscp']['meta_info'].parent =_meta_table['Syslog.Ipv6']['meta_info']
_meta_table['Syslog.Ipv6.Precedence']['meta_info'].parent =_meta_table['Syslog.Ipv6']['meta_info']
_meta_table['Syslog.Ipv6.TrafficClass']['meta_info'].parent =_meta_table['Syslog.Ipv6']['meta_info']
_meta_table['Syslog.MonitorLogging.MonitorDiscriminator']['meta_info'].parent =_meta_table['Syslog.MonitorLogging']['meta_info']
_meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf']['meta_info'].parent =_meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs']['meta_info']
_meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs']['meta_info'].parent =_meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue']['meta_info']
_meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue']['meta_info'].parent =_meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues']['meta_info']
_meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues']['meta_info'].parent =_meta_table['Syslog.SourceInterfaceTable']['meta_info']
_meta_table['Syslog.AlarmLogger']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.Archive']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.BufferedLogging']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.ConsoleLogging']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.Files']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.HistoryLogging']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.HostServer']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.Ipv4']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.Ipv6']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.LoggingFacilities']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.MonitorLogging']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.SourceInterfaceTable']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['Syslog.TrapLogging']['meta_info'].parent =_meta_table['Syslog']['meta_info']
_meta_table['SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue']['meta_info'].parent =_meta_table['SyslogService.Timestamps.Debug.DebugDatetime']['meta_info']
_meta_table['SyslogService.Timestamps.Debug.DebugDatetime']['meta_info'].parent =_meta_table['SyslogService.Timestamps.Debug']['meta_info']
_meta_table['SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue']['meta_info'].parent =_meta_table['SyslogService.Timestamps.Log.LogDatetime']['meta_info']
_meta_table['SyslogService.Timestamps.Log.LogDatetime']['meta_info'].parent =_meta_table['SyslogService.Timestamps.Log']['meta_info']
_meta_table['SyslogService.Timestamps.Debug']['meta_info'].parent =_meta_table['SyslogService.Timestamps']['meta_info']
_meta_table['SyslogService.Timestamps.Log']['meta_info'].parent =_meta_table['SyslogService.Timestamps']['meta_info']
_meta_table['SyslogService.Timestamps']['meta_info'].parent =_meta_table['SyslogService']['meta_info']
