


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CommunityTypeEnum' : _MetaInfoEnum('CommunityTypeEnum', 'ydk.models.openconfig.openconfig_bgp_types',
        {
            'STANDARD':'STANDARD',
            'EXTENDED':'EXTENDED',
            'BOTH':'BOTH',
            'NONE':'NONE',
        }, 'openconfig-bgp-types', _yang_ns._namespaces['openconfig-bgp-types']),
    'BgpOriginAttrTypeEnum' : _MetaInfoEnum('BgpOriginAttrTypeEnum', 'ydk.models.openconfig.openconfig_bgp_types',
        {
            'IGP':'IGP',
            'EGP':'EGP',
            'INCOMPLETE':'INCOMPLETE',
        }, 'openconfig-bgp-types', _yang_ns._namespaces['openconfig-bgp-types']),
    'BgpSessionDirectionEnum' : _MetaInfoEnum('BgpSessionDirectionEnum', 'ydk.models.openconfig.openconfig_bgp_types',
        {
            'INBOUND':'INBOUND',
            'OUTBOUND':'OUTBOUND',
        }, 'openconfig-bgp-types', _yang_ns._namespaces['openconfig-bgp-types']),
    'RemovePrivateAsOptionEnum' : _MetaInfoEnum('RemovePrivateAsOptionEnum', 'ydk.models.openconfig.openconfig_bgp_types',
        {
            'ALL':'ALL',
            'REPLACE':'REPLACE',
        }, 'openconfig-bgp-types', _yang_ns._namespaces['openconfig-bgp-types']),
    'PeerTypeEnum' : _MetaInfoEnum('PeerTypeEnum', 'ydk.models.openconfig.openconfig_bgp_types',
        {
            'INTERNAL':'INTERNAL',
            'EXTERNAL':'EXTERNAL',
        }, 'openconfig-bgp-types', _yang_ns._namespaces['openconfig-bgp-types']),
    'BgpCapabilityIdentity' : {
        'meta_info' : _MetaInfoClass('BgpCapabilityIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'bgp-capability',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'AfiSafiTypeIdentity' : {
        'meta_info' : _MetaInfoClass('AfiSafiTypeIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'afi-safi-type',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'BgpWellKnownStdCommunityIdentity' : {
        'meta_info' : _MetaInfoClass('BgpWellKnownStdCommunityIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'bgp-well-known-std-community',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'RouteRefreshIdentity' : {
        'meta_info' : _MetaInfoClass('RouteRefreshIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'ROUTE-REFRESH',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'No_ExportIdentity' : {
        'meta_info' : _MetaInfoClass('No_ExportIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'NO_EXPORT',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'No_Export_SubconfedIdentity' : {
        'meta_info' : _MetaInfoClass('No_Export_SubconfedIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'NO_EXPORT_SUBCONFED',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'L3VpnIpv4MulticastIdentity' : {
        'meta_info' : _MetaInfoClass('L3VpnIpv4MulticastIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'l3vpn-ipv4-multicast',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'L2VpnVplsIdentity' : {
        'meta_info' : _MetaInfoClass('L2VpnVplsIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'l2vpn-vpls',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'NopeerIdentity' : {
        'meta_info' : _MetaInfoClass('NopeerIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'NOPEER',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'Ipv6LabelledUnicastIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv6LabelledUnicastIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'ipv6-labelled-unicast',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'GracefulRestartIdentity' : {
        'meta_info' : _MetaInfoClass('GracefulRestartIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'GRACEFUL-RESTART',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'MpbgpIdentity' : {
        'meta_info' : _MetaInfoClass('MpbgpIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'MPBGP',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'Ipv4UnicastIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv4UnicastIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'ipv4-unicast',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'L3VpnIpv6UnicastIdentity' : {
        'meta_info' : _MetaInfoClass('L3VpnIpv6UnicastIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'l3vpn-ipv6-unicast',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'Asn32Identity' : {
        'meta_info' : _MetaInfoClass('Asn32Identity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'ASN32',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'L3VpnIpv4UnicastIdentity' : {
        'meta_info' : _MetaInfoClass('L3VpnIpv4UnicastIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'l3vpn-ipv4-unicast',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'Ipv4LabelledUnicastIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv4LabelledUnicastIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'ipv4-labelled-unicast',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'L3VpnIpv6MulticastIdentity' : {
        'meta_info' : _MetaInfoClass('L3VpnIpv6MulticastIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'l3vpn-ipv6-multicast',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'No_AdvertiseIdentity' : {
        'meta_info' : _MetaInfoClass('No_AdvertiseIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'NO_ADVERTISE',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'AddPathsIdentity' : {
        'meta_info' : _MetaInfoClass('AddPathsIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'ADD-PATHS',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'Ipv6UnicastIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv6UnicastIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'ipv6-unicast',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
    'L2VpnEvpnIdentity' : {
        'meta_info' : _MetaInfoClass('L2VpnEvpnIdentity',
            False, 
            [
            ],
            'openconfig-bgp-types',
            'l2vpn-evpn',
            _yang_ns._namespaces['openconfig-bgp-types'],
        'ydk.models.openconfig.openconfig_bgp_types'
        ),
    },
}
