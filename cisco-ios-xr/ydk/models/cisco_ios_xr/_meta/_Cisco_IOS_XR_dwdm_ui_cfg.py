


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PrbsPatternEnum' : _MetaInfoEnum('PrbsPatternEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'none':'none',
            'null':'null',
            'pn11':'pn11',
            'pn23':'pn23',
            'pn31':'pn31',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'FecEnum' : _MetaInfoEnum('FecEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'none':'none',
            'standard':'standard',
            'enhanced':'enhanced',
            'high-gain-hd':'high_gain_hd',
            'long-haul-hd':'long_haul_hd',
            'high-gain-sd':'high_gain_sd',
            'long-haul-sd':'long_haul_sd',
            'ci-bch':'ci_bch',
            'high-gain-multivendor-hd':'high_gain_multivendor_hd',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'WaveChannelNumEnum' : _MetaInfoEnum('WaveChannelNumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'default':'default',
            'channel-wavelength':'channel_wavelength',
            'channel-frequency':'channel_frequency',
            '100mhz-frequency':'Y_100mhz_frequency',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'TxTtiEnum' : _MetaInfoEnum('TxTtiEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'tx-tti-ascii':'tx_tti_ascii',
            'tx-tti-hex':'tx_tti_hex',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'DwdmAdminStateEnum' : _MetaInfoEnum('DwdmAdminStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'out-of-service':'out_of_service',
            'in-service':'in_service',
            'maintenance':'maintenance',
            'in-service-config-allowed':'in_service_config_allowed',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'OtuThresholdEnum' : _MetaInfoEnum('OtuThresholdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'prefec-sd':'prefec_sd',
            'prefec-sf':'prefec_sf',
            'otu-sd':'otu_sd',
            'otu-sf':'otu_sf',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'ExpectedTtiEnum' : _MetaInfoEnum('ExpectedTtiEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'expected-tti-ascii':'expected_tti_ascii',
            'expected-tti-hex':'expected_tti_hex',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'DwdmLoopbackEnum' : _MetaInfoEnum('DwdmLoopbackEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'none':'none',
            'line':'line',
            'internal':'internal',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'ProactiveEnum' : _MetaInfoEnum('ProactiveEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'default':'default',
            'graceful':'graceful',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'FramingEnum' : _MetaInfoEnum('FramingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'opu1e':'opu1e',
            'opu2e':'opu2e',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'OtuAlarmEnum' : _MetaInfoEnum('OtuAlarmEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'los':'los',
            'lof':'lof',
            'lom':'lom',
            'iae':'iae',
            'otu-bdi':'otu_bdi',
            'otu-tim':'otu_tim',
            'otu-sf':'otu_sf',
            'otu-sd':'otu_sd',
            'fec-mismatch':'fec_mismatch',
            'prefec-sd-ber':'prefec_sd_ber',
            'prefec-sf-ber':'prefec_sf_ber',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'OduThresholdEnum' : _MetaInfoEnum('OduThresholdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'odu-sd':'odu_sd',
            'odu-sf':'odu_sf',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'OduAlarmEnum' : _MetaInfoEnum('OduAlarmEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'oci':'oci',
            'odu-ais':'odu_ais',
            'lck':'lck',
            'odu-bdi':'odu_bdi',
            'odu-sf':'odu_sf',
            'odu-sd':'odu_sd',
            'plm':'plm',
            'odu-tim':'odu_tim',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'PrbsModeEnum' : _MetaInfoEnum('PrbsModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'source':'source',
            'sink':'sink',
            'source-sink':'source_sink',
            'invalid':'invalid',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
    'EfecEnum' : _MetaInfoEnum('EfecEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_cfg',
        {
            'none':'none',
            'i.4':'i__DOT__4',
            'i.7':'i__DOT__7',
        }, 'Cisco-IOS-XR-dwdm-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-cfg']),
}
