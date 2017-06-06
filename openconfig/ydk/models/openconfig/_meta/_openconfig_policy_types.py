


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MatchSetOptionsRestrictedTypeEnum' : _MetaInfoEnum('MatchSetOptionsRestrictedTypeEnum', 'ydk.models.openconfig.openconfig_policy_types',
        {
            'ANY':'ANY',
            'INVERT':'INVERT',
        }, 'openconfig-policy-types', _yang_ns._namespaces['openconfig-policy-types']),
    'MatchSetOptionsTypeEnum' : _MetaInfoEnum('MatchSetOptionsTypeEnum', 'ydk.models.openconfig.openconfig_policy_types',
        {
            'ANY':'ANY',
            'ALL':'ALL',
            'INVERT':'INVERT',
        }, 'openconfig-policy-types', _yang_ns._namespaces['openconfig-policy-types']),
    'AttributeComparisonIdentity' : {
        'meta_info' : _MetaInfoClass('AttributeComparisonIdentity',
            False, 
            [
            ],
            'openconfig-policy-types',
            'attribute-comparison',
            _yang_ns._namespaces['openconfig-policy-types'],
        'ydk.models.openconfig.openconfig_policy_types'
        ),
    },
    'InstallProtocolTypeIdentity' : {
        'meta_info' : _MetaInfoClass('InstallProtocolTypeIdentity',
            False, 
            [
            ],
            'openconfig-policy-types',
            'install-protocol-type',
            _yang_ns._namespaces['openconfig-policy-types'],
        'ydk.models.openconfig.openconfig_policy_types'
        ),
    },
    'AttributeLeIdentity' : {
        'meta_info' : _MetaInfoClass('AttributeLeIdentity',
            False, 
            [
            ],
            'openconfig-policy-types',
            'attribute-le',
            _yang_ns._namespaces['openconfig-policy-types'],
        'ydk.models.openconfig.openconfig_policy_types'
        ),
    },
    'DirectlyConnectedIdentity' : {
        'meta_info' : _MetaInfoClass('DirectlyConnectedIdentity',
            False, 
            [
            ],
            'openconfig-policy-types',
            'DIRECTLY-CONNECTED',
            _yang_ns._namespaces['openconfig-policy-types'],
        'ydk.models.openconfig.openconfig_policy_types'
        ),
    },
    'AttributeEqIdentity' : {
        'meta_info' : _MetaInfoClass('AttributeEqIdentity',
            False, 
            [
            ],
            'openconfig-policy-types',
            'attribute-eq',
            _yang_ns._namespaces['openconfig-policy-types'],
        'ydk.models.openconfig.openconfig_policy_types'
        ),
    },
    'BgpIdentity' : {
        'meta_info' : _MetaInfoClass('BgpIdentity',
            False, 
            [
            ],
            'openconfig-policy-types',
            'BGP',
            _yang_ns._namespaces['openconfig-policy-types'],
        'ydk.models.openconfig.openconfig_policy_types'
        ),
    },
    'AttributeGeIdentity' : {
        'meta_info' : _MetaInfoClass('AttributeGeIdentity',
            False, 
            [
            ],
            'openconfig-policy-types',
            'attribute-ge',
            _yang_ns._namespaces['openconfig-policy-types'],
        'ydk.models.openconfig.openconfig_policy_types'
        ),
    },
    'OspfIdentity' : {
        'meta_info' : _MetaInfoClass('OspfIdentity',
            False, 
            [
            ],
            'openconfig-policy-types',
            'OSPF',
            _yang_ns._namespaces['openconfig-policy-types'],
        'ydk.models.openconfig.openconfig_policy_types'
        ),
    },
    'LocalAggregateIdentity' : {
        'meta_info' : _MetaInfoClass('LocalAggregateIdentity',
            False, 
            [
            ],
            'openconfig-policy-types',
            'LOCAL-AGGREGATE',
            _yang_ns._namespaces['openconfig-policy-types'],
        'ydk.models.openconfig.openconfig_policy_types'
        ),
    },
    'IsisIdentity' : {
        'meta_info' : _MetaInfoClass('IsisIdentity',
            False, 
            [
            ],
            'openconfig-policy-types',
            'ISIS',
            _yang_ns._namespaces['openconfig-policy-types'],
        'ydk.models.openconfig.openconfig_policy_types'
        ),
    },
    'Ospf3Identity' : {
        'meta_info' : _MetaInfoClass('Ospf3Identity',
            False, 
            [
            ],
            'openconfig-policy-types',
            'OSPF3',
            _yang_ns._namespaces['openconfig-policy-types'],
        'ydk.models.openconfig.openconfig_policy_types'
        ),
    },
    'StaticIdentity' : {
        'meta_info' : _MetaInfoClass('StaticIdentity',
            False, 
            [
            ],
            'openconfig-policy-types',
            'STATIC',
            _yang_ns._namespaces['openconfig-policy-types'],
        'ydk.models.openconfig.openconfig_policy_types'
        ),
    },
}
