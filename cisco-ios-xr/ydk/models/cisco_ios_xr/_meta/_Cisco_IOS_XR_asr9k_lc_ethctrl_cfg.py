


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PermitPluggablePidEnum' : _MetaInfoEnum('PermitPluggablePidEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_cfg',
        {
            'all':'all',
        }, 'Cisco-IOS-XR-asr9k-lc-ethctrl-cfg', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-cfg']),
    'EtherCtrlTransportModeEnum' : _MetaInfoEnum('EtherCtrlTransportModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_cfg',
        {
            'wan':'wan',
            'otnopu1e':'otnopu1e',
            'otnopu2e':'otnopu2e',
        }, 'Cisco-IOS-XR-asr9k-lc-ethctrl-cfg', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-cfg']),
    'PermitPluggableEnum' : _MetaInfoEnum('PermitPluggableEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_cfg',
        {
            'all':'all',
        }, 'Cisco-IOS-XR-asr9k-lc-ethctrl-cfg', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-cfg']),
}
