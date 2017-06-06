


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'LinkLayerAddrEnum' : _MetaInfoEnum('LinkLayerAddrEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg',
        {
            'set':'set',
        }, 'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg']),
    'SubscriberIdEnum' : _MetaInfoEnum('SubscriberIdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg',
        {
            'pppoe':'pppoe',
        }, 'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg']),
    'InsertEnum' : _MetaInfoEnum('InsertEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg',
        {
            'local':'local',
            'received':'received',
            'pppoe':'pppoe',
        }, 'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg']),
    'Dhcpv6.Database' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Database',
            False, 
            [
            _MetaInfoClassMember('full-write-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '1440')], [], 
                '''                Full file write interval (default 10 minutes)
                ''',
                'full_write_interval',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('incremental-write-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '1440')], [], 
                '''                Incremental file write interval (default 1
                minutes)
                ''',
                'incremental_write_interval',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('proxy', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable DHCP proxy binding database storage to
                file system
                ''',
                'proxy',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('relay', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable DHCP relay binding database storage to
                file system
                ''',
                'relay',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('server', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable DHCP server binding database storage to
                file system
                ''',
                'server',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'database',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('helper-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Server Global unicast address
                ''',
                'helper_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'helper-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Relay.HelperAddresses' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Relay.HelperAddresses',
            False, 
            [
            _MetaInfoClassMember('helper-address', REFERENCE_LIST, 'HelperAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress', 
                [], [], 
                '''                Specify the server helper address
                ''',
                'helper_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'helper-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Relay' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Relay',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable None. Deletion of this object also
                causes deletion of all associated objects
                under Relay.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('helper-addresses', REFERENCE_CLASS, 'HelperAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Relay.HelperAddresses', 
                [], [], 
                '''                Table of HelperAddress
                ''',
                'helper_addresses',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('iana-route-add', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable route addition for IANA
                ''',
                'iana_route_add',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'relay',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Base.Default.Profile_' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Base.Default.Profile_',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('proxy-mode', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify mode-class based Proxy Option
                ''',
                'proxy_mode',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('server-mode', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify mode-class based Server option
                ''',
                'server_mode',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'profile',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Base.Default' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Base.Default',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Base.Default.Profile_', 
                [], [], 
                '''                Enter proxy or server profile
                ''',
                'profile',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'default',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Base.Classes.Class_.Profile_' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Base.Classes.Class_.Profile_',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('proxy-mode', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify mode-class based Proxy Option
                ''',
                'proxy_mode',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('server-mode', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify mode-class based Server option
                ''',
                'server_mode',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'profile',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Base.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Base.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 128)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Base.Classes.Class_.Profile_', 
                [], [], 
                '''                Enter proxy or server profile
                ''',
                'profile',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'class',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Base.Classes' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Base.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Base.Classes.Class_', 
                [], [], 
                '''                Specify PPP/IPoE class option
                ''',
                'class_',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'classes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Base' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Base',
            False, 
            [
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Base.Classes', 
                [], [], 
                '''                Enter match option
                ''',
                'classes',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('default', REFERENCE_CLASS, 'Default' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Base.Default', 
                [], [], 
                '''                Default match option
                ''',
                'default',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable None. Deletion of this object also
                causes deletion of all associated objects
                under Base.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'base',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface to configure
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('interface-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Physical interface ID
                ''',
                'interface_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Interfaces' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface', 
                [], [], 
                '''                None
                ''',
                'interface',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId',
            False, 
            [
            _MetaInfoClassMember('insert', REFERENCE_ENUM_CLASS, 'InsertEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'InsertEnum', 
                [], [], 
                '''                Configure InterfaceID insert type
                ''',
                'insert',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'interface-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Relay.Option' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Relay.Option',
            False, 
            [
            _MetaInfoClassMember('interface-id', REFERENCE_CLASS, 'InterfaceId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId', 
                [], [], 
                '''                Interface Id option
                ''',
                'interface_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('link-layer-addr', REFERENCE_ENUM_CLASS, 'LinkLayerAddrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'LinkLayerAddrEnum', 
                [], [], 
                '''                Configure Received link-layer-Addr
                ''',
                'link_layer_addr',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('remote-i-dreceived', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set remote-id value from SADB
                ''',
                'remote_i_dreceived',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('remote-id', ATTRIBUTE, 'str' , None, None, 
                [(1, 256)], [], 
                '''                Enter remote-id value
                ''',
                'remote_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('subscriber-id', REFERENCE_ENUM_CLASS, 'SubscriberIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'SubscriberIdEnum', 
                [], [], 
                '''                Configure Received SubscriberID
                ''',
                'subscriber_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'option',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Relay' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Relay',
            False, 
            [
            _MetaInfoClassMember('option', REFERENCE_CLASS, 'Option' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Relay.Option', 
                [], [], 
                '''                Specify relay option configuration
                ''',
                'option',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'relay',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress',
            False, 
            [
            _MetaInfoClassMember('helper-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCPv6 Helper Address
                ''',
                'helper_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('any-out-interface', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                DHCPv6 HelperAddress Output Interface
                ''',
                'any_out_interface',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('out-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                DHCPv6 HelperAddress Specific Output
                Interface
                ''',
                'out_interface',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'helper-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses',
            False, 
            [
            _MetaInfoClassMember('helper-address', REFERENCE_LIST, 'HelperAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress', 
                [], [], 
                '''                DHCPv6 Helper Address
                ''',
                'helper_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'helper-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('helper-addresses', REFERENCE_CLASS, 'HelperAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses', 
                [], [], 
                '''                Table of HelperAddress
                ''',
                'helper_addresses',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Vrfs' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf', 
                [], [], 
                '''                IPv6 DHCP proxy VRF name
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses.HelperAddress' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses.HelperAddress',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('helper-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Server address
                ''',
                'helper_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'helper-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses',
            False, 
            [
            _MetaInfoClassMember('helper-address', REFERENCE_LIST, 'HelperAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses.HelperAddress', 
                [], [], 
                '''                Specify the server helper address
                ''',
                'helper_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'helper-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 128)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('helper-addresses', REFERENCE_CLASS, 'HelperAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses', 
                [], [], 
                '''                Table of HelperAddress
                ''',
                'helper_addresses',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('link-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv6 address to be filled in link-address
                ''',
                'link_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False, [
                    _MetaInfoClassMember('link-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address to be filled in link-address
                        ''',
                        'link_address',
                        'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
                    _MetaInfoClassMember('link-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address to be filled in link-address
                        ''',
                        'link_address',
                        'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'class',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Classes' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Classes.Class_', 
                [], [], 
                '''                None
                ''',
                'class_',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'classes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle',
            False, 
            [
            _MetaInfoClassMember('block', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Throttle blocking period (in secs)
                ''',
                'block',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Number of solicits at which to throttle
                ''',
                'limit',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('request', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Throttle request period (in secs)
                ''',
                'request',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac',
            False, 
            [
            _MetaInfoClassMember('throttle', REFERENCE_CLASS, 'Throttle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle', 
                [], [], 
                '''                Throttle DHCP sessions from any one MAC
                address
                ''',
                'throttle',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'mac',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Sessions' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Sessions',
            False, 
            [
            _MetaInfoClassMember('mac', REFERENCE_CLASS, 'Mac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac', 
                [], [], 
                '''                Throttle DHCP sessions based on MAC address
                ''',
                'mac',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy',
            False, 
            [
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Classes', 
                [], [], 
                '''                Table of Class
                ''',
                'classes',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable None. Deletion of this object also
                causes deletion of all associated objects
                under Proxy.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Interfaces', 
                [], [], 
                '''                Table of Interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('link-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv6 address to be filled in link-address
                ''',
                'link_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False, [
                    _MetaInfoClassMember('link-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address to be filled in link-address
                        ''',
                        'link_address',
                        'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
                    _MetaInfoClassMember('link-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address to be filled in link-address
                        ''',
                        'link_address',
                        'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
                ]),
            _MetaInfoClassMember('relay', REFERENCE_CLASS, 'Relay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Relay', 
                [], [], 
                '''                Specify relay configuration
                ''',
                'relay',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('route-add-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RouteDisable
                ''',
                'route_add_disable',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Sessions', 
                [], [], 
                '''                Change sessions configuration
                ''',
                'sessions',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('src-intf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Create or enter proxy profile Source
                Interface Name
                ''',
                'src_intf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Vrfs', 
                [], [], 
                '''                VRF related configuration
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'proxy',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle',
            False, 
            [
            _MetaInfoClassMember('block', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Throttle blocking period (in secs)
                ''',
                'block',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Number of solicits at which to throttle
                ''',
                'limit',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('request', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Throttle request period (in secs)
                ''',
                'request',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server.Sessions.Mac' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server.Sessions.Mac',
            False, 
            [
            _MetaInfoClassMember('throttle', REFERENCE_CLASS, 'Throttle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle', 
                [], [], 
                '''                Throttle DHCP sessions from any one MAC
                address
                ''',
                'throttle',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'mac',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server.Sessions' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server.Sessions',
            False, 
            [
            _MetaInfoClassMember('mac', REFERENCE_CLASS, 'Mac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server.Sessions.Mac', 
                [], [], 
                '''                Throttle DHCP sessions based on MAC address
                ''',
                'mac',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server.DnsServers' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server.DnsServers',
            False, 
            [
            _MetaInfoClassMember('dns-server', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Server's IPv6 address
                ''',
                'dns_server',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False, [
                    _MetaInfoClassMember('dns-server', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Server's IPv6 address
                        ''',
                        'dns_server',
                        'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False, max_elements=8),
                    _MetaInfoClassMember('dns-server', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Server's IPv6 address
                        ''',
                        'dns_server',
                        'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False, max_elements=8),
                ], max_elements=8),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'dns-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server.Classes.Class_.DnsServers' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server.Classes.Class_.DnsServers',
            False, 
            [
            _MetaInfoClassMember('dns-server', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Server's IPv6 address
                ''',
                'dns_server',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False, [
                    _MetaInfoClassMember('dns-server', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Server's IPv6 address
                        ''',
                        'dns_server',
                        'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False, max_elements=8),
                    _MetaInfoClassMember('dns-server', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Server's IPv6 address
                        ''',
                        'dns_server',
                        'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False, max_elements=8),
                ], max_elements=8),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'dns-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 128)], [], 
                '''                class name
                ''',
                'class_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('address-pool', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Address pool name
                ''',
                'address_pool',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('dns-servers', REFERENCE_CLASS, 'DnsServers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server.Classes.Class_.DnsServers', 
                [], [], 
                '''                DNS servers
                ''',
                'dns_servers',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('preference', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                DHCP Server Preference
                ''',
                'preference',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('prefix-pool', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Prefix pool name
                ''',
                'prefix_pool',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'class',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server.Classes' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server.Classes.Class_', 
                [], [], 
                '''                None
                ''',
                'class_',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'classes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server.Lease' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server.Lease',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [('0', '365')], [], 
                '''                Days
                ''',
                'days',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [('0', '23')], [], 
                '''                Hours
                ''',
                'hours',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('infinite', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set string
                ''',
                'infinite',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [('1', '59')], [], 
                '''                Minutes
                ''',
                'minutes',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'lease',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set string
                ''',
                'type',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('vendor-options', ATTRIBUTE, 'str' , None, None, 
                [(1, 512)], [], 
                '''                Vendor options
                ''',
                'vendor_options',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'vendor-options',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server.Dhcpv6Options' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server.Dhcpv6Options',
            False, 
            [
            _MetaInfoClassMember('vendor-options', REFERENCE_CLASS, 'VendorOptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions', 
                [], [], 
                '''                Vendor options
                ''',
                'vendor_options',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'dhcpv6-options',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server',
            False, 
            [
            _MetaInfoClassMember('address-pool', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Address pool name
                ''',
                'address_pool',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('aftr-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                AFTR name
                ''',
                'aftr_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server.Classes', 
                [], [], 
                '''                Table of Class
                ''',
                'classes',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('dhcpv6-options', REFERENCE_CLASS, 'Dhcpv6Options' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server.Dhcpv6Options', 
                [], [], 
                '''                DHCPv6 options
                ''',
                'dhcpv6_options',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('dns-servers', REFERENCE_CLASS, 'DnsServers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server.DnsServers', 
                [], [], 
                '''                DNS servers
                ''',
                'dns_servers',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable None. Deletion of this object also
                causes deletion of all associated objects
                under Server.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('lease', REFERENCE_CLASS, 'Lease' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server.Lease', 
                [], [], 
                '''                lease
                ''',
                'lease',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                DHCP Server Preference
                ''',
                'preference',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('prefix-pool', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Prefix pool name
                ''',
                'prefix_pool',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('rapid-commit', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow RAPID Commit
                ''',
                'rapid_commit',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server.Sessions', 
                [], [], 
                '''                Change sessions configuration
                ''',
                'sessions',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('base', REFERENCE_CLASS, 'Base' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Base', 
                [], [], 
                '''                None
                ''',
                'base',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('proxy', REFERENCE_CLASS, 'Proxy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy', 
                [], [], 
                '''                None
                ''',
                'proxy',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('relay', REFERENCE_CLASS, 'Relay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Relay', 
                [], [], 
                '''                None
                ''',
                'relay',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('server', REFERENCE_CLASS, 'Server' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server', 
                [], [], 
                '''                None
                ''',
                'server',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'profile',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile', 
                [], [], 
                '''                None
                ''',
                'profile',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'profiles',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Interfaces.Interface.Pppoe' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Interfaces.Interface.Pppoe',
            False, 
            [
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Enter profile name
                ''',
                'profile',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Interfaces.Interface.Proxy' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Interfaces.Interface.Proxy',
            False, 
            [
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Enter profile name
                ''',
                'profile',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'proxy',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Interfaces.Interface.Base' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Interfaces.Interface.Base',
            False, 
            [
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Enter profile name
                ''',
                'profile',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'base',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Interfaces.Interface.Server' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Interfaces.Interface.Server',
            False, 
            [
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Enter profile name
                ''',
                'profile',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Interfaces.Interface.Relay' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Interfaces.Interface.Relay',
            False, 
            [
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Enter profile name
                ''',
                'profile',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'relay',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface to configure
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('base', REFERENCE_CLASS, 'Base' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Interfaces.Interface.Base', 
                [], [], 
                '''                Assign a base profile to interface
                ''',
                'base',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Interfaces.Interface.Pppoe', 
                [], [], 
                '''                PPPoE subscriber interface
                ''',
                'pppoe',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('proxy', REFERENCE_CLASS, 'Proxy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Interfaces.Interface.Proxy', 
                [], [], 
                '''                Assign a proxy profile to interface
                ''',
                'proxy',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('relay', REFERENCE_CLASS, 'Relay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Interfaces.Interface.Relay', 
                [], [], 
                '''                Assign a relay profile to interface
                ''',
                'relay',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('server', REFERENCE_CLASS, 'Server' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Interfaces.Interface.Server', 
                [], [], 
                '''                Assign a server profile to interface
                ''',
                'server',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Interfaces' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Interfaces.Interface', 
                [], [], 
                '''                None
                ''',
                'interface',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6' : {
        'meta_info' : _MetaInfoClass('Dhcpv6',
            False, 
            [
            _MetaInfoClassMember('allow-duid-change', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                For BNG session, allow duid change for a client
                MAC
                ''',
                'allow_duid_change',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('database', REFERENCE_CLASS, 'Database' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Database', 
                [], [], 
                '''                Enable DHCP binding database storage to file
                system
                ''',
                'database',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable None. Deletion of this object also causes
                deletion of all associated objects under DHCPv6.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Interfaces', 
                [], [], 
                '''                Table of Interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('profiles', REFERENCE_CLASS, 'Profiles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles', 
                [], [], 
                '''                Table of Profile
                ''',
                'profiles',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'dhcpv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
}
_meta_table['Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Relay.HelperAddresses']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Relay.HelperAddresses']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Relay']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Base.Default.Profile_']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Base.Default']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Base.Classes.Class_.Profile_']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Base.Classes.Class_']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Base.Classes.Class_']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Base.Classes']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Base.Default']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Base']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Base.Classes']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Base']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Interfaces']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Relay.Option']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Relay.Option']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Relay']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses.HelperAddress']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes.Class_']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes.Class_']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Sessions']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Interfaces']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Relay']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Sessions']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Server.Sessions.Mac']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server.Sessions.Mac']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Server.Sessions']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server.Classes.Class_.DnsServers']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Server.Classes.Class_']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server.Classes.Class_']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Server.Classes']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Server.Dhcpv6Options']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server.Sessions']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Server']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server.DnsServers']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Server']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server.Classes']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Server']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server.Lease']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Server']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server.Dhcpv6Options']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Server']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Relay']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Base']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile']['meta_info'].parent =_meta_table['Dhcpv6.Profiles']['meta_info']
_meta_table['Dhcpv6.Interfaces.Interface.Pppoe']['meta_info'].parent =_meta_table['Dhcpv6.Interfaces.Interface']['meta_info']
_meta_table['Dhcpv6.Interfaces.Interface.Proxy']['meta_info'].parent =_meta_table['Dhcpv6.Interfaces.Interface']['meta_info']
_meta_table['Dhcpv6.Interfaces.Interface.Base']['meta_info'].parent =_meta_table['Dhcpv6.Interfaces.Interface']['meta_info']
_meta_table['Dhcpv6.Interfaces.Interface.Server']['meta_info'].parent =_meta_table['Dhcpv6.Interfaces.Interface']['meta_info']
_meta_table['Dhcpv6.Interfaces.Interface.Relay']['meta_info'].parent =_meta_table['Dhcpv6.Interfaces.Interface']['meta_info']
_meta_table['Dhcpv6.Interfaces.Interface']['meta_info'].parent =_meta_table['Dhcpv6.Interfaces']['meta_info']
_meta_table['Dhcpv6.Database']['meta_info'].parent =_meta_table['Dhcpv6']['meta_info']
_meta_table['Dhcpv6.Profiles']['meta_info'].parent =_meta_table['Dhcpv6']['meta_info']
_meta_table['Dhcpv6.Interfaces']['meta_info'].parent =_meta_table['Dhcpv6']['meta_info']
