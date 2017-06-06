


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EndPortEnum' : _MetaInfoEnum('EndPortEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg',
        {
            'echo':'echo',
            'discard':'discard',
            'daytime':'daytime',
            'chargen':'chargen',
            'ftp-data':'ftp_data',
            'ftp':'ftp',
            'ssh':'ssh',
            'telnet':'telnet',
            'smtp':'smtp',
            'time':'time',
            'nicname':'nicname',
            'tacacs':'tacacs',
            'domain':'domain',
            'gopher':'gopher',
            'finger':'finger',
            'www':'www',
            'host-name':'host_name',
            'pop2':'pop2',
            'pop3':'pop3',
            'sun-rpc':'sun_rpc',
            'ident':'ident',
            'nntp':'nntp',
            'bgp':'bgp',
            'irc':'irc',
            'pim-auto-rp':'pim_auto_rp',
            'exec':'exec_',
            'login':'login',
            'cmd':'cmd',
            'lpd':'lpd',
            'uucp':'uucp',
            'klogin':'klogin',
            'kshell':'kshell',
            'talk':'talk',
            'ldp':'ldp',
        }, 'Cisco-IOS-XR-infra-objmgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg']),
    'PortEnum' : _MetaInfoEnum('PortEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg',
        {
            'echo':'echo',
            'discard':'discard',
            'daytime':'daytime',
            'chargen':'chargen',
            'ftp-data':'ftp_data',
            'ftp':'ftp',
            'ssh':'ssh',
            'telnet':'telnet',
            'smtp':'smtp',
            'time':'time',
            'nicname':'nicname',
            'tacacs':'tacacs',
            'domain':'domain',
            'gopher':'gopher',
            'finger':'finger',
            'www':'www',
            'host-name':'host_name',
            'pop2':'pop2',
            'pop3':'pop3',
            'sun-rpc':'sun_rpc',
            'ident':'ident',
            'nntp':'nntp',
            'bgp':'bgp',
            'irc':'irc',
            'pim-auto-rp':'pim_auto_rp',
            'exec':'exec_',
            'login':'login',
            'cmd':'cmd',
            'lpd':'lpd',
            'uucp':'uucp',
            'klogin':'klogin',
            'kshell':'kshell',
            'talk':'talk',
            'ldp':'ldp',
        }, 'Cisco-IOS-XR-infra-objmgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg']),
    'PortOperatorEnum' : _MetaInfoEnum('PortOperatorEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg',
        {
            'equal':'equal',
            'not-equal':'not_equal',
            'greater-than':'greater_than',
            'less-than':'less_than',
        }, 'Cisco-IOS-XR-infra-objmgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg']),
    'StartPortEnum' : _MetaInfoEnum('StartPortEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg',
        {
            'echo':'echo',
            'discard':'discard',
            'daytime':'daytime',
            'chargen':'chargen',
            'ftp-data':'ftp_data',
            'ftp':'ftp',
            'ssh':'ssh',
            'telnet':'telnet',
            'smtp':'smtp',
            'time':'time',
            'nicname':'nicname',
            'tacacs':'tacacs',
            'domain':'domain',
            'gopher':'gopher',
            'finger':'finger',
            'www':'www',
            'host-name':'host_name',
            'pop2':'pop2',
            'pop3':'pop3',
            'sun-rpc':'sun_rpc',
            'ident':'ident',
            'nntp':'nntp',
            'bgp':'bgp',
            'irc':'irc',
            'pim-auto-rp':'pim_auto_rp',
            'exec':'exec_',
            'login':'login',
            'cmd':'cmd',
            'lpd':'lpd',
            'uucp':'uucp',
            'klogin':'klogin',
            'kshell':'kshell',
            'talk':'talk',
            'ldp':'ldp',
        }, 'Cisco-IOS-XR-infra-objmgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg']),
    'ObjectGroup.Port.UdfObjects.UdfObject.Operators.Operator' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.UdfObjects.UdfObject.Operators.Operator',
            False, 
            [
            _MetaInfoClassMember('operator-type', REFERENCE_ENUM_CLASS, 'PortOperatorEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'PortOperatorEnum', 
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
                    _MetaInfoClassMember('port', REFERENCE_ENUM_CLASS, 'PortEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'PortEnum', 
                        [], [], 
                        '''                        Port number
                        ''',
                        'port',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                        [('0', '65535')], [], 
                        '''                        Port number
                        ''',
                        'port',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'operator',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Port.UdfObjects.UdfObject.Operators' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.UdfObjects.UdfObject.Operators',
            False, 
            [
            _MetaInfoClassMember('operator', REFERENCE_LIST, 'Operator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Port.UdfObjects.UdfObject.Operators.Operator', 
                [], [], 
                '''                op class
                ''',
                'operator',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'operators',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Port.UdfObjects.UdfObject.NestedGroups.NestedGroup' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.UdfObjects.UdfObject.NestedGroups.NestedGroup',
            False, 
            [
            _MetaInfoClassMember('nested-group-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Name of a nested object group
                ''',
                'nested_group_name',
                'Cisco-IOS-XR-infra-objmgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'nested-group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Port.UdfObjects.UdfObject.NestedGroups' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.UdfObjects.UdfObject.NestedGroups',
            False, 
            [
            _MetaInfoClassMember('nested-group', REFERENCE_LIST, 'NestedGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Port.UdfObjects.UdfObject.NestedGroups.NestedGroup', 
                [], [], 
                '''                nested object group
                ''',
                'nested_group',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'nested-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Port.UdfObjects.UdfObject.PortRanges.PortRange' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.UdfObjects.UdfObject.PortRanges.PortRange',
            False, 
            [
            _MetaInfoClassMember('start-port', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Port number
                ''',
                'start_port',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('start-port', REFERENCE_ENUM_CLASS, 'StartPortEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'StartPortEnum', 
                        [], [], 
                        '''                        Port number
                        ''',
                        'start_port',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('start-port', ATTRIBUTE, 'int' , None, None, 
                        [('0', '65535')], [], 
                        '''                        Port number
                        ''',
                        'start_port',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            _MetaInfoClassMember('end-port', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Port number
                ''',
                'end_port',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('end-port', REFERENCE_ENUM_CLASS, 'EndPortEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'EndPortEnum', 
                        [], [], 
                        '''                        Port number
                        ''',
                        'end_port',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('end-port', ATTRIBUTE, 'int' , None, None, 
                        [('0', '65535')], [], 
                        '''                        Port number
                        ''',
                        'end_port',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'port-range',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Port.UdfObjects.UdfObject.PortRanges' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.UdfObjects.UdfObject.PortRanges',
            False, 
            [
            _MetaInfoClassMember('port-range', REFERENCE_LIST, 'PortRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Port.UdfObjects.UdfObject.PortRanges.PortRange', 
                [], [], 
                '''                Match only packets on a given port range
                ''',
                'port_range',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'port-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Port.UdfObjects.UdfObject' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.UdfObjects.UdfObject',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Port object group name - maximum 64
                characters
                ''',
                'object_name',
                'Cisco-IOS-XR-infra-objmgr-cfg', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(1, 100)], [], 
                '''                Up to 100 characters describing this object
                ''',
                'description',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('nested-groups', REFERENCE_CLASS, 'NestedGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Port.UdfObjects.UdfObject.NestedGroups', 
                [], [], 
                '''                Table of nested port object groups
                ''',
                'nested_groups',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('operators', REFERENCE_CLASS, 'Operators' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Port.UdfObjects.UdfObject.Operators', 
                [], [], 
                '''                Table of port operators
                ''',
                'operators',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('port-ranges', REFERENCE_CLASS, 'PortRanges' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Port.UdfObjects.UdfObject.PortRanges', 
                [], [], 
                '''                Table of port range addresses
                ''',
                'port_ranges',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'udf-object',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Port.UdfObjects' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.UdfObjects',
            False, 
            [
            _MetaInfoClassMember('udf-object', REFERENCE_LIST, 'UdfObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Port.UdfObjects.UdfObject', 
                [], [], 
                '''                Port object group
                ''',
                'udf_object',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'udf-objects',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Port' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port',
            False, 
            [
            _MetaInfoClassMember('udf-objects', REFERENCE_CLASS, 'UdfObjects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Port.UdfObjects', 
                [], [], 
                '''                Table of port objects groups
                ''',
                'udf_objects',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'port',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.NestedGroups.NestedGroup' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.NestedGroups.NestedGroup',
            False, 
            [
            _MetaInfoClassMember('nested-group-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Enter the name of a nested object group
                ''',
                'nested_group_name',
                'Cisco-IOS-XR-infra-objmgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'nested-group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.NestedGroups' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.NestedGroups',
            False, 
            [
            _MetaInfoClassMember('nested-group', REFERENCE_LIST, 'NestedGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.NestedGroups.NestedGroup', 
                [], [], 
                '''                nested object group
                ''',
                'nested_group',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'nested-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.AddressRanges.AddressRange' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.AddressRanges.AddressRange',
            False, 
            [
            _MetaInfoClassMember('start-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv6 address
                ''',
                'start_address',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address
                        ''',
                        'start_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address
                        ''',
                        'start_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            _MetaInfoClassMember('end-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv6 address
                ''',
                'end_address',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('end-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address
                        ''',
                        'end_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('end-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address
                        ''',
                        'end_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'address-range',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.AddressRanges' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.AddressRanges',
            False, 
            [
            _MetaInfoClassMember('address-range', REFERENCE_LIST, 'AddressRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.AddressRanges.AddressRange', 
                [], [], 
                '''                Range of host addresses
                ''',
                'address_range',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'address-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Addresses.Address' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Addresses.Address',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv6 prefix x:x::x/y
                ''',
                'prefix',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 prefix x:x::x/y
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 prefix x:x::x/y
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Prefix of the IP Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-infra-objmgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Addresses' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Addresses',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Addresses.Address', 
                [], [], 
                '''                IPv6 address
                ''',
                'address',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Hosts.Host' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Hosts.Host',
            False, 
            [
            _MetaInfoClassMember('host-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                host ipv6 address
                ''',
                'host_address',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('host-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        host ipv6 address
                        ''',
                        'host_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('host-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        host ipv6 address
                        ''',
                        'host_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'host',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Hosts' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Hosts',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Hosts.Host', 
                [], [], 
                '''                A single host address
                ''',
                'host',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.UdfObjects.UdfObject' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.UdfObjects.UdfObject',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                IPv6 object group name - maximum 64
                characters
                ''',
                'object_name',
                'Cisco-IOS-XR-infra-objmgr-cfg', True),
            _MetaInfoClassMember('address-ranges', REFERENCE_CLASS, 'AddressRanges' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.AddressRanges', 
                [], [], 
                '''                Table of ipv6 address ranges
                ''',
                'address_ranges',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Addresses', 
                [], [], 
                '''                Table of ipv6 addresses
                ''',
                'addresses',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(1, 100)], [], 
                '''                Up to 100 characters describing this object
                ''',
                'description',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Hosts', 
                [], [], 
                '''                Table of ipv6 host addresses
                ''',
                'hosts',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('nested-groups', REFERENCE_CLASS, 'NestedGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.NestedGroups', 
                [], [], 
                '''                Table of nested ipv6 object groups
                ''',
                'nested_groups',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'udf-object',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6.UdfObjects' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.UdfObjects',
            False, 
            [
            _MetaInfoClassMember('udf-object', REFERENCE_LIST, 'UdfObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.UdfObjects.UdfObject', 
                [], [], 
                '''                IPv6 object group
                ''',
                'udf_object',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'udf-objects',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv6' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6',
            False, 
            [
            _MetaInfoClassMember('udf-objects', REFERENCE_CLASS, 'UdfObjects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6.UdfObjects', 
                [], [], 
                '''                Table of ipv6 object groups
                ''',
                'udf_objects',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.NestedGroups.NestedGroup' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.NestedGroups.NestedGroup',
            False, 
            [
            _MetaInfoClassMember('nested-group-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Nested object group
                ''',
                'nested_group_name',
                'Cisco-IOS-XR-infra-objmgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'nested-group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.NestedGroups' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.NestedGroups',
            False, 
            [
            _MetaInfoClassMember('nested-group', REFERENCE_LIST, 'NestedGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.NestedGroups.NestedGroup', 
                [], [], 
                '''                Nested object group
                ''',
                'nested_group',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'nested-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.AddressRanges.AddressRange' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.AddressRanges.AddressRange',
            False, 
            [
            _MetaInfoClassMember('start-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4 address
                ''',
                'start_address',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address
                        ''',
                        'start_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address
                        ''',
                        'start_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            _MetaInfoClassMember('end-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4 address
                ''',
                'end_address',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('end-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address
                        ''',
                        'end_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('end-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address
                        ''',
                        'end_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'address-range',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.AddressRanges' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.AddressRanges',
            False, 
            [
            _MetaInfoClassMember('address-range', REFERENCE_LIST, 'AddressRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.AddressRanges.AddressRange', 
                [], [], 
                '''                Range of host addresses
                ''',
                'address_range',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'address-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Addresses.Address' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Addresses.Address',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4 address/prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address/prefix
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address/prefix
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Prefix of the IP Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-infra-objmgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Addresses' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Addresses',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Addresses.Address', 
                [], [], 
                '''                IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Hosts.Host' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Hosts.Host',
            False, 
            [
            _MetaInfoClassMember('host-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Host ipv4 address
                ''',
                'host_address',
                'Cisco-IOS-XR-infra-objmgr-cfg', True, [
                    _MetaInfoClassMember('host-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Host ipv4 address
                        ''',
                        'host_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                    _MetaInfoClassMember('host-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Host ipv4 address
                        ''',
                        'host_address',
                        'Cisco-IOS-XR-infra-objmgr-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'host',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Hosts' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Hosts',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Hosts.Host', 
                [], [], 
                '''                A single host address
                ''',
                'host',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.UdfObjects.UdfObject' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.UdfObjects.UdfObject',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                IPv4 object group name - maximum 64
                characters
                ''',
                'object_name',
                'Cisco-IOS-XR-infra-objmgr-cfg', True),
            _MetaInfoClassMember('address-ranges', REFERENCE_CLASS, 'AddressRanges' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.AddressRanges', 
                [], [], 
                '''                Table of ipv4 host address ranges
                ''',
                'address_ranges',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Addresses', 
                [], [], 
                '''                Table of addresses
                ''',
                'addresses',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(1, 100)], [], 
                '''                Up to 100 characters describing this object
                ''',
                'description',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Hosts', 
                [], [], 
                '''                Table of host addresses
                ''',
                'hosts',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('nested-groups', REFERENCE_CLASS, 'NestedGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.NestedGroups', 
                [], [], 
                '''                Table of nested ipv4 object groups
                ''',
                'nested_groups',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'udf-object',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4.UdfObjects' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.UdfObjects',
            False, 
            [
            _MetaInfoClassMember('udf-object', REFERENCE_LIST, 'UdfObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.UdfObjects.UdfObject', 
                [], [], 
                '''                IPv4 object group
                ''',
                'udf_object',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'udf-objects',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network.Ipv4' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4',
            False, 
            [
            _MetaInfoClassMember('udf-objects', REFERENCE_CLASS, 'UdfObjects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4.UdfObjects', 
                [], [], 
                '''                Table of ipv4 object groups
                ''',
                'udf_objects',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup.Network' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv4', 
                [], [], 
                '''                IPv4 object group
                ''',
                'ipv4',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network.Ipv6', 
                [], [], 
                '''                IPv6 object group
                ''',
                'ipv6',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'network',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
    'ObjectGroup' : {
        'meta_info' : _MetaInfoClass('ObjectGroup',
            False, 
            [
            _MetaInfoClassMember('network', REFERENCE_CLASS, 'Network' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Network', 
                [], [], 
                '''                Network object group
                ''',
                'network',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            _MetaInfoClassMember('port', REFERENCE_CLASS, 'Port' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg', 'ObjectGroup.Port', 
                [], [], 
                '''                Port object group
                ''',
                'port',
                'Cisco-IOS-XR-infra-objmgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-cfg',
            'object-group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_cfg'
        ),
    },
}
_meta_table['ObjectGroup.Port.UdfObjects.UdfObject.Operators.Operator']['meta_info'].parent =_meta_table['ObjectGroup.Port.UdfObjects.UdfObject.Operators']['meta_info']
_meta_table['ObjectGroup.Port.UdfObjects.UdfObject.NestedGroups.NestedGroup']['meta_info'].parent =_meta_table['ObjectGroup.Port.UdfObjects.UdfObject.NestedGroups']['meta_info']
_meta_table['ObjectGroup.Port.UdfObjects.UdfObject.PortRanges.PortRange']['meta_info'].parent =_meta_table['ObjectGroup.Port.UdfObjects.UdfObject.PortRanges']['meta_info']
_meta_table['ObjectGroup.Port.UdfObjects.UdfObject.Operators']['meta_info'].parent =_meta_table['ObjectGroup.Port.UdfObjects.UdfObject']['meta_info']
_meta_table['ObjectGroup.Port.UdfObjects.UdfObject.NestedGroups']['meta_info'].parent =_meta_table['ObjectGroup.Port.UdfObjects.UdfObject']['meta_info']
_meta_table['ObjectGroup.Port.UdfObjects.UdfObject.PortRanges']['meta_info'].parent =_meta_table['ObjectGroup.Port.UdfObjects.UdfObject']['meta_info']
_meta_table['ObjectGroup.Port.UdfObjects.UdfObject']['meta_info'].parent =_meta_table['ObjectGroup.Port.UdfObjects']['meta_info']
_meta_table['ObjectGroup.Port.UdfObjects']['meta_info'].parent =_meta_table['ObjectGroup.Port']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.NestedGroups.NestedGroup']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.NestedGroups']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.AddressRanges.AddressRange']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.AddressRanges']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Addresses.Address']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Addresses']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Hosts.Host']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Hosts']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.NestedGroups']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.UdfObjects.UdfObject']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.AddressRanges']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.UdfObjects.UdfObject']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Addresses']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.UdfObjects.UdfObject']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.UdfObjects.UdfObject.Hosts']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.UdfObjects.UdfObject']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.UdfObjects.UdfObject']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.UdfObjects']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.UdfObjects']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.NestedGroups.NestedGroup']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.NestedGroups']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.AddressRanges.AddressRange']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.AddressRanges']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Addresses.Address']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Addresses']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Hosts.Host']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Hosts']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.NestedGroups']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.UdfObjects.UdfObject']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.AddressRanges']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.UdfObjects.UdfObject']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Addresses']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.UdfObjects.UdfObject']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.UdfObjects.UdfObject.Hosts']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.UdfObjects.UdfObject']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.UdfObjects.UdfObject']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.UdfObjects']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.UdfObjects']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6']['meta_info'].parent =_meta_table['ObjectGroup.Network']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4']['meta_info'].parent =_meta_table['ObjectGroup.Network']['meta_info']
_meta_table['ObjectGroup.Port']['meta_info'].parent =_meta_table['ObjectGroup']['meta_info']
_meta_table['ObjectGroup.Network']['meta_info'].parent =_meta_table['ObjectGroup']['meta_info']
