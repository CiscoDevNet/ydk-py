


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'InsertEnum' : _MetaInfoEnum('InsertEnum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg',
        {
            'local':'LOCAL',
            'received':'RECEIVED',
        }, 'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg']),
    'Dhcpv6.Database' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Database',
            False, 
            [
            _MetaInfoClassMember('proxy', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable DHCP proxy binding database storage to
                file system
                ''',
                'proxy',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('server', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable DHCP server binding database storage to
                file system
                ''',
                'server',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('relay', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable DHCP relay binding database storage to
                file system
                ''',
                'relay',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('full-write-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 1440)], [], 
                '''                Full file write interval (default 10 minutes)
                ''',
                'full_write_interval',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('incremental-write-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 1440)], [], 
                '''                Incremental file write interval (default 1
                minutes)
                ''',
                'incremental_write_interval',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'database',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('helper-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Server Global unicast address
                ''',
                'helper_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'helper-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Relay.HelperAddresses' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Relay.HelperAddresses',
            False, 
            [
            _MetaInfoClassMember('helper-address', REFERENCE_LIST, 'HelperAddress' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress', 
                [], [], 
                '''                Specify the server helper address
                ''',
                'helper_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'helper-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Relay' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Relay',
            False, 
            [
            _MetaInfoClassMember('helper-addresses', REFERENCE_CLASS, 'HelperAddresses' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Relay.HelperAddresses', 
                [], [], 
                '''                Table of HelperAddress
                ''',
                'helper_addresses',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable None. Deletion of this object also
                causes deletion of all associated objects
                under Relay.
                ''',
                'enable',
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
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
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
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Interfaces' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface', 
                [], [], 
                '''                None
                ''',
                'interface',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId',
            False, 
            [
            _MetaInfoClassMember('insert', REFERENCE_ENUM_CLASS, 'InsertEnum' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'InsertEnum', 
                [], [], 
                '''                Configure InterfaceID insert type
                ''',
                'insert',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'interface-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Relay.Option' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Relay.Option',
            False, 
            [
            _MetaInfoClassMember('interface-id', REFERENCE_CLASS, 'InterfaceId' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId', 
                [], [], 
                '''                Interface Id option
                ''',
                'interface_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('remote-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Enter remote-id value
                ''',
                'remote_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'option',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Relay' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Relay',
            False, 
            [
            _MetaInfoClassMember('option', REFERENCE_CLASS, 'Option' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Relay.Option', 
                [], [], 
                '''                Specify relay option configuration
                ''',
                'option',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'relay',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress',
            False, 
            [
            _MetaInfoClassMember('helper-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCPv6 Helper Address
                ''',
                'helper_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('out-interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                DHCPv6 HelperAddress Specific Output
                Interface
                ''',
                'out_interface',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('any-out-interface', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                DHCPv6 HelperAddress Output Interface
                ''',
                'any_out_interface',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'helper-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses',
            False, 
            [
            _MetaInfoClassMember('helper-address', REFERENCE_LIST, 'HelperAddress' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress', 
                [], [], 
                '''                DHCPv6 Helper Address
                ''',
                'helper_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'helper-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('helper-addresses', REFERENCE_CLASS, 'HelperAddresses' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses', 
                [], [], 
                '''                Table of HelperAddress
                ''',
                'helper_addresses',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Vrfs' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf', 
                [], [], 
                '''                IPv6 DHCP proxy VRF name
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses.HelperAddress' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses.HelperAddress',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('helper-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Server address
                ''',
                'helper_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'helper-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses',
            False, 
            [
            _MetaInfoClassMember('helper-address', REFERENCE_LIST, 'HelperAddress' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses.HelperAddress', 
                [], [], 
                '''                Specify the server helper address
                ''',
                'helper_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'helper-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Classes.Class' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Classes.Class',
            False, 
            [
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('helper-addresses', REFERENCE_CLASS, 'HelperAddresses' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses', 
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
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address to be filled in link-address
                        ''',
                        'link_address',
                        'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
                    _MetaInfoClassMember('link-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address to be filled in link-address
                        ''',
                        'link_address',
                        'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'class',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Classes' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Classes.Class', 
                [], [], 
                '''                None
                ''',
                'class_',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'classes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle',
            False, 
            [
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of solicits at which to throttle
                ''',
                'limit',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('request', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                Throttle request period (in secs)
                ''',
                'request',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('block', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                Throttle blocking period (in secs)
                ''',
                'block',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac',
            False, 
            [
            _MetaInfoClassMember('throttle', REFERENCE_CLASS, 'Throttle' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle', 
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
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy.Sessions' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy.Sessions',
            False, 
            [
            _MetaInfoClassMember('mac', REFERENCE_CLASS, 'Mac' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac', 
                [], [], 
                '''                Throttle DHCP sessions based on MAC address
                ''',
                'mac',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Proxy' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Proxy',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Interfaces', 
                [], [], 
                '''                Table of Interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('relay', REFERENCE_CLASS, 'Relay' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Relay', 
                [], [], 
                '''                Specify relay configuration
                ''',
                'relay',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Vrfs', 
                [], [], 
                '''                VRF related configuration
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Classes', 
                [], [], 
                '''                Table of Class
                ''',
                'classes',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy.Sessions', 
                [], [], 
                '''                Change sessions configuration
                ''',
                'sessions',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('link-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv6 address to be filled in link-address
                ''',
                'link_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False, [
                    _MetaInfoClassMember('link-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address to be filled in link-address
                        ''',
                        'link_address',
                        'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
                    _MetaInfoClassMember('link-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address to be filled in link-address
                        ''',
                        'link_address',
                        'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
                ]),
            _MetaInfoClassMember('src-intf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Create or enter proxy profile Source
                Interface Name
                ''',
                'src_intf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable None. Deletion of this object also
                causes deletion of all associated objects
                under Proxy.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'proxy',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle',
            False, 
            [
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of solicits at which to throttle
                ''',
                'limit',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('request', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                Throttle request period (in secs)
                ''',
                'request',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('block', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                Throttle blocking period (in secs)
                ''',
                'block',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server.Sessions.Mac' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server.Sessions.Mac',
            False, 
            [
            _MetaInfoClassMember('throttle', REFERENCE_CLASS, 'Throttle' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle', 
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
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server.Sessions' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server.Sessions',
            False, 
            [
            _MetaInfoClassMember('mac', REFERENCE_CLASS, 'Mac' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server.Sessions.Mac', 
                [], [], 
                '''                Throttle DHCP sessions based on MAC address
                ''',
                'mac',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
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
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Server's IPv6 address
                        ''',
                        'dns_server',
                        'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False, max_elements=8),
                    _MetaInfoClassMember('dns-server', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Server's IPv6 address
                        ''',
                        'dns_server',
                        'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False, max_elements=8),
                ], max_elements=8),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'dns-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server.Classes.Class.DnsServers' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server.Classes.Class.DnsServers',
            False, 
            [
            _MetaInfoClassMember('dns-server', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Server's IPv6 address
                ''',
                'dns_server',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False, [
                    _MetaInfoClassMember('dns-server', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Server's IPv6 address
                        ''',
                        'dns_server',
                        'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False, max_elements=8),
                    _MetaInfoClassMember('dns-server', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Server's IPv6 address
                        ''',
                        'dns_server',
                        'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False, max_elements=8),
                ], max_elements=8),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'dns-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server.Classes.Class' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server.Classes.Class',
            False, 
            [
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                class name
                ''',
                'class_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('dns-servers', REFERENCE_CLASS, 'DnsServers' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server.Classes.Class.DnsServers', 
                [], [], 
                '''                DNS servers
                ''',
                'dns_servers',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('address-pool', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Address pool name
                ''',
                'address_pool',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('preference', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                DHCP Server Preference
                ''',
                'preference',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('prefix-pool', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Prefix pool name
                ''',
                'prefix_pool',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'class',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server.Classes' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server.Classes.Class', 
                [], [], 
                '''                None
                ''',
                'class_',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'classes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server.Lease' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server.Lease',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [(0, 365)], [], 
                '''                Days
                ''',
                'days',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [(0, 23)], [], 
                '''                Hours
                ''',
                'hours',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [(1, 59)], [], 
                '''                Minutes
                ''',
                'minutes',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('infinite', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set string
                ''',
                'infinite',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'lease',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile.Server' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile.Server',
            False, 
            [
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server.Sessions', 
                [], [], 
                '''                Change sessions configuration
                ''',
                'sessions',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('dns-servers', REFERENCE_CLASS, 'DnsServers' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server.DnsServers', 
                [], [], 
                '''                DNS servers
                ''',
                'dns_servers',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server.Classes', 
                [], [], 
                '''                Table of Class
                ''',
                'classes',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('lease', REFERENCE_CLASS, 'Lease' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server.Lease', 
                [], [], 
                '''                lease
                ''',
                'lease',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('address-pool', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Address pool name
                ''',
                'address_pool',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('aftr-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                AFTR name
                ''',
                'aftr_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('preference', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                DHCP Server Preference
                ''',
                'preference',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('rapid-commit', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow RAPID Commit
                ''',
                'rapid_commit',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable None. Deletion of this object also
                causes deletion of all associated objects
                under Server.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('prefix-pool', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Prefix pool name
                ''',
                'prefix_pool',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles.Profile' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles.Profile',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('relay', REFERENCE_CLASS, 'Relay' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Relay', 
                [], [], 
                '''                None
                ''',
                'relay',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('proxy', REFERENCE_CLASS, 'Proxy' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Proxy', 
                [], [], 
                '''                None
                ''',
                'proxy',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('server', REFERENCE_CLASS, 'Server' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile.Server', 
                [], [], 
                '''                None
                ''',
                'server',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'profile',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Profiles' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Profiles',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles.Profile', 
                [], [], 
                '''                None
                ''',
                'profile',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'profiles',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Interfaces.Interface.Pppoe' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Interfaces.Interface.Pppoe',
            False, 
            [
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Enter profile name
                ''',
                'profile',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Interfaces.Interface.Proxy' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Interfaces.Interface.Proxy',
            False, 
            [
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Enter profile name
                ''',
                'profile',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'proxy',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Interfaces.Interface.Server' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Interfaces.Interface.Server',
            False, 
            [
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Enter profile name
                ''',
                'profile',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Interfaces.Interface.Relay' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Interfaces.Interface.Relay',
            False, 
            [
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Enter profile name
                ''',
                'profile',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'relay',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface to configure
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', True),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Interfaces.Interface.Pppoe', 
                [], [], 
                '''                PPPoE subscriber interface
                ''',
                'pppoe',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('proxy', REFERENCE_CLASS, 'Proxy' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Interfaces.Interface.Proxy', 
                [], [], 
                '''                Assign a proxy profile to interface
                ''',
                'proxy',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('server', REFERENCE_CLASS, 'Server' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Interfaces.Interface.Server', 
                [], [], 
                '''                Assign a server profile to interface
                ''',
                'server',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('relay', REFERENCE_CLASS, 'Relay' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Interfaces.Interface.Relay', 
                [], [], 
                '''                Assign a relay profile to interface
                ''',
                'relay',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6.Interfaces' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Interfaces.Interface', 
                [], [], 
                '''                None
                ''',
                'interface',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
    'Dhcpv6' : {
        'meta_info' : _MetaInfoClass('Dhcpv6',
            False, 
            [
            _MetaInfoClassMember('database', REFERENCE_CLASS, 'Database' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Database', 
                [], [], 
                '''                Enable DHCP binding database storage to file
                system
                ''',
                'database',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('profiles', REFERENCE_CLASS, 'Profiles' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Profiles', 
                [], [], 
                '''                Table of Profile
                ''',
                'profiles',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Dhcpv6.Interfaces', 
                [], [], 
                '''                Table of Interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable None. Deletion of this object also causes
                deletion of all associated objects under DHCPv6.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            _MetaInfoClassMember('allow-duid-change', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                For BNG session, allow duid change for a client
                MAC
                ''',
                'allow_duid_change',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg',
            'dhcpv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg'
        ),
    },
}
_meta_table['Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Relay.HelperAddresses']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Relay.HelperAddresses']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Relay']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Interfaces']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Relay.Option']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Relay.Option']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Relay']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses.HelperAddress']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes.Class']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes.Class']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy.Sessions']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Interfaces']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Relay']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy.Sessions']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Proxy']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Server.Sessions.Mac']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server.Sessions.Mac']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Server.Sessions']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server.Classes.Class.DnsServers']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Server.Classes.Class']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server.Classes.Class']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Server.Classes']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server.Sessions']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Server']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server.DnsServers']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Server']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server.Classes']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Server']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server.Lease']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile.Server']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Relay']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Proxy']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile.Server']['meta_info'].parent =_meta_table['Dhcpv6.Profiles.Profile']['meta_info']
_meta_table['Dhcpv6.Profiles.Profile']['meta_info'].parent =_meta_table['Dhcpv6.Profiles']['meta_info']
_meta_table['Dhcpv6.Interfaces.Interface.Pppoe']['meta_info'].parent =_meta_table['Dhcpv6.Interfaces.Interface']['meta_info']
_meta_table['Dhcpv6.Interfaces.Interface.Proxy']['meta_info'].parent =_meta_table['Dhcpv6.Interfaces.Interface']['meta_info']
_meta_table['Dhcpv6.Interfaces.Interface.Server']['meta_info'].parent =_meta_table['Dhcpv6.Interfaces.Interface']['meta_info']
_meta_table['Dhcpv6.Interfaces.Interface.Relay']['meta_info'].parent =_meta_table['Dhcpv6.Interfaces.Interface']['meta_info']
_meta_table['Dhcpv6.Interfaces.Interface']['meta_info'].parent =_meta_table['Dhcpv6.Interfaces']['meta_info']
_meta_table['Dhcpv6.Database']['meta_info'].parent =_meta_table['Dhcpv6']['meta_info']
_meta_table['Dhcpv6.Profiles']['meta_info'].parent =_meta_table['Dhcpv6']['meta_info']
_meta_table['Dhcpv6.Interfaces']['meta_info'].parent =_meta_table['Dhcpv6']['meta_info']
