


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'MplsLdpNbrPasswordEnum' : _MetaInfoEnum('MplsLdpNbrPasswordEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_ldp_cfg_datatypes',
        {
            'disable':'DISABLE',
            'specified':'SPECIFIED',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg-datatypes']),
    'MplsLdpDownstreamOnDemandEnum' : _MetaInfoEnum('MplsLdpDownstreamOnDemandEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_ldp_cfg_datatypes',
        {
            'peer-acl':'PEER_ACL',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg-datatypes']),
    'MplsLdpRouterIdEnum' : _MetaInfoEnum('MplsLdpRouterIdEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_ldp_cfg_datatypes',
        {
            'address':'ADDRESS',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg-datatypes']),
    'MplsLdpafNameEnum' : _MetaInfoEnum('MplsLdpafNameEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_ldp_cfg_datatypes',
        {
            'ipv4':'IPV4',
            'ipv6':'IPV6',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg-datatypes']),
    'MplsLdpSessionProtectionEnum' : _MetaInfoEnum('MplsLdpSessionProtectionEnum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_ldp_cfg_datatypes',
        {
            'all':'ALL',
            'for':'FOR',
            'all-with-duration':'ALL_WITH_DURATION',
            'for-with-duration':'FOR_WITH_DURATION',
            'all-with-forever':'ALL_WITH_FOREVER',
            'for-with-forever':'FOR_WITH_FOREVER',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg-datatypes']),
}
