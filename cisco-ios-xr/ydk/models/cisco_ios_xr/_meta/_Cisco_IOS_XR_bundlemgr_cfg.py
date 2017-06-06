


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'BundleMaximumActiveLinksModeEnum' : _MetaInfoEnum('BundleMaximumActiveLinksModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'default':'default',
            'hot-standby':'hot_standby',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundleModeEnum' : _MetaInfoEnum('BundleModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'on':'on',
            'active':'active',
            'passive':'passive',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'ChurnLoggingEnum' : _MetaInfoEnum('ChurnLoggingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'actor':'actor',
            'partner':'partner',
            'both':'both',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundleMinimumBandwidthRangeEnum' : _MetaInfoEnum('BundleMinimumBandwidthRangeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'none':'none',
            'kbps':'kbps',
            'mbps':'mbps',
            'gbps':'gbps',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundlePortActivityEnum' : _MetaInfoEnum('BundlePortActivityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'on':'on',
            'active':'active',
            'passive':'passive',
            'inherit':'inherit',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundleCiscoExtTypesEnum' : _MetaInfoEnum('BundleCiscoExtTypesEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'lon-signaling-off':'lon_signaling_off',
            'lon-signaling-on':'lon_signaling_on',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundlePeriodEnum' : _MetaInfoEnum('BundlePeriodEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'true':'true',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'BundleLoadBalanceEnum' : _MetaInfoEnum('BundleLoadBalanceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'default':'default',
            'efp-auto':'efp_auto',
            'efp-value':'efp_value',
            'source-ip':'source_ip',
            'destination-ip':'destination_ip',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'MlacpMaximizeParameterEnum' : _MetaInfoEnum('MlacpMaximizeParameterEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'links':'links',
            'bandwidth':'bandwidth',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'MlacpSwitchoverEnum' : _MetaInfoEnum('MlacpSwitchoverEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'brute-force':'brute_force',
            'revertive':'revertive',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'BfdModeEnum' : _MetaInfoEnum('BfdModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'no-cfg':'no_cfg',
            'cisco':'cisco',
            'ietf':'ietf',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'PeriodShortEnumEnum' : _MetaInfoEnum('PeriodShortEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_bundlemgr_cfg',
        {
            'true':'true',
        }, 'Cisco-IOS-XR-bundlemgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg']),
    'Lacp' : {
        'meta_info' : _MetaInfoClass('Lacp',
            False, 
            [
            _MetaInfoClassMember('system-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
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
