


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'PacketFilterDirectionEnum' : _MetaInfoEnum('PacketFilterDirectionEnum', 'ydk.models.ietf.ietf_dmm_threegpp',
        {
            'preRel7Tft':'preRel7Tft',
            'uplink':'uplink',
            'downlink':'downlink',
            'bidirectional':'bidirectional',
        }, 'ietf-dmm-threegpp', _yang_ns._namespaces['ietf-dmm-threegpp']),
    'ComponentTypeEnumEnum' : _MetaInfoEnum('ComponentTypeEnumEnum', 'ydk.models.ietf.ietf_dmm_threegpp',
        {
            'ipv4RemoteAddress':'ipv4RemoteAddress',
            'ipv4LocalAddress':'ipv4LocalAddress',
            'ipv6RemoteAddress':'ipv6RemoteAddress',
            'ipv6RemoteAddressPrefix':'ipv6RemoteAddressPrefix',
            'ipv6LocalAddressPrefix':'ipv6LocalAddressPrefix',
            'protocolNextHeader':'protocolNextHeader',
            'localPort':'localPort',
            'localPortRange':'localPortRange',
            'reomotePort':'reomotePort',
            'remotePortRange':'remotePortRange',
            'secParamIndex':'secParamIndex',
            'tosTraffClass':'tosTraffClass',
            'flowLabel':'flowLabel',
        }, 'ietf-dmm-threegpp', _yang_ns._namespaces['ietf-dmm-threegpp']),
    'ThreegppMobilityIdentity' : {
        'meta_info' : _MetaInfoClass('ThreegppMobilityIdentity',
            False, 
            [
            ],
            'ietf-dmm-threegpp',
            'threeGPP-mobility',
            _yang_ns._namespaces['ietf-dmm-threegpp'],
        'ydk.models.ietf.ietf_dmm_threegpp'
        ),
    },
    'ThreegppQosProfileParametersIdentity' : {
        'meta_info' : _MetaInfoClass('ThreegppQosProfileParametersIdentity',
            False, 
            [
            ],
            'ietf-dmm-threegpp',
            'threeGPP-qos-profile-parameters',
            _yang_ns._namespaces['ietf-dmm-threegpp'],
        'ydk.models.ietf.ietf_dmm_threegpp'
        ),
    },
    'ThreegppTunnelTypeIdentity' : {
        'meta_info' : _MetaInfoClass('ThreegppTunnelTypeIdentity',
            False, 
            [
            ],
            'ietf-dmm-threegpp',
            'threeGPP-tunnel-type',
            _yang_ns._namespaces['ietf-dmm-threegpp'],
        'ydk.models.ietf.ietf_dmm_threegpp'
        ),
    },
    'ThreegppAccessTypeIdentity' : {
        'meta_info' : _MetaInfoClass('ThreegppAccessTypeIdentity',
            False, 
            [
            ],
            'ietf-dmm-threegpp',
            'threeGPP-access-type',
            _yang_ns._namespaces['ietf-dmm-threegpp'],
        'ydk.models.ietf.ietf_dmm_threegpp'
        ),
    },
    'Gtpv1Identity' : {
        'meta_info' : _MetaInfoClass('Gtpv1Identity',
            False, 
            [
            ],
            'ietf-dmm-threegpp',
            'gtpv1',
            _yang_ns._namespaces['ietf-dmm-threegpp'],
        'ydk.models.ietf.ietf_dmm_threegpp'
        ),
    },
    'Gtpv2Identity' : {
        'meta_info' : _MetaInfoClass('Gtpv2Identity',
            False, 
            [
            ],
            'ietf-dmm-threegpp',
            'gtpv2',
            _yang_ns._namespaces['ietf-dmm-threegpp'],
        'ydk.models.ietf.ietf_dmm_threegpp'
        ),
    },
}
