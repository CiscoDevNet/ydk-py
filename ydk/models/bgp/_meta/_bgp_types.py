


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.models import _yang_ns

_meta_table = {
    'RemovePrivateAsOptionEnum' : _MetaInfoEnum('RemovePrivateAsOptionEnum', 'ydk.models.bgp.bgp_types',
        {
            'ALL':'ALL',
            'REPLACE':'REPLACE',
        }, 'bgp-types', _yang_ns._namespaces['bgp-types']),
    'CommunityTypeEnum' : _MetaInfoEnum('CommunityTypeEnum', 'ydk.models.bgp.bgp_types',
        {
            'STANDARD':'STANDARD',
            'EXTENDED':'EXTENDED',
            'BOTH':'BOTH',
            'NONE':'NONE',
        }, 'bgp-types', _yang_ns._namespaces['bgp-types']),
    'PeerTypeEnum' : _MetaInfoEnum('PeerTypeEnum', 'ydk.models.bgp.bgp_types',
        {
            'INTERNAL':'INTERNAL',
            'EXTERNAL':'EXTERNAL',
        }, 'bgp-types', _yang_ns._namespaces['bgp-types']),
    'BgpSessionDirectionEnum' : _MetaInfoEnum('BgpSessionDirectionEnum', 'ydk.models.bgp.bgp_types',
        {
            'INBOUND':'INBOUND',
            'OUTBOUND':'OUTBOUND',
        }, 'bgp-types', _yang_ns._namespaces['bgp-types']),
    'BgpOriginAttrTypeEnum' : _MetaInfoEnum('BgpOriginAttrTypeEnum', 'ydk.models.bgp.bgp_types',
        {
            'IGP':'IGP',
            'EGP':'EGP',
            'INCOMPLETE':'INCOMPLETE',
        }, 'bgp-types', _yang_ns._namespaces['bgp-types']),
    'AfiSafiTypeIdentity' : {
        'meta_info' : _MetaInfoClass('AfiSafiTypeIdentity',
            False, 
            [
            ],
            'bgp-types',
            'afi-safi-type',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'BgpCapabilityIdentity' : {
        'meta_info' : _MetaInfoClass('BgpCapabilityIdentity',
            False, 
            [
            ],
            'bgp-types',
            'bgp-capability',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'BgpWellKnownStdCommunityIdentity' : {
        'meta_info' : _MetaInfoClass('BgpWellKnownStdCommunityIdentity',
            False, 
            [
            ],
            'bgp-types',
            'bgp-well-known-std-community',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'RouteRefreshIdentity' : {
        'meta_info' : _MetaInfoClass('RouteRefreshIdentity',
            False, 
            [
            ],
            'bgp-types',
            'ROUTE-REFRESH',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'No_Export_SubconfedIdentity' : {
        'meta_info' : _MetaInfoClass('No_Export_SubconfedIdentity',
            False, 
            [
            ],
            'bgp-types',
            'NO_EXPORT_SUBCONFED',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'No_AdvertiseIdentity' : {
        'meta_info' : _MetaInfoClass('No_AdvertiseIdentity',
            False, 
            [
            ],
            'bgp-types',
            'NO_ADVERTISE',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'MpbgpIdentity' : {
        'meta_info' : _MetaInfoClass('MpbgpIdentity',
            False, 
            [
            ],
            'bgp-types',
            'MPBGP',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'Ipv4UnicastIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv4UnicastIdentity',
            False, 
            [
            ],
            'bgp-types',
            'ipv4-unicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'AddPathsIdentity' : {
        'meta_info' : _MetaInfoClass('AddPathsIdentity',
            False, 
            [
            ],
            'bgp-types',
            'ADD-PATHS',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'L3VpnIpv4MulticastIdentity' : {
        'meta_info' : _MetaInfoClass('L3VpnIpv4MulticastIdentity',
            False, 
            [
            ],
            'bgp-types',
            'l3vpn-ipv4-multicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'No_ExportIdentity' : {
        'meta_info' : _MetaInfoClass('No_ExportIdentity',
            False, 
            [
            ],
            'bgp-types',
            'NO_EXPORT',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'L2VpnEvpnIdentity' : {
        'meta_info' : _MetaInfoClass('L2VpnEvpnIdentity',
            False, 
            [
            ],
            'bgp-types',
            'l2vpn-evpn',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'Ipv4LabelledUnicastIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv4LabelledUnicastIdentity',
            False, 
            [
            ],
            'bgp-types',
            'ipv4-labelled-unicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'L3VpnIpv6UnicastIdentity' : {
        'meta_info' : _MetaInfoClass('L3VpnIpv6UnicastIdentity',
            False, 
            [
            ],
            'bgp-types',
            'l3vpn-ipv6-unicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'Ipv6LabelledUnicastIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv6LabelledUnicastIdentity',
            False, 
            [
            ],
            'bgp-types',
            'ipv6-labelled-unicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'L3VpnIpv6MulticastIdentity' : {
        'meta_info' : _MetaInfoClass('L3VpnIpv6MulticastIdentity',
            False, 
            [
            ],
            'bgp-types',
            'l3vpn-ipv6-multicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'GracefulRestartIdentity' : {
        'meta_info' : _MetaInfoClass('GracefulRestartIdentity',
            False, 
            [
            ],
            'bgp-types',
            'GRACEFUL-RESTART',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'Ipv6UnicastIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv6UnicastIdentity',
            False, 
            [
            ],
            'bgp-types',
            'ipv6-unicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'L2VpnVplsIdentity' : {
        'meta_info' : _MetaInfoClass('L2VpnVplsIdentity',
            False, 
            [
            ],
            'bgp-types',
            'l2vpn-vpls',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'Asn32Identity' : {
        'meta_info' : _MetaInfoClass('Asn32Identity',
            False, 
            [
            ],
            'bgp-types',
            'ASN32',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'L3VpnIpv4UnicastIdentity' : {
        'meta_info' : _MetaInfoClass('L3VpnIpv4UnicastIdentity',
            False, 
            [
            ],
            'bgp-types',
            'l3vpn-ipv4-unicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'NopeerIdentity' : {
        'meta_info' : _MetaInfoClass('NopeerIdentity',
            False, 
            [
            ],
            'bgp-types',
            'NOPEER',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'InternetIdentity' : {
        'meta_info' : _MetaInfoClass('InternetIdentity',
            False, 
            [
            ],
            'bgp-types',
            'INTERNET',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
}
