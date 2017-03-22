


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength' : {
        'meta_info' : _MetaInfoClass('HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength',
            False, 
            [
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-fia-hw-profile-cfg', True),
            _MetaInfoClassMember('ipv4-unicast-prefix-percent', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                curve out percentage of TCAM table
                entries
                ''',
                'ipv4_unicast_prefix_percent',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            ],
            'Cisco-IOS-XR-fia-hw-profile-cfg',
            'ipv4-unicast-prefix-length',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-hw-profile-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg'
        ),
    },
    'HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths' : {
        'meta_info' : _MetaInfoClass('HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths',
            False, 
            [
            _MetaInfoClassMember('ipv4-unicast-prefix-length', REFERENCE_LIST, 'Ipv4UnicastPrefixLength' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg', 'HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength', 
                [], [], 
                '''                IPv4 Unicast prefix length
                ''',
                'ipv4_unicast_prefix_length',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            ],
            'Cisco-IOS-XR-fia-hw-profile-cfg',
            'ipv4-unicast-prefix-lengths',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-hw-profile-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg'
        ),
    },
    'HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast' : {
        'meta_info' : _MetaInfoClass('HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast',
            False, 
            [
            _MetaInfoClassMember('ipv4-unicast-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                curve out percentage of TCAM table entries
                ''',
                'ipv4_unicast_percent',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            _MetaInfoClassMember('ipv4-unicast-prefix-lengths', REFERENCE_CLASS, 'Ipv4UnicastPrefixLengths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg', 'HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths', 
                [], [], 
                '''                IPv4 Unicast prefix 
                ''',
                'ipv4_unicast_prefix_lengths',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            ],
            'Cisco-IOS-XR-fia-hw-profile-cfg',
            'ipv4-unicast',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-hw-profile-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg'
        ),
    },
    'HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address' : {
        'meta_info' : _MetaInfoClass('HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address',
            False, 
            [
            _MetaInfoClassMember('ipv4-unicast', REFERENCE_CLASS, 'Ipv4Unicast' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg', 'HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast', 
                [], [], 
                '''                Unicast table for TCAM LC cards
                ''',
                'ipv4_unicast',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            ],
            'Cisco-IOS-XR-fia-hw-profile-cfg',
            'ipv4-address',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-hw-profile-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg'
        ),
    },
    'HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength' : {
        'meta_info' : _MetaInfoClass('HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength',
            False, 
            [
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-fia-hw-profile-cfg', True),
            _MetaInfoClassMember('ipv6-unicast-prefix-percent', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                curve out percentage of TCAM table
                entries
                ''',
                'ipv6_unicast_prefix_percent',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            ],
            'Cisco-IOS-XR-fia-hw-profile-cfg',
            'ipv6-unicast-prefix-length',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-hw-profile-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg'
        ),
    },
    'HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths' : {
        'meta_info' : _MetaInfoClass('HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths',
            False, 
            [
            _MetaInfoClassMember('ipv6-unicast-prefix-length', REFERENCE_LIST, 'Ipv6UnicastPrefixLength' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg', 'HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength', 
                [], [], 
                '''                IPv6 Unicast prefix length
                ''',
                'ipv6_unicast_prefix_length',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            ],
            'Cisco-IOS-XR-fia-hw-profile-cfg',
            'ipv6-unicast-prefix-lengths',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-hw-profile-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg'
        ),
    },
    'HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast' : {
        'meta_info' : _MetaInfoClass('HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast',
            False, 
            [
            _MetaInfoClassMember('ipv6-unicast-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                curve out percentage of TCAM table entries
                ''',
                'ipv6_unicast_percent',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            _MetaInfoClassMember('ipv6-unicast-prefix-lengths', REFERENCE_CLASS, 'Ipv6UnicastPrefixLengths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg', 'HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths', 
                [], [], 
                '''                IPv6 Unicast prefix 
                ''',
                'ipv6_unicast_prefix_lengths',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            ],
            'Cisco-IOS-XR-fia-hw-profile-cfg',
            'ipv6-unicast',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-hw-profile-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg'
        ),
    },
    'HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address' : {
        'meta_info' : _MetaInfoClass('HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address',
            False, 
            [
            _MetaInfoClassMember('ipv6-unicast', REFERENCE_CLASS, 'Ipv6Unicast' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg', 'HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast', 
                [], [], 
                '''                Unicast table for TCAM LC cards
                ''',
                'ipv6_unicast',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            ],
            'Cisco-IOS-XR-fia-hw-profile-cfg',
            'ipv6-address',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-hw-profile-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg'
        ),
    },
    'HwModuleProfileConfig.Profile.TcamTable.FibTable' : {
        'meta_info' : _MetaInfoClass('HwModuleProfileConfig.Profile.TcamTable.FibTable',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', REFERENCE_CLASS, 'Ipv4Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg', 'HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address', 
                [], [], 
                '''                IPv4 table for TCAM LC cards
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            _MetaInfoClassMember('ipv6-address', REFERENCE_CLASS, 'Ipv6Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg', 'HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address', 
                [], [], 
                '''                IPv6 table for TCAM LC cards
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            ],
            'Cisco-IOS-XR-fia-hw-profile-cfg',
            'fib-table',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-hw-profile-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg'
        ),
    },
    'HwModuleProfileConfig.Profile.TcamTable' : {
        'meta_info' : _MetaInfoClass('HwModuleProfileConfig.Profile.TcamTable',
            False, 
            [
            _MetaInfoClassMember('fib-table', REFERENCE_CLASS, 'FibTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg', 'HwModuleProfileConfig.Profile.TcamTable.FibTable', 
                [], [], 
                '''                FIB table for TCAM LC cards
                ''',
                'fib_table',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            ],
            'Cisco-IOS-XR-fia-hw-profile-cfg',
            'tcam-table',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-hw-profile-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg'
        ),
    },
    'HwModuleProfileConfig.Profile' : {
        'meta_info' : _MetaInfoClass('HwModuleProfileConfig.Profile',
            False, 
            [
            _MetaInfoClassMember('tcam-table', REFERENCE_CLASS, 'TcamTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg', 'HwModuleProfileConfig.Profile.TcamTable', 
                [], [], 
                '''                Configure profile for TCAM LC cards
                ''',
                'tcam_table',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            ],
            'Cisco-IOS-XR-fia-hw-profile-cfg',
            'profile',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-hw-profile-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg'
        ),
    },
    'HwModuleProfileConfig' : {
        'meta_info' : _MetaInfoClass('HwModuleProfileConfig',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_CLASS, 'Profile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg', 'HwModuleProfileConfig.Profile', 
                [], [], 
                '''                Configure profile.
                ''',
                'profile',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            ],
            'Cisco-IOS-XR-fia-hw-profile-cfg',
            'hw-module-profile-config',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-hw-profile-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg'
        ),
    },
}
_meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength']['meta_info'].parent =_meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths']['meta_info']
_meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths']['meta_info'].parent =_meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast']['meta_info']
_meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast']['meta_info'].parent =_meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address']['meta_info']
_meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength']['meta_info'].parent =_meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths']['meta_info']
_meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths']['meta_info'].parent =_meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast']['meta_info']
_meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast']['meta_info'].parent =_meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address']['meta_info']
_meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address']['meta_info'].parent =_meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable']['meta_info']
_meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address']['meta_info'].parent =_meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable']['meta_info']
_meta_table['HwModuleProfileConfig.Profile.TcamTable.FibTable']['meta_info'].parent =_meta_table['HwModuleProfileConfig.Profile.TcamTable']['meta_info']
_meta_table['HwModuleProfileConfig.Profile.TcamTable']['meta_info'].parent =_meta_table['HwModuleProfileConfig.Profile']['meta_info']
_meta_table['HwModuleProfileConfig.Profile']['meta_info'].parent =_meta_table['HwModuleProfileConfig']['meta_info']
