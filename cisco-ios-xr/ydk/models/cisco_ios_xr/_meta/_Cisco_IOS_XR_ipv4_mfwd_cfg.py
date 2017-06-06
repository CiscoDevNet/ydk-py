


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AccountingModeEnum' : _MetaInfoEnum('AccountingModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg',
        {
            'enable':'enable',
            'forward-only-enable':'forward_only_enable',
        }, 'Cisco-IOS-XR-ipv4-mfwd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg']),
    'Mfwd.DefaultContext.Ipv6.StaticRpfRules.StaticRpfRule' : {
        'meta_info' : _MetaInfoClass('Mfwd.DefaultContext.Ipv6.StaticRpfRules.StaticRpfRule',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of the RPF prefix
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the RPF prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-mfwd-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the RPF prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-mfwd-cfg', True),
                ]),
            _MetaInfoClassMember('prefix-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Prefix mask of the RPF Prefix
                ''',
                'prefix_mask',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the RPF interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address of the RPF Prefix
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address of the RPF Prefix
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address of the RPF Prefix
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'static-rpf-rule',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.DefaultContext.Ipv6.StaticRpfRules' : {
        'meta_info' : _MetaInfoClass('Mfwd.DefaultContext.Ipv6.StaticRpfRules',
            False, 
            [
            _MetaInfoClassMember('static-rpf-rule', REFERENCE_LIST, 'StaticRpfRule' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.DefaultContext.Ipv6.StaticRpfRules.StaticRpfRule', 
                [], [], 
                '''                RPF prefix address and mask
                ''',
                'static_rpf_rule',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'static-rpf-rules',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.DefaultContext.Ipv6.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Mfwd.DefaultContext.Ipv6.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', True),
            _MetaInfoClassMember('boundary', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Boundary for administratively scoped multicast
                addresses
                ''',
                'boundary',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('enable-on-interface', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable IP multicast on the
                interface
                ''',
                'enable_on_interface',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('ttl-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                TTL threshold for multicast packets
                ''',
                'ttl_threshold',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.DefaultContext.Ipv6.Interfaces' : {
        'meta_info' : _MetaInfoClass('Mfwd.DefaultContext.Ipv6.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.DefaultContext.Ipv6.Interfaces.Interface', 
                [], [], 
                '''                The name of the interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.DefaultContext.Ipv6' : {
        'meta_info' : _MetaInfoClass('Mfwd.DefaultContext.Ipv6',
            False, 
            [
            _MetaInfoClassMember('accounting', REFERENCE_ENUM_CLASS, 'AccountingModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'AccountingModeEnum', 
                [], [], 
                '''                Per-prefix accounting mode
                ''',
                'accounting',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('enable-on-all-interfaces', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure all interfaces for multicast routing
                and forwarding
                ''',
                'enable_on_all_interfaces',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('forwarding-latency', ATTRIBUTE, 'int' , None, None, 
                [('5', '500')], [], 
                '''                Knob to delay traffic being forwarded on a route
                ''',
                'forwarding_latency',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('interface-inheritance-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable interface inheritance configuration
                ''',
                'interface_inheritance_disable',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.DefaultContext.Ipv6.Interfaces', 
                [], [], 
                '''                Interface-level Configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('log-traps', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging trap event
                ''',
                'log_traps',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('maximum-checking-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable state limit maximum checking
                ''',
                'maximum_checking_disable',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('mofrr-lockout-timer-config', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Mofrr Lockout timer value
                ''',
                'mofrr_lockout_timer_config',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('mofrr-loss-detection-timer-config', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Mofrr Loss Detection timer value
                ''',
                'mofrr_loss_detection_timer_config',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('multicast-forwarding', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable IP multicast routing and forwarding
                ''',
                'multicast_forwarding',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('rate-per-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable per (S,G) rate calculation
                ''',
                'rate_per_route',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('static-rpf-rules', REFERENCE_CLASS, 'StaticRpfRules' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.DefaultContext.Ipv6.StaticRpfRules', 
                [], [], 
                '''                Configure a static RPF rule for a given prefix
                ''',
                'static_rpf_rules',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.DefaultContext.Ipv4.StaticRpfRules.StaticRpfRule' : {
        'meta_info' : _MetaInfoClass('Mfwd.DefaultContext.Ipv4.StaticRpfRules.StaticRpfRule',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of the RPF prefix
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the RPF prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-mfwd-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the RPF prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-mfwd-cfg', True),
                ]),
            _MetaInfoClassMember('prefix-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Prefix mask of the RPF Prefix
                ''',
                'prefix_mask',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the RPF interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address of the RPF Prefix
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address of the RPF Prefix
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address of the RPF Prefix
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'static-rpf-rule',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.DefaultContext.Ipv4.StaticRpfRules' : {
        'meta_info' : _MetaInfoClass('Mfwd.DefaultContext.Ipv4.StaticRpfRules',
            False, 
            [
            _MetaInfoClassMember('static-rpf-rule', REFERENCE_LIST, 'StaticRpfRule' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.DefaultContext.Ipv4.StaticRpfRules.StaticRpfRule', 
                [], [], 
                '''                RPF prefix address and mask
                ''',
                'static_rpf_rule',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'static-rpf-rules',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.DefaultContext.Ipv4.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Mfwd.DefaultContext.Ipv4.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', True),
            _MetaInfoClassMember('boundary', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Boundary for administratively scoped multicast
                addresses
                ''',
                'boundary',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('enable-on-interface', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable IP multicast on the
                interface
                ''',
                'enable_on_interface',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('ttl-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                TTL threshold for multicast packets
                ''',
                'ttl_threshold',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.DefaultContext.Ipv4.Interfaces' : {
        'meta_info' : _MetaInfoClass('Mfwd.DefaultContext.Ipv4.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.DefaultContext.Ipv4.Interfaces.Interface', 
                [], [], 
                '''                The name of the interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.DefaultContext.Ipv4' : {
        'meta_info' : _MetaInfoClass('Mfwd.DefaultContext.Ipv4',
            False, 
            [
            _MetaInfoClassMember('accounting', REFERENCE_ENUM_CLASS, 'AccountingModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'AccountingModeEnum', 
                [], [], 
                '''                Per-prefix accounting mode
                ''',
                'accounting',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('enable-on-all-interfaces', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure all interfaces for multicast routing
                and forwarding
                ''',
                'enable_on_all_interfaces',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('forwarding-latency', ATTRIBUTE, 'int' , None, None, 
                [('5', '500')], [], 
                '''                Knob to delay traffic being forwarded on a route
                ''',
                'forwarding_latency',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('interface-inheritance-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable interface inheritance configuration
                ''',
                'interface_inheritance_disable',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.DefaultContext.Ipv4.Interfaces', 
                [], [], 
                '''                Interface-level Configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('log-traps', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging trap event
                ''',
                'log_traps',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('maximum-checking-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable state limit maximum checking
                ''',
                'maximum_checking_disable',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('mofrr-lockout-timer-config', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Mofrr Lockout timer value
                ''',
                'mofrr_lockout_timer_config',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('mofrr-loss-detection-timer-config', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Mofrr Loss Detection timer value
                ''',
                'mofrr_loss_detection_timer_config',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('multicast-forwarding', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable IP multicast routing and forwarding
                ''',
                'multicast_forwarding',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('out-of-memory-handling', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable out-of-memory handling
                ''',
                'out_of_memory_handling',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('rate-per-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable per (S,G) rate calculation
                ''',
                'rate_per_route',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('static-rpf-rules', REFERENCE_CLASS, 'StaticRpfRules' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.DefaultContext.Ipv4.StaticRpfRules', 
                [], [], 
                '''                Configure a static RPF rule for a given prefix
                ''',
                'static_rpf_rules',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.DefaultContext' : {
        'meta_info' : _MetaInfoClass('Mfwd.DefaultContext',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.DefaultContext.Ipv4', 
                [], [], 
                '''                IPV4 commands in the default context
                ''',
                'ipv4',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.DefaultContext.Ipv6', 
                [], [], 
                '''                IPV6 commands in the default context
                ''',
                'ipv6',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'default-context',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules.StaticRpfRule' : {
        'meta_info' : _MetaInfoClass('Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules.StaticRpfRule',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of the RPF prefix
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the RPF prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-mfwd-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the RPF prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-mfwd-cfg', True),
                ]),
            _MetaInfoClassMember('prefix-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Prefix mask of the RPF Prefix
                ''',
                'prefix_mask',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the RPF interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address of the RPF Prefix
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address of the RPF Prefix
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address of the RPF Prefix
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'static-rpf-rule',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules' : {
        'meta_info' : _MetaInfoClass('Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules',
            False, 
            [
            _MetaInfoClassMember('static-rpf-rule', REFERENCE_LIST, 'StaticRpfRule' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules.StaticRpfRule', 
                [], [], 
                '''                RPF prefix address and mask
                ''',
                'static_rpf_rule',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'static-rpf-rules',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.Vrfs.Vrf.Ipv6.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Mfwd.Vrfs.Vrf.Ipv6.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', True),
            _MetaInfoClassMember('boundary', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Boundary for administratively scoped multicast
                addresses
                ''',
                'boundary',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('enable-on-interface', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable IP multicast on the
                interface
                ''',
                'enable_on_interface',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('ttl-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                TTL threshold for multicast packets
                ''',
                'ttl_threshold',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.Vrfs.Vrf.Ipv6.Interfaces' : {
        'meta_info' : _MetaInfoClass('Mfwd.Vrfs.Vrf.Ipv6.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.Vrfs.Vrf.Ipv6.Interfaces.Interface', 
                [], [], 
                '''                The name of the interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.Vrfs.Vrf.Ipv6' : {
        'meta_info' : _MetaInfoClass('Mfwd.Vrfs.Vrf.Ipv6',
            False, 
            [
            _MetaInfoClassMember('accounting', REFERENCE_ENUM_CLASS, 'AccountingModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'AccountingModeEnum', 
                [], [], 
                '''                Per-prefix accounting mode
                ''',
                'accounting',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('enable-on-all-interfaces', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure all interfaces for multicast routing
                and forwarding
                ''',
                'enable_on_all_interfaces',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.Vrfs.Vrf.Ipv6.Interfaces', 
                [], [], 
                '''                Interface-level Configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('log-traps', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging trap event
                ''',
                'log_traps',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('multicast-forwarding', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable IP multicast routing and forwarding
                ''',
                'multicast_forwarding',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('rate-per-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable per (S,G) rate calculation
                ''',
                'rate_per_route',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('static-rpf-rules', REFERENCE_CLASS, 'StaticRpfRules' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules', 
                [], [], 
                '''                Configure a static RPF rule for a given prefix
                ''',
                'static_rpf_rules',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules.StaticRpfRule' : {
        'meta_info' : _MetaInfoClass('Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules.StaticRpfRule',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of the RPF prefix
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the RPF prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-mfwd-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the RPF prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-mfwd-cfg', True),
                ]),
            _MetaInfoClassMember('prefix-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Prefix mask of the RPF Prefix
                ''',
                'prefix_mask',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the RPF interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address of the RPF Prefix
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address of the RPF Prefix
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address of the RPF Prefix
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'static-rpf-rule',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules' : {
        'meta_info' : _MetaInfoClass('Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules',
            False, 
            [
            _MetaInfoClassMember('static-rpf-rule', REFERENCE_LIST, 'StaticRpfRule' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules.StaticRpfRule', 
                [], [], 
                '''                RPF prefix address and mask
                ''',
                'static_rpf_rule',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'static-rpf-rules',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.Vrfs.Vrf.Ipv4.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Mfwd.Vrfs.Vrf.Ipv4.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', True),
            _MetaInfoClassMember('boundary', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Boundary for administratively scoped multicast
                addresses
                ''',
                'boundary',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('enable-on-interface', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable IP multicast on the
                interface
                ''',
                'enable_on_interface',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('ttl-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                TTL threshold for multicast packets
                ''',
                'ttl_threshold',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.Vrfs.Vrf.Ipv4.Interfaces' : {
        'meta_info' : _MetaInfoClass('Mfwd.Vrfs.Vrf.Ipv4.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.Vrfs.Vrf.Ipv4.Interfaces.Interface', 
                [], [], 
                '''                The name of the interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.Vrfs.Vrf.Ipv4' : {
        'meta_info' : _MetaInfoClass('Mfwd.Vrfs.Vrf.Ipv4',
            False, 
            [
            _MetaInfoClassMember('accounting', REFERENCE_ENUM_CLASS, 'AccountingModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'AccountingModeEnum', 
                [], [], 
                '''                Per-prefix accounting mode
                ''',
                'accounting',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('enable-on-all-interfaces', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure all interfaces for multicast routing
                and forwarding
                ''',
                'enable_on_all_interfaces',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.Vrfs.Vrf.Ipv4.Interfaces', 
                [], [], 
                '''                Interface-level Configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('log-traps', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging trap event
                ''',
                'log_traps',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('multicast-forwarding', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable IP multicast routing and forwarding
                ''',
                'multicast_forwarding',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('rate-per-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable per (S,G) rate calculation
                ''',
                'rate_per_route',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('static-rpf-rules', REFERENCE_CLASS, 'StaticRpfRules' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules', 
                [], [], 
                '''                Configure a static RPF rule for a given prefix
                ''',
                'static_rpf_rules',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Mfwd.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', True),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.Vrfs.Vrf.Ipv4', 
                [], [], 
                '''                VRF table for IPV4 commands
                ''',
                'ipv4',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.Vrfs.Vrf.Ipv6', 
                [], [], 
                '''                VRF table for IPV6 commands
                ''',
                'ipv6',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd.Vrfs' : {
        'meta_info' : _MetaInfoClass('Mfwd.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.Vrfs.Vrf', 
                [], [], 
                '''                VRF table names
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
    'Mfwd' : {
        'meta_info' : _MetaInfoClass('Mfwd',
            False, 
            [
            _MetaInfoClassMember('default-context', REFERENCE_CLASS, 'DefaultContext' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.DefaultContext', 
                [], [], 
                '''                Default Context
                ''',
                'default_context',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'Mfwd.Vrfs', 
                [], [], 
                '''                VRF Table
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-mfwd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-mfwd-cfg',
            'mfwd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-mfwd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg'
        ),
    },
}
_meta_table['Mfwd.DefaultContext.Ipv6.StaticRpfRules.StaticRpfRule']['meta_info'].parent =_meta_table['Mfwd.DefaultContext.Ipv6.StaticRpfRules']['meta_info']
_meta_table['Mfwd.DefaultContext.Ipv6.Interfaces.Interface']['meta_info'].parent =_meta_table['Mfwd.DefaultContext.Ipv6.Interfaces']['meta_info']
_meta_table['Mfwd.DefaultContext.Ipv6.StaticRpfRules']['meta_info'].parent =_meta_table['Mfwd.DefaultContext.Ipv6']['meta_info']
_meta_table['Mfwd.DefaultContext.Ipv6.Interfaces']['meta_info'].parent =_meta_table['Mfwd.DefaultContext.Ipv6']['meta_info']
_meta_table['Mfwd.DefaultContext.Ipv4.StaticRpfRules.StaticRpfRule']['meta_info'].parent =_meta_table['Mfwd.DefaultContext.Ipv4.StaticRpfRules']['meta_info']
_meta_table['Mfwd.DefaultContext.Ipv4.Interfaces.Interface']['meta_info'].parent =_meta_table['Mfwd.DefaultContext.Ipv4.Interfaces']['meta_info']
_meta_table['Mfwd.DefaultContext.Ipv4.StaticRpfRules']['meta_info'].parent =_meta_table['Mfwd.DefaultContext.Ipv4']['meta_info']
_meta_table['Mfwd.DefaultContext.Ipv4.Interfaces']['meta_info'].parent =_meta_table['Mfwd.DefaultContext.Ipv4']['meta_info']
_meta_table['Mfwd.DefaultContext.Ipv6']['meta_info'].parent =_meta_table['Mfwd.DefaultContext']['meta_info']
_meta_table['Mfwd.DefaultContext.Ipv4']['meta_info'].parent =_meta_table['Mfwd.DefaultContext']['meta_info']
_meta_table['Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules.StaticRpfRule']['meta_info'].parent =_meta_table['Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules']['meta_info']
_meta_table['Mfwd.Vrfs.Vrf.Ipv6.Interfaces.Interface']['meta_info'].parent =_meta_table['Mfwd.Vrfs.Vrf.Ipv6.Interfaces']['meta_info']
_meta_table['Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules']['meta_info'].parent =_meta_table['Mfwd.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Mfwd.Vrfs.Vrf.Ipv6.Interfaces']['meta_info'].parent =_meta_table['Mfwd.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules.StaticRpfRule']['meta_info'].parent =_meta_table['Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules']['meta_info']
_meta_table['Mfwd.Vrfs.Vrf.Ipv4.Interfaces.Interface']['meta_info'].parent =_meta_table['Mfwd.Vrfs.Vrf.Ipv4.Interfaces']['meta_info']
_meta_table['Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules']['meta_info'].parent =_meta_table['Mfwd.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Mfwd.Vrfs.Vrf.Ipv4.Interfaces']['meta_info'].parent =_meta_table['Mfwd.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Mfwd.Vrfs.Vrf.Ipv6']['meta_info'].parent =_meta_table['Mfwd.Vrfs.Vrf']['meta_info']
_meta_table['Mfwd.Vrfs.Vrf.Ipv4']['meta_info'].parent =_meta_table['Mfwd.Vrfs.Vrf']['meta_info']
_meta_table['Mfwd.Vrfs.Vrf']['meta_info'].parent =_meta_table['Mfwd.Vrfs']['meta_info']
_meta_table['Mfwd.DefaultContext']['meta_info'].parent =_meta_table['Mfwd']['meta_info']
_meta_table['Mfwd.Vrfs']['meta_info'].parent =_meta_table['Mfwd']['meta_info']
