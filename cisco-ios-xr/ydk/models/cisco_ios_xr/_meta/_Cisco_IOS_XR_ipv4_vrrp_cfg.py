


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Vrrp.Logging' : {
        'meta_info' : _MetaInfoClass('Vrrp.Logging',
            False, 
            [
            _MetaInfoClassMember('state-change-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                VRRP state change IOS messages disable
                ''',
                'state_change_disable',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                VRRP virtual global IPv6 address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        VRRP virtual global IPv6 address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        VRRP virtual global IPv6 address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'global-ipv6-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses',
            False, 
            [
            _MetaInfoClassMember('global-ipv6-address', REFERENCE_LIST, 'GlobalIpv6Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address', 
                [], [], 
                '''                A VRRP virtual global IPv6 IP address
                ''',
                'global_ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'global-ipv6-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Object to be tracked, interface name for
                interfaces
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Priority decrement
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'track',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks',
            False, 
            [
            _MetaInfoClassMember('track', REFERENCE_LIST, 'Track' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track', 
                [], [], 
                '''                Object to be tracked
                ''',
                'track',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer',
            False, 
            [
            _MetaInfoClassMember('advertisement-time-in-msec', ATTRIBUTE, 'int' , None, None, 
                [('100', '40950')], [], 
                '''                Advertisement time in milliseconds
                ''',
                'advertisement_time_in_msec',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('advertisement-time-in-sec', ATTRIBUTE, 'int' , None, None, 
                [('1', '40')], [], 
                '''                Advertisement time in seconds
                ''',
                'advertisement_time_in_sec',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('forced', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE - Force configured timer values to
                be used, required when configured in
                milliseconds
                ''',
                'forced',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('in-msec', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE - Advertise time configured in
                milliseconds, FALSE - Advertise time
                configured in seconds
                ''',
                'in_msec',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'timer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Object to be tracked, interface name for
                interfaces
                ''',
                'object_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'tracked-object',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects',
            False, 
            [
            _MetaInfoClassMember('tracked-object', REFERENCE_LIST, 'TrackedObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject', 
                [], [], 
                '''                Object to be tracked
                ''',
                'tracked_object',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'tracked-objects',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address',
            False, 
            [
            _MetaInfoClassMember('auto-configure', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if the virtual linklocal address is
                to be autoconfigured FALSE if an IPv6
                virtual linklocal address is configured
                ''',
                'auto_configure',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                VRRP IPv6 virtual linklocal address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        VRRP IPv6 virtual linklocal address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        VRRP IPv6 virtual linklocal address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'link-local-ipv6-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter',
            False, 
            [
            _MetaInfoClassMember('vr-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                VRID Virtual Router Identifier
                ''',
                'vr_id',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('accept-mode-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Accept Mode for this virtual
                IPAddress
                ''',
                'accept_mode_disable',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Enable use of Bidirectional Forwarding
                Detection for this IP
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, [
                    _MetaInfoClassMember('bfd', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Enable use of Bidirectional Forwarding
                        Detection for this IP
                        ''',
                        'bfd',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
                    _MetaInfoClassMember('bfd', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Enable use of Bidirectional Forwarding
                        Detection for this IP
                        ''',
                        'bfd',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
                ]),
            _MetaInfoClassMember('global-ipv6-addresses', REFERENCE_CLASS, 'GlobalIpv6Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses', 
                [], [], 
                '''                The table of VRRP virtual global IPv6
                addresses
                ''',
                'global_ipv6_addresses',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('link-local-ipv6-address', REFERENCE_CLASS, 'LinkLocalIpv6Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address', 
                [], [], 
                '''                The VRRP IPv6 virtual linklocal address
                ''',
                'link_local_ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Preempt Master router if higher priority
                ''',
                'preempt',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Priority value
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 16)], [], 
                '''                VRRP Session Name
                ''',
                'session_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('timer', REFERENCE_CLASS, 'Timer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer', 
                [], [], 
                '''                Set advertisement timer
                ''',
                'timer',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('tracked-objects', REFERENCE_CLASS, 'TrackedObjects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects', 
                [], [], 
                '''                Track an object, reducing priority if it
                goes down
                ''',
                'tracked_objects',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('tracks', REFERENCE_CLASS, 'Tracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks', 
                [], [], 
                '''                Track an item, reducing priority if it
                goes down
                ''',
                'tracks',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'virtual-router',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters',
            False, 
            [
            _MetaInfoClassMember('virtual-router', REFERENCE_LIST, 'VirtualRouter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter', 
                [], [], 
                '''                The VRRP virtual router being configured
                ''',
                'virtual_router',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'virtual-routers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.Version3' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.Version3',
            False, 
            [
            _MetaInfoClassMember('virtual-routers', REFERENCE_CLASS, 'VirtualRouters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters', 
                [], [], 
                '''                The VRRP virtual router configuration table
                ''',
                'virtual_routers',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'version3',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address',
            False, 
            [
            _MetaInfoClassMember('auto-configure', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if the virtual linklocal address is
                to be autoconfigured FALSE if an IPv6
                virtual linklocal address is configured
                ''',
                'auto_configure',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                VRRP IPv6 virtual linklocal address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        VRRP IPv6 virtual linklocal address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        VRRP IPv6 virtual linklocal address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'link-local-ipv6-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                VRRP virtual global IPv6 address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        VRRP virtual global IPv6 address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        VRRP virtual global IPv6 address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'global-ipv6-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses',
            False, 
            [
            _MetaInfoClassMember('global-ipv6-address', REFERENCE_LIST, 'GlobalIpv6Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address', 
                [], [], 
                '''                A VRRP virtual global IPv6 IP address
                ''',
                'global_ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'global-ipv6-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter',
            False, 
            [
            _MetaInfoClassMember('slave-virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Virtual Router ID
                ''',
                'slave_virtual_router_id',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('accept-mode-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Accept Mode for this virtual
                IPAddress
                ''',
                'accept_mode_disable',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('follow', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRRP Session name for this slave to follow
                ''',
                'follow',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('global-ipv6-addresses', REFERENCE_CLASS, 'GlobalIpv6Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses', 
                [], [], 
                '''                The table of VRRP virtual global IPv6
                addresses
                ''',
                'global_ipv6_addresses',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('link-local-ipv6-address', REFERENCE_CLASS, 'LinkLocalIpv6Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address', 
                [], [], 
                '''                The VRRP IPv6 virtual linklocal address
                ''',
                'link_local_ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'slave-virtual-router',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters',
            False, 
            [
            _MetaInfoClassMember('slave-virtual-router', REFERENCE_LIST, 'SlaveVirtualRouter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter', 
                [], [], 
                '''                The VRRP slave being configured
                ''',
                'slave_virtual_router',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'slave-virtual-routers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv6' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv6',
            False, 
            [
            _MetaInfoClassMember('slave-virtual-routers', REFERENCE_CLASS, 'SlaveVirtualRouters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters', 
                [], [], 
                '''                The VRRP slave group configuration table
                ''',
                'slave_virtual_routers',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('version3', REFERENCE_CLASS, 'Version3' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6.Version3', 
                [], [], 
                '''                Version 3 VRRP configuration
                ''',
                'version3',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Delay' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Delay',
            False, 
            [
            _MetaInfoClassMember('min-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '10000')], [], 
                '''                Minimum delay in seconds
                ''',
                'min_delay',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('reload-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '10000')], [], 
                '''                Reload delay in seconds
                ''',
                'reload_delay',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'delay',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer',
            False, 
            [
            _MetaInfoClassMember('advertisement-time-in-msec', ATTRIBUTE, 'int' , None, None, 
                [('100', '40950')], [], 
                '''                Advertisement time in milliseconds
                ''',
                'advertisement_time_in_msec',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('advertisement-time-in-sec', ATTRIBUTE, 'int' , None, None, 
                [('1', '40')], [], 
                '''                Advertisement time in seconds
                ''',
                'advertisement_time_in_sec',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('forced', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE - Force configured timer values to
                be used, required when configured in
                milliseconds
                ''',
                'forced',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('in-msec', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE - Advertise time configured in
                milliseconds, FALSE - Advertise time
                configured in seconds
                ''',
                'in_msec',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'timer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address',
            False, 
            [
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                VRRP Secondary IPv4 address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'secondary-ipv4-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses',
            False, 
            [
            _MetaInfoClassMember('secondary-ipv4-address', REFERENCE_LIST, 'SecondaryIpv4Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address', 
                [], [], 
                '''                A VRRP secondary IPv4 address
                ''',
                'secondary_ipv4_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'secondary-ipv4-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Object to be tracked, interface name for
                interfaces
                ''',
                'object_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'tracked-object',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects',
            False, 
            [
            _MetaInfoClassMember('tracked-object', REFERENCE_LIST, 'TrackedObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject', 
                [], [], 
                '''                Object to be tracked
                ''',
                'tracked_object',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'tracked-objects',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Object to be tracked, interface name for
                interfaces
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Priority decrement
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'track',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks',
            False, 
            [
            _MetaInfoClassMember('track', REFERENCE_LIST, 'Track' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track', 
                [], [], 
                '''                Object to be tracked
                ''',
                'track',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter',
            False, 
            [
            _MetaInfoClassMember('vr-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                VRID Virtual Router Identifier
                ''',
                'vr_id',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('accept-mode-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Accept Mode for this virtual
                IPAddress
                ''',
                'accept_mode_disable',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('bfd', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Enable use of Bidirectional Forwarding
                Detection for this IP
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Preempt Master router if higher priority
                ''',
                'preempt',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('primary-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Primary VRRP IPv4 address
                ''',
                'primary_ipv4_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Priority value
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('secondary-ipv4-addresses', REFERENCE_CLASS, 'SecondaryIpv4Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses', 
                [], [], 
                '''                The table of VRRP secondary IPv4 addresses
                ''',
                'secondary_ipv4_addresses',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 16)], [], 
                '''                VRRP Session Name
                ''',
                'session_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('timer', REFERENCE_CLASS, 'Timer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer', 
                [], [], 
                '''                Set advertisement timer
                ''',
                'timer',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('tracked-objects', REFERENCE_CLASS, 'TrackedObjects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects', 
                [], [], 
                '''                Track an object, reducing priority if it
                goes down
                ''',
                'tracked_objects',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('tracks', REFERENCE_CLASS, 'Tracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks', 
                [], [], 
                '''                Track an item, reducing priority if it
                goes down
                ''',
                'tracks',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'virtual-router',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters',
            False, 
            [
            _MetaInfoClassMember('virtual-router', REFERENCE_LIST, 'VirtualRouter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter', 
                [], [], 
                '''                The VRRP virtual router being configured
                ''',
                'virtual_router',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'virtual-routers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version3' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version3',
            False, 
            [
            _MetaInfoClassMember('virtual-routers', REFERENCE_CLASS, 'VirtualRouters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters', 
                [], [], 
                '''                The VRRP virtual router configuration table
                ''',
                'virtual_routers',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'version3',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address',
            False, 
            [
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                VRRP Secondary IPv4 address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'secondary-ipv4-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses',
            False, 
            [
            _MetaInfoClassMember('secondary-ipv4-address', REFERENCE_LIST, 'SecondaryIpv4Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address', 
                [], [], 
                '''                A VRRP secondary IPv4 address
                ''',
                'secondary_ipv4_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'secondary-ipv4-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter',
            False, 
            [
            _MetaInfoClassMember('slave-virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Virtual Router ID
                ''',
                'slave_virtual_router_id',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('accept-mode-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Accept Mode for this virtual
                IPAddress
                ''',
                'accept_mode_disable',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('follow', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRRP Session name for this slave to follow
                ''',
                'follow',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('primary-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Primary VRRP IPv4 address
                ''',
                'primary_ipv4_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('secondary-ipv4-addresses', REFERENCE_CLASS, 'SecondaryIpv4Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses', 
                [], [], 
                '''                The table of VRRP secondary IPv4 addresses
                ''',
                'secondary_ipv4_addresses',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'slave-virtual-router',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters',
            False, 
            [
            _MetaInfoClassMember('slave-virtual-router', REFERENCE_LIST, 'SlaveVirtualRouter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter', 
                [], [], 
                '''                The VRRP slave being configured
                ''',
                'slave_virtual_router',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'slave-virtual-routers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer',
            False, 
            [
            _MetaInfoClassMember('advertisement-time-in-msec', ATTRIBUTE, 'int' , None, None, 
                [('100', '40950')], [], 
                '''                Advertisement time in milliseconds
                ''',
                'advertisement_time_in_msec',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('advertisement-time-in-sec', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Advertisement time in seconds
                ''',
                'advertisement_time_in_sec',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('forced', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE - Force configured timer values to
                be used, required when configured in
                milliseconds
                ''',
                'forced',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('in-msec', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE - Advertise time configured in
                milliseconds, FALSE - Advertise time
                configured in seconds
                ''',
                'in_msec',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'timer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address',
            False, 
            [
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                VRRP Secondary IPv4 address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'secondary-ipv4-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses',
            False, 
            [
            _MetaInfoClassMember('secondary-ipv4-address', REFERENCE_LIST, 'SecondaryIpv4Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address', 
                [], [], 
                '''                A VRRP secondary IPv4 address
                ''',
                'secondary_ipv4_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'secondary-ipv4-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Object to be tracked, interface name for
                interfaces
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Priority decrement
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'track',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks',
            False, 
            [
            _MetaInfoClassMember('track', REFERENCE_LIST, 'Track' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track', 
                [], [], 
                '''                Object to be tracked
                ''',
                'track',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Object to be tracked, interface name for
                interfaces
                ''',
                'object_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'tracked-object',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects',
            False, 
            [
            _MetaInfoClassMember('tracked-object', REFERENCE_LIST, 'TrackedObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject', 
                [], [], 
                '''                Object to be tracked
                ''',
                'tracked_object',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'tracked-objects',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter',
            False, 
            [
            _MetaInfoClassMember('vr-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                VRID Virtual Router Identifier
                ''',
                'vr_id',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('accept-mode-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Accept Mode for this virtual
                IPAddress
                ''',
                'accept_mode_disable',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('bfd', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Enable use of Bidirectional Forwarding
                Detection for this IP
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Preempt Master router if higher priority
                ''',
                'preempt',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('primary-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Primary VRRP IPv4 address
                ''',
                'primary_ipv4_address',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Priority value
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('secondary-ipv4-addresses', REFERENCE_CLASS, 'SecondaryIpv4Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses', 
                [], [], 
                '''                The table of VRRP secondary IPv4 addresses
                ''',
                'secondary_ipv4_addresses',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 16)], [], 
                '''                VRRP Session Name
                ''',
                'session_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('text-password', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Authentication password, 8 chars max
                ''',
                'text_password',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('timer', REFERENCE_CLASS, 'Timer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer', 
                [], [], 
                '''                Set advertisement timer
                ''',
                'timer',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('tracked-objects', REFERENCE_CLASS, 'TrackedObjects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects', 
                [], [], 
                '''                Track an object, reducing priority if it
                goes down
                ''',
                'tracked_objects',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('tracks', REFERENCE_CLASS, 'Tracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks', 
                [], [], 
                '''                Track an item, reducing priority if it
                goes down
                ''',
                'tracks',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'virtual-router',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters',
            False, 
            [
            _MetaInfoClassMember('virtual-router', REFERENCE_LIST, 'VirtualRouter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter', 
                [], [], 
                '''                The VRRP virtual router being configured
                ''',
                'virtual_router',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'virtual-routers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4.Version2' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4.Version2',
            False, 
            [
            _MetaInfoClassMember('virtual-routers', REFERENCE_CLASS, 'VirtualRouters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters', 
                [], [], 
                '''                The VRRP virtual router configuration table
                ''',
                'virtual_routers',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'version2',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Ipv4' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Ipv4',
            False, 
            [
            _MetaInfoClassMember('slave-virtual-routers', REFERENCE_CLASS, 'SlaveVirtualRouters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters', 
                [], [], 
                '''                The VRRP slave group configuration table
                ''',
                'slave_virtual_routers',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('version2', REFERENCE_CLASS, 'Version2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version2', 
                [], [], 
                '''                Version 2 VRRP configuration
                ''',
                'version2',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('version3', REFERENCE_CLASS, 'Version3' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4.Version3', 
                [], [], 
                '''                Version 3 VRRP configuration
                ''',
                'version3',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface.Bfd' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '50')], [], 
                '''                Detection multiplier for BFD sessions created
                by vrrp
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval for BFD sessions created by
                vrrp
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name to configure
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', True),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('delay', REFERENCE_CLASS, 'Delay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Delay', 
                [], [], 
                '''                Minimum and Reload Delay
                ''',
                'delay',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv4', 
                [], [], 
                '''                IPv4 VRRP configuration
                ''',
                'ipv4',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface.Ipv6', 
                [], [], 
                '''                IPv6 VRRP configuration
                ''',
                'ipv6',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('mac-refresh', ATTRIBUTE, 'int' , None, None, 
                [('0', '10000')], [], 
                '''                VRRP Slave MAC-refresh rate in seconds
                ''',
                'mac_refresh',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp.Interfaces' : {
        'meta_info' : _MetaInfoClass('Vrrp.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces.Interface', 
                [], [], 
                '''                The interface being configured
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
    'Vrrp' : {
        'meta_info' : _MetaInfoClass('Vrrp',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Interfaces', 
                [], [], 
                '''                Interface configuration table
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg', 'Vrrp.Logging', 
                [], [], 
                '''                VRRP logging options
                ''',
                'logging',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'vrrp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg'
        ),
    },
}
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv6']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface.Ipv4']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv6']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Delay']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Ipv4']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface']['meta_info']
_meta_table['Vrrp.Interfaces.Interface.Bfd']['meta_info'].parent =_meta_table['Vrrp.Interfaces.Interface']['meta_info']
_meta_table['Vrrp.Interfaces.Interface']['meta_info'].parent =_meta_table['Vrrp.Interfaces']['meta_info']
_meta_table['Vrrp.Logging']['meta_info'].parent =_meta_table['Vrrp']['meta_info']
_meta_table['Vrrp.Interfaces']['meta_info'].parent =_meta_table['Vrrp']['meta_info']
