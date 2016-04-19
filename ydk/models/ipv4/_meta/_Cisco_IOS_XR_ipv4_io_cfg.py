


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'Ipv4DefaultPingEnum' : _MetaInfoEnum('Ipv4DefaultPingEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_io_cfg',
        {
            'disabled':'DISABLED',
            'enabled':'ENABLED',
        }, 'Cisco-IOS-XR-ipv4-io-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg']),
    'Ipv4SelfPingEnum' : _MetaInfoEnum('Ipv4SelfPingEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_io_cfg',
        {
            'disabled':'DISABLED',
            'enabled':'ENABLED',
        }, 'Cisco-IOS-XR-ipv4-io-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg']),
    'Ipv4ReachableEnum' : _MetaInfoEnum('Ipv4ReachableEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_io_cfg',
        {
            'any':'ANY',
            'received':'RECEIVED',
        }, 'Cisco-IOS-XR-ipv4-io-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg']),
    'Ipv4InterfaceQppbEnum' : _MetaInfoEnum('Ipv4InterfaceQppbEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_io_cfg',
        {
            'ip-precedence':'IP_PRECEDENCE',
            'qos-group':'QOS_GROUP',
            'both':'BOTH',
        }, 'Cisco-IOS-XR-ipv4-io-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg']),
}
