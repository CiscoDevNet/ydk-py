


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'TcpAddressFamilyEnum' : _MetaInfoEnum('TcpAddressFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-ip-tcp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper']),
    'MessageTypeIcmpEnum' : _MetaInfoEnum('MessageTypeIcmpEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper',
        {
            'echo-reply':'echo_reply',
            'destination-unreachable':'destination_unreachable',
            'source-quench':'source_quench',
            'redirect':'redirect',
            'alternate-host-address':'alternate_host_address',
            'echo':'echo',
            'router-advertisement':'router_advertisement',
            'router-selection':'router_selection',
            'time-exceeded':'time_exceeded',
            'parameter-problem':'parameter_problem',
            'time-stamp':'time_stamp',
            'time-stamp-reply':'time_stamp_reply',
            'information-request':'information_request',
            'information-reply':'information_reply',
            'address-mask-request':'address_mask_request',
            'address-mask-reply':'address_mask_reply',
            'trace-route':'trace_route',
            'datagram-conversion-error':'datagram_conversion_error',
            'mobile-host-redirect':'mobile_host_redirect',
            'where-are-you':'where_are_you',
            'iam-here':'iam_here',
            'mobile-registration-request':'mobile_registration_request',
            'mobile-registration-reply':'mobile_registration_reply',
            'domain-name-request':'domain_name_request',
        }, 'Cisco-IOS-XR-ip-tcp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper']),
    'PakPrioEnum' : _MetaInfoEnum('PakPrioEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper',
        {
            'unspecified-packet':'unspecified_packet',
            'normal-packet':'normal_packet',
            'medium-packet':'medium_packet',
            'high-packet':'high_packet',
            'crucial-packet':'crucial_packet',
        }, 'Cisco-IOS-XR-ip-tcp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper']),
    'TcpConnStateEnum' : _MetaInfoEnum('TcpConnStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper',
        {
            'closed':'closed',
            'listen':'listen',
            'syn-sent':'syn_sent',
            'syn-received':'syn_received',
            'established':'established',
            'close-wait':'close_wait',
            'fin-wait1':'fin_wait1',
            'closing':'closing',
            'last-ack':'last_ack',
            'fin-wait2':'fin_wait2',
            'time-wait':'time_wait',
        }, 'Cisco-IOS-XR-ip-tcp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper']),
    'MessageTypeIcmpEnum' : _MetaInfoEnum('MessageTypeIcmpEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper',
        {
            'echo-reply':'echo_reply',
            'destination-unreachable':'destination_unreachable',
            'source-quench':'source_quench',
            'redirect':'redirect',
            'alternate-host-address':'alternate_host_address',
            'echo':'echo',
            'router-advertisement':'router_advertisement',
            'router-selection':'router_selection',
            'time-exceeded':'time_exceeded',
            'parameter-problem':'parameter_problem',
            'time-stamp':'time_stamp',
            'time-stamp-reply':'time_stamp_reply',
            'information-request':'information_request',
            'information-reply':'information_reply',
            'address-mask-request':'address_mask_request',
            'address-mask-reply':'address_mask_reply',
            'trace-route':'trace_route',
            'datagram-conversion-error':'datagram_conversion_error',
            'mobile-host-redirect':'mobile_host_redirect',
            'where-are-you':'where_are_you',
            'iam-here':'iam_here',
            'mobile-registration-request':'mobile_registration_request',
            'mobile-registration-reply':'mobile_registration_reply',
            'domain-name-request':'domain_name_request',
        }, 'Cisco-IOS-XR-ip-tcp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper']),
    'NsrDownReasonEnum' : _MetaInfoEnum('NsrDownReasonEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper',
        {
            'none':'none',
            'init-sync-aborted':'init_sync_aborted',
            'client-disabled':'client_disabled',
            'client-disconnect':'client_disconnect',
            'tcp-disconnect':'tcp_disconnect',
            'failover':'failover',
            'nsr-clear':'nsr_clear',
            'internal-error':'internal_error',
            'retransmit-threshold-exceed':'retransmit_threshold_exceed',
            'init-sync-failure-thresh-exceeded':'init_sync_failure_thresh_exceeded',
            'audit-timeout':'audit_timeout',
            'audit-failed':'audit_failed',
            'standby-sscb-deleted':'standby_sscb_deleted',
            'standby-session-close':'standby_session_close',
            'standby-rxpath-frozen':'standby_rxpath_frozen',
            'partner-deleted':'partner_deleted',
        }, 'Cisco-IOS-XR-ip-tcp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper']),
    'MessageTypeIgmpEnum' : _MetaInfoEnum('MessageTypeIgmpEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper',
        {
            'membership-query':'membership_query',
            'v1-membership-report':'v1_membership_report',
            'dvmrp':'dvmrp',
            'pi-mv1':'pi_mv1',
            'cisco-trace-messages':'cisco_trace_messages',
            'v2-membership-report':'v2_membership_report',
            'v2-leave-group':'v2_leave_group',
            'multicast-traceroute-response':'multicast_traceroute_response',
            'multicast-traceroute':'multicast_traceroute',
            'v3-membership-report':'v3_membership_report',
            'multicast-router-advertisement':'multicast_router_advertisement',
            'multicast-router-solicitation':'multicast_router_solicitation',
            'multicast-router-termination':'multicast_router_termination',
        }, 'Cisco-IOS-XR-ip-tcp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper']),
    'MessageTypeIcmpv6Enum' : _MetaInfoEnum('MessageTypeIcmpv6Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper',
        {
            'destination-unreachable':'destination_unreachable',
            'packet-too-big':'packet_too_big',
            'time-exceeded':'time_exceeded',
            'parameter-problem':'parameter_problem',
            'echo-request':'echo_request',
            'echo-reply':'echo_reply',
            'multicast-listener-query':'multicast_listener_query',
            'multicast-listener-report':'multicast_listener_report',
            'multicast-listener-done':'multicast_listener_done',
            'router-solicitation':'router_solicitation',
            'router-advertisement':'router_advertisement',
            'neighbor-solicitation':'neighbor_solicitation',
            'neighbor-advertisement':'neighbor_advertisement',
            'redirect-message':'redirect_message',
            'router-renumbering':'router_renumbering',
            'node-information-query':'node_information_query',
            'node-information-reply':'node_information_reply',
            'inverse-neighbor-discovery-solicitaion':'inverse_neighbor_discovery_solicitaion',
            'inverse-neighbor-discover-advertisement':'inverse_neighbor_discover_advertisement',
            'v2-multicast-listener-report':'v2_multicast_listener_report',
            'home-agent-address-discovery-request':'home_agent_address_discovery_request',
            'home-agent-address-discovery-reply':'home_agent_address_discovery_reply',
            'mobile-prefix-solicitation':'mobile_prefix_solicitation',
            'mobile-prefix-advertisement':'mobile_prefix_advertisement',
            'certification-path-solicitation-message':'certification_path_solicitation_message',
            'certification-path-advertisement-message':'certification_path_advertisement_message',
            'experimental-mobility-protocols':'experimental_mobility_protocols',
            'multicast-router-advertisement':'multicast_router_advertisement',
            'multicast-router-solicitation':'multicast_router_solicitation',
            'multicast-router-termination':'multicast_router_termination',
            'fmipv6-messages':'fmipv6_messages',
        }, 'Cisco-IOS-XR-ip-tcp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper']),
    'NsrStatusEnum' : _MetaInfoEnum('NsrStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper',
        {
            'down':'down',
            'up':'up',
            'na':'na',
        }, 'Cisco-IOS-XR-ip-tcp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper']),
    'PacketEnum' : _MetaInfoEnum('PacketEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper',
        {
            'icmp':'icmp',
            'icm-pv6':'icm_pv6',
            'igmp':'igmp',
            'unknown':'unknown',
        }, 'Cisco-IOS-XR-ip-tcp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper']),
    'TcpTimerEnum' : _MetaInfoEnum('TcpTimerEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper',
        {
            'retransmission-timer':'retransmission_timer',
            'window-probe-timer':'window_probe_timer',
            'timewait-state-timer':'timewait_state_timer',
            'ack-hold-timer':'ack_hold_timer',
            'keep-alive-timer':'keep_alive_timer',
            'pmtu-ager-timer':'pmtu_ager_timer',
            'retransmission-giveup-timer':'retransmission_giveup_timer',
            'throttle-timer':'throttle_timer',
        }, 'Cisco-IOS-XR-ip-tcp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper']),
    'AddrFamilyEnum' : _MetaInfoEnum('AddrFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper',
        {
            'internetwork':'internetwork',
            'ip-version6':'ip_version6',
        }, 'Cisco-IOS-XR-ip-tcp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper']),
    'ShowEnum' : _MetaInfoEnum('ShowEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper',
        {
            'all':'all',
            'static-policy':'static_policy',
            'interface-filter':'interface_filter',
            'packet-filter':'packet_filter',
        }, 'Cisco-IOS-XR-ip-tcp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper']),
    'MessageTypeIcmpv6Enum' : _MetaInfoEnum('MessageTypeIcmpv6Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper',
        {
            'destination-unreachable':'destination_unreachable',
            'packet-too-big':'packet_too_big',
            'time-exceeded':'time_exceeded',
            'parameter-problem':'parameter_problem',
            'echo-request':'echo_request',
            'echo-reply':'echo_reply',
            'multicast-listener-query':'multicast_listener_query',
            'multicast-listener-report':'multicast_listener_report',
            'multicast-listener-done':'multicast_listener_done',
            'router-solicitation':'router_solicitation',
            'router-advertisement':'router_advertisement',
            'neighbor-solicitation':'neighbor_solicitation',
            'neighbor-advertisement':'neighbor_advertisement',
            'redirect-message':'redirect_message',
            'router-renumbering':'router_renumbering',
            'node-information-query':'node_information_query',
            'node-information-reply':'node_information_reply',
            'inverse-neighbor-discovery-solicitaion':'inverse_neighbor_discovery_solicitaion',
            'inverse-neighbor-discover-advertisement':'inverse_neighbor_discover_advertisement',
            'v2-multicast-listener-report':'v2_multicast_listener_report',
            'home-agent-address-discovery-request':'home_agent_address_discovery_request',
            'home-agent-address-discovery-reply':'home_agent_address_discovery_reply',
            'mobile-prefix-solicitation':'mobile_prefix_solicitation',
            'mobile-prefix-advertisement':'mobile_prefix_advertisement',
            'certification-path-solicitation-message':'certification_path_solicitation_message',
            'certification-path-advertisement-message':'certification_path_advertisement_message',
            'experimental-mobility-protocols':'experimental_mobility_protocols',
            'multicast-router-advertisement':'multicast_router_advertisement',
            'multicast-router-solicitation':'multicast_router_solicitation',
            'multicast-router-termination':'multicast_router_termination',
            'fmipv6-messages':'fmipv6_messages',
        }, 'Cisco-IOS-XR-ip-tcp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper']),
    'MessageTypeIgmpEnum' : _MetaInfoEnum('MessageTypeIgmpEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper',
        {
            'membership-query':'membership_query',
            'v1-membership-report':'v1_membership_report',
            'dvmrp':'dvmrp',
            'pi-mv1':'pi_mv1',
            'cisco-trace-messages':'cisco_trace_messages',
            'v2-membership-report':'v2_membership_report',
            'v2-leave-group':'v2_leave_group',
            'multicast-traceroute-response':'multicast_traceroute_response',
            'multicast-traceroute':'multicast_traceroute',
            'v3-membership-report':'v3_membership_report',
            'multicast-router-advertisement':'multicast_router_advertisement',
            'multicast-router-solicitation':'multicast_router_solicitation',
            'multicast-router-termination':'multicast_router_termination',
        }, 'Cisco-IOS-XR-ip-tcp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper']),
    'TcpConnection.Nodes.Node.Statistics.Clients.Client' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.Statistics.Clients.Client',
            False, 
            [
            _MetaInfoClassMember('client-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Displaying client's aggregated statistics
                ''',
                'client_id',
                'Cisco-IOS-XR-ip-tcp-oper', True),
            _MetaInfoClassMember('client-jid', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Job ID of the transport client
                ''',
                'client_jid',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('client-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 21)], [], 
                '''                Transport client name
                ''',
                'client_name',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv4-received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total IPv4 packets received from client
                ''',
                'ipv4_received_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv4-sent-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total IPv4 packets sent to client
                ''',
                'ipv4_sent_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv6-received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total IPv6 packets received from app
                ''',
                'ipv6_received_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv6-sent-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total IPv6 packets sent to app
                ''',
                'ipv6_sent_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'client',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.Statistics.Clients' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.Statistics.Clients',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_LIST, 'Client' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.Statistics.Clients.Client', 
                [], [], 
                '''                Describing Client ID
                ''',
                'client',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'clients',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.ReadIoCounts' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.ReadIoCounts',
            False, 
            [
            _MetaInfoClassMember('arm-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                How many times socket was armed by application
                ''',
                'arm_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('autoarm-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                How many times socket was auto-armed by TCP
                ''',
                'autoarm_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('io-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of I/O operations done by application
                ''',
                'io_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('unarm-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                How many times socket was unarmed by application
                ''',
                'unarm_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'read-io-counts',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.WriteIoCounts' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.WriteIoCounts',
            False, 
            [
            _MetaInfoClassMember('arm-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                How many times socket was armed by application
                ''',
                'arm_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('autoarm-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                How many times socket was auto-armed by TCP
                ''',
                'autoarm_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('io-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of I/O operations done by application
                ''',
                'io_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('unarm-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                How many times socket was unarmed by application
                ''',
                'unarm_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'write-io-counts',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats',
            False, 
            [
            _MetaInfoClassMember('async-session', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag of async session
                ''',
                'async_session',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('control-read-error-num', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failed control read from XIPC
                ''',
                'control_read_error_num',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=5),
            _MetaInfoClassMember('control-read-success-num', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful control read to XIPC
                ''',
                'control_read_success_num',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=5),
            _MetaInfoClassMember('control-write-error-num', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failed control write to XIPC
                ''',
                'control_write_error_num',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=5),
            _MetaInfoClassMember('control-write-success-num', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful control write to XIPC
                ''',
                'control_write_success_num',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=5),
            _MetaInfoClassMember('data-read-byte', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of bytes data has been read
                ''',
                'data_read_byte',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=2),
            _MetaInfoClassMember('data-read-error-num', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failed data read from XIPC
                ''',
                'data_read_error_num',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=2),
            _MetaInfoClassMember('data-read-success-num', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful data read from XIPC
                ''',
                'data_read_success_num',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=2),
            _MetaInfoClassMember('data-write-byte', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of bytes data has been written
                ''',
                'data_write_byte',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=2),
            _MetaInfoClassMember('data-write-error-num', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failed data write to XIPC
                ''',
                'data_write_error_num',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=2),
            _MetaInfoClassMember('data-write-success-num', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful data write to XIPC
                ''',
                'data_write_success_num',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'async-session-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Displaying statistics associated with a
                particular PCB
                ''',
                'id',
                'Cisco-IOS-XR-ip-tcp-oper', True),
            _MetaInfoClassMember('async-session-stats', REFERENCE_CLASS, 'AsyncSessionStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats', 
                [], [], 
                '''                Statistics of Async TCP Sessions
                ''',
                'async_session_stats',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-paw-socket', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PAW or non-PAW socket?
                ''',
                'is_paw_socket',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets received from network
                ''',
                'packets_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets received from application
                ''',
                'packets_sent',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('pcb', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PCB Address
                ''',
                'pcb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('read-io-counts', REFERENCE_CLASS, 'ReadIoCounts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.ReadIoCounts', 
                [], [], 
                '''                Read  I/O counts
                ''',
                'read_io_counts',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('read-io-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which receive buffer was last read from
                ''',
                'read_io_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('receive-queue-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received packets failed to be queued to
                application
                ''',
                'receive_queue_failed',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('received-packets-queued', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets queued to application
                ''',
                'received_packets_queued',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('segment-instruction-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Segment Instruction received from partner node
                ''',
                'segment_instruction_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('send-packets-queued', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets queued to v4/v6 IO
                ''',
                'send_packets_queued',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('send-packets-queued-net-io', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets queued to NetIO
                ''',
                'send_packets_queued_net_io',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('send-queue-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets failed to be queued to v4/v6 IO
                ''',
                'send_queue_failed',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('send-queue-net-io-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets failed to be queued to NetIO
                ''',
                'send_queue_net_io_failed',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('send-window-shrink-ignored', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times send window shrinkage by peer was
                ignored
                ''',
                'send_window_shrink_ignored',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF Id
                ''',
                'vrf_id',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('write-io-counts', REFERENCE_CLASS, 'WriteIoCounts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.WriteIoCounts', 
                [], [], 
                '''                Write I/O counts
                ''',
                'write_io_counts',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('write-io-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which send buffer was last written to
                ''',
                'write_io_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('xipc-pulse-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                XIPC pulses received from application
                ''',
                'xipc_pulse_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'pcb',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.Statistics.Pcbs' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.Statistics.Pcbs',
            False, 
            [
            _MetaInfoClassMember('pcb', REFERENCE_LIST, 'Pcb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb', 
                [], [], 
                '''                Protocol Control Block ID
                ''',
                'pcb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'pcbs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.Statistics.Summary' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.Statistics.Summary',
            False, 
            [
            _MetaInfoClassMember('ack-only-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Ack only packets sent (incl. delay)
                ''',
                'ack_only_packets_sent',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ack-packets-for-unsent-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Ack packets for unsent data
                ''',
                'ack_packets_for_unsent_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ack-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Ack packets received
                ''',
                'ack_packets_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ackbytes-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bytes acked by ack packets
                ''',
                'ackbytes_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('after-window-bytes-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                After-window bytes received
                ''',
                'after_window_bytes_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('after-window-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                After-window packets received
                ''',
                'after_window_packets_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('bad-checksum-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets received with bad checksum
                ''',
                'bad_checksum_packets_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('bytes-retransmitted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Data bytes retransmitted
                ''',
                'bytes_retransmitted',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('connection-rate-limited', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Connections rate-limited
                ''',
                'connection_rate_limited',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('connections-accepted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Connection requests accepted
                ''',
                'connections_accepted',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('connections-closed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                connections closed (incl. drops)
                ''',
                'connections_closed',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('connections-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                connections dropped
                ''',
                'connections_dropped',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('connections-established', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Connections established
                ''',
                'connections_established',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('connections-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Connections failed
                ''',
                'connections_failed',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('connections-forcibly-closed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Connections forcibly closed
                ''',
                'connections_forcibly_closed',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('connections-requested', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Connection requests sent
                ''',
                'connections_requested',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('control-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Control (SYN|FIN|RST) packets sent
                ''',
                'control_packets_sent',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-bytes-received-in-sequence', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Data bytes received in sequence
                ''',
                'data_bytes_received_in_sequence',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-bytes-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Data bytes sent
                ''',
                'data_bytes_sent',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-packets-received-in-sequence', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Data packets received in sequence
                ''',
                'data_packets_received_in_sequence',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-pakets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Data packets sent
                ''',
                'data_pakets_sent',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('delay-ack-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Delay ack packets sent
                ''',
                'delay_ack_packets_sent',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('duplicate-bytes-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duplicate bytes received
                ''',
                'duplicate_bytes_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('duplicate-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duplicate packets received
                ''',
                'duplicate_packets_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('duplicated-ack-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duplicate ack packets
                ''',
                'duplicated_ack_packets_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('embryonic-connection-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Embryonic connections dropped
                ''',
                'embryonic_connection_dropped',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('established-connections-reset', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Established connections reset
                ''',
                'established_connections_reset',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('high-water-mark-throttle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times high water mark throttle was on
                ''',
                'high_water_mark_throttle',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('iq-sock-aborts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of aborted socket-lib writes
                ''',
                'iq_sock_aborts',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('iq-sock-retries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of retried write attempts
                ''',
                'iq_sock_retries',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('iq-sock-writes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of write attempts from socket-lib into an
                IQ
                ''',
                'iq_sock_writes',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('keep-alive-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Connection drops due to keepalive timeouts
                ''',
                'keep_alive_dropped',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('keep-alive-probes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Keepalive probes sent
                ''',
                'keep_alive_probes',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('keep-alive-timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Keepalive timeouts
                ''',
                'keep_alive_timeouts',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('low-water-mark-throttle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times low water mark throttle was on
                ''',
                'low_water_mark_throttle',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('malformed-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets received with malformed header
                ''',
                'malformed_packets_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mss-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times MSS was decreased
                ''',
                'mss_down',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mss-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times MSS was increased
                ''',
                'mss_up',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('no-port-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets rcceived with no wild listener
                ''',
                'no_port_packets_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('no-throttle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times throttle mode was off
                ''',
                'no_throttle',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('num-open-sockets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Open sockets
                ''',
                'num_open_sockets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('out-of-order-bytes-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Out-of-order bytes received
                ''',
                'out_of_order_bytes_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('out-of-order-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Out-of-order packets received
                ''',
                'out_of_order_packets_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('packet-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packet allocation errors
                ''',
                'packet_failures',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('packets-received-after-close-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets received after close
                ''',
                'packets_received_after_close_packet',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('packets-retransmitted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Data packets retransmitted
                ''',
                'packets_retransmitted',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('partial-duplicate-ack-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets with partial dup data
                ''',
                'partial_duplicate_ack_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('partial-duplicate-bytes-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bytes with partial dup data
                ''',
                'partial_duplicate_bytes_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('paws-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Segments dropped due to PAWS
                ''',
                'paws_dropped',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('persist-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Segments dropped due to window probe
                ''',
                'persist_dropped',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('pulse-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Punt (down to ip) failures
                ''',
                'pulse_errors',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('reassembly-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets owned by TCP reassembly
                ''',
                'reassembly_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('received-auth-packets-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received packets dropped due to authentication
                failures
                ''',
                'received_auth_packets_dropped',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('received-packets-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received packets dropped due to general failures
                ''',
                'received_packets_dropped',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('received-packets-dropped-stale-c-hdr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received packets dropped due to stale cached
                header
                ''',
                'received_packets_dropped_stale_c_hdr',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('recovered-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets freed after starvation
                ''',
                'recovered_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('retransmit-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Connection drops during retransmit timeouts
                ''',
                'retransmit_dropped',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('retransmit-timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Retransmit timeouts (incl. data packets)
                ''',
                'retransmit_timeouts',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('rst-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RST packets sent
                ''',
                'rst_packets_sent',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('send-auth-packets-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total transmit packets dropped due to
                authentication failures
                ''',
                'send_auth_packets_dropped',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('send-packets-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total transmit packets dropped due to general
                failures
                ''',
                'send_packets_dropped',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('socket-layer-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets owned by the socket layer
                ''',
                'socket_layer_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('stalled-timer-tickle-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times a stalled tcp timer was tickled
                ''',
                'stalled_timer_tickle_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('stalled-timer-tickle-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last timestamp when a stalled tcp timer was
                tickled
                ''',
                'stalled_timer_tickle_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('syn-cache-aborted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SYN Cache entries aborted (no mem)
                ''',
                'syn_cache_aborted',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('syn-cache-added', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SYN Cache entries added
                ''',
                'syn_cache_added',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('syn-cache-bucket-oflow', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SYN Cache entries dropped due to bucket overflow
                ''',
                'syn_cache_bucket_oflow',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('syn-cache-completed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SYN Cache connections completed
                ''',
                'syn_cache_completed',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('syn-cache-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current number of SYN cache entries
                ''',
                'syn_cache_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('syn-cache-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SYN Cache entries dropped (no route/mem)
                ''',
                'syn_cache_dropped',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('syn-cache-duplicate-sy-ns', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SYN Cache duplicate SYNs received
                ''',
                'syn_cache_duplicate_sy_ns',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('syn-cache-overflow', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SYN Cache entries dropped due to overflow
                ''',
                'syn_cache_overflow',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('syn-cache-reset', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SYN Cache entries dropped due to RST
                ''',
                'syn_cache_reset',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('syn-cache-timed-out', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SYN Cache entries timed out
                ''',
                'syn_cache_timed_out',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('syn-cache-unreach', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SYN Cache entries dropped due to ICMP unreach
                ''',
                'syn_cache_unreach',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('synacl-match-pkts-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received packets dropped due to ACL DENY on SYN
                pkts
                ''',
                'synacl_match_pkts_dropped',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('too-short-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets received with too short size
                ''',
                'too_short_packets_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('total-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total packets received
                ''',
                'total_packets_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('total-pakets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total packets sent
                ''',
                'total_pakets_sent',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('truncated-write-iov', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Segments truncated due to insufficient Write I/O
                vectors
                ''',
                'truncated_write_iov',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('try-lock-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Segments dropped due to trylock fail
                ''',
                'try_lock_dropped',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('urgent-only-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Urgent only packets sent
                ''',
                'urgent_only_packets_sent',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('window-probe-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Window probe packets received
                ''',
                'window_probe_packets_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('window-probe-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Window probe packets sent
                ''',
                'window_probe_packets_sent',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('window-update-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Window update packets received
                ''',
                'window_update_packets_received',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('window-update-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Window update packets sent
                ''',
                'window_update_packets_sent',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.Statistics' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.Statistics',
            False, 
            [
            _MetaInfoClassMember('clients', REFERENCE_CLASS, 'Clients' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.Statistics.Clients', 
                [], [], 
                '''                Table listing clients
                ''',
                'clients',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('pcbs', REFERENCE_CLASS, 'Pcbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.Statistics.Pcbs', 
                [], [], 
                '''                Table listing the TCP connections for which
                statistics are provided
                ''',
                'pcbs',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.Statistics.Summary', 
                [], [], 
                '''                Summary statistics across all TCP connections
                ''',
                'summary',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.LocalAddress' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'AddrFamilyEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.ForeignAddress' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.ForeignAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'AddrFamilyEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'foreign-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Options' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Options',
            False, 
            [
            _MetaInfoClassMember('is-ip-sla', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IP SLA
                ''',
                'is_ip_sla',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-receive-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Receive filter enabled
                ''',
                'is_receive_filter',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'options',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.LptsFlags' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.LptsFlags',
            False, 
            [
            _MetaInfoClassMember('is-ignore-vrf-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ignore VRF Filter
                ''',
                'is_ignore_vrf_filter',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-local-address-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Sent drop packets
                ''',
                'is_local_address_ignore',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-pcb-bound', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PCB bound
                ''',
                'is_pcb_bound',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'lpts-flags',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.AcceptMask' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.AcceptMask',
            False, 
            [
            _MetaInfoClassMember('is-interface', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set interface
                ''',
                'is_interface',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-local-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set Local Address
                ''',
                'is_local_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-local-port', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set Local Port
                ''',
                'is_local_port',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-packet-type', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set packet type
                ''',
                'is_packet_type',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-remote-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set Remote address
                ''',
                'is_remote_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-remote-port', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set Remote Port
                ''',
                'is_remote_port',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'accept-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.PacketType' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.PacketType',
            False, 
            [
            _MetaInfoClassMember('icm-pv6-message-type', REFERENCE_ENUM_CLASS, 'MessageTypeIcmpv6Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'MessageTypeIcmpv6Enum', 
                [], [], 
                '''                ICMPv6 message type
                ''',
                'icm_pv6_message_type',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('icmp-message-type', REFERENCE_ENUM_CLASS, 'MessageTypeIcmpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'MessageTypeIcmpEnum', 
                [], [], 
                '''                ICMP message type
                ''',
                'icmp_message_type',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('igmp-message-type', REFERENCE_ENUM_CLASS, 'MessageTypeIgmpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'MessageTypeIgmpEnum', 
                [], [], 
                '''                IGMP message type
                ''',
                'igmp_message_type',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('message-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message type in number
                ''',
                'message_id',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'PacketEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'PacketEnum', 
                [], [], 
                '''                Type
                ''',
                'type',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'packet-type',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.RemoteAddress' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.RemoteAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'AddrFamilyEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'remote-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.LocalAddress' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'AddrFamilyEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter',
            False, 
            [
            _MetaInfoClassMember('flow-types-info', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                flow information
                ''',
                'flow_types_info',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.LocalAddress', 
                [], [], 
                '''                Local address
                ''',
                'local_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local address length
                ''',
                'local_length',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('packet-type', REFERENCE_CLASS, 'PacketType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.PacketType', 
                [], [], 
                '''                Protocol-specific packet type
                ''',
                'packet_type',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Priority
                ''',
                'priority',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('receive-local-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Receive Local port
                ''',
                'receive_local_port',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('receive-remote-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Receive Remote port
                ''',
                'receive_remote_port',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('remote-address', REFERENCE_CLASS, 'RemoteAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.RemoteAddress', 
                [], [], 
                '''                Remote address
                ''',
                'remote_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('remote-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remote address length
                ''',
                'remote_length',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Minimum TTL
                ''',
                'ttl',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb',
            False, 
            [
            _MetaInfoClassMember('accept-mask', REFERENCE_CLASS, 'AcceptMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.AcceptMask', 
                [], [], 
                '''                AcceptMask
                ''',
                'accept_mask',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('filter', REFERENCE_LIST, 'Filter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter', 
                [], [], 
                '''                Interface Filters
                ''',
                'filter',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('flow-types-info', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                flow information
                ''',
                'flow_types_info',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('lpts-flags', REFERENCE_CLASS, 'LptsFlags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.LptsFlags', 
                [], [], 
                '''                LPTS flags
                ''',
                'lpts_flags',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('options', REFERENCE_CLASS, 'Options' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Options', 
                [], [], 
                '''                Receive options
                ''',
                'options',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Minimum TTL
                ''',
                'ttl',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'lpts-pcb',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'AddrFamilyEnum', 
                [], [], 
                '''                Address Family
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('lpts-pcb', REFERENCE_CLASS, 'LptsPcb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb', 
                [], [], 
                '''                LPTS PCB information
                ''',
                'lpts_pcb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'common',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId',
            False, 
            [
            _MetaInfoClassMember('pcb-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Displaying inforamtion based on selected
                display type associatedwith a particular
                PCB
                ''',
                'pcb_id',
                'Cisco-IOS-XR-ip-tcp-oper', True),
            _MetaInfoClassMember('common', REFERENCE_CLASS, 'Common' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common', 
                [], [], 
                '''                Common PCB information
                ''',
                'common',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('foreign-address', REFERENCE_CLASS, 'ForeignAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.ForeignAddress', 
                [], [], 
                '''                Remote IP address
                ''',
                'foreign_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('foreign-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remote port
                ''',
                'foreign_port',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('l4-protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Layer 4 protocol
                ''',
                'l4_protocol',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.LocalAddress', 
                [], [], 
                '''                Local IP address
                ''',
                'local_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local port
                ''',
                'local_port',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'connection-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType',
            False, 
            [
            _MetaInfoClassMember('disp-type', REFERENCE_ENUM_CLASS, 'ShowEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'ShowEnum', 
                [], [], 
                '''                Specifying display type
                ''',
                'disp_type',
                'Cisco-IOS-XR-ip-tcp-oper', True),
            _MetaInfoClassMember('connection-id', REFERENCE_LIST, 'ConnectionId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId', 
                [], [], 
                '''                Describing connection ID
                ''',
                'connection_id',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'display-type',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes',
            False, 
            [
            _MetaInfoClassMember('display-type', REFERENCE_LIST, 'DisplayType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType', 
                [], [], 
                '''                Describing particular display type
                ''',
                'display_type',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'display-types',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.ExtendedInformation' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.ExtendedInformation',
            False, 
            [
            _MetaInfoClassMember('display-types', REFERENCE_CLASS, 'DisplayTypes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes', 
                [], [], 
                '''                Table listing display types
                ''',
                'display_types',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'extended-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.LocalAddress' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.DetailInformations.DetailInformation.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'TcpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpAddressFamilyEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ForeignAddress' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ForeignAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'TcpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpAddressFamilyEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'foreign-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketOptionFlags' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketOptionFlags',
            False, 
            [
            _MetaInfoClassMember('accept-connection', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Socket has had listen()
                ''',
                'accept_connection',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('broadcast', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Permit sending of broadcast msgs
                ''',
                'broadcast',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('debug', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Turn on debugging info recording
                ''',
                'debug',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('dont-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Just use interface addresses
                ''',
                'dont_route',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('keep-alive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Keep connections alive
                ''',
                'keep_alive',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('linger', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Linger on close if data present
                ''',
                'linger',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nonblocking-io', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Nonblocking socket I/O operation
                ''',
                'nonblocking_io',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('out-of-band-inline', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Leave received Out-of-band data inline
                ''',
                'out_of_band_inline',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('reuse-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow local address reuse
                ''',
                'reuse_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('reuse-port', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow local address & port reuse
                ''',
                'reuse_port',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('use-loopback', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Bypass hardware when possible
                ''',
                'use_loopback',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'socket-option-flags',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketStateFlags' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketStateFlags',
            False, 
            [
            _MetaInfoClassMember('async-io-notify', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Async i/o notify
                ''',
                'async_io_notify',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('block-close', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Close is blocked (i.e. socket is a replicated
                socket on a standby node
                ''',
                'block_close',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('block-receive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Socket is blocked for receive - while going
                through SSO initial sync
                ''',
                'block_receive',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('block-send', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Socket is blocked for send (if it is a
                replicated socket on a standby node)
                ''',
                'block_send',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('cant-receive-more', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Can't recv more data from peer
                ''',
                'cant_receive_more',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('cant-send-more', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Can't send more data to peer
                ''',
                'cant_send_more',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-confirming', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Deciding to accept connection req
                ''',
                'is_confirming',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-connected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Socket is connected to peer
                ''',
                'is_connected',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-connecting', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Connecting in progress
                ''',
                'is_connecting',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-detached', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PCB and socket are detached
                ''',
                'is_detached',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-disconnecting', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disconnecting in progress
                ''',
                'is_disconnecting',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-solock', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Mutex acquired by solock()
                ''',
                'is_solock',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('no-file-descriptor-reference', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                No file descriptor ref
                ''',
                'no_file_descriptor_reference',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('privileged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Privileged for broadcast, raw...
                ''',
                'privileged',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('received-at-mark', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                At mark on input
                ''',
                'received_at_mark',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'socket-state-flags',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FeatureFlags' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FeatureFlags',
            False, 
            [
            _MetaInfoClassMember('connection-keep-alive-timer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Keepalive timer is on?
                ''',
                'connection_keep_alive_timer',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('giveup-timer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Giveup timer is on?
                ''',
                'giveup_timer',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('md5', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MD5 option on?
                ''',
                'md5',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mss-cisco', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                tcp mss feature is on?
                ''',
                'mss_cisco',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nagle', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Nagle algorithm on?
                ''',
                'nagle',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('path-mtu-discovery', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Path MTU Discovery feature is on?
                ''',
                'path_mtu_discovery',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('selective-ack', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Selective ack on?
                ''',
                'selective_ack',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('timestamps', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Timestamps on?
                ''',
                'timestamps',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('window-scaling', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Window-scaling on?
                ''',
                'window_scaling',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'feature-flags',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.StateFlags' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.DetailInformations.DetailInformation.StateFlags',
            False, 
            [
            _MetaInfoClassMember('ack-needed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Send an ACK
                ''',
                'ack_needed',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('fin-sent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                FIN has been sent
                ''',
                'fin_sent',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('in-syn-cache', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Connection is in SYN cache
                ''',
                'in_syn_cache',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nagle-wait', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Nagle has delayed output
                ''',
                'nagle_wait',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('need-push', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Need to push data out
                ''',
                'need_push',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('path-mtu-ager', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Path MTU aging timer is running
                ''',
                'path_mtu_ager',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('probing', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Probing a closed window
                ''',
                'probing',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('pushed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A segment is pushed due to MSG_PUSH
                ''',
                'pushed',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'state-flags',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.RequestFlags' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.DetailInformations.DetailInformation.RequestFlags',
            False, 
            [
            _MetaInfoClassMember('connection-keep-alive-timer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Keepalive timer is on?
                ''',
                'connection_keep_alive_timer',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('giveup-timer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Giveup timer is on?
                ''',
                'giveup_timer',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('md5', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MD5 option on?
                ''',
                'md5',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mss-cisco', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                tcp mss feature is on?
                ''',
                'mss_cisco',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nagle', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Nagle algorithm on?
                ''',
                'nagle',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('path-mtu-discovery', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Path MTU Discovery feature is on?
                ''',
                'path_mtu_discovery',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('selective-ack', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Selective ack on?
                ''',
                'selective_ack',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('timestamps', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Timestamps on?
                ''',
                'timestamps',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('window-scaling', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Window-scaling on?
                ''',
                'window_scaling',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'request-flags',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ReceiveBufStateFlags' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ReceiveBufStateFlags',
            False, 
            [
            _MetaInfoClassMember('async-io', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Async I/O
                ''',
                'async_io',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('connect-wakeup', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Connect wakeup pending
                ''',
                'connect_wakeup',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('delayed-wakeup', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Want delayed wakeups
                ''',
                'delayed_wakeup',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('input-select', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Buffer is selected for INPUT
                ''',
                'input_select',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('io-timer-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Read/write timer set
                ''',
                'io_timer_set',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('locked', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Lock on data queue (so_rcv only)
                ''',
                'locked',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('not-interruptible', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Not interruptible
                ''',
                'not_interruptible',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('out-of-band-select', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Buffer is selected for OBAND
                ''',
                'out_of_band_select',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('output-select', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Buffer is selected for OUTPUT
                ''',
                'output_select',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('waiting-for-data', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Someone is waiting for data/space
                ''',
                'waiting_for_data',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('waiting-for-lock', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Someone is waiting to lock
                ''',
                'waiting_for_lock',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('wakeup', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Read/write wakeup pending
                ''',
                'wakeup',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'receive-buf-state-flags',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendBufStateFlags' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendBufStateFlags',
            False, 
            [
            _MetaInfoClassMember('async-io', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Async I/O
                ''',
                'async_io',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('connect-wakeup', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Connect wakeup pending
                ''',
                'connect_wakeup',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('delayed-wakeup', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Want delayed wakeups
                ''',
                'delayed_wakeup',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('input-select', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Buffer is selected for INPUT
                ''',
                'input_select',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('io-timer-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Read/write timer set
                ''',
                'io_timer_set',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('locked', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Lock on data queue (so_rcv only)
                ''',
                'locked',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('not-interruptible', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Not interruptible
                ''',
                'not_interruptible',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('out-of-band-select', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Buffer is selected for OBAND
                ''',
                'out_of_band_select',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('output-select', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Buffer is selected for OUTPUT
                ''',
                'output_select',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('waiting-for-data', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Someone is waiting for data/space
                ''',
                'waiting_for_data',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('waiting-for-lock', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Someone is waiting to lock
                ''',
                'waiting_for_lock',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('wakeup', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Read/write wakeup pending
                ''',
                'wakeup',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'send-buf-state-flags',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.Timer' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.DetailInformations.DetailInformation.Timer',
            False, 
            [
            _MetaInfoClassMember('timer-activations', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of timer activations
                ''',
                'timer_activations',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('timer-expirations', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of timer expirations
                ''',
                'timer_expirations',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('timer-next-activation', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Timer next activation (msec)
                ''',
                'timer_next_activation',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('timer-type', REFERENCE_ENUM_CLASS, 'TcpTimerEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpTimerEnum', 
                [], [], 
                '''                Timer Type
                ''',
                'timer_type',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'timer',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SackBlk' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SackBlk',
            False, 
            [
            _MetaInfoClassMember('end', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                End   seq no. of sack block
                ''',
                'end',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Start seq no. of sack block
                ''',
                'start',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'sack-blk',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendSackHole' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendSackHole',
            False, 
            [
            _MetaInfoClassMember('duplicated-ack', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of dup (s)acks for this hole
                ''',
                'duplicated_ack',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('end', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                End   seq no. of hole
                ''',
                'end',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('retransmitted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Next seq. no in hole to be retransmitted
                ''',
                'retransmitted',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Start seq no. of hole
                ''',
                'start',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'send-sack-hole',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.DetailInformations.DetailInformation' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.DetailInformations.DetailInformation',
            False, 
            [
            _MetaInfoClassMember('pcb-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Detail information about TCP connection, put
                null for all
                ''',
                'pcb_id',
                'Cisco-IOS-XR-ip-tcp-oper', True),
            _MetaInfoClassMember('ack-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ACK hold time (msec)
                ''',
                'ack_hold_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'TcpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpAddressFamilyEnum', 
                [], [], 
                '''                Address Family
                ''',
                'address_family',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('connect-retries', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of times connect will be retried?
                ''',
                'connect_retries',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('connect-retry-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Connect retry interval in seconds
                ''',
                'connect_retry_interval',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('connection-state', REFERENCE_ENUM_CLASS, 'TcpConnStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnStateEnum', 
                [], [], 
                '''                Connection state
                ''',
                'connection_state',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('current-receive-queue-packet-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current receive queue size in packets
                ''',
                'current_receive_queue_packet_size',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('current-receive-queue-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current receive queue size in bytes
                ''',
                'current_receive_queue_size',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('current-send-queue-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current send queue size in bytes
                ''',
                'current_send_queue_size',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('established-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which connection is established
                ''',
                'established_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('feature-flags', REFERENCE_CLASS, 'FeatureFlags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FeatureFlags', 
                [], [], 
                '''                Connection feature flags
                ''',
                'feature_flags',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('fib-label-output', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cached Label stack
                ''',
                'fib_label_output',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=7),
            _MetaInfoClassMember('fib-pd-ctx', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cached fib pd context
                ''',
                'fib_pd_ctx',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=4),
            _MetaInfoClassMember('fib-pd-ctx-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cached fib pd context size
                ''',
                'fib_pd_ctx_size',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('foreign-address', REFERENCE_CLASS, 'ForeignAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ForeignAddress', 
                [], [], 
                '''                Foreign address
                ''',
                'foreign_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('foreign-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Foreign port
                ''',
                'foreign_port',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('giveup-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Giveup time (msec)
                ''',
                'giveup_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('hash-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the Hash Bucket
                ''',
                'hash_index',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-retrans-forever', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Retransimit forever?
                ''',
                'is_retrans_forever',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('keep-alive-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Keepalive time (msec)
                ''',
                'keep_alive_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('krtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Round trip time (karn algorithm) (msec)
                ''',
                'krtt',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('last-ack-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ACK number of a sent segment
                ''',
                'last_ack_sent',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.LocalAddress', 
                [], [], 
                '''                Local address
                ''',
                'local_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-app-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Instance number of the local process
                ''',
                'local_app_instance',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-pid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Id of the local process
                ''',
                'local_pid',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local port
                ''',
                'local_port',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('max-mss', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Highest MSS ever used
                ''',
                'max_mss',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('max-receive-queue-packet-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max receive queue size in packets
                ''',
                'max_receive_queue_packet_size',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('max-receive-queue-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max receive queue size in bytes
                ''',
                'max_receive_queue_size',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('max-rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max RTT (msec)
                ''',
                'max_rtt',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('max-send-queue-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max send queue size in bytes
                ''',
                'max_send_queue_size',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('min-mss', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lowest MSS ever used
                ''',
                'min_mss',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('min-rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Min RTT (msec)
                ''',
                'min_rtt',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mss', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max segment size calculated in bytes
                ''',
                'mss',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('num-labels', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of labels returned by fib lookup
                ''',
                'num_labels',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('output-ifhandle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cached Outgoing interface  handle
                ''',
                'output_ifhandle',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('packet-priority', REFERENCE_ENUM_CLASS, 'PakPrioEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'PakPrioEnum', 
                [], [], 
                '''                Priority given to packets on this socket
                ''',
                'packet_priority',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('packet-tos', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Type of Service value to be applied to
                transmistted packets
                ''',
                'packet_tos',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('packet-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                TTL to be applied to transmited packets
                ''',
                'packet_ttl',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('pcb', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PCB Address
                ''',
                'pcb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('peer-mss', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max segment size offered by the peer in bytes
                ''',
                'peer_mss',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('receive-adv-window-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Receive advertised window size in bytes
                ''',
                'receive_adv_window_size',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('receive-buf-state-flags', REFERENCE_CLASS, 'ReceiveBufStateFlags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ReceiveBufStateFlags', 
                [], [], 
                '''                Receive buffer state flags
                ''',
                'receive_buf_state_flags',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('receive-initial-sequence-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Initial receive sequence number
                ''',
                'receive_initial_sequence_num',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('receive-next-sequence-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Next sequence number expected
                ''',
                'receive_next_sequence_num',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('receive-window-scale', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Window scaling for receive window
                ''',
                'receive_window_scale',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('receive-window-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Receive window size in bytes
                ''',
                'receive_window_size',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('recvbuf-hiwat', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Receive buffer's high water mark
                ''',
                'recvbuf_hiwat',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('recvbuf-lowwat', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Receive buffer's low water mark
                ''',
                'recvbuf_lowwat',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('request-flags', REFERENCE_CLASS, 'RequestFlags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.RequestFlags', 
                [], [], 
                '''                Connection request flags
                ''',
                'request_flags',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('request-receive-window-scale', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Requested receive window scale
                ''',
                'request_receive_window_scale',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('retries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of retries
                ''',
                'retries',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('rqst-send-wnd-scale', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Requested send window scale
                ''',
                'rqst_send_wnd_scale',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('rtto', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Round trip timeout (msec)
                ''',
                'rtto',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('rxsy-naclname', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                RX Syn acl name
                ''',
                'rxsy_naclname',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sack-blk', REFERENCE_LIST, 'SackBlk' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SackBlk', 
                [], [], 
                '''                Seq nos. of sack blocks
                ''',
                'sack_blk',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=6),
            _MetaInfoClassMember('save-queue-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Save queue (out-of seq data) size in bytes
                ''',
                'save_queue_size',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('send-buf-state-flags', REFERENCE_CLASS, 'SendBufStateFlags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendBufStateFlags', 
                [], [], 
                '''                Send buffer state flags
                ''',
                'send_buf_state_flags',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('send-congestion-window-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Send congestion window size in bytes
                ''',
                'send_congestion_window_size',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('send-initial-sequence-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Initial send sequence number
                ''',
                'send_initial_sequence_num',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('send-max-sequence-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Highest sequence number sent
                ''',
                'send_max_sequence_num',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('send-next-sequence-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sequence number of next data to be sent
                ''',
                'send_next_sequence_num',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('send-pdu-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                # of PDU's in Send Buffer
                ''',
                'send_pdu_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('send-sack-hole', REFERENCE_LIST, 'SendSackHole' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendSackHole', 
                [], [], 
                '''                Sorted list of sack holes
                ''',
                'send_sack_hole',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=6),
            _MetaInfoClassMember('send-unack-sequence-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sequence number of unacked data
                ''',
                'send_unack_sequence_num',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('send-window-scale', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Window scaling for send window
                ''',
                'send_window_scale',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('send-window-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Send window size in bytes
                ''',
                'send_window_size',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sendbuf-hiwat', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Send buffer's high water mark
                ''',
                'sendbuf_hiwat',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sendbuf-lowwat', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Send buffer's low water mark
                ''',
                'sendbuf_lowwat',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sendbuf-notify-thresh', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Send buffer's notify threshold
                ''',
                'sendbuf_notify_thresh',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('so', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Socket Address
                ''',
                'so',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sock-error', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Socket error code
                ''',
                'sock_error',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('socket-option-flags', REFERENCE_CLASS, 'SocketOptionFlags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketOptionFlags', 
                [], [], 
                '''                Socket option flags
                ''',
                'socket_option_flags',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('socket-state-flags', REFERENCE_CLASS, 'SocketStateFlags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketStateFlags', 
                [], [], 
                '''                Socket state flags
                ''',
                'socket_state_flags',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('soft-error', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Error code from ICMP Notify
                ''',
                'soft_error',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('srtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Smoothed round trip time * 8 (msec)
                ''',
                'srtt',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('srtv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Smoothed round trip time variance * 4 (msec)
                ''',
                'srtv',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('state-flags', REFERENCE_CLASS, 'StateFlags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.StateFlags', 
                [], [], 
                '''                Connection state flags
                ''',
                'state_flags',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('syn-wait-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SYN wait time (msec)
                ''',
                'syn_wait_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('tcpcb', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                TCPCB Address
                ''',
                'tcpcb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('time-stamp-recent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Timestamp from remote host
                ''',
                'time_stamp_recent',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('time-stamp-recent-age', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Timestamp when last updated
                ''',
                'time_stamp_recent_age',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('timer', REFERENCE_LIST, 'Timer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.DetailInformations.DetailInformation.Timer', 
                [], [], 
                '''                Timers
                ''',
                'timer',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=8),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF Id
                ''',
                'vrf_id',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'detail-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.DetailInformations' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.DetailInformations',
            False, 
            [
            _MetaInfoClassMember('detail-information', REFERENCE_LIST, 'DetailInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.DetailInformations.DetailInformation', 
                [], [], 
                '''                Protocol Control Block ID
                ''',
                'detail_information',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'detail-informations',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.BriefInformations.BriefInformation.LocalAddress' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.BriefInformations.BriefInformation.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'TcpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpAddressFamilyEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.BriefInformations.BriefInformation.ForeignAddress' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.BriefInformations.BriefInformation.ForeignAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'TcpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpAddressFamilyEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'foreign-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.BriefInformations.BriefInformation' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.BriefInformations.BriefInformation',
            False, 
            [
            _MetaInfoClassMember('pcb-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Protocol Control Block ID
                ''',
                'pcb_id',
                'Cisco-IOS-XR-ip-tcp-oper', True),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'TcpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('connection-state', REFERENCE_ENUM_CLASS, 'TcpConnStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnStateEnum', 
                [], [], 
                '''                Connection state
                ''',
                'connection_state',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('current-receive-queue-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current receive queue size in bytes
                ''',
                'current_receive_queue_size',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('current-send-queue-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current send queue size in bytes
                ''',
                'current_send_queue_size',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('foreign-address', REFERENCE_CLASS, 'ForeignAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.BriefInformations.BriefInformation.ForeignAddress', 
                [], [], 
                '''                Foreign address
                ''',
                'foreign_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('foreign-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Foreign port
                ''',
                'foreign_port',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.BriefInformations.BriefInformation.LocalAddress', 
                [], [], 
                '''                Local address
                ''',
                'local_address',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-pid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Id of the local process
                ''',
                'local_pid',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local port
                ''',
                'local_port',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('pcb', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PCB Address
                ''',
                'pcb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF ID
                ''',
                'vrf_id',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node.BriefInformations' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node.BriefInformations',
            False, 
            [
            _MetaInfoClassMember('brief-information', REFERENCE_LIST, 'BriefInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.BriefInformations.BriefInformation', 
                [], [], 
                '''                Brief information about a TCP connection
                ''',
                'brief_information',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'brief-informations',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Describing a location
                ''',
                'id',
                'Cisco-IOS-XR-ip-tcp-oper', True),
            _MetaInfoClassMember('brief-informations', REFERENCE_CLASS, 'BriefInformations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.BriefInformations', 
                [], [], 
                '''                Table listing connections for which brief
                information is provided.Note that not all
                connections are listed in the brief table.
                ''',
                'brief_informations',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('detail-informations', REFERENCE_CLASS, 'DetailInformations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.DetailInformations', 
                [], [], 
                '''                Table listing TCP connections for which
                detailed information is provided
                ''',
                'detail_informations',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('extended-information', REFERENCE_CLASS, 'ExtendedInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.ExtendedInformation', 
                [], [], 
                '''                Extended Filter related Information
                ''',
                'extended_information',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node.Statistics', 
                [], [], 
                '''                Statistics of all TCP connections
                ''',
                'statistics',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection.Nodes' : {
        'meta_info' : _MetaInfoClass('TcpConnection.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes.Node', 
                [], [], 
                '''                Information about a single node
                ''',
                'node',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpConnection' : {
        'meta_info' : _MetaInfoClass('TcpConnection',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpConnection.Nodes', 
                [], [], 
                '''                Table of information about all nodes present on
                the system
                ''',
                'nodes',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'tcp-connection',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'Tcp.Nodes.Node.Statistics.Ipv4Traffic' : {
        'meta_info' : _MetaInfoClass('Tcp.Nodes.Node.Statistics.Ipv4Traffic',
            False, 
            [
            _MetaInfoClassMember('tcp-checksum-error-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TCP packets with checksum errors
                ''',
                'tcp_checksum_error_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('tcp-dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TCP packets dropped (no port)
                ''',
                'tcp_dropped_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('tcp-input-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TCP packets received
                ''',
                'tcp_input_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('tcp-output-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TCP packets transmitted
                ''',
                'tcp_output_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('tcp-retransmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TCP packets retransmitted
                ''',
                'tcp_retransmitted_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'ipv4-traffic',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'Tcp.Nodes.Node.Statistics.Ipv6Traffic' : {
        'meta_info' : _MetaInfoClass('Tcp.Nodes.Node.Statistics.Ipv6Traffic',
            False, 
            [
            _MetaInfoClassMember('tcp-checksum-error-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TCP packets with checksum errors
                ''',
                'tcp_checksum_error_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('tcp-dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TCP packets dropped (no port)
                ''',
                'tcp_dropped_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('tcp-input-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TCP packets received
                ''',
                'tcp_input_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('tcp-output-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TCP packets transmitted
                ''',
                'tcp_output_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('tcp-retransmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TCP packets retransmitted
                ''',
                'tcp_retransmitted_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'ipv6-traffic',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'Tcp.Nodes.Node.Statistics' : {
        'meta_info' : _MetaInfoClass('Tcp.Nodes.Node.Statistics',
            False, 
            [
            _MetaInfoClassMember('ipv4-traffic', REFERENCE_CLASS, 'Ipv4Traffic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'Tcp.Nodes.Node.Statistics.Ipv4Traffic', 
                [], [], 
                '''                TCP Traffic statistics for IPv4
                ''',
                'ipv4_traffic',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('ipv6-traffic', REFERENCE_CLASS, 'Ipv6Traffic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'Tcp.Nodes.Node.Statistics.Ipv6Traffic', 
                [], [], 
                '''                TCP Traffic statistics for IPv6
                ''',
                'ipv6_traffic',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'Tcp.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Tcp.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-ip-tcp-oper', True),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'Tcp.Nodes.Node.Statistics', 
                [], [], 
                '''                Statistical TCP operational data for a node
                ''',
                'statistics',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'Tcp.Nodes' : {
        'meta_info' : _MetaInfoClass('Tcp.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'Tcp.Nodes.Node', 
                [], [], 
                '''                TCP operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'Tcp' : {
        'meta_info' : _MetaInfoClass('Tcp',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'Tcp.Nodes', 
                [], [], 
                '''                Node-specific TCP operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'tcp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Session.BriefSessions.BriefSession' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Session.BriefSessions.BriefSession',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ID of NSR Sesison
                ''',
                'id',
                'Cisco-IOS-XR-ip-tcp-oper', True),
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'AddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'AddrFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'address_family',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('foreign-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Foreign address
                ''',
                'foreign_address',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=4),
            _MetaInfoClassMember('foreign-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Foreign port
                ''',
                'foreign_port',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-admin-configured-up', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is NSR administratively configured?
                ''',
                'is_admin_configured_up',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-ds-operational-up', REFERENCE_ENUM_CLASS, 'NsrStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'NsrStatusEnum', 
                [], [], 
                '''                Is Downstream NSR operational?
                ''',
                'is_ds_operational_up',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-only-receive-path-replication', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is replication limited to receive-path only
                ''',
                'is_only_receive_path_replication',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-us-operational-up', REFERENCE_ENUM_CLASS, 'NsrStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'NsrStatusEnum', 
                [], [], 
                '''                Is Upstream NSR operational?
                ''',
                'is_us_operational_up',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Local address
                ''',
                'local_address',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=4),
            _MetaInfoClassMember('local-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local port
                ''',
                'local_port',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('pcb', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PCB Address
                ''',
                'pcb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sscb', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                SSCB Address
                ''',
                'sscb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF Id
                ''',
                'vrf_id',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'brief-session',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Session.BriefSessions' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Session.BriefSessions',
            False, 
            [
            _MetaInfoClassMember('brief-session', REFERENCE_LIST, 'BriefSession' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Session.BriefSessions.BriefSession', 
                [], [], 
                '''                Brief information about NSR Sessions
                ''',
                'brief_session',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'brief-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.SetInformation' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.SetInformation',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'AddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'AddrFamilyEnum', 
                [], [], 
                '''                Address Family of the sessions in this set
                ''',
                'address_family',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('client-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Instance of the Client that owns this
                Session-set
                ''',
                'client_instance',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('client-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                the name of Clinet that owns this Session-set
                ''',
                'client_name',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-init-sync-in-progress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is an initial sync in progress currently?
                ''',
                'is_init_sync_in_progress',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-sscb-init-sync-ready', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is the SSCB ready for another initial sync?
                ''',
                'is_sscb_init_sync_ready',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Instance of the client application on the local
                node
                ''',
                'local_instance',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-node', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Local node of this set
                ''',
                'local_node',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session-set mode
                ''',
                'mode',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Sessions in the set
                ''',
                'number_of_sessions',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-synced-sessions-down-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                How many sessions are synced with downstream
                partner
                ''',
                'number_of_synced_sessions_down_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-synced-sessions-up-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                How many sessions are synced with upstream
                partner
                ''',
                'number_of_synced_sessions_up_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('pid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PID of the Client that owns this Session-set
                ''',
                'pid',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('protect-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Instance of the client application on the
                protection node
                ''',
                'protect_instance',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('protect-node', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node protecting this set
                ''',
                'protect_node',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('set-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ID of this Session-set
                ''',
                'set_id',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sscb', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Address of the Session Set Control Block
                ''',
                'sscb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sso-role', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TCP role for this set?
                ''',
                'sso_role',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('well-known-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Well Known Port of the client
                ''',
                'well_known_port',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'set-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.PacketHoldQueue' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.PacketHoldQueue',
            False, 
            [
            _MetaInfoClassMember('acknoledgement-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Ack Number
                ''',
                'acknoledgement_number',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Data Length
                ''',
                'data_length',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'packet-hold-queue',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.InternalAckHoldQueue' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.InternalAckHoldQueue',
            False, 
            [
            _MetaInfoClassMember('acknoledgement-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Ack Number
                ''',
                'acknoledgement_number',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Data Length
                ''',
                'data_length',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'internal-ack-hold-queue',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ID of NSR Sesison
                ''',
                'id',
                'Cisco-IOS-XR-ip-tcp-oper', True),
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'AddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'AddrFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'address_family',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('cookie', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Cookie provided by active APP
                ''',
                'cookie',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('fist-standby-sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If initial sync is completed, then the FSSN -
                First Standby Sequence Number
                ''',
                'fist_standby_sequence_number',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('fist-standby-sequence-number-down-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FSSN for the upstream partner
                ''',
                'fist_standby_sequence_number_down_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('fist-standby-sequence-number-up-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FSSN for the upstream partner
                ''',
                'fist_standby_sequence_number_up_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('foreign-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Foreign address
                ''',
                'foreign_address',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=4),
            _MetaInfoClassMember('foreign-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Foreign port
                ''',
                'foreign_port',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('fssn-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Offset of FSSN in input stream
                ''',
                'fssn_offset',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('init-sync-end-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which the initial sync operation was
                ended (in seconds since 1st Jan 1970 00:00:00)
                ''',
                'init_sync_end_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('init-sync-end-time-down-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which the initial sync operation was
                ended (in seconds since 1st Jan 1970 00:00:00)
                ''',
                'init_sync_end_time_down_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('init-sync-end-time-up-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which the initial sync operation was
                ended (in seconds since 1st Jan 1970 00:00:00)
                ''',
                'init_sync_end_time_up_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('init-sync-error', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Initial sync failure reason, if any
                ''',
                'init_sync_error',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('init-sync-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Init Sync flags for the session
                ''',
                'init_sync_flags',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('init-sync-start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which the initial sync operation was
                started (in seconds since 1st Jan 1970 00:00:00)
                ''',
                'init_sync_start_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('init-sync-start-time-down-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which the initial sync operation was
                started (in seconds since 1st Jan 1970 00:00:00)
                ''',
                'init_sync_start_time_down_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('init-sync-start-time-up-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which the initial sync operation was
                started (in seconds since 1st Jan 1970 00:00:00)
                ''',
                'init_sync_start_time_up_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('internal-ack-hold-queue', REFERENCE_LIST, 'InternalAckHoldQueue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.InternalAckHoldQueue', 
                [], [], 
                '''                Sequence Number and datalength of each node in
                hold_iackqueue
                ''',
                'internal_ack_hold_queue',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-admin-configured-up', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is NSR administratively configured?
                ''',
                'is_admin_configured_up',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-ds-operational-up', REFERENCE_ENUM_CLASS, 'NsrStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'NsrStatusEnum', 
                [], [], 
                '''                Is Downstream NSR operational?
                ''',
                'is_ds_operational_up',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-init-sync-error-local', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Initial sync failed due to a local error or
                remote stack
                ''',
                'is_init_sync_error_local',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-init-sync-in-progress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is initial-sync currently in progress?
                ''',
                'is_init_sync_in_progress',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-init-sync-second-phase', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is initial sync in the second phase?
                ''',
                'is_init_sync_second_phase',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-only-receive-path-replication', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is replication limited to receive-path only
                ''',
                'is_only_receive_path_replication',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-session-replicated', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has the session been replicated to standby?
                ''',
                'is_session_replicated',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-session-synced', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has the session completed initial-sync?
                ''',
                'is_session_synced',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-us-operational-up', REFERENCE_ENUM_CLASS, 'NsrStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'NsrStatusEnum', 
                [], [], 
                '''                Is Upstream NSR operational?
                ''',
                'is_us_operational_up',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Local address
                ''',
                'local_address',
                'Cisco-IOS-XR-ip-tcp-oper', False, max_elements=4),
            _MetaInfoClassMember('local-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local port
                ''',
                'local_port',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('max-number-of-held-internal-ack', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Max number of internal acks have been held
                ''',
                'max_number_of_held_internal_ack',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('max-number-of-held-internal-ack-reach-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max number of held internal acks reaches at
                ''',
                'max_number_of_held_internal_ack_reach_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('max-number-of-held-packet', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Max number of incoming packets have been held
                ''',
                'max_number_of_held_packet',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('max-number-of-held-packet-reach-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max number of held incoming packets reaches at
                ''',
                'max_number_of_held_packet_reach_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nsr-down-reason', REFERENCE_ENUM_CLASS, 'NsrDownReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'NsrDownReasonEnum', 
                [], [], 
                '''                If NSR is not up, the reason for it.
                ''',
                'nsr_down_reason',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nsr-down-reason-down-stream', REFERENCE_ENUM_CLASS, 'NsrDownReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'NsrDownReasonEnum', 
                [], [], 
                '''                The reason NSR is not up towards the upstream
                partner
                ''',
                'nsr_down_reason_down_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nsr-down-reason-up-stream', REFERENCE_ENUM_CLASS, 'NsrDownReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'NsrDownReasonEnum', 
                [], [], 
                '''                The reason NSR is not up towards the upstream
                partner
                ''',
                'nsr_down_reason_up_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nsr-down-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which NSR went down
                ''',
                'nsr_down_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nsr-down-time-down-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which NSR went down
                ''',
                'nsr_down_time_down_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nsr-down-time-up-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which NSR went down
                ''',
                'nsr_down_time_up_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('packet-hold-queue', REFERENCE_LIST, 'PacketHoldQueue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.PacketHoldQueue', 
                [], [], 
                '''                Sequence Number and datalength of each node in
                hold_pakqueue
                ''',
                'packet_hold_queue',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('pcb', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PCB Address
                ''',
                'pcb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('peer-endp-hdl-down-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Peer NCD endp handle
                ''',
                'peer_endp_hdl_down_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('peer-endp-hdl-up-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Peer NCD endp handle
                ''',
                'peer_endp_hdl_up_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sequence-number-of-init-sync', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ID of the Initial sync operation
                ''',
                'sequence_number_of_init_sync',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sequence-number-of-init-sync-down-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ID of the Initial sync operation
                ''',
                'sequence_number_of_init_sync_down_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sequence-number-of-init-sync-up-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ID of the Initial sync operation
                ''',
                'sequence_number_of_init_sync_up_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('set-information', REFERENCE_CLASS, 'SetInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.SetInformation', 
                [], [], 
                '''                Sesson-set information
                ''',
                'set_information',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sscb', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                SSCB Address
                ''',
                'sscb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF Id
                ''',
                'vrf_id',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'detail-session',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Session.DetailSessions' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Session.DetailSessions',
            False, 
            [
            _MetaInfoClassMember('detail-session', REFERENCE_LIST, 'DetailSession' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession', 
                [], [], 
                '''                showing detailed information of NSR Sessions
                ''',
                'detail_session',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'detail-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Session' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Session',
            False, 
            [
            _MetaInfoClassMember('brief-sessions', REFERENCE_CLASS, 'BriefSessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Session.BriefSessions', 
                [], [], 
                '''                Information about TCP NSR Sessions
                ''',
                'brief_sessions',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('detail-sessions', REFERENCE_CLASS, 'DetailSessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Session.DetailSessions', 
                [], [], 
                '''                Table about TCP NSR Sessions details
                ''',
                'detail_sessions',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Client.DetailClients.DetailClient' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Client.DetailClients.DetailClient',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ID of NSR client
                ''',
                'id',
                'Cisco-IOS-XR-ip-tcp-oper', True),
            _MetaInfoClassMember('ccb', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Address of the Client Control Block
                ''',
                'ccb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('connected-at', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time of connect (in seconds since 1st Jan 1970
                00:00:00)
                ''',
                'connected_at',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Instance of the Client
                ''',
                'instance',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-notification-registered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Registered with TCP for notifications?
                ''',
                'is_notification_registered',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('job-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                JOb ID of Client
                ''',
                'job_id',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions owned by this client 
                ''',
                'number_of_sessions',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions with NSR up
                ''',
                'number_of_up_sessions',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('numberof-sets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Sets owned by this client 
                ''',
                'numberof_sets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('pid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PID of the Client
                ''',
                'pid',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Proc name of Clinet
                ''',
                'process_name',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'detail-client',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Client.DetailClients' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Client.DetailClients',
            False, 
            [
            _MetaInfoClassMember('detail-client', REFERENCE_LIST, 'DetailClient' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Client.DetailClients.DetailClient', 
                [], [], 
                '''                showing detailed information of NSR Clients
                ''',
                'detail_client',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'detail-clients',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Client.BriefClients.BriefClient' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Client.BriefClients.BriefClient',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ID of NSR client
                ''',
                'id',
                'Cisco-IOS-XR-ip-tcp-oper', True),
            _MetaInfoClassMember('ccb', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Address of the Client Control Block
                ''',
                'ccb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Instance of the Client
                ''',
                'instance',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('job-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                JOb ID of Client
                ''',
                'job_id',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions owned by this client 
                ''',
                'number_of_sessions',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions with NSR up 
                ''',
                'number_of_up_sessions',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('numberof-sets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Sets owned by this client 
                ''',
                'numberof_sets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('pid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PID of the Client
                ''',
                'pid',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Proc name of Clinet
                ''',
                'process_name',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'brief-client',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Client.BriefClients' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Client.BriefClients',
            False, 
            [
            _MetaInfoClassMember('brief-client', REFERENCE_LIST, 'BriefClient' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Client.BriefClients.BriefClient', 
                [], [], 
                '''                Brief information about NSR Client
                ''',
                'brief_client',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'brief-clients',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Client' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Client',
            False, 
            [
            _MetaInfoClassMember('brief-clients', REFERENCE_CLASS, 'BriefClients' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Client.BriefClients', 
                [], [], 
                '''                Information about TCP NSR Client
                ''',
                'brief_clients',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('detail-clients', REFERENCE_CLASS, 'DetailClients' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Client.DetailClients', 
                [], [], 
                '''                Table about TCP NSR Client details
                ''',
                'detail_clients',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'client',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.SessionSet.DetailSets.DetailSet' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.SessionSet.DetailSets.DetailSet',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ID of NSR Sesison Set
                ''',
                'id',
                'Cisco-IOS-XR-ip-tcp-oper', True),
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'AddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'AddrFamilyEnum', 
                [], [], 
                '''                Address Family of the sessions in this set
                ''',
                'address_family',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('audit-end-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which the last audit operation was ended
                (in seconds since 1st Jan 1970 00:00:00)
                ''',
                'audit_end_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('audit-seq-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ID of the current or the last audit operation
                ''',
                'audit_seq_number',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('audit-start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which last or current audit operation
                was started (in seconds since 1st Jan 1970 00:00
                :00)
                ''',
                'audit_start_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('init-sync-end-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which the last initial sync operation
                was ended (in seconds since 1st Jan 1970 00:00
                :00)
                ''',
                'init_sync_end_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('init-sync-error', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Initial sync failure reason, if any
                ''',
                'init_sync_error',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('init-sync-ready-end-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which the session set last went
                not-ready for initial sync (in seconds since 1st
                Jan 1970 00:00:00)
                ''',
                'init_sync_ready_end_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('init-sync-ready-start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which the session was ready for initial
                sync last (in seconds since 1st Jan 1970 00:00
                :00)
                ''',
                'init_sync_ready_start_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('init-sync-start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which last or current initial sync
                operation was started (in seconds since 1st Jan
                1970 00:00:00)
                ''',
                'init_sync_start_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('init-sync-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time left on the initial sync timer
                ''',
                'init_sync_timer',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-audit-in-progress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is an audit in progress currently?
                ''',
                'is_audit_in_progress',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-init-sync-error-local', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Initial sync failed due to a local error or
                remote stack
                ''',
                'is_init_sync_error_local',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-init-sync-in-progress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is an initial sync in progress currently?
                ''',
                'is_init_sync_in_progress',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-init-sync-second-phase', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is initial sync in the second phase?
                ''',
                'is_init_sync_second_phase',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-sscb-init-sync-ready', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is the SSCB ready for another initial sync?
                ''',
                'is_sscb_init_sync_ready',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Instance of the client application on the local
                node
                ''',
                'local_instance',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-node', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Local node of this set
                ''',
                'local_node',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session-set mode
                ''',
                'mode',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nsr-reset-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time at which NSR was last reset on the session
                set (in seconds since 1st Jan 1970 00:00:00)
                ''',
                'nsr_reset_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-init-synced-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions that are synced as part of
                the current initial sync operation
                ''',
                'number_of_init_synced_sessions',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Sessions in the set
                ''',
                'number_of_sessions',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-sessions-init-sync-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions that failed to sync as part
                of the current initial sync operation
                ''',
                'number_of_sessions_init_sync_failed',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-synced-sessions-down-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                How many sessions are synced with downstream
                partner
                ''',
                'number_of_synced_sessions_down_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-synced-sessions-up-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                How many sessions are synced with upstream
                partner
                ''',
                'number_of_synced_sessions_up_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('pid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PID of the Client that owns this Session-set
                ''',
                'pid',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('protect-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Instance of the client application on the
                protection node
                ''',
                'protect_instance',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('protect-node', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node protecting this set
                ''',
                'protect_node',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sequence-number-of-init-sync', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ID of the current or the last initial sync
                operation
                ''',
                'sequence_number_of_init_sync',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('set-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ID of this Session-set
                ''',
                'set_id',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sscb', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Address of the Session Set Control Block
                ''',
                'sscb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sso-role', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TCP role for this set?
                ''',
                'sso_role',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('total-number-of-init-sync-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions being synced as part of the
                current initial sync operation
                ''',
                'total_number_of_init_sync_sessions',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('well-known-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Well Known Port of the client
                ''',
                'well_known_port',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'detail-set',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.SessionSet.DetailSets' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.SessionSet.DetailSets',
            False, 
            [
            _MetaInfoClassMember('detail-set', REFERENCE_LIST, 'DetailSet' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.SessionSet.DetailSets.DetailSet', 
                [], [], 
                '''                showing detailed information of NSR Session
                Sets
                ''',
                'detail_set',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'detail-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.SessionSet.BriefSets.BriefSet' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.SessionSet.BriefSets.BriefSet',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ID of NSR Session Set
                ''',
                'id',
                'Cisco-IOS-XR-ip-tcp-oper', True),
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'AddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'AddrFamilyEnum', 
                [], [], 
                '''                Address Family of the sessions in this set
                ''',
                'address_family',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('client-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Instance of the Client that owns this
                Session-set
                ''',
                'client_instance',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('client-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                the name of Clinet that owns this Session-set
                ''',
                'client_name',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-init-sync-in-progress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is an initial sync in progress currently?
                ''',
                'is_init_sync_in_progress',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('is-sscb-init-sync-ready', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is the SSCB ready for another initial sync?
                ''',
                'is_sscb_init_sync_ready',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Instance of the client application on the local
                node
                ''',
                'local_instance',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('local-node', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Local node of this set
                ''',
                'local_node',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session-set mode
                ''',
                'mode',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Sessions in the set
                ''',
                'number_of_sessions',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-synced-sessions-down-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                How many sessions are synced with downstream
                partner
                ''',
                'number_of_synced_sessions_down_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-synced-sessions-up-stream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                How many sessions are synced with upstream
                partner
                ''',
                'number_of_synced_sessions_up_stream',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('pid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PID of the Client that owns this Session-set
                ''',
                'pid',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('protect-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Instance of the client application on the
                protection node
                ''',
                'protect_instance',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('protect-node', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node protecting this set
                ''',
                'protect_node',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('set-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ID of this Session-set
                ''',
                'set_id',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sscb', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Address of the Session Set Control Block
                ''',
                'sscb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sso-role', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TCP role for this set?
                ''',
                'sso_role',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('well-known-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Well Known Port of the client
                ''',
                'well_known_port',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'brief-set',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.SessionSet.BriefSets' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.SessionSet.BriefSets',
            False, 
            [
            _MetaInfoClassMember('brief-set', REFERENCE_LIST, 'BriefSet' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.SessionSet.BriefSets.BriefSet', 
                [], [], 
                '''                Brief information about NSR Session Sets
                ''',
                'brief_set',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'brief-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.SessionSet' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.SessionSet',
            False, 
            [
            _MetaInfoClassMember('brief-sets', REFERENCE_CLASS, 'BriefSets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.SessionSet.BriefSets', 
                [], [], 
                '''                Information about TCP NSR Session Sets
                ''',
                'brief_sets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('detail-sets', REFERENCE_CLASS, 'DetailSets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.SessionSet.DetailSets', 
                [], [], 
                '''                Table about TCP NSR Session Sets details
                ''',
                'detail_sets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'session-set',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.Common' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.Common',
            False, 
            [
            _MetaInfoClassMember('cleanup-rcv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of received Cleanup messages
                ''',
                'cleanup_rcv',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('cleanup-rcv-fail-buffer-trim', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Cleanup messages that had trim
                failures
                ''',
                'cleanup_rcv_fail_buffer_trim',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('cleanup-rcv-success', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successfully received Cleanup messages
                ''',
                'cleanup_rcv_success',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('cleanup-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful Cleanup messages
                ''',
                'cleanup_send',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('cleanup-send-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failed Cleanup messages
                ''',
                'cleanup_send_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-xfer-rcv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of received DATA transfers
                ''',
                'data_xfer_rcv',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-xfer-rcv-fail-buffer-trim', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of received DATA transfers that had
                buffer trim failures
                ''',
                'data_xfer_rcv_fail_buffer_trim',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-xfer-rcv-fail-snd-una-out-of-sync', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of received DATA transfers that had
                failures because the send path was out of sync
                ''',
                'data_xfer_rcv_fail_snd_una_out_of_sync',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-xfer-rcv-success', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successfully received DATA transfers
                ''',
                'data_xfer_rcv_success',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-xfer-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful DATA transfers
                ''',
                'data_xfer_send',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-xfer-send-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failed DATA transfers
                ''',
                'data_xfer_send_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-xfer-send-iov-alloc', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of data transfer msgs., that required new
                IOV's to be allocated
                ''',
                'data_xfer_send_iov_alloc',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-xfer-send-total', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Amount of data transferred
                ''',
                'data_xfer_send_total',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nack-rcv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of received NACK messages
                ''',
                'nack_rcv',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nack-rcv-fail-data-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of received NACK messages that had
                failures when sending data in response to the
                NACK
                ''',
                'nack_rcv_fail_data_send',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nack-rcv-success', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successfully received NACK messages
                ''',
                'nack_rcv_success',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nack-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful NACK messages
                ''',
                'nack_send',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nack-send-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failed NACK messages
                ''',
                'nack_send_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('seg-instr-rcv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of received Segmentation instruction
                messages
                ''',
                'seg_instr_rcv',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('seg-instr-rcv-fail-buffer-trim', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of received Segmentation instructions
                that had buffer trim failures
                ''',
                'seg_instr_rcv_fail_buffer_trim',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('seg-instr-rcv-fail-tcp-process', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of received Segmentation instructions
                that had failures during TCP processing
                ''',
                'seg_instr_rcv_fail_tcp_process',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('seg-instr-rcv-success', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successfully received Segmentation
                instruction messages
                ''',
                'seg_instr_rcv_success',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('seg-instr-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful Segmentation instruction
                messages
                ''',
                'seg_instr_send',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('seg-instr-send-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failed Segmentation instruction
                messages
                ''',
                'seg_instr_send_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('seg-instr-send-units', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of segement units transferred via the
                successful Segmentation instruction messages
                ''',
                'seg_instr_send_units',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'common',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.AggrOnly' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.AggrOnly',
            False, 
            [
            _MetaInfoClassMember('cleanup-rcv-drop-no-pcb', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Cleanup messages dropped because PCB
                wasn't found
                ''',
                'cleanup_rcv_drop_no_pcb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('cleanup-rcv-drop-no-scb-dp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Cleanup messages dropped because SCB
                DP wasn't found
                ''',
                'cleanup_rcv_drop_no_scb_dp',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-xfer-rcv-drop-no-pcb', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Data transfer messages dropped because
                PCB wasn't found
                ''',
                'data_xfer_rcv_drop_no_pcb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-xfer-rcv-drop-no-scb-dp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Data transfer messages dropped because
                SCB DP wasn't found
                ''',
                'data_xfer_rcv_drop_no_scb_dp',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nack-rcv-drop-no-pcb', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of NACK messages dropped because PCB
                wasn't found
                ''',
                'nack_rcv_drop_no_pcb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nack-rcv-drop-no-scb-dp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of NACK messages dropped because SCB DP
                wasn't found
                ''',
                'nack_rcv_drop_no_scb_dp',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('seg-instr-rcv-drop-no-pcb', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Segmentation instruction messages
                dropped because PCB wasn't found
                ''',
                'seg_instr_rcv_drop_no_pcb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('seg-instr-rcv-drop-no-scb-dp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Segmentation instruction messages
                dropped because SCB DP wasn't found
                ''',
                'seg_instr_rcv_drop_no_scb_dp',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'aggr-only',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Statistics.Summary.SndCounters' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Statistics.Summary.SndCounters',
            False, 
            [
            _MetaInfoClassMember('aggr-only', REFERENCE_CLASS, 'AggrOnly' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.AggrOnly', 
                [], [], 
                '''                Aggregate only send path counters
                ''',
                'aggr_only',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('common', REFERENCE_CLASS, 'Common' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.Common', 
                [], [], 
                '''                Common send path counters
                ''',
                'common',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'snd-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.Common' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.Common',
            False, 
            [
            _MetaInfoClassMember('abort', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times the active aborted an audit
                session
                ''',
                'abort',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mark-session-set-ack-rcv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of audit mark acks received by active
                ''',
                'mark_session_set_ack_rcv',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mark-session-set-ack-rcv-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of audit mark acks dropped by active
                ''',
                'mark_session_set_ack_rcv_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mark-session-set-ack-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful audit mark acks sent by
                standby
                ''',
                'mark_session_set_ack_send',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mark-session-set-ack-send-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of audit mark acks that couldn't be sent
                by standby
                ''',
                'mark_session_set_ack_send_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mark-session-set-nack-rcv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of audit mark nacks received by active
                ''',
                'mark_session_set_nack_rcv',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mark-session-set-nack-rcv-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of audit mark nacks dropped by active
                ''',
                'mark_session_set_nack_rcv_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mark-session-set-nack-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful audit mark nacks sent by
                standby
                ''',
                'mark_session_set_nack_send',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mark-session-set-nack-send-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of audit mark nacks that couldn't be sent
                by standby
                ''',
                'mark_session_set_nack_send_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mark-session-set-rcv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful session-set Mark's received
                by standby
                ''',
                'mark_session_set_rcv',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mark-session-set-rcv-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of session-set Mark's dropped by standby
                ''',
                'mark_session_set_rcv_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mark-session-set-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful session-set Mark's sent by
                active
                ''',
                'mark_session_set_send',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mark-session-set-send-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failed session-set Mark's
                ''',
                'mark_session_set_send_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('session-rcv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of session audits received by standby
                ''',
                'session_rcv',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('session-rcv-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of session audits dropped by standby
                ''',
                'session_rcv_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('session-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful session audits sent by
                active
                ''',
                'session_send',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('session-send-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of session audits that couldn't be sent
                by active
                ''',
                'session_send_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('session-set-response-rcv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of audit responses received by active
                ''',
                'session_set_response_rcv',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('session-set-response-rcv-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of audit responses dropped by active
                ''',
                'session_set_response_rcv_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('session-set-response-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful audit responses sent by
                standby
                ''',
                'session_set_response_send',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('session-set-response-send-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of audit responses that couldn't be sent
                by standby
                ''',
                'session_set_response_send_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sweep-session-set-rcv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful session-set Sweep's
                received by standby
                ''',
                'sweep_session_set_rcv',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sweep-session-set-rcv-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of session-set Sweep's dropped by standby
                ''',
                'sweep_session_set_rcv_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sweep-session-set-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful session-set Sweep's sent by
                active
                ''',
                'sweep_session_set_send',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sweep-session-set-send-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failed session-set Sweep's
                ''',
                'sweep_session_set_send_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'common',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.AggrOnly' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.AggrOnly',
            False, 
            [
            _MetaInfoClassMember('mark-session-set-ack-rcv-drop-aggr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of session-set mark ack messages dropped
                by active
                ''',
                'mark_session_set_ack_rcv_drop_aggr',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mark-session-set-nack-rcv-drop-aggr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of session-set mark nack messages dropped
                by active
                ''',
                'mark_session_set_nack_rcv_drop_aggr',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('mark-session-set-rcv-drop-aggr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of session-set Mark messages dropped by
                standby
                ''',
                'mark_session_set_rcv_drop_aggr',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('session-rcv-drop-aggr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of session audit messages dropped by
                standby
                ''',
                'session_rcv_drop_aggr',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('session-set-response-rcv-drop-aggr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of session-set response messages dropped
                by active
                ''',
                'session_set_response_rcv_drop_aggr',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sweep-session-set-rcv-drop-aggr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of session-set Sweep messages dropped by
                standby
                ''',
                'sweep_session_set_rcv_drop_aggr',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'aggr-only',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters',
            False, 
            [
            _MetaInfoClassMember('aggr-only', REFERENCE_CLASS, 'AggrOnly' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.AggrOnly', 
                [], [], 
                '''                Aggregate only audit counters
                ''',
                'aggr_only',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('common', REFERENCE_CLASS, 'Common' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.Common', 
                [], [], 
                '''                Common audit counters
                ''',
                'common',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'audit-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Statistics.Summary.NotificationStatistic' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Statistics.Summary.NotificationStatistic',
            False, 
            [
            _MetaInfoClassMember('delivered-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                How many were picked up by app?
                ''',
                'delivered_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('dropped-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                How many were dropped because of timeout
                ''',
                'dropped_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('failed-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Errors while queuing the notifs
                ''',
                'failed_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('queued-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                how many were queued
                ''',
                'queued_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'notification-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Statistics.Summary' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Statistics.Summary',
            False, 
            [
            _MetaInfoClassMember('audit-counters', REFERENCE_CLASS, 'AuditCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters', 
                [], [], 
                '''                Aggregate Audit counters
                ''',
                'audit_counters',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('held-packet-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of held packets dropped because of errors
                ''',
                'held_packet_drops',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('internal-ack-drops-immediate-match', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of iACKs not held because of an immediate
                match
                ''',
                'internal_ack_drops_immediate_match',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('internal-ack-drops-initsync-first-phase', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of iACKs dropped because init-sync is in
                1st phase
                ''',
                'internal_ack_drops_initsync_first_phase',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('internal-ack-drops-not-replicated', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of iACKs dropped because session is not
                replicated
                ''',
                'internal_ack_drops_not_replicated',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('internal-ack-drops-stale', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of stale iACKs dropped
                ''',
                'internal_ack_drops_stale',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('last-cleared-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time of last clear (in seconds since 1st Jan
                1970 00:00:00)
                ''',
                'last_cleared_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('notification-statistic', REFERENCE_LIST, 'NotificationStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Statistics.Summary.NotificationStatistic', 
                [], [], 
                '''                Various types of notification stats
                ''',
                'notification_statistic',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-added-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of added sessions
                ''',
                'number_of_added_sessions',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-attempted-init-sync', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                no. of initial-sync attempts
                ''',
                'number_of_attempted_init_sync',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-connected-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of disconnected clients
                ''',
                'number_of_connected_clients',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-created-session-sets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of created session sets
                ''',
                'number_of_created_session_sets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-current-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of current  clients
                ''',
                'number_of_current_clients',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-current-session-sets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of current session sets
                ''',
                'number_of_current_session_sets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-current-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of current sessions
                ''',
                'number_of_current_sessions',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-deleted-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of deleted sessions
                ''',
                'number_of_deleted_sessions',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-destroyed-session-sets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of destroyed session sets
                ''',
                'number_of_destroyed_session_sets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-disconnected-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of disconnected clients
                ''',
                'number_of_disconnected_clients',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-failed-init-sync', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                no. of initial-sync fails
                ''',
                'number_of_failed_init_sync',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-held-but-dropped-internal-acks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of held Internal Acks dropped by Active
                TCP
                ''',
                'number_of_held_but_dropped_internal_acks',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-held-but-dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of held packets dropped by Active TCP
                ''',
                'number_of_held_but_dropped_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-held-internal-acks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Internal Acks held by Active TCP
                ''',
                'number_of_held_internal_acks',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-held-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Packets held by Active TCP
                ''',
                'number_of_held_packets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-internal-ack-drops-no-pcb', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of iACKs dropped because there is no PCB
                ''',
                'number_of_internal_ack_drops_no_pcb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-internal-ack-drops-no-scbdp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of iACKs dropped because there is no
                datapath SCB
                ''',
                'number_of_internal_ack_drops_no_scbdp',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-partner-node', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Number of Parner Nodes
                ''',
                'number_of_partner_node',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-qad-receive-messages-accepts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of messages accepted from partner TCP
                stack(s)
                ''',
                'number_of_qad_receive_messages_accepts',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-qad-receive-messages-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of dropped messages from partner TCP
                stack(s)
                ''',
                'number_of_qad_receive_messages_drops',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-qad-receive-messages-unknowns', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unknown messages from partner TCP
                stack(s)
                ''',
                'number_of_qad_receive_messages_unknowns',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-qad-stale-receive-messages-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of dropped messages from partner TCP
                stack(s) because they were out-of-order
                ''',
                'number_of_qad_stale_receive_messages_drops',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-qad-transfer-message-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of messages failed to be sent to partner
                TCP stack(s)
                ''',
                'number_of_qad_transfer_message_drops',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-qad-transfer-message-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of messages sent to partner TCP stack(s)
                ''',
                'number_of_qad_transfer_message_sent',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-received-internal-acks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Internal Acks received by Active TCP
                ''',
                'number_of_received_internal_acks',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-sent-internal-acks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Internal Acks sent to Active TCP by
                Standby TCP
                ''',
                'number_of_sent_internal_acks',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-succeeded-init-sync', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                no. of initial-sync successes
                ''',
                'number_of_succeeded_init_sync',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('snd-counters', REFERENCE_CLASS, 'SndCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Statistics.Summary.SndCounters', 
                [], [], 
                '''                Aggregate Send path counters
                ''',
                'snd_counters',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient.NotificationStatistic' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient.NotificationStatistic',
            False, 
            [
            _MetaInfoClassMember('delivered-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                How many were picked up by app?
                ''',
                'delivered_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('dropped-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                How many were dropped because of timeout
                ''',
                'dropped_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('failed-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Errors while queuing the notifs
                ''',
                'failed_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('queued-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                how many were queued
                ''',
                'queued_count',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'notification-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ID of NSR Client
                ''',
                'id',
                'Cisco-IOS-XR-ip-tcp-oper', True),
            _MetaInfoClassMember('ccb', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Address of the Client Control Block
                ''',
                'ccb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('connected-at', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time of connect (in seconds since 1st Jan 1970
                00:00:00)
                ''',
                'connected_at',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Instance of the Client
                ''',
                'instance',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('job-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                JOb ID of Client
                ''',
                'job_id',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('last-cleared-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time of last clear (in seconds since 1st Jan
                1970 00:00:00)
                ''',
                'last_cleared_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('notification-statistic', REFERENCE_LIST, 'NotificationStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient.NotificationStatistic', 
                [], [], 
                '''                Various types of notification stats
                ''',
                'notification_statistic',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-created-sscb', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Num of created session sets
                ''',
                'number_of_created_sscb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-deleted-sscb', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Num of deleted session sets
                ''',
                'number_of_deleted_sscb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('pid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PID of the Client
                ''',
                'pid',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Proc name of Clinet
                ''',
                'process_name',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'statistic-client',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Statistics.StatisticClients' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Statistics.StatisticClients',
            False, 
            [
            _MetaInfoClassMember('statistic-client', REFERENCE_LIST, 'StatisticClient' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient', 
                [], [], 
                '''                showing statistic information of NSR Clients
                ''',
                'statistic_client',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'statistic-clients',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Statistics.StatisticSets.StatisticSet' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Statistics.StatisticSets.StatisticSet',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ID of NSR Session Set
                ''',
                'id',
                'Cisco-IOS-XR-ip-tcp-oper', True),
            _MetaInfoClassMember('last-cleared-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time of last clear (in seconds since 1st Jan
                1970 00:00:00)
                ''',
                'last_cleared_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-attempted-init-sync', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                no. of initial-sync attempts
                ''',
                'number_of_attempted_init_sync',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-failed-init-sync', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                no. of initial-sync failures
                ''',
                'number_of_failed_init_sync',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-failover', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Switch-overs
                ''',
                'number_of_failover',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-nsr-resets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times NSR was reset for the session
                ''',
                'number_of_nsr_resets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-succeeded-init-sync', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                no. of initial-sync successes
                ''',
                'number_of_succeeded_init_sync',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('set-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ID of this Session-set
                ''',
                'set_id',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('sscb', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                SSCB Address
                ''',
                'sscb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'statistic-set',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Statistics.StatisticSets' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Statistics.StatisticSets',
            False, 
            [
            _MetaInfoClassMember('statistic-set', REFERENCE_LIST, 'StatisticSet' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Statistics.StatisticSets.StatisticSet', 
                [], [], 
                '''                showing statistic information of NSR Session
                Set
                ''',
                'statistic_set',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'statistic-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession.SndCounters' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession.SndCounters',
            False, 
            [
            _MetaInfoClassMember('cleanup-rcv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of received Cleanup messages
                ''',
                'cleanup_rcv',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('cleanup-rcv-fail-buffer-trim', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Cleanup messages that had trim
                failures
                ''',
                'cleanup_rcv_fail_buffer_trim',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('cleanup-rcv-success', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successfully received Cleanup messages
                ''',
                'cleanup_rcv_success',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('cleanup-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful Cleanup messages
                ''',
                'cleanup_send',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('cleanup-send-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failed Cleanup messages
                ''',
                'cleanup_send_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-xfer-rcv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of received DATA transfers
                ''',
                'data_xfer_rcv',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-xfer-rcv-fail-buffer-trim', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of received DATA transfers that had
                buffer trim failures
                ''',
                'data_xfer_rcv_fail_buffer_trim',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-xfer-rcv-fail-snd-una-out-of-sync', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of received DATA transfers that had
                failures because the send path was out of sync
                ''',
                'data_xfer_rcv_fail_snd_una_out_of_sync',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-xfer-rcv-success', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successfully received DATA transfers
                ''',
                'data_xfer_rcv_success',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-xfer-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful DATA transfers
                ''',
                'data_xfer_send',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-xfer-send-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failed DATA transfers
                ''',
                'data_xfer_send_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-xfer-send-iov-alloc', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of data transfer msgs., that required new
                IOV's to be allocated
                ''',
                'data_xfer_send_iov_alloc',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('data-xfer-send-total', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Amount of data transferred
                ''',
                'data_xfer_send_total',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nack-rcv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of received NACK messages
                ''',
                'nack_rcv',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nack-rcv-fail-data-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of received NACK messages that had
                failures when sending data in response to the
                NACK
                ''',
                'nack_rcv_fail_data_send',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nack-rcv-success', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successfully received NACK messages
                ''',
                'nack_rcv_success',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nack-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful NACK messages
                ''',
                'nack_send',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('nack-send-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failed NACK messages
                ''',
                'nack_send_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('seg-instr-rcv', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of received Segmentation instruction
                messages
                ''',
                'seg_instr_rcv',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('seg-instr-rcv-fail-buffer-trim', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of received Segmentation instructions
                that had buffer trim failures
                ''',
                'seg_instr_rcv_fail_buffer_trim',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('seg-instr-rcv-fail-tcp-process', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of received Segmentation instructions
                that had failures during TCP processing
                ''',
                'seg_instr_rcv_fail_tcp_process',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('seg-instr-rcv-success', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successfully received Segmentation
                instruction messages
                ''',
                'seg_instr_rcv_success',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('seg-instr-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of successful Segmentation instruction
                messages
                ''',
                'seg_instr_send',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('seg-instr-send-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failed Segmentation instruction
                messages
                ''',
                'seg_instr_send_drop',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('seg-instr-send-units', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of segement units transferred via the
                successful Segmentation instruction messages
                ''',
                'seg_instr_send_units',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'snd-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ID of TCP connection
                ''',
                'id',
                'Cisco-IOS-XR-ip-tcp-oper', True),
            _MetaInfoClassMember('internal-ack-drops-immediate-match', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of iACKs not held because of an immediate
                match
                ''',
                'internal_ack_drops_immediate_match',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('internal-ack-drops-initsync-first-phase', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of iACKs dropped because 1st phase of
                init-sync is in progress
                ''',
                'internal_ack_drops_initsync_first_phase',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('internal-ack-drops-not-replicated', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of iACKs dropped because session is not
                replicated
                ''',
                'internal_ack_drops_not_replicated',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('internal-ack-drops-stale', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of stale iACKs dropped
                ''',
                'internal_ack_drops_stale',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('last-cleared-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time of last clear (in seconds since 1st Jan
                1970 00:00:00)
                ''',
                'last_cleared_time',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-timers-nsr-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                no. of times nsr went down
                ''',
                'number_of_timers_nsr_down',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-times-nsr-disabled', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                no. of times nsr was disabled
                ''',
                'number_of_times_nsr_disabled',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-times-nsr-fail-over', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                no. of times fail-over occured
                ''',
                'number_of_times_nsr_fail_over',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('number-of-times-nsr-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                no. of times nsr went up
                ''',
                'number_of_times_nsr_up',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('pcb', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PCB Address
                ''',
                'pcb',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('snd-counters', REFERENCE_CLASS, 'SndCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession.SndCounters', 
                [], [], 
                '''                Send path counters for the PCB
                ''',
                'snd_counters',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'statistic-session',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Statistics.StatisticSessions' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Statistics.StatisticSessions',
            False, 
            [
            _MetaInfoClassMember('statistic-session', REFERENCE_LIST, 'StatisticSession' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession', 
                [], [], 
                '''                showing statistic information of TCP
                connections
                ''',
                'statistic_session',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'statistic-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node.Statistics' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node.Statistics',
            False, 
            [
            _MetaInfoClassMember('statistic-clients', REFERENCE_CLASS, 'StatisticClients' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Statistics.StatisticClients', 
                [], [], 
                '''                Table listing NSR connections for which
                statistic information is provided
                ''',
                'statistic_clients',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('statistic-sessions', REFERENCE_CLASS, 'StatisticSessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Statistics.StatisticSessions', 
                [], [], 
                '''                Table listing NSR connections for which
                statistic information is provided
                ''',
                'statistic_sessions',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('statistic-sets', REFERENCE_CLASS, 'StatisticSets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Statistics.StatisticSets', 
                [], [], 
                '''                Table listing NSR connections for which
                statistic information is provided
                ''',
                'statistic_sets',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Statistics.Summary', 
                [], [], 
                '''                Summary statistics across all NSR connections
                ''',
                'summary',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Describing a location
                ''',
                'id',
                'Cisco-IOS-XR-ip-tcp-oper', True),
            _MetaInfoClassMember('client', REFERENCE_CLASS, 'Client' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Client', 
                [], [], 
                '''                Information about TCP NSR Client
                ''',
                'client',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Session', 
                [], [], 
                '''                Information about TCP NSR Sessions
                ''',
                'session',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('session-set', REFERENCE_CLASS, 'SessionSet' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.SessionSet', 
                [], [], 
                '''                Information about TCP NSR Session Sets
                ''',
                'session_set',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node.Statistics', 
                [], [], 
                '''                Statis Information about TCP NSR connections
                ''',
                'statistics',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr.Nodes' : {
        'meta_info' : _MetaInfoClass('TcpNsr.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes.Node', 
                [], [], 
                '''                Information about a single node
                ''',
                'node',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
    'TcpNsr' : {
        'meta_info' : _MetaInfoClass('TcpNsr',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper', 'TcpNsr.Nodes', 
                [], [], 
                '''                Table of information about all nodes present on
                the system
                ''',
                'nodes',
                'Cisco-IOS-XR-ip-tcp-oper', False),
            ],
            'Cisco-IOS-XR-ip-tcp-oper',
            'tcp-nsr',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-tcp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper'
        ),
    },
}
_meta_table['TcpConnection.Nodes.Node.Statistics.Clients.Client']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.Statistics.Clients']['meta_info']
_meta_table['TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.ReadIoCounts']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb']['meta_info']
_meta_table['TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.WriteIoCounts']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb']['meta_info']
_meta_table['TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb']['meta_info']
_meta_table['TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.Statistics.Pcbs']['meta_info']
_meta_table['TcpConnection.Nodes.Node.Statistics.Clients']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.Statistics']['meta_info']
_meta_table['TcpConnection.Nodes.Node.Statistics.Pcbs']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.Statistics']['meta_info']
_meta_table['TcpConnection.Nodes.Node.Statistics.Summary']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.Statistics']['meta_info']
_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.PacketType']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter']['meta_info']
_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.RemoteAddress']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter']['meta_info']
_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.LocalAddress']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter']['meta_info']
_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Options']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb']['meta_info']
_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.LptsFlags']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb']['meta_info']
_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.AcceptMask']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb']['meta_info']
_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb']['meta_info']
_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common']['meta_info']
_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.LocalAddress']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId']['meta_info']
_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.ForeignAddress']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId']['meta_info']
_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId']['meta_info']
_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType']['meta_info']
_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes']['meta_info']
_meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.ExtendedInformation']['meta_info']
_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.LocalAddress']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation']['meta_info']
_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ForeignAddress']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation']['meta_info']
_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketOptionFlags']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation']['meta_info']
_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketStateFlags']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation']['meta_info']
_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FeatureFlags']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation']['meta_info']
_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.StateFlags']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation']['meta_info']
_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.RequestFlags']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation']['meta_info']
_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ReceiveBufStateFlags']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation']['meta_info']
_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendBufStateFlags']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation']['meta_info']
_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.Timer']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation']['meta_info']
_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SackBlk']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation']['meta_info']
_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendSackHole']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation']['meta_info']
_meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.DetailInformations']['meta_info']
_meta_table['TcpConnection.Nodes.Node.BriefInformations.BriefInformation.LocalAddress']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.BriefInformations.BriefInformation']['meta_info']
_meta_table['TcpConnection.Nodes.Node.BriefInformations.BriefInformation.ForeignAddress']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.BriefInformations.BriefInformation']['meta_info']
_meta_table['TcpConnection.Nodes.Node.BriefInformations.BriefInformation']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node.BriefInformations']['meta_info']
_meta_table['TcpConnection.Nodes.Node.Statistics']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node']['meta_info']
_meta_table['TcpConnection.Nodes.Node.ExtendedInformation']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node']['meta_info']
_meta_table['TcpConnection.Nodes.Node.DetailInformations']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node']['meta_info']
_meta_table['TcpConnection.Nodes.Node.BriefInformations']['meta_info'].parent =_meta_table['TcpConnection.Nodes.Node']['meta_info']
_meta_table['TcpConnection.Nodes.Node']['meta_info'].parent =_meta_table['TcpConnection.Nodes']['meta_info']
_meta_table['TcpConnection.Nodes']['meta_info'].parent =_meta_table['TcpConnection']['meta_info']
_meta_table['Tcp.Nodes.Node.Statistics.Ipv4Traffic']['meta_info'].parent =_meta_table['Tcp.Nodes.Node.Statistics']['meta_info']
_meta_table['Tcp.Nodes.Node.Statistics.Ipv6Traffic']['meta_info'].parent =_meta_table['Tcp.Nodes.Node.Statistics']['meta_info']
_meta_table['Tcp.Nodes.Node.Statistics']['meta_info'].parent =_meta_table['Tcp.Nodes.Node']['meta_info']
_meta_table['Tcp.Nodes.Node']['meta_info'].parent =_meta_table['Tcp.Nodes']['meta_info']
_meta_table['Tcp.Nodes']['meta_info'].parent =_meta_table['Tcp']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Session.BriefSessions.BriefSession']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Session.BriefSessions']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.SetInformation']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.PacketHoldQueue']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.InternalAckHoldQueue']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Session.DetailSessions']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Session.BriefSessions']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Session']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Session.DetailSessions']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Session']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Client.DetailClients.DetailClient']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Client.DetailClients']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Client.BriefClients.BriefClient']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Client.BriefClients']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Client.DetailClients']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Client']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Client.BriefClients']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Client']['meta_info']
_meta_table['TcpNsr.Nodes.Node.SessionSet.DetailSets.DetailSet']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.SessionSet.DetailSets']['meta_info']
_meta_table['TcpNsr.Nodes.Node.SessionSet.BriefSets.BriefSet']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.SessionSet.BriefSets']['meta_info']
_meta_table['TcpNsr.Nodes.Node.SessionSet.DetailSets']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.SessionSet']['meta_info']
_meta_table['TcpNsr.Nodes.Node.SessionSet.BriefSets']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.SessionSet']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.Common']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Statistics.Summary.SndCounters']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.AggrOnly']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Statistics.Summary.SndCounters']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.Common']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.AggrOnly']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Statistics.Summary.SndCounters']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Statistics.Summary']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Statistics.Summary']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Statistics.Summary.NotificationStatistic']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Statistics.Summary']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient.NotificationStatistic']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Statistics.StatisticClients']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Statistics.StatisticSets.StatisticSet']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Statistics.StatisticSets']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession.SndCounters']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Statistics.StatisticSessions']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Statistics.Summary']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Statistics']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Statistics.StatisticClients']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Statistics']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Statistics.StatisticSets']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Statistics']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Statistics.StatisticSessions']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node.Statistics']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Session']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Client']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node']['meta_info']
_meta_table['TcpNsr.Nodes.Node.SessionSet']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node']['meta_info']
_meta_table['TcpNsr.Nodes.Node.Statistics']['meta_info'].parent =_meta_table['TcpNsr.Nodes.Node']['meta_info']
_meta_table['TcpNsr.Nodes.Node']['meta_info'].parent =_meta_table['TcpNsr.Nodes']['meta_info']
_meta_table['TcpNsr.Nodes']['meta_info'].parent =_meta_table['TcpNsr']['meta_info']
