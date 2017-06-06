


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IpTcp.Directory' : {
        'meta_info' : _MetaInfoClass('IpTcp.Directory',
            False, 
            [
            _MetaInfoClassMember('directoryname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Directory name 
                ''',
                'directoryname',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('max-debug-files', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Set number of Debug files
                ''',
                'max_debug_files',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('max-file-size-files', ATTRIBUTE, 'int' , None, None, 
                [('1024', '4294967295')], [], 
                '''                Set size of debug files in bytes
                ''',
                'max_file_size_files',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'directory',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'IpTcp.Throttle' : {
        'meta_info' : _MetaInfoClass('IpTcp.Throttle',
            False, 
            [
            _MetaInfoClassMember('tcpmaxthrottle', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Max throttle
                ''',
                'tcpmaxthrottle',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('tcpmin-throttle', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Min throttle
                ''',
                'tcpmin_throttle',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'IpTcp.NumThread' : {
        'meta_info' : _MetaInfoClass('IpTcp.NumThread',
            False, 
            [
            _MetaInfoClassMember('tcp-in-q-threads', ATTRIBUTE, 'int' , None, None, 
                [('1', '16')], [], 
                '''                InQ Threads
                ''',
                'tcp_in_q_threads',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('tcp-out-q-threads', ATTRIBUTE, 'int' , None, None, 
                [('1', '16')], [], 
                '''                OutQ Threads
                ''',
                'tcp_out_q_threads',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'num-thread',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'IpTcp' : {
        'meta_info' : _MetaInfoClass('IpTcp',
            False, 
            [
            _MetaInfoClassMember('accept-rate', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                TCP connection accept rate
                ''',
                'accept_rate',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('directory', REFERENCE_CLASS, 'Directory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'IpTcp.Directory', 
                [], [], 
                '''                TCP directory details
                ''',
                'directory',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('maximum-segment-size', ATTRIBUTE, 'int' , None, None, 
                [('68', '10000')], [], 
                '''                TCP initial maximum segment size
                ''',
                'maximum_segment_size',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('num-thread', REFERENCE_CLASS, 'NumThread' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'IpTcp.NumThread', 
                [], [], 
                '''                TCP InQueue and OutQueue threads
                ''',
                'num_thread',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('path-mtu-discovery', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Aging time; 0 for infinite, and range be (10,30)
                ''',
                'path_mtu_discovery',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('receive-q', ATTRIBUTE, 'int' , None, None, 
                [('40', '800')], [], 
                '''                TCP receive Queue Size
                ''',
                'receive_q',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('selective-ack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable TCP selective-ACK
                ''',
                'selective_ack',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('syn-wait-time', ATTRIBUTE, 'int' , None, None, 
                [('5', '30')], [], 
                '''                Time to wait on new TCP connections in seconds
                ''',
                'syn_wait_time',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('throttle', REFERENCE_CLASS, 'Throttle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'IpTcp.Throttle', 
                [], [], 
                '''                Throttle TCP receive buffer (in percentage)
                ''',
                'throttle',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('timestamp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable TCP timestamp option
                ''',
                'timestamp',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('window-size', ATTRIBUTE, 'int' , None, None, 
                [('2048', '65535')], [], 
                '''                TCP receive window size (bytes)
                ''',
                'window_size',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'ip-tcp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers',
            False, 
            [
            _MetaInfoClassMember('access-control-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access list
                ''',
                'access_control_list_name',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('small-server', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set number of allowable TCP small servers,
                specify 0 for no-limit
                ''',
                'small_server',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'tcp-small-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers',
            False, 
            [
            _MetaInfoClassMember('access-control-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Specify the access list
                ''',
                'access_control_list_name',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            _MetaInfoClassMember('small-server', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Set number of allowable small servers, specify
                0 for no-limit
                ''',
                'small_server',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-udp-cfg',
            'udp-small-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Ipv4.SmallServers' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Ipv4.SmallServers',
            False, 
            [
            _MetaInfoClassMember('tcp-small-servers', REFERENCE_CLASS, 'TcpSmallServers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers', 
                [], [], 
                '''                Describing TCP related IPV4 and IPV6 small
                servers
                ''',
                'tcp_small_servers',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('udp-small-servers', REFERENCE_CLASS, 'UdpSmallServers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers', 
                [], [], 
                '''                UDP small servers configuration
                ''',
                'udp_small_servers',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'small-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Ipv4' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Ipv4',
            False, 
            [
            _MetaInfoClassMember('small-servers', REFERENCE_CLASS, 'SmallServers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv4.SmallServers', 
                [], [], 
                '''                Describing IPV4 and IPV6 small servers
                ''',
                'small_servers',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access list
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('maximum-server', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Set number of allowable servers
                ''',
                'maximum_server',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'tcp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet',
            False, 
            [
            _MetaInfoClassMember('tcp', REFERENCE_CLASS, 'Tcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp', 
                [], [], 
                '''                TCP details
                ''',
                'tcp',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'telnet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access list
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('dscp-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set IP DSCP (DiffServ CodePoint) for TFTP
                Server Packets
                ''',
                'dscp_value',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('home-directory', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Specify device name where file is read from (e
                .g. flash:)
                ''',
                'home_directory',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('maximum-server', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Set number of allowable servers, 0 for
                no-limit
                ''',
                'maximum_server',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'udp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp',
            False, 
            [
            _MetaInfoClassMember('udp', REFERENCE_CLASS, 'Udp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp', 
                [], [], 
                '''                UDP details
                ''',
                'udp',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'tftp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv6',
            False, 
            [
            _MetaInfoClassMember('telnet', REFERENCE_CLASS, 'Telnet' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet', 
                [], [], 
                '''                TELNET server configuration commands
                ''',
                'telnet',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('tftp', REFERENCE_CLASS, 'Tftp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp', 
                [], [], 
                '''                TFTP server configuration commands
                ''',
                'tftp',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access list
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('maximum-server', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Set number of allowable servers
                ''',
                'maximum_server',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'tcp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet',
            False, 
            [
            _MetaInfoClassMember('tcp', REFERENCE_CLASS, 'Tcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp', 
                [], [], 
                '''                TCP details
                ''',
                'tcp',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'telnet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access list
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('dscp-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set IP DSCP (DiffServ CodePoint) for TFTP
                Server Packets
                ''',
                'dscp_value',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('home-directory', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Specify device name where file is read from (e
                .g. flash:)
                ''',
                'home_directory',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('maximum-server', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Set number of allowable servers, 0 for
                no-limit
                ''',
                'maximum_server',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'udp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp',
            False, 
            [
            _MetaInfoClassMember('udp', REFERENCE_CLASS, 'Udp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp', 
                [], [], 
                '''                UDP details
                ''',
                'udp',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'tftp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf.Ipv4',
            False, 
            [
            _MetaInfoClassMember('telnet', REFERENCE_CLASS, 'Telnet' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet', 
                [], [], 
                '''                TELNET server configuration commands
                ''',
                'telnet',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('tftp', REFERENCE_CLASS, 'Tftp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp', 
                [], [], 
                '''                TFTP server configuration commands
                ''',
                'tftp',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the VRF instance
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-tcp-cfg', True),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv4', 
                [], [], 
                '''                IPV4 related services
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf.Ipv6', 
                [], [], 
                '''                IPV6 related services
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs.Vrf', 
                [], [], 
                '''                VRF specific data
                ''',
                'vrf',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers',
            False, 
            [
            _MetaInfoClassMember('access-control-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access list
                ''',
                'access_control_list_name',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('small-server', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set number of allowable TCP small servers,
                specify 0 for no-limit
                ''',
                'small_server',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'tcp-small-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Ipv6.SmallServers' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Ipv6.SmallServers',
            False, 
            [
            _MetaInfoClassMember('tcp-small-servers', REFERENCE_CLASS, 'TcpSmallServers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers', 
                [], [], 
                '''                Describing TCP related IPV4 and IPV6 small
                servers
                ''',
                'tcp_small_servers',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'small-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services.Ipv6' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services.Ipv6',
            False, 
            [
            _MetaInfoClassMember('small-servers', REFERENCE_CLASS, 'SmallServers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv6.SmallServers', 
                [], [], 
                '''                Describing IPV4 and IPV6 small servers
                ''',
                'small_servers',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd.Services' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd.Services',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv4', 
                [], [], 
                '''                IPV4 related services
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Ipv6', 
                [], [], 
                '''                IPV6 related services
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services.Vrfs', 
                [], [], 
                '''                VRF table
                ''',
                'vrfs',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'services',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.Cinetd' : {
        'meta_info' : _MetaInfoClass('Ip.Cinetd',
            False, 
            [
            _MetaInfoClassMember('services', REFERENCE_CLASS, 'Services' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd.Services', 
                [], [], 
                '''                Describing services of cinetd
                ''',
                'services',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'cinetd',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.ForwardProtocol.Udp.Ports.Port' : {
        'meta_info' : _MetaInfoClass('Ip.ForwardProtocol.Udp.Ports.Port',
            False, 
            [
            _MetaInfoClassMember('port-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Port number
                ''',
                'port_id',
                'Cisco-IOS-XR-ip-udp-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify 'false' to disable well-known ports
                Domain (53), TFTP (69), NameServer (42),
                TACACS (49), NetBiosNameService (137), or
                NetBiosDatagramService (138).  Specify
                'true' to enable non well-known ports.
                ''',
                'enable',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-udp-cfg',
            'port',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.ForwardProtocol.Udp.Ports' : {
        'meta_info' : _MetaInfoClass('Ip.ForwardProtocol.Udp.Ports',
            False, 
            [
            _MetaInfoClassMember('port', REFERENCE_LIST, 'Port' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.ForwardProtocol.Udp.Ports.Port', 
                [], [], 
                '''                Well-known ports are enabled by default and
                non well-known ports are disabled by default.
                It is not allowed to configure the default.
                ''',
                'port',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-udp-cfg',
            'ports',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.ForwardProtocol.Udp' : {
        'meta_info' : _MetaInfoClass('Ip.ForwardProtocol.Udp',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable IP Forward Protocol UDP
                ''',
                'disable',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            _MetaInfoClassMember('ports', REFERENCE_CLASS, 'Ports' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.ForwardProtocol.Udp.Ports', 
                [], [], 
                '''                Port configuration
                ''',
                'ports',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-udp-cfg',
            'udp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip.ForwardProtocol' : {
        'meta_info' : _MetaInfoClass('Ip.ForwardProtocol',
            False, 
            [
            _MetaInfoClassMember('udp', REFERENCE_CLASS, 'Udp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.ForwardProtocol.Udp', 
                [], [], 
                '''                Packets to a specific UDP port
                ''',
                'udp',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-udp-cfg',
            'forward-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
    'Ip' : {
        'meta_info' : _MetaInfoClass('Ip',
            False, 
            [
            _MetaInfoClassMember('cinetd', REFERENCE_CLASS, 'Cinetd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.Cinetd', 
                [], [], 
                '''                Cinetd configuration data
                ''',
                'cinetd',
                'Cisco-IOS-XR-ip-tcp-cfg', False),
            _MetaInfoClassMember('forward-protocol', REFERENCE_CLASS, 'ForwardProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip.ForwardProtocol', 
                [], [], 
                '''                Controls forwarding of physical and directed IP
                broadcasts
                ''',
                'forward_protocol',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-tcp-cfg',
            'ip',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg'
        ),
    },
}
_meta_table['IpTcp.Directory']['meta_info'].parent =_meta_table['IpTcp']['meta_info']
_meta_table['IpTcp.Throttle']['meta_info'].parent =_meta_table['IpTcp']['meta_info']
_meta_table['IpTcp.NumThread']['meta_info'].parent =_meta_table['IpTcp']['meta_info']
_meta_table['Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Ipv4.SmallServers']['meta_info']
_meta_table['Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Ipv4.SmallServers']['meta_info']
_meta_table['Ip.Cinetd.Services.Ipv4.SmallServers']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Ipv4']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv6']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf.Ipv4']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs.Vrf']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Vrfs']['meta_info']
_meta_table['Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Ipv6.SmallServers']['meta_info']
_meta_table['Ip.Cinetd.Services.Ipv6.SmallServers']['meta_info'].parent =_meta_table['Ip.Cinetd.Services.Ipv6']['meta_info']
_meta_table['Ip.Cinetd.Services.Ipv4']['meta_info'].parent =_meta_table['Ip.Cinetd.Services']['meta_info']
_meta_table['Ip.Cinetd.Services.Vrfs']['meta_info'].parent =_meta_table['Ip.Cinetd.Services']['meta_info']
_meta_table['Ip.Cinetd.Services.Ipv6']['meta_info'].parent =_meta_table['Ip.Cinetd.Services']['meta_info']
_meta_table['Ip.Cinetd.Services']['meta_info'].parent =_meta_table['Ip.Cinetd']['meta_info']
_meta_table['Ip.ForwardProtocol.Udp.Ports.Port']['meta_info'].parent =_meta_table['Ip.ForwardProtocol.Udp.Ports']['meta_info']
_meta_table['Ip.ForwardProtocol.Udp.Ports']['meta_info'].parent =_meta_table['Ip.ForwardProtocol.Udp']['meta_info']
_meta_table['Ip.ForwardProtocol.Udp']['meta_info'].parent =_meta_table['Ip.ForwardProtocol']['meta_info']
_meta_table['Ip.Cinetd']['meta_info'].parent =_meta_table['Ip']['meta_info']
_meta_table['Ip.ForwardProtocol']['meta_info'].parent =_meta_table['Ip']['meta_info']
