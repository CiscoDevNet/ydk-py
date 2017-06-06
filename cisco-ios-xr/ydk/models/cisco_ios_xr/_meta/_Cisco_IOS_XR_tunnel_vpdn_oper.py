


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SessionStateEnum' : _MetaInfoEnum('SessionStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper',
        {
            'idle':'idle',
            'connected':'connected',
            'established':'established',
        }, 'Cisco-IOS-XR-tunnel-vpdn-oper', _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper']),
    'VpdnFailcodeEnum' : _MetaInfoEnum('VpdnFailcodeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper',
        {
            'unknown':'unknown',
            'peer-action':'peer_action',
            'authentication':'authentication',
            'authentication-error':'authentication_error',
            'authentication-failed':'authentication_failed',
            'authorization':'authorization',
            'authorization-failed':'authorization_failed',
            'home-gatewayfailure':'home_gatewayfailure',
            'connection-termination':'connection_termination',
            'no-resources-available':'no_resources_available',
            'timer-expiry':'timer_expiry',
            'session-mid-exceeded':'session_mid_exceeded',
            'soft-shut':'soft_shut',
            'session-limit-exceeded':'session_limit_exceeded',
            'administrative':'administrative',
            'link-failure':'link_failure',
            'security':'security',
            'tunnel-in-resync':'tunnel_in_resync',
            'call-prarmeters':'call_prarmeters',
        }, 'Cisco-IOS-XR-tunnel-vpdn-oper', _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper']),
    'VpdnStateEnum' : _MetaInfoEnum('VpdnStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper',
        {
            'initial-state':'initial_state',
            'init-sync-in-progress':'init_sync_in_progress',
            'steady-state':'steady_state',
        }, 'Cisco-IOS-XR-tunnel-vpdn-oper', _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper']),
    'VpdnNasPortEnum' : _MetaInfoEnum('VpdnNasPortEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper',
        {
            'none':'none',
            'primary':'primary',
            'bri':'bri',
            'serial':'serial',
            'asynchronous':'asynchronous',
            'vty':'vty',
            'atm':'atm',
            'ethernet':'ethernet',
            'ppp-atm':'ppp_atm',
            'pppoe-over-atm':'pppoe_over_atm',
            'pppoe-over-ethernet':'pppoe_over_ethernet',
            'pppoe-over-vlan':'pppoe_over_vlan',
            'pppoe-over-q-in-q':'pppoe_over_q_in_q',
            'v120':'v120',
            'v110':'v110',
            'piafs':'piafs',
            'x75':'x75',
            'ip-sec':'ip_sec',
            'other':'other',
            'virtual-pppoe-over-ethernet':'virtual_pppoe_over_ethernet',
            'virtual-pppoe-over-vlan':'virtual_pppoe_over_vlan',
            'virtual-pppoe-over-q-in-q':'virtual_pppoe_over_q_in_q',
            'ipo-e-over-ethernet':'ipo_e_over_ethernet',
            'ipo-e-over-vlan':'ipo_e_over_vlan',
            'ipo-e-over-q-in-q':'ipo_e_over_q_in_q',
            'virtual-i-po-e-over-ethernet':'virtual_i_po_e_over_ethernet',
            'virtual-i-po-e-over-vlan':'virtual_i_po_e_over_vlan',
            'virtual-i-po-e-over-q-in-q':'virtual_i_po_e_over_q_in_q',
            'unknown':'unknown',
        }, 'Cisco-IOS-XR-tunnel-vpdn-oper', _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper']),
    'LsgStatusEnum' : _MetaInfoEnum('LsgStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper',
        {
            'none':'none',
            'active':'active',
            'down':'down',
            'testable':'testable',
            'testing':'testing',
        }, 'Cisco-IOS-XR-tunnel-vpdn-oper', _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper']),
    'TosModeEnum' : _MetaInfoEnum('TosModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper',
        {
            'default':'default',
            'set':'set',
            'reflect':'reflect',
        }, 'Cisco-IOS-XR-tunnel-vpdn-oper', _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper']),
    'Vpdn.Sessions.Session.Session_' : {
        'meta_info' : _MetaInfoClass('Vpdn.Sessions.Session.Session_',
            False, 
            [
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Session interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('l2tp-session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                L2TP session ID
                ''',
                'l2tp_session_id',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('l2tp-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                L2TP tunnel ID
                ''',
                'l2tp_tunnel_id',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('last-change', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Elapsed time since last change in hh:mm:ss
                format
                ''',
                'last_change',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('srg-slave', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Session SRG Slave
                ''',
                'srg_slave',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'SessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'SessionStateEnum', 
                [], [], 
                '''                Session state
                ''',
                'state',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('username', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Authentication username
                ''',
                'username',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-oper',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper'
        ),
    },
    'Vpdn.Sessions.Session.L2Tp' : {
        'meta_info' : _MetaInfoClass('Vpdn.Sessions.Session.L2Tp',
            False, 
            [
            _MetaInfoClassMember('call-serial-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Call serial number
                ''',
                'call_serial_number',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('is-l2tp-class-attribute-mask-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if L2TP class attribute mask is set
                ''',
                'is_l2tp_class_attribute_mask_set',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('is-tunnel-authentication-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if tunnel authentication is enabled
                ''',
                'is_tunnel_authentication_enabled',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('local-endpoint', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Local endpoint IP address
                ''',
                'local_endpoint',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('local-session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local session ID
                ''',
                'local_session_id',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('local-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local tunnel ID
                ''',
                'local_tunnel_id',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('remote-endpoint', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote endpoint IP address
                ''',
                'remote_endpoint',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('remote-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remote port
                ''',
                'remote_port',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('remote-session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remote session ID
                ''',
                'remote_session_id',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('remote-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remote tunnel ID
                ''',
                'remote_tunnel_id',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('tunnel-assignment-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Tunnel assignment ID
                ''',
                'tunnel_assignment_id',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('tunnel-client-authentication-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Tunnel client authentication ID
                ''',
                'tunnel_client_authentication_id',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('tunnel-server-authentication-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Tunnel server authentication ID
                ''',
                'tunnel_server_authentication_id',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-oper',
            'l2tp',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper'
        ),
    },
    'Vpdn.Sessions.Session.Subscriber' : {
        'meta_info' : _MetaInfoClass('Vpdn.Sessions.Session.Subscriber',
            False, 
            [
            _MetaInfoClassMember('nas-port', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                NAS port ID
                ''',
                'nas_port',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('nas-port-type', REFERENCE_ENUM_CLASS, 'VpdnNasPortEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'VpdnNasPortEnum', 
                [], [], 
                '''                NAS port type
                ''',
                'nas_port_type',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('physical-channel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Physical channel ID
                ''',
                'physical_channel_id',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('receive-connect-speed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Receive connect speed in nanoseconds
                ''',
                'receive_connect_speed',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('transmit-connect-speed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmit connect speed in nanoseconds
                ''',
                'transmit_connect_speed',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-oper',
            'subscriber',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper'
        ),
    },
    'Vpdn.Sessions.Session.Configuration.VpnId' : {
        'meta_info' : _MetaInfoClass('Vpdn.Sessions.Session.Configuration.VpnId',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index
                ''',
                'index',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('oui', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OUI
                ''',
                'oui',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-oper',
            'vpn-id',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper'
        ),
    },
    'Vpdn.Sessions.Session.Configuration' : {
        'meta_info' : _MetaInfoClass('Vpdn.Sessions.Session.Configuration',
            False, 
            [
            _MetaInfoClassMember('dsl-line-forwarding', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if DSL line info forwarding is enabled
                ''',
                'dsl_line_forwarding',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('l2tp-busy-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                L2TP busy timeout in seconds
                ''',
                'l2tp_busy_timeout',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('tos', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TOS setting value
                ''',
                'tos',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('tos-mode', REFERENCE_ENUM_CLASS, 'TosModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'TosModeEnum', 
                [], [], 
                '''                TOS mode
                ''',
                'tos_mode',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('vpn-id', REFERENCE_CLASS, 'VpnId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'Vpdn.Sessions.Session.Configuration.VpnId', 
                [], [], 
                '''                VPN ID
                ''',
                'vpn_id',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-oper',
            'configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper'
        ),
    },
    'Vpdn.Sessions.Session' : {
        'meta_info' : _MetaInfoClass('Vpdn.Sessions.Session',
            False, 
            [
            _MetaInfoClassMember('session-label', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Session label
                ''',
                'session_label',
                'Cisco-IOS-XR-tunnel-vpdn-oper', True),
            _MetaInfoClassMember('configuration', REFERENCE_CLASS, 'Configuration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'Vpdn.Sessions.Session.Configuration', 
                [], [], 
                '''                Configuration data
                ''',
                'configuration',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('l2tp', REFERENCE_CLASS, 'L2Tp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'Vpdn.Sessions.Session.L2Tp', 
                [], [], 
                '''                L2TP data
                ''',
                'l2tp',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('parent-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Parent interface name
                ''',
                'parent_interface_name',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'Vpdn.Sessions.Session.Session_', 
                [], [], 
                '''                Session data
                ''',
                'session',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('setup-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time to setup session in sec:msec
                ''',
                'setup_time',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('subscriber', REFERENCE_CLASS, 'Subscriber' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'Vpdn.Sessions.Session.Subscriber', 
                [], [], 
                '''                Subscriber data
                ''',
                'subscriber',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-oper',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper'
        ),
    },
    'Vpdn.Sessions' : {
        'meta_info' : _MetaInfoClass('Vpdn.Sessions',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'Vpdn.Sessions.Session', 
                [], [], 
                '''                 VPDN session information
                ''',
                'session',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-oper',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper'
        ),
    },
    'Vpdn.TunnelDestinations.TunnelDestination' : {
        'meta_info' : _MetaInfoClass('Vpdn.TunnelDestinations.TunnelDestination',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('connects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of tunnels connected
                ''',
                'connects',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('disconnects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of tunnels disconnected
                ''',
                'disconnects',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('load', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current load on LNS
                ''',
                'load',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('retry', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Retries
                ''',
                'retry',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'LsgStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'LsgStatusEnum', 
                [], [], 
                '''                Status of LNS
                ''',
                'status',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('status-change-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds since last status change
                ''',
                'status_change_time',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('vrf-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name_xr',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-oper',
            'tunnel-destination',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper'
        ),
    },
    'Vpdn.TunnelDestinations' : {
        'meta_info' : _MetaInfoClass('Vpdn.TunnelDestinations',
            False, 
            [
            _MetaInfoClassMember('tunnel-destination', REFERENCE_LIST, 'TunnelDestination' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'Vpdn.TunnelDestinations.TunnelDestination', 
                [], [], 
                '''                VPDN tunnel destination information
                ''',
                'tunnel_destination',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-oper',
            'tunnel-destinations',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper'
        ),
    },
    'Vpdn.VpdnMirroring.QadSendStats' : {
        'meta_info' : _MetaInfoClass('Vpdn.VpdnMirroring.QadSendStats',
            False, 
            [
            _MetaInfoClassMember('acks-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                acks failed
                ''',
                'acks_failed',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('acks-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                acks sent
                ''',
                'acks_sent',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                msgs sent
                ''',
                'msgs_sent',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('no-partner', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                no partner
                ''',
                'no_partner',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('pending-acks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pending acks
                ''',
                'pending_acks',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-ack-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qad ack count
                ''',
                'qad_ack_count',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-frag-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qad frag count
                ''',
                'qad_frag_count',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-last-seq-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qad last seq number
                ''',
                'qad_last_seq_number',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-rx-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qad rx count
                ''',
                'qad_rx_count',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-rx-first-seq-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qad rx first seq number
                ''',
                'qad_rx_first_seq_number',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-rx-list-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qad rx list count
                ''',
                'qad_rx_list_count',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-rx-list-q-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qad rx list q size
                ''',
                'qad_rx_list_q_size',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qad timeouts
                ''',
                'qad_timeouts',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-unknown-acks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qad unknown acks
                ''',
                'qad_unknown_acks',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('resumes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                resumes
                ''',
                'resumes',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('sends-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                sends failed
                ''',
                'sends_failed',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('sends-fragment', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                sends fragment
                ''',
                'sends_fragment',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('suspends', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                suspends
                ''',
                'suspends',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                timeouts
                ''',
                'timeouts',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-oper',
            'qad-send-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper'
        ),
    },
    'Vpdn.VpdnMirroring.QadRecvStats' : {
        'meta_info' : _MetaInfoClass('Vpdn.VpdnMirroring.QadRecvStats',
            False, 
            [
            _MetaInfoClassMember('acks-recvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                acks recvd
                ''',
                'acks_recvd',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('init-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                init drops
                ''',
                'init_drops',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('msg-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                msg drops
                ''',
                'msg_drops',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('msgs-recvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                msgs recvd
                ''',
                'msgs_recvd',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('ooo-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ooo drops
                ''',
                'ooo_drops',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('recvd-acks-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                recvd acks failed
                ''',
                'recvd_acks_failed',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('stale-msgs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                stale msgs
                ''',
                'stale_msgs',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-oper',
            'qad-recv-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper'
        ),
    },
    'Vpdn.VpdnMirroring.QadSendStatsLastClear' : {
        'meta_info' : _MetaInfoClass('Vpdn.VpdnMirroring.QadSendStatsLastClear',
            False, 
            [
            _MetaInfoClassMember('acks-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                acks failed
                ''',
                'acks_failed',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('acks-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                acks sent
                ''',
                'acks_sent',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                msgs sent
                ''',
                'msgs_sent',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('no-partner', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                no partner
                ''',
                'no_partner',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('pending-acks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pending acks
                ''',
                'pending_acks',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-ack-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qad ack count
                ''',
                'qad_ack_count',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-frag-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qad frag count
                ''',
                'qad_frag_count',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-last-seq-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qad last seq number
                ''',
                'qad_last_seq_number',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-rx-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qad rx count
                ''',
                'qad_rx_count',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-rx-first-seq-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qad rx first seq number
                ''',
                'qad_rx_first_seq_number',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-rx-list-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qad rx list count
                ''',
                'qad_rx_list_count',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-rx-list-q-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qad rx list q size
                ''',
                'qad_rx_list_q_size',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qad timeouts
                ''',
                'qad_timeouts',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-unknown-acks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qad unknown acks
                ''',
                'qad_unknown_acks',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('resumes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                resumes
                ''',
                'resumes',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('sends-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                sends failed
                ''',
                'sends_failed',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('sends-fragment', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                sends fragment
                ''',
                'sends_fragment',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('suspends', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                suspends
                ''',
                'suspends',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                timeouts
                ''',
                'timeouts',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-oper',
            'qad-send-stats-last-clear',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper'
        ),
    },
    'Vpdn.VpdnMirroring.QadRecvStatsLastClear' : {
        'meta_info' : _MetaInfoClass('Vpdn.VpdnMirroring.QadRecvStatsLastClear',
            False, 
            [
            _MetaInfoClassMember('acks-recvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                acks recvd
                ''',
                'acks_recvd',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('init-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                init drops
                ''',
                'init_drops',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('msg-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                msg drops
                ''',
                'msg_drops',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('msgs-recvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                msgs recvd
                ''',
                'msgs_recvd',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('ooo-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ooo drops
                ''',
                'ooo_drops',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('recvd-acks-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                recvd acks failed
                ''',
                'recvd_acks_failed',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('stale-msgs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                stale msgs
                ''',
                'stale_msgs',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-oper',
            'qad-recv-stats-last-clear',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper'
        ),
    },
    'Vpdn.VpdnMirroring' : {
        'meta_info' : _MetaInfoClass('Vpdn.VpdnMirroring',
            False, 
            [
            _MetaInfoClassMember('alloc-cnt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                alloc cnt
                ''',
                'alloc_cnt',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('alloc-err-cnt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                alloc err cnt
                ''',
                'alloc_err_cnt',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-recv-stats', REFERENCE_CLASS, 'QadRecvStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'Vpdn.VpdnMirroring.QadRecvStats', 
                [], [], 
                '''                qad recv stats
                ''',
                'qad_recv_stats',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-recv-stats-last-clear', REFERENCE_CLASS, 'QadRecvStatsLastClear' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'Vpdn.VpdnMirroring.QadRecvStatsLastClear', 
                [], [], 
                '''                qad recv stats last clear
                ''',
                'qad_recv_stats_last_clear',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-send-stats', REFERENCE_CLASS, 'QadSendStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'Vpdn.VpdnMirroring.QadSendStats', 
                [], [], 
                '''                qad send stats
                ''',
                'qad_send_stats',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('qad-send-stats-last-clear', REFERENCE_CLASS, 'QadSendStatsLastClear' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'Vpdn.VpdnMirroring.QadSendStatsLastClear', 
                [], [], 
                '''                qad send stats last clear
                ''',
                'qad_send_stats_last_clear',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('sso-batch-err-cnt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                sso batch err cnt
                ''',
                'sso_batch_err_cnt',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('sso-err-cnt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                sso err cnt
                ''',
                'sso_err_cnt',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('sync-not-conn-cnt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                sync not conn cnt
                ''',
                'sync_not_conn_cnt',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-oper',
            'vpdn-mirroring',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper'
        ),
    },
    'Vpdn.VpdnRedundancy' : {
        'meta_info' : _MetaInfoClass('Vpdn.VpdnRedundancy',
            False, 
            [
            _MetaInfoClassMember('abort-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                abort time
                ''',
                'abort_time',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('finish-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                finish time
                ''',
                'finish_time',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('session-synced', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                session synced
                ''',
                'session_synced',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('session-total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                session total
                ''',
                'session_total',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                start time
                ''',
                'start_time',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'VpdnStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'VpdnStateEnum', 
                [], [], 
                '''                state
                ''',
                'state',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-oper',
            'vpdn-redundancy',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper'
        ),
    },
    'Vpdn.HistoryFailures.HistoryFailure' : {
        'meta_info' : _MetaInfoClass('Vpdn.HistoryFailures.HistoryFailure',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                NAS IP address
                ''',
                'destination_address',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('error-repeat-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Error repeat count
                ''',
                'error_repeat_count',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('event-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Event logged time in Ex: Wed Aug  3 10:28:30
                2011
                ''',
                'event_time',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('failure-type', REFERENCE_ENUM_CLASS, 'VpdnFailcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'VpdnFailcodeEnum', 
                [], [], 
                '''                Failure type
                ''',
                'failure_type',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('home-gateway', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Home gateway
                ''',
                'home_gateway',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('local-client-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local client ID
                ''',
                'local_client_id',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('mid', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VPDN user session ID
                ''',
                'mid',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('nas', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Network access server
                ''',
                'nas',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('remote-client-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remote client ID
                ''',
                'remote_client_id',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('remote-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Remote name
                ''',
                'remote_name',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source IP address
                ''',
                'source_address',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('username', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Username
                ''',
                'username',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('username-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Authentication username
                ''',
                'username_xr',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-oper',
            'history-failure',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper'
        ),
    },
    'Vpdn.HistoryFailures' : {
        'meta_info' : _MetaInfoClass('Vpdn.HistoryFailures',
            False, 
            [
            _MetaInfoClassMember('history-failure', REFERENCE_LIST, 'HistoryFailure' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'Vpdn.HistoryFailures.HistoryFailure', 
                [], [], 
                '''                VPDN history failure information
                ''',
                'history_failure',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-oper',
            'history-failures',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper'
        ),
    },
    'Vpdn' : {
        'meta_info' : _MetaInfoClass('Vpdn',
            False, 
            [
            _MetaInfoClassMember('history-failures', REFERENCE_CLASS, 'HistoryFailures' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'Vpdn.HistoryFailures', 
                [], [], 
                '''                VPDN history failure list
                ''',
                'history_failures',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'Vpdn.Sessions', 
                [], [], 
                '''                VPDN session list
                ''',
                'sessions',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('tunnel-destinations', REFERENCE_CLASS, 'TunnelDestinations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'Vpdn.TunnelDestinations', 
                [], [], 
                '''                VPDN tunnel Destinations
                ''',
                'tunnel_destinations',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('vpdn-mirroring', REFERENCE_CLASS, 'VpdnMirroring' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'Vpdn.VpdnMirroring', 
                [], [], 
                '''                VPDN Mirroring Statistics
                ''',
                'vpdn_mirroring',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            _MetaInfoClassMember('vpdn-redundancy', REFERENCE_CLASS, 'VpdnRedundancy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'Vpdn.VpdnRedundancy', 
                [], [], 
                '''                Show VPDN Redundancy information
                ''',
                'vpdn_redundancy',
                'Cisco-IOS-XR-tunnel-vpdn-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-oper',
            'vpdn',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper'
        ),
    },
}
_meta_table['Vpdn.Sessions.Session.Configuration.VpnId']['meta_info'].parent =_meta_table['Vpdn.Sessions.Session.Configuration']['meta_info']
_meta_table['Vpdn.Sessions.Session.Session_']['meta_info'].parent =_meta_table['Vpdn.Sessions.Session']['meta_info']
_meta_table['Vpdn.Sessions.Session.L2Tp']['meta_info'].parent =_meta_table['Vpdn.Sessions.Session']['meta_info']
_meta_table['Vpdn.Sessions.Session.Subscriber']['meta_info'].parent =_meta_table['Vpdn.Sessions.Session']['meta_info']
_meta_table['Vpdn.Sessions.Session.Configuration']['meta_info'].parent =_meta_table['Vpdn.Sessions.Session']['meta_info']
_meta_table['Vpdn.Sessions.Session']['meta_info'].parent =_meta_table['Vpdn.Sessions']['meta_info']
_meta_table['Vpdn.TunnelDestinations.TunnelDestination']['meta_info'].parent =_meta_table['Vpdn.TunnelDestinations']['meta_info']
_meta_table['Vpdn.VpdnMirroring.QadSendStats']['meta_info'].parent =_meta_table['Vpdn.VpdnMirroring']['meta_info']
_meta_table['Vpdn.VpdnMirroring.QadRecvStats']['meta_info'].parent =_meta_table['Vpdn.VpdnMirroring']['meta_info']
_meta_table['Vpdn.VpdnMirroring.QadSendStatsLastClear']['meta_info'].parent =_meta_table['Vpdn.VpdnMirroring']['meta_info']
_meta_table['Vpdn.VpdnMirroring.QadRecvStatsLastClear']['meta_info'].parent =_meta_table['Vpdn.VpdnMirroring']['meta_info']
_meta_table['Vpdn.HistoryFailures.HistoryFailure']['meta_info'].parent =_meta_table['Vpdn.HistoryFailures']['meta_info']
_meta_table['Vpdn.Sessions']['meta_info'].parent =_meta_table['Vpdn']['meta_info']
_meta_table['Vpdn.TunnelDestinations']['meta_info'].parent =_meta_table['Vpdn']['meta_info']
_meta_table['Vpdn.VpdnMirroring']['meta_info'].parent =_meta_table['Vpdn']['meta_info']
_meta_table['Vpdn.VpdnRedundancy']['meta_info'].parent =_meta_table['Vpdn']['meta_info']
_meta_table['Vpdn.HistoryFailures']['meta_info'].parent =_meta_table['Vpdn']['meta_info']
