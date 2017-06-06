


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6' : {
        'meta_info' : _MetaInfoClass('Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6',
            False, 
            [
            _MetaInfoClassMember('bad-header-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bad Header Packets
                ''',
                'bad_header_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('bad-source-address-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bad Source Address Packets
                ''',
                'bad_source_address_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('format-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Format Errors
                ''',
                'format_errors',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('forwarded-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets Forwarded
                ''',
                'forwarded_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('fragment-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fragmented Packet Count
                ''',
                'fragment_count',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('fragment-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fragment Failures
                ''',
                'fragment_failures',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('fragmented-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets Fragmented
                ''',
                'fragmented_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('fragments', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fragments
                ''',
                'fragments',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('generated-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets Output
                ''',
                'generated_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('hop-count-exceeded-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hop Count Exceeded Packets
                ''',
                'hop_count_exceeded_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('lisp-decap-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lisp Decap errors
                ''',
                'lisp_decap_errors',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('lisp-encap-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lisp Encap errors
                ''',
                'lisp_encap_errors',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('lisp-v4-decap-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lisp IPv4 Decapped packets
                ''',
                'lisp_v4_decap_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('lisp-v4-encap-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lisp IPv4 Encapped packets
                ''',
                'lisp_v4_encap_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('lisp-v6-decap-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lisp IPv6 Decapped packets
                ''',
                'lisp_v6_decap_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('lisp-v6-encap-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lisp IPv6 Encapped packets
                ''',
                'lisp_v6_encap_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('local-destination-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Destination Packets
                ''',
                'local_destination_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('miscellaneous-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Misc. drops
                ''',
                'miscellaneous_drops',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('no-route-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No Route Packets
                ''',
                'no_route_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('reassembled-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reassembled Packets
                ''',
                'reassembled_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('reassembly-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reassembly Failures
                ''',
                'reassembly_failures',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('reassembly-maximum-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reassembly Reach Maximum Drop
                ''',
                'reassembly_maximum_drops',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('reassembly-timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reassembly Timeouts
                ''',
                'reassembly_timeouts',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-multicast-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Multicast In
                ''',
                'received_multicast_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-multicast-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Multicast Out
                ''',
                'sent_multicast_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('source-routed-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets Source Routed
                ''',
                'source_routed_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('too-big-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packet Too Big
                ''',
                'too_big_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('total-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Packets
                ''',
                'total_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('truncated-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Truncated Packets
                ''',
                'truncated_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('unknown-option-type-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unknown Option Type Packets
                ''',
                'unknown_option_type_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('unknown-protocol-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unknown Protocol Packets
                ''',
                'unknown_protocol_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-io-oper',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper'
        ),
    },
    'Ipv6Io.Nodes.Node.Statistics.Traffic.Icmp' : {
        'meta_info' : _MetaInfoClass('Ipv6Io.Nodes.Node.Statistics.Traffic.Icmp',
            False, 
            [
            _MetaInfoClassMember('checksum-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Checksum Errors
                ''',
                'checksum_error_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('output-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Transmitted
                ''',
                'output_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-echo-reply-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Echo Reply Received
                ''',
                'received_echo_reply_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-echo-request-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Echo Request Received
                ''',
                'received_echo_request_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-hop-count-expired-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Hop Count Expired Received
                ''',
                'received_hop_count_expired_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-parameter-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Parameter Error Messages Received
                ''',
                'received_parameter_error_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-parameter-header-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Parameter Next Header Messages Received
                ''',
                'received_parameter_header_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-parameter-option-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Parameter Option Problem Received
                ''',
                'received_parameter_option_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-parameter-unknown-type-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Parameter Unknown Type Messages Received
                ''',
                'received_parameter_unknown_type_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-reassembly-timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Reassembly Timeouts
                ''',
                'received_reassembly_timeouts',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-too-big-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Too Big Messages Received
                ''',
                'received_too_big_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-unknown-timeout-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Unknown Timeout Messages Received
                ''',
                'received_unknown_timeout_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-unreachable-address-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Addr Unreachable Received
                ''',
                'received_unreachable_address_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-unreachable-admin-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Admin Unreachable Received
                ''',
                'received_unreachable_admin_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-unreachable-neighbor-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Host Unreachable Received
                ''',
                'received_unreachable_neighbor_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-unreachable-port-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Port Unreachable Received
                ''',
                'received_unreachable_port_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-unreachable-routing-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Route Unreachable Received
                ''',
                'received_unreachable_routing_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-unreachable-unknown-type-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Unreachable Unknown Messages Received
                ''',
                'received_unreachable_unknown_type_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-echo-reply-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Echo Reply Sent
                ''',
                'sent_echo_reply_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-echo-request-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Echo Request Sent
                ''',
                'sent_echo_request_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-hop-count-expired-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Hop Count Expired Sent
                ''',
                'sent_hop_count_expired_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-parameter-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Parameter Error Messages Sent
                ''',
                'sent_parameter_error_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-parameter-header-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Parameter Next Header Messages Sent
                ''',
                'sent_parameter_header_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-parameter-option-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Parameter Option Messages Sent
                ''',
                'sent_parameter_option_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-parameter-unknown-type-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Parameter Unknown Type Messages Sent
                ''',
                'sent_parameter_unknown_type_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-rate-limited-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Sent Packets Ratelimited
                ''',
                'sent_rate_limited_packets',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-reassembly-timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Reassembly Timeouts
                ''',
                'sent_reassembly_timeouts',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-too-big-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Too Big Messages Sent
                ''',
                'sent_too_big_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-unknown-timeout-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Unknown Timeout Messages Sent
                ''',
                'sent_unknown_timeout_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-unreachable-address-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Addr Unreachable Sent
                ''',
                'sent_unreachable_address_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-unreachable-admin-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Admin Unreachable Sent
                ''',
                'sent_unreachable_admin_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-unreachable-neighbor-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Host Unreachable Sent
                ''',
                'sent_unreachable_neighbor_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-unreachable-port-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Port Unreachable Sent
                ''',
                'sent_unreachable_port_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-unreachable-routing-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Route Unreachable Sent
                ''',
                'sent_unreachable_routing_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-unreachable-unknown-type-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Unreachable Unknown Messages Sent
                ''',
                'sent_unreachable_unknown_type_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('too-short-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Too Short Errors
                ''',
                'too_short_error_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('total-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Received
                ''',
                'total_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('unknown-error-type-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Unknown Error
                ''',
                'unknown_error_type_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-io-oper',
            'icmp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper'
        ),
    },
    'Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6NodeDiscovery' : {
        'meta_info' : _MetaInfoClass('Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6NodeDiscovery',
            False, 
            [
            _MetaInfoClassMember('received-neighbor-advertisement-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Neighbor Advertisements Received
                ''',
                'received_neighbor_advertisement_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-neighbor-solicitation-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Neighbor Solicitations Received
                ''',
                'received_neighbor_solicitation_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-redirect-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Redirect Received
                ''',
                'received_redirect_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-router-advertisement-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Router Advertisements Received
                ''',
                'received_router_advertisement_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('received-router-solicitation-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Router Solicitations Received
                ''',
                'received_router_solicitation_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-neighbor-advertisement-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Neighbor Advertisements Sent
                ''',
                'sent_neighbor_advertisement_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-neighbor-solicitation-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Neighbor Solicitations Sent
                ''',
                'sent_neighbor_solicitation_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-redirect-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Redirect Sent
                ''',
                'sent_redirect_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-router-advertisement-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Router Advertisements Sent
                ''',
                'sent_router_advertisement_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('sent-router-solicitation-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Router Solicitations Sent
                ''',
                'sent_router_solicitation_messages',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-io-oper',
            'ipv6-node-discovery',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper'
        ),
    },
    'Ipv6Io.Nodes.Node.Statistics.Traffic' : {
        'meta_info' : _MetaInfoClass('Ipv6Io.Nodes.Node.Statistics.Traffic',
            False, 
            [
            _MetaInfoClassMember('icmp', REFERENCE_CLASS, 'Icmp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper', 'Ipv6Io.Nodes.Node.Statistics.Traffic.Icmp', 
                [], [], 
                '''                ICMP Statistics
                ''',
                'icmp',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper', 'Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6', 
                [], [], 
                '''                IPv6 Statistics
                ''',
                'ipv6',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            _MetaInfoClassMember('ipv6-node-discovery', REFERENCE_CLASS, 'Ipv6NodeDiscovery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper', 'Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6NodeDiscovery', 
                [], [], 
                '''                IPv6 Node Discovery Statistics
                ''',
                'ipv6_node_discovery',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-io-oper',
            'traffic',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper'
        ),
    },
    'Ipv6Io.Nodes.Node.Statistics' : {
        'meta_info' : _MetaInfoClass('Ipv6Io.Nodes.Node.Statistics',
            False, 
            [
            _MetaInfoClassMember('traffic', REFERENCE_CLASS, 'Traffic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper', 'Ipv6Io.Nodes.Node.Statistics.Traffic', 
                [], [], 
                '''                Traffic statistics for a node
                ''',
                'traffic',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-io-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper'
        ),
    },
    'Ipv6Io.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Ipv6Io.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-ipv6-io-oper', True),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper', 'Ipv6Io.Nodes.Node.Statistics', 
                [], [], 
                '''                Statistical IPv6 network operational data for
                a node
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-io-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper'
        ),
    },
    'Ipv6Io.Nodes' : {
        'meta_info' : _MetaInfoClass('Ipv6Io.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper', 'Ipv6Io.Nodes.Node', 
                [], [], 
                '''                IPv6 network operational data for a particular
                node
                ''',
                'node',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-io-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper'
        ),
    },
    'Ipv6Io' : {
        'meta_info' : _MetaInfoClass('Ipv6Io',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper', 'Ipv6Io.Nodes', 
                [], [], 
                '''                Node-specific IPv6 IO operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-ipv6-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-io-oper',
            'ipv6-io',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper'
        ),
    },
}
_meta_table['Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6']['meta_info'].parent =_meta_table['Ipv6Io.Nodes.Node.Statistics.Traffic']['meta_info']
_meta_table['Ipv6Io.Nodes.Node.Statistics.Traffic.Icmp']['meta_info'].parent =_meta_table['Ipv6Io.Nodes.Node.Statistics.Traffic']['meta_info']
_meta_table['Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6NodeDiscovery']['meta_info'].parent =_meta_table['Ipv6Io.Nodes.Node.Statistics.Traffic']['meta_info']
_meta_table['Ipv6Io.Nodes.Node.Statistics.Traffic']['meta_info'].parent =_meta_table['Ipv6Io.Nodes.Node.Statistics']['meta_info']
_meta_table['Ipv6Io.Nodes.Node.Statistics']['meta_info'].parent =_meta_table['Ipv6Io.Nodes.Node']['meta_info']
_meta_table['Ipv6Io.Nodes.Node']['meta_info'].parent =_meta_table['Ipv6Io.Nodes']['meta_info']
_meta_table['Ipv6Io.Nodes']['meta_info'].parent =_meta_table['Ipv6Io']['meta_info']
