


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'NasPortValueEnum' : _MetaInfoEnum('NasPortValueEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_aaacore_cfg',
        {
            'async':'async',
            'sync':'sync',
            'isdn':'isdn',
            'isdn-async-v120':'isdn_async_v120',
            'isdn-async-v110':'isdn_async_v110',
            'virtual':'virtual',
            'isdn-async-piafs':'isdn_async_piafs',
            'x75':'x75',
            'ethernet':'ethernet',
            'pppoa':'pppoa',
            'pppoeoa':'pppoeoa',
            'pppoeoe':'pppoeoe',
            'pppoeovlan':'pppoeovlan',
            'pppoeoqinq':'pppoeoqinq',
            'virtual-pppoeoe':'virtual_pppoeoe',
            'virtual-pppoeovlan':'virtual_pppoeovlan',
            'virtual-pppoeoqinaq':'virtual_pppoeoqinaq',
            'ipsec':'ipsec',
            'ipoeoe':'ipoeoe',
            'ipoeovlan':'ipoeovlan',
            'ipoeoqinq':'ipoeoqinq',
            'virtual-ipoeoe':'virtual_ipoeoe',
            'virtual-ipoeovlan':'virtual_ipoeovlan',
            'virtual-ipoeoqinq':'virtual_ipoeoqinq',
        }, 'Cisco-IOS-XR-aaa-aaacore-cfg', _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg']),
    'AaaServiceAccountingEnum' : _MetaInfoEnum('AaaServiceAccountingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_aaacore_cfg',
        {
            'none':'none',
            'extended':'extended',
            'brief':'brief',
        }, 'Cisco-IOS-XR-aaa-aaacore-cfg', _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg']),
}
