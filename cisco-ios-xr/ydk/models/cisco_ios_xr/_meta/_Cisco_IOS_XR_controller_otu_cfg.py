


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'OtnSendTtiTypeSapiEnum' : _MetaInfoEnum('OtnSendTtiTypeSapiEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg',
        {
            'send-tti-sapi-ascii/sapi-ascii':'send_tti_sapi_ascii__FWD_SLASH__sapi_ascii',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnPerMonEnum' : _MetaInfoEnum('OtnPerMonEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnExpTtiTypeFullEnum' : _MetaInfoEnum('OtnExpTtiTypeFullEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg',
        {
            'exp-tti-full-ascii/full-ascii':'exp_tti_full_ascii__FWD_SLASH__full_ascii',
            'exp-tti-hex/hex':'exp_tti_hex__FWD_SLASH__hex',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSendTtiTypeOsEnum' : _MetaInfoEnum('OtnSendTtiTypeOsEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg',
        {
            'send-tti-os-ascii/os-ascii':'send_tti_os_ascii__FWD_SLASH__os_ascii',
            'send-tti-os-hex/os-hex':'send_tti_os_hex__FWD_SLASH__os_hex',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnExpTtiTypeDapiEnum' : _MetaInfoEnum('OtnExpTtiTypeDapiEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg',
        {
            'exp-tti-dapi-ascii/dapi-ascii':'exp_tti_dapi_ascii__FWD_SLASH__dapi_ascii',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSecAdminStateEnum' : _MetaInfoEnum('OtnSecAdminStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg',
        {
            'normal':'normal',
            'maintenance':'maintenance',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnExpTtiTypeSapiEnum' : _MetaInfoEnum('OtnExpTtiTypeSapiEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg',
        {
            'exp-tti-sapi-ascii/sapi-ascii':'exp_tti_sapi_ascii__FWD_SLASH__sapi_ascii',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtuForwardErrorCorrectionEnum' : _MetaInfoEnum('OtuForwardErrorCorrectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg',
        {
            'none':'none',
            'standard':'standard',
            'enhanced-i7':'enhanced_i7',
            'enhanced-i4':'enhanced_i4',
            'enhanced-swizzle':'enhanced_swizzle',
            'enhanced-hg20':'enhanced_hg20',
            'enhanced-hg7':'enhanced_hg7',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSendTtiTypeFullEnum' : _MetaInfoEnum('OtnSendTtiTypeFullEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg',
        {
            'send-tti-full-ascii/full-ascii':'send_tti_full_ascii__FWD_SLASH__full_ascii',
            'send-tti-hex/hex':'send_tti_hex__FWD_SLASH__hex',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnLoopbackEnum' : _MetaInfoEnum('OtnLoopbackEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg',
        {
            'line':'line',
            'internal':'internal',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSendTtiTypeDapiEnum' : _MetaInfoEnum('OtnSendTtiTypeDapiEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg',
        {
            'send-tti-dapi-ascii/dapi-ascii':'send_tti_dapi_ascii__FWD_SLASH__dapi_ascii',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnExpTtiTypeOsEnum' : _MetaInfoEnum('OtnExpTtiTypeOsEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_cfg',
        {
            'exp-tti-os-ascii/os-ascii':'exp_tti_os_ascii__FWD_SLASH__os_ascii',
            'exp-tti-os-hex/os-hex':'exp_tti_os_hex__FWD_SLASH__os_hex',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
}
