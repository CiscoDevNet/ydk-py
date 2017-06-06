


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MessageTypeIcmpEnum' : _MetaInfoEnum('MessageTypeIcmpEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper',
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
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'MessageTypeIcmpEnum' : _MetaInfoEnum('MessageTypeIcmpEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper',
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
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'LptsPcbQueryEnum' : _MetaInfoEnum('LptsPcbQueryEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper',
        {
            'all':'all',
            'static-policy':'static_policy',
            'interface':'interface',
            'packet':'packet',
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'PacketEnum' : _MetaInfoEnum('PacketEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper',
        {
            'icmp':'icmp',
            'icm-pv6':'icm_pv6',
            'igmp':'igmp',
            'unknown':'unknown',
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'MessageTypeIcmpv6Enum' : _MetaInfoEnum('MessageTypeIcmpv6Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper',
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
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'MessageTypeIgmpEnum' : _MetaInfoEnum('MessageTypeIgmpEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper',
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
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'UdpAddressFamilyEnum' : _MetaInfoEnum('UdpAddressFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'AddrFamilyEnum' : _MetaInfoEnum('AddrFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper',
        {
            'unspecified':'unspecified',
            'local':'local',
            'inet':'inet',
            'implink':'implink',
            'pup':'pup',
            'chaos':'chaos',
            'ns':'ns',
            'iso':'iso',
            'ecma':'ecma',
            'data-kit':'data_kit',
            'ccitt':'ccitt',
            'sna':'sna',
            'de-cnet':'de_cnet',
            'dli':'dli',
            'lat':'lat',
            'hylink':'hylink',
            'appletalk':'appletalk',
            'route':'route',
            'link':'link',
            'pseudo-xtp':'pseudo_xtp',
            'coip':'coip',
            'cnt':'cnt',
            'pseudo-rtip':'pseudo_rtip',
            'ipx':'ipx',
            'sip':'sip',
            'pseudo-pip':'pseudo_pip',
            'inet6':'inet6',
            'snap':'snap',
            'clnl':'clnl',
            'chdlc':'chdlc',
            'ppp':'ppp',
            'host-cas':'host_cas',
            'dsp':'dsp',
            'sap':'sap',
            'atm':'atm',
            'fr':'fr',
            'mso':'mso',
            'dchan':'dchan',
            'cas':'cas',
            'nat':'nat',
            'ether':'ether',
            'srp':'srp',
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'MessageTypeIcmpv6Enum' : _MetaInfoEnum('MessageTypeIcmpv6Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper',
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
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'MessageTypeIgmpEnum' : _MetaInfoEnum('MessageTypeIgmpEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper',
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
        }, 'Cisco-IOS-XR-ip-udp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper']),
    'Udp.Nodes.Node.Statistics.Ipv4Traffic' : {
        'meta_info' : _MetaInfoClass('Udp.Nodes.Node.Statistics.Ipv4Traffic',
            False, 
            [
            _MetaInfoClassMember('udp-bad-length-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                UDP bad length
                ''',
                'udp_bad_length_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-checksum-error-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                UDP Checksum Errors
                ''',
                'udp_checksum_error_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                UDP drop for other reason
                ''',
                'udp_dropped_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-input-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                UDP Received
                ''',
                'udp_input_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-no-port-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                UDP No Port
                ''',
                'udp_no_port_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-output-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                UDP Transmitted
                ''',
                'udp_output_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'ipv4-traffic',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'Udp.Nodes.Node.Statistics.Ipv6Traffic' : {
        'meta_info' : _MetaInfoClass('Udp.Nodes.Node.Statistics.Ipv6Traffic',
            False, 
            [
            _MetaInfoClassMember('udp-bad-length-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                UDP bad length
                ''',
                'udp_bad_length_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-checksum-error-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                UDP Checksum Errors
                ''',
                'udp_checksum_error_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                UDP drop for other reason
                ''',
                'udp_dropped_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-input-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                UDP Received
                ''',
                'udp_input_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-no-port-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                UDP No Port
                ''',
                'udp_no_port_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('udp-output-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                UDP Transmitted
                ''',
                'udp_output_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'ipv6-traffic',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'Udp.Nodes.Node.Statistics' : {
        'meta_info' : _MetaInfoClass('Udp.Nodes.Node.Statistics',
            False, 
            [
            _MetaInfoClassMember('ipv4-traffic', REFERENCE_CLASS, 'Ipv4Traffic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'Udp.Nodes.Node.Statistics.Ipv4Traffic', 
                [], [], 
                '''                UDP Traffic statistics for IPv4
                ''',
                'ipv4_traffic',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-traffic', REFERENCE_CLASS, 'Ipv6Traffic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'Udp.Nodes.Node.Statistics.Ipv6Traffic', 
                [], [], 
                '''                UDP Traffic statistics for IPv6
                ''',
                'ipv6_traffic',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'Udp.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Udp.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-ip-udp-oper', True),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'Udp.Nodes.Node.Statistics', 
                [], [], 
                '''                Statistical UDP operational data for a node
                ''',
                'statistics',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'Udp.Nodes' : {
        'meta_info' : _MetaInfoClass('Udp.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'Udp.Nodes.Node', 
                [], [], 
                '''                UDP operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'Udp' : {
        'meta_info' : _MetaInfoClass('Udp',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'Udp.Nodes', 
                [], [], 
                '''                Node-specific UDP operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'udp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Statistics.Clients.Client' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Statistics.Clients.Client',
            False, 
            [
            _MetaInfoClassMember('client-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Displaying client's aggregated statistics
                ''',
                'client_id',
                'Cisco-IOS-XR-ip-udp-oper', True),
            _MetaInfoClassMember('client-jid', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Job ID of the transport client
                ''',
                'client_jid',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('client-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 21)], [], 
                '''                Transport client name
                ''',
                'client_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total IPv4 packets received from client
                ''',
                'ipv4_received_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-sent-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total IPv4 packets sent to client
                ''',
                'ipv4_sent_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total IPv6 packets received from app
                ''',
                'ipv6_received_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-sent-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total IPv6 packets sent to app
                ''',
                'ipv6_sent_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'client',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Statistics.Clients' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Statistics.Clients',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_LIST, 'Client' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Statistics.Clients.Client', 
                [], [], 
                '''                Describing Client ID
                ''',
                'client',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'clients',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Statistics.Summary' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Statistics.Summary',
            False, 
            [
            _MetaInfoClassMember('cloned-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total cloned packets
                ''',
                'cloned_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('failed-clone-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total failed cloned packets
                ''',
                'failed_clone_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('forward-broadcast-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total forwarding broadcast packets
                ''',
                'forward_broadcast_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('received-bad-checksum-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets received has bad checksum
                ''',
                'received_bad_checksum_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('received-drop-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets dropped for other reasons
                ''',
                'received_drop_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('received-no-port-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets received when no wild listener
                ''',
                'received_no_port_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('received-too-short-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets received is too short
                ''',
                'received_too_short_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('received-total-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total packets received
                ''',
                'received_total_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('sent-error-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total send erorr packets
                ''',
                'sent_error_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('sent-total-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total packets sent
                ''',
                'sent_total_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send',
            False, 
            [
            _MetaInfoClassMember('failed-queued-net-io-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets failed getting queued to network (NetIO)
                ''',
                'failed_queued_net_io_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('failed-queued-network-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets failed getting queued to network (v4/v6
                IO)
                ''',
                'failed_queued_network_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('received-application-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes received from application
                ''',
                'received_application_bytes',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('received-xipc-pulses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                XIPC pulses received from application
                ''',
                'received_xipc_pulses',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('sent-net-io-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets sent to network (NetIO)
                ''',
                'sent_net_io_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('sent-network-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets sent to network (v4/v6 IO)
                ''',
                'sent_network_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'send',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive',
            False, 
            [
            _MetaInfoClassMember('failed-queued-application-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets failed queued to application
                ''',
                'failed_queued_application_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('failed-queued-application-socket-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packet that couldn't be queued to application.on
                socket
                ''',
                'failed_queued_application_socket_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('queued-application-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets queued to application
                ''',
                'queued_application_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('queued-application-socket-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets queued to application on socket
                ''',
                'queued_application_socket_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('received-network-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets received from network
                ''',
                'received_network_packets',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'receive',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic',
            False, 
            [
            _MetaInfoClassMember('pcb-address', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Protocol Control Block address
                ''',
                'pcb_address',
                'Cisco-IOS-XR-ip-udp-oper', True),
            _MetaInfoClassMember('is-paw-socket', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if paw socket
                ''',
                'is_paw_socket',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('receive', REFERENCE_CLASS, 'Receive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive', 
                [], [], 
                '''                UDP receive statistics
                ''',
                'receive',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('send', REFERENCE_CLASS, 'Send' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send', 
                [], [], 
                '''                UDP send statistics
                ''',
                'send',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF ID
                ''',
                'vrf_id',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'pcb-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Statistics.PcbStatistics' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Statistics.PcbStatistics',
            False, 
            [
            _MetaInfoClassMember('pcb-statistic', REFERENCE_LIST, 'PcbStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic', 
                [], [], 
                '''                Satistics associated with a particular PCB
                ''',
                'pcb_statistic',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'pcb-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Statistics' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Statistics',
            False, 
            [
            _MetaInfoClassMember('clients', REFERENCE_CLASS, 'Clients' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Statistics.Clients', 
                [], [], 
                '''                Table listing clients
                ''',
                'clients',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('pcb-statistics', REFERENCE_CLASS, 'PcbStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Statistics.PcbStatistics', 
                [], [], 
                '''                Table listing the UDP connections for which
                statistics are provided
                ''',
                'pcb_statistics',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Statistics.Summary', 
                [], [], 
                '''                Summary statistics across all UDP connections
                ''',
                'summary',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'AddrFamilyEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'AddrFamilyEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'foreign-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options',
            False, 
            [
            _MetaInfoClassMember('is-ip-sla', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IP SLA
                ''',
                'is_ip_sla',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('is-receive-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Receive filter enabled
                ''',
                'is_receive_filter',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'options',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags',
            False, 
            [
            _MetaInfoClassMember('is-ignore-vrf-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ignore VRF Filter
                ''',
                'is_ignore_vrf_filter',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('is-local-address-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Sent drop packets
                ''',
                'is_local_address_ignore',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('is-pcb-bound', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PCB bound
                ''',
                'is_pcb_bound',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'lpts-flags',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask',
            False, 
            [
            _MetaInfoClassMember('is-interface', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set interface
                ''',
                'is_interface',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('is-local-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set Local Address
                ''',
                'is_local_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('is-local-port', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set Local Port
                ''',
                'is_local_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('is-packet-type', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set packet type
                ''',
                'is_packet_type',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('is-remote-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set Remote address
                ''',
                'is_remote_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('is-remote-port', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set Remote Port
                ''',
                'is_remote_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'accept-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType',
            False, 
            [
            _MetaInfoClassMember('icm-pv6-message-type', REFERENCE_ENUM_CLASS, 'MessageTypeIcmpv6Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'MessageTypeIcmpv6Enum', 
                [], [], 
                '''                ICMPv6 message type
                ''',
                'icm_pv6_message_type',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('icmp-message-type', REFERENCE_ENUM_CLASS, 'MessageTypeIcmpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'MessageTypeIcmpEnum', 
                [], [], 
                '''                ICMP message type
                ''',
                'icmp_message_type',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('igmp-message-type', REFERENCE_ENUM_CLASS, 'MessageTypeIgmpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'MessageTypeIgmpEnum', 
                [], [], 
                '''                IGMP message type
                ''',
                'igmp_message_type',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('message-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message type in number
                ''',
                'message_id',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'PacketEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'PacketEnum', 
                [], [], 
                '''                Type
                ''',
                'type',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'packet-type',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'AddrFamilyEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'remote-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'AddrFamilyEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter',
            False, 
            [
            _MetaInfoClassMember('flow-types-info', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                flow information
                ''',
                'flow_types_info',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress', 
                [], [], 
                '''                Local address
                ''',
                'local_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('local-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local address length
                ''',
                'local_length',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('packet-type', REFERENCE_CLASS, 'PacketType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType', 
                [], [], 
                '''                Protocol-specific packet type
                ''',
                'packet_type',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Priority
                ''',
                'priority',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('receive-local-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Receive Local port
                ''',
                'receive_local_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('receive-remote-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Receive Remote port
                ''',
                'receive_remote_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('remote-address', REFERENCE_CLASS, 'RemoteAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress', 
                [], [], 
                '''                Remote address
                ''',
                'remote_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('remote-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remote address length
                ''',
                'remote_length',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Minimum TTL
                ''',
                'ttl',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb',
            False, 
            [
            _MetaInfoClassMember('accept-mask', REFERENCE_CLASS, 'AcceptMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask', 
                [], [], 
                '''                AcceptMask
                ''',
                'accept_mask',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('filter', REFERENCE_LIST, 'Filter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter', 
                [], [], 
                '''                Interface Filters
                ''',
                'filter',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('flow-types-info', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                flow information
                ''',
                'flow_types_info',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('lpts-flags', REFERENCE_CLASS, 'LptsFlags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags', 
                [], [], 
                '''                LPTS flags
                ''',
                'lpts_flags',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('options', REFERENCE_CLASS, 'Options' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options', 
                [], [], 
                '''                Receive options
                ''',
                'options',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Minimum TTL
                ''',
                'ttl',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'lpts-pcb',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'AddrFamilyEnum', 
                [], [], 
                '''                Address Family
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('lpts-pcb', REFERENCE_CLASS, 'LptsPcb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb', 
                [], [], 
                '''                LPTS PCB information
                ''',
                'lpts_pcb',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'common',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb',
            False, 
            [
            _MetaInfoClassMember('pcb-address', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                PCB address
                ''',
                'pcb_address',
                'Cisco-IOS-XR-ip-udp-oper', True),
            _MetaInfoClassMember('common', REFERENCE_CLASS, 'Common' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common', 
                [], [], 
                '''                Common PCB information
                ''',
                'common',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('foreign-address', REFERENCE_CLASS, 'ForeignAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress', 
                [], [], 
                '''                Remote IP address
                ''',
                'foreign_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('foreign-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remote port
                ''',
                'foreign_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('l4-protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Layer 4 protocol
                ''',
                'l4_protocol',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress', 
                [], [], 
                '''                Local IP address
                ''',
                'local_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('local-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local port
                ''',
                'local_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'pcb',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs',
            False, 
            [
            _MetaInfoClassMember('pcb', REFERENCE_LIST, 'Pcb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb', 
                [], [], 
                '''                A PCB information
                ''',
                'pcb',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'pcbs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries.Query' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries.Query',
            False, 
            [
            _MetaInfoClassMember('query-name', REFERENCE_ENUM_CLASS, 'LptsPcbQueryEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'LptsPcbQueryEnum', 
                [], [], 
                '''                Query option
                ''',
                'query_name',
                'Cisco-IOS-XR-ip-udp-oper', True),
            _MetaInfoClassMember('pcbs', REFERENCE_CLASS, 'Pcbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs', 
                [], [], 
                '''                List of PCBs
                ''',
                'pcbs',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'query',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts.Queries' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts.Queries',
            False, 
            [
            _MetaInfoClassMember('query', REFERENCE_LIST, 'Query' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries.Query', 
                [], [], 
                '''                Query option
                ''',
                'query',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'queries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.Lpts' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.Lpts',
            False, 
            [
            _MetaInfoClassMember('queries', REFERENCE_CLASS, 'Queries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts.Queries', 
                [], [], 
                '''                List of query options
                ''',
                'queries',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'lpts',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'UdpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpAddressFamilyEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'UdpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpAddressFamilyEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'foreign-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.PcbDetails.PcbDetail' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.PcbDetails.PcbDetail',
            False, 
            [
            _MetaInfoClassMember('pcb-address', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Protocol Control Block address
                ''',
                'pcb_address',
                'Cisco-IOS-XR-ip-udp-oper', True),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'UdpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('foreign-address', REFERENCE_CLASS, 'ForeignAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress', 
                [], [], 
                '''                Foreign address
                ''',
                'foreign_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('foreign-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Foreign port
                ''',
                'foreign_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress', 
                [], [], 
                '''                Local address
                ''',
                'local_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('local-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local port
                ''',
                'local_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('local-process-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ID of local process
                ''',
                'local_process_id',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('receive-queue', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Receive queue count
                ''',
                'receive_queue',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('send-queue', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Send queue count
                ''',
                'send_queue',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF ID
                ''',
                'vrf_id',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'pcb-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.PcbDetails' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.PcbDetails',
            False, 
            [
            _MetaInfoClassMember('pcb-detail', REFERENCE_LIST, 'PcbDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.PcbDetails.PcbDetail', 
                [], [], 
                '''                Detail information about a UDP connection
                ''',
                'pcb_detail',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'pcb-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'UdpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpAddressFamilyEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'UdpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpAddressFamilyEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'foreign-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.PcbBriefs.PcbBrief' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.PcbBriefs.PcbBrief',
            False, 
            [
            _MetaInfoClassMember('pcb-address', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Protocol Control Block address
                ''',
                'pcb_address',
                'Cisco-IOS-XR-ip-udp-oper', True),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'UdpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('foreign-address', REFERENCE_CLASS, 'ForeignAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress', 
                [], [], 
                '''                Foreign address
                ''',
                'foreign_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('foreign-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Foreign port
                ''',
                'foreign_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress', 
                [], [], 
                '''                Local address
                ''',
                'local_address',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('local-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local port
                ''',
                'local_port',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('receive-queue', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Receive queue count
                ''',
                'receive_queue',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('send-queue', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Send queue count
                ''',
                'send_queue',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF ID
                ''',
                'vrf_id',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'pcb-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node.PcbBriefs' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node.PcbBriefs',
            False, 
            [
            _MetaInfoClassMember('pcb-brief', REFERENCE_LIST, 'PcbBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.PcbBriefs.PcbBrief', 
                [], [], 
                '''                Brief information about a UDP connection
                ''',
                'pcb_brief',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'pcb-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-ip-udp-oper', True),
            _MetaInfoClassMember('lpts', REFERENCE_CLASS, 'Lpts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Lpts', 
                [], [], 
                '''                LPTS statistical data
                ''',
                'lpts',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('pcb-briefs', REFERENCE_CLASS, 'PcbBriefs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.PcbBriefs', 
                [], [], 
                '''                Brief information for list of UDP connections.
                ''',
                'pcb_briefs',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('pcb-details', REFERENCE_CLASS, 'PcbDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.PcbDetails', 
                [], [], 
                '''                Detail information for list of UDP connections
                .
                ''',
                'pcb_details',
                'Cisco-IOS-XR-ip-udp-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node.Statistics', 
                [], [], 
                '''                Statistics of UDP connections
                ''',
                'statistics',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection.Nodes' : {
        'meta_info' : _MetaInfoClass('UdpConnection.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes.Node', 
                [], [], 
                '''                Information about a particular node
                ''',
                'node',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
    'UdpConnection' : {
        'meta_info' : _MetaInfoClass('UdpConnection',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpConnection.Nodes', 
                [], [], 
                '''                List of UDP connections nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-ip-udp-oper', False),
            ],
            'Cisco-IOS-XR-ip-udp-oper',
            'udp-connection',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper'
        ),
    },
}
_meta_table['Udp.Nodes.Node.Statistics.Ipv4Traffic']['meta_info'].parent =_meta_table['Udp.Nodes.Node.Statistics']['meta_info']
_meta_table['Udp.Nodes.Node.Statistics.Ipv6Traffic']['meta_info'].parent =_meta_table['Udp.Nodes.Node.Statistics']['meta_info']
_meta_table['Udp.Nodes.Node.Statistics']['meta_info'].parent =_meta_table['Udp.Nodes.Node']['meta_info']
_meta_table['Udp.Nodes.Node']['meta_info'].parent =_meta_table['Udp.Nodes']['meta_info']
_meta_table['Udp.Nodes']['meta_info'].parent =_meta_table['Udp']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Statistics.Clients.Client']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Statistics.Clients']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Statistics.Clients']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Statistics']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Statistics.Summary']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Statistics']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Statistics']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts.Queries']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts.Queries']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.Lpts']['meta_info']
_meta_table['UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.PcbDetails.PcbDetail']['meta_info']
_meta_table['UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.PcbDetails.PcbDetail']['meta_info']
_meta_table['UdpConnection.Nodes.Node.PcbDetails.PcbDetail']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.PcbDetails']['meta_info']
_meta_table['UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.PcbBriefs.PcbBrief']['meta_info']
_meta_table['UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.PcbBriefs.PcbBrief']['meta_info']
_meta_table['UdpConnection.Nodes.Node.PcbBriefs.PcbBrief']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node.PcbBriefs']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Statistics']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node']['meta_info']
_meta_table['UdpConnection.Nodes.Node.Lpts']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node']['meta_info']
_meta_table['UdpConnection.Nodes.Node.PcbDetails']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node']['meta_info']
_meta_table['UdpConnection.Nodes.Node.PcbBriefs']['meta_info'].parent =_meta_table['UdpConnection.Nodes.Node']['meta_info']
_meta_table['UdpConnection.Nodes.Node']['meta_info'].parent =_meta_table['UdpConnection.Nodes']['meta_info']
_meta_table['UdpConnection.Nodes']['meta_info'].parent =_meta_table['UdpConnection']['meta_info']
