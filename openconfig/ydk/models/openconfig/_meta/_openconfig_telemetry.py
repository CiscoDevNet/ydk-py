


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'TelemetryStreamProtocolEnum' : _MetaInfoEnum('TelemetryStreamProtocolEnum', 'ydk.models.openconfig.openconfig_telemetry',
        {
            'TCP':'TCP',
            'UDP':'UDP',
        }, 'openconfig-telemetry', _yang_ns._namespaces['openconfig-telemetry']),
    'TelemetrySystem.SensorGroups.SensorGroup.Config' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.SensorGroups.SensorGroup.Config',
            False, 
            [
            _MetaInfoClassMember('sensor-group-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name or identifier for the sensor group itself.
                Will be referenced by other configuration specifying a
                sensor group
                ''',
                'sensor_group_id',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'config',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.SensorGroups.SensorGroup.State' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.SensorGroups.SensorGroup.State',
            False, 
            [
            _MetaInfoClassMember('sensor-group-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name or identifier for the sensor group itself.
                Will be referenced by other configuration specifying a
                sensor group
                ''',
                'sensor_group_id',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'state',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config',
            False, 
            [
            _MetaInfoClassMember('exclude-filter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Filter to exclude certain values out of the state
                values
                ''',
                'exclude_filter',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Path to a section of operational state of interest
                (the sensor).
                ''',
                'path',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'config',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State',
            False, 
            [
            _MetaInfoClassMember('exclude-filter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Filter to exclude certain values out of the state
                values
                ''',
                'exclude_filter',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Path to a section of operational state of interest
                (the sensor).
                ''',
                'path',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'state',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath',
            False, 
            [
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the path of interest
                ''',
                'path',
                'openconfig-telemetry', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config', 
                [], [], 
                '''                Configuration parameters to configure a set
                of data model paths as a sensor grouping
                ''',
                'config',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State', 
                [], [], 
                '''                Configuration parameters to configure a set
                of data model paths as a sensor grouping
                ''',
                'state',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'sensor-path',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.SensorGroups.SensorGroup.SensorPaths' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.SensorGroups.SensorGroup.SensorPaths',
            False, 
            [
            _MetaInfoClassMember('sensor-path', REFERENCE_LIST, 'SensorPath' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath', 
                [], [], 
                '''                List of paths in the model which together
                comprise a sensor grouping. Filters for each path
                to exclude items are also provided.
                ''',
                'sensor_path',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'sensor-paths',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.SensorGroups.SensorGroup' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.SensorGroups.SensorGroup',
            False, 
            [
            _MetaInfoClassMember('sensor-group-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the name or identifier of the
                sensor grouping
                ''',
                'sensor_group_id',
                'openconfig-telemetry', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.SensorGroups.SensorGroup.Config', 
                [], [], 
                '''                Configuration parameters relating to the
                telemetry sensor grouping
                ''',
                'config',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('sensor-paths', REFERENCE_CLASS, 'SensorPaths' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.SensorGroups.SensorGroup.SensorPaths', 
                [], [], 
                '''                Top level container to hold a set of sensor
                paths grouped together
                ''',
                'sensor_paths',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.SensorGroups.SensorGroup.State', 
                [], [], 
                '''                State information relating to the telemetry
                sensor group
                ''',
                'state',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'sensor-group',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.SensorGroups' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.SensorGroups',
            False, 
            [
            _MetaInfoClassMember('sensor-group', REFERENCE_LIST, 'SensorGroup' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.SensorGroups.SensorGroup', 
                [], [], 
                '''                List of telemetry sensory groups on the local
                system, where a sensor grouping represents a resuable
                grouping of multiple paths and exclude filters.
                ''',
                'sensor_group',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'sensor-groups',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.DestinationGroups.DestinationGroup.Config' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.DestinationGroups.DestinationGroup.Config',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Unique identifier for the destination group
                ''',
                'group_id',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'config',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.DestinationGroups.DestinationGroup.State' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.DestinationGroups.DestinationGroup.State',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Unique identifier for destination group
                ''',
                'group_id',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'state',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config',
            False, 
            [
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of the telemetry stream destination
                ''',
                'destination_address',
                'openconfig-telemetry', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the telemetry stream destination
                        ''',
                        'destination_address',
                        'openconfig-telemetry', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the telemetry stream destination
                        ''',
                        'destination_address',
                        'openconfig-telemetry', False),
                ]),
            _MetaInfoClassMember('destination-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Protocol (udp or tcp) port number for the telemetry
                stream destination
                ''',
                'destination_port',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('destination-protocol', REFERENCE_ENUM_CLASS, 'TelemetryStreamProtocolEnum' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetryStreamProtocolEnum', 
                [], [], 
                '''                Protocol used to transmit telemetry data to the
                collector
                ''',
                'destination_protocol',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'config',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.State' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.State',
            False, 
            [
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of the telemetry stream destination
                ''',
                'destination_address',
                'openconfig-telemetry', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the telemetry stream destination
                        ''',
                        'destination_address',
                        'openconfig-telemetry', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the telemetry stream destination
                        ''',
                        'destination_address',
                        'openconfig-telemetry', False),
                ]),
            _MetaInfoClassMember('destination-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Protocol (udp or tcp) port number for the telemetry
                stream destination
                ''',
                'destination_port',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('destination-protocol', REFERENCE_ENUM_CLASS, 'TelemetryStreamProtocolEnum' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetryStreamProtocolEnum', 
                [], [], 
                '''                Protocol used to transmit telemetry data to the
                collector
                ''',
                'destination_protocol',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'state',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination',
            False, 
            [
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Reference to the destination address of the
                telemetry stream
                ''',
                'destination_address',
                'openconfig-telemetry', True, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Reference to the destination address of the
                        telemetry stream
                        ''',
                        'destination_address',
                        'openconfig-telemetry', True),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Reference to the destination address of the
                        telemetry stream
                        ''',
                        'destination_address',
                        'openconfig-telemetry', True),
                ]),
            _MetaInfoClassMember('destination-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Reference to the port number of the stream
                destination
                ''',
                'destination_port',
                'openconfig-telemetry', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config', 
                [], [], 
                '''                Configuration parameters relating to
                telemetry destinations
                ''',
                'config',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.State', 
                [], [], 
                '''                State information associated with
                telemetry destinations
                ''',
                'state',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'destination',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.DestinationGroups.DestinationGroup.Destinations' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.DestinationGroups.DestinationGroup.Destinations',
            False, 
            [
            _MetaInfoClassMember('destination', REFERENCE_LIST, 'Destination' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination', 
                [], [], 
                '''                List of telemetry stream destinations
                ''',
                'destination',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'destinations',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.DestinationGroups.DestinationGroup' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.DestinationGroups.DestinationGroup',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Unique identifier for the destination group
                ''',
                'group_id',
                'openconfig-telemetry', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.DestinationGroups.DestinationGroup.Config', 
                [], [], 
                '''                Top level config container for destination groups
                ''',
                'config',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('destinations', REFERENCE_CLASS, 'Destinations' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.DestinationGroups.DestinationGroup.Destinations', 
                [], [], 
                '''                The destination container lists the destination
                information such as IP address and port of the
                telemetry messages from the network element.
                ''',
                'destinations',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.DestinationGroups.DestinationGroup.State', 
                [], [], 
                '''                Top level state container for destination groups
                ''',
                'state',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'destination-group',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.DestinationGroups' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.DestinationGroups',
            False, 
            [
            _MetaInfoClassMember('destination-group', REFERENCE_LIST, 'DestinationGroup' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.DestinationGroups.DestinationGroup', 
                [], [], 
                '''                List of destination-groups. Destination groups allow the
                reuse of common telemetry destinations across the
                telemetry configuration. An operator references a
                set of destinations via the configurable
                destination-group-identifier.
                
                A destination group may contain one or more telemetry
                destinations
                ''',
                'destination_group',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'destination-groups',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription.Config' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions.Persistent.Subscription.Config',
            False, 
            [
            _MetaInfoClassMember('local-source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IP address which will be the source of packets from
                the device to a telemetry collector destination.
                ''',
                'local_source_address',
                'openconfig-telemetry', False, [
                    _MetaInfoClassMember('local-source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address which will be the source of packets from
                        the device to a telemetry collector destination.
                        ''',
                        'local_source_address',
                        'openconfig-telemetry', False),
                    _MetaInfoClassMember('local-source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address which will be the source of packets from
                        the device to a telemetry collector destination.
                        ''',
                        'local_source_address',
                        'openconfig-telemetry', False),
                ]),
            _MetaInfoClassMember('originated-qos-marking', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                DSCP marking of packets generated by the telemetry
                subsystem on the network device.
                ''',
                'originated_qos_marking',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('subscription-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Identifer of the telemetry subscription.
                Will be used by configuration operations needing
                to modify or delete the telemetry subscription
                ''',
                'subscription_id',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'config',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription.State' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions.Persistent.Subscription.State',
            False, 
            [
            _MetaInfoClassMember('local-source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IP address which will be the source of packets from
                the device to a telemetry collector destination.
                ''',
                'local_source_address',
                'openconfig-telemetry', False, [
                    _MetaInfoClassMember('local-source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address which will be the source of packets from
                        the device to a telemetry collector destination.
                        ''',
                        'local_source_address',
                        'openconfig-telemetry', False),
                    _MetaInfoClassMember('local-source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address which will be the source of packets from
                        the device to a telemetry collector destination.
                        ''',
                        'local_source_address',
                        'openconfig-telemetry', False),
                ]),
            _MetaInfoClassMember('originated-qos-marking', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                DSCP marking of packets generated by the telemetry
                subsystem on the network device.
                ''',
                'originated_qos_marking',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('subscription-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Identifer of the telemetry subscription.
                Will be used by configuration operations needing
                to modify or delete the telemetry subscription
                ''',
                'subscription_id',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'state',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config',
            False, 
            [
            _MetaInfoClassMember('heartbeat-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Maximum time interval in seconds that may pass
                between updates from a device to a telemetry collector.
                If this interval expires, but there is no updated data to
                send (such as if suppress_updates has been configured), the
                device must send a telemetry message to the collector.
                ''',
                'heartbeat_interval',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time in milliseconds between the device's sample of a
                telemetry data source. For example, setting this to 100
                would require the local device to collect the telemetry
                data every 100 milliseconds. There can be latency or jitter
                in transmitting the data, but the sample must occur at
                the specified interval.
                
                The timestamp must reflect the actual time when the data
                was sampled, not simply the previous sample timestamp +
                sample-interval.
                
                If sample-interval is set to 0, the telemetry sensor
                becomes event based. The sensor must then emit data upon
                every change of the underlying data source.
                ''',
                'sample_interval',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('sensor-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the sensor group which is used in the profile
                ''',
                'sensor_group',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('suppress-redundant', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean flag to control suppression of redundant
                telemetry updates to the collector platform. If this flag is
                set to TRUE, then the collector will only send an update at
                the configured interval if a subscribed data value has
                changed. Otherwise, the device will not send an update to
                the collector until expiration of the heartbeat interval.
                ''',
                'suppress_redundant',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'config',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State',
            False, 
            [
            _MetaInfoClassMember('heartbeat-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Maximum time interval in seconds that may pass
                between updates from a device to a telemetry collector.
                If this interval expires, but there is no updated data to
                send (such as if suppress_updates has been configured), the
                device must send a telemetry message to the collector.
                ''',
                'heartbeat_interval',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time in milliseconds between the device's sample of a
                telemetry data source. For example, setting this to 100
                would require the local device to collect the telemetry
                data every 100 milliseconds. There can be latency or jitter
                in transmitting the data, but the sample must occur at
                the specified interval.
                
                The timestamp must reflect the actual time when the data
                was sampled, not simply the previous sample timestamp +
                sample-interval.
                
                If sample-interval is set to 0, the telemetry sensor
                becomes event based. The sensor must then emit data upon
                every change of the underlying data source.
                ''',
                'sample_interval',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('sensor-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the sensor group which is used in the profile
                ''',
                'sensor_group',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('suppress-redundant', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean flag to control suppression of redundant
                telemetry updates to the collector platform. If this flag is
                set to TRUE, then the collector will only send an update at
                the configured interval if a subscribed data value has
                changed. Otherwise, the device will not send an update to
                the collector until expiration of the heartbeat interval.
                ''',
                'suppress_redundant',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'state',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile',
            False, 
            [
            _MetaInfoClassMember('sensor-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the telemetry sensor group name
                ''',
                'sensor_group',
                'openconfig-telemetry', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config', 
                [], [], 
                '''                Configuration parameters related to the sensor
                profile for a subscription
                ''',
                'config',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State', 
                [], [], 
                '''                State information relating to the sensor profile
                for a subscription
                ''',
                'state',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'sensor-profile',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles',
            False, 
            [
            _MetaInfoClassMember('sensor-profile', REFERENCE_LIST, 'SensorProfile' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile', 
                [], [], 
                '''                List of telemetry sensor groups used
                in the subscription
                ''',
                'sensor_profile',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'sensor-profiles',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The destination group id references a reusable
                group of destination addresses and ports for
                the telemetry stream.
                ''',
                'group_id',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'config',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.State' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.State',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The destination group id references a reusable
                group of destination addresses and ports for
                the telemetry stream.
                ''',
                'group_id',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'state',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The destination group id references a configured
                group of destinations for the telemetry stream.
                ''',
                'group_id',
                'openconfig-telemetry', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config', 
                [], [], 
                '''                Configuration parameters related to telemetry
                destinations.
                ''',
                'config',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.State', 
                [], [], 
                '''                State information related to telemetry
                destinations
                ''',
                'state',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'destination-group',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups',
            False, 
            [
            _MetaInfoClassMember('destination-group', REFERENCE_LIST, 'DestinationGroup' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup', 
                [], [], 
                '''                Identifier of the previously defined destination
                group
                ''',
                'destination_group',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'destination-groups',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions.Persistent.Subscription' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions.Persistent.Subscription',
            False, 
            [
            _MetaInfoClassMember('subscription-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Reference to the identifier of the subscription
                itself. The id will be the handle to refer to the
                subscription once created
                ''',
                'subscription_id',
                'openconfig-telemetry', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions.Persistent.Subscription.Config', 
                [], [], 
                '''                Config parameters relating to the telemetry
                subscriptions on the local device
                ''',
                'config',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('destination-groups', REFERENCE_CLASS, 'DestinationGroups' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups', 
                [], [], 
                '''                A subscription may specify destination addresses.
                If the subscription supplies destination addresses,
                the network element will be the initiator of the
                telemetry streaming, sending it to the destination(s)
                specified.
                
                If the destination set is omitted, the subscription
                preconfigures certain elements such as paths and
                sample intervals under a specified subscription ID.
                In this case, the network element will NOT initiate an
                outbound connection for telemetry, but will wait for
                an inbound connection from a network management
                system.
                
                It is expected that the network management system
                connecting to the network element will reference
                the preconfigured subscription ID when initiating
                a subscription.
                ''',
                'destination_groups',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('sensor-profiles', REFERENCE_CLASS, 'SensorProfiles' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles', 
                [], [], 
                '''                A sensor profile is a set of sensor groups or
                individual sensor paths which are associated with a
                telemetry subscription. This is the source of the
                telemetry data for the subscription to send to the
                defined collectors.
                ''',
                'sensor_profiles',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions.Persistent.Subscription.State', 
                [], [], 
                '''                State parameters relating to the telemetry
                subscriptions on the local device
                ''',
                'state',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'subscription',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions.Persistent' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions.Persistent',
            False, 
            [
            _MetaInfoClassMember('subscription', REFERENCE_LIST, 'Subscription' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions.Persistent.Subscription', 
                [], [], 
                '''                List of telemetry subscriptions. A telemetry
                subscription consists of a set of collection
                destinations, stream attributes, and associated paths to
                state information in the model (sensor data)
                ''',
                'subscription',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'persistent',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions.Dynamic.Subscription.State' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions.Dynamic.Subscription.State',
            False, 
            [
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of the telemetry stream destination
                ''',
                'destination_address',
                'openconfig-telemetry', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the telemetry stream destination
                        ''',
                        'destination_address',
                        'openconfig-telemetry', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the telemetry stream destination
                        ''',
                        'destination_address',
                        'openconfig-telemetry', False),
                ]),
            _MetaInfoClassMember('destination-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Protocol (udp or tcp) port number for the telemetry
                stream destination
                ''',
                'destination_port',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('destination-protocol', REFERENCE_ENUM_CLASS, 'TelemetryStreamProtocolEnum' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetryStreamProtocolEnum', 
                [], [], 
                '''                Protocol used to transmit telemetry data to the
                collector
                ''',
                'destination_protocol',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('heartbeat-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Maximum time interval in seconds that may pass
                between updates from a device to a telemetry collector.
                If this interval expires, but there is no updated data to
                send (such as if suppress_updates has been configured), the
                device must send a telemetry message to the collector.
                ''',
                'heartbeat_interval',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('originated-qos-marking', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                DSCP marking of packets generated by the telemetry
                subsystem on the network device.
                ''',
                'originated_qos_marking',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time in milliseconds between the device's sample of a
                telemetry data source. For example, setting this to 100
                would require the local device to collect the telemetry
                data every 100 milliseconds. There can be latency or jitter
                in transmitting the data, but the sample must occur at
                the specified interval.
                
                The timestamp must reflect the actual time when the data
                was sampled, not simply the previous sample timestamp +
                sample-interval.
                
                If sample-interval is set to 0, the telemetry sensor
                becomes event based. The sensor must then emit data upon
                every change of the underlying data source.
                ''',
                'sample_interval',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('subscription-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Identifer of the telemetry subscription.
                Will be used by configuration operations needing
                to modify or delete the telemetry subscription
                ''',
                'subscription_id',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('suppress-redundant', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean flag to control suppression of redundant
                telemetry updates to the collector platform. If this flag is
                set to TRUE, then the collector will only send an update at
                the configured interval if a subscribed data value has
                changed. Otherwise, the device will not send an update to
                the collector until expiration of the heartbeat interval.
                ''',
                'suppress_redundant',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'state',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State',
            False, 
            [
            _MetaInfoClassMember('exclude-filter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Filter to exclude certain values out of the state
                values
                ''',
                'exclude_filter',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Path to a section of operational state of interest
                (the sensor).
                ''',
                'path',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'state',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath',
            False, 
            [
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the path of interest
                ''',
                'path',
                'openconfig-telemetry', True),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State', 
                [], [], 
                '''                State information for a dynamic subscription's
                paths of interest
                ''',
                'state',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'sensor-path',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths',
            False, 
            [
            _MetaInfoClassMember('sensor-path', REFERENCE_LIST, 'SensorPath' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath', 
                [], [], 
                '''                List of paths in the model which together
                comprise a sensor grouping. Filters for each path
                to exclude items are also provided.
                ''',
                'sensor_path',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'sensor-paths',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions.Dynamic.Subscription' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions.Dynamic.Subscription',
            False, 
            [
            _MetaInfoClassMember('subscription-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Reference to the identifier of the subscription
                itself. The id will be the handle to refer to the
                subscription once created
                ''',
                'subscription_id',
                'openconfig-telemetry', True),
            _MetaInfoClassMember('sensor-paths', REFERENCE_CLASS, 'SensorPaths' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths', 
                [], [], 
                '''                Top level container to hold a set of sensor
                paths grouped together
                ''',
                'sensor_paths',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions.Dynamic.Subscription.State', 
                [], [], 
                '''                State information relating to dynamic telemetry
                subscriptions.
                ''',
                'state',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'subscription',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions.Dynamic' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions.Dynamic',
            False, 
            [
            _MetaInfoClassMember('subscription', REFERENCE_LIST, 'Subscription' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions.Dynamic.Subscription', 
                [], [], 
                '''                List representation of telemetry subscriptions that
                are configured via an inline RPC, otherwise known
                as dynamic telemetry subscriptions.
                ''',
                'subscription',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'dynamic',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem.Subscriptions' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem.Subscriptions',
            False, 
            [
            _MetaInfoClassMember('dynamic', REFERENCE_CLASS, 'Dynamic' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions.Dynamic', 
                [], [], 
                '''                This container holds information relating to dynamic
                telemetry subscriptions. A dynamic subscription is
                typically configured through an RPC channel, and does not
                persist across device restarts, or if the RPC channel is
                reset or otherwise torn down.
                ''',
                'dynamic',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('persistent', REFERENCE_CLASS, 'Persistent' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions.Persistent', 
                [], [], 
                '''                This container holds information relating to persistent
                telemetry subscriptions. A persistent telemetry
                subscription is configued locally on the device through
                configuration, and is persistent across device restarts or
                other redundancy changes.
                ''',
                'persistent',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'subscriptions',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
    'TelemetrySystem' : {
        'meta_info' : _MetaInfoClass('TelemetrySystem',
            False, 
            [
            _MetaInfoClassMember('destination-groups', REFERENCE_CLASS, 'DestinationGroups' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.DestinationGroups', 
                [], [], 
                '''                Top level container for destination group configuration
                and state.
                ''',
                'destination_groups',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('sensor-groups', REFERENCE_CLASS, 'SensorGroups' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.SensorGroups', 
                [], [], 
                '''                Top level container for sensor-groups.
                ''',
                'sensor_groups',
                'openconfig-telemetry', False),
            _MetaInfoClassMember('subscriptions', REFERENCE_CLASS, 'Subscriptions' , 'ydk.models.openconfig.openconfig_telemetry', 'TelemetrySystem.Subscriptions', 
                [], [], 
                '''                This container holds information for both persistent
                and dynamic telemetry subscriptions.
                ''',
                'subscriptions',
                'openconfig-telemetry', False),
            ],
            'openconfig-telemetry',
            'telemetry-system',
            _yang_ns._namespaces['openconfig-telemetry'],
        'ydk.models.openconfig.openconfig_telemetry'
        ),
    },
}
_meta_table['TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config']['meta_info'].parent =_meta_table['TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath']['meta_info']
_meta_table['TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State']['meta_info'].parent =_meta_table['TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath']['meta_info']
_meta_table['TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath']['meta_info'].parent =_meta_table['TelemetrySystem.SensorGroups.SensorGroup.SensorPaths']['meta_info']
_meta_table['TelemetrySystem.SensorGroups.SensorGroup.Config']['meta_info'].parent =_meta_table['TelemetrySystem.SensorGroups.SensorGroup']['meta_info']
_meta_table['TelemetrySystem.SensorGroups.SensorGroup.State']['meta_info'].parent =_meta_table['TelemetrySystem.SensorGroups.SensorGroup']['meta_info']
_meta_table['TelemetrySystem.SensorGroups.SensorGroup.SensorPaths']['meta_info'].parent =_meta_table['TelemetrySystem.SensorGroups.SensorGroup']['meta_info']
_meta_table['TelemetrySystem.SensorGroups.SensorGroup']['meta_info'].parent =_meta_table['TelemetrySystem.SensorGroups']['meta_info']
_meta_table['TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config']['meta_info'].parent =_meta_table['TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination']['meta_info']
_meta_table['TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.State']['meta_info'].parent =_meta_table['TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination']['meta_info']
_meta_table['TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination']['meta_info'].parent =_meta_table['TelemetrySystem.DestinationGroups.DestinationGroup.Destinations']['meta_info']
_meta_table['TelemetrySystem.DestinationGroups.DestinationGroup.Config']['meta_info'].parent =_meta_table['TelemetrySystem.DestinationGroups.DestinationGroup']['meta_info']
_meta_table['TelemetrySystem.DestinationGroups.DestinationGroup.State']['meta_info'].parent =_meta_table['TelemetrySystem.DestinationGroups.DestinationGroup']['meta_info']
_meta_table['TelemetrySystem.DestinationGroups.DestinationGroup.Destinations']['meta_info'].parent =_meta_table['TelemetrySystem.DestinationGroups.DestinationGroup']['meta_info']
_meta_table['TelemetrySystem.DestinationGroups.DestinationGroup']['meta_info'].parent =_meta_table['TelemetrySystem.DestinationGroups']['meta_info']
_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config']['meta_info'].parent =_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile']['meta_info']
_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State']['meta_info'].parent =_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile']['meta_info']
_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile']['meta_info'].parent =_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles']['meta_info']
_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config']['meta_info'].parent =_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup']['meta_info']
_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.State']['meta_info'].parent =_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup']['meta_info']
_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup']['meta_info'].parent =_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups']['meta_info']
_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.Config']['meta_info'].parent =_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription']['meta_info']
_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.State']['meta_info'].parent =_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription']['meta_info']
_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles']['meta_info'].parent =_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription']['meta_info']
_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups']['meta_info'].parent =_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription']['meta_info']
_meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription']['meta_info'].parent =_meta_table['TelemetrySystem.Subscriptions.Persistent']['meta_info']
_meta_table['TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State']['meta_info'].parent =_meta_table['TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath']['meta_info']
_meta_table['TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath']['meta_info'].parent =_meta_table['TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths']['meta_info']
_meta_table['TelemetrySystem.Subscriptions.Dynamic.Subscription.State']['meta_info'].parent =_meta_table['TelemetrySystem.Subscriptions.Dynamic.Subscription']['meta_info']
_meta_table['TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths']['meta_info'].parent =_meta_table['TelemetrySystem.Subscriptions.Dynamic.Subscription']['meta_info']
_meta_table['TelemetrySystem.Subscriptions.Dynamic.Subscription']['meta_info'].parent =_meta_table['TelemetrySystem.Subscriptions.Dynamic']['meta_info']
_meta_table['TelemetrySystem.Subscriptions.Persistent']['meta_info'].parent =_meta_table['TelemetrySystem.Subscriptions']['meta_info']
_meta_table['TelemetrySystem.Subscriptions.Dynamic']['meta_info'].parent =_meta_table['TelemetrySystem.Subscriptions']['meta_info']
_meta_table['TelemetrySystem.SensorGroups']['meta_info'].parent =_meta_table['TelemetrySystem']['meta_info']
_meta_table['TelemetrySystem.DestinationGroups']['meta_info'].parent =_meta_table['TelemetrySystem']['meta_info']
_meta_table['TelemetrySystem.Subscriptions']['meta_info'].parent =_meta_table['TelemetrySystem']['meta_info']
