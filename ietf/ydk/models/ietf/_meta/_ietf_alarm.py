


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'Alarms.Alarm.DirectionEnum' : _MetaInfoEnum('DirectionEnum', 'ydk.models.ietf.ietf_alarm',
        {
            'NA':'NA',
            'Rx':'Rx',
            'Tx':'Tx',
        }, 'ietf-alarm', _yang_ns._namespaces['ietf-alarm']),
    'Alarms.Alarm.LocationEnum' : _MetaInfoEnum('LocationEnum', 'ydk.models.ietf.ietf_alarm',
        {
            'NA':'NA',
            'nearEnd':'nearEnd',
            'farEnd':'farEnd',
        }, 'ietf-alarm', _yang_ns._namespaces['ietf-alarm']),
    'Alarms.Alarm.PerceivedSeverityEnum' : _MetaInfoEnum('PerceivedSeverityEnum', 'ydk.models.ietf.ietf_alarm',
        {
            'Critical':'Critical',
            'Major':'Major',
            'Minor':'Minor',
            'Warning':'Warning',
            'Cleared':'Cleared',
            'Indeterminate':'Indeterminate',
        }, 'ietf-alarm', _yang_ns._namespaces['ietf-alarm']),
    'Alarms.Alarm.TrendIndicationEnum' : _MetaInfoEnum('TrendIndicationEnum', 'ydk.models.ietf.ietf_alarm',
        {
            'moreSevere':'moreSevere',
            'noChange':'noChange',
            'lessSevere':'lessSevere',
        }, 'ietf-alarm', _yang_ns._namespaces['ietf-alarm']),
    'Alarms.Alarm' : {
        'meta_info' : _MetaInfoClass('Alarms.Alarm',
            False, 
            [
            _MetaInfoClassMember('alarm-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Unique alarm id for the alarm. In most cases this
                will be a combination of entity-type, entity-id,
                probable-cause and severity.
                ''',
                'alarm_id',
                'ietf-alarm', True),
            _MetaInfoClassMember('additional-text', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This parameter, when present, allows a free form
                text description to be reported.
                ''',
                'additional_text',
                'ietf-alarm', False),
            _MetaInfoClassMember('alarm-time', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Time at which the alarm was raised / reported.
                ''',
                'alarm_time',
                'ietf-alarm', False),
            _MetaInfoClassMember('correlated-notifications', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This parameter contains a set of Notification
                identifiers of the correlated alarms.
                ''',
                'correlated_notifications',
                'ietf-alarm', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'DirectionEnum' , 'ydk.models.ietf.ietf_alarm', 'Alarms.Alarm.DirectionEnum', 
                [], [], 
                '''                Direction for which alarm is reported.
                ''',
                'direction',
                'ietf-alarm', False),
            _MetaInfoClassMember('entity-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An identifier for the entity on which the alarm is
                raised. This entity can be in the device, domain
                controllers, element management systems, or
                northbound orchestrators.
                ''',
                'entity_id',
                'ietf-alarm', False),
            _MetaInfoClassMember('entity-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Type of the entity on which the alarm is raised.
                ''',
                'entity_type',
                'ietf-alarm', False),
            _MetaInfoClassMember('event-type', REFERENCE_IDENTITY_CLASS, 'EventTypeIdentity' , 'ydk.models.ietf.ietf_alarm_types', 'EventTypeIdentity', 
                [], [], 
                '''                This parameter categorizes the alarm.
                ''',
                'event_type',
                'ietf-alarm', False),
            _MetaInfoClassMember('location', REFERENCE_ENUM_CLASS, 'LocationEnum' , 'ydk.models.ietf.ietf_alarm', 'Alarms.Alarm.LocationEnum', 
                [], [], 
                '''                Location where the alarm is reported.
                ''',
                'location',
                'ietf-alarm', False),
            _MetaInfoClassMember('notification-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This parameter provides an identifier for the
                notification, which may be carried in the
                correlated notifications parameter of future
                notifications. Notification identifiers must be
                chosen to be unique across all notifications of
                a particular managed object throughout the time
                that correlation is significant.
                ''',
                'notification_identifier',
                'ietf-alarm', False),
            _MetaInfoClassMember('perceived-severity', REFERENCE_ENUM_CLASS, 'PerceivedSeverityEnum' , 'ydk.models.ietf.ietf_alarm', 'Alarms.Alarm.PerceivedSeverityEnum', 
                [], [], 
                '''                This parameter indicates the perceived severity
                level of the alarm.
                ''',
                'perceived_severity',
                'ietf-alarm', False),
            _MetaInfoClassMember('probable-cause', REFERENCE_IDENTITY_CLASS, 'ProbableCauseTypeIdentity' , 'ydk.models.ietf.ietf_alarm_types', 'ProbableCauseTypeIdentity', 
                [], [], 
                '''                This parameter defines further qualification as to
                the probable cause of the alarm.
                ''',
                'probable_cause',
                'ietf-alarm', False),
            _MetaInfoClassMember('service-affecting', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This parameter indicates if the alarm impacts an
                active service. If the alarm is service affecting
                then the value is true. If the alarm does not
                affect the service then the value is false.
                ''',
                'service_affecting',
                'ietf-alarm', False),
            _MetaInfoClassMember('trend-indication', REFERENCE_ENUM_CLASS, 'TrendIndicationEnum' , 'ydk.models.ietf.ietf_alarm', 'Alarms.Alarm.TrendIndicationEnum', 
                [], [], 
                '''                This parameter, when present, specifies the current
                severity trend of the managed entity.
                ''',
                'trend_indication',
                'ietf-alarm', False),
            ],
            'ietf-alarm',
            'alarm',
            _yang_ns._namespaces['ietf-alarm'],
        'ydk.models.ietf.ietf_alarm'
        ),
    },
    'Alarms' : {
        'meta_info' : _MetaInfoClass('Alarms',
            False, 
            [
            _MetaInfoClassMember('alarm', REFERENCE_LIST, 'Alarm' , 'ydk.models.ietf.ietf_alarm', 'Alarms.Alarm', 
                [], [], 
                '''                List of active alarms.
                ''',
                'alarm',
                'ietf-alarm', False),
            ],
            'ietf-alarm',
            'alarms',
            _yang_ns._namespaces['ietf-alarm'],
        'ydk.models.ietf.ietf_alarm'
        ),
    },
}
_meta_table['Alarms.Alarm']['meta_info'].parent =_meta_table['Alarms']['meta_info']
