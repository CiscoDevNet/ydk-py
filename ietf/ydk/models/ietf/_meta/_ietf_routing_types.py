


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'LinkAccessTypeEnum' : _MetaInfoEnum('LinkAccessTypeEnum', 'ydk.models.ietf.ietf_routing_types',
        {
            'broadcast':'broadcast',
            'non-broadcast-multiaccess':'non_broadcast_multiaccess',
            'point-to-multipoint':'point_to_multipoint',
            'point-to-point':'point_to_point',
        }, 'ietf-routing-types', _yang_ns._namespaces['ietf-routing-types']),
    'Ipv6MulticastSourceAddressEnum' : _MetaInfoEnum('Ipv6MulticastSourceAddressEnum', 'ydk.models.ietf.ietf_routing_types',
        {
            '*':'Y__STAR__',
        }, 'ietf-routing-types', _yang_ns._namespaces['ietf-routing-types']),
    'TimerValueMillisecondsEnum' : _MetaInfoEnum('TimerValueMillisecondsEnum', 'ydk.models.ietf.ietf_routing_types',
        {
            'infinity':'infinity',
            'not-set':'not_set',
        }, 'ietf-routing-types', _yang_ns._namespaces['ietf-routing-types']),
    'TimerValueSeconds16Enum' : _MetaInfoEnum('TimerValueSeconds16Enum', 'ydk.models.ietf.ietf_routing_types',
        {
            'infinity':'infinity',
            'not-set':'not_set',
        }, 'ietf-routing-types', _yang_ns._namespaces['ietf-routing-types']),
    'TimerValueSeconds32Enum' : _MetaInfoEnum('TimerValueSeconds32Enum', 'ydk.models.ietf.ietf_routing_types',
        {
            'infinity':'infinity',
            'not-set':'not_set',
        }, 'ietf-routing-types', _yang_ns._namespaces['ietf-routing-types']),
    'Ipv4MulticastSourceAddressEnum' : _MetaInfoEnum('Ipv4MulticastSourceAddressEnum', 'ydk.models.ietf.ietf_routing_types',
        {
            '*':'Y__STAR__',
        }, 'ietf-routing-types', _yang_ns._namespaces['ietf-routing-types']),
    'RouteTargetTypeEnum' : _MetaInfoEnum('RouteTargetTypeEnum', 'ydk.models.ietf.ietf_routing_types',
        {
            'import':'import_',
            'export':'export',
            'both':'both',
        }, 'ietf-routing-types', _yang_ns._namespaces['ietf-routing-types']),
    'MplsLabelSpecialPurposeValueIdentity' : {
        'meta_info' : _MetaInfoClass('MplsLabelSpecialPurposeValueIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'mpls-label-special-purpose-value',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'AddressFamilyIdentity' : {
        'meta_info' : _MetaInfoClass('AddressFamilyIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'address-family',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'MplsTpSectionEidIdentity' : {
        'meta_info' : _MetaInfoClass('MplsTpSectionEidIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'mpls-tp-section-eid',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'MtV6Identity' : {
        'meta_info' : _MetaInfoClass('MtV6Identity',
            False, 
            [
            ],
            'ietf-routing-types',
            'mt-v6',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'HdlcIdentity' : {
        'meta_info' : _MetaInfoClass('HdlcIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'hdlc',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'Ieee802Identity' : {
        'meta_info' : _MetaInfoClass('Ieee802Identity',
            False, 
            [
            ],
            'ietf-routing-types',
            'ieee802',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'MtV4Identity' : {
        'meta_info' : _MetaInfoClass('MtV4Identity',
            False, 
            [
            ],
            'ietf-routing-types',
            'mt-v4',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'IpxIdentity' : {
        'meta_info' : _MetaInfoClass('IpxIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'ipx',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'GalLabelIdentity' : {
        'meta_info' : _MetaInfoClass('GalLabelIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'gal-label',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'OamAlertLabelIdentity' : {
        'meta_info' : _MetaInfoClass('OamAlertLabelIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'oam-alert-label',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'X121Identity' : {
        'meta_info' : _MetaInfoClass('X121Identity',
            False, 
            [
            ],
            'ietf-routing-types',
            'x121',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'ExtensionLabelIdentity' : {
        'meta_info' : _MetaInfoClass('ExtensionLabelIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'extension-label',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'MplsTpPweEidIdentity' : {
        'meta_info' : _MetaInfoClass('MplsTpPweEidIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'mpls-tp-pwe-eid',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'E164NsapIdentity' : {
        'meta_info' : _MetaInfoClass('E164NsapIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'e164-nsap',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'L2VpnIdentity' : {
        'meta_info' : _MetaInfoClass('L2VpnIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'l2vpn',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'DecnetIvIdentity' : {
        'meta_info' : _MetaInfoClass('DecnetIvIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'decnet-iv',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'XtpIdentity' : {
        'meta_info' : _MetaInfoClass('XtpIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'xtp',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'Ipv4ExplicitNullLabelIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv4ExplicitNullLabelIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'ipv4-explicit-null-label',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'XtpV4Identity' : {
        'meta_info' : _MetaInfoClass('XtpV4Identity',
            False, 
            [
            ],
            'ietf-routing-types',
            'xtp-v4',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'XtpV6Identity' : {
        'meta_info' : _MetaInfoClass('XtpV6Identity',
            False, 
            [
            ],
            'ietf-routing-types',
            'xtp-v6',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'FcPortIdentity' : {
        'meta_info' : _MetaInfoClass('FcPortIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'fc-port',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'E163Identity' : {
        'meta_info' : _MetaInfoClass('E163Identity',
            False, 
            [
            ],
            'ietf-routing-types',
            'e163',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'E164Identity' : {
        'meta_info' : _MetaInfoClass('E164Identity',
            False, 
            [
            ],
            'ietf-routing-types',
            'e164',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'Ipv4Identity' : {
        'meta_info' : _MetaInfoClass('Ipv4Identity',
            False, 
            [
            ],
            'ietf-routing-types',
            'ipv4',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'DnsIdentity' : {
        'meta_info' : _MetaInfoClass('DnsIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'dns',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'Ipv6Identity' : {
        'meta_info' : _MetaInfoClass('Ipv6Identity',
            False, 
            [
            ],
            'ietf-routing-types',
            'ipv6',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'MplsTpLspEidIdentity' : {
        'meta_info' : _MetaInfoClass('MplsTpLspEidIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'mpls-tp-lsp-eid',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'ImplicitNullLabelIdentity' : {
        'meta_info' : _MetaInfoClass('ImplicitNullLabelIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'implicit-null-label',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'DnIdentity' : {
        'meta_info' : _MetaInfoClass('DnIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'dn',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'F69Identity' : {
        'meta_info' : _MetaInfoClass('F69Identity',
            False, 
            [
            ],
            'ietf-routing-types',
            'f69',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'FcNodeIdentity' : {
        'meta_info' : _MetaInfoClass('FcNodeIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'fc-node',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'Ipv6ExplicitNullLabelIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv6ExplicitNullLabelIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'ipv6-explicit-null-label',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'EntropyLabelIndicatorIdentity' : {
        'meta_info' : _MetaInfoClass('EntropyLabelIndicatorIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'entropy-label-indicator',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'NsapIdentity' : {
        'meta_info' : _MetaInfoClass('NsapIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'nsap',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'GwidIdentity' : {
        'meta_info' : _MetaInfoClass('GwidIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'gwid',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'VinesIdentity' : {
        'meta_info' : _MetaInfoClass('VinesIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'vines',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'AsNumIdentity' : {
        'meta_info' : _MetaInfoClass('AsNumIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'as-num',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'AppletalkIdentity' : {
        'meta_info' : _MetaInfoClass('AppletalkIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'appletalk',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'RouterAlertLabelIdentity' : {
        'meta_info' : _MetaInfoClass('RouterAlertLabelIdentity',
            False, 
            [
            ],
            'ietf-routing-types',
            'router-alert-label',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
    'Bbn1822Identity' : {
        'meta_info' : _MetaInfoClass('Bbn1822Identity',
            False, 
            [
            ],
            'ietf-routing-types',
            'bbn1822',
            _yang_ns._namespaces['ietf-routing-types'],
        'ydk.models.ietf.ietf_routing_types'
        ),
    },
}
