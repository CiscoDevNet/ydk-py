


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
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
