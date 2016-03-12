


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CancelTelemetrySubscriptionRpc' : {
        'meta_info' : _MetaInfoClass('CancelTelemetrySubscriptionRpc',
            False, 
            [
            _MetaInfoClassMember('subscription-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Subscription identifier as returned by the device when
                subscription was requested
                ''',
                'subscription_id',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'cancelTelemetrySubscription',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'EditConfigCommands_Identity' : {
        'meta_info' : _MetaInfoClass('EditConfigCommands_Identity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'edit-config-commands',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'EditConfigRpc.ConfigCommand' : {
        'meta_info' : _MetaInfoClass('EditConfigRpc.ConfigCommand',
            False, 
            [
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Data model path corresponding to the data in the message
                ''',
                'path',
                'openconfig-rpc-api', True),
            _MetaInfoClassMember('command', REFERENCE_IDENTITY_CLASS, 'EditConfigCommands_Identity' , 'ydk.models.openconfig.openconfig_rpc_api', 'EditConfigCommands_Identity', 
                [], [], 
                '''                The type of configuration modification requested for the
                corresponding path.  Note that some commands, such as
                'delete' do not specify any associated data with the
                path.
                ''',
                'command',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('values', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Data encoded using the encoding specified in
                setDataEncoding, or the device's default encoding.  This
                data may be specified by the management system, e.g., when
                sending configuration data, or by the device when returning
                configuration or operational state / telemetry data.
                ''',
                'values',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'config-command',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'EditConfigRpc' : {
        'meta_info' : _MetaInfoClass('EditConfigRpc',
            False, 
            [
            _MetaInfoClassMember('config-command', REFERENCE_LIST, 'ConfigCommand' , 'ydk.models.openconfig.openconfig_rpc_api', 'EditConfigRpc.ConfigCommand', 
                [], [], 
                '''                List of configuration data items, each consisting of the
                data model path, and corresponding data encoded based on
                the requested format
                ''',
                'config_command',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error or information text associated with the return-code
                value.
                ''',
                'message',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Identifier sent in request messages
                ''',
                'request_id',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The request id corresponding to the request
                ''',
                'request_id',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('response-code', REFERENCE_IDENTITY_CLASS, 'OpenconfigRpcResponseTypes_Identity' , 'ydk.models.openconfig.openconfig_rpc_api', 'OpenconfigRpcResponseTypes_Identity', 
                [], [], 
                '''                Numerical code corresponding to the returned message.
                ''',
                'response_code',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'editConfig',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetConfigRpc.Data' : {
        'meta_info' : _MetaInfoClass('GetConfigRpc.Data',
            False, 
            [
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Data model path corresponding to the data in the message
                ''',
                'path',
                'openconfig-rpc-api', True),
            _MetaInfoClassMember('values', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Data encoded using the encoding specified in
                setDataEncoding, or the device's default encoding.  This
                data may be specified by the management system, e.g., when
                sending configuration data, or by the device when returning
                configuration or operational state / telemetry data.
                ''',
                'values',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'data',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetConfigRpc' : {
        'meta_info' : _MetaInfoClass('GetConfigRpc',
            False, 
            [
            _MetaInfoClassMember('data', REFERENCE_LIST, 'Data' , 'ydk.models.openconfig.openconfig_rpc_api', 'GetConfigRpc.Data', 
                [], [], 
                '''                List of configuration data items, each consisting of the
                data model path, and corresponding data encoded based on
                the requested format
                ''',
                'data',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error or information text associated with the return-code
                value.
                ''',
                'message',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('path', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                List of data model paths to retrieve
                ''',
                'path',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Identifier sent in request messages
                ''',
                'request_id',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The request id corresponding to the request
                ''',
                'request_id',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('response-code', REFERENCE_IDENTITY_CLASS, 'OpenconfigRpcResponseTypes_Identity' , 'ydk.models.openconfig.openconfig_rpc_api', 'OpenconfigRpcResponseTypes_Identity', 
                [], [], 
                '''                Numerical code corresponding to the returned message.
                ''',
                'response_code',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'getConfig',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetDataEncodingsRpc' : {
        'meta_info' : _MetaInfoClass('GetDataEncodingsRpc',
            False, 
            [
            _MetaInfoClassMember('encoding', REFERENCE_LIST, 'OpenconfigDataEncodingTypes_Identity' , 'ydk.models.openconfig.openconfig_rpc_api', 'OpenconfigDataEncodingTypes_Identity', 
                [], [], 
                '''                List of identifiers indicating the supported encoding
                schemes
                ''',
                'encoding',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'getDataEncodings',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetModelsRpc.Schema' : {
        'meta_info' : _MetaInfoClass('GetModelsRpc.Schema',
            False, 
            [
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the corresponding YANG module
                ''',
                'model_name',
                'openconfig-rpc-api', True),
            _MetaInfoClassMember('model-data', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Model data, formatted according to the requested format
                (e.g., JSON-Schema, YANG, etc.) and using the requested
                mode (URI, file, etc.)
                ''',
                'model_data',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('model-namespace', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Namespace the model belongs to, whether standard or ad-hoc
                ''',
                'model_namespace',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('model-version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Model version -- for YANG models this should be at least the
                'revision' but could also include a more conventional
                version number
                ''',
                'model_version',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'schema',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetModelsRpc' : {
        'meta_info' : _MetaInfoClass('GetModelsRpc',
            False, 
            [
            _MetaInfoClassMember('request-mode', REFERENCE_IDENTITY_CLASS, 'OpenconfigSchemaModeTypes_Identity' , 'ydk.models.openconfig.openconfig_rpc_api', 'OpenconfigSchemaModeTypes_Identity', 
                [], [], 
                '''                Mode for delivering the schema data
                ''',
                'request_mode',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('schema', REFERENCE_LIST, 'Schema' , 'ydk.models.openconfig.openconfig_rpc_api', 'GetModelsRpc.Schema', 
                [], [], 
                '''                list of supported schemas
                ''',
                'schema',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('schema-format', REFERENCE_IDENTITY_CLASS, 'OpenconfigSchemaFormatTypes_Identity' , 'ydk.models.openconfig.openconfig_rpc_api', 'OpenconfigSchemaFormatTypes_Identity', 
                [], [], 
                '''                Schema format requested, e.g., JSON-Schema, XSD, Proto,
                YANG
                ''',
                'schema_format',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'getModels',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetOperationalRpc.Data' : {
        'meta_info' : _MetaInfoClass('GetOperationalRpc.Data',
            False, 
            [
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Data model path corresponding to the data in the message
                ''',
                'path',
                'openconfig-rpc-api', True),
            _MetaInfoClassMember('values', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Data encoded using the encoding specified in
                setDataEncoding, or the device's default encoding.  This
                data may be specified by the management system, e.g., when
                sending configuration data, or by the device when returning
                configuration or operational state / telemetry data.
                ''',
                'values',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'data',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetOperationalRpc' : {
        'meta_info' : _MetaInfoClass('GetOperationalRpc',
            False, 
            [
            _MetaInfoClassMember('data', REFERENCE_LIST, 'Data' , 'ydk.models.openconfig.openconfig_rpc_api', 'GetOperationalRpc.Data', 
                [], [], 
                '''                List of operational state data items, each consisting of the
                data model path, and corresponding data encoded based on
                the requested format
                ''',
                'data',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error or information text associated with the return-code
                value.
                ''',
                'message',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('oper-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When this is set to true, the device should return only the
                operational state data that is marked as operational: true.
                Otherwise, it should return all operational state date
                (config: false).
                ''',
                'oper_only',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('path', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                List of data model paths to retrieve
                ''',
                'path',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Identifier sent in request messages
                ''',
                'request_id',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The request id corresponding to the request
                ''',
                'request_id',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('response-code', REFERENCE_IDENTITY_CLASS, 'OpenconfigRpcResponseTypes_Identity' , 'ydk.models.openconfig.openconfig_rpc_api', 'OpenconfigRpcResponseTypes_Identity', 
                [], [], 
                '''                Numerical code corresponding to the returned message.
                ''',
                'response_code',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'getOperational',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetTelemetrySubscriptionsRpc.Subscription.Collectors' : {
        'meta_info' : _MetaInfoClass('GetTelemetrySubscriptionsRpc.Subscription.Collectors',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of collector endpoint
                ''',
                'address',
                'openconfig-rpc-api', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of collector endpoint
                        ''',
                        'address',
                        'openconfig-rpc-api', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of collector endpoint
                        ''',
                        'address',
                        'openconfig-rpc-api', True),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Transport protocol port number for the collector
                destination
                ''',
                'port',
                'openconfig-rpc-api', True),
            ],
            'openconfig-rpc-api',
            'collectors',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetTelemetrySubscriptionsRpc.Subscription.Paths' : {
        'meta_info' : _MetaInfoClass('GetTelemetrySubscriptionsRpc.Subscription.Paths',
            False, 
            [
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Data model path of interest
                ''',
                'path',
                'openconfig-rpc-api', True),
            _MetaInfoClassMember('filter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Regular expression to be used in filtering state leaves
                ''',
                'filter',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('max-silent-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum time in ms the target device may go without sending
                a message to the collector. If this time expires with
                suppress-unchanged set, the target device must send an update
                message regardless if the data values have changed.
                ''',
                'max_silent_interval',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('sample-frequency', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time in ms between collection and transmission of the
                specified data to the collector platform. The target device
                will sample the corresponding data (e.g,. a counter) and
                immediately send to the collector destination.
                
                If sample-frequency is set to 0, then the network device
                must emit an update upon every datum change.
                ''',
                'sample_frequency',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('suppress-unchanged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this is set to true, the target device will only send
                updates to the collector upon a change in data value
                ''',
                'suppress_unchanged',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'paths',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetTelemetrySubscriptionsRpc.Subscription' : {
        'meta_info' : _MetaInfoClass('GetTelemetrySubscriptionsRpc.Subscription',
            False, 
            [
            _MetaInfoClassMember('subscription-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Unique id for the subscription on the device.  This is
                generated by the device and returned in a subscription
                request or when listing existing subscriptions
                ''',
                'subscription_id',
                'openconfig-rpc-api', True),
            _MetaInfoClassMember('collectors', REFERENCE_LIST, 'Collectors' , 'ydk.models.openconfig.openconfig_rpc_api', 'GetTelemetrySubscriptionsRpc.Subscription.Collectors', 
                [], [], 
                '''                List of optional collector endpoints to send data for
                this subscription, specified as an ip+port combination.
                If no collector destinations are specified, the collector
                destination is inferred from requester on the rpc channel.
                ''',
                'collectors',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('export-dscp-marking', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
                '''                The DSCP code point value to be set on telemetry messages
                to the collector platform.
                ''',
                'export_dscp_marking',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('paths', REFERENCE_LIST, 'Paths' , 'ydk.models.openconfig.openconfig_rpc_api', 'GetTelemetrySubscriptionsRpc.Subscription.Paths', 
                [], [], 
                '''                List of data model paths, keyed by path name
                ''',
                'paths',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'subscription',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetTelemetrySubscriptionsRpc' : {
        'meta_info' : _MetaInfoClass('GetTelemetrySubscriptionsRpc',
            False, 
            [
            _MetaInfoClassMember('subscription', REFERENCE_LIST, 'Subscription' , 'ydk.models.openconfig.openconfig_rpc_api', 'GetTelemetrySubscriptionsRpc.Subscription', 
                [], [], 
                '''                List of current telemetry subscriptions
                ''',
                'subscription',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'getTelemetrySubscriptions',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'OpenconfigDataEncodingTypes_Identity' : {
        'meta_info' : _MetaInfoClass('OpenconfigDataEncodingTypes_Identity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'openconfig-data-encoding-types',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'OpenconfigRpcResponseTypes_Identity' : {
        'meta_info' : _MetaInfoClass('OpenconfigRpcResponseTypes_Identity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'openconfig-rpc-response-types',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'OpenconfigSchemaFormatTypes_Identity' : {
        'meta_info' : _MetaInfoClass('OpenconfigSchemaFormatTypes_Identity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'openconfig-schema-format-types',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'OpenconfigSchemaModeTypes_Identity' : {
        'meta_info' : _MetaInfoClass('OpenconfigSchemaModeTypes_Identity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'openconfig-schema-mode-types',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'SetDataEncodingRpc' : {
        'meta_info' : _MetaInfoClass('SetDataEncodingRpc',
            False, 
            [
            _MetaInfoClassMember('encoding', REFERENCE_IDENTITY_CLASS, 'OpenconfigDataEncodingTypes_Identity' , 'ydk.models.openconfig.openconfig_rpc_api', 'OpenconfigDataEncodingTypes_Identity', 
                [], [], 
                '''                Identifier for the encoding scheme
                ''',
                'encoding',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'setDataEncoding',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'TelemetrySubscribeRpc.Collectors' : {
        'meta_info' : _MetaInfoClass('TelemetrySubscribeRpc.Collectors',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of collector endpoint
                ''',
                'address',
                'openconfig-rpc-api', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of collector endpoint
                        ''',
                        'address',
                        'openconfig-rpc-api', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of collector endpoint
                        ''',
                        'address',
                        'openconfig-rpc-api', True),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Transport protocol port number for the collector
                destination
                ''',
                'port',
                'openconfig-rpc-api', True),
            ],
            'openconfig-rpc-api',
            'collectors',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'TelemetrySubscribeRpc.Collectors' : {
        'meta_info' : _MetaInfoClass('TelemetrySubscribeRpc.Collectors',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of collector endpoint
                ''',
                'address',
                'openconfig-rpc-api', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of collector endpoint
                        ''',
                        'address',
                        'openconfig-rpc-api', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of collector endpoint
                        ''',
                        'address',
                        'openconfig-rpc-api', True),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Transport protocol port number for the collector
                destination
                ''',
                'port',
                'openconfig-rpc-api', True),
            ],
            'openconfig-rpc-api',
            'collectors',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'TelemetrySubscribeRpc.Paths' : {
        'meta_info' : _MetaInfoClass('TelemetrySubscribeRpc.Paths',
            False, 
            [
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Data model path of interest
                ''',
                'path',
                'openconfig-rpc-api', True),
            _MetaInfoClassMember('filter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Regular expression to be used in filtering state leaves
                ''',
                'filter',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('max-silent-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum time in ms the target device may go without sending
                a message to the collector. If this time expires with
                suppress-unchanged set, the target device must send an update
                message regardless if the data values have changed.
                ''',
                'max_silent_interval',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('sample-frequency', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time in ms between collection and transmission of the
                specified data to the collector platform. The target device
                will sample the corresponding data (e.g,. a counter) and
                immediately send to the collector destination.
                
                If sample-frequency is set to 0, then the network device
                must emit an update upon every datum change.
                ''',
                'sample_frequency',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('suppress-unchanged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this is set to true, the target device will only send
                updates to the collector upon a change in data value
                ''',
                'suppress_unchanged',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'paths',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'TelemetrySubscribeRpc.Paths' : {
        'meta_info' : _MetaInfoClass('TelemetrySubscribeRpc.Paths',
            False, 
            [
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Data model path of interest
                ''',
                'path',
                'openconfig-rpc-api', True),
            _MetaInfoClassMember('filter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Regular expression to be used in filtering state leaves
                ''',
                'filter',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('max-silent-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum time in ms the target device may go without sending
                a message to the collector. If this time expires with
                suppress-unchanged set, the target device must send an update
                message regardless if the data values have changed.
                ''',
                'max_silent_interval',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('sample-frequency', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time in ms between collection and transmission of the
                specified data to the collector platform. The target device
                will sample the corresponding data (e.g,. a counter) and
                immediately send to the collector destination.
                
                If sample-frequency is set to 0, then the network device
                must emit an update upon every datum change.
                ''',
                'sample_frequency',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('suppress-unchanged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this is set to true, the target device will only send
                updates to the collector upon a change in data value
                ''',
                'suppress_unchanged',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'paths',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'TelemetrySubscribeRpc' : {
        'meta_info' : _MetaInfoClass('TelemetrySubscribeRpc',
            False, 
            [
            _MetaInfoClassMember('collectors', REFERENCE_LIST, 'Collectors' , 'ydk.models.openconfig.openconfig_rpc_api', 'TelemetrySubscribeRpc.Collectors', 
                [], [], 
                '''                List of optional collector endpoints to send data for
                this subscription, specified as an ip+port combination.
                If no collector destinations are specified, the collector
                destination is assumed to be the requester on the rpc channel
                ''',
                'collectors',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('collectors', REFERENCE_LIST, 'Collectors' , 'ydk.models.openconfig.openconfig_rpc_api', 'TelemetrySubscribeRpc.Collectors', 
                [], [], 
                '''                List of optional collector endpoints to send data for
                this subscription, specified as an ip+port combination.
                If no collector destinations are specified, the collector
                destination is inferred from requester on the rpc channel.
                ''',
                'collectors',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('export-dscp-marking', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
                '''                The DSCP code point value to be set on telemetry messages
                to the collector platform.
                ''',
                'export_dscp_marking',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('export-dscp-marking', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
                '''                The DSCP code point value to be set on telemetry messages
                to the collector platform.
                ''',
                'export_dscp_marking',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('paths', REFERENCE_LIST, 'Paths' , 'ydk.models.openconfig.openconfig_rpc_api', 'TelemetrySubscribeRpc.Paths', 
                [], [], 
                '''                List of data model paths, keyed by path name
                ''',
                'paths',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('paths', REFERENCE_LIST, 'Paths' , 'ydk.models.openconfig.openconfig_rpc_api', 'TelemetrySubscribeRpc.Paths', 
                [], [], 
                '''                List of data model paths, keyed by path name
                ''',
                'paths',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('subscription-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Unique id for the subscription on the device.  This is
                generated by the device and returned in a subscription
                request or when listing existing subscriptions
                ''',
                'subscription_id',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'telemetrySubscribe',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'DeleteConfig_Identity' : {
        'meta_info' : _MetaInfoClass('DeleteConfig_Identity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'delete-config',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'EncodingJsonIetf_Identity' : {
        'meta_info' : _MetaInfoClass('EncodingJsonIetf_Identity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'encoding-json-ietf',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'EncodingProto3_Identity' : {
        'meta_info' : _MetaInfoClass('EncodingProto3_Identity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'encoding-proto3',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'EncodingXml_Identity' : {
        'meta_info' : _MetaInfoClass('EncodingXml_Identity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'encoding-xml',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'FileMode_Identity' : {
        'meta_info' : _MetaInfoClass('FileMode_Identity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'file-mode',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'JsonSchema_Identity' : {
        'meta_info' : _MetaInfoClass('JsonSchema_Identity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'json-schema',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'ReplaceConfig_Identity' : {
        'meta_info' : _MetaInfoClass('ReplaceConfig_Identity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'replace-config',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'UpdateConfig_Identity' : {
        'meta_info' : _MetaInfoClass('UpdateConfig_Identity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'update-config',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'UriMode_Identity' : {
        'meta_info' : _MetaInfoClass('UriMode_Identity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'uri-mode',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'XsdSchema_Identity' : {
        'meta_info' : _MetaInfoClass('XsdSchema_Identity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'xsd-schema',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'YangSchema_Identity' : {
        'meta_info' : _MetaInfoClass('YangSchema_Identity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'yang-schema',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
}
_meta_table['EditConfigRpc.ConfigCommand']['meta_info'].parent =_meta_table['EditConfigRpc']['meta_info']
_meta_table['GetConfigRpc.Data']['meta_info'].parent =_meta_table['GetConfigRpc']['meta_info']
_meta_table['GetModelsRpc.Schema']['meta_info'].parent =_meta_table['GetModelsRpc']['meta_info']
_meta_table['GetOperationalRpc.Data']['meta_info'].parent =_meta_table['GetOperationalRpc']['meta_info']
_meta_table['GetTelemetrySubscriptionsRpc.Subscription.Collectors']['meta_info'].parent =_meta_table['GetTelemetrySubscriptionsRpc.Subscription']['meta_info']
_meta_table['GetTelemetrySubscriptionsRpc.Subscription.Paths']['meta_info'].parent =_meta_table['GetTelemetrySubscriptionsRpc.Subscription']['meta_info']
_meta_table['GetTelemetrySubscriptionsRpc.Subscription']['meta_info'].parent =_meta_table['GetTelemetrySubscriptionsRpc']['meta_info']
_meta_table['TelemetrySubscribeRpc.Collectors']['meta_info'].parent =_meta_table['TelemetrySubscribeRpc']['meta_info']
_meta_table['TelemetrySubscribeRpc.Collectors']['meta_info'].parent =_meta_table['TelemetrySubscribeRpc']['meta_info']
_meta_table['TelemetrySubscribeRpc.Paths']['meta_info'].parent =_meta_table['TelemetrySubscribeRpc']['meta_info']
_meta_table['TelemetrySubscribeRpc.Paths']['meta_info'].parent =_meta_table['TelemetrySubscribeRpc']['meta_info']
