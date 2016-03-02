


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'RemovePrivateAsOption_Enum' : _MetaInfoEnum('RemovePrivateAsOption_Enum', 'ydk.models.bgp.bgp_types',
        {
            'ALL':'ALL',
            'REPLACE':'REPLACE',
        }, 'bgp-types', _yang_ns._namespaces['bgp-types']),
    'CommunityType_Enum' : _MetaInfoEnum('CommunityType_Enum', 'ydk.models.bgp.bgp_types',
        {
            'STANDARD':'STANDARD',
            'EXTENDED':'EXTENDED',
            'BOTH':'BOTH',
            'NONE':'NONE',
        }, 'bgp-types', _yang_ns._namespaces['bgp-types']),
    'PeerType_Enum' : _MetaInfoEnum('PeerType_Enum', 'ydk.models.bgp.bgp_types',
        {
            'INTERNAL':'INTERNAL',
            'EXTERNAL':'EXTERNAL',
        }, 'bgp-types', _yang_ns._namespaces['bgp-types']),
    'BgpSessionDirection_Enum' : _MetaInfoEnum('BgpSessionDirection_Enum', 'ydk.models.bgp.bgp_types',
        {
            'INBOUND':'INBOUND',
            'OUTBOUND':'OUTBOUND',
        }, 'bgp-types', _yang_ns._namespaces['bgp-types']),
    'BgpOriginAttrType_Enum' : _MetaInfoEnum('BgpOriginAttrType_Enum', 'ydk.models.bgp.bgp_types',
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
    'ADDPATHS_Identity' : {
        'meta_info' : _MetaInfoClass('ADDPATHS_Identity',
            False, 
            [
            ],
            'bgp-types',
            'ADD-PATHS',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'ASN32_Identity' : {
        'meta_info' : _MetaInfoClass('ASN32_Identity',
            False, 
            [
            ],
            'bgp-types',
            'ASN32',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'GRACEFULRESTART_Identity' : {
        'meta_info' : _MetaInfoClass('GRACEFULRESTART_Identity',
            False, 
            [
            ],
            'bgp-types',
            'GRACEFUL-RESTART',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'INTERNET_Identity' : {
        'meta_info' : _MetaInfoClass('INTERNET_Identity',
            False, 
            [
            ],
            'bgp-types',
            'INTERNET',
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
    'L2vpnEvpn_Identity' : {
        'meta_info' : _MetaInfoClass('L2vpnEvpn_Identity',
            False, 
            [
            ],
            'bgp-types',
            'l2vpn-evpn',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'L2vpnVpls_Identity' : {
        'meta_info' : _MetaInfoClass('L2vpnVpls_Identity',
            False, 
            [
            ],
            'bgp-types',
            'l2vpn-vpls',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'L3vpnIpv4Multicast_Identity' : {
        'meta_info' : _MetaInfoClass('L3vpnIpv4Multicast_Identity',
            False, 
            [
            ],
            'bgp-types',
            'l3vpn-ipv4-multicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'L3vpnIpv4Unicast_Identity' : {
        'meta_info' : _MetaInfoClass('L3vpnIpv4Unicast_Identity',
            False, 
            [
            ],
            'bgp-types',
            'l3vpn-ipv4-unicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'L3vpnIpv6Multicast_Identity' : {
        'meta_info' : _MetaInfoClass('L3vpnIpv6Multicast_Identity',
            False, 
            [
            ],
            'bgp-types',
            'l3vpn-ipv6-multicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'L3vpnIpv6Unicast_Identity' : {
        'meta_info' : _MetaInfoClass('L3vpnIpv6Unicast_Identity',
            False, 
            [
            ],
            'bgp-types',
            'l3vpn-ipv6-unicast',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'MPBGP_Identity' : {
        'meta_info' : _MetaInfoClass('MPBGP_Identity',
            False, 
            [
            ],
            'bgp-types',
            'MPBGP',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'NOPEER_Identity' : {
        'meta_info' : _MetaInfoClass('NOPEER_Identity',
            False, 
            [
            ],
            'bgp-types',
            'NOPEER',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'NO_ADVERTISE_Identity' : {
        'meta_info' : _MetaInfoClass('NO_ADVERTISE_Identity',
            False, 
            [
            ],
            'bgp-types',
            'NO_ADVERTISE',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'NO_EXPORT_Identity' : {
        'meta_info' : _MetaInfoClass('NO_EXPORT_Identity',
            False, 
            [
            ],
            'bgp-types',
            'NO_EXPORT',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'NO_EXPORT_SUBCONFED_Identity' : {
        'meta_info' : _MetaInfoClass('NO_EXPORT_SUBCONFED_Identity',
            False, 
            [
            ],
            'bgp-types',
            'NO_EXPORT_SUBCONFED',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
    'ROUTEREFRESH_Identity' : {
        'meta_info' : _MetaInfoClass('ROUTEREFRESH_Identity',
            False, 
            [
            ],
            'bgp-types',
            'ROUTE-REFRESH',
            _yang_ns._namespaces['bgp-types'],
        'ydk.models.bgp.bgp_types'
        ),
    },
}
