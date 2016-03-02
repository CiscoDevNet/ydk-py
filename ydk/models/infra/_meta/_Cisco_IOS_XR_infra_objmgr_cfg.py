


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'EndPort_Enum' : _MetaInfoEnum('EndPort_Enum', 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg',
        {
            'echo':'ECHO',
            'discard':'DISCARD',
            'daytime':'DAYTIME',
            'chargen':'CHARGEN',
            'ftp-data':'FTP_DATA',
            'ftp':'FTP',
            'ssh':'SSH',
            'telnet':'TELNET',
            'smtp':'SMTP',
            'time':'TIME',
            'nicname':'NICNAME',
            'tacacs':'TACACS',
            'domain':'DOMAIN',
            'gopher':'GOPHER',
            'finger':'FINGER',
            'www':'WWW',
            'host-name':'HOST_NAME',
            'pop2':'POP2',
            'pop3':'POP3',
            'sun-rpc':'SUN_RPC',
            'ident':'IDENT',
            'nntp':'NNTP',
            'bgp':'BGP',
            'irc':'IRC',
            'pim-auto-rp':'PIM_AUTO_RP',
            'exec':'EXEC',
            'login':'LOGIN',
            'cmd':'CMD',
            'lpd':'LPD',
            'uucp':'UUCP',
            'klogin':'KLOGIN',
            'kshell':'KSHELL',
            'talk':'TALK',
            'ldp':'LDP',
        }, 'Cisco-IOS-XR-infra-objmgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg']),
    'PortOperator_Enum' : _MetaInfoEnum('PortOperator_Enum', 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg',
        {
            'equal':'EQUAL',
            'not-equal':'NOT_EQUAL',
            'greater-than':'GREATER_THAN',
            'less-than':'LESS_THAN',
        }, 'Cisco-IOS-XR-infra-objmgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg']),
    'Port_Enum' : _MetaInfoEnum('Port_Enum', 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg',
        {
            'echo':'ECHO',
            'discard':'DISCARD',
            'daytime':'DAYTIME',
            'chargen':'CHARGEN',
            'ftp-data':'FTP_DATA',
            'ftp':'FTP',
            'ssh':'SSH',
            'telnet':'TELNET',
            'smtp':'SMTP',
            'time':'TIME',
            'nicname':'NICNAME',
            'tacacs':'TACACS',
            'domain':'DOMAIN',
            'gopher':'GOPHER',
            'finger':'FINGER',
            'www':'WWW',
            'host-name':'HOST_NAME',
            'pop2':'POP2',
            'pop3':'POP3',
            'sun-rpc':'SUN_RPC',
            'ident':'IDENT',
            'nntp':'NNTP',
            'bgp':'BGP',
            'irc':'IRC',
            'pim-auto-rp':'PIM_AUTO_RP',
            'exec':'EXEC',
            'login':'LOGIN',
            'cmd':'CMD',
            'lpd':'LPD',
            'uucp':'UUCP',
            'klogin':'KLOGIN',
            'kshell':'KSHELL',
            'talk':'TALK',
            'ldp':'LDP',
        }, 'Cisco-IOS-XR-infra-objmgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg']),
    'StartPort_Enum' : _MetaInfoEnum('StartPort_Enum', 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg',
        {
            'echo':'ECHO',
            'discard':'DISCARD',
            'daytime':'DAYTIME',
            'chargen':'CHARGEN',
            'ftp-data':'FTP_DATA',
            'ftp':'FTP',
            'ssh':'SSH',
            'telnet':'TELNET',
            'smtp':'SMTP',
            'time':'TIME',
            'nicname':'NICNAME',
            'tacacs':'TACACS',
            'domain':'DOMAIN',
            'gopher':'GOPHER',
            'finger':'FINGER',
            'www':'WWW',
            'host-name':'HOST_NAME',
            'pop2':'POP2',
            'pop3':'POP3',
            'sun-rpc':'SUN_RPC',
            'ident':'IDENT',
            'nntp':'NNTP',
            'bgp':'BGP',
            'irc':'IRC',
            'pim-auto-rp':'PIM_AUTO_RP',
            'exec':'EXEC',
            'login':'LOGIN',
            'cmd':'CMD',
            'lpd':'LPD',
            'uucp':'UUCP',
            'klogin':'KLOGIN',
            'kshell':'KSHELL',
            'talk':'TALK',
            'ldp':'LDP',
        }, 'Cisco-IOS-XR-infra-objmgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg']),
    'ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange',
            False, 
            [
            _MetaInfoClassMember('end-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4 address
                ''',
                'end_address',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('end-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address
                        ''',
                        'end_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('end-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address
                        ''',
                        'end_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            _MetaInfoClassMember('start-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4 address
                ''',
                'start_address',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address
                        ''',
                        'start_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address
                        ''',
                        'start_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'address-range',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges',
            False, 
            [
            _MetaInfoClassMember('address-range', REFERENCE_LIST, 'AddressRange' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange', 
                [], [], 
                '''                Range of host addresses
                ''',
                'address_range',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'address-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4 address/prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address/prefix
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address/prefix
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [(0, 32)], [], 
                '''                Prefix of the IP Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-infra-objmgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object.Addresses' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object.Addresses',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address', 
                [], [], 
                '''                IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host',
            False, 
            [
            _MetaInfoClassMember('host-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Host ipv4 address
                ''',
                'host_address',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('host-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Host ipv4 address
                        ''',
                        'host_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('host-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Host ipv4 address
                        ''',
                        'host_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'host',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object.Hosts' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object.Hosts',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host', 
                [], [], 
                '''                A single host address
                ''',
                'host',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup',
            False, 
            [
            _MetaInfoClassMember('nested-group-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Nested object group
                ''',
                'nested_group_name',
                'Cisco-IOS-XR-infra-objmgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'nested-group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups',
            False, 
            [
            _MetaInfoClassMember('nested-group', REFERENCE_LIST, 'NestedGroup' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup', 
                [], [], 
                '''                Nested object group
                ''',
                'nested_group',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'nested-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                IPv4 object group name - maximum 64
                characters
                ''',
                'object_name',
                'Cisco-IOS-XR-infra-objmgr-cfg', True),
            _MetaInfoClassMember('address-ranges', REFERENCE_CLASS, 'AddressRanges' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges', 
                [], [], 
                '''                Table of ipv4 host address ranges
                ''',
                'address_ranges',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.Objects.Object.Addresses', 
                [], [], 
                '''                Table of addresses
                ''',
                'addresses',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 100)], [], 
                '''                Up to 100 characters describing this object
                ''',
                'description',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.Objects.Object.Hosts', 
                [], [], 
                '''                Table of host addresses
                ''',
                'hosts',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('nested-groups', REFERENCE_CLASS, 'NestedGroups' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups', 
                [], [], 
                '''                Table of nested ipv4 object groups
                ''',
                'nested_groups',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'object',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LIST, 'Object' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.Objects.Object', 
                [], [], 
                '''                IPv4 object group
                ''',
                'object',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'objects',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4',
            False, 
            [
            _MetaInfoClassMember('objects', REFERENCE_CLASS, 'Objects' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.Objects', 
                [], [], 
                '''                Table of ipv4 object groups
                ''',
                'objects',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange',
            False, 
            [
            _MetaInfoClassMember('end-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv6 address
                ''',
                'end_address',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('end-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address
                        ''',
                        'end_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('end-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address
                        ''',
                        'end_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            _MetaInfoClassMember('start-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv6 address
                ''',
                'start_address',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address
                        ''',
                        'start_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address
                        ''',
                        'start_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'address-range',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges',
            False, 
            [
            _MetaInfoClassMember('address-range', REFERENCE_LIST, 'AddressRange' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange', 
                [], [], 
                '''                Range of host addresses
                ''',
                'address_range',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'address-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv6 prefix x:x::x/y
                ''',
                'prefix',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 prefix x:x::x/y
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 prefix x:x::x/y
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [(0, 128)], [], 
                '''                Prefix of the IP Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-infra-objmgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object.Addresses' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object.Addresses',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address', 
                [], [], 
                '''                IPv6 address
                ''',
                'address',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host',
            False, 
            [
            _MetaInfoClassMember('host-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                host ipv6 address
                ''',
                'host_address',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('host-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        host ipv6 address
                        ''',
                        'host_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('host-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        host ipv6 address
                        ''',
                        'host_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'host',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object.Hosts' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object.Hosts',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host', 
                [], [], 
                '''                A single host address
                ''',
                'host',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup',
            False, 
            [
            _MetaInfoClassMember('nested-group-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Enter the name of a nested object group
                ''',
                'nested_group_name',
                'Cisco-IOS-XR-infra-objmgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'nested-group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups',
            False, 
            [
            _MetaInfoClassMember('nested-group', REFERENCE_LIST, 'NestedGroup' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup', 
                [], [], 
                '''                nested object group
                ''',
                'nested_group',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'nested-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                IPv6 object group name - maximum 64
                characters
                ''',
                'object_name',
                'Cisco-IOS-XR-infra-objmgr-cfg', True),
            _MetaInfoClassMember('address-ranges', REFERENCE_CLASS, 'AddressRanges' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges', 
                [], [], 
                '''                Table of ipv6 address ranges
                ''',
                'address_ranges',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.Objects.Object.Addresses', 
                [], [], 
                '''                Table of ipv6 addresses
                ''',
                'addresses',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 100)], [], 
                '''                Up to 100 characters describing this object
                ''',
                'description',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.Objects.Object.Hosts', 
                [], [], 
                '''                Table of ipv6 host addresses
                ''',
                'hosts',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('nested-groups', REFERENCE_CLASS, 'NestedGroups' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups', 
                [], [], 
                '''                Table of nested ipv6 object groups
                ''',
                'nested_groups',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'object',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LIST, 'Object' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.Objects.Object', 
                [], [], 
                '''                IPv6 object group
                ''',
                'object',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'objects',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6',
            False, 
            [
            _MetaInfoClassMember('objects', REFERENCE_CLASS, 'Objects' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.Objects', 
                [], [], 
                '''                Table of ipv6 object groups
                ''',
                'objects',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4', 
                [], [], 
                '''                IPv4 object group
                ''',
                'ipv4',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6', 
                [], [], 
                '''                IPv6 object group
                ''',
                'ipv6',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'network',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup',
            False, 
            [
            _MetaInfoClassMember('nested-group-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Name of a nested object group
                ''',
                'nested_group_name',
                'Cisco-IOS-XR-infra-objmgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'nested-group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Port.Objects.Object.NestedGroups' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.Objects.Object.NestedGroups',
            False, 
            [
            _MetaInfoClassMember('nested-group', REFERENCE_LIST, 'NestedGroup' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup', 
                [], [], 
                '''                nested object group
                ''',
                'nested_group',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'nested-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Port.Objects.Object.Operators.Operator' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.Objects.Object.Operators.Operator',
            False, 
            [
            _MetaInfoClassMember('operator-type', REFERENCE_ENUM_CLASS, 'PortOperator_Enum' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'PortOperator_Enum', 
                [], [], 
                '''                operation for ports
                ''',
                'operator_type',
                'Cisco-IOS-XR-infra-objmgr-cfg', True),
            _MetaInfoClassMember('port', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Port number
                ''',
                'port',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('port', REFERENCE_ENUM_CLASS, 'Port_Enum' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'Port_Enum', 
                        [], [], 
                        '''                        Port number
                        ''',
                        'port',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                        [(0, 65535)], [], 
                        '''                        Port number
                        ''',
                        'port',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'operator',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Port.Objects.Object.Operators' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.Objects.Object.Operators',
            False, 
            [
            _MetaInfoClassMember('operator', REFERENCE_LIST, 'Operator' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Port.Objects.Object.Operators.Operator', 
                [], [], 
                '''                op class
                ''',
                'operator',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'operators',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Port.Objects.Object.PortRanges.PortRange' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.Objects.Object.PortRanges.PortRange',
            False, 
            [
            _MetaInfoClassMember('end-port', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Port number
                ''',
                'end_port',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('end-port', REFERENCE_ENUM_CLASS, 'EndPort_Enum' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'EndPort_Enum', 
                        [], [], 
                        '''                        Port number
                        ''',
                        'end_port',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('end-port', ATTRIBUTE, 'int' , None, None, 
                        [(0, 65535)], [], 
                        '''                        Port number
                        ''',
                        'end_port',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            _MetaInfoClassMember('start-port', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Port number
                ''',
                'start_port',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('start-port', REFERENCE_ENUM_CLASS, 'StartPort_Enum' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'StartPort_Enum', 
                        [], [], 
                        '''                        Port number
                        ''',
                        'start_port',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('start-port', ATTRIBUTE, 'int' , None, None, 
                        [(0, 65535)], [], 
                        '''                        Port number
                        ''',
                        'start_port',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'port-range',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Port.Objects.Object.PortRanges' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.Objects.Object.PortRanges',
            False, 
            [
            _MetaInfoClassMember('port-range', REFERENCE_LIST, 'PortRange' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Port.Objects.Object.PortRanges.PortRange', 
                [], [], 
                '''                Match only packets on a given port range
                ''',
                'port_range',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'port-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Port.Objects.Object' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.Objects.Object',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Port object group name - maximum 64
                characters
                ''',
                'object_name',
                'Cisco-IOS-XR-infra-objmgr-cfg', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 100)], [], 
                '''                Up to 100 characters describing this object
                ''',
                'description',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('nested-groups', REFERENCE_CLASS, 'NestedGroups' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Port.Objects.Object.NestedGroups', 
                [], [], 
                '''                Table of nested port object groups
                ''',
                'nested_groups',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('operators', REFERENCE_CLASS, 'Operators' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Port.Objects.Object.Operators', 
                [], [], 
                '''                Table of port operators
                ''',
                'operators',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('port-ranges', REFERENCE_CLASS, 'PortRanges' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Port.Objects.Object.PortRanges', 
                [], [], 
                '''                Table of port range addresses
                ''',
                'port_ranges',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'object',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Port.Objects' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.Objects',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LIST, 'Object' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Port.Objects.Object', 
                [], [], 
                '''                Port object group
                ''',
                'object',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'objects',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Port' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port',
            False, 
            [
            _MetaInfoClassMember('objects', REFERENCE_CLASS, 'Objects' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Port.Objects', 
                [], [], 
                '''                Table of port objects groups
                ''',
                'objects',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'port',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup' : {
        'meta_info' : _MetaInfoClass('ObjectGroup',
            False, 
            [
            _MetaInfoClassMember('network', REFERENCE_CLASS, 'Network' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network', 
                [], [], 
                '''                Network object group
                ''',
                'network',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('port', REFERENCE_CLASS, 'Port' , 'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Port', 
                [], [], 
                '''                Port object group
                ''',
                'port',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'object-group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
}
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Addresses']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Hosts']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Addresses']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Hosts']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Addresses']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Hosts']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Addresses']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Hosts']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4']['meta_info'].parent =_meta_table['ObjectGroup.Network']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6']['meta_info'].parent =_meta_table['ObjectGroup.Network']['meta_info']
_meta_table['ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup']['meta_info'].parent =_meta_table['ObjectGroup.Port.Objects.Object.NestedGroups']['meta_info']
_meta_table['ObjectGroup.Port.Objects.Object.Operators.Operator']['meta_info'].parent =_meta_table['ObjectGroup.Port.Objects.Object.Operators']['meta_info']
_meta_table['ObjectGroup.Port.Objects.Object.PortRanges.PortRange']['meta_info'].parent =_meta_table['ObjectGroup.Port.Objects.Object.PortRanges']['meta_info']
_meta_table['ObjectGroup.Port.Objects.Object.NestedGroups']['meta_info'].parent =_meta_table['ObjectGroup.Port.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Port.Objects.Object.Operators']['meta_info'].parent =_meta_table['ObjectGroup.Port.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Port.Objects.Object.PortRanges']['meta_info'].parent =_meta_table['ObjectGroup.Port.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Port.Objects.Object']['meta_info'].parent =_meta_table['ObjectGroup.Port.Objects']['meta_info']
_meta_table['ObjectGroup.Port.Objects']['meta_info'].parent =_meta_table['ObjectGroup.Port']['meta_info']
_meta_table['ObjectGroup.Network']['meta_info'].parent =_meta_table['ObjectGroup']['meta_info']
_meta_table['ObjectGroup.Port']['meta_info'].parent =_meta_table['ObjectGroup']['meta_info']
