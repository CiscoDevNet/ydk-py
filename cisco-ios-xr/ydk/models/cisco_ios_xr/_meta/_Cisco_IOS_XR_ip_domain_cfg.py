


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host',
            False, 
            [
            _MetaInfoClassMember('host-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A hostname
                ''',
                'host_name',
                'Cisco-IOS-XR-ip-domain-cfg', True),
            _MetaInfoClassMember('address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Host IPv6 addresses
                ''',
                'address',
                'Cisco-IOS-XR-ip-domain-cfg', False, max_elements=4, min_elements=1),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'ipv6-host',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-domain-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg'
        ),
    },
    'IpDomain.Vrfs.Vrf.Ipv6Hosts' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Ipv6Hosts',
            False, 
            [
            _MetaInfoClassMember('ipv6-host', REFERENCE_LIST, 'Ipv6Host' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host', 
                [], [], 
                '''                Host name and up to 4 host IPv6 addresses
                ''',
                'ipv6_host',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'ipv6-hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-domain-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg'
        ),
    },
    'IpDomain.Vrfs.Vrf.Servers.Server' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Servers.Server',
            False, 
            [
            _MetaInfoClassMember('order', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This is used to sort the servers in the
                order of precedence
                ''',
                'order',
                'Cisco-IOS-XR-ip-domain-cfg', True),
            _MetaInfoClassMember('server-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                A name server address
                ''',
                'server_address',
                'Cisco-IOS-XR-ip-domain-cfg', True, [
                    _MetaInfoClassMember('server-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        A name server address
                        ''',
                        'server_address',
                        'Cisco-IOS-XR-ip-domain-cfg', True),
                    _MetaInfoClassMember('server-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        A name server address
                        ''',
                        'server_address',
                        'Cisco-IOS-XR-ip-domain-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-domain-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg'
        ),
    },
    'IpDomain.Vrfs.Vrf.Servers' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Servers',
            False, 
            [
            _MetaInfoClassMember('server', REFERENCE_LIST, 'Server' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs.Vrf.Servers.Server', 
                [], [], 
                '''                Name server address
                ''',
                'server',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'servers',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-domain-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg'
        ),
    },
    'IpDomain.Vrfs.Vrf.Lists.List' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Lists.List',
            False, 
            [
            _MetaInfoClassMember('order', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This is used to sort the names in the order
                of precedence
                ''',
                'order',
                'Cisco-IOS-XR-ip-domain-cfg', True),
            _MetaInfoClassMember('list-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                A domain name
                ''',
                'list_name',
                'Cisco-IOS-XR-ip-domain-cfg', True),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'list',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-domain-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg'
        ),
    },
    'IpDomain.Vrfs.Vrf.Lists' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Lists',
            False, 
            [
            _MetaInfoClassMember('list', REFERENCE_LIST, 'List' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs.Vrf.Lists.List', 
                [], [], 
                '''                Domain name to complete unqualified host
                names
                ''',
                'list',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'lists',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-domain-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg'
        ),
    },
    'IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host',
            False, 
            [
            _MetaInfoClassMember('host-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A hostname
                ''',
                'host_name',
                'Cisco-IOS-XR-ip-domain-cfg', True),
            _MetaInfoClassMember('address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Host IPv4 addresses
                ''',
                'address',
                'Cisco-IOS-XR-ip-domain-cfg', False, max_elements=8, min_elements=1),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'ipv4-host',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-domain-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg'
        ),
    },
    'IpDomain.Vrfs.Vrf.Ipv4Hosts' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf.Ipv4Hosts',
            False, 
            [
            _MetaInfoClassMember('ipv4-host', REFERENCE_LIST, 'Ipv4Host' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host', 
                [], [], 
                '''                Host name and up to 8 host IPv4 addresses
                ''',
                'ipv4_host',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'ipv4-hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-domain-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg'
        ),
    },
    'IpDomain.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the VRF instance
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-domain-cfg', True),
            _MetaInfoClassMember('ipv4-hosts', REFERENCE_CLASS, 'Ipv4Hosts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs.Vrf.Ipv4Hosts', 
                [], [], 
                '''                IPv4 host
                ''',
                'ipv4_hosts',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            _MetaInfoClassMember('ipv6-hosts', REFERENCE_CLASS, 'Ipv6Hosts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs.Vrf.Ipv6Hosts', 
                [], [], 
                '''                IPv6 host
                ''',
                'ipv6_hosts',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            _MetaInfoClassMember('lists', REFERENCE_CLASS, 'Lists' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs.Vrf.Lists', 
                [], [], 
                '''                Domain names to complete unqualified host
                names
                ''',
                'lists',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            _MetaInfoClassMember('lookup', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Domain Name System hostname
                translation
                ''',
                'lookup',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            _MetaInfoClassMember('multicast-domain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Default multicast domain name
                ''',
                'multicast_domain',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Default domain name
                ''',
                'name',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            _MetaInfoClassMember('servers', REFERENCE_CLASS, 'Servers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs.Vrf.Servers', 
                [], [], 
                '''                Name server addresses
                ''',
                'servers',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Specify interface for source address in
                connections
                ''',
                'source_interface',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-domain-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg'
        ),
    },
    'IpDomain.Vrfs' : {
        'meta_info' : _MetaInfoClass('IpDomain.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs.Vrf', 
                [], [], 
                '''                VRF specific data
                ''',
                'vrf',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-domain-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg'
        ),
    },
    'IpDomain' : {
        'meta_info' : _MetaInfoClass('IpDomain',
            False, 
            [
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg', 'IpDomain.Vrfs', 
                [], [], 
                '''                VRF table
                ''',
                'vrfs',
                'Cisco-IOS-XR-ip-domain-cfg', False),
            ],
            'Cisco-IOS-XR-ip-domain-cfg',
            'ip-domain',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-domain-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg'
        ),
    },
}
_meta_table['IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf.Ipv6Hosts']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Servers.Server']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf.Servers']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Lists.List']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf.Lists']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf.Ipv4Hosts']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Ipv6Hosts']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Servers']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Lists']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf.Ipv4Hosts']['meta_info'].parent =_meta_table['IpDomain.Vrfs.Vrf']['meta_info']
_meta_table['IpDomain.Vrfs.Vrf']['meta_info'].parent =_meta_table['IpDomain.Vrfs']['meta_info']
_meta_table['IpDomain.Vrfs']['meta_info'].parent =_meta_table['IpDomain']['meta_info']
