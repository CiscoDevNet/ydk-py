


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MplsLabelEnum' : _MetaInfoEnum('MplsLabelEnum', 'ydk.models.openconfig.openconfig_mpls_types',
        {
            'IPV4_EXPLICIT_NULL':'IPV4_EXPLICIT_NULL',
            'ROUTER_ALERT':'ROUTER_ALERT',
            'IPV6_EXPLICIT_NULL':'IPV6_EXPLICIT_NULL',
            'IMPLICIT_NULL':'IMPLICIT_NULL',
            'ENTROPY_LABEL_INDICATOR':'ENTROPY_LABEL_INDICATOR',
        }, 'openconfig-mpls-types', _yang_ns._namespaces['openconfig-mpls-types']),
    'TunnelTypeEnum' : _MetaInfoEnum('TunnelTypeEnum', 'ydk.models.openconfig.openconfig_mpls_types',
        {
            'P2P':'P2P',
            'P2MP':'P2MP',
            'MP2MP':'MP2MP',
        }, 'openconfig-mpls-types', _yang_ns._namespaces['openconfig-mpls-types']),
    'TunnelAdminStatusIdentity' : {
        'meta_info' : _MetaInfoClass('TunnelAdminStatusIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'tunnel-admin-status',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'LspOperStatusIdentity' : {
        'meta_info' : _MetaInfoClass('LspOperStatusIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'lsp-oper-status',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'PathSetupProtocolIdentity' : {
        'meta_info' : _MetaInfoClass('PathSetupProtocolIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'path-setup-protocol',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'NullLabelTypeIdentity' : {
        'meta_info' : _MetaInfoClass('NullLabelTypeIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'null-label-type',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'LspRoleIdentity' : {
        'meta_info' : _MetaInfoClass('LspRoleIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'lsp-role',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'ProtectionTypeIdentity' : {
        'meta_info' : _MetaInfoClass('ProtectionTypeIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'protection-type',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'TunnelTypeIdentity' : {
        'meta_info' : _MetaInfoClass('TunnelTypeIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'tunnel-type',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'P2PIdentity' : {
        'meta_info' : _MetaInfoClass('P2PIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'P2P',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'UnprotectedIdentity' : {
        'meta_info' : _MetaInfoClass('UnprotectedIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'unprotected',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'Admin_UpIdentity' : {
        'meta_info' : _MetaInfoClass('Admin_UpIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'ADMIN_UP',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'DownIdentity' : {
        'meta_info' : _MetaInfoClass('DownIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'DOWN',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'PathSetupLdpIdentity' : {
        'meta_info' : _MetaInfoClass('PathSetupLdpIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'path-setup-ldp',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'UpIdentity' : {
        'meta_info' : _MetaInfoClass('UpIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'UP',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'TransitIdentity' : {
        'meta_info' : _MetaInfoClass('TransitIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'TRANSIT',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'LinkNodeProtectionRequestedIdentity' : {
        'meta_info' : _MetaInfoClass('LinkNodeProtectionRequestedIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'link-node-protection-requested',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'EgressIdentity' : {
        'meta_info' : _MetaInfoClass('EgressIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'EGRESS',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'LinkProtectionRequestedIdentity' : {
        'meta_info' : _MetaInfoClass('LinkProtectionRequestedIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'link-protection-requested',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'ExplicitIdentity' : {
        'meta_info' : _MetaInfoClass('ExplicitIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'EXPLICIT',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'PathSetupSrIdentity' : {
        'meta_info' : _MetaInfoClass('PathSetupSrIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'path-setup-sr',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'Admin_DownIdentity' : {
        'meta_info' : _MetaInfoClass('Admin_DownIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'ADMIN_DOWN',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'IngressIdentity' : {
        'meta_info' : _MetaInfoClass('IngressIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'INGRESS',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'ImplicitIdentity' : {
        'meta_info' : _MetaInfoClass('ImplicitIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'IMPLICIT',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'PathSetupRsvpIdentity' : {
        'meta_info' : _MetaInfoClass('PathSetupRsvpIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'path-setup-rsvp',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'P2MpIdentity' : {
        'meta_info' : _MetaInfoClass('P2MpIdentity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'P2MP',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
}
