


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'WaveChannelNumEnum' : _MetaInfoEnum('WaveChannelNumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'default':'DEFAULT',
            'channel-wavelength':'CHANNEL_WAVELENGTH',
            'channel-frequency':'CHANNEL_FREQUENCY',
            '100mhz-frequency':'Y_100MHZ_FREQUENCY',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'DwdmLoopbackEnum' : _MetaInfoEnum('DwdmLoopbackEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'none':'NONE',
            'line':'LINE',
            'internal':'INTERNAL',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'FecEnum' : _MetaInfoEnum('FecEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'none':'NONE',
            'standard':'STANDARD',
            'enhanced':'ENHANCED',
            'high-gain-hd':'HIGH_GAIN_HD',
            'long-haul-hd':'LONG_HAUL_HD',
            'high-gain-sd':'HIGH_GAIN_SD',
            'long-haul-sd':'LONG_HAUL_SD',
            'ci-bch':'CI_BCH',
            'high-gain-multivendor-hd':'HIGH_GAIN_MULTIVENDOR_HD',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'OduAlarmEnum' : _MetaInfoEnum('OduAlarmEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'oci':'OCI',
            'odu-ais':'ODU_AIS',
            'lck':'LCK',
            'odu-bdi':'ODU_BDI',
            'odu-sf':'ODU_SF',
            'odu-sd':'ODU_SD',
            'plm':'PLM',
            'odu-tim':'ODU_TIM',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'PrbsModeEnum' : _MetaInfoEnum('PrbsModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'source':'SOURCE',
            'sink':'SINK',
            'source-sink':'SOURCE_SINK',
            'invalid':'INVALID',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'ExpectedTtiEnum' : _MetaInfoEnum('ExpectedTtiEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'expected-tti-ascii':'EXPECTED_TTI_ASCII',
            'expected-tti-hex':'EXPECTED_TTI_HEX',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'DwdmAdminStateEnum' : _MetaInfoEnum('DwdmAdminStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'out-of-service':'OUT_OF_SERVICE',
            'in-service':'IN_SERVICE',
            'maintenance':'MAINTENANCE',
            'in-service-config-allowed':'IN_SERVICE_CONFIG_ALLOWED',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'PrbsPatternEnum' : _MetaInfoEnum('PrbsPatternEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'none':'NONE',
            'null':'NULL',
            'pn11':'PN11',
            'pn23':'PN23',
            'pn31':'PN31',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'OtuThresholdEnum' : _MetaInfoEnum('OtuThresholdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'prefec-sd':'PREFEC_SD',
            'prefec-sf':'PREFEC_SF',
            'otu-sd':'OTU_SD',
            'otu-sf':'OTU_SF',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'OtuAlarmEnum' : _MetaInfoEnum('OtuAlarmEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'los':'LOS',
            'lof':'LOF',
            'lom':'LOM',
            'iae':'IAE',
            'otu-bdi':'OTU_BDI',
            'otu-tim':'OTU_TIM',
            'otu-sf':'OTU_SF',
            'otu-sd':'OTU_SD',
            'fec-mismatch':'FEC_MISMATCH',
            'prefec-sd-ber':'PREFEC_SD_BER',
            'prefec-sf-ber':'PREFEC_SF_BER',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'OduThresholdEnum' : _MetaInfoEnum('OduThresholdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'odu-sd':'ODU_SD',
            'odu-sf':'ODU_SF',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'TxTtiEnum' : _MetaInfoEnum('TxTtiEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'tx-tti-ascii':'TX_TTI_ASCII',
            'tx-tti-hex':'TX_TTI_HEX',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'EfecEnum' : _MetaInfoEnum('EfecEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'none':'NONE',
            'i.4':'I__DOT__4',
            'i.7':'I__DOT__7',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'ProactiveEnum' : _MetaInfoEnum('ProactiveEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'default':'DEFAULT',
            'graceful':'GRACEFUL',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'FramingEnum' : _MetaInfoEnum('FramingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'opu1e':'OPU1E',
            'opu2e':'OPU2E',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
}
