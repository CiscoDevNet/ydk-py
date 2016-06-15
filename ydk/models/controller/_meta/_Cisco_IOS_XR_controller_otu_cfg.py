


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.models import _yang_ns

_meta_table = {
    'OtnLoopbackEnum' : _MetaInfoEnum('OtnLoopbackEnum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'line':'LINE',
            'internal':'INTERNAL',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnExpTtiTypeSapiEnum' : _MetaInfoEnum('OtnExpTtiTypeSapiEnum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'exp-tti-sapi-ascii/sapi-ascii':'EXP_TTI_SAPI_ASCII__FWD_SLASH__SAPI_ASCII',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnPerMonEnum' : _MetaInfoEnum('OtnPerMonEnum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'disable':'DISABLE',
            'enable':'ENABLE',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSendTtiTypeOsEnum' : _MetaInfoEnum('OtnSendTtiTypeOsEnum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'send-tti-os-ascii/os-ascii':'SEND_TTI_OS_ASCII__FWD_SLASH__OS_ASCII',
            'send-tti-os-hex/os-hex':'SEND_TTI_OS_HEX__FWD_SLASH__OS_HEX',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSendTtiTypeSapiEnum' : _MetaInfoEnum('OtnSendTtiTypeSapiEnum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'send-tti-sapi-ascii/sapi-ascii':'SEND_TTI_SAPI_ASCII__FWD_SLASH__SAPI_ASCII',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSendTtiTypeDapiEnum' : _MetaInfoEnum('OtnSendTtiTypeDapiEnum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'send-tti-dapi-ascii/dapi-ascii':'SEND_TTI_DAPI_ASCII__FWD_SLASH__DAPI_ASCII',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnExpTtiTypeOsEnum' : _MetaInfoEnum('OtnExpTtiTypeOsEnum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'exp-tti-os-ascii/os-ascii':'EXP_TTI_OS_ASCII__FWD_SLASH__OS_ASCII',
            'exp-tti-os-hex/os-hex':'EXP_TTI_OS_HEX__FWD_SLASH__OS_HEX',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSecAdminStateEnum' : _MetaInfoEnum('OtnSecAdminStateEnum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'normal':'NORMAL',
            'maintenance':'MAINTENANCE',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnExpTtiTypeFullEnum' : _MetaInfoEnum('OtnExpTtiTypeFullEnum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'exp-tti-full-ascii/full-ascii':'EXP_TTI_FULL_ASCII__FWD_SLASH__FULL_ASCII',
            'exp-tti-hex/hex':'EXP_TTI_HEX__FWD_SLASH__HEX',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtuForwardErrorCorrectionEnum' : _MetaInfoEnum('OtuForwardErrorCorrectionEnum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'none':'NONE',
            'standard':'STANDARD',
            'enhanced-i7':'ENHANCED_I7',
            'enhanced-i4':'ENHANCED_I4',
            'enhanced-swizzle':'ENHANCED_SWIZZLE',
            'enhanced-hg20':'ENHANCED_HG20',
            'enhanced-hg7':'ENHANCED_HG7',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnExpTtiTypeDapiEnum' : _MetaInfoEnum('OtnExpTtiTypeDapiEnum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'exp-tti-dapi-ascii/dapi-ascii':'EXP_TTI_DAPI_ASCII__FWD_SLASH__DAPI_ASCII',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSendTtiTypeFullEnum' : _MetaInfoEnum('OtnSendTtiTypeFullEnum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'send-tti-full-ascii/full-ascii':'SEND_TTI_FULL_ASCII__FWD_SLASH__FULL_ASCII',
            'send-tti-hex/hex':'SEND_TTI_HEX__FWD_SLASH__HEX',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
}
