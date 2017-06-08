


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'LispAddressFamilyIdentity' : {
        'meta_info' : _MetaInfoClass('LispAddressFamilyIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'lisp-address-family',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'Ipv6AfiIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv6AfiIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'ipv6-afi',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'AsNumberAfiIdentity' : {
        'meta_info' : _MetaInfoClass('AsNumberAfiIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'as-number-afi',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'LcafIdentity' : {
        'meta_info' : _MetaInfoClass('LcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'NullAddressLcafIdentity' : {
        'meta_info' : _MetaInfoClass('NullAddressLcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'null-address-lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'ReplicationListLcafIdentity' : {
        'meta_info' : _MetaInfoClass('ReplicationListLcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'replication-list-lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'ExplicitLocatorPathLcafIdentity' : {
        'meta_info' : _MetaInfoClass('ExplicitLocatorPathLcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'explicit-locator-path-lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'NoAddressAfiIdentity' : {
        'meta_info' : _MetaInfoClass('NoAddressAfiIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'no-address-afi',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'EncapsulationFormatLcafIdentity' : {
        'meta_info' : _MetaInfoClass('EncapsulationFormatLcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'encapsulation-format-lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'NatTraversalLcafIdentity' : {
        'meta_info' : _MetaInfoClass('NatTraversalLcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'nat-traversal-lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'KeyValueAddressLcafIdentity' : {
        'meta_info' : _MetaInfoClass('KeyValueAddressLcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'key-value-address-lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'Ipv4AfiIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv4AfiIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'ipv4-afi',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'MulticastInfoLcafIdentity' : {
        'meta_info' : _MetaInfoClass('MulticastInfoLcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'multicast-info-lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'SecurityKeyLcafIdentity' : {
        'meta_info' : _MetaInfoClass('SecurityKeyLcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'security-key-lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'Ipv4PrefixAfiIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv4PrefixAfiIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'ipv4-prefix-afi',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'Ipv6PrefixAfiIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv6PrefixAfiIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'ipv6-prefix-afi',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'AfiListLcafIdentity' : {
        'meta_info' : _MetaInfoClass('AfiListLcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'afi-list-lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'DistinguishedNameAfiIdentity' : {
        'meta_info' : _MetaInfoClass('DistinguishedNameAfiIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'distinguished-name-afi',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'OpaqueKeyLcafIdentity' : {
        'meta_info' : _MetaInfoClass('OpaqueKeyLcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'opaque-key-lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'ApplicationDataLcafIdentity' : {
        'meta_info' : _MetaInfoClass('ApplicationDataLcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'application-data-lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'JsonDataModelLcafIdentity' : {
        'meta_info' : _MetaInfoClass('JsonDataModelLcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'json-data-model-lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'SourceDestKeyLcafIdentity' : {
        'meta_info' : _MetaInfoClass('SourceDestKeyLcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'source-dest-key-lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'MacAfiIdentity' : {
        'meta_info' : _MetaInfoClass('MacAfiIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'mac-afi',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'ServicePathLcafIdentity' : {
        'meta_info' : _MetaInfoClass('ServicePathLcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'service-path-lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'GeoCoordinatesLcafIdentity' : {
        'meta_info' : _MetaInfoClass('GeoCoordinatesLcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'geo-coordinates-lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'InstanceIdLcafIdentity' : {
        'meta_info' : _MetaInfoClass('InstanceIdLcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'instance-id-lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'AsNumberLcafIdentity' : {
        'meta_info' : _MetaInfoClass('AsNumberLcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'as-number-lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
    'NonceLocatorLcafIdentity' : {
        'meta_info' : _MetaInfoClass('NonceLocatorLcafIdentity',
            False, 
            [
            ],
            'ietf-lisp-address-types',
            'nonce-locator-lcaf',
            _yang_ns._namespaces['ietf-lisp-address-types'],
        'ydk.models.ietf.ietf_lisp_address_types'
        ),
    },
}
