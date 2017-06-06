


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'HsrpLinklocalEnum' : _MetaInfoEnum('HsrpLinklocalEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg',
        {
            'manual':'manual',
            'auto':'auto',
            'legacy':'legacy',
        }, 'Cisco-IOS-XR-ipv4-hsrp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg']),
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Enable BFD for this remote IP
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name to run BFD
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface being tracked
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces',
            False, 
            [
            _MetaInfoClassMember('tracked-interface', REFERENCE_LIST, 'TrackedInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface', 
                [], [], 
                '''                Interface being tracked
                ''',
                'tracked_interface',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Interface being tracked
                ''',
                'object_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-object',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects',
            False, 
            [
            _MetaInfoClassMember('tracked-object', REFERENCE_LIST, 'TrackedObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject', 
                [], [], 
                '''                Object being tracked
                ''',
                'tracked_object',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-objects',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers',
            False, 
            [
            _MetaInfoClassMember('hello-msec', ATTRIBUTE, 'int' , None, None, 
                [('100', '3000')], [], 
                '''                Hello time in msecs
                ''',
                'hello_msec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hello-msec-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE - Hello time configured in
                milliseconds, FALSE - Hello time
                configured in seconds
                ''',
                'hello_msec_flag',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hello-sec', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Hello time in seconds
                ''',
                'hello_sec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hold-msec', ATTRIBUTE, 'int' , None, None, 
                [('100', '3000')], [], 
                '''                Hold time in msecs
                ''',
                'hold_msec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hold-msec-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE - Hold time configured in
                milliseconds, FALSE - Hold time
                configured in seconds
                ''',
                'hold_msec_flag',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hold-sec', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Hold time in seconds
                ''',
                'hold_sec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                HSRP IPv6 virtual linklocal address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('auto-configure', REFERENCE_ENUM_CLASS, 'HsrpLinklocalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'HsrpLinklocalEnum', 
                [], [], 
                '''                Linklocal Configuration Type
                ''',
                'auto_configure',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'link-local-ipv6-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                HSRP virtual global IPv6 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'global-ipv6-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses',
            False, 
            [
            _MetaInfoClassMember('global-ipv6-address', REFERENCE_LIST, 'GlobalIpv6Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address', 
                [], [], 
                '''                A HSRP virtual global IPv6 IP address
                ''',
                'global_ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'global-ipv6-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group',
            False, 
            [
            _MetaInfoClassMember('group-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                HSRP group number
                ''',
                'group_number',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd', 
                [], [], 
                '''                Enable use of Bidirectional Forwarding
                Detection
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('global-ipv6-addresses', REFERENCE_CLASS, 'GlobalIpv6Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses', 
                [], [], 
                '''                The table of HSRP virtual global IPv6
                addresses
                ''',
                'global_ipv6_addresses',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('link-local-ipv6-address', REFERENCE_CLASS, 'LinkLocalIpv6Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address', 
                [], [], 
                '''                The HSRP IPv6 virtual linklocal address
                ''',
                'link_local_ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Force active if higher priority
                ''',
                'preempt',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Priority value
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 16)], [], 
                '''                HSRP Session name (for MGO)
                ''',
                'session_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers', 
                [], [], 
                '''                Hello and hold timers
                ''',
                'timers',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('tracked-interfaces', REFERENCE_CLASS, 'TrackedInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces', 
                [], [], 
                '''                The HSRP tracked interface configuration
                table
                ''',
                'tracked_interfaces',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('tracked-objects', REFERENCE_CLASS, 'TrackedObjects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects', 
                [], [], 
                '''                The HSRP tracked interface configuration
                table
                ''',
                'tracked_objects',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('virtual-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                HSRP MAC address
                ''',
                'virtual_mac_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2.Groups',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group', 
                [], [], 
                '''                The HSRP group being configured
                ''',
                'group',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.Version2' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.Version2',
            False, 
            [
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2.Groups', 
                [], [], 
                '''                The HSRP group configuration table
                ''',
                'groups',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'version2',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                HSRP IPv6 virtual linklocal address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('auto-configure', REFERENCE_ENUM_CLASS, 'HsrpLinklocalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'HsrpLinklocalEnum', 
                [], [], 
                '''                Linklocal Configuration Type
                ''',
                'auto_configure',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'link-local-ipv6-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                HSRP virtual global IPv6 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'global-ipv6-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses',
            False, 
            [
            _MetaInfoClassMember('global-ipv6-address', REFERENCE_LIST, 'GlobalIpv6Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address', 
                [], [], 
                '''                A HSRP virtual global IPv6 IP address
                ''',
                'global_ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'global-ipv6-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup',
            False, 
            [
            _MetaInfoClassMember('slave-group-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                HSRP group number
                ''',
                'slave_group_number',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('follow', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                HSRP Group name for this slave to follow
                ''',
                'follow',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('global-ipv6-addresses', REFERENCE_CLASS, 'GlobalIpv6Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses', 
                [], [], 
                '''                The table of HSRP virtual global IPv6
                addresses
                ''',
                'global_ipv6_addresses',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('link-local-ipv6-address', REFERENCE_CLASS, 'LinkLocalIpv6Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address', 
                [], [], 
                '''                The HSRP IPv6 virtual linklocal address
                ''',
                'link_local_ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('virtual-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                HSRP MAC address
                ''',
                'virtual_mac_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'slave-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6.SlaveGroups',
            False, 
            [
            _MetaInfoClassMember('slave-group', REFERENCE_LIST, 'SlaveGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup', 
                [], [], 
                '''                The HSRP slave group being configured
                ''',
                'slave_group',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'slave-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv6' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv6',
            False, 
            [
            _MetaInfoClassMember('slave-groups', REFERENCE_CLASS, 'SlaveGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.SlaveGroups', 
                [], [], 
                '''                The HSRP slave group configuration table
                ''',
                'slave_groups',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('version2', REFERENCE_CLASS, 'Version2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6.Version2', 
                [], [], 
                '''                Version 2 HSRP configuration
                ''',
                'version2',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Bfd' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '50')], [], 
                '''                Detection multiplier for BFD sessions created
                by hsrp
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval for BFD sessions created by
                hsrp
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Delay' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Delay',
            False, 
            [
            _MetaInfoClassMember('minimum-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '10000')], [], 
                '''                Minimum delay in seconds
                ''',
                'minimum_delay',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('reload-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '10000')], [], 
                '''                Reload delay in seconds
                ''',
                'reload_delay',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'delay',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                HSRP IP address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'secondary-ipv4-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses',
            False, 
            [
            _MetaInfoClassMember('secondary-ipv4-address', REFERENCE_LIST, 'SecondaryIpv4Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address', 
                [], [], 
                '''                Secondary HSRP IP address
                ''',
                'secondary_ipv4_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'secondary-ipv4-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup',
            False, 
            [
            _MetaInfoClassMember('slave-group-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                HSRP group number
                ''',
                'slave_group_number',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('follow', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                HSRP Group name for this slave to follow
                ''',
                'follow',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('primary-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Primary HSRP IP address
                ''',
                'primary_ipv4_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('secondary-ipv4-addresses', REFERENCE_CLASS, 'SecondaryIpv4Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses', 
                [], [], 
                '''                Secondary HSRP IP address Table
                ''',
                'secondary_ipv4_addresses',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('virtual-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                HSRP MAC address
                ''',
                'virtual_mac_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'slave-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.SlaveGroups' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.SlaveGroups',
            False, 
            [
            _MetaInfoClassMember('slave-group', REFERENCE_LIST, 'SlaveGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup', 
                [], [], 
                '''                The HSRP slave group being configured
                ''',
                'slave_group',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'slave-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface being tracked
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces',
            False, 
            [
            _MetaInfoClassMember('tracked-interface', REFERENCE_LIST, 'TrackedInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface', 
                [], [], 
                '''                Interface being tracked
                ''',
                'tracked_interface',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Enable BFD for this remote IP
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name to run BFD
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Interface being tracked
                ''',
                'object_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-object',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects',
            False, 
            [
            _MetaInfoClassMember('tracked-object', REFERENCE_LIST, 'TrackedObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject', 
                [], [], 
                '''                Object being tracked
                ''',
                'tracked_object',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-objects',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers',
            False, 
            [
            _MetaInfoClassMember('hello-msec', ATTRIBUTE, 'int' , None, None, 
                [('100', '3000')], [], 
                '''                Hello time in msecs
                ''',
                'hello_msec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hello-msec-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE - Hello time configured in
                milliseconds, FALSE - Hello time
                configured in seconds
                ''',
                'hello_msec_flag',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hello-sec', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Hello time in seconds
                ''',
                'hello_sec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hold-msec', ATTRIBUTE, 'int' , None, None, 
                [('100', '3000')], [], 
                '''                Hold time in msecs
                ''',
                'hold_msec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hold-msec-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE - Hold time configured in
                milliseconds, FALSE - Hold time
                configured in seconds
                ''',
                'hold_msec_flag',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hold-sec', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Hold time in seconds
                ''',
                'hold_sec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                HSRP IP address.
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('virtual-ip-learn', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if the HSRP protocol is to learn the
                virtual IP address it is to use
                ''',
                'virtual_ip_learn',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'primary-ipv4-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                HSRP IP address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'secondary-ipv4-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses',
            False, 
            [
            _MetaInfoClassMember('secondary-ipv4-address', REFERENCE_LIST, 'SecondaryIpv4Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address', 
                [], [], 
                '''                Secondary HSRP IP address
                ''',
                'secondary_ipv4_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'secondary-ipv4-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group',
            False, 
            [
            _MetaInfoClassMember('group-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                HSRP group number
                ''',
                'group_number',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('authentication', ATTRIBUTE, 'str' , None, None, 
                [(1, 8)], [], 
                '''                Authentication string
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd', 
                [], [], 
                '''                Enable use of Bidirectional Forwarding
                Detection
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Force active if higher priority
                ''',
                'preempt',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('primary-ipv4-address', REFERENCE_CLASS, 'PrimaryIpv4Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address', 
                [], [], 
                '''                Primary HSRP IP address
                ''',
                'primary_ipv4_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Priority value
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('secondary-ipv4-addresses', REFERENCE_CLASS, 'SecondaryIpv4Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses', 
                [], [], 
                '''                Secondary HSRP IP address Table
                ''',
                'secondary_ipv4_addresses',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 16)], [], 
                '''                HSRP Session name (for MGO)
                ''',
                'session_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers', 
                [], [], 
                '''                Hello and hold timers
                ''',
                'timers',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('tracked-interfaces', REFERENCE_CLASS, 'TrackedInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces', 
                [], [], 
                '''                The HSRP tracked interface configuration
                table
                ''',
                'tracked_interfaces',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('tracked-objects', REFERENCE_CLASS, 'TrackedObjects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects', 
                [], [], 
                '''                The HSRP tracked interface configuration
                table
                ''',
                'tracked_objects',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('virtual-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                HSRP MAC address
                ''',
                'virtual_mac_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1.Groups',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group', 
                [], [], 
                '''                The HSRP group being configured
                ''',
                'group',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version1' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version1',
            False, 
            [
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1.Groups', 
                [], [], 
                '''                The HSRP group configuration table
                ''',
                'groups',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'version1',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                HSRP IP address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'secondary-ipv4-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses',
            False, 
            [
            _MetaInfoClassMember('secondary-ipv4-address', REFERENCE_LIST, 'SecondaryIpv4Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address', 
                [], [], 
                '''                Secondary HSRP IP address
                ''',
                'secondary_ipv4_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'secondary-ipv4-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Enable BFD for this remote IP
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name to run BFD
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                HSRP IP address.
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('virtual-ip-learn', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if the HSRP protocol is to learn the
                virtual IP address it is to use
                ''',
                'virtual_ip_learn',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'primary-ipv4-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Interface being tracked
                ''',
                'object_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-object',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects',
            False, 
            [
            _MetaInfoClassMember('tracked-object', REFERENCE_LIST, 'TrackedObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject', 
                [], [], 
                '''                Object being tracked
                ''',
                'tracked_object',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-objects',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface being tracked
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces',
            False, 
            [
            _MetaInfoClassMember('tracked-interface', REFERENCE_LIST, 'TrackedInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface', 
                [], [], 
                '''                Interface being tracked
                ''',
                'tracked_interface',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'tracked-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers',
            False, 
            [
            _MetaInfoClassMember('hello-msec', ATTRIBUTE, 'int' , None, None, 
                [('100', '3000')], [], 
                '''                Hello time in msecs
                ''',
                'hello_msec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hello-msec-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE - Hello time configured in
                milliseconds, FALSE - Hello time
                configured in seconds
                ''',
                'hello_msec_flag',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hello-sec', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Hello time in seconds
                ''',
                'hello_sec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hold-msec', ATTRIBUTE, 'int' , None, None, 
                [('100', '3000')], [], 
                '''                Hold time in msecs
                ''',
                'hold_msec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hold-msec-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE - Hold time configured in
                milliseconds, FALSE - Hold time
                configured in seconds
                ''',
                'hold_msec_flag',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('hold-sec', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Hold time in seconds
                ''',
                'hold_sec',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group',
            False, 
            [
            _MetaInfoClassMember('group-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                HSRP group number
                ''',
                'group_number',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd', 
                [], [], 
                '''                Enable use of Bidirectional Forwarding
                Detection
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Force active if higher priority
                ''',
                'preempt',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('primary-ipv4-address', REFERENCE_CLASS, 'PrimaryIpv4Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address', 
                [], [], 
                '''                Primary HSRP IP address
                ''',
                'primary_ipv4_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Priority value
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('secondary-ipv4-addresses', REFERENCE_CLASS, 'SecondaryIpv4Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses', 
                [], [], 
                '''                Secondary HSRP IP address Table
                ''',
                'secondary_ipv4_addresses',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 16)], [], 
                '''                HSRP Session name (for MGO)
                ''',
                'session_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers', 
                [], [], 
                '''                Hello and hold timers
                ''',
                'timers',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('tracked-interfaces', REFERENCE_CLASS, 'TrackedInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces', 
                [], [], 
                '''                The HSRP tracked interface configuration
                table
                ''',
                'tracked_interfaces',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('tracked-objects', REFERENCE_CLASS, 'TrackedObjects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects', 
                [], [], 
                '''                The HSRP tracked interface configuration
                table
                ''',
                'tracked_objects',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('virtual-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                HSRP MAC address
                ''',
                'virtual_mac_address',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2.Groups',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group', 
                [], [], 
                '''                The HSRP group being configured
                ''',
                'group',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4.Version2' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4.Version2',
            False, 
            [
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2.Groups', 
                [], [], 
                '''                The HSRP group configuration table
                ''',
                'groups',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'version2',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface.Ipv4' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface.Ipv4',
            False, 
            [
            _MetaInfoClassMember('slave-groups', REFERENCE_CLASS, 'SlaveGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.SlaveGroups', 
                [], [], 
                '''                The HSRP slave group configuration table
                ''',
                'slave_groups',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('version1', REFERENCE_CLASS, 'Version1' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version1', 
                [], [], 
                '''                Version 1 HSRP configuration
                ''',
                'version1',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('version2', REFERENCE_CLASS, 'Version2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4.Version2', 
                [], [], 
                '''                Version 2 HSRP configuration
                ''',
                'version2',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', True),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('delay', REFERENCE_CLASS, 'Delay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Delay', 
                [], [], 
                '''                Minimum and Reload Delay
                ''',
                'delay',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv4', 
                [], [], 
                '''                IPv4 HSRP configuration
                ''',
                'ipv4',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface.Ipv6', 
                [], [], 
                '''                IPv6 HSRP configuration
                ''',
                'ipv6',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('mac-refresh', ATTRIBUTE, 'int' , None, None, 
                [('0', '10000')], [], 
                '''                HSRP MGO slave MAC refresh rate
                ''',
                'mac_refresh',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('redirects-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable HSRP filtered ICMP redirects
                ''',
                'redirects_disable',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('use-bia', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Use burned-in address
                ''',
                'use_bia',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Interfaces' : {
        'meta_info' : _MetaInfoClass('Hsrp.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces.Interface', 
                [], [], 
                '''                Per-interface HSRP configuration
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp.Logging' : {
        'meta_info' : _MetaInfoClass('Hsrp.Logging',
            False, 
            [
            _MetaInfoClassMember('state-change-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HSRP state change IOS messages disable
                ''',
                'state_change_disable',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
    'Hsrp' : {
        'meta_info' : _MetaInfoClass('Hsrp',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Interfaces', 
                [], [], 
                '''                Interface Table for HSRP configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'Hsrp.Logging', 
                [], [], 
                '''                HSRP logging options
                ''',
                'logging',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'hsrp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg'
        ),
    },
}
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv6']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.SlaveGroups']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.SlaveGroups']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface.Ipv4']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv6']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Bfd']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Delay']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface']['meta_info']
_meta_table['Hsrp.Interfaces.Interface.Ipv4']['meta_info'].parent =_meta_table['Hsrp.Interfaces.Interface']['meta_info']
_meta_table['Hsrp.Interfaces.Interface']['meta_info'].parent =_meta_table['Hsrp.Interfaces']['meta_info']
_meta_table['Hsrp.Interfaces']['meta_info'].parent =_meta_table['Hsrp']['meta_info']
_meta_table['Hsrp.Logging']['meta_info'].parent =_meta_table['Hsrp']['meta_info']
