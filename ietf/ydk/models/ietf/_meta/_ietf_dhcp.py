


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'AllocateTypeEnum' : _MetaInfoEnum('AllocateTypeEnum', 'ydk.models.ietf.ietf_dhcp',
        {
            'automatic':'automatic',
            'dynamic':'dynamic',
            'manual':'manual',
        }, 'ietf-dhcp', _yang_ns._namespaces['ietf-dhcp']),
    'Dhcp.Server.Option' : {
        'meta_info' : _MetaInfoClass('Dhcp.Server.Option',
            False, 
            [
            _MetaInfoClassMember('dhcp-server-identifier', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                DHCP server identifier
                ''',
                'dhcp_server_identifier',
                'ietf-dhcp', False, [
                    _MetaInfoClassMember('dhcp-server-identifier', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        DHCP server identifier
                        ''',
                        'dhcp_server_identifier',
                        'ietf-dhcp', False),
                    _MetaInfoClassMember('dhcp-server-identifier', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        DHCP server identifier
                        ''',
                        'dhcp_server_identifier',
                        'ietf-dhcp', False),
                ]),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the domain
                ''',
                'domain_name',
                'ietf-dhcp', False),
            _MetaInfoClassMember('domain-name-server', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4 address of the domain
                ''',
                'domain_name_server',
                'ietf-dhcp', False, [
                    _MetaInfoClassMember('domain-name-server', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address of the domain
                        ''',
                        'domain_name_server',
                        'ietf-dhcp', False),
                    _MetaInfoClassMember('domain-name-server', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address of the domain
                        ''',
                        'domain_name_server',
                        'ietf-dhcp', False),
                ]),
            _MetaInfoClassMember('interface-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Minimum Transmission Unit (MTU) of the interface
                ''',
                'interface_mtu',
                'ietf-dhcp', False),
            _MetaInfoClassMember('netbios-name-server', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                NETBIOS name server
                ''',
                'netbios_name_server',
                'ietf-dhcp', False, [
                    _MetaInfoClassMember('netbios-name-server', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        NETBIOS name server
                        ''',
                        'netbios_name_server',
                        'ietf-dhcp', False),
                    _MetaInfoClassMember('netbios-name-server', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        NETBIOS name server
                        ''',
                        'netbios_name_server',
                        'ietf-dhcp', False),
                ]),
            _MetaInfoClassMember('netbios-node-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                NETBIOS node type
                ''',
                'netbios_node_type',
                'ietf-dhcp', False),
            _MetaInfoClassMember('netbios-scope', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                NETBIOS scope
                ''',
                'netbios_scope',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'option',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'Dhcp.Server.DhcpIpPool.ManualAllocation' : {
        'meta_info' : _MetaInfoClass('Dhcp.Server.DhcpIpPool.ManualAllocation',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4 address of the host
                ''',
                'ip_address',
                'ietf-dhcp', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address of the host
                        ''',
                        'ip_address',
                        'ietf-dhcp', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address of the host
                        ''',
                        'ip_address',
                        'ietf-dhcp', True),
                ]),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address of the host
                ''',
                'mac_address',
                'ietf-dhcp', True),
            ],
            'ietf-dhcp',
            'manual-allocation',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'Dhcp.Server.DhcpIpPool.Section' : {
        'meta_info' : _MetaInfoClass('Dhcp.Server.DhcpIpPool.Section',
            False, 
            [
            _MetaInfoClassMember('section-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Index of IPv4 address range
                ''',
                'section_index',
                'ietf-dhcp', True),
            _MetaInfoClassMember('section-end-ip', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Last IPv4 Address of a section
                ''',
                'section_end_ip',
                'ietf-dhcp', False),
            _MetaInfoClassMember('section-start-ip', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Starting IPv4 Address of a section
                ''',
                'section_start_ip',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'section',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'Dhcp.Server.DhcpIpPool.Option' : {
        'meta_info' : _MetaInfoClass('Dhcp.Server.DhcpIpPool.Option',
            False, 
            [
            _MetaInfoClassMember('dhcp-server-identifier', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                DHCP server identifier
                ''',
                'dhcp_server_identifier',
                'ietf-dhcp', False, [
                    _MetaInfoClassMember('dhcp-server-identifier', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        DHCP server identifier
                        ''',
                        'dhcp_server_identifier',
                        'ietf-dhcp', False),
                    _MetaInfoClassMember('dhcp-server-identifier', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        DHCP server identifier
                        ''',
                        'dhcp_server_identifier',
                        'ietf-dhcp', False),
                ]),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the domain
                ''',
                'domain_name',
                'ietf-dhcp', False),
            _MetaInfoClassMember('domain-name-server', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4 address of the domain
                ''',
                'domain_name_server',
                'ietf-dhcp', False, [
                    _MetaInfoClassMember('domain-name-server', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address of the domain
                        ''',
                        'domain_name_server',
                        'ietf-dhcp', False),
                    _MetaInfoClassMember('domain-name-server', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address of the domain
                        ''',
                        'domain_name_server',
                        'ietf-dhcp', False),
                ]),
            _MetaInfoClassMember('interface-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Minimum Transmission Unit (MTU) of the interface
                ''',
                'interface_mtu',
                'ietf-dhcp', False),
            _MetaInfoClassMember('netbios-name-server', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                NETBIOS name server
                ''',
                'netbios_name_server',
                'ietf-dhcp', False, [
                    _MetaInfoClassMember('netbios-name-server', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        NETBIOS name server
                        ''',
                        'netbios_name_server',
                        'ietf-dhcp', False),
                    _MetaInfoClassMember('netbios-name-server', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        NETBIOS name server
                        ''',
                        'netbios_name_server',
                        'ietf-dhcp', False),
                ]),
            _MetaInfoClassMember('netbios-node-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                NETBIOS node type
                ''',
                'netbios_node_type',
                'ietf-dhcp', False),
            _MetaInfoClassMember('netbios-scope', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                NETBIOS scope
                ''',
                'netbios_scope',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'option',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'Dhcp.Server.DhcpIpPool' : {
        'meta_info' : _MetaInfoClass('Dhcp.Server.DhcpIpPool',
            False, 
            [
            _MetaInfoClassMember('ip-pool-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Name of the IP pool
                ''',
                'ip_pool_name',
                'ietf-dhcp', True),
            _MetaInfoClassMember('gateway-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4 address of the gateway
                ''',
                'gateway_ip',
                'ietf-dhcp', False, [
                    _MetaInfoClassMember('gateway-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address of the gateway
                        ''',
                        'gateway_ip',
                        'ietf-dhcp', False),
                    _MetaInfoClassMember('gateway-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address of the gateway
                        ''',
                        'gateway_ip',
                        'ietf-dhcp', False),
                ]),
            _MetaInfoClassMember('gateway-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Network submask of the gateway
                ''',
                'gateway_mask',
                'ietf-dhcp', False, [
                    _MetaInfoClassMember('gateway-mask', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Network submask of the gateway
                        ''',
                        'gateway_mask',
                        'ietf-dhcp', False),
                    _MetaInfoClassMember('gateway-mask', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Network submask of the gateway
                        ''',
                        'gateway_mask',
                        'ietf-dhcp', False),
                ]),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the interface
                ''',
                'interface',
                'ietf-dhcp', False),
            _MetaInfoClassMember('lease-time', ATTRIBUTE, 'int' , None, None, 
                [('180', '31536000')], [], 
                '''                Default network address lease time assigned to DHCP clients
                ''',
                'lease_time',
                'ietf-dhcp', False),
            _MetaInfoClassMember('manual-allocation', REFERENCE_LIST, 'ManualAllocation' , 'ydk.models.ietf.ietf_dhcp', 'Dhcp.Server.DhcpIpPool.ManualAllocation', 
                [], [], 
                '''                Mapping from MAC address to IP address
                ''',
                'manual_allocation',
                'ietf-dhcp', False),
            _MetaInfoClassMember('option', REFERENCE_CLASS, 'Option' , 'ydk.models.ietf.ietf_dhcp', 'Dhcp.Server.DhcpIpPool.Option', 
                [], [], 
                '''                Configuration option
                ''',
                'option',
                'ietf-dhcp', False),
            _MetaInfoClassMember('section', REFERENCE_LIST, 'Section' , 'ydk.models.ietf.ietf_dhcp', 'Dhcp.Server.DhcpIpPool.Section', 
                [], [], 
                '''                IPv4 address for the range
                ''',
                'section',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'dhcp-ip-pool',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'Dhcp.Server' : {
        'meta_info' : _MetaInfoClass('Dhcp.Server',
            False, 
            [
            _MetaInfoClassMember('dhcp-ip-pool', REFERENCE_LIST, 'DhcpIpPool' , 'ydk.models.ietf.ietf_dhcp', 'Dhcp.Server.DhcpIpPool', 
                [], [], 
                '''                Global IP pool configuration
                ''',
                'dhcp_ip_pool',
                'ietf-dhcp', False),
            _MetaInfoClassMember('lease-time', ATTRIBUTE, 'int' , None, None, 
                [('180', '31536000')], [], 
                '''                Default network address lease time assigned to DHCP clients
                ''',
                'lease_time',
                'ietf-dhcp', False),
            _MetaInfoClassMember('option', REFERENCE_CLASS, 'Option' , 'ydk.models.ietf.ietf_dhcp', 'Dhcp.Server.Option', 
                [], [], 
                '''                Configuration option
                ''',
                'option',
                'ietf-dhcp', False),
            _MetaInfoClassMember('ping-packet-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '10')], [], 
                '''                Number of ping packets
                ''',
                'ping_packet_number',
                'ietf-dhcp', False),
            _MetaInfoClassMember('ping-packet-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '10000')], [], 
                '''                Timeout of ping packet
                ''',
                'ping_packet_timeout',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'server',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'Dhcp.Relay.ServerGroup' : {
        'meta_info' : _MetaInfoClass('Dhcp.Relay.ServerGroup',
            False, 
            [
            _MetaInfoClassMember('server-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of a DHCP server group
                ''',
                'server_group_name',
                'ietf-dhcp', True),
            _MetaInfoClassMember('gateway-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address of the gateway
                ''',
                'gateway_address',
                'ietf-dhcp', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the interface
                ''',
                'interface',
                'ietf-dhcp', False),
            _MetaInfoClassMember('server-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address of the server
                ''',
                'server_address',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'server-group',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'Dhcp.Relay' : {
        'meta_info' : _MetaInfoClass('Dhcp.Relay',
            False, 
            [
            _MetaInfoClassMember('server-group', REFERENCE_LIST, 'ServerGroup' , 'ydk.models.ietf.ietf_dhcp', 'Dhcp.Relay.ServerGroup', 
                [], [], 
                '''                DHCP server group configuration that DHCP relays to
                ''',
                'server_group',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'relay',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'Dhcp.Client.Interfaces' : {
        'meta_info' : _MetaInfoClass('Dhcp.Client.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the interface
                ''',
                'interface',
                'ietf-dhcp', True),
            _MetaInfoClassMember('client-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                DHCP client identifier
                ''',
                'client_id',
                'ietf-dhcp', False),
            _MetaInfoClassMember('lease', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Default network address lease time assigned to DHCP clients
                ''',
                'lease',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'interfaces',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'Dhcp.Client' : {
        'meta_info' : _MetaInfoClass('Dhcp.Client',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_LIST, 'Interfaces' , 'ydk.models.ietf.ietf_dhcp', 'Dhcp.Client.Interfaces', 
                [], [], 
                '''                Interface configuration
                ''',
                'interfaces',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'client',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'Dhcp' : {
        'meta_info' : _MetaInfoClass('Dhcp',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_CLASS, 'Client' , 'ydk.models.ietf.ietf_dhcp', 'Dhcp.Client', 
                [], [], 
                '''                DHCP client configuration
                ''',
                'client',
                'ietf-dhcp', False),
            _MetaInfoClassMember('relay', REFERENCE_CLASS, 'Relay' , 'ydk.models.ietf.ietf_dhcp', 'Dhcp.Relay', 
                [], [], 
                '''                DHCP relay agent configuration
                ''',
                'relay',
                'ietf-dhcp', False),
            _MetaInfoClassMember('server', REFERENCE_CLASS, 'Server' , 'ydk.models.ietf.ietf_dhcp', 'Dhcp.Server', 
                [], [], 
                '''                DHCP server configuration
                ''',
                'server',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'dhcp',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'DhcpState.Server.PacketStatistics.Receive' : {
        'meta_info' : _MetaInfoClass('DhcpState.Server.PacketStatistics.Receive',
            False, 
            [
            _MetaInfoClassMember('decline-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPDECLINE packets
                ''',
                'decline_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('discover-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPDISCOVER packets
                ''',
                'discover_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('inform-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPINFORM packets
                ''',
                'inform_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('release-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPRELEASE packets
                ''',
                'release_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('request-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPREQUEST packets
                ''',
                'request_packet',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'receive',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'DhcpState.Server.PacketStatistics.Send' : {
        'meta_info' : _MetaInfoClass('DhcpState.Server.PacketStatistics.Send',
            False, 
            [
            _MetaInfoClassMember('ack-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPACK packets
                ''',
                'ack_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('nack-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPNAK packets
                ''',
                'nack_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('offer-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPOFFER packets
                ''',
                'offer_packet',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'send',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'DhcpState.Server.PacketStatistics' : {
        'meta_info' : _MetaInfoClass('DhcpState.Server.PacketStatistics',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the interface
                ''',
                'interface',
                'ietf-dhcp', False),
            _MetaInfoClassMember('receive', REFERENCE_CLASS, 'Receive' , 'ydk.models.ietf.ietf_dhcp', 'DhcpState.Server.PacketStatistics.Receive', 
                [], [], 
                '''                Number of  received packets
                ''',
                'receive',
                'ietf-dhcp', False),
            _MetaInfoClassMember('send', REFERENCE_CLASS, 'Send' , 'ydk.models.ietf.ietf_dhcp', 'DhcpState.Server.PacketStatistics.Send', 
                [], [], 
                '''                Number of sent packets
                ''',
                'send',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'packet-statistics',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'DhcpState.Server.Host' : {
        'meta_info' : _MetaInfoClass('DhcpState.Server.Host',
            False, 
            [
            _MetaInfoClassMember('host-hardware-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                MAC address of the host
                ''',
                'host_hardware_address',
                'ietf-dhcp', False),
            _MetaInfoClassMember('host-ip', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPv4 address of the host
                ''',
                'host_ip',
                'ietf-dhcp', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the interface
                ''',
                'interface',
                'ietf-dhcp', False),
            _MetaInfoClassMember('lease', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default network address lease
                time assigned to DHCP clients
                ''',
                'lease',
                'ietf-dhcp', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'AllocateTypeEnum' , 'ydk.models.ietf.ietf_dhcp', 'AllocateTypeEnum', 
                [], [], 
                '''                Mechanisms for IP address allocation
                ''',
                'type',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'host',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'DhcpState.Server.IpPool' : {
        'meta_info' : _MetaInfoClass('DhcpState.Server.IpPool',
            False, 
            [
            _MetaInfoClassMember('ip-pool-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Name of an IP pool
                ''',
                'ip_pool_name',
                'ietf-dhcp', True),
            _MetaInfoClassMember('conflict-ip-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of conflict IPv4 addresses
                ''',
                'conflict_ip_count',
                'ietf-dhcp', False),
            _MetaInfoClassMember('gateway-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4 address of the gateway
                ''',
                'gateway_ip',
                'ietf-dhcp', False, [
                    _MetaInfoClassMember('gateway-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address of the gateway
                        ''',
                        'gateway_ip',
                        'ietf-dhcp', False),
                    _MetaInfoClassMember('gateway-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address of the gateway
                        ''',
                        'gateway_ip',
                        'ietf-dhcp', False),
                ]),
            _MetaInfoClassMember('gateway-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Network submask of the gateway
                ''',
                'gateway_mask',
                'ietf-dhcp', False, [
                    _MetaInfoClassMember('gateway-mask', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Network submask of the gateway
                        ''',
                        'gateway_mask',
                        'ietf-dhcp', False),
                    _MetaInfoClassMember('gateway-mask', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Network submask of the gateway
                        ''',
                        'gateway_mask',
                        'ietf-dhcp', False),
                ]),
            _MetaInfoClassMember('idle-ip-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of idle IPv4 addresses
                ''',
                'idle_ip_count',
                'ietf-dhcp', False),
            _MetaInfoClassMember('total-ip-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of IPv4 addresses
                ''',
                'total_ip_count',
                'ietf-dhcp', False),
            _MetaInfoClassMember('used-ip-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of used IPv4 addresses
                ''',
                'used_ip_count',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'ip-pool',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'DhcpState.Server' : {
        'meta_info' : _MetaInfoClass('DhcpState.Server',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_CLASS, 'Host' , 'ydk.models.ietf.ietf_dhcp', 'DhcpState.Server.Host', 
                [], [], 
                '''                Host status information
                ''',
                'host',
                'ietf-dhcp', False),
            _MetaInfoClassMember('ip-pool', REFERENCE_LIST, 'IpPool' , 'ydk.models.ietf.ietf_dhcp', 'DhcpState.Server.IpPool', 
                [], [], 
                '''                Global IP pool configuration
                ''',
                'ip_pool',
                'ietf-dhcp', False),
            _MetaInfoClassMember('packet-statistics', REFERENCE_CLASS, 'PacketStatistics' , 'ydk.models.ietf.ietf_dhcp', 'DhcpState.Server.PacketStatistics', 
                [], [], 
                '''                Packet statistics
                ''',
                'packet_statistics',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'server',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'DhcpState.Relay.PacketStatistics.Receive' : {
        'meta_info' : _MetaInfoClass('DhcpState.Relay.PacketStatistics.Receive',
            False, 
            [
            _MetaInfoClassMember('ack-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPACK packets
                ''',
                'ack_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('decline-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPDECLINE packets
                ''',
                'decline_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('discover-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPDISCOVER packets
                ''',
                'discover_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('inform-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPINFORM packets
                ''',
                'inform_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('nack-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPNAK packets
                ''',
                'nack_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('offer-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPOFFER packets
                ''',
                'offer_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('release-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPRELEASE packets
                ''',
                'release_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('request-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPREQUEST packets
                ''',
                'request_packet',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'receive',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'DhcpState.Relay.PacketStatistics.Send' : {
        'meta_info' : _MetaInfoClass('DhcpState.Relay.PacketStatistics.Send',
            False, 
            [
            _MetaInfoClassMember('ack-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPACK packets
                ''',
                'ack_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('decline-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPDECLINE packets
                ''',
                'decline_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('discover-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPDISCOVER packets
                ''',
                'discover_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('inform-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPINFORM packets
                ''',
                'inform_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('nack-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPNAK packets
                ''',
                'nack_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('offer-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPOFFER packets
                ''',
                'offer_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('release-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPRELEASE packets
                ''',
                'release_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('request-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPREQUEST packets
                ''',
                'request_packet',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'send',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'DhcpState.Relay.PacketStatistics' : {
        'meta_info' : _MetaInfoClass('DhcpState.Relay.PacketStatistics',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the interface
                ''',
                'interface',
                'ietf-dhcp', False),
            _MetaInfoClassMember('receive', REFERENCE_CLASS, 'Receive' , 'ydk.models.ietf.ietf_dhcp', 'DhcpState.Relay.PacketStatistics.Receive', 
                [], [], 
                '''                Number of  received packets
                ''',
                'receive',
                'ietf-dhcp', False),
            _MetaInfoClassMember('send', REFERENCE_CLASS, 'Send' , 'ydk.models.ietf.ietf_dhcp', 'DhcpState.Relay.PacketStatistics.Send', 
                [], [], 
                '''                Number of sent packets
                ''',
                'send',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'packet-statistics',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'DhcpState.Relay' : {
        'meta_info' : _MetaInfoClass('DhcpState.Relay',
            False, 
            [
            _MetaInfoClassMember('packet-statistics', REFERENCE_CLASS, 'PacketStatistics' , 'ydk.models.ietf.ietf_dhcp', 'DhcpState.Relay.PacketStatistics', 
                [], [], 
                '''                Packet statistics
                ''',
                'packet_statistics',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'relay',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'DhcpState.Client.PacketStatistics.Receive' : {
        'meta_info' : _MetaInfoClass('DhcpState.Client.PacketStatistics.Receive',
            False, 
            [
            _MetaInfoClassMember('ack-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPACK packets
                ''',
                'ack_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('nack-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPNAK packets
                ''',
                'nack_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('offer-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPOFFER packets
                ''',
                'offer_packet',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'receive',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'DhcpState.Client.PacketStatistics.Send' : {
        'meta_info' : _MetaInfoClass('DhcpState.Client.PacketStatistics.Send',
            False, 
            [
            _MetaInfoClassMember('decline-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPDECLINE packets
                ''',
                'decline_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('discover-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPDISCOVER packets
                ''',
                'discover_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('inform-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPINFORM packets
                ''',
                'inform_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('release-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPRELEASE packets
                ''',
                'release_packet',
                'ietf-dhcp', False),
            _MetaInfoClassMember('request-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of DHCPREQUEST packets
                ''',
                'request_packet',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'send',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'DhcpState.Client.PacketStatistics' : {
        'meta_info' : _MetaInfoClass('DhcpState.Client.PacketStatistics',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the interface
                ''',
                'interface',
                'ietf-dhcp', False),
            _MetaInfoClassMember('receive', REFERENCE_CLASS, 'Receive' , 'ydk.models.ietf.ietf_dhcp', 'DhcpState.Client.PacketStatistics.Receive', 
                [], [], 
                '''                Number of  received packets
                ''',
                'receive',
                'ietf-dhcp', False),
            _MetaInfoClassMember('send', REFERENCE_CLASS, 'Send' , 'ydk.models.ietf.ietf_dhcp', 'DhcpState.Client.PacketStatistics.Send', 
                [], [], 
                '''                Number of sent packets
                ''',
                'send',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'packet-statistics',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'DhcpState.Client' : {
        'meta_info' : _MetaInfoClass('DhcpState.Client',
            False, 
            [
            _MetaInfoClassMember('packet-statistics', REFERENCE_CLASS, 'PacketStatistics' , 'ydk.models.ietf.ietf_dhcp', 'DhcpState.Client.PacketStatistics', 
                [], [], 
                '''                Packet statistics
                ''',
                'packet_statistics',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'client',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'DhcpState' : {
        'meta_info' : _MetaInfoClass('DhcpState',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_CLASS, 'Client' , 'ydk.models.ietf.ietf_dhcp', 'DhcpState.Client', 
                [], [], 
                '''                DHCP client state data
                ''',
                'client',
                'ietf-dhcp', False),
            _MetaInfoClassMember('relay', REFERENCE_CLASS, 'Relay' , 'ydk.models.ietf.ietf_dhcp', 'DhcpState.Relay', 
                [], [], 
                '''                DHCP reply agent state data
                ''',
                'relay',
                'ietf-dhcp', False),
            _MetaInfoClassMember('server', REFERENCE_CLASS, 'Server' , 'ydk.models.ietf.ietf_dhcp', 'DhcpState.Server', 
                [], [], 
                '''                DHCP server state data
                ''',
                'server',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'dhcp-state',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'CleanServerStatisticsRpc.Input' : {
        'meta_info' : _MetaInfoClass('CleanServerStatisticsRpc.Input',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the interface
                ''',
                'interface',
                'ietf-dhcp', False),
            _MetaInfoClassMember('clean-at', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                The start time to clean packet statistics
                ''',
                'clean_at',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'input',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'CleanServerStatisticsRpc.Output' : {
        'meta_info' : _MetaInfoClass('CleanServerStatisticsRpc.Output',
            False, 
            [
            _MetaInfoClassMember('clean-finished-at', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                The finish time to clean packet statistics
                ''',
                'clean_finished_at',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'output',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'CleanServerStatisticsRpc' : {
        'meta_info' : _MetaInfoClass('CleanServerStatisticsRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_dhcp', 'CleanServerStatisticsRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-dhcp', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_dhcp', 'CleanServerStatisticsRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'clean-server-statistics',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'CleanRelayStatisticsRpc.Input' : {
        'meta_info' : _MetaInfoClass('CleanRelayStatisticsRpc.Input',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the interface
                ''',
                'interface',
                'ietf-dhcp', False),
            _MetaInfoClassMember('clean-at', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                The start time to clean packet statistics
                ''',
                'clean_at',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'input',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'CleanRelayStatisticsRpc.Output' : {
        'meta_info' : _MetaInfoClass('CleanRelayStatisticsRpc.Output',
            False, 
            [
            _MetaInfoClassMember('clean-finished-at', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                The finish time to clean packet statistics
                ''',
                'clean_finished_at',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'output',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'CleanRelayStatisticsRpc' : {
        'meta_info' : _MetaInfoClass('CleanRelayStatisticsRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_dhcp', 'CleanRelayStatisticsRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-dhcp', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_dhcp', 'CleanRelayStatisticsRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'clean-relay-statistics',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'CleanClientStatisticsRpc.Input' : {
        'meta_info' : _MetaInfoClass('CleanClientStatisticsRpc.Input',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the interface
                ''',
                'interface',
                'ietf-dhcp', False),
            _MetaInfoClassMember('clean-at', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                The start time to clean packet statistics
                ''',
                'clean_at',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'input',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'CleanClientStatisticsRpc.Output' : {
        'meta_info' : _MetaInfoClass('CleanClientStatisticsRpc.Output',
            False, 
            [
            _MetaInfoClassMember('clean-finished-at', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                The finish time to clean packet statistics
                ''',
                'clean_finished_at',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'output',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
    'CleanClientStatisticsRpc' : {
        'meta_info' : _MetaInfoClass('CleanClientStatisticsRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_dhcp', 'CleanClientStatisticsRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-dhcp', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_dhcp', 'CleanClientStatisticsRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-dhcp', False),
            ],
            'ietf-dhcp',
            'clean-client-statistics',
            _yang_ns._namespaces['ietf-dhcp'],
        'ydk.models.ietf.ietf_dhcp'
        ),
    },
}
_meta_table['Dhcp.Server.DhcpIpPool.ManualAllocation']['meta_info'].parent =_meta_table['Dhcp.Server.DhcpIpPool']['meta_info']
_meta_table['Dhcp.Server.DhcpIpPool.Section']['meta_info'].parent =_meta_table['Dhcp.Server.DhcpIpPool']['meta_info']
_meta_table['Dhcp.Server.DhcpIpPool.Option']['meta_info'].parent =_meta_table['Dhcp.Server.DhcpIpPool']['meta_info']
_meta_table['Dhcp.Server.Option']['meta_info'].parent =_meta_table['Dhcp.Server']['meta_info']
_meta_table['Dhcp.Server.DhcpIpPool']['meta_info'].parent =_meta_table['Dhcp.Server']['meta_info']
_meta_table['Dhcp.Relay.ServerGroup']['meta_info'].parent =_meta_table['Dhcp.Relay']['meta_info']
_meta_table['Dhcp.Client.Interfaces']['meta_info'].parent =_meta_table['Dhcp.Client']['meta_info']
_meta_table['Dhcp.Server']['meta_info'].parent =_meta_table['Dhcp']['meta_info']
_meta_table['Dhcp.Relay']['meta_info'].parent =_meta_table['Dhcp']['meta_info']
_meta_table['Dhcp.Client']['meta_info'].parent =_meta_table['Dhcp']['meta_info']
_meta_table['DhcpState.Server.PacketStatistics.Receive']['meta_info'].parent =_meta_table['DhcpState.Server.PacketStatistics']['meta_info']
_meta_table['DhcpState.Server.PacketStatistics.Send']['meta_info'].parent =_meta_table['DhcpState.Server.PacketStatistics']['meta_info']
_meta_table['DhcpState.Server.PacketStatistics']['meta_info'].parent =_meta_table['DhcpState.Server']['meta_info']
_meta_table['DhcpState.Server.Host']['meta_info'].parent =_meta_table['DhcpState.Server']['meta_info']
_meta_table['DhcpState.Server.IpPool']['meta_info'].parent =_meta_table['DhcpState.Server']['meta_info']
_meta_table['DhcpState.Relay.PacketStatistics.Receive']['meta_info'].parent =_meta_table['DhcpState.Relay.PacketStatistics']['meta_info']
_meta_table['DhcpState.Relay.PacketStatistics.Send']['meta_info'].parent =_meta_table['DhcpState.Relay.PacketStatistics']['meta_info']
_meta_table['DhcpState.Relay.PacketStatistics']['meta_info'].parent =_meta_table['DhcpState.Relay']['meta_info']
_meta_table['DhcpState.Client.PacketStatistics.Receive']['meta_info'].parent =_meta_table['DhcpState.Client.PacketStatistics']['meta_info']
_meta_table['DhcpState.Client.PacketStatistics.Send']['meta_info'].parent =_meta_table['DhcpState.Client.PacketStatistics']['meta_info']
_meta_table['DhcpState.Client.PacketStatistics']['meta_info'].parent =_meta_table['DhcpState.Client']['meta_info']
_meta_table['DhcpState.Server']['meta_info'].parent =_meta_table['DhcpState']['meta_info']
_meta_table['DhcpState.Relay']['meta_info'].parent =_meta_table['DhcpState']['meta_info']
_meta_table['DhcpState.Client']['meta_info'].parent =_meta_table['DhcpState']['meta_info']
_meta_table['CleanServerStatisticsRpc.Input']['meta_info'].parent =_meta_table['CleanServerStatisticsRpc']['meta_info']
_meta_table['CleanServerStatisticsRpc.Output']['meta_info'].parent =_meta_table['CleanServerStatisticsRpc']['meta_info']
_meta_table['CleanRelayStatisticsRpc.Input']['meta_info'].parent =_meta_table['CleanRelayStatisticsRpc']['meta_info']
_meta_table['CleanRelayStatisticsRpc.Output']['meta_info'].parent =_meta_table['CleanRelayStatisticsRpc']['meta_info']
_meta_table['CleanClientStatisticsRpc.Input']['meta_info'].parent =_meta_table['CleanClientStatisticsRpc']['meta_info']
_meta_table['CleanClientStatisticsRpc.Output']['meta_info'].parent =_meta_table['CleanClientStatisticsRpc']['meta_info']
