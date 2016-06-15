


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.models import _yang_ns

_meta_table = {
    'AtmVpiBitsModeEnum' : _MetaInfoEnum('AtmVpiBitsModeEnum', 'ydk.models.atm.Cisco_IOS_XR_atm_vcm_cfg',
        {
            'twelve':'TWELVE',
        }, 'Cisco-IOS-XR-atm-vcm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg']),
    'AtmPvcTestModeEnum' : _MetaInfoEnum('AtmPvcTestModeEnum', 'ydk.models.atm.Cisco_IOS_XR_atm_vcm_cfg',
        {
            'loop':'LOOP',
            'reserved':'RESERVED',
        }, 'Cisco-IOS-XR-atm-vcm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg']),
    'AtmPvpTestModeEnum' : _MetaInfoEnum('AtmPvpTestModeEnum', 'ydk.models.atm.Cisco_IOS_XR_atm_vcm_cfg',
        {
            'loop':'LOOP',
        }, 'Cisco-IOS-XR-atm-vcm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg']),
}
