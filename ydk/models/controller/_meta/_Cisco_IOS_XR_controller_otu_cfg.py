


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'OtnLoopback_Enum' : _MetaInfoEnum('OtnLoopback_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'line':'LINE',
            'internal':'INTERNAL',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnExpTtiTypeSapi_Enum' : _MetaInfoEnum('OtnExpTtiTypeSapi_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'exp-tti-sapi-ascii/sapi-ascii':'EXP_TTI_SAPI_ASCII__FWD_SLASH__SAPI_ASCII',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnPerMon_Enum' : _MetaInfoEnum('OtnPerMon_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'disable':'DISABLE',
            'enable':'ENABLE',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSendTtiTypeOs_Enum' : _MetaInfoEnum('OtnSendTtiTypeOs_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'send-tti-os-ascii/os-ascii':'SEND_TTI_OS_ASCII__FWD_SLASH__OS_ASCII',
            'send-tti-os-hex/os-hex':'SEND_TTI_OS_HEX__FWD_SLASH__OS_HEX',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSendTtiTypeSapi_Enum' : _MetaInfoEnum('OtnSendTtiTypeSapi_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'send-tti-sapi-ascii/sapi-ascii':'SEND_TTI_SAPI_ASCII__FWD_SLASH__SAPI_ASCII',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSendTtiTypeDapi_Enum' : _MetaInfoEnum('OtnSendTtiTypeDapi_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'send-tti-dapi-ascii/dapi-ascii':'SEND_TTI_DAPI_ASCII__FWD_SLASH__DAPI_ASCII',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnExpTtiTypeOs_Enum' : _MetaInfoEnum('OtnExpTtiTypeOs_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'exp-tti-os-ascii/os-ascii':'EXP_TTI_OS_ASCII__FWD_SLASH__OS_ASCII',
            'exp-tti-os-hex/os-hex':'EXP_TTI_OS_HEX__FWD_SLASH__OS_HEX',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSecAdminState_Enum' : _MetaInfoEnum('OtnSecAdminState_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'normal':'NORMAL',
            'maintenance':'MAINTENANCE',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnExpTtiTypeFull_Enum' : _MetaInfoEnum('OtnExpTtiTypeFull_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'exp-tti-full-ascii/full-ascii':'EXP_TTI_FULL_ASCII__FWD_SLASH__FULL_ASCII',
            'exp-tti-hex/hex':'EXP_TTI_HEX__FWD_SLASH__HEX',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtuForwardErrorCorrection_Enum' : _MetaInfoEnum('OtuForwardErrorCorrection_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'none':'NONE',
            'standard':'STANDARD',
            'enhanced-i7':'ENHANCED_I7',
            'enhanced-i4':'ENHANCED_I4',
            'enhanced-swizzle':'ENHANCED_SWIZZLE',
            'enhanced-hg20':'ENHANCED_HG20',
            'enhanced-hg7':'ENHANCED_HG7',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnExpTtiTypeDapi_Enum' : _MetaInfoEnum('OtnExpTtiTypeDapi_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'exp-tti-dapi-ascii/dapi-ascii':'EXP_TTI_DAPI_ASCII__FWD_SLASH__DAPI_ASCII',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
    'OtnSendTtiTypeFull_Enum' : _MetaInfoEnum('OtnSendTtiTypeFull_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg',
        {
            'send-tti-full-ascii/full-ascii':'SEND_TTI_FULL_ASCII__FWD_SLASH__FULL_ASCII',
            'send-tti-hex/hex':'SEND_TTI_HEX__FWD_SLASH__HEX',
        }, 'Cisco-IOS-XR-controller-otu-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg']),
}
