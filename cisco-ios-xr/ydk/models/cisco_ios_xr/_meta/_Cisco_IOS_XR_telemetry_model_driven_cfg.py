


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'ProtoTypeEnum' : _MetaInfoEnum('ProtoTypeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        {
            'grpc':'GRPC',
            'tcp':'TCP',
        }, 'Cisco-IOS-XR-telemetry-model-driven-cfg', _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg']),
    'EncodeTypeEnum' : _MetaInfoEnum('EncodeTypeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        {
            'gpb':'GPB',
            'self-describing-gpb':'SELF_DESCRIBING_GPB',
            'json':'JSON',
        }, 'Cisco-IOS-XR-telemetry-model-driven-cfg', _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg']),
    'AfEnum' : _MetaInfoEnum('AfEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg',
        {
            'ipv4':'IPV4',
            'ipv6':'IPV6',
        }, 'Cisco-IOS-XR-telemetry-model-driven-cfg', _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg']),
    'TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath',
            False, 
            [
            _MetaInfoClassMember('telemetry-sensor-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sensor Path
                ''',
                'telemetry_sensor_path',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'sensor-path',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths',
            False, 
            [
            _MetaInfoClassMember('sensor-path', REFERENCE_LIST, 'SensorPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath', 
                [], [], 
                '''                Sensor path configuration
                ''',
                'sensor_path',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'sensor-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven.SensorGroups.SensorGroup' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.SensorGroups.SensorGroup',
            False, 
            [
            _MetaInfoClassMember('sensor-group-identifier', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The identifier for this group
                ''',
                'sensor_group_identifier',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Sensor Group
                ''',
                'enable',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('sensor-paths', REFERENCE_CLASS, 'SensorPaths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths', 
                [], [], 
                '''                Sensor path configuration
                ''',
                'sensor_paths',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'sensor-group',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven.SensorGroups' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.SensorGroups',
            False, 
            [
            _MetaInfoClassMember('sensor-group', REFERENCE_LIST, 'SensorGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.SensorGroups.SensorGroup', 
                [], [], 
                '''                Sensor group configuration
                ''',
                'sensor_group',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'sensor-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.SourceAddress' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.SourceAddress',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'AfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'AfEnum', 
                [], [], 
                '''                Address Family type, IPv4|IPv6
                ''',
                'address_family',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source IPv4 address
                ''',
                'ip_address',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPV6 address of the Source
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile',
            False, 
            [
            _MetaInfoClassMember('sensorgroupid', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Reference to the telemetry sensor group name
                ''',
                'sensorgroupid',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            _MetaInfoClassMember('heartbeat-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Heartbeat interval in Seconds
                ''',
                'heartbeat_interval',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sample interval in milliseconds
                ''',
                'sample_interval',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('supress-redundant', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Supress Redundant updates
                ''',
                'supress_redundant',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'sensor-profile',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles',
            False, 
            [
            _MetaInfoClassMember('sensor-profile', REFERENCE_LIST, 'SensorProfile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile', 
                [], [], 
                '''                Associate Sensor Group with Subscription
                ''',
                'sensor_profile',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'sensor-profiles',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile',
            False, 
            [
            _MetaInfoClassMember('destination-id', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Destination Id to associate with
                Subscription
                ''',
                'destination_id',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Associate destintion id with Subscription
                ''',
                'enable',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'destination-profile',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles',
            False, 
            [
            _MetaInfoClassMember('destination-profile', REFERENCE_LIST, 'DestinationProfile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile', 
                [], [], 
                '''                Associate Destination Group with Subscription
                ''',
                'destination_profile',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'destination-profiles',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven.Subscriptions.Subscription' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions.Subscription',
            False, 
            [
            _MetaInfoClassMember('subscription-identifier', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Subscription identifier string
                ''',
                'subscription_identifier',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            _MetaInfoClassMember('destination-profiles', REFERENCE_CLASS, 'DestinationProfiles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles', 
                [], [], 
                '''                Associate Destination Groups with Subscription
                ''',
                'destination_profiles',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('sensor-profiles', REFERENCE_CLASS, 'SensorProfiles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles', 
                [], [], 
                '''                Associate Sensor Groups with Subscription
                ''',
                'sensor_profiles',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.Subscriptions.Subscription.SourceAddress', 
                [], [], 
                '''                Source address to use for streaming telemetry
                information
                ''',
                'source_address',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('source-qos-marking', ATTRIBUTE, 'int' , None, None, 
                [('10', '300')], [], 
                '''                Outgoing DSCP value
                ''',
                'source_qos_marking',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'subscription',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven.Subscriptions' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.Subscriptions',
            False, 
            [
            _MetaInfoClassMember('subscription', REFERENCE_LIST, 'Subscription' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.Subscriptions.Subscription', 
                [], [], 
                '''                Streaming Telemetry Subscription
                ''',
                'subscription',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'subscriptions',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination.Ipv4.Protocol' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination.Ipv4.Protocol',
            False, 
            [
            _MetaInfoClassMember('no-tls', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                no tls
                ''',
                'no_tls',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('protocol', REFERENCE_ENUM_CLASS, 'ProtoTypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'ProtoTypeEnum', 
                [], [], 
                '''                protocol
                ''',
                'protocol',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('tls-hostname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                tls hostname
                ''',
                'tls_hostname',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination.Ipv4' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination.Ipv4',
            False, 
            [
            _MetaInfoClassMember('destination-port', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                destination port
                ''',
                'destination_port',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            _MetaInfoClassMember('ipv4-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True, [
                    _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination IPv4 address
                        ''',
                        'ipv4_address',
                        'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
                    _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination IPv4 address
                        ''',
                        'ipv4_address',
                        'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
                ]),
            _MetaInfoClassMember('encoding', REFERENCE_ENUM_CLASS, 'EncodeTypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'EncodeTypeEnum', 
                [], [], 
                '''                Encoding used to transmit telemetry data to
                the collector
                ''',
                'encoding',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('protocol', REFERENCE_CLASS, 'Protocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination.Ipv4.Protocol', 
                [], [], 
                '''                Transport Protocol used to transmit
                telemetry data to the collector
                ''',
                'protocol',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination.Ipv6.Protocol' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination.Ipv6.Protocol',
            False, 
            [
            _MetaInfoClassMember('no-tls', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                no tls
                ''',
                'no_tls',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('protocol', REFERENCE_ENUM_CLASS, 'ProtoTypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'ProtoTypeEnum', 
                [], [], 
                '''                protocol
                ''',
                'protocol',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('tls-hostname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                tls hostname
                ''',
                'tls_hostname',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination.Ipv6' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination.Ipv6',
            False, 
            [
            _MetaInfoClassMember('destination-port', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                destination port
                ''',
                'destination_port',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                IPV6 address of the destination
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            _MetaInfoClassMember('encoding', REFERENCE_ENUM_CLASS, 'EncodeTypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'EncodeTypeEnum', 
                [], [], 
                '''                Encoding used to transmit telemetry data to
                the collector
                ''',
                'encoding',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('protocol', REFERENCE_CLASS, 'Protocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination.Ipv6.Protocol', 
                [], [], 
                '''                Transport Protocol used to transmit
                telemetry data to the collector
                ''',
                'protocol',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'AfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'AfEnum', 
                [], [], 
                '''                Address Family type, IPv4|IPv6
                ''',
                'address_family',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            _MetaInfoClassMember('ipv4', REFERENCE_LIST, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination.Ipv4', 
                [], [], 
                '''                ipv4
                ''',
                'ipv4',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_LIST, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination.Ipv6', 
                [], [], 
                '''                ipv6
                ''',
                'ipv6',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'destination',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations',
            False, 
            [
            _MetaInfoClassMember('destination', REFERENCE_LIST, 'Destination' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination', 
                [], [], 
                '''                Destination address configuration
                ''',
                'destination',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'destinations',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven.DestinationGroups.DestinationGroup' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.DestinationGroups.DestinationGroup',
            False, 
            [
            _MetaInfoClassMember('destination-id', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                destination group id string
                ''',
                'destination_id',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', True),
            _MetaInfoClassMember('destinations', REFERENCE_CLASS, 'Destinations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations', 
                [], [], 
                '''                Destination configuration
                ''',
                'destinations',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'destination-group',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven.DestinationGroups' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven.DestinationGroups',
            False, 
            [
            _MetaInfoClassMember('destination-group', REFERENCE_LIST, 'DestinationGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.DestinationGroups.DestinationGroup', 
                [], [], 
                '''                Destination Group
                ''',
                'destination_group',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'destination-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
    'TelemetryModelDriven' : {
        'meta_info' : _MetaInfoClass('TelemetryModelDriven',
            False, 
            [
            _MetaInfoClassMember('destination-groups', REFERENCE_CLASS, 'DestinationGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.DestinationGroups', 
                [], [], 
                '''                Destination Group configuration
                ''',
                'destination_groups',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Model Driven Telemetry
                ''',
                'enable',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('sensor-groups', REFERENCE_CLASS, 'SensorGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.SensorGroups', 
                [], [], 
                '''                Sensor group configuration
                ''',
                'sensor_groups',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            _MetaInfoClassMember('subscriptions', REFERENCE_CLASS, 'Subscriptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'TelemetryModelDriven.Subscriptions', 
                [], [], 
                '''                Streaming Telemetry Subscription
                ''',
                'subscriptions',
                'Cisco-IOS-XR-telemetry-model-driven-cfg', False),
            ],
            'Cisco-IOS-XR-telemetry-model-driven-cfg',
            'telemetry-model-driven',
            _yang_ns._namespaces['Cisco-IOS-XR-telemetry-model-driven-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg'
        ),
    },
}
_meta_table['TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath']['meta_info'].parent =_meta_table['TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths']['meta_info']
_meta_table['TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths']['meta_info'].parent =_meta_table['TelemetryModelDriven.SensorGroups.SensorGroup']['meta_info']
_meta_table['TelemetryModelDriven.SensorGroups.SensorGroup']['meta_info'].parent =_meta_table['TelemetryModelDriven.SensorGroups']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.SourceAddress']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions.Subscription']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions.Subscription']['meta_info'].parent =_meta_table['TelemetryModelDriven.Subscriptions']['meta_info']
_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination.Ipv4.Protocol']['meta_info'].parent =_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination.Ipv4']['meta_info']
_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination.Ipv6.Protocol']['meta_info'].parent =_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination.Ipv6']['meta_info']
_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination.Ipv4']['meta_info'].parent =_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination']['meta_info']
_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination.Ipv6']['meta_info'].parent =_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination']['meta_info']
_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations.Destination']['meta_info'].parent =_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations']['meta_info']
_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Destinations']['meta_info'].parent =_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup']['meta_info']
_meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup']['meta_info'].parent =_meta_table['TelemetryModelDriven.DestinationGroups']['meta_info']
_meta_table['TelemetryModelDriven.SensorGroups']['meta_info'].parent =_meta_table['TelemetryModelDriven']['meta_info']
_meta_table['TelemetryModelDriven.Subscriptions']['meta_info'].parent =_meta_table['TelemetryModelDriven']['meta_info']
_meta_table['TelemetryModelDriven.DestinationGroups']['meta_info'].parent =_meta_table['TelemetryModelDriven']['meta_info']
