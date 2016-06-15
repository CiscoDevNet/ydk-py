


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.models import _yang_ns

_meta_table = {
    'Qosl2DataLinkEnum' : _MetaInfoEnum('Qosl2DataLinkEnum', 'ydk.models.qos.Cisco_IOS_XR_qos_ma_cfg',
        {
            'aal5':'AAL5',
        }, 'Cisco-IOS-XR-qos-ma-cfg', _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-cfg']),
    'QosPolicyAccountEnum' : _MetaInfoEnum('QosPolicyAccountEnum', 'ydk.models.qos.Cisco_IOS_XR_qos_ma_cfg',
        {
            'no-preference':'NO_PREFERENCE',
            'layer2':'LAYER2',
            'no-layer2':'NO_LAYER2',
            'user-defined':'USER_DEFINED',
            'layer1':'LAYER1',
        }, 'Cisco-IOS-XR-qos-ma-cfg', _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-cfg']),
    'Qosl2EncapEnum' : _MetaInfoEnum('Qosl2EncapEnum', 'ydk.models.qos.Cisco_IOS_XR_qos_ma_cfg',
        {
            'snap-pppoa':'SNAP_PPPOA',
            'mux-pppoa':'MUX_PPPOA',
            'snap1483-routed':'SNAP1483_ROUTED',
            'mux1483-routed':'MUX1483_ROUTED',
            'snap-rbe':'SNAP_RBE',
            'snap-dot1qrbe':'SNAP_DOT1QRBE',
            'mux-rbe':'MUX_RBE',
            'mux-dot1qrbe':'MUX_DOT1QRBE',
        }, 'Cisco-IOS-XR-qos-ma-cfg', _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-cfg']),
}
