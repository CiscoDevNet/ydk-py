


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EndPortEnum' : _MetaInfoEnum('EndPortEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper',
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
        }, 'Cisco-IOS-XR-infra-objmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper']),
    'PortEnum' : _MetaInfoEnum('PortEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper',
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
        }, 'Cisco-IOS-XR-infra-objmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper']),
    'PortOperatorEnum' : _MetaInfoEnum('PortOperatorEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper',
        {
            'equal':'equal',
            'not-equal':'not_equal',
            'greater-than':'greater_than',
            'less-than':'less_than',
        }, 'Cisco-IOS-XR-infra-objmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper']),
    'StartPortEnum' : _MetaInfoEnum('StartPortEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper',
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
        }, 'Cisco-IOS-XR-infra-objmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper']),
    'ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup',
            False, 
            [
            _MetaInfoClassMember('nested-group-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Nested object group
                ''',
                'nested_group_name',
                'Cisco-IOS-XR-infra-objmgr-oper', True),
            _MetaInfoClassMember('nested-group-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Nested group
                ''',
                'nested_group_name_xr',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'nested-group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Port.Objects.Object.NestedGroups' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.Objects.Object.NestedGroups',
            False, 
            [
            _MetaInfoClassMember('nested-group', REFERENCE_LIST, 'NestedGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup', 
                [], [], 
                '''                nested object group
                ''',
                'nested_group',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'nested-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Port.Objects.Object.Operators.Operator' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.Objects.Object.Operators.Operator',
            False, 
            [
            _MetaInfoClassMember('operator-type', REFERENCE_ENUM_CLASS, 'PortOperatorEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'PortOperatorEnum', 
                [], [], 
                '''                operation for ports
                ''',
                'operator_type',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('operator-type-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Operator
                ''',
                'operator_type_xr',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('port', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Port number
                ''',
                'port',
                'Cisco-IOS-XR-infra-objmgr-oper', False, [
                    _MetaInfoClassMember('port', REFERENCE_ENUM_CLASS, 'PortEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'PortEnum', 
                        [], [], 
                        '''                        Port number
                        ''',
                        'port',
                        'Cisco-IOS-XR-infra-objmgr-oper', False),
                    _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                        [('0', '65535')], [], 
                        '''                        Port number
                        ''',
                        'port',
                        'Cisco-IOS-XR-infra-objmgr-oper', False),
                ]),
            _MetaInfoClassMember('port-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Port
                ''',
                'port_xr',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'operator',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Port.Objects.Object.Operators' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.Objects.Object.Operators',
            False, 
            [
            _MetaInfoClassMember('operator', REFERENCE_LIST, 'Operator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Port.Objects.Object.Operators.Operator', 
                [], [], 
                '''                op class
                ''',
                'operator',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'operators',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Port.Objects.Object.PortRanges.PortRange' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.Objects.Object.PortRanges.PortRange',
            False, 
            [
            _MetaInfoClassMember('end-port', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                End port number
                ''',
                'end_port',
                'Cisco-IOS-XR-infra-objmgr-oper', False, [
                    _MetaInfoClassMember('end-port', REFERENCE_ENUM_CLASS, 'EndPortEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'EndPortEnum', 
                        [], [], 
                        '''                        End port number
                        ''',
                        'end_port',
                        'Cisco-IOS-XR-infra-objmgr-oper', False),
                    _MetaInfoClassMember('end-port', ATTRIBUTE, 'int' , None, None, 
                        [('0', '65535')], [], 
                        '''                        End port number
                        ''',
                        'end_port',
                        'Cisco-IOS-XR-infra-objmgr-oper', False),
                ]),
            _MetaInfoClassMember('end-port-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Port end address
                ''',
                'end_port_xr',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('start-port', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Start port number
                ''',
                'start_port',
                'Cisco-IOS-XR-infra-objmgr-oper', False, [
                    _MetaInfoClassMember('start-port', REFERENCE_ENUM_CLASS, 'StartPortEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'StartPortEnum', 
                        [], [], 
                        '''                        Start port number
                        ''',
                        'start_port',
                        'Cisco-IOS-XR-infra-objmgr-oper', False),
                    _MetaInfoClassMember('start-port', ATTRIBUTE, 'int' , None, None, 
                        [('0', '65535')], [], 
                        '''                        Start port number
                        ''',
                        'start_port',
                        'Cisco-IOS-XR-infra-objmgr-oper', False),
                ]),
            _MetaInfoClassMember('start-port-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Port start address
                ''',
                'start_port_xr',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'port-range',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Port.Objects.Object.PortRanges' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.Objects.Object.PortRanges',
            False, 
            [
            _MetaInfoClassMember('port-range', REFERENCE_LIST, 'PortRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Port.Objects.Object.PortRanges.PortRange', 
                [], [], 
                '''                Match only packets on a given port range
                ''',
                'port_range',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'port-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Port.Objects.Object.ParentGroups.ParentGroup' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.Objects.Object.ParentGroups.ParentGroup',
            False, 
            [
            _MetaInfoClassMember('parent-group-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Nested object group
                ''',
                'parent_group_name',
                'Cisco-IOS-XR-infra-objmgr-oper', True),
            _MetaInfoClassMember('parent-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Parent node
                ''',
                'parent_name',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'parent-group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Port.Objects.Object.ParentGroups' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.Objects.Object.ParentGroups',
            False, 
            [
            _MetaInfoClassMember('parent-group', REFERENCE_LIST, 'ParentGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Port.Objects.Object.ParentGroups.ParentGroup', 
                [], [], 
                '''                Parent object group
                ''',
                'parent_group',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'parent-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Port.Objects.Object' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.Objects.Object',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Port object group name
                ''',
                'object_name',
                'Cisco-IOS-XR-infra-objmgr-oper', True),
            _MetaInfoClassMember('nested-groups', REFERENCE_CLASS, 'NestedGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Port.Objects.Object.NestedGroups', 
                [], [], 
                '''                Table of NestedGroup
                ''',
                'nested_groups',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('operators', REFERENCE_CLASS, 'Operators' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Port.Objects.Object.Operators', 
                [], [], 
                '''                Table of Operator
                ''',
                'operators',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('parent-groups', REFERENCE_CLASS, 'ParentGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Port.Objects.Object.ParentGroups', 
                [], [], 
                '''                Table of ParentGroup
                ''',
                'parent_groups',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('port-ranges', REFERENCE_CLASS, 'PortRanges' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Port.Objects.Object.PortRanges', 
                [], [], 
                '''                Table of PortRange
                ''',
                'port_ranges',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'object',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Port.Objects' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port.Objects',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LIST, 'Object' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Port.Objects.Object', 
                [], [], 
                '''                Port object group
                ''',
                'object',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'objects',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Port' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Port',
            False, 
            [
            _MetaInfoClassMember('objects', REFERENCE_CLASS, 'Objects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Port.Objects', 
                [], [], 
                '''                Table of Object
                ''',
                'objects',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'port',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup',
            False, 
            [
            _MetaInfoClassMember('nested-group-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Enter the name of a nested object group
                ''',
                'nested_group_name',
                'Cisco-IOS-XR-infra-objmgr-oper', True),
            _MetaInfoClassMember('nested-group-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Nested group
                ''',
                'nested_group_name_xr',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'nested-group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups',
            False, 
            [
            _MetaInfoClassMember('nested-group', REFERENCE_LIST, 'NestedGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup', 
                [], [], 
                '''                nested object group
                ''',
                'nested_group',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'nested-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 prefix x:x::x/y
                ''',
                'prefix',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Prefix of the IP Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('prefix-length-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length
                ''',
                'prefix_length_xr',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('prefix-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'prefix_xr',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object.Addresses' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object.Addresses',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address', 
                [], [], 
                '''                IPv6 address
                ''',
                'address',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange',
            False, 
            [
            _MetaInfoClassMember('end-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'end_address',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('end-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Range end address
                ''',
                'end_address_xr',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'start_address',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('start-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Range start address
                ''',
                'start_address_xr',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'address-range',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges',
            False, 
            [
            _MetaInfoClassMember('address-range', REFERENCE_LIST, 'AddressRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange', 
                [], [], 
                '''                Range of host addresses
                ''',
                'address_range',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'address-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups.ParentGroup' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups.ParentGroup',
            False, 
            [
            _MetaInfoClassMember('parent-group-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Nested object group
                ''',
                'parent_group_name',
                'Cisco-IOS-XR-infra-objmgr-oper', True),
            _MetaInfoClassMember('parent-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Parent node
                ''',
                'parent_name',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'parent-group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups',
            False, 
            [
            _MetaInfoClassMember('parent-group', REFERENCE_LIST, 'ParentGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups.ParentGroup', 
                [], [], 
                '''                Parent object group
                ''',
                'parent_group',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'parent-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host',
            False, 
            [
            _MetaInfoClassMember('host-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                host ipv6 address
                ''',
                'host_address',
                'Cisco-IOS-XR-infra-objmgr-oper', True),
            _MetaInfoClassMember('host-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Host address
                ''',
                'host_address_xr',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'host',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object.Hosts' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object.Hosts',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host', 
                [], [], 
                '''                A single host address
                ''',
                'host',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects.Object' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects.Object',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                IPv6 object group name - maximum 64
                characters
                ''',
                'object_name',
                'Cisco-IOS-XR-infra-objmgr-oper', True),
            _MetaInfoClassMember('address-ranges', REFERENCE_CLASS, 'AddressRanges' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges', 
                [], [], 
                '''                Table of AddressRange
                ''',
                'address_ranges',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv6.Objects.Object.Addresses', 
                [], [], 
                '''                Table of Address
                ''',
                'addresses',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv6.Objects.Object.Hosts', 
                [], [], 
                '''                Table of Host
                ''',
                'hosts',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('nested-groups', REFERENCE_CLASS, 'NestedGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups', 
                [], [], 
                '''                Table of NestedGroup
                ''',
                'nested_groups',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('parent-groups', REFERENCE_CLASS, 'ParentGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups', 
                [], [], 
                '''                Table of parent object group
                ''',
                'parent_groups',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'object',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv6.Objects' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6.Objects',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LIST, 'Object' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv6.Objects.Object', 
                [], [], 
                '''                IPv6 object group
                ''',
                'object',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'objects',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv6' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv6',
            False, 
            [
            _MetaInfoClassMember('objects', REFERENCE_CLASS, 'Objects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv6.Objects', 
                [], [], 
                '''                Table of Object
                ''',
                'objects',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup',
            False, 
            [
            _MetaInfoClassMember('nested-group-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Nested object group
                ''',
                'nested_group_name',
                'Cisco-IOS-XR-infra-objmgr-oper', True),
            _MetaInfoClassMember('nested-group-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Nested group
                ''',
                'nested_group_name_xr',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'nested-group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups',
            False, 
            [
            _MetaInfoClassMember('nested-group', REFERENCE_LIST, 'NestedGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup', 
                [], [], 
                '''                Nested object group
                ''',
                'nested_group',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'nested-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address/prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Prefix of the IP Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('prefix-length-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length
                ''',
                'prefix_length_xr',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('prefix-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'prefix_xr',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object.Addresses' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object.Addresses',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address', 
                [], [], 
                '''                IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange',
            False, 
            [
            _MetaInfoClassMember('end-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'end_address',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('end-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Range end address
                ''',
                'end_address_xr',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'start_address',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('start-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Range start address
                ''',
                'start_address_xr',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'address-range',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges',
            False, 
            [
            _MetaInfoClassMember('address-range', REFERENCE_LIST, 'AddressRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange', 
                [], [], 
                '''                Range of host addresses
                ''',
                'address_range',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'address-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups.ParentGroup' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups.ParentGroup',
            False, 
            [
            _MetaInfoClassMember('parent-group-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Nested object group
                ''',
                'parent_group_name',
                'Cisco-IOS-XR-infra-objmgr-oper', True),
            _MetaInfoClassMember('parent-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Parent node
                ''',
                'parent_name',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'parent-group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups',
            False, 
            [
            _MetaInfoClassMember('parent-group', REFERENCE_LIST, 'ParentGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups.ParentGroup', 
                [], [], 
                '''                Parent object group
                ''',
                'parent_group',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'parent-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host',
            False, 
            [
            _MetaInfoClassMember('host-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Host ipv4 address
                ''',
                'host_address',
                'Cisco-IOS-XR-infra-objmgr-oper', True),
            _MetaInfoClassMember('host-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Host address
                ''',
                'host_address_xr',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'host',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object.Hosts' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object.Hosts',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host', 
                [], [], 
                '''                A single host address
                ''',
                'host',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects.Object' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects.Object',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                IPv4 object group name - maximum 64
                characters
                ''',
                'object_name',
                'Cisco-IOS-XR-infra-objmgr-oper', True),
            _MetaInfoClassMember('address-ranges', REFERENCE_CLASS, 'AddressRanges' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges', 
                [], [], 
                '''                Table of AddressRange
                ''',
                'address_ranges',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv4.Objects.Object.Addresses', 
                [], [], 
                '''                Table of Address
                ''',
                'addresses',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv4.Objects.Object.Hosts', 
                [], [], 
                '''                Table of Host
                ''',
                'hosts',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('nested-groups', REFERENCE_CLASS, 'NestedGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups', 
                [], [], 
                '''                Table of NestedGroup
                ''',
                'nested_groups',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('parent-groups', REFERENCE_CLASS, 'ParentGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups', 
                [], [], 
                '''                Table of parent object group
                ''',
                'parent_groups',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'object',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv4.Objects' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4.Objects',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LIST, 'Object' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv4.Objects.Object', 
                [], [], 
                '''                IPv4 object group
                ''',
                'object',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'objects',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network.Ipv4' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network.Ipv4',
            False, 
            [
            _MetaInfoClassMember('objects', REFERENCE_CLASS, 'Objects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv4.Objects', 
                [], [], 
                '''                Table of Object
                ''',
                'objects',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup.Network' : {
        'meta_info' : _MetaInfoClass('ObjectGroup.Network',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv4', 
                [], [], 
                '''                IPv4 object group
                ''',
                'ipv4',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network.Ipv6', 
                [], [], 
                '''                IPv6 object group
                ''',
                'ipv6',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'network',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
    'ObjectGroup' : {
        'meta_info' : _MetaInfoClass('ObjectGroup',
            False, 
            [
            _MetaInfoClassMember('network', REFERENCE_CLASS, 'Network' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Network', 
                [], [], 
                '''                Network object group
                ''',
                'network',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            _MetaInfoClassMember('port', REFERENCE_CLASS, 'Port' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper', 'ObjectGroup.Port', 
                [], [], 
                '''                Port object group
                ''',
                'port',
                'Cisco-IOS-XR-infra-objmgr-oper', False),
            ],
            'Cisco-IOS-XR-infra-objmgr-oper',
            'object-group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-objmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_objmgr_oper'
        ),
    },
}
_meta_table['ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup']['meta_info'].parent =_meta_table['ObjectGroup.Port.Objects.Object.NestedGroups']['meta_info']
_meta_table['ObjectGroup.Port.Objects.Object.Operators.Operator']['meta_info'].parent =_meta_table['ObjectGroup.Port.Objects.Object.Operators']['meta_info']
_meta_table['ObjectGroup.Port.Objects.Object.PortRanges.PortRange']['meta_info'].parent =_meta_table['ObjectGroup.Port.Objects.Object.PortRanges']['meta_info']
_meta_table['ObjectGroup.Port.Objects.Object.ParentGroups.ParentGroup']['meta_info'].parent =_meta_table['ObjectGroup.Port.Objects.Object.ParentGroups']['meta_info']
_meta_table['ObjectGroup.Port.Objects.Object.NestedGroups']['meta_info'].parent =_meta_table['ObjectGroup.Port.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Port.Objects.Object.Operators']['meta_info'].parent =_meta_table['ObjectGroup.Port.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Port.Objects.Object.PortRanges']['meta_info'].parent =_meta_table['ObjectGroup.Port.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Port.Objects.Object.ParentGroups']['meta_info'].parent =_meta_table['ObjectGroup.Port.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Port.Objects.Object']['meta_info'].parent =_meta_table['ObjectGroup.Port.Objects']['meta_info']
_meta_table['ObjectGroup.Port.Objects']['meta_info'].parent =_meta_table['ObjectGroup.Port']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Addresses']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups.ParentGroup']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Hosts']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Addresses']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.ParentGroups']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Hosts']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects.Object']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6.Objects']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6.Objects']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv6']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Addresses']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups.ParentGroup']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Hosts']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Addresses']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.ParentGroups']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Hosts']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects.Object']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects.Object']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4.Objects']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4.Objects']['meta_info'].parent =_meta_table['ObjectGroup.Network.Ipv4']['meta_info']
_meta_table['ObjectGroup.Network.Ipv6']['meta_info'].parent =_meta_table['ObjectGroup.Network']['meta_info']
_meta_table['ObjectGroup.Network.Ipv4']['meta_info'].parent =_meta_table['ObjectGroup.Network']['meta_info']
_meta_table['ObjectGroup.Port']['meta_info'].parent =_meta_table['ObjectGroup']['meta_info']
_meta_table['ObjectGroup.Network']['meta_info'].parent =_meta_table['ObjectGroup']['meta_info']
