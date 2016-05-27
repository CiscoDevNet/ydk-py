


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
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
    'AfiSafiType_Identity' : {
        'meta_info' : _MetaInfoClass('AfiSafiType_Identity',
            False, 
            [
            ],
            'bgp-types',
            'afi-safi-type',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'BgpCapability_Identity' : {
        'meta_info' : _MetaInfoClass('BgpCapability_Identity',
            False, 
            [
            ],
            'bgp-types',
            'bgp-capability',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'BgpWellKnownStdCommunity_Identity' : {
        'meta_info' : _MetaInfoClass('BgpWellKnownStdCommunity_Identity',
            False, 
            [
            ],
            'bgp-types',
            'bgp-well-known-std-community',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'L2VpnVpls_Identity' : {
        'meta_info' : _MetaInfoClass('L2VpnVpls_Identity',
            False, 
            [
            ],
            'bgp-types',
            'l2vpn-vpls',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'L3VpnIpv6Unicast_Identity' : {
        'meta_info' : _MetaInfoClass('L3VpnIpv6Unicast_Identity',
            False, 
            [
            ],
            'bgp-types',
            'l3vpn-ipv6-unicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'Internet_Identity' : {
        'meta_info' : _MetaInfoClass('Internet_Identity',
            False, 
            [
            ],
            'bgp-types',
            'INTERNET',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'AddPaths_Identity' : {
        'meta_info' : _MetaInfoClass('AddPaths_Identity',
            False, 
            [
            ],
            'bgp-types',
            'ADD-PATHS',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'GracefulRestart_Identity' : {
        'meta_info' : _MetaInfoClass('GracefulRestart_Identity',
            False, 
            [
            ],
            'bgp-types',
            'GRACEFUL-RESTART',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'Ipv6LabelledUnicast_Identity' : {
        'meta_info' : _MetaInfoClass('Ipv6LabelledUnicast_Identity',
            False, 
            [
            ],
            'bgp-types',
            'ipv6-labelled-unicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'RouteRefresh_Identity' : {
        'meta_info' : _MetaInfoClass('RouteRefresh_Identity',
            False, 
            [
            ],
            'bgp-types',
            'ROUTE-REFRESH',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'No_Export_Subconfed_Identity' : {
        'meta_info' : _MetaInfoClass('No_Export_Subconfed_Identity',
            False, 
            [
            ],
            'bgp-types',
            'NO_EXPORT_SUBCONFED',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'L3VpnIpv4Unicast_Identity' : {
        'meta_info' : _MetaInfoClass('L3VpnIpv4Unicast_Identity',
            False, 
            [
            ],
            'bgp-types',
            'l3vpn-ipv4-unicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'L3VpnIpv6Multicast_Identity' : {
        'meta_info' : _MetaInfoClass('L3VpnIpv6Multicast_Identity',
            False, 
            [
            ],
            'bgp-types',
            'l3vpn-ipv6-multicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'No_Export_Identity' : {
        'meta_info' : _MetaInfoClass('No_Export_Identity',
            False, 
            [
            ],
            'bgp-types',
            'NO_EXPORT',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'No_Advertise_Identity' : {
        'meta_info' : _MetaInfoClass('No_Advertise_Identity',
            False, 
            [
            ],
            'bgp-types',
            'NO_ADVERTISE',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'L3VpnIpv4Multicast_Identity' : {
        'meta_info' : _MetaInfoClass('L3VpnIpv4Multicast_Identity',
            False, 
            [
            ],
            'bgp-types',
            'l3vpn-ipv4-multicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'Asn32_Identity' : {
        'meta_info' : _MetaInfoClass('Asn32_Identity',
            False, 
            [
            ],
            'bgp-types',
            'ASN32',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'Mpbgp_Identity' : {
        'meta_info' : _MetaInfoClass('Mpbgp_Identity',
            False, 
            [
            ],
            'bgp-types',
            'MPBGP',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'Ipv6Unicast_Identity' : {
        'meta_info' : _MetaInfoClass('Ipv6Unicast_Identity',
            False, 
            [
            ],
            'bgp-types',
            'ipv6-unicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'Ipv4LabelledUnicast_Identity' : {
        'meta_info' : _MetaInfoClass('Ipv4LabelledUnicast_Identity',
            False, 
            [
            ],
            'bgp-types',
            'ipv4-labelled-unicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'Ipv4Unicast_Identity' : {
        'meta_info' : _MetaInfoClass('Ipv4Unicast_Identity',
            False, 
            [
            ],
            'bgp-types',
            'ipv4-unicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'Nopeer_Identity' : {
        'meta_info' : _MetaInfoClass('Nopeer_Identity',
            False, 
            [
            ],
            'bgp-types',
            'NOPEER',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'L2VpnEvpn_Identity' : {
        'meta_info' : _MetaInfoClass('L2VpnEvpn_Identity',
            False, 
            [
            ],
            'bgp-types',
            'l2vpn-evpn',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
}
