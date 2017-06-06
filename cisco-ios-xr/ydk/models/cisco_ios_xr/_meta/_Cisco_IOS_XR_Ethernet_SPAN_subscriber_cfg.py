


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SpanMirrorIntervalEnum' : _MetaInfoEnum('SpanMirrorIntervalEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg',
        {
            '512':'Y_512',
            '1k':'Y_1k',
            '2k':'Y_2k',
            '4k':'Y_4k',
            '8k':'Y_8k',
            '16k':'Y_16k',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg']),
    'SpanTrafficDirectionEnum' : _MetaInfoEnum('SpanTrafficDirectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg',
        {
            'rx-only':'rx_only',
            'tx-only':'tx_only',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg']),
}
