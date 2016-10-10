


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'PermitPluggableEnum' : _MetaInfoEnum('PermitPluggableEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_cfg',
        {
            'all':'ALL',
        }, 'Cisco-IOS-XR-asr9k-lc-ethctrl-cfg', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-cfg']),
    'EtherCtrlTransportModeEnum' : _MetaInfoEnum('EtherCtrlTransportModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_cfg',
        {
            'wan':'WAN',
            'otnopu1e':'OTNOPU1E',
            'otnopu2e':'OTNOPU2E',
        }, 'Cisco-IOS-XR-asr9k-lc-ethctrl-cfg', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-cfg']),
    'PermitPluggablePidEnum' : _MetaInfoEnum('PermitPluggablePidEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_cfg',
        {
            'all':'ALL',
        }, 'Cisco-IOS-XR-asr9k-lc-ethctrl-cfg', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-cfg']),
}
