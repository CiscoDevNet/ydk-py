


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'ThresholdEnum' : _MetaInfoEnum('ThresholdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg',
        {
            'low':'LOW',
            'high':'HIGH',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsFecEnum' : _MetaInfoEnum('OpticsFecEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg',
        {
            'fec-none':'FEC_NONE',
            'fec-h15':'FEC_H15',
            'fec-h25':'FEC_H25',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsLoopbackEnum' : _MetaInfoEnum('OpticsLoopbackEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg',
        {
            'none':'NONE',
            'internal':'INTERNAL',
            'line':'LINE',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsDwdmCarrierGridEnum' : _MetaInfoEnum('OpticsDwdmCarrierGridEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg',
        {
            '50g-hz-grid':'Y_50G_HZ_GRID',
            '100mhz-grid':'Y_100MHZ_GRID',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsDwdmCarrierParamEnum' : _MetaInfoEnum('OpticsDwdmCarrierParamEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg',
        {
            'itu-ch':'ITU_CH',
            'wavelength':'WAVELENGTH',
            'frequency':'FREQUENCY',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg']),
}
