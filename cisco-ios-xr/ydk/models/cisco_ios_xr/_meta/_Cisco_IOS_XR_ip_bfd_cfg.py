


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'BfdBundleCoexistenceBobBlbEnum' : _MetaInfoEnum('BfdBundleCoexistenceBobBlbEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg',
        {
            'inherited':'inherited',
            'logical':'logical',
        }, 'Cisco-IOS-XR-ip-bfd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-cfg']),
    'BfdIfIpv6ChecksumUsageEnum' : _MetaInfoEnum('BfdIfIpv6ChecksumUsageEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-ip-bfd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-cfg']),
    'BfdIfEchoUsageEnum' : _MetaInfoEnum('BfdIfEchoUsageEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'Cisco-IOS-XR-ip-bfd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-cfg']),
    'BfdEchoStartupValidateEnum' : _MetaInfoEnum('BfdEchoStartupValidateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg',
        {
            'off':'off',
            'on':'on',
            'force':'force',
        }, 'Cisco-IOS-XR-ip-bfd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-cfg']),
    'Bfd.FlapDamp.BundleMember' : {
        'meta_info' : _MetaInfoClass('Bfd.FlapDamp.BundleMember',
            False, 
            [
            _MetaInfoClassMember('initial-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '518400000')], [], 
                '''                Initial delay before bringing up session
                ''',
                'initial_delay',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('l3-only-mode', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Apply immediate dampening and only when
                failure is L3 specific
                ''',
                'l3_only_mode',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('maximum-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '518400000')], [], 
                '''                Maximum delay before bringing up session
                ''',
                'maximum_delay',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('secondary-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '518400000')], [], 
                '''                Secondary delay before bringing up session
                ''',
                'secondary_delay',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-bfd-cfg',
            'bundle-member',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg'
        ),
    },
    'Bfd.FlapDamp.Extensions' : {
        'meta_info' : _MetaInfoClass('Bfd.FlapDamp.Extensions',
            False, 
            [
            _MetaInfoClassMember('down-monitor', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                If set, DOWN state monitoring mode is enabled
                ''',
                'down_monitor',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-bfd-cfg',
            'extensions',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg'
        ),
    },
    'Bfd.FlapDamp' : {
        'meta_info' : _MetaInfoClass('Bfd.FlapDamp',
            False, 
            [
            _MetaInfoClassMember('bundle-member', REFERENCE_CLASS, 'BundleMember' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg', 'Bfd.FlapDamp.BundleMember', 
                [], [], 
                '''                Bundle per member feature class container
                ''',
                'bundle_member',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('dampen-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Dampening Enable/Disable
                ''',
                'dampen_disable',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('extensions', REFERENCE_CLASS, 'Extensions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg', 'Bfd.FlapDamp.Extensions', 
                [], [], 
                '''                Extensions to the BFD dampening feature
                ''',
                'extensions',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('initial-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600000')], [], 
                '''                Initial delay before bringing up session
                ''',
                'initial_delay',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('maximum-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600000')], [], 
                '''                Maximum delay before bringing up session
                ''',
                'maximum_delay',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('secondary-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600000')], [], 
                '''                Secondary delay before bringing up session
                ''',
                'secondary_delay',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('60000', '3600000')], [], 
                '''                Stability threshold to enable dampening
                ''',
                'threshold',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-bfd-cfg',
            'flap-damp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg'
        ),
    },
    'Bfd.EchoLatency.Detect' : {
        'meta_info' : _MetaInfoClass('Bfd.EchoLatency.Detect',
            False, 
            [
            _MetaInfoClassMember('latency-detect-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Echo latency detect count
                ''',
                'latency_detect_count',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('latency-detect-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set, echo latency detect is enabled
                ''',
                'latency_detect_enabled',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('latency-detect-percentage', ATTRIBUTE, 'int' , None, None, 
                [('100', '250')], [], 
                '''                Echo latency detect percentage
                ''',
                'latency_detect_percentage',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-bfd-cfg',
            'detect',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg'
        ),
    },
    'Bfd.EchoLatency' : {
        'meta_info' : _MetaInfoClass('Bfd.EchoLatency',
            False, 
            [
            _MetaInfoClassMember('detect', REFERENCE_CLASS, 'Detect' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg', 'Bfd.EchoLatency.Detect', 
                [], [], 
                '''                BFD echo latency detection
                ''',
                'detect',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-bfd-cfg',
            'echo-latency',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg'
        ),
    },
    'Bfd.EchoStartup' : {
        'meta_info' : _MetaInfoClass('Bfd.EchoStartup',
            False, 
            [
            _MetaInfoClassMember('validate', REFERENCE_ENUM_CLASS, 'BfdEchoStartupValidateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg', 'BfdEchoStartupValidateEnum', 
                [], [], 
                '''                BFD echo validation prior to session bringup
                ''',
                'validate',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-bfd-cfg',
            'echo-startup',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg'
        ),
    },
    'Bfd.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Bfd.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-cfg', True),
            _MetaInfoClassMember('interface-echo-usage', REFERENCE_ENUM_CLASS, 'BfdIfEchoUsageEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg', 'BfdIfEchoUsageEnum', 
                [], [], 
                '''                Echo usage for this interface
                ''',
                'interface_echo_usage',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('interface-ipv4-echo-source', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Interface IPv4 echo source address
                configuration
                ''',
                'interface_ipv4_echo_source',
                'Cisco-IOS-XR-ip-bfd-cfg', False, [
                    _MetaInfoClassMember('interface-ipv4-echo-source', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Interface IPv4 echo source address
                        configuration
                        ''',
                        'interface_ipv4_echo_source',
                        'Cisco-IOS-XR-ip-bfd-cfg', False),
                    _MetaInfoClassMember('interface-ipv4-echo-source', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Interface IPv4 echo source address
                        configuration
                        ''',
                        'interface_ipv4_echo_source',
                        'Cisco-IOS-XR-ip-bfd-cfg', False),
                ]),
            _MetaInfoClassMember('ipv6-checksum', REFERENCE_ENUM_CLASS, 'BfdIfIpv6ChecksumUsageEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg', 'BfdIfIpv6ChecksumUsageEnum', 
                [], [], 
                '''                IPv6 checksum usage for this interface -
                Interface config will always take precedence
                over global config
                ''',
                'ipv6_checksum',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-bfd-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg'
        ),
    },
    'Bfd.Interfaces' : {
        'meta_info' : _MetaInfoClass('Bfd.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg', 'Bfd.Interfaces.Interface', 
                [], [], 
                '''                Single interface configuration
                ''',
                'interface',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-bfd-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg'
        ),
    },
    'Bfd.MultiPathIncludes.MultiPathInclude' : {
        'meta_info' : _MetaInfoClass('Bfd.MultiPathIncludes.MultiPathInclude',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-cfg', True),
            ],
            'Cisco-IOS-XR-ip-bfd-cfg',
            'multi-path-include',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg'
        ),
    },
    'Bfd.MultiPathIncludes' : {
        'meta_info' : _MetaInfoClass('Bfd.MultiPathIncludes',
            False, 
            [
            _MetaInfoClassMember('multi-path-include', REFERENCE_LIST, 'MultiPathInclude' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg', 'Bfd.MultiPathIncludes.MultiPathInclude', 
                [], [], 
                '''                Location configuration
                ''',
                'multi_path_include',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-bfd-cfg',
            'multi-path-includes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg'
        ),
    },
    'Bfd.Bundle.Coexistence' : {
        'meta_info' : _MetaInfoClass('Bfd.Bundle.Coexistence',
            False, 
            [
            _MetaInfoClassMember('bob-blb', REFERENCE_ENUM_CLASS, 'BfdBundleCoexistenceBobBlbEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg', 'BfdBundleCoexistenceBobBlbEnum', 
                [], [], 
                '''                Coexistence mode for BoB and BLB feature
                ''',
                'bob_blb',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-bfd-cfg',
            'coexistence',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg'
        ),
    },
    'Bfd.Bundle' : {
        'meta_info' : _MetaInfoClass('Bfd.Bundle',
            False, 
            [
            _MetaInfoClassMember('coexistence', REFERENCE_CLASS, 'Coexistence' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg', 'Bfd.Bundle.Coexistence', 
                [], [], 
                '''                Coexistence mode for BFD on bundle feature
                ''',
                'coexistence',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-bfd-cfg',
            'bundle',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg'
        ),
    },
    'Bfd' : {
        'meta_info' : _MetaInfoClass('Bfd',
            False, 
            [
            _MetaInfoClassMember('bundle', REFERENCE_CLASS, 'Bundle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg', 'Bfd.Bundle', 
                [], [], 
                '''                Configuration related to BFD over Bundle
                ''',
                'bundle',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('echo-latency', REFERENCE_CLASS, 'EchoLatency' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg', 'Bfd.EchoLatency', 
                [], [], 
                '''                BFD echo latency feature class container
                ''',
                'echo_latency',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('echo-startup', REFERENCE_CLASS, 'EchoStartup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg', 'Bfd.EchoStartup', 
                [], [], 
                '''                BFD echo startup feature class container
                ''',
                'echo_startup',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('flap-damp', REFERENCE_CLASS, 'FlapDamp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg', 'Bfd.FlapDamp', 
                [], [], 
                '''                Flapping class container
                ''',
                'flap_damp',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('global-echo-min-interval', ATTRIBUTE, 'int' , None, None, 
                [('15', '2000')], [], 
                '''                Configure echo min-interval for bundle interface
                ''',
                'global_echo_min_interval',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('global-echo-usage', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Echo configuration
                ''',
                'global_echo_usage',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('global-ipv4-echo-source', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4 echo source address configuration
                ''',
                'global_ipv4_echo_source',
                'Cisco-IOS-XR-ip-bfd-cfg', False, [
                    _MetaInfoClassMember('global-ipv4-echo-source', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 echo source address configuration
                        ''',
                        'global_ipv4_echo_source',
                        'Cisco-IOS-XR-ip-bfd-cfg', False),
                    _MetaInfoClassMember('global-ipv4-echo-source', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 echo source address configuration
                        ''',
                        'global_ipv4_echo_source',
                        'Cisco-IOS-XR-ip-bfd-cfg', False),
                ]),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg', 'Bfd.Interfaces', 
                [], [], 
                '''                Interface configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('ipv6-checksum-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                To disable IPv6 checksum configuration
                ''',
                'ipv6_checksum_disable',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('multi-path-includes', REFERENCE_CLASS, 'MultiPathIncludes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg', 'Bfd.MultiPathIncludes', 
                [], [], 
                '''                Multipath Include configuration
                ''',
                'multi_path_includes',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('single-hop-trap', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Single hop trap configuration
                ''',
                'single_hop_trap',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('ttl-drop-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '254')], [], 
                '''                Multihop TTL Drop Threshold
                ''',
                'ttl_drop_threshold',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-bfd-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg'
        ),
    },
}
_meta_table['Bfd.FlapDamp.BundleMember']['meta_info'].parent =_meta_table['Bfd.FlapDamp']['meta_info']
_meta_table['Bfd.FlapDamp.Extensions']['meta_info'].parent =_meta_table['Bfd.FlapDamp']['meta_info']
_meta_table['Bfd.EchoLatency.Detect']['meta_info'].parent =_meta_table['Bfd.EchoLatency']['meta_info']
_meta_table['Bfd.Interfaces.Interface']['meta_info'].parent =_meta_table['Bfd.Interfaces']['meta_info']
_meta_table['Bfd.MultiPathIncludes.MultiPathInclude']['meta_info'].parent =_meta_table['Bfd.MultiPathIncludes']['meta_info']
_meta_table['Bfd.Bundle.Coexistence']['meta_info'].parent =_meta_table['Bfd.Bundle']['meta_info']
_meta_table['Bfd.FlapDamp']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.EchoLatency']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.EchoStartup']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Interfaces']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.MultiPathIncludes']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Bundle']['meta_info'].parent =_meta_table['Bfd']['meta_info']
