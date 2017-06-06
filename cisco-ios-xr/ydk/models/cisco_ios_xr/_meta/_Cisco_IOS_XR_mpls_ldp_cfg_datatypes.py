


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MplsLdpRouterIdEnum' : _MetaInfoEnum('MplsLdpRouterIdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg_datatypes',
        {
            'address':'address',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg-datatypes']),
    'MplsLdpafNameEnum' : _MetaInfoEnum('MplsLdpafNameEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg_datatypes',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg-datatypes']),
    'MplsLdpDownstreamOnDemandEnum' : _MetaInfoEnum('MplsLdpDownstreamOnDemandEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg_datatypes',
        {
            'peer-acl':'peer_acl',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg-datatypes']),
    'MplsLdpSessionProtectionEnum' : _MetaInfoEnum('MplsLdpSessionProtectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg_datatypes',
        {
            'all':'all',
            'for':'for_',
            'all-with-duration':'all_with_duration',
            'for-with-duration':'for_with_duration',
            'all-with-forever':'all_with_forever',
            'for-with-forever':'for_with_forever',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg-datatypes']),
    'MplsLdpNbrPasswordEnum' : _MetaInfoEnum('MplsLdpNbrPasswordEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg_datatypes',
        {
            'disable':'disable',
            'specified':'specified',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg-datatypes']),
}
