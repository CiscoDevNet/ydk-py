


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Qosl2DataLinkEnum' : _MetaInfoEnum('Qosl2DataLinkEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg',
        {
            'aal5':'aal5',
        }, 'Cisco-IOS-XR-qos-ma-bng-cfg', _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg']),
    'Qosl2EncapEnum' : _MetaInfoEnum('Qosl2EncapEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg',
        {
            'snap-pppoa':'snap_pppoa',
            'mux-pppoa':'mux_pppoa',
            'snap1483-routed':'snap1483_routed',
            'mux1483-routed':'mux1483_routed',
            'snap-rbe':'snap_rbe',
            'snap-dot1qrbe':'snap_dot1qrbe',
            'mux-rbe':'mux_rbe',
            'mux-dot1qrbe':'mux_dot1qrbe',
        }, 'Cisco-IOS-XR-qos-ma-bng-cfg', _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg']),
}
