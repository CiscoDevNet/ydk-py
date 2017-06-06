


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'TimingBucketEnum' : _MetaInfoEnum('TimingBucketEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper',
        {
            'not-specified':'not_specified',
            'fifteen-min':'fifteen_min',
            'one-day':'one_day',
        }, 'Cisco-IOS-XR-alarmgr-server-oper', _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper']),
    'AlarmClientStateEnum' : _MetaInfoEnum('AlarmClientStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper',
        {
            'start':'start',
            'init':'init',
            'connecting':'connecting',
            'connected':'connected',
            'registered':'registered',
            'disconnected':'disconnected',
            'ready':'ready',
        }, 'Cisco-IOS-XR-alarmgr-server-oper', _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper']),
    'AlarmSeverityEnum' : _MetaInfoEnum('AlarmSeverityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper',
        {
            'unknown':'unknown',
            'not-reported':'not_reported',
            'not-alarmed':'not_alarmed',
            'minor':'minor',
            'major':'major',
            'critical':'critical',
            'severity-last':'severity_last',
        }, 'Cisco-IOS-XR-alarmgr-server-oper', _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper']),
    'AlarmServiceAffectingEnum' : _MetaInfoEnum('AlarmServiceAffectingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper',
        {
            'unknown':'unknown',
            'not-service-affecting':'not_service_affecting',
            'service-affecting':'service_affecting',
        }, 'Cisco-IOS-XR-alarmgr-server-oper', _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper']),
    'AlarmClientEnum' : _MetaInfoEnum('AlarmClientEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper',
        {
            'unknown':'unknown',
            'producer':'producer',
            'consumer':'consumer',
            'subscriber':'subscriber',
            'client-last':'client_last',
        }, 'Cisco-IOS-XR-alarmgr-server-oper', _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper']),
    'AlarmNotificationSrcEnum' : _MetaInfoEnum('AlarmNotificationSrcEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper',
        {
            'not-specified':'not_specified',
            'near-end':'near_end',
            'far-end':'far_end',
        }, 'Cisco-IOS-XR-alarmgr-server-oper', _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper']),
    'AlarmDirectionEnum' : _MetaInfoEnum('AlarmDirectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper',
        {
            'not-specified':'not_specified',
            'send':'send',
            'receive':'receive',
            'send-receive':'send_receive',
        }, 'Cisco-IOS-XR-alarmgr-server-oper', _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper']),
    'AlarmStatusEnum' : _MetaInfoEnum('AlarmStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper',
        {
            'unknown':'unknown',
            'set':'set',
            'clear':'clear',
            'suppress':'suppress',
            'last':'last',
        }, 'Cisco-IOS-XR-alarmgr-server-oper', _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper']),
    'AlarmEventEnum' : _MetaInfoEnum('AlarmEventEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper',
        {
            'default':'default',
            'notification':'notification',
            'last':'last',
        }, 'Cisco-IOS-XR-alarmgr-server-oper', _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper']),
    'AlarmGroupsEnum' : _MetaInfoEnum('AlarmGroupsEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper',
        {
            'unknown':'unknown',
            'environ':'environ',
            'ethernet':'ethernet',
            'fabric':'fabric',
            'power':'power',
            'software':'software',
            'slice':'slice',
            'cpu':'cpu',
            'controller':'controller',
            'sonet':'sonet',
            'otn':'otn',
            'sdh-controller':'sdh_controller',
            'asic':'asic',
            'fpd-infra':'fpd_infra',
            'shelf':'shelf',
            'mpa':'mpa',
            'ots':'ots',
            'last':'last',
        }, 'Cisco-IOS-XR-alarmgr-server-oper', _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper']),
    'Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AlarmDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmDirectionEnum', 
                [], [], 
                '''                Alarm direction 
                ''',
                'direction',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('notification-source', REFERENCE_ENUM_CLASS, 'AlarmNotificationSrcEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmNotificationSrcEnum', 
                [], [], 
                '''                Source of Alarm
                ''',
                'notification_source',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'otn',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca',
            False, 
            [
            _MetaInfoClassMember('bucket-type', REFERENCE_ENUM_CLASS, 'TimingBucketEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'TimingBucketEnum', 
                [], [], 
                '''                Timing Bucket
                ''',
                'bucket_type',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('current-value', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                Alarm Threshold
                ''',
                'current_value',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('threshold-value', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                Alarm Threshold 
                ''',
                'threshold_value',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'tca',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailSystem.Active.AlarmInfo' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailSystem.Active.AlarmInfo',
            False, 
            [
            _MetaInfoClassMember('aid', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm aid
                ''',
                'aid',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('alarm-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm name
                ''',
                'alarm_name',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('clear-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm clear time
                ''',
                'clear_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('clear-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm clear time(timestamp format)
                ''',
                'clear_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Alarm description
                ''',
                'description',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('eid', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm eid
                ''',
                'eid',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'AlarmGroupsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroupsEnum', 
                [], [], 
                '''                Alarm group
                ''',
                'group',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm interface name
                ''',
                'interface',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm location
                ''',
                'location',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('module', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm module description
                ''',
                'module',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('otn', REFERENCE_CLASS, 'Otn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn', 
                [], [], 
                '''                OTN feature specific alarm attributes
                ''',
                'otn',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('pending-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Pending async flag
                ''',
                'pending_sync',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('reporting-agent-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reporting agent id
                ''',
                'reporting_agent_id',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('service-affecting', REFERENCE_ENUM_CLASS, 'AlarmServiceAffectingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmServiceAffectingEnum', 
                [], [], 
                '''                Alarm service affecting
                ''',
                'service_affecting',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm set time
                ''',
                'set_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm set time(timestamp format)
                ''',
                'set_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'AlarmSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverityEnum', 
                [], [], 
                '''                Alarm severity
                ''',
                'severity',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'AlarmStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmStatusEnum', 
                [], [], 
                '''                Alarm status
                ''',
                'status',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm tag description
                ''',
                'tag',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('tca', REFERENCE_CLASS, 'Tca' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca', 
                [], [], 
                '''                TCA feature specific alarm attributes
                ''',
                'tca',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'AlarmEventEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmEventEnum', 
                [], [], 
                '''                alarm event type
                ''',
                'type',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'alarm-info',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailSystem.Active' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailSystem.Active',
            False, 
            [
            _MetaInfoClassMember('alarm-info', REFERENCE_LIST, 'AlarmInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailSystem.Active.AlarmInfo', 
                [], [], 
                '''                Alarm List
                ''',
                'alarm_info',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailSystem.History.AlarmInfo.Otn' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailSystem.History.AlarmInfo.Otn',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AlarmDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmDirectionEnum', 
                [], [], 
                '''                Alarm direction 
                ''',
                'direction',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('notification-source', REFERENCE_ENUM_CLASS, 'AlarmNotificationSrcEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmNotificationSrcEnum', 
                [], [], 
                '''                Source of Alarm
                ''',
                'notification_source',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'otn',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailSystem.History.AlarmInfo.Tca' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailSystem.History.AlarmInfo.Tca',
            False, 
            [
            _MetaInfoClassMember('bucket-type', REFERENCE_ENUM_CLASS, 'TimingBucketEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'TimingBucketEnum', 
                [], [], 
                '''                Timing Bucket
                ''',
                'bucket_type',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('current-value', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                Alarm Threshold
                ''',
                'current_value',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('threshold-value', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                Alarm Threshold 
                ''',
                'threshold_value',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'tca',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailSystem.History.AlarmInfo' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailSystem.History.AlarmInfo',
            False, 
            [
            _MetaInfoClassMember('aid', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm aid
                ''',
                'aid',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('alarm-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm name
                ''',
                'alarm_name',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('clear-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm clear time
                ''',
                'clear_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('clear-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm clear time(timestamp format)
                ''',
                'clear_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Alarm description
                ''',
                'description',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('eid', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm eid
                ''',
                'eid',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'AlarmGroupsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroupsEnum', 
                [], [], 
                '''                Alarm group
                ''',
                'group',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm interface name
                ''',
                'interface',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm location
                ''',
                'location',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('module', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm module description
                ''',
                'module',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('otn', REFERENCE_CLASS, 'Otn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailSystem.History.AlarmInfo.Otn', 
                [], [], 
                '''                OTN feature specific alarm attributes
                ''',
                'otn',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('pending-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Pending async flag
                ''',
                'pending_sync',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('reporting-agent-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reporting agent id
                ''',
                'reporting_agent_id',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('service-affecting', REFERENCE_ENUM_CLASS, 'AlarmServiceAffectingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmServiceAffectingEnum', 
                [], [], 
                '''                Alarm service affecting
                ''',
                'service_affecting',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm set time
                ''',
                'set_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm set time(timestamp format)
                ''',
                'set_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'AlarmSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverityEnum', 
                [], [], 
                '''                Alarm severity
                ''',
                'severity',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'AlarmStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmStatusEnum', 
                [], [], 
                '''                Alarm status
                ''',
                'status',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm tag description
                ''',
                'tag',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('tca', REFERENCE_CLASS, 'Tca' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailSystem.History.AlarmInfo.Tca', 
                [], [], 
                '''                TCA feature specific alarm attributes
                ''',
                'tca',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'AlarmEventEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmEventEnum', 
                [], [], 
                '''                alarm event type
                ''',
                'type',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'alarm-info',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailSystem.History' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailSystem.History',
            False, 
            [
            _MetaInfoClassMember('alarm-info', REFERENCE_LIST, 'AlarmInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailSystem.History.AlarmInfo', 
                [], [], 
                '''                Alarm List
                ''',
                'alarm_info',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'history',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AlarmDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmDirectionEnum', 
                [], [], 
                '''                Alarm direction 
                ''',
                'direction',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('notification-source', REFERENCE_ENUM_CLASS, 'AlarmNotificationSrcEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmNotificationSrcEnum', 
                [], [], 
                '''                Source of Alarm
                ''',
                'notification_source',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'otn',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo',
            False, 
            [
            _MetaInfoClassMember('aid', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm aid
                ''',
                'aid',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('alarm-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm name
                ''',
                'alarm_name',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Alarm description
                ''',
                'description',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('eid', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm eid
                ''',
                'eid',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'AlarmGroupsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroupsEnum', 
                [], [], 
                '''                Alarm group
                ''',
                'group',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm interface name
                ''',
                'interface',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm location
                ''',
                'location',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('module', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm module description
                ''',
                'module',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('otn', REFERENCE_CLASS, 'Otn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn', 
                [], [], 
                '''                OTN feature specific alarm attributes
                ''',
                'otn',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('pending-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Pending async flag
                ''',
                'pending_sync',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('reporting-agent-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reporting agent id
                ''',
                'reporting_agent_id',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('service-affecting', REFERENCE_ENUM_CLASS, 'AlarmServiceAffectingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmServiceAffectingEnum', 
                [], [], 
                '''                Alarm service affecting 
                ''',
                'service_affecting',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm set time
                ''',
                'set_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm set time(timestamp format)
                ''',
                'set_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'AlarmSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverityEnum', 
                [], [], 
                '''                Alarm severity
                ''',
                'severity',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'AlarmStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmStatusEnum', 
                [], [], 
                '''                Alarm status
                ''',
                'status',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('suppressed-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm suppressed time
                ''',
                'suppressed_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('suppressed-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm suppressed time(timestamp format)
                ''',
                'suppressed_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm tag description
                ''',
                'tag',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'suppressed-info',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailSystem.Suppressed' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailSystem.Suppressed',
            False, 
            [
            _MetaInfoClassMember('suppressed-info', REFERENCE_LIST, 'SuppressedInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo', 
                [], [], 
                '''                Suppressed Alarm List
                ''',
                'suppressed_info',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'suppressed',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailSystem.Stats' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailSystem.Stats',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarms that are currently in the active state
                ''',
                'active',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('cache-hit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total alarms which had the cache hit
                ''',
                'cache_hit',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('cache-miss', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total alarms which had the cache miss
                ''',
                'cache_miss',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarms that we couldn't keep track due to some
                error or other
                ''',
                'dropped',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('dropped-clear-without-set', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Alarms dropped clear without set
                ''',
                'dropped_clear_without_set',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('dropped-db-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Alarms dropped due to db error
                ''',
                'dropped_db_error',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('dropped-duplicate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Alarms dropped which were duplicate
                ''',
                'dropped_duplicate',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('dropped-insuff-mem', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Alarms dropped due to insufficient memory
                ''',
                'dropped_insuff_mem',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('dropped-invalid-aid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Alarms dropped due to invalid aid
                ''',
                'dropped_invalid_aid',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('history', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarms that are cleared. This one is counted
                over a long period of time
                ''',
                'history',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('reported', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarms that were in all reported to this Alarm
                Mgr
                ''',
                'reported',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('suppressed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarms that are in suppressed state
                ''',
                'suppressed',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('sysadmin-active', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarms that are currently in the active
                state(sysadmin plane)
                ''',
                'sysadmin_active',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('sysadmin-history', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarms that are cleared in sysadmin plane. This
                one is counted over a long period of time
                ''',
                'sysadmin_history',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('sysadmin-suppressed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarms that are suppressed in sysadmin plane.
                ''',
                'sysadmin_suppressed',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'stats',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailSystem.Clients.ClientInfo' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailSystem.Clients.ClientInfo',
            False, 
            [
            _MetaInfoClassMember('connect-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times the agent connected to the alarm
                mgr
                ''',
                'connect_count',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('connect-timestamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Agent connect timestamp
                ''',
                'connect_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('filter-disp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The current subscription status of the client
                ''',
                'filter_disp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('filter-group', REFERENCE_ENUM_CLASS, 'AlarmGroupsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroupsEnum', 
                [], [], 
                '''                The filter used for alarm group
                ''',
                'filter_group',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('filter-severity', REFERENCE_ENUM_CLASS, 'AlarmSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverityEnum', 
                [], [], 
                '''                The filter used for alarm severity
                ''',
                'filter_severity',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('filter-state', REFERENCE_ENUM_CLASS, 'AlarmStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmStatusEnum', 
                [], [], 
                '''                The filter used for alarm bi-state state+
                ''',
                'filter_state',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('get-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times the agent queried for alarms
                ''',
                'get_count',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('handle', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                The client handle through which interface
                ''',
                'handle',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Alarms agent id of the client
                ''',
                'id',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                The location of this client
                ''',
                'location',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm client
                ''',
                'name',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('report-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times the agent reported alarms
                ''',
                'report_count',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'AlarmClientStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmClientStateEnum', 
                [], [], 
                '''                The current state of the client
                ''',
                'state',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('subscribe-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times the agent subscribed for alarms
                ''',
                'subscribe_count',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('subscriber-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Alarms agent subscriber id of the client
                ''',
                'subscriber_id',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'AlarmClientEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmClientEnum', 
                [], [], 
                '''                The type of the client
                ''',
                'type',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'client-info',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailSystem.Clients' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailSystem.Clients',
            False, 
            [
            _MetaInfoClassMember('client-info', REFERENCE_LIST, 'ClientInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailSystem.Clients.ClientInfo', 
                [], [], 
                '''                Client List
                ''',
                'client_info',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'clients',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailSystem' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailSystem',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailSystem.Active', 
                [], [], 
                '''                Show the active alarms at this scope.
                ''',
                'active',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('clients', REFERENCE_CLASS, 'Clients' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailSystem.Clients', 
                [], [], 
                '''                Show the clients associated with this service.
                ''',
                'clients',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('history', REFERENCE_CLASS, 'History' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailSystem.History', 
                [], [], 
                '''                Show the history alarms at this scope.
                ''',
                'history',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('stats', REFERENCE_CLASS, 'Stats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailSystem.Stats', 
                [], [], 
                '''                Show the service statistics.
                ''',
                'stats',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('suppressed', REFERENCE_CLASS, 'Suppressed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailSystem.Suppressed', 
                [], [], 
                '''                Show the suppressed alarms at this scope.
                ''',
                'suppressed',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'detail-system',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AlarmDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmDirectionEnum', 
                [], [], 
                '''                Alarm direction 
                ''',
                'direction',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('notification-source', REFERENCE_ENUM_CLASS, 'AlarmNotificationSrcEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmNotificationSrcEnum', 
                [], [], 
                '''                Source of Alarm
                ''',
                'notification_source',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'otn',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca',
            False, 
            [
            _MetaInfoClassMember('bucket-type', REFERENCE_ENUM_CLASS, 'TimingBucketEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'TimingBucketEnum', 
                [], [], 
                '''                Timing Bucket
                ''',
                'bucket_type',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('current-value', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                Alarm Threshold
                ''',
                'current_value',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('threshold-value', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                Alarm Threshold 
                ''',
                'threshold_value',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'tca',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo',
            False, 
            [
            _MetaInfoClassMember('aid', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm aid
                ''',
                'aid',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('alarm-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm name
                ''',
                'alarm_name',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('clear-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm clear time
                ''',
                'clear_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('clear-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm clear time(timestamp format)
                ''',
                'clear_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Alarm description
                ''',
                'description',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('eid', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm eid
                ''',
                'eid',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'AlarmGroupsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroupsEnum', 
                [], [], 
                '''                Alarm group
                ''',
                'group',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm interface name
                ''',
                'interface',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm location
                ''',
                'location',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('module', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm module description
                ''',
                'module',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('otn', REFERENCE_CLASS, 'Otn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn', 
                [], [], 
                '''                OTN feature specific alarm attributes
                ''',
                'otn',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('pending-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Pending async flag
                ''',
                'pending_sync',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('reporting-agent-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reporting agent id
                ''',
                'reporting_agent_id',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('service-affecting', REFERENCE_ENUM_CLASS, 'AlarmServiceAffectingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmServiceAffectingEnum', 
                [], [], 
                '''                Alarm service affecting
                ''',
                'service_affecting',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm set time
                ''',
                'set_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm set time(timestamp format)
                ''',
                'set_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'AlarmSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverityEnum', 
                [], [], 
                '''                Alarm severity
                ''',
                'severity',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'AlarmStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmStatusEnum', 
                [], [], 
                '''                Alarm status
                ''',
                'status',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm tag description
                ''',
                'tag',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('tca', REFERENCE_CLASS, 'Tca' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca', 
                [], [], 
                '''                TCA feature specific alarm attributes
                ''',
                'tca',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'AlarmEventEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmEventEnum', 
                [], [], 
                '''                alarm event type
                ''',
                'type',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'alarm-info',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active',
            False, 
            [
            _MetaInfoClassMember('alarm-info', REFERENCE_LIST, 'AlarmInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo', 
                [], [], 
                '''                Alarm List
                ''',
                'alarm_info',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AlarmDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmDirectionEnum', 
                [], [], 
                '''                Alarm direction 
                ''',
                'direction',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('notification-source', REFERENCE_ENUM_CLASS, 'AlarmNotificationSrcEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmNotificationSrcEnum', 
                [], [], 
                '''                Source of Alarm
                ''',
                'notification_source',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'otn',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca',
            False, 
            [
            _MetaInfoClassMember('bucket-type', REFERENCE_ENUM_CLASS, 'TimingBucketEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'TimingBucketEnum', 
                [], [], 
                '''                Timing Bucket
                ''',
                'bucket_type',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('current-value', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                Alarm Threshold
                ''',
                'current_value',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('threshold-value', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                Alarm Threshold 
                ''',
                'threshold_value',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'tca',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo',
            False, 
            [
            _MetaInfoClassMember('aid', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm aid
                ''',
                'aid',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('alarm-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm name
                ''',
                'alarm_name',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('clear-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm clear time
                ''',
                'clear_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('clear-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm clear time(timestamp format)
                ''',
                'clear_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Alarm description
                ''',
                'description',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('eid', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm eid
                ''',
                'eid',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'AlarmGroupsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroupsEnum', 
                [], [], 
                '''                Alarm group
                ''',
                'group',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm interface name
                ''',
                'interface',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm location
                ''',
                'location',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('module', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm module description
                ''',
                'module',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('otn', REFERENCE_CLASS, 'Otn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn', 
                [], [], 
                '''                OTN feature specific alarm attributes
                ''',
                'otn',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('pending-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Pending async flag
                ''',
                'pending_sync',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('reporting-agent-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reporting agent id
                ''',
                'reporting_agent_id',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('service-affecting', REFERENCE_ENUM_CLASS, 'AlarmServiceAffectingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmServiceAffectingEnum', 
                [], [], 
                '''                Alarm service affecting
                ''',
                'service_affecting',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm set time
                ''',
                'set_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm set time(timestamp format)
                ''',
                'set_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'AlarmSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverityEnum', 
                [], [], 
                '''                Alarm severity
                ''',
                'severity',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'AlarmStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmStatusEnum', 
                [], [], 
                '''                Alarm status
                ''',
                'status',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm tag description
                ''',
                'tag',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('tca', REFERENCE_CLASS, 'Tca' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca', 
                [], [], 
                '''                TCA feature specific alarm attributes
                ''',
                'tca',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'AlarmEventEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmEventEnum', 
                [], [], 
                '''                alarm event type
                ''',
                'type',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'alarm-info',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History',
            False, 
            [
            _MetaInfoClassMember('alarm-info', REFERENCE_LIST, 'AlarmInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo', 
                [], [], 
                '''                Alarm List
                ''',
                'alarm_info',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'history',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AlarmDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmDirectionEnum', 
                [], [], 
                '''                Alarm direction 
                ''',
                'direction',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('notification-source', REFERENCE_ENUM_CLASS, 'AlarmNotificationSrcEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmNotificationSrcEnum', 
                [], [], 
                '''                Source of Alarm
                ''',
                'notification_source',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'otn',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo',
            False, 
            [
            _MetaInfoClassMember('aid', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm aid
                ''',
                'aid',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('alarm-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm name
                ''',
                'alarm_name',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Alarm description
                ''',
                'description',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('eid', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm eid
                ''',
                'eid',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'AlarmGroupsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroupsEnum', 
                [], [], 
                '''                Alarm group
                ''',
                'group',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm interface name
                ''',
                'interface',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm location
                ''',
                'location',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('module', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm module description
                ''',
                'module',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('otn', REFERENCE_CLASS, 'Otn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn', 
                [], [], 
                '''                OTN feature specific alarm attributes
                ''',
                'otn',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('pending-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Pending async flag
                ''',
                'pending_sync',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('reporting-agent-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reporting agent id
                ''',
                'reporting_agent_id',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('service-affecting', REFERENCE_ENUM_CLASS, 'AlarmServiceAffectingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmServiceAffectingEnum', 
                [], [], 
                '''                Alarm service affecting 
                ''',
                'service_affecting',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm set time
                ''',
                'set_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm set time(timestamp format)
                ''',
                'set_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'AlarmSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverityEnum', 
                [], [], 
                '''                Alarm severity
                ''',
                'severity',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'AlarmStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmStatusEnum', 
                [], [], 
                '''                Alarm status
                ''',
                'status',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('suppressed-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm suppressed time
                ''',
                'suppressed_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('suppressed-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm suppressed time(timestamp format)
                ''',
                'suppressed_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm tag description
                ''',
                'tag',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'suppressed-info',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed',
            False, 
            [
            _MetaInfoClassMember('suppressed-info', REFERENCE_LIST, 'SuppressedInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo', 
                [], [], 
                '''                Suppressed Alarm List
                ''',
                'suppressed_info',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'suppressed',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarms that are currently in the active state
                ''',
                'active',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('cache-hit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total alarms which had the cache hit
                ''',
                'cache_hit',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('cache-miss', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total alarms which had the cache miss
                ''',
                'cache_miss',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarms that we couldn't keep track due to some
                error or other
                ''',
                'dropped',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('dropped-clear-without-set', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Alarms dropped clear without set
                ''',
                'dropped_clear_without_set',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('dropped-db-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Alarms dropped due to db error
                ''',
                'dropped_db_error',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('dropped-duplicate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Alarms dropped which were duplicate
                ''',
                'dropped_duplicate',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('dropped-insuff-mem', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Alarms dropped due to insufficient memory
                ''',
                'dropped_insuff_mem',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('dropped-invalid-aid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Alarms dropped due to invalid aid
                ''',
                'dropped_invalid_aid',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('history', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarms that are cleared. This one is counted
                over a long period of time
                ''',
                'history',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('reported', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarms that were in all reported to this Alarm
                Mgr
                ''',
                'reported',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('suppressed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarms that are in suppressed state
                ''',
                'suppressed',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('sysadmin-active', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarms that are currently in the active
                state(sysadmin plane)
                ''',
                'sysadmin_active',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('sysadmin-history', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarms that are cleared in sysadmin plane. This
                one is counted over a long period of time
                ''',
                'sysadmin_history',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('sysadmin-suppressed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarms that are suppressed in sysadmin plane.
                ''',
                'sysadmin_suppressed',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'stats',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients.ClientInfo' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients.ClientInfo',
            False, 
            [
            _MetaInfoClassMember('connect-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times the agent connected to the alarm
                mgr
                ''',
                'connect_count',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('connect-timestamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Agent connect timestamp
                ''',
                'connect_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('filter-disp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The current subscription status of the client
                ''',
                'filter_disp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('filter-group', REFERENCE_ENUM_CLASS, 'AlarmGroupsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroupsEnum', 
                [], [], 
                '''                The filter used for alarm group
                ''',
                'filter_group',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('filter-severity', REFERENCE_ENUM_CLASS, 'AlarmSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverityEnum', 
                [], [], 
                '''                The filter used for alarm severity
                ''',
                'filter_severity',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('filter-state', REFERENCE_ENUM_CLASS, 'AlarmStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmStatusEnum', 
                [], [], 
                '''                The filter used for alarm bi-state state+
                ''',
                'filter_state',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('get-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times the agent queried for alarms
                ''',
                'get_count',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('handle', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                The client handle through which interface
                ''',
                'handle',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Alarms agent id of the client
                ''',
                'id',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                The location of this client
                ''',
                'location',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm client
                ''',
                'name',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('report-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times the agent reported alarms
                ''',
                'report_count',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'AlarmClientStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmClientStateEnum', 
                [], [], 
                '''                The current state of the client
                ''',
                'state',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('subscribe-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times the agent subscribed for alarms
                ''',
                'subscribe_count',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('subscriber-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Alarms agent subscriber id of the client
                ''',
                'subscriber_id',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'AlarmClientEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmClientEnum', 
                [], [], 
                '''                The type of the client
                ''',
                'type',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'client-info',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients',
            False, 
            [
            _MetaInfoClassMember('client-info', REFERENCE_LIST, 'ClientInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients.ClientInfo', 
                [], [], 
                '''                Client List
                ''',
                'client_info',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'clients',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailCard.DetailLocations.DetailLocation' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailCard.DetailLocations.DetailLocation',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                NodeID of the Location
                ''',
                'node_id',
                'Cisco-IOS-XR-alarmgr-server-oper', True),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active', 
                [], [], 
                '''                Show the active alarms at this scope.
                ''',
                'active',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('clients', REFERENCE_CLASS, 'Clients' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients', 
                [], [], 
                '''                Show the clients associated with this
                service.
                ''',
                'clients',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('history', REFERENCE_CLASS, 'History' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History', 
                [], [], 
                '''                Show the history alarms at this scope.
                ''',
                'history',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('stats', REFERENCE_CLASS, 'Stats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats', 
                [], [], 
                '''                Show the service statistics.
                ''',
                'stats',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('suppressed', REFERENCE_CLASS, 'Suppressed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed', 
                [], [], 
                '''                Show the suppressed alarms at this scope.
                ''',
                'suppressed',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'detail-location',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailCard.DetailLocations' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailCard.DetailLocations',
            False, 
            [
            _MetaInfoClassMember('detail-location', REFERENCE_LIST, 'DetailLocation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailCard.DetailLocations.DetailLocation', 
                [], [], 
                '''                Specify a card location for alarms.
                ''',
                'detail_location',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'detail-locations',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail.DetailCard' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail.DetailCard',
            False, 
            [
            _MetaInfoClassMember('detail-locations', REFERENCE_CLASS, 'DetailLocations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailCard.DetailLocations', 
                [], [], 
                '''                Table of DetailLocation
                ''',
                'detail_locations',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'detail-card',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Detail' : {
        'meta_info' : _MetaInfoClass('Alarms.Detail',
            False, 
            [
            _MetaInfoClassMember('detail-card', REFERENCE_CLASS, 'DetailCard' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailCard', 
                [], [], 
                '''                Show detail card scope alarm related data.
                ''',
                'detail_card',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('detail-system', REFERENCE_CLASS, 'DetailSystem' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail.DetailSystem', 
                [], [], 
                '''                show detail system scope alarm related data.
                ''',
                'detail_system',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active.AlarmInfo' : {
        'meta_info' : _MetaInfoClass('Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active.AlarmInfo',
            False, 
            [
            _MetaInfoClassMember('clear-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm clear time
                ''',
                'clear_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('clear-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm clear time(timestamp format)
                ''',
                'clear_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Alarm description
                ''',
                'description',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'AlarmGroupsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroupsEnum', 
                [], [], 
                '''                Alarm group
                ''',
                'group',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm location
                ''',
                'location',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm set time
                ''',
                'set_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm set time(timestamp format)
                ''',
                'set_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'AlarmSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverityEnum', 
                [], [], 
                '''                Alarm severity
                ''',
                'severity',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'alarm-info',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active' : {
        'meta_info' : _MetaInfoClass('Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active',
            False, 
            [
            _MetaInfoClassMember('alarm-info', REFERENCE_LIST, 'AlarmInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active.AlarmInfo', 
                [], [], 
                '''                Alarm List
                ''',
                'alarm_info',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History.AlarmInfo' : {
        'meta_info' : _MetaInfoClass('Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History.AlarmInfo',
            False, 
            [
            _MetaInfoClassMember('clear-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm clear time
                ''',
                'clear_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('clear-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm clear time(timestamp format)
                ''',
                'clear_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Alarm description
                ''',
                'description',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'AlarmGroupsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroupsEnum', 
                [], [], 
                '''                Alarm group
                ''',
                'group',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm location
                ''',
                'location',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm set time
                ''',
                'set_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm set time(timestamp format)
                ''',
                'set_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'AlarmSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverityEnum', 
                [], [], 
                '''                Alarm severity
                ''',
                'severity',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'alarm-info',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History' : {
        'meta_info' : _MetaInfoClass('Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History',
            False, 
            [
            _MetaInfoClassMember('alarm-info', REFERENCE_LIST, 'AlarmInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History.AlarmInfo', 
                [], [], 
                '''                Alarm List
                ''',
                'alarm_info',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'history',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed.SuppressedInfo' : {
        'meta_info' : _MetaInfoClass('Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed.SuppressedInfo',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Alarm description
                ''',
                'description',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'AlarmGroupsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroupsEnum', 
                [], [], 
                '''                Alarm group
                ''',
                'group',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm location
                ''',
                'location',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm set time
                ''',
                'set_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm set time(timestamp format)
                ''',
                'set_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'AlarmSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverityEnum', 
                [], [], 
                '''                Alarm severity
                ''',
                'severity',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('suppressed-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm suppressed time
                ''',
                'suppressed_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('suppressed-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm suppressed time(timestamp format)
                ''',
                'suppressed_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'suppressed-info',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed' : {
        'meta_info' : _MetaInfoClass('Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed',
            False, 
            [
            _MetaInfoClassMember('suppressed-info', REFERENCE_LIST, 'SuppressedInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed.SuppressedInfo', 
                [], [], 
                '''                Suppressed Alarm List
                ''',
                'suppressed_info',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'suppressed',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Brief.BriefCard.BriefLocations.BriefLocation' : {
        'meta_info' : _MetaInfoClass('Alarms.Brief.BriefCard.BriefLocations.BriefLocation',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                NodeID of the Location
                ''',
                'node_id',
                'Cisco-IOS-XR-alarmgr-server-oper', True),
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active', 
                [], [], 
                '''                Show the active alarms at this scope.
                ''',
                'active',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('history', REFERENCE_CLASS, 'History' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History', 
                [], [], 
                '''                Show the history alarms at this scope.
                ''',
                'history',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('suppressed', REFERENCE_CLASS, 'Suppressed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed', 
                [], [], 
                '''                Show the suppressed alarms at this scope.
                ''',
                'suppressed',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'brief-location',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Brief.BriefCard.BriefLocations' : {
        'meta_info' : _MetaInfoClass('Alarms.Brief.BriefCard.BriefLocations',
            False, 
            [
            _MetaInfoClassMember('brief-location', REFERENCE_LIST, 'BriefLocation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Brief.BriefCard.BriefLocations.BriefLocation', 
                [], [], 
                '''                Specify a card location for alarms.
                ''',
                'brief_location',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'brief-locations',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Brief.BriefCard' : {
        'meta_info' : _MetaInfoClass('Alarms.Brief.BriefCard',
            False, 
            [
            _MetaInfoClassMember('brief-locations', REFERENCE_CLASS, 'BriefLocations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Brief.BriefCard.BriefLocations', 
                [], [], 
                '''                Table of BriefLocation
                ''',
                'brief_locations',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'brief-card',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Brief.BriefSystem.Active.AlarmInfo' : {
        'meta_info' : _MetaInfoClass('Alarms.Brief.BriefSystem.Active.AlarmInfo',
            False, 
            [
            _MetaInfoClassMember('clear-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm clear time
                ''',
                'clear_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('clear-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm clear time(timestamp format)
                ''',
                'clear_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Alarm description
                ''',
                'description',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'AlarmGroupsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroupsEnum', 
                [], [], 
                '''                Alarm group
                ''',
                'group',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm location
                ''',
                'location',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm set time
                ''',
                'set_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm set time(timestamp format)
                ''',
                'set_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'AlarmSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverityEnum', 
                [], [], 
                '''                Alarm severity
                ''',
                'severity',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'alarm-info',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Brief.BriefSystem.Active' : {
        'meta_info' : _MetaInfoClass('Alarms.Brief.BriefSystem.Active',
            False, 
            [
            _MetaInfoClassMember('alarm-info', REFERENCE_LIST, 'AlarmInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Brief.BriefSystem.Active.AlarmInfo', 
                [], [], 
                '''                Alarm List
                ''',
                'alarm_info',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Brief.BriefSystem.History.AlarmInfo' : {
        'meta_info' : _MetaInfoClass('Alarms.Brief.BriefSystem.History.AlarmInfo',
            False, 
            [
            _MetaInfoClassMember('clear-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm clear time
                ''',
                'clear_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('clear-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm clear time(timestamp format)
                ''',
                'clear_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Alarm description
                ''',
                'description',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'AlarmGroupsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroupsEnum', 
                [], [], 
                '''                Alarm group
                ''',
                'group',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm location
                ''',
                'location',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm set time
                ''',
                'set_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm set time(timestamp format)
                ''',
                'set_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'AlarmSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverityEnum', 
                [], [], 
                '''                Alarm severity
                ''',
                'severity',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'alarm-info',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Brief.BriefSystem.History' : {
        'meta_info' : _MetaInfoClass('Alarms.Brief.BriefSystem.History',
            False, 
            [
            _MetaInfoClassMember('alarm-info', REFERENCE_LIST, 'AlarmInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Brief.BriefSystem.History.AlarmInfo', 
                [], [], 
                '''                Alarm List
                ''',
                'alarm_info',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'history',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Brief.BriefSystem.Suppressed.SuppressedInfo' : {
        'meta_info' : _MetaInfoClass('Alarms.Brief.BriefSystem.Suppressed.SuppressedInfo',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Alarm description
                ''',
                'description',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'AlarmGroupsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroupsEnum', 
                [], [], 
                '''                Alarm group
                ''',
                'group',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Alarm location
                ''',
                'location',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm set time
                ''',
                'set_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('set-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm set time(timestamp format)
                ''',
                'set_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'AlarmSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverityEnum', 
                [], [], 
                '''                Alarm severity
                ''',
                'severity',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('suppressed-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Alarm suppressed time
                ''',
                'suppressed_time',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('suppressed-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm suppressed time(timestamp format)
                ''',
                'suppressed_timestamp',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'suppressed-info',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Brief.BriefSystem.Suppressed' : {
        'meta_info' : _MetaInfoClass('Alarms.Brief.BriefSystem.Suppressed',
            False, 
            [
            _MetaInfoClassMember('suppressed-info', REFERENCE_LIST, 'SuppressedInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Brief.BriefSystem.Suppressed.SuppressedInfo', 
                [], [], 
                '''                Suppressed Alarm List
                ''',
                'suppressed_info',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'suppressed',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Brief.BriefSystem' : {
        'meta_info' : _MetaInfoClass('Alarms.Brief.BriefSystem',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Brief.BriefSystem.Active', 
                [], [], 
                '''                Show the active alarms at this scope.
                ''',
                'active',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('history', REFERENCE_CLASS, 'History' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Brief.BriefSystem.History', 
                [], [], 
                '''                Show the history alarms at this scope.
                ''',
                'history',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('suppressed', REFERENCE_CLASS, 'Suppressed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Brief.BriefSystem.Suppressed', 
                [], [], 
                '''                Show the suppressed alarms at this scope.
                ''',
                'suppressed',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'brief-system',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms.Brief' : {
        'meta_info' : _MetaInfoClass('Alarms.Brief',
            False, 
            [
            _MetaInfoClassMember('brief-card', REFERENCE_CLASS, 'BriefCard' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Brief.BriefCard', 
                [], [], 
                '''                Show brief card scope alarm related data.
                ''',
                'brief_card',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('brief-system', REFERENCE_CLASS, 'BriefSystem' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Brief.BriefSystem', 
                [], [], 
                '''                Show brief system scope alarm related data.
                ''',
                'brief_system',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'brief',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
    'Alarms' : {
        'meta_info' : _MetaInfoClass('Alarms',
            False, 
            [
            _MetaInfoClassMember('brief', REFERENCE_CLASS, 'Brief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Brief', 
                [], [], 
                '''                A set of brief alarm commands.
                ''',
                'brief',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'Alarms.Detail', 
                [], [], 
                '''                A set of detail alarm commands.
                ''',
                'detail',
                'Cisco-IOS-XR-alarmgr-server-oper', False),
            ],
            'Cisco-IOS-XR-alarmgr-server-oper',
            'alarms',
            _yang_ns._namespaces['Cisco-IOS-XR-alarmgr-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper'
        ),
    },
}
_meta_table['Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn']['meta_info'].parent =_meta_table['Alarms.Detail.DetailSystem.Active.AlarmInfo']['meta_info']
_meta_table['Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca']['meta_info'].parent =_meta_table['Alarms.Detail.DetailSystem.Active.AlarmInfo']['meta_info']
_meta_table['Alarms.Detail.DetailSystem.Active.AlarmInfo']['meta_info'].parent =_meta_table['Alarms.Detail.DetailSystem.Active']['meta_info']
_meta_table['Alarms.Detail.DetailSystem.History.AlarmInfo.Otn']['meta_info'].parent =_meta_table['Alarms.Detail.DetailSystem.History.AlarmInfo']['meta_info']
_meta_table['Alarms.Detail.DetailSystem.History.AlarmInfo.Tca']['meta_info'].parent =_meta_table['Alarms.Detail.DetailSystem.History.AlarmInfo']['meta_info']
_meta_table['Alarms.Detail.DetailSystem.History.AlarmInfo']['meta_info'].parent =_meta_table['Alarms.Detail.DetailSystem.History']['meta_info']
_meta_table['Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn']['meta_info'].parent =_meta_table['Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo']['meta_info']
_meta_table['Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo']['meta_info'].parent =_meta_table['Alarms.Detail.DetailSystem.Suppressed']['meta_info']
_meta_table['Alarms.Detail.DetailSystem.Clients.ClientInfo']['meta_info'].parent =_meta_table['Alarms.Detail.DetailSystem.Clients']['meta_info']
_meta_table['Alarms.Detail.DetailSystem.Active']['meta_info'].parent =_meta_table['Alarms.Detail.DetailSystem']['meta_info']
_meta_table['Alarms.Detail.DetailSystem.History']['meta_info'].parent =_meta_table['Alarms.Detail.DetailSystem']['meta_info']
_meta_table['Alarms.Detail.DetailSystem.Suppressed']['meta_info'].parent =_meta_table['Alarms.Detail.DetailSystem']['meta_info']
_meta_table['Alarms.Detail.DetailSystem.Stats']['meta_info'].parent =_meta_table['Alarms.Detail.DetailSystem']['meta_info']
_meta_table['Alarms.Detail.DetailSystem.Clients']['meta_info'].parent =_meta_table['Alarms.Detail.DetailSystem']['meta_info']
_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn']['meta_info'].parent =_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo']['meta_info']
_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca']['meta_info'].parent =_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo']['meta_info']
_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo']['meta_info'].parent =_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active']['meta_info']
_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn']['meta_info'].parent =_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo']['meta_info']
_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca']['meta_info'].parent =_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo']['meta_info']
_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo']['meta_info'].parent =_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History']['meta_info']
_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn']['meta_info'].parent =_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo']['meta_info']
_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo']['meta_info'].parent =_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed']['meta_info']
_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients.ClientInfo']['meta_info'].parent =_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients']['meta_info']
_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active']['meta_info'].parent =_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation']['meta_info']
_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History']['meta_info'].parent =_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation']['meta_info']
_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed']['meta_info'].parent =_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation']['meta_info']
_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats']['meta_info'].parent =_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation']['meta_info']
_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients']['meta_info'].parent =_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation']['meta_info']
_meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation']['meta_info'].parent =_meta_table['Alarms.Detail.DetailCard.DetailLocations']['meta_info']
_meta_table['Alarms.Detail.DetailCard.DetailLocations']['meta_info'].parent =_meta_table['Alarms.Detail.DetailCard']['meta_info']
_meta_table['Alarms.Detail.DetailSystem']['meta_info'].parent =_meta_table['Alarms.Detail']['meta_info']
_meta_table['Alarms.Detail.DetailCard']['meta_info'].parent =_meta_table['Alarms.Detail']['meta_info']
_meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active.AlarmInfo']['meta_info'].parent =_meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active']['meta_info']
_meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History.AlarmInfo']['meta_info'].parent =_meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History']['meta_info']
_meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed.SuppressedInfo']['meta_info'].parent =_meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed']['meta_info']
_meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active']['meta_info'].parent =_meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation']['meta_info']
_meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History']['meta_info'].parent =_meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation']['meta_info']
_meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed']['meta_info'].parent =_meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation']['meta_info']
_meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation']['meta_info'].parent =_meta_table['Alarms.Brief.BriefCard.BriefLocations']['meta_info']
_meta_table['Alarms.Brief.BriefCard.BriefLocations']['meta_info'].parent =_meta_table['Alarms.Brief.BriefCard']['meta_info']
_meta_table['Alarms.Brief.BriefSystem.Active.AlarmInfo']['meta_info'].parent =_meta_table['Alarms.Brief.BriefSystem.Active']['meta_info']
_meta_table['Alarms.Brief.BriefSystem.History.AlarmInfo']['meta_info'].parent =_meta_table['Alarms.Brief.BriefSystem.History']['meta_info']
_meta_table['Alarms.Brief.BriefSystem.Suppressed.SuppressedInfo']['meta_info'].parent =_meta_table['Alarms.Brief.BriefSystem.Suppressed']['meta_info']
_meta_table['Alarms.Brief.BriefSystem.Active']['meta_info'].parent =_meta_table['Alarms.Brief.BriefSystem']['meta_info']
_meta_table['Alarms.Brief.BriefSystem.History']['meta_info'].parent =_meta_table['Alarms.Brief.BriefSystem']['meta_info']
_meta_table['Alarms.Brief.BriefSystem.Suppressed']['meta_info'].parent =_meta_table['Alarms.Brief.BriefSystem']['meta_info']
_meta_table['Alarms.Brief.BriefCard']['meta_info'].parent =_meta_table['Alarms.Brief']['meta_info']
_meta_table['Alarms.Brief.BriefSystem']['meta_info'].parent =_meta_table['Alarms.Brief']['meta_info']
_meta_table['Alarms.Detail']['meta_info'].parent =_meta_table['Alarms']['meta_info']
_meta_table['Alarms.Brief']['meta_info'].parent =_meta_table['Alarms']['meta_info']
