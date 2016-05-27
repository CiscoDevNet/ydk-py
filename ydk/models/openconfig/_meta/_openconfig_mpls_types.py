


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'TunnelTypeEnum' : _MetaInfoEnum('TunnelTypeEnum', 'ydk.models.openconfig.openconfig_mpls_types',
        {
            'P2P':'P2P',
            'P2MP':'P2MP',
            'MP2MP':'MP2MP',
        }, 'openconfig-mpls-types', _yang_ns._namespaces['openconfig-mpls-types']),
    'MplsLabelEnum' : _MetaInfoEnum('MplsLabelEnum', 'ydk.models.openconfig.openconfig_mpls_types',
        {
            'IPV4_EXPLICIT_NULL':'IPV4_EXPLICIT_NULL',
            'ROUTER_ALERT':'ROUTER_ALERT',
            'IPV6_EXPLICIT_NULL':'IPV6_EXPLICIT_NULL',
            'IMPLICIT_NULL':'IMPLICIT_NULL',
            'ENTROPY_LABEL_INDICATOR':'ENTROPY_LABEL_INDICATOR',
        }, 'openconfig-mpls-types', _yang_ns._namespaces['openconfig-mpls-types']),
    'LspRole_Identity' : {
        'meta_info' : _MetaInfoClass('LspRole_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'lsp-role',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'LspOperStatus_Identity' : {
        'meta_info' : _MetaInfoClass('LspOperStatus_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'lsp-oper-status',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'ProtectionType_Identity' : {
        'meta_info' : _MetaInfoClass('ProtectionType_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'protection-type',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'TunnelAdminStatus_Identity' : {
        'meta_info' : _MetaInfoClass('TunnelAdminStatus_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'tunnel-admin-status',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'NullLabelType_Identity' : {
        'meta_info' : _MetaInfoClass('NullLabelType_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'null-label-type',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'TunnelType_Identity' : {
        'meta_info' : _MetaInfoClass('TunnelType_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'tunnel-type',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'PathSetupProtocol_Identity' : {
        'meta_info' : _MetaInfoClass('PathSetupProtocol_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'path-setup-protocol',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'LinkNodeProtectionRequested_Identity' : {
        'meta_info' : _MetaInfoClass('LinkNodeProtectionRequested_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'link-node-protection-requested',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'P2P_Identity' : {
        'meta_info' : _MetaInfoClass('P2P_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'P2P',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'Transit_Identity' : {
        'meta_info' : _MetaInfoClass('Transit_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'TRANSIT',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'PathSetupRsvp_Identity' : {
        'meta_info' : _MetaInfoClass('PathSetupRsvp_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'path-setup-rsvp',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'Explicit_Identity' : {
        'meta_info' : _MetaInfoClass('Explicit_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'EXPLICIT',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'Egress_Identity' : {
        'meta_info' : _MetaInfoClass('Egress_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'EGRESS',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'Admin_Down_Identity' : {
        'meta_info' : _MetaInfoClass('Admin_Down_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'ADMIN_DOWN',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'LinkProtectionRequested_Identity' : {
        'meta_info' : _MetaInfoClass('LinkProtectionRequested_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'link-protection-requested',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'PathSetupSr_Identity' : {
        'meta_info' : _MetaInfoClass('PathSetupSr_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'path-setup-sr',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'Implicit_Identity' : {
        'meta_info' : _MetaInfoClass('Implicit_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'IMPLICIT',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'Down_Identity' : {
        'meta_info' : _MetaInfoClass('Down_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'DOWN',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'P2Mp_Identity' : {
        'meta_info' : _MetaInfoClass('P2Mp_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'P2MP',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'Ingress_Identity' : {
        'meta_info' : _MetaInfoClass('Ingress_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'INGRESS',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'Unprotected_Identity' : {
        'meta_info' : _MetaInfoClass('Unprotected_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'unprotected',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'Up_Identity' : {
        'meta_info' : _MetaInfoClass('Up_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'UP',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'PathSetupLdp_Identity' : {
        'meta_info' : _MetaInfoClass('PathSetupLdp_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'path-setup-ldp',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
    'Admin_Up_Identity' : {
        'meta_info' : _MetaInfoClass('Admin_Up_Identity',
            False, 
            [
            ],
            'openconfig-mpls-types',
            'ADMIN_UP',
            _yang_ns._namespaces['openconfig-mpls-types'],
        'ydk.models.openconfig.openconfig_mpls_types'
        ),
    },
}
