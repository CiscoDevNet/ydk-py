""" Cisco_IOS_XR_ipv6_io_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-io package operational data.

This module contains definitions
for the following management objects\:
  ipv6\-io\: IPv6 IO Operational Data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Ipv6Io(object):
    """
    IPv6 IO Operational Data
    
    .. attribute:: nodes
    
    	Node\-specific IPv6 IO operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper.Ipv6Io.Nodes>`
    
    

    """

    _prefix = 'ipv6-io-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Ipv6Io.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Node\-specific IPv6 IO operational data
        
        .. attribute:: node
        
        	IPv6 network operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper.Ipv6Io.Nodes.Node>`
        
        

        """

        _prefix = 'ipv6-io-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            IPv6 network operational data for a particular
            node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: statistics
            
            	Statistical IPv6 network operational data for a node
            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper.Ipv6Io.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ipv6-io-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.statistics = Ipv6Io.Nodes.Node.Statistics()
                self.statistics.parent = self


            class Statistics(object):
                """
                Statistical IPv6 network operational data for
                a node
                
                .. attribute:: traffic
                
                	Traffic statistics for a node
                	**type**\:   :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper.Ipv6Io.Nodes.Node.Statistics.Traffic>`
                
                

                """

                _prefix = 'ipv6-io-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.traffic = Ipv6Io.Nodes.Node.Statistics.Traffic()
                    self.traffic.parent = self


                class Traffic(object):
                    """
                    Traffic statistics for a node
                    
                    .. attribute:: icmp
                    
                    	ICMP Statistics
                    	**type**\:   :py:class:`Icmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper.Ipv6Io.Nodes.Node.Statistics.Traffic.Icmp>`
                    
                    .. attribute:: ipv6
                    
                    	IPv6 Statistics
                    	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper.Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6>`
                    
                    .. attribute:: ipv6_node_discovery
                    
                    	IPv6 Node Discovery Statistics
                    	**type**\:   :py:class:`Ipv6NodeDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper.Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6NodeDiscovery>`
                    
                    

                    """

                    _prefix = 'ipv6-io-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.icmp = Ipv6Io.Nodes.Node.Statistics.Traffic.Icmp()
                        self.icmp.parent = self
                        self.ipv6 = Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6()
                        self.ipv6.parent = self
                        self.ipv6_node_discovery = Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6NodeDiscovery()
                        self.ipv6_node_discovery.parent = self


                    class Ipv6(object):
                        """
                        IPv6 Statistics
                        
                        .. attribute:: bad_header_packets
                        
                        	Bad Header Packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_source_address_packets
                        
                        	Bad Source Address Packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: format_errors
                        
                        	Format Errors
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: forwarded_packets
                        
                        	Packets Forwarded
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fragment_count
                        
                        	Fragmented Packet Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fragment_failures
                        
                        	Fragment Failures
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fragmented_packets
                        
                        	Packets Fragmented
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fragments
                        
                        	Fragments
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generated_packets
                        
                        	Packets Output
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hop_count_exceeded_packets
                        
                        	Hop Count Exceeded Packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_decap_errors
                        
                        	Lisp Decap errors
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_encap_errors
                        
                        	Lisp Encap errors
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v4_decap_packets
                        
                        	Lisp IPv4 Decapped packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v4_encap_packets
                        
                        	Lisp IPv4 Encapped packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v6_decap_packets
                        
                        	Lisp IPv6 Decapped packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v6_encap_packets
                        
                        	Lisp IPv6 Encapped packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_destination_packets
                        
                        	Local Destination Packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: miscellaneous_drops
                        
                        	Misc. drops
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_route_packets
                        
                        	No Route Packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassembled_packets
                        
                        	Reassembled Packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassembly_failures
                        
                        	Reassembly Failures
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassembly_maximum_drops
                        
                        	Reassembly Reach Maximum Drop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassembly_timeouts
                        
                        	Reassembly Timeouts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_multicast_packets
                        
                        	Multicast In
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_multicast_packets
                        
                        	Multicast Out
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: source_routed_packets
                        
                        	Packets Source Routed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: too_big_packets
                        
                        	Packet Too Big
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_packets
                        
                        	Total Packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: truncated_packets
                        
                        	Truncated Packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_option_type_packets
                        
                        	Unknown Option Type Packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_protocol_packets
                        
                        	Unknown Protocol Packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-io-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.bad_header_packets = None
                            self.bad_source_address_packets = None
                            self.format_errors = None
                            self.forwarded_packets = None
                            self.fragment_count = None
                            self.fragment_failures = None
                            self.fragmented_packets = None
                            self.fragments = None
                            self.generated_packets = None
                            self.hop_count_exceeded_packets = None
                            self.lisp_decap_errors = None
                            self.lisp_encap_errors = None
                            self.lisp_v4_decap_packets = None
                            self.lisp_v4_encap_packets = None
                            self.lisp_v6_decap_packets = None
                            self.lisp_v6_encap_packets = None
                            self.local_destination_packets = None
                            self.miscellaneous_drops = None
                            self.no_route_packets = None
                            self.reassembled_packets = None
                            self.reassembly_failures = None
                            self.reassembly_maximum_drops = None
                            self.reassembly_timeouts = None
                            self.received_multicast_packets = None
                            self.sent_multicast_packets = None
                            self.source_routed_packets = None
                            self.too_big_packets = None
                            self.total_packets = None
                            self.truncated_packets = None
                            self.unknown_option_type_packets = None
                            self.unknown_protocol_packets = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-io-oper:ipv6'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_header_packets is not None:
                                return True

                            if self.bad_source_address_packets is not None:
                                return True

                            if self.format_errors is not None:
                                return True

                            if self.forwarded_packets is not None:
                                return True

                            if self.fragment_count is not None:
                                return True

                            if self.fragment_failures is not None:
                                return True

                            if self.fragmented_packets is not None:
                                return True

                            if self.fragments is not None:
                                return True

                            if self.generated_packets is not None:
                                return True

                            if self.hop_count_exceeded_packets is not None:
                                return True

                            if self.lisp_decap_errors is not None:
                                return True

                            if self.lisp_encap_errors is not None:
                                return True

                            if self.lisp_v4_decap_packets is not None:
                                return True

                            if self.lisp_v4_encap_packets is not None:
                                return True

                            if self.lisp_v6_decap_packets is not None:
                                return True

                            if self.lisp_v6_encap_packets is not None:
                                return True

                            if self.local_destination_packets is not None:
                                return True

                            if self.miscellaneous_drops is not None:
                                return True

                            if self.no_route_packets is not None:
                                return True

                            if self.reassembled_packets is not None:
                                return True

                            if self.reassembly_failures is not None:
                                return True

                            if self.reassembly_maximum_drops is not None:
                                return True

                            if self.reassembly_timeouts is not None:
                                return True

                            if self.received_multicast_packets is not None:
                                return True

                            if self.sent_multicast_packets is not None:
                                return True

                            if self.source_routed_packets is not None:
                                return True

                            if self.too_big_packets is not None:
                                return True

                            if self.total_packets is not None:
                                return True

                            if self.truncated_packets is not None:
                                return True

                            if self.unknown_option_type_packets is not None:
                                return True

                            if self.unknown_protocol_packets is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_io_oper as meta
                            return meta._meta_table['Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6']['meta_info']


                    class Icmp(object):
                        """
                        ICMP Statistics
                        
                        .. attribute:: checksum_error_messages
                        
                        	ICMP Checksum Errors
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: output_messages
                        
                        	ICMP Transmitted
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_echo_reply_messages
                        
                        	ICMP Echo Reply Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_echo_request_messages
                        
                        	ICMP Echo Request Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_hop_count_expired_messages
                        
                        	ICMP Hop Count Expired Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_parameter_error_messages
                        
                        	ICMP Parameter Error Messages Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_parameter_header_messages
                        
                        	ICMP Parameter Next Header Messages Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_parameter_option_messages
                        
                        	ICMP Parameter Option Problem Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_parameter_unknown_type_messages
                        
                        	ICMP Parameter Unknown Type Messages Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_reassembly_timeouts
                        
                        	ICMP Reassembly Timeouts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_too_big_messages
                        
                        	ICMP Too Big Messages Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_unknown_timeout_messages
                        
                        	ICMP Unknown Timeout Messages Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_unreachable_address_messages
                        
                        	ICMP Addr Unreachable Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_unreachable_admin_messages
                        
                        	ICMP Admin Unreachable Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_unreachable_neighbor_messages
                        
                        	ICMP Host Unreachable Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_unreachable_port_messages
                        
                        	ICMP Port Unreachable Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_unreachable_routing_messages
                        
                        	ICMP Route Unreachable Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_unreachable_unknown_type_messages
                        
                        	ICMP Unreachable Unknown Messages Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_echo_reply_messages
                        
                        	ICMP Echo Reply Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_echo_request_messages
                        
                        	ICMP Echo Request Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_hop_count_expired_messages
                        
                        	ICMP Hop Count Expired Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_parameter_error_messages
                        
                        	ICMP Parameter Error Messages Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_parameter_header_messages
                        
                        	ICMP Parameter Next Header Messages Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_parameter_option_messages
                        
                        	ICMP Parameter Option Messages Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_parameter_unknown_type_messages
                        
                        	ICMP Parameter Unknown Type Messages Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_rate_limited_packets
                        
                        	ICMP Sent Packets Ratelimited
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_reassembly_timeouts
                        
                        	ICMP Reassembly Timeouts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_too_big_messages
                        
                        	ICMP Too Big Messages Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_unknown_timeout_messages
                        
                        	ICMP Unknown Timeout Messages Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_unreachable_address_messages
                        
                        	ICMP Addr Unreachable Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_unreachable_admin_messages
                        
                        	ICMP Admin Unreachable Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_unreachable_neighbor_messages
                        
                        	ICMP Host Unreachable Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_unreachable_port_messages
                        
                        	ICMP Port Unreachable Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_unreachable_routing_messages
                        
                        	ICMP Route Unreachable Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_unreachable_unknown_type_messages
                        
                        	ICMP Unreachable Unknown Messages Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: too_short_error_messages
                        
                        	ICMP Too Short Errors
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_messages
                        
                        	ICMP Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_error_type_messages
                        
                        	ICMP Unknown Error
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-io-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.checksum_error_messages = None
                            self.output_messages = None
                            self.received_echo_reply_messages = None
                            self.received_echo_request_messages = None
                            self.received_hop_count_expired_messages = None
                            self.received_parameter_error_messages = None
                            self.received_parameter_header_messages = None
                            self.received_parameter_option_messages = None
                            self.received_parameter_unknown_type_messages = None
                            self.received_reassembly_timeouts = None
                            self.received_too_big_messages = None
                            self.received_unknown_timeout_messages = None
                            self.received_unreachable_address_messages = None
                            self.received_unreachable_admin_messages = None
                            self.received_unreachable_neighbor_messages = None
                            self.received_unreachable_port_messages = None
                            self.received_unreachable_routing_messages = None
                            self.received_unreachable_unknown_type_messages = None
                            self.sent_echo_reply_messages = None
                            self.sent_echo_request_messages = None
                            self.sent_hop_count_expired_messages = None
                            self.sent_parameter_error_messages = None
                            self.sent_parameter_header_messages = None
                            self.sent_parameter_option_messages = None
                            self.sent_parameter_unknown_type_messages = None
                            self.sent_rate_limited_packets = None
                            self.sent_reassembly_timeouts = None
                            self.sent_too_big_messages = None
                            self.sent_unknown_timeout_messages = None
                            self.sent_unreachable_address_messages = None
                            self.sent_unreachable_admin_messages = None
                            self.sent_unreachable_neighbor_messages = None
                            self.sent_unreachable_port_messages = None
                            self.sent_unreachable_routing_messages = None
                            self.sent_unreachable_unknown_type_messages = None
                            self.too_short_error_messages = None
                            self.total_messages = None
                            self.unknown_error_type_messages = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-io-oper:icmp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.checksum_error_messages is not None:
                                return True

                            if self.output_messages is not None:
                                return True

                            if self.received_echo_reply_messages is not None:
                                return True

                            if self.received_echo_request_messages is not None:
                                return True

                            if self.received_hop_count_expired_messages is not None:
                                return True

                            if self.received_parameter_error_messages is not None:
                                return True

                            if self.received_parameter_header_messages is not None:
                                return True

                            if self.received_parameter_option_messages is not None:
                                return True

                            if self.received_parameter_unknown_type_messages is not None:
                                return True

                            if self.received_reassembly_timeouts is not None:
                                return True

                            if self.received_too_big_messages is not None:
                                return True

                            if self.received_unknown_timeout_messages is not None:
                                return True

                            if self.received_unreachable_address_messages is not None:
                                return True

                            if self.received_unreachable_admin_messages is not None:
                                return True

                            if self.received_unreachable_neighbor_messages is not None:
                                return True

                            if self.received_unreachable_port_messages is not None:
                                return True

                            if self.received_unreachable_routing_messages is not None:
                                return True

                            if self.received_unreachable_unknown_type_messages is not None:
                                return True

                            if self.sent_echo_reply_messages is not None:
                                return True

                            if self.sent_echo_request_messages is not None:
                                return True

                            if self.sent_hop_count_expired_messages is not None:
                                return True

                            if self.sent_parameter_error_messages is not None:
                                return True

                            if self.sent_parameter_header_messages is not None:
                                return True

                            if self.sent_parameter_option_messages is not None:
                                return True

                            if self.sent_parameter_unknown_type_messages is not None:
                                return True

                            if self.sent_rate_limited_packets is not None:
                                return True

                            if self.sent_reassembly_timeouts is not None:
                                return True

                            if self.sent_too_big_messages is not None:
                                return True

                            if self.sent_unknown_timeout_messages is not None:
                                return True

                            if self.sent_unreachable_address_messages is not None:
                                return True

                            if self.sent_unreachable_admin_messages is not None:
                                return True

                            if self.sent_unreachable_neighbor_messages is not None:
                                return True

                            if self.sent_unreachable_port_messages is not None:
                                return True

                            if self.sent_unreachable_routing_messages is not None:
                                return True

                            if self.sent_unreachable_unknown_type_messages is not None:
                                return True

                            if self.too_short_error_messages is not None:
                                return True

                            if self.total_messages is not None:
                                return True

                            if self.unknown_error_type_messages is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_io_oper as meta
                            return meta._meta_table['Ipv6Io.Nodes.Node.Statistics.Traffic.Icmp']['meta_info']


                    class Ipv6NodeDiscovery(object):
                        """
                        IPv6 Node Discovery Statistics
                        
                        .. attribute:: received_neighbor_advertisement_messages
                        
                        	ICMP Neighbor Advertisements Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_neighbor_solicitation_messages
                        
                        	ICMP Neighbor Solicitations Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_redirect_messages
                        
                        	ICMP Redirect Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_router_advertisement_messages
                        
                        	ICMP Router Advertisements Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_router_solicitation_messages
                        
                        	ICMP Router Solicitations Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_neighbor_advertisement_messages
                        
                        	ICMP Neighbor Advertisements Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_neighbor_solicitation_messages
                        
                        	ICMP Neighbor Solicitations Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_redirect_messages
                        
                        	ICMP Redirect Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_router_advertisement_messages
                        
                        	ICMP Router Advertisements Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_router_solicitation_messages
                        
                        	ICMP Router Solicitations Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-io-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.received_neighbor_advertisement_messages = None
                            self.received_neighbor_solicitation_messages = None
                            self.received_redirect_messages = None
                            self.received_router_advertisement_messages = None
                            self.received_router_solicitation_messages = None
                            self.sent_neighbor_advertisement_messages = None
                            self.sent_neighbor_solicitation_messages = None
                            self.sent_redirect_messages = None
                            self.sent_router_advertisement_messages = None
                            self.sent_router_solicitation_messages = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-io-oper:ipv6-node-discovery'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.received_neighbor_advertisement_messages is not None:
                                return True

                            if self.received_neighbor_solicitation_messages is not None:
                                return True

                            if self.received_redirect_messages is not None:
                                return True

                            if self.received_router_advertisement_messages is not None:
                                return True

                            if self.received_router_solicitation_messages is not None:
                                return True

                            if self.sent_neighbor_advertisement_messages is not None:
                                return True

                            if self.sent_neighbor_solicitation_messages is not None:
                                return True

                            if self.sent_redirect_messages is not None:
                                return True

                            if self.sent_router_advertisement_messages is not None:
                                return True

                            if self.sent_router_solicitation_messages is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_io_oper as meta
                            return meta._meta_table['Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6NodeDiscovery']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-io-oper:traffic'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.icmp is not None and self.icmp._has_data():
                            return True

                        if self.ipv6 is not None and self.ipv6._has_data():
                            return True

                        if self.ipv6_node_discovery is not None and self.ipv6_node_discovery._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_io_oper as meta
                        return meta._meta_table['Ipv6Io.Nodes.Node.Statistics.Traffic']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-io-oper:statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.traffic is not None and self.traffic._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_io_oper as meta
                    return meta._meta_table['Ipv6Io.Nodes.Node.Statistics']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-ipv6-io-oper:ipv6-io/Cisco-IOS-XR-ipv6-io-oper:nodes/Cisco-IOS-XR-ipv6-io-oper:node[Cisco-IOS-XR-ipv6-io-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.statistics is not None and self.statistics._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_io_oper as meta
                return meta._meta_table['Ipv6Io.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-io-oper:ipv6-io/Cisco-IOS-XR-ipv6-io-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_io_oper as meta
            return meta._meta_table['Ipv6Io.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-io-oper:ipv6-io'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_io_oper as meta
        return meta._meta_table['Ipv6Io']['meta_info']


