


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'SpanSessionClassOldEnum' : _MetaInfoEnum('SpanSessionClassOldEnum', 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_datatypes',
        {
            'true':'TRUE',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-datatypes']),
    'SpanSessionClassEnum' : _MetaInfoEnum('SpanSessionClassEnum', 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_datatypes',
        {
            'ethernet':'ETHERNET',
            'ipv4':'IPV4',
            'ipv6':'IPV6',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-datatypes']),
}
