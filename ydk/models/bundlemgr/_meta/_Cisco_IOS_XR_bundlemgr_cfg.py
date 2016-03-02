


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'BundleMaximumActiveLinksMode_Enum' : _MetaInfoEnum('BundleMaximumActiveLinksMode_Enum', 'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'default':'DEFAULT',
            'hot-standby':'HOT_STANDBY',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundleCiscoExtTypes_Enum' : _MetaInfoEnum('BundleCiscoExtTypes_Enum', 'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'lon-signaling-off':'LON_SIGNALING_OFF',
            'lon-signaling-on':'LON_SIGNALING_ON',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundleLoadBalance_Enum' : _MetaInfoEnum('BundleLoadBalance_Enum', 'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'default':'DEFAULT',
            'efp-auto':'EFP_AUTO',
            'efp-value':'EFP_VALUE',
            'source-ip':'SOURCE_IP',
            'destination-ip':'DESTINATION_IP',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'ChurnLogging_Enum' : _MetaInfoEnum('ChurnLogging_Enum', 'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'actor':'ACTOR',
            'partner':'PARTNER',
            'both':'BOTH',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'MlacpSwitchover_Enum' : _MetaInfoEnum('MlacpSwitchover_Enum', 'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'brute-force':'BRUTE_FORCE',
            'revertive':'REVERTIVE',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'MlacpMaximizeParameter_Enum' : _MetaInfoEnum('MlacpMaximizeParameter_Enum', 'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'links':'LINKS',
            'bandwidth':'BANDWIDTH',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'BfdMode_Enum' : _MetaInfoEnum('BfdMode_Enum', 'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'no-cfg':'NO_CFG',
            'cisco':'CISCO',
            'ietf':'IETF',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'PeriodShortEnum_Enum' : _MetaInfoEnum('PeriodShortEnum_Enum', 'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'true':'TRUE',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundlePortActivity_Enum' : _MetaInfoEnum('BundlePortActivity_Enum', 'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg',
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
                [(1, 65535)], [], 
                '''                Priority for this system. Lower value is higher
                priority.
                ''',
                'system_priority',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'lacp',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg'
        ),
    },
}
