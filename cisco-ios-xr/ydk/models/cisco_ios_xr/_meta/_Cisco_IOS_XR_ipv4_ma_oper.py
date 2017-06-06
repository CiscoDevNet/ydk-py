


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ipv4MaOperLineStateEnum' : _MetaInfoEnum('Ipv4MaOperLineStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper',
        {
            'unknown':'unknown',
            'shutdown':'shutdown',
            'down':'down',
            'up':'up',
        }, 'Cisco-IOS-XR-ipv4-ma-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper']),
    'RpfModeEnum' : _MetaInfoEnum('RpfModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper',
        {
            'strict':'strict',
            'loose':'loose',
        }, 'Cisco-IOS-XR-ipv4-ma-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper']),
}
