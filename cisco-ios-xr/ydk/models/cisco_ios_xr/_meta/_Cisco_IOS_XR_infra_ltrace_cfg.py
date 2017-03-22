


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'InfraLtraceScaleEnum' : _MetaInfoEnum('InfraLtraceScaleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg',
        {
            '0':'Y_0',
            '1':'Y_1',
            '2':'Y_2',
            '4':'Y_4',
            '8':'Y_8',
            '16':'Y_16',
        }, 'Cisco-IOS-XR-infra-ltrace-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-ltrace-cfg']),
    'InfraLtraceModeEnum' : _MetaInfoEnum('InfraLtraceModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg',
        {
            'static':'static',
            'dynamic':'dynamic',
        }, 'Cisco-IOS-XR-infra-ltrace-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-ltrace-cfg']),
}
