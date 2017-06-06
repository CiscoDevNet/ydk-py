


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'OpticsOtsAmpliControlModeEnum' : _MetaInfoEnum('OpticsOtsAmpliControlModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg',
        {
            'automatic':'automatic',
            'manual':'manual',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsFecEnum' : _MetaInfoEnum('OpticsFecEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg',
        {
            'fec-none':'fec_none',
            'fec-h15':'fec_h15',
            'fec-h25':'fec_h25',
            'fec-h15-de':'fec_h15_de',
            'fec-h25-de':'fec_h25_de',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsOtsAmpliGainRangeEnum' : _MetaInfoEnum('OpticsOtsAmpliGainRangeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg',
        {
            'normal':'normal',
            'extended':'extended',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsOtsSafetyControlModeEnum' : _MetaInfoEnum('OpticsOtsSafetyControlModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg',
        {
            'auto':'auto',
            'disabled':'disabled',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsDwdmCarrierGridEnum' : _MetaInfoEnum('OpticsDwdmCarrierGridEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg',
        {
            '50g-hz-grid':'Y_50g_hz_grid',
            '100mhz-grid':'Y_100mhz_grid',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsDwdmCarrierParamEnum' : _MetaInfoEnum('OpticsDwdmCarrierParamEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg',
        {
            'itu-ch':'itu_ch',
            'wavelength':'wavelength',
            'frequency':'frequency',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsLoopbackEnum' : _MetaInfoEnum('OpticsLoopbackEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg',
        {
            'none':'none',
            'internal':'internal',
            'line':'line',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg']),
    'ThresholdEnum' : _MetaInfoEnum('ThresholdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_cfg',
        {
            'low':'low',
            'high':'high',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg']),
}
