


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'Ipv4DefaultPing_Enum' : _MetaInfoEnum('Ipv4DefaultPing_Enum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_io_cfg',
        {
            'disabled':'DISABLED',
            'enabled':'ENABLED',
        }, 'Cisco-IOS-XR-ipv4-io-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg']),
    'Ipv4SelfPing_Enum' : _MetaInfoEnum('Ipv4SelfPing_Enum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_io_cfg',
        {
            'disabled':'DISABLED',
            'enabled':'ENABLED',
        }, 'Cisco-IOS-XR-ipv4-io-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg']),
    'Ipv4Reachable_Enum' : _MetaInfoEnum('Ipv4Reachable_Enum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_io_cfg',
        {
            'any':'ANY',
            'received':'RECEIVED',
        }, 'Cisco-IOS-XR-ipv4-io-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg']),
    'Ipv4InterfaceQppb_Enum' : _MetaInfoEnum('Ipv4InterfaceQppb_Enum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_io_cfg',
        {
            'ip-precedence':'IP_PRECEDENCE',
            'qos-group':'QOS_GROUP',
            'both':'BOTH',
        }, 'Cisco-IOS-XR-ipv4-io-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg']),
}
