


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ipv6QppbEnum' : _MetaInfoEnum('Ipv6QppbEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_cfg',
        {
            'none':'none',
            'ip-precedence':'ip_precedence',
            'qos-group':'qos_group',
            'both':'both',
        }, 'Cisco-IOS-XR-ipv6-ma-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg']),
    'Ipv6ReachableEnum' : _MetaInfoEnum('Ipv6ReachableEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_cfg',
        {
            'any':'any',
            'received':'received',
        }, 'Cisco-IOS-XR-ipv6-ma-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg']),
    'Ipv6DefaultPingEnum' : _MetaInfoEnum('Ipv6DefaultPingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_cfg',
        {
            'disabled':'disabled',
            'enabled':'enabled',
        }, 'Cisco-IOS-XR-ipv6-ma-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg']),
    'Ipv6SelfPingEnum' : _MetaInfoEnum('Ipv6SelfPingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_cfg',
        {
            'disabled':'disabled',
            'enabled':'enabled',
        }, 'Cisco-IOS-XR-ipv6-ma-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg']),
}
