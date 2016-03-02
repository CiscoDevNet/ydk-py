


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'Ipv6NdHopLimit_Enum' : _MetaInfoEnum('Ipv6NdHopLimit_Enum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_nd_subscriber_cfg',
        {
            'unspecified':'UNSPECIFIED',
        }, 'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-subscriber-cfg']),
    'Ipv6NdRouterPrefTemplate_Enum' : _MetaInfoEnum('Ipv6NdRouterPrefTemplate_Enum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_nd_subscriber_cfg',
        {
            'high':'HIGH',
            'medium':'MEDIUM',
            'low':'LOW',
        }, 'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-subscriber-cfg']),
}
