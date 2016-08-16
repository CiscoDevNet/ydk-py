


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'OpenconfigRpcResponseTypesIdentity' : {
        'meta_info' : _MetaInfoClass('OpenconfigRpcResponseTypesIdentity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'openconfig-rpc-response-types',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'OpenconfigDataEncodingTypesIdentity' : {
        'meta_info' : _MetaInfoClass('OpenconfigDataEncodingTypesIdentity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'openconfig-data-encoding-types',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'EditConfigCommandsIdentity' : {
        'meta_info' : _MetaInfoClass('EditConfigCommandsIdentity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'edit-config-commands',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'OpenconfigSchemaFormatTypesIdentity' : {
        'meta_info' : _MetaInfoClass('OpenconfigSchemaFormatTypesIdentity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'openconfig-schema-format-types',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'OpenconfigSchemaModeTypesIdentity' : {
        'meta_info' : _MetaInfoClass('OpenconfigSchemaModeTypesIdentity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'openconfig-schema-mode-types',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetmodelsRpc.Input' : {
        'meta_info' : _MetaInfoClass('GetmodelsRpc.Input',
            False, 
            [
            _MetaInfoClassMember('schema-format', REFERENCE_IDENTITY_CLASS, 'OpenconfigSchemaFormatTypesIdentity' , 'ydk.models.openconfig.openconfig_rpc_api', 'OpenconfigSchemaFormatTypesIdentity', 
                [], [], 
                '''                Schema format requested, e.g., JSON-Schema, XSD, Proto,
                YANG
                ''',
                'schema_format',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('request-mode', REFERENCE_IDENTITY_CLASS, 'OpenconfigSchemaModeTypesIdentity' , 'ydk.models.openconfig.openconfig_rpc_api', 'OpenconfigSchemaModeTypesIdentity', 
                [], [], 
                '''                Mode for delivering the schema data
                ''',
                'request_mode',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'input',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetmodelsRpc.Output.Schema' : {
        'meta_info' : _MetaInfoClass('GetmodelsRpc.Output.Schema',
            False, 
            [
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the corresponding YANG module
                ''',
                'model_name',
                'openconfig-rpc-api', True),
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
            _MetaInfoClassMember('model-data', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Model data, formatted according to the requested format
                (e.g., JSON-Schema, YANG, etc.) and using the requested
                mode (URI, file, etc.)
                ''',
                'model_data',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'schema',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetmodelsRpc.Output' : {
        'meta_info' : _MetaInfoClass('GetmodelsRpc.Output',
            False, 
            [
            _MetaInfoClassMember('schema', REFERENCE_LIST, 'Schema' , 'ydk.models.openconfig.openconfig_rpc_api', 'GetmodelsRpc.Output.Schema', 
                [], [], 
                '''                list of supported schemas
                ''',
                'schema',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'output',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetmodelsRpc' : {
        'meta_info' : _MetaInfoClass('GetmodelsRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.openconfig.openconfig_rpc_api', 'GetmodelsRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.openconfig.openconfig_rpc_api', 'GetmodelsRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'getModels',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'SetdataencodingRpc.Input' : {
        'meta_info' : _MetaInfoClass('SetdataencodingRpc.Input',
            False, 
            [
            _MetaInfoClassMember('encoding', REFERENCE_IDENTITY_CLASS, 'OpenconfigDataEncodingTypesIdentity' , 'ydk.models.openconfig.openconfig_rpc_api', 'OpenconfigDataEncodingTypesIdentity', 
                [], [], 
                '''                Identifier for the encoding scheme
                ''',
                'encoding',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'input',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'SetdataencodingRpc' : {
        'meta_info' : _MetaInfoClass('SetdataencodingRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.openconfig.openconfig_rpc_api', 'SetdataencodingRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'setDataEncoding',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetdataencodingsRpc.Output' : {
        'meta_info' : _MetaInfoClass('GetdataencodingsRpc.Output',
            False, 
            [
            _MetaInfoClassMember('encoding', REFERENCE_LEAFLIST, 'OpenconfigDataEncodingTypesIdentity' , 'ydk.models.openconfig.openconfig_rpc_api', 'OpenconfigDataEncodingTypesIdentity', 
                [], [], 
                '''                List of identifiers indicating the supported encoding
                schemes
                ''',
                'encoding',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'output',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetdataencodingsRpc' : {
        'meta_info' : _MetaInfoClass('GetdataencodingsRpc',
            False, 
            [
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.openconfig.openconfig_rpc_api', 'GetdataencodingsRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'getDataEncodings',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'EditconfigRpc.Input.ConfigCommand' : {
        'meta_info' : _MetaInfoClass('EditconfigRpc.Input.ConfigCommand',
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
            _MetaInfoClassMember('command', REFERENCE_IDENTITY_CLASS, 'EditConfigCommandsIdentity' , 'ydk.models.openconfig.openconfig_rpc_api', 'EditConfigCommandsIdentity', 
                [], [], 
                '''                The type of configuration modification requested for the
                corresponding path.  Note that some commands, such as
                'delete' do not specify any associated data with the
                path.
                ''',
                'command',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'config-command',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'EditconfigRpc.Input' : {
        'meta_info' : _MetaInfoClass('EditconfigRpc.Input',
            False, 
            [
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Identifier sent in request messages
                ''',
                'request_id',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('config-command', REFERENCE_LIST, 'ConfigCommand' , 'ydk.models.openconfig.openconfig_rpc_api', 'EditconfigRpc.Input.ConfigCommand', 
                [], [], 
                '''                List of configuration data items, each consisting of the
                data model path, and corresponding data encoded based on
                the requested format
                ''',
                'config_command',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'input',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'EditconfigRpc.Output' : {
        'meta_info' : _MetaInfoClass('EditconfigRpc.Output',
            False, 
            [
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The request id corresponding to the request
                ''',
                'request_id',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('response-code', REFERENCE_IDENTITY_CLASS, 'OpenconfigRpcResponseTypesIdentity' , 'ydk.models.openconfig.openconfig_rpc_api', 'OpenconfigRpcResponseTypesIdentity', 
                [], [], 
                '''                Numerical code corresponding to the returned message.
                ''',
                'response_code',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error or information text associated with the return-code
                value.
                ''',
                'message',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'output',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'EditconfigRpc' : {
        'meta_info' : _MetaInfoClass('EditconfigRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.openconfig.openconfig_rpc_api', 'EditconfigRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.openconfig.openconfig_rpc_api', 'EditconfigRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'editConfig',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'TelemetrysubscribeRpc.Input.Collectors' : {
        'meta_info' : _MetaInfoClass('TelemetrysubscribeRpc.Input.Collectors',
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
    'TelemetrysubscribeRpc.Input.Paths' : {
        'meta_info' : _MetaInfoClass('TelemetrysubscribeRpc.Input.Paths',
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
            _MetaInfoClassMember('suppress-unchanged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this is set to true, the target device will only send
                updates to the collector upon a change in data value
                ''',
                'suppress_unchanged',
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
            ],
            'openconfig-rpc-api',
            'paths',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'TelemetrysubscribeRpc.Input' : {
        'meta_info' : _MetaInfoClass('TelemetrysubscribeRpc.Input',
            False, 
            [
            _MetaInfoClassMember('collectors', REFERENCE_LIST, 'Collectors' , 'ydk.models.openconfig.openconfig_rpc_api', 'TelemetrysubscribeRpc.Input.Collectors', 
                [], [], 
                '''                List of optional collector endpoints to send data for
                this subscription, specified as an ip+port combination.
                If no collector destinations are specified, the collector
                destination is assumed to be the requester on the rpc channel
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
            _MetaInfoClassMember('paths', REFERENCE_LIST, 'Paths' , 'ydk.models.openconfig.openconfig_rpc_api', 'TelemetrysubscribeRpc.Input.Paths', 
                [], [], 
                '''                List of data model paths, keyed by path name
                ''',
                'paths',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'input',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'TelemetrysubscribeRpc.Output.Collectors' : {
        'meta_info' : _MetaInfoClass('TelemetrysubscribeRpc.Output.Collectors',
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
    'TelemetrysubscribeRpc.Output.Paths' : {
        'meta_info' : _MetaInfoClass('TelemetrysubscribeRpc.Output.Paths',
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
            _MetaInfoClassMember('suppress-unchanged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this is set to true, the target device will only send
                updates to the collector upon a change in data value
                ''',
                'suppress_unchanged',
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
            ],
            'openconfig-rpc-api',
            'paths',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'TelemetrysubscribeRpc.Output' : {
        'meta_info' : _MetaInfoClass('TelemetrysubscribeRpc.Output',
            False, 
            [
            _MetaInfoClassMember('subscription-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Unique id for the subscription on the device.  This is
                generated by the device and returned in a subscription
                request or when listing existing subscriptions
                ''',
                'subscription_id',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('collectors', REFERENCE_LIST, 'Collectors' , 'ydk.models.openconfig.openconfig_rpc_api', 'TelemetrysubscribeRpc.Output.Collectors', 
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
            _MetaInfoClassMember('paths', REFERENCE_LIST, 'Paths' , 'ydk.models.openconfig.openconfig_rpc_api', 'TelemetrysubscribeRpc.Output.Paths', 
                [], [], 
                '''                List of data model paths, keyed by path name
                ''',
                'paths',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'output',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'TelemetrysubscribeRpc' : {
        'meta_info' : _MetaInfoClass('TelemetrysubscribeRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.openconfig.openconfig_rpc_api', 'TelemetrysubscribeRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.openconfig.openconfig_rpc_api', 'TelemetrysubscribeRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'telemetrySubscribe',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GettelemetrysubscriptionsRpc.Output.Subscription.Collectors' : {
        'meta_info' : _MetaInfoClass('GettelemetrysubscriptionsRpc.Output.Subscription.Collectors',
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
    'GettelemetrysubscriptionsRpc.Output.Subscription.Paths' : {
        'meta_info' : _MetaInfoClass('GettelemetrysubscriptionsRpc.Output.Subscription.Paths',
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
            _MetaInfoClassMember('suppress-unchanged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this is set to true, the target device will only send
                updates to the collector upon a change in data value
                ''',
                'suppress_unchanged',
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
            ],
            'openconfig-rpc-api',
            'paths',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GettelemetrysubscriptionsRpc.Output.Subscription' : {
        'meta_info' : _MetaInfoClass('GettelemetrysubscriptionsRpc.Output.Subscription',
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
            _MetaInfoClassMember('collectors', REFERENCE_LIST, 'Collectors' , 'ydk.models.openconfig.openconfig_rpc_api', 'GettelemetrysubscriptionsRpc.Output.Subscription.Collectors', 
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
            _MetaInfoClassMember('paths', REFERENCE_LIST, 'Paths' , 'ydk.models.openconfig.openconfig_rpc_api', 'GettelemetrysubscriptionsRpc.Output.Subscription.Paths', 
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
    'GettelemetrysubscriptionsRpc.Output' : {
        'meta_info' : _MetaInfoClass('GettelemetrysubscriptionsRpc.Output',
            False, 
            [
            _MetaInfoClassMember('subscription', REFERENCE_LIST, 'Subscription' , 'ydk.models.openconfig.openconfig_rpc_api', 'GettelemetrysubscriptionsRpc.Output.Subscription', 
                [], [], 
                '''                List of current telemetry subscriptions
                ''',
                'subscription',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'output',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GettelemetrysubscriptionsRpc' : {
        'meta_info' : _MetaInfoClass('GettelemetrysubscriptionsRpc',
            False, 
            [
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.openconfig.openconfig_rpc_api', 'GettelemetrysubscriptionsRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'getTelemetrySubscriptions',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'CanceltelemetrysubscriptionRpc.Input' : {
        'meta_info' : _MetaInfoClass('CanceltelemetrysubscriptionRpc.Input',
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
            'input',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'CanceltelemetrysubscriptionRpc' : {
        'meta_info' : _MetaInfoClass('CanceltelemetrysubscriptionRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.openconfig.openconfig_rpc_api', 'CanceltelemetrysubscriptionRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'cancelTelemetrySubscription',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetconfigRpc.Input' : {
        'meta_info' : _MetaInfoClass('GetconfigRpc.Input',
            False, 
            [
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Identifier sent in request messages
                ''',
                'request_id',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('path', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                List of data model paths to retrieve
                ''',
                'path',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'input',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetconfigRpc.Output.Data' : {
        'meta_info' : _MetaInfoClass('GetconfigRpc.Output.Data',
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
    'GetconfigRpc.Output' : {
        'meta_info' : _MetaInfoClass('GetconfigRpc.Output',
            False, 
            [
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The request id corresponding to the request
                ''',
                'request_id',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('response-code', REFERENCE_IDENTITY_CLASS, 'OpenconfigRpcResponseTypesIdentity' , 'ydk.models.openconfig.openconfig_rpc_api', 'OpenconfigRpcResponseTypesIdentity', 
                [], [], 
                '''                Numerical code corresponding to the returned message.
                ''',
                'response_code',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error or information text associated with the return-code
                value.
                ''',
                'message',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('data', REFERENCE_LIST, 'Data' , 'ydk.models.openconfig.openconfig_rpc_api', 'GetconfigRpc.Output.Data', 
                [], [], 
                '''                List of configuration data items, each consisting of the
                data model path, and corresponding data encoded based on
                the requested format
                ''',
                'data',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'output',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetconfigRpc' : {
        'meta_info' : _MetaInfoClass('GetconfigRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.openconfig.openconfig_rpc_api', 'GetconfigRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.openconfig.openconfig_rpc_api', 'GetconfigRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'getConfig',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetoperationalRpc.Input' : {
        'meta_info' : _MetaInfoClass('GetoperationalRpc.Input',
            False, 
            [
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Identifier sent in request messages
                ''',
                'request_id',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('path', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                List of data model paths to retrieve
                ''',
                'path',
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
            ],
            'openconfig-rpc-api',
            'input',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetoperationalRpc.Output.Data' : {
        'meta_info' : _MetaInfoClass('GetoperationalRpc.Output.Data',
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
    'GetoperationalRpc.Output' : {
        'meta_info' : _MetaInfoClass('GetoperationalRpc.Output',
            False, 
            [
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The request id corresponding to the request
                ''',
                'request_id',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('response-code', REFERENCE_IDENTITY_CLASS, 'OpenconfigRpcResponseTypesIdentity' , 'ydk.models.openconfig.openconfig_rpc_api', 'OpenconfigRpcResponseTypesIdentity', 
                [], [], 
                '''                Numerical code corresponding to the returned message.
                ''',
                'response_code',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error or information text associated with the return-code
                value.
                ''',
                'message',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('data', REFERENCE_LIST, 'Data' , 'ydk.models.openconfig.openconfig_rpc_api', 'GetoperationalRpc.Output.Data', 
                [], [], 
                '''                List of operational state data items, each consisting of the
                data model path, and corresponding data encoded based on
                the requested format
                ''',
                'data',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'output',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'GetoperationalRpc' : {
        'meta_info' : _MetaInfoClass('GetoperationalRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.openconfig.openconfig_rpc_api', 'GetoperationalRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'openconfig-rpc-api', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.openconfig.openconfig_rpc_api', 'GetoperationalRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'openconfig-rpc-api', False),
            ],
            'openconfig-rpc-api',
            'getOperational',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'ReplaceConfigIdentity' : {
        'meta_info' : _MetaInfoClass('ReplaceConfigIdentity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'replace-config',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'XsdSchemaIdentity' : {
        'meta_info' : _MetaInfoClass('XsdSchemaIdentity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'xsd-schema',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'YangSchemaIdentity' : {
        'meta_info' : _MetaInfoClass('YangSchemaIdentity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'yang-schema',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'EncodingXmlIdentity' : {
        'meta_info' : _MetaInfoClass('EncodingXmlIdentity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'encoding-xml',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'JsonSchemaIdentity' : {
        'meta_info' : _MetaInfoClass('JsonSchemaIdentity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'json-schema',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'FileModeIdentity' : {
        'meta_info' : _MetaInfoClass('FileModeIdentity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'file-mode',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'DeleteConfigIdentity' : {
        'meta_info' : _MetaInfoClass('DeleteConfigIdentity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'delete-config',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'EncodingJsonIetfIdentity' : {
        'meta_info' : _MetaInfoClass('EncodingJsonIetfIdentity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'encoding-json-ietf',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'EncodingProto3Identity' : {
        'meta_info' : _MetaInfoClass('EncodingProto3Identity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'encoding-proto3',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'UpdateConfigIdentity' : {
        'meta_info' : _MetaInfoClass('UpdateConfigIdentity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'update-config',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
    'UriModeIdentity' : {
        'meta_info' : _MetaInfoClass('UriModeIdentity',
            False, 
            [
            ],
            'openconfig-rpc-api',
            'uri-mode',
            _yang_ns._namespaces['openconfig-rpc-api'],
        'ydk.models.openconfig.openconfig_rpc_api'
        ),
    },
}
_meta_table['GetmodelsRpc.Output.Schema']['meta_info'].parent =_meta_table['GetmodelsRpc.Output']['meta_info']
_meta_table['GetmodelsRpc.Input']['meta_info'].parent =_meta_table['GetmodelsRpc']['meta_info']
_meta_table['GetmodelsRpc.Output']['meta_info'].parent =_meta_table['GetmodelsRpc']['meta_info']
_meta_table['SetdataencodingRpc.Input']['meta_info'].parent =_meta_table['SetdataencodingRpc']['meta_info']
_meta_table['GetdataencodingsRpc.Output']['meta_info'].parent =_meta_table['GetdataencodingsRpc']['meta_info']
_meta_table['EditconfigRpc.Input.ConfigCommand']['meta_info'].parent =_meta_table['EditconfigRpc.Input']['meta_info']
_meta_table['EditconfigRpc.Input']['meta_info'].parent =_meta_table['EditconfigRpc']['meta_info']
_meta_table['EditconfigRpc.Output']['meta_info'].parent =_meta_table['EditconfigRpc']['meta_info']
_meta_table['TelemetrysubscribeRpc.Input.Collectors']['meta_info'].parent =_meta_table['TelemetrysubscribeRpc.Input']['meta_info']
_meta_table['TelemetrysubscribeRpc.Input.Paths']['meta_info'].parent =_meta_table['TelemetrysubscribeRpc.Input']['meta_info']
_meta_table['TelemetrysubscribeRpc.Output.Collectors']['meta_info'].parent =_meta_table['TelemetrysubscribeRpc.Output']['meta_info']
_meta_table['TelemetrysubscribeRpc.Output.Paths']['meta_info'].parent =_meta_table['TelemetrysubscribeRpc.Output']['meta_info']
_meta_table['TelemetrysubscribeRpc.Input']['meta_info'].parent =_meta_table['TelemetrysubscribeRpc']['meta_info']
_meta_table['TelemetrysubscribeRpc.Output']['meta_info'].parent =_meta_table['TelemetrysubscribeRpc']['meta_info']
_meta_table['GettelemetrysubscriptionsRpc.Output.Subscription.Collectors']['meta_info'].parent =_meta_table['GettelemetrysubscriptionsRpc.Output.Subscription']['meta_info']
_meta_table['GettelemetrysubscriptionsRpc.Output.Subscription.Paths']['meta_info'].parent =_meta_table['GettelemetrysubscriptionsRpc.Output.Subscription']['meta_info']
_meta_table['GettelemetrysubscriptionsRpc.Output.Subscription']['meta_info'].parent =_meta_table['GettelemetrysubscriptionsRpc.Output']['meta_info']
_meta_table['GettelemetrysubscriptionsRpc.Output']['meta_info'].parent =_meta_table['GettelemetrysubscriptionsRpc']['meta_info']
_meta_table['CanceltelemetrysubscriptionRpc.Input']['meta_info'].parent =_meta_table['CanceltelemetrysubscriptionRpc']['meta_info']
_meta_table['GetconfigRpc.Output.Data']['meta_info'].parent =_meta_table['GetconfigRpc.Output']['meta_info']
_meta_table['GetconfigRpc.Input']['meta_info'].parent =_meta_table['GetconfigRpc']['meta_info']
_meta_table['GetconfigRpc.Output']['meta_info'].parent =_meta_table['GetconfigRpc']['meta_info']
_meta_table['GetoperationalRpc.Output.Data']['meta_info'].parent =_meta_table['GetoperationalRpc.Output']['meta_info']
_meta_table['GetoperationalRpc.Input']['meta_info'].parent =_meta_table['GetoperationalRpc']['meta_info']
_meta_table['GetoperationalRpc.Output']['meta_info'].parent =_meta_table['GetoperationalRpc']['meta_info']
