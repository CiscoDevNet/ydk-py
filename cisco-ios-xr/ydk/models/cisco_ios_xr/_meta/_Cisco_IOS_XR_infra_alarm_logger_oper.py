


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AlAlarmSeverityEnum' : _MetaInfoEnum('AlAlarmSeverityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper',
        {
            'unknown':'unknown',
            'emergency':'emergency',
            'alert':'alert',
            'critical':'critical',
            'error':'error',
            'warning':'warning',
            'notice':'notice',
            'informational':'informational',
            'debugging':'debugging',
        }, 'Cisco-IOS-XR-infra-alarm-logger-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-alarm-logger-oper']),
    'AlAlarmBistateEnum' : _MetaInfoEnum('AlAlarmBistateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper',
        {
            'not-available':'not_available',
            'active':'active',
            'clear':'clear',
        }, 'Cisco-IOS-XR-infra-alarm-logger-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-alarm-logger-oper']),
    'AlarmLogger.BufferStatus' : {
        'meta_info' : _MetaInfoClass('AlarmLogger.BufferStatus',
            False, 
            [
            _MetaInfoClassMember('capacity-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Percentage of the buffer utilization which, when
                exceeded, triggers the  generation of a
                notification for the clients of the XML agent
                ''',
                'capacity_threshold',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False),
            _MetaInfoClassMember('log-buffer-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current Logging Buffer Size (Bytes)
                ''',
                'log_buffer_size',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False),
            _MetaInfoClassMember('max-log-buffer-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum Logging Buffer Size (Bytes) 
                ''',
                'max_log_buffer_size',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False),
            _MetaInfoClassMember('record-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Records in the Buffer
                ''',
                'record_count',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False),
            _MetaInfoClassMember('severity-filter', REFERENCE_ENUM_CLASS, 'AlAlarmSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper', 'AlAlarmSeverityEnum', 
                [], [], 
                '''                Severity Filter
                ''',
                'severity_filter',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False),
            ],
            'Cisco-IOS-XR-infra-alarm-logger-oper',
            'buffer-status',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-alarm-logger-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper'
        ),
    },
    'AlarmLogger.Alarms.Alarm' : {
        'meta_info' : _MetaInfoClass('AlarmLogger.Alarms.Alarm',
            False, 
            [
            _MetaInfoClassMember('event-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Event ID
                ''',
                'event_id',
                'Cisco-IOS-XR-infra-alarm-logger-oper', True),
            _MetaInfoClassMember('additional-text', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Full text of the Alarm
                ''',
                'additional_text',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False),
            _MetaInfoClassMember('category', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Category of the alarm
                ''',
                'category',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False),
            _MetaInfoClassMember('code', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Alarm code which further qualifies the alarm
                within a message group
                ''',
                'code',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False),
            _MetaInfoClassMember('correlation-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Correlation Identifier
                ''',
                'correlation_id',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False),
            _MetaInfoClassMember('group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Group of messages to which this alarm belongs to
                ''',
                'group',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False),
            _MetaInfoClassMember('is-admin', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates the event id admin-level
                ''',
                'is_admin',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'AlAlarmSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper', 'AlAlarmSeverityEnum', 
                [], [], 
                '''                Severity of the alarm
                ''',
                'severity',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False),
            _MetaInfoClassMember('source-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Identifier(Location).Indicates the node
                in which the alarm was generated
                ''',
                'source_id',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'AlAlarmBistateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper', 'AlAlarmBistateEnum', 
                [], [], 
                '''                State of the alarm (bistate alarms only)
                ''',
                'state',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False),
            _MetaInfoClassMember('timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time when the alarm was generated. It is
                expressed in number of milliseconds since 00:00
                :00 UTC, January 1, 1970
                ''',
                'timestamp',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False),
            ],
            'Cisco-IOS-XR-infra-alarm-logger-oper',
            'alarm',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-alarm-logger-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper'
        ),
    },
    'AlarmLogger.Alarms' : {
        'meta_info' : _MetaInfoClass('AlarmLogger.Alarms',
            False, 
            [
            _MetaInfoClassMember('alarm', REFERENCE_LIST, 'Alarm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper', 'AlarmLogger.Alarms.Alarm', 
                [], [], 
                '''                One of the logged alarms
                ''',
                'alarm',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False),
            ],
            'Cisco-IOS-XR-infra-alarm-logger-oper',
            'alarms',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-alarm-logger-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper'
        ),
    },
    'AlarmLogger' : {
        'meta_info' : _MetaInfoClass('AlarmLogger',
            False, 
            [
            _MetaInfoClassMember('alarms', REFERENCE_CLASS, 'Alarms' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper', 'AlarmLogger.Alarms', 
                [], [], 
                '''                Table that contains the database of logged
                alarms
                ''',
                'alarms',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False),
            _MetaInfoClassMember('buffer-status', REFERENCE_CLASS, 'BufferStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper', 'AlarmLogger.BufferStatus', 
                [], [], 
                '''                Describes buffer utilization and parameters
                configured
                ''',
                'buffer_status',
                'Cisco-IOS-XR-infra-alarm-logger-oper', False),
            ],
            'Cisco-IOS-XR-infra-alarm-logger-oper',
            'alarm-logger',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-alarm-logger-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper'
        ),
    },
}
_meta_table['AlarmLogger.Alarms.Alarm']['meta_info'].parent =_meta_table['AlarmLogger.Alarms']['meta_info']
_meta_table['AlarmLogger.BufferStatus']['meta_info'].parent =_meta_table['AlarmLogger']['meta_info']
_meta_table['AlarmLogger.Alarms']['meta_info'].parent =_meta_table['AlarmLogger']['meta_info']
