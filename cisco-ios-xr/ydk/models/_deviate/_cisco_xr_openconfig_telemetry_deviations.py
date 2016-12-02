
from enum import Enum
from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION
from ydk.providers._importer import _yang_ns


_deviation_table = {
    'TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config.exclude_filter' : {
        'deviation_typ' : 'not_supported',
    },
    'TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State.exclude_filter' : {
        'deviation_typ' : 'not_supported',
    },
    'TelemetrySystem.Subscriptions.Dynamic.Subscription' : {
        'deviation_typ' : 'not_supported',
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription.Config.local_source_address' : {
        'deviation_typ' : 'not_supported',
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription.Config.originated_qos_marking' : {
        'deviation_typ' : 'not_supported',
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config.heartbeat_interval' : {
        'deviation_typ' : 'not_supported',
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config.suppress_redundant' : {
        'deviation_typ' : 'not_supported',
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State.heartbeat_interval' : {
        'deviation_typ' : 'not_supported',
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State.suppress_redundant' : {
        'deviation_typ' : 'not_supported',
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription.State.local_source_address' : {
        'deviation_typ' : 'not_supported',
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription.State.originated_qos_marking' : {
        'deviation_typ' : 'not_supported',
    },
}
