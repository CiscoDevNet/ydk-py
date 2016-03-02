


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'Ipv6SelfPing_Enum' : _MetaInfoEnum('Ipv6SelfPing_Enum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_ma_cfg',
        {
            'disabled':'DISABLED',
            'enabled':'ENABLED',
        }, 'Cisco-IOS-XR-ipv6-ma-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg']),
    'Ipv6Qppb_Enum' : _MetaInfoEnum('Ipv6Qppb_Enum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_ma_cfg',
        {
            'none':'NONE',
            'ip-precedence':'IP_PRECEDENCE',
            'qos-group':'QOS_GROUP',
            'both':'BOTH',
        }, 'Cisco-IOS-XR-ipv6-ma-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg']),
    'Ipv6DefaultPing_Enum' : _MetaInfoEnum('Ipv6DefaultPing_Enum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_ma_cfg',
        {
            'disabled':'DISABLED',
            'enabled':'ENABLED',
        }, 'Cisco-IOS-XR-ipv6-ma-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg']),
    'Ipv6Reachable_Enum' : _MetaInfoEnum('Ipv6Reachable_Enum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_ma_cfg',
        {
            'any':'ANY',
            'received':'RECEIVED',
        }, 'Cisco-IOS-XR-ipv6-ma-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg']),
}
