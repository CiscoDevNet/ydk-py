


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'BundleMaximumActiveLinksModeEnum' : _MetaInfoEnum('BundleMaximumActiveLinksModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'default':'DEFAULT',
            'hot-standby':'HOT_STANDBY',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundleCiscoExtTypesEnum' : _MetaInfoEnum('BundleCiscoExtTypesEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'lon-signaling-off':'LON_SIGNALING_OFF',
            'lon-signaling-on':'LON_SIGNALING_ON',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundleLoadBalanceEnum' : _MetaInfoEnum('BundleLoadBalanceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'default':'DEFAULT',
            'efp-auto':'EFP_AUTO',
            'efp-value':'EFP_VALUE',
            'source-ip':'SOURCE_IP',
            'destination-ip':'DESTINATION_IP',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'ChurnLoggingEnum' : _MetaInfoEnum('ChurnLoggingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'actor':'ACTOR',
            'partner':'PARTNER',
            'both':'BOTH',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'MlacpSwitchoverEnum' : _MetaInfoEnum('MlacpSwitchoverEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'brute-force':'BRUTE_FORCE',
            'revertive':'REVERTIVE',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'MlacpMaximizeParameterEnum' : _MetaInfoEnum('MlacpMaximizeParameterEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'links':'LINKS',
            'bandwidth':'BANDWIDTH',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'BfdModeEnum' : _MetaInfoEnum('BfdModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'no-cfg':'NO_CFG',
            'cisco':'CISCO',
            'ietf':'IETF',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'PeriodShortEnumEnum' : _MetaInfoEnum('PeriodShortEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'true':'TRUE',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundlePortActivityEnum' : _MetaInfoEnum('BundlePortActivityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'on':'ON',
            'active':'ACTIVE',
            'passive':'PASSIVE',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'Lacp' : {
        'meta_info' : _MetaInfoClass('Lacp',
            False, 
            [
            _MetaInfoClassMember('system-mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Unique identifier for this system.
                ''',
                'system_mac',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('system-priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Priority for this system. Lower value is higher
                priority.
                ''',
                'system_priority',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'lacp',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg'
        ),
    },
}
