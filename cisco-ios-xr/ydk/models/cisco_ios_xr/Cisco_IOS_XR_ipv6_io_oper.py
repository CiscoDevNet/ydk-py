""" Cisco_IOS_XR_ipv6_io_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-io package operational data.

This module contains definitions
for the following management objects\:
  ipv6\-io\: IPv6 IO Operational Data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ipv6Io(Entity):
    """
    IPv6 IO Operational Data
    
    .. attribute:: nodes
    
    	Node\-specific IPv6 IO operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper.Ipv6Io.Nodes>`
    
    

    """

    _prefix = 'ipv6-io-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ipv6Io, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6-io"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-io-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", Ipv6Io.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = Ipv6Io.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-io-oper:ipv6-io"


    class Nodes(Entity):
        """
        Node\-specific IPv6 IO operational data
        
        .. attribute:: node
        
        	IPv6 network operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper.Ipv6Io.Nodes.Node>`
        
        

        """

        _prefix = 'ipv6-io-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv6Io.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ipv6-io"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", Ipv6Io.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-io-oper:ipv6-io/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6Io.Nodes, [], name, value)


        class Node(Entity):
            """
            IPv6 network operational data for a particular
            node
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: statistics
            
            	Statistical IPv6 network operational data for a node
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper.Ipv6Io.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ipv6-io-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv6Io.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_container_classes = OrderedDict([("statistics", ("statistics", Ipv6Io.Nodes.Node.Statistics))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                ])
                self.node_name = None

                self.statistics = Ipv6Io.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-io-oper:ipv6-io/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6Io.Nodes.Node, ['node_name'], name, value)


            class Statistics(Entity):
                """
                Statistical IPv6 network operational data for
                a node
                
                .. attribute:: traffic
                
                	Traffic statistics for a node
                	**type**\:  :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper.Ipv6Io.Nodes.Node.Statistics.Traffic>`
                
                

                """

                _prefix = 'ipv6-io-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6Io.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("traffic", ("traffic", Ipv6Io.Nodes.Node.Statistics.Traffic))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.traffic = Ipv6Io.Nodes.Node.Statistics.Traffic()
                    self.traffic.parent = self
                    self._children_name_map["traffic"] = "traffic"
                    self._children_yang_names.add("traffic")
                    self._segment_path = lambda: "statistics"


                class Traffic(Entity):
                    """
                    Traffic statistics for a node
                    
                    .. attribute:: ipv6
                    
                    	IPv6 Statistics
                    	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper.Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6>`
                    
                    .. attribute:: icmp
                    
                    	ICMP Statistics
                    	**type**\:  :py:class:`Icmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper.Ipv6Io.Nodes.Node.Statistics.Traffic.Icmp>`
                    
                    .. attribute:: ipv6_node_discovery
                    
                    	IPv6 Node Discovery Statistics
                    	**type**\:  :py:class:`Ipv6NodeDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper.Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6NodeDiscovery>`
                    
                    

                    """

                    _prefix = 'ipv6-io-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6Io.Nodes.Node.Statistics.Traffic, self).__init__()

                        self.yang_name = "traffic"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("ipv6", ("ipv6", Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6)), ("icmp", ("icmp", Ipv6Io.Nodes.Node.Statistics.Traffic.Icmp)), ("ipv6-node-discovery", ("ipv6_node_discovery", Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6NodeDiscovery))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.ipv6 = Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6()
                        self.ipv6.parent = self
                        self._children_name_map["ipv6"] = "ipv6"
                        self._children_yang_names.add("ipv6")

                        self.icmp = Ipv6Io.Nodes.Node.Statistics.Traffic.Icmp()
                        self.icmp.parent = self
                        self._children_name_map["icmp"] = "icmp"
                        self._children_yang_names.add("icmp")

                        self.ipv6_node_discovery = Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6NodeDiscovery()
                        self.ipv6_node_discovery.parent = self
                        self._children_name_map["ipv6_node_discovery"] = "ipv6-node-discovery"
                        self._children_yang_names.add("ipv6-node-discovery")
                        self._segment_path = lambda: "traffic"


                    class Ipv6(Entity):
                        """
                        IPv6 Statistics
                        
                        .. attribute:: total_packets
                        
                        	Total Packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_destination_packets
                        
                        	Local Destination Packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: format_errors
                        
                        	Format Errors
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: truncated_packets
                        
                        	Truncated Packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hop_count_exceeded_packets
                        
                        	Hop Count Exceeded Packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_source_address_packets
                        
                        	Bad Source Address Packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_header_packets
                        
                        	Bad Header Packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_option_type_packets
                        
                        	Unknown Option Type Packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_protocol_packets
                        
                        	Unknown Protocol Packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fragments
                        
                        	Fragments
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassembled_packets
                        
                        	Reassembled Packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassembly_timeouts
                        
                        	Reassembly Timeouts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassembly_failures
                        
                        	Reassembly Failures
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassembly_maximum_drops
                        
                        	Reassembly Reach Maximum Drop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generated_packets
                        
                        	Packets Output
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: forwarded_packets
                        
                        	Packets Forwarded
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: source_routed_packets
                        
                        	Packets Source Routed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fragmented_packets
                        
                        	Packets Fragmented
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fragment_count
                        
                        	Fragmented Packet Count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fragment_failures
                        
                        	Fragment Failures
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_route_packets
                        
                        	No Route Packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: too_big_packets
                        
                        	Packet Too Big
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_multicast_packets
                        
                        	Multicast In
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_multicast_packets
                        
                        	Multicast Out
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: miscellaneous_drops
                        
                        	Misc. drops
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v4_encap_packets
                        
                        	Lisp IPv4 Encapped packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v4_decap_packets
                        
                        	Lisp IPv4 Decapped packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v6_encap_packets
                        
                        	Lisp IPv6 Encapped packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v6_decap_packets
                        
                        	Lisp IPv6 Decapped packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_encap_errors
                        
                        	Lisp Encap errors
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_decap_errors
                        
                        	Lisp Decap errors
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-io-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6, self).__init__()

                            self.yang_name = "ipv6"
                            self.yang_parent_name = "traffic"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('total_packets', YLeaf(YType.uint32, 'total-packets')),
                                ('local_destination_packets', YLeaf(YType.uint32, 'local-destination-packets')),
                                ('format_errors', YLeaf(YType.uint32, 'format-errors')),
                                ('truncated_packets', YLeaf(YType.uint32, 'truncated-packets')),
                                ('hop_count_exceeded_packets', YLeaf(YType.uint32, 'hop-count-exceeded-packets')),
                                ('bad_source_address_packets', YLeaf(YType.uint32, 'bad-source-address-packets')),
                                ('bad_header_packets', YLeaf(YType.uint32, 'bad-header-packets')),
                                ('unknown_option_type_packets', YLeaf(YType.uint32, 'unknown-option-type-packets')),
                                ('unknown_protocol_packets', YLeaf(YType.uint32, 'unknown-protocol-packets')),
                                ('fragments', YLeaf(YType.uint32, 'fragments')),
                                ('reassembled_packets', YLeaf(YType.uint32, 'reassembled-packets')),
                                ('reassembly_timeouts', YLeaf(YType.uint32, 'reassembly-timeouts')),
                                ('reassembly_failures', YLeaf(YType.uint32, 'reassembly-failures')),
                                ('reassembly_maximum_drops', YLeaf(YType.uint32, 'reassembly-maximum-drops')),
                                ('generated_packets', YLeaf(YType.uint32, 'generated-packets')),
                                ('forwarded_packets', YLeaf(YType.uint32, 'forwarded-packets')),
                                ('source_routed_packets', YLeaf(YType.uint32, 'source-routed-packets')),
                                ('fragmented_packets', YLeaf(YType.uint32, 'fragmented-packets')),
                                ('fragment_count', YLeaf(YType.uint32, 'fragment-count')),
                                ('fragment_failures', YLeaf(YType.uint32, 'fragment-failures')),
                                ('no_route_packets', YLeaf(YType.uint32, 'no-route-packets')),
                                ('too_big_packets', YLeaf(YType.uint32, 'too-big-packets')),
                                ('received_multicast_packets', YLeaf(YType.uint32, 'received-multicast-packets')),
                                ('sent_multicast_packets', YLeaf(YType.uint32, 'sent-multicast-packets')),
                                ('miscellaneous_drops', YLeaf(YType.uint32, 'miscellaneous-drops')),
                                ('lisp_v4_encap_packets', YLeaf(YType.uint32, 'lisp-v4-encap-packets')),
                                ('lisp_v4_decap_packets', YLeaf(YType.uint32, 'lisp-v4-decap-packets')),
                                ('lisp_v6_encap_packets', YLeaf(YType.uint32, 'lisp-v6-encap-packets')),
                                ('lisp_v6_decap_packets', YLeaf(YType.uint32, 'lisp-v6-decap-packets')),
                                ('lisp_encap_errors', YLeaf(YType.uint32, 'lisp-encap-errors')),
                                ('lisp_decap_errors', YLeaf(YType.uint32, 'lisp-decap-errors')),
                            ])
                            self.total_packets = None
                            self.local_destination_packets = None
                            self.format_errors = None
                            self.truncated_packets = None
                            self.hop_count_exceeded_packets = None
                            self.bad_source_address_packets = None
                            self.bad_header_packets = None
                            self.unknown_option_type_packets = None
                            self.unknown_protocol_packets = None
                            self.fragments = None
                            self.reassembled_packets = None
                            self.reassembly_timeouts = None
                            self.reassembly_failures = None
                            self.reassembly_maximum_drops = None
                            self.generated_packets = None
                            self.forwarded_packets = None
                            self.source_routed_packets = None
                            self.fragmented_packets = None
                            self.fragment_count = None
                            self.fragment_failures = None
                            self.no_route_packets = None
                            self.too_big_packets = None
                            self.received_multicast_packets = None
                            self.sent_multicast_packets = None
                            self.miscellaneous_drops = None
                            self.lisp_v4_encap_packets = None
                            self.lisp_v4_decap_packets = None
                            self.lisp_v6_encap_packets = None
                            self.lisp_v6_decap_packets = None
                            self.lisp_encap_errors = None
                            self.lisp_decap_errors = None
                            self._segment_path = lambda: "ipv6"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6, ['total_packets', 'local_destination_packets', 'format_errors', 'truncated_packets', 'hop_count_exceeded_packets', 'bad_source_address_packets', 'bad_header_packets', 'unknown_option_type_packets', 'unknown_protocol_packets', 'fragments', 'reassembled_packets', 'reassembly_timeouts', 'reassembly_failures', 'reassembly_maximum_drops', 'generated_packets', 'forwarded_packets', 'source_routed_packets', 'fragmented_packets', 'fragment_count', 'fragment_failures', 'no_route_packets', 'too_big_packets', 'received_multicast_packets', 'sent_multicast_packets', 'miscellaneous_drops', 'lisp_v4_encap_packets', 'lisp_v4_decap_packets', 'lisp_v6_encap_packets', 'lisp_v6_decap_packets', 'lisp_encap_errors', 'lisp_decap_errors'], name, value)


                    class Icmp(Entity):
                        """
                        ICMP Statistics
                        
                        .. attribute:: total_messages
                        
                        	ICMP Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: too_short_error_messages
                        
                        	ICMP Too Short Errors
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: checksum_error_messages
                        
                        	ICMP Checksum Errors
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_error_type_messages
                        
                        	ICMP Unknown Error
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: output_messages
                        
                        	ICMP Transmitted
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_rate_limited_packets
                        
                        	ICMP Sent Packets Ratelimited
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_unreachable_routing_messages
                        
                        	ICMP Route Unreachable Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_unreachable_admin_messages
                        
                        	ICMP Admin Unreachable Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_unreachable_neighbor_messages
                        
                        	ICMP Host Unreachable Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_unreachable_address_messages
                        
                        	ICMP Addr Unreachable Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_unreachable_port_messages
                        
                        	ICMP Port Unreachable Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_unreachable_routing_messages
                        
                        	ICMP Route Unreachable Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_unreachable_admin_messages
                        
                        	ICMP Admin Unreachable Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_unreachable_neighbor_messages
                        
                        	ICMP Host Unreachable Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_unreachable_address_messages
                        
                        	ICMP Addr Unreachable Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_unreachable_port_messages
                        
                        	ICMP Port Unreachable Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_hop_count_expired_messages
                        
                        	ICMP Hop Count Expired Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_reassembly_timeouts
                        
                        	ICMP Reassembly Timeouts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_hop_count_expired_messages
                        
                        	ICMP Hop Count Expired Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_reassembly_timeouts
                        
                        	ICMP Reassembly Timeouts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_too_big_messages
                        
                        	ICMP Too Big Messages Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_too_big_messages
                        
                        	ICMP Too Big Messages Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_parameter_error_messages
                        
                        	ICMP Parameter Error Messages Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_parameter_header_messages
                        
                        	ICMP Parameter Next Header Messages Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_parameter_option_messages
                        
                        	ICMP Parameter Option Messages Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_parameter_error_messages
                        
                        	ICMP Parameter Error Messages Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_parameter_header_messages
                        
                        	ICMP Parameter Next Header Messages Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_parameter_option_messages
                        
                        	ICMP Parameter Option Problem Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_echo_request_messages
                        
                        	ICMP Echo Request Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_echo_reply_messages
                        
                        	ICMP Echo Reply Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_echo_request_messages
                        
                        	ICMP Echo Request Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_echo_reply_messages
                        
                        	ICMP Echo Reply Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_unknown_timeout_messages
                        
                        	ICMP Unknown Timeout Messages Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_unknown_timeout_messages
                        
                        	ICMP Unknown Timeout Messages Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_parameter_unknown_type_messages
                        
                        	ICMP Parameter Unknown Type Messages Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_parameter_unknown_type_messages
                        
                        	ICMP Parameter Unknown Type Messages Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_unreachable_unknown_type_messages
                        
                        	ICMP Unreachable Unknown Messages Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_unreachable_unknown_type_messages
                        
                        	ICMP Unreachable Unknown Messages Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-io-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6Io.Nodes.Node.Statistics.Traffic.Icmp, self).__init__()

                            self.yang_name = "icmp"
                            self.yang_parent_name = "traffic"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('total_messages', YLeaf(YType.uint32, 'total-messages')),
                                ('too_short_error_messages', YLeaf(YType.uint32, 'too-short-error-messages')),
                                ('checksum_error_messages', YLeaf(YType.uint32, 'checksum-error-messages')),
                                ('unknown_error_type_messages', YLeaf(YType.uint32, 'unknown-error-type-messages')),
                                ('output_messages', YLeaf(YType.uint32, 'output-messages')),
                                ('sent_rate_limited_packets', YLeaf(YType.uint32, 'sent-rate-limited-packets')),
                                ('sent_unreachable_routing_messages', YLeaf(YType.uint32, 'sent-unreachable-routing-messages')),
                                ('sent_unreachable_admin_messages', YLeaf(YType.uint32, 'sent-unreachable-admin-messages')),
                                ('sent_unreachable_neighbor_messages', YLeaf(YType.uint32, 'sent-unreachable-neighbor-messages')),
                                ('sent_unreachable_address_messages', YLeaf(YType.uint32, 'sent-unreachable-address-messages')),
                                ('sent_unreachable_port_messages', YLeaf(YType.uint32, 'sent-unreachable-port-messages')),
                                ('received_unreachable_routing_messages', YLeaf(YType.uint32, 'received-unreachable-routing-messages')),
                                ('received_unreachable_admin_messages', YLeaf(YType.uint32, 'received-unreachable-admin-messages')),
                                ('received_unreachable_neighbor_messages', YLeaf(YType.uint32, 'received-unreachable-neighbor-messages')),
                                ('received_unreachable_address_messages', YLeaf(YType.uint32, 'received-unreachable-address-messages')),
                                ('received_unreachable_port_messages', YLeaf(YType.uint32, 'received-unreachable-port-messages')),
                                ('sent_hop_count_expired_messages', YLeaf(YType.uint32, 'sent-hop-count-expired-messages')),
                                ('sent_reassembly_timeouts', YLeaf(YType.uint32, 'sent-reassembly-timeouts')),
                                ('received_hop_count_expired_messages', YLeaf(YType.uint32, 'received-hop-count-expired-messages')),
                                ('received_reassembly_timeouts', YLeaf(YType.uint32, 'received-reassembly-timeouts')),
                                ('sent_too_big_messages', YLeaf(YType.uint32, 'sent-too-big-messages')),
                                ('received_too_big_messages', YLeaf(YType.uint32, 'received-too-big-messages')),
                                ('sent_parameter_error_messages', YLeaf(YType.uint32, 'sent-parameter-error-messages')),
                                ('sent_parameter_header_messages', YLeaf(YType.uint32, 'sent-parameter-header-messages')),
                                ('sent_parameter_option_messages', YLeaf(YType.uint32, 'sent-parameter-option-messages')),
                                ('received_parameter_error_messages', YLeaf(YType.uint32, 'received-parameter-error-messages')),
                                ('received_parameter_header_messages', YLeaf(YType.uint32, 'received-parameter-header-messages')),
                                ('received_parameter_option_messages', YLeaf(YType.uint32, 'received-parameter-option-messages')),
                                ('sent_echo_request_messages', YLeaf(YType.uint32, 'sent-echo-request-messages')),
                                ('sent_echo_reply_messages', YLeaf(YType.uint32, 'sent-echo-reply-messages')),
                                ('received_echo_request_messages', YLeaf(YType.uint32, 'received-echo-request-messages')),
                                ('received_echo_reply_messages', YLeaf(YType.uint32, 'received-echo-reply-messages')),
                                ('sent_unknown_timeout_messages', YLeaf(YType.uint32, 'sent-unknown-timeout-messages')),
                                ('received_unknown_timeout_messages', YLeaf(YType.uint32, 'received-unknown-timeout-messages')),
                                ('sent_parameter_unknown_type_messages', YLeaf(YType.uint32, 'sent-parameter-unknown-type-messages')),
                                ('received_parameter_unknown_type_messages', YLeaf(YType.uint32, 'received-parameter-unknown-type-messages')),
                                ('sent_unreachable_unknown_type_messages', YLeaf(YType.uint32, 'sent-unreachable-unknown-type-messages')),
                                ('received_unreachable_unknown_type_messages', YLeaf(YType.uint32, 'received-unreachable-unknown-type-messages')),
                            ])
                            self.total_messages = None
                            self.too_short_error_messages = None
                            self.checksum_error_messages = None
                            self.unknown_error_type_messages = None
                            self.output_messages = None
                            self.sent_rate_limited_packets = None
                            self.sent_unreachable_routing_messages = None
                            self.sent_unreachable_admin_messages = None
                            self.sent_unreachable_neighbor_messages = None
                            self.sent_unreachable_address_messages = None
                            self.sent_unreachable_port_messages = None
                            self.received_unreachable_routing_messages = None
                            self.received_unreachable_admin_messages = None
                            self.received_unreachable_neighbor_messages = None
                            self.received_unreachable_address_messages = None
                            self.received_unreachable_port_messages = None
                            self.sent_hop_count_expired_messages = None
                            self.sent_reassembly_timeouts = None
                            self.received_hop_count_expired_messages = None
                            self.received_reassembly_timeouts = None
                            self.sent_too_big_messages = None
                            self.received_too_big_messages = None
                            self.sent_parameter_error_messages = None
                            self.sent_parameter_header_messages = None
                            self.sent_parameter_option_messages = None
                            self.received_parameter_error_messages = None
                            self.received_parameter_header_messages = None
                            self.received_parameter_option_messages = None
                            self.sent_echo_request_messages = None
                            self.sent_echo_reply_messages = None
                            self.received_echo_request_messages = None
                            self.received_echo_reply_messages = None
                            self.sent_unknown_timeout_messages = None
                            self.received_unknown_timeout_messages = None
                            self.sent_parameter_unknown_type_messages = None
                            self.received_parameter_unknown_type_messages = None
                            self.sent_unreachable_unknown_type_messages = None
                            self.received_unreachable_unknown_type_messages = None
                            self._segment_path = lambda: "icmp"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6Io.Nodes.Node.Statistics.Traffic.Icmp, ['total_messages', 'too_short_error_messages', 'checksum_error_messages', 'unknown_error_type_messages', 'output_messages', 'sent_rate_limited_packets', 'sent_unreachable_routing_messages', 'sent_unreachable_admin_messages', 'sent_unreachable_neighbor_messages', 'sent_unreachable_address_messages', 'sent_unreachable_port_messages', 'received_unreachable_routing_messages', 'received_unreachable_admin_messages', 'received_unreachable_neighbor_messages', 'received_unreachable_address_messages', 'received_unreachable_port_messages', 'sent_hop_count_expired_messages', 'sent_reassembly_timeouts', 'received_hop_count_expired_messages', 'received_reassembly_timeouts', 'sent_too_big_messages', 'received_too_big_messages', 'sent_parameter_error_messages', 'sent_parameter_header_messages', 'sent_parameter_option_messages', 'received_parameter_error_messages', 'received_parameter_header_messages', 'received_parameter_option_messages', 'sent_echo_request_messages', 'sent_echo_reply_messages', 'received_echo_request_messages', 'received_echo_reply_messages', 'sent_unknown_timeout_messages', 'received_unknown_timeout_messages', 'sent_parameter_unknown_type_messages', 'received_parameter_unknown_type_messages', 'sent_unreachable_unknown_type_messages', 'received_unreachable_unknown_type_messages'], name, value)


                    class Ipv6NodeDiscovery(Entity):
                        """
                        IPv6 Node Discovery Statistics
                        
                        .. attribute:: sent_router_solicitation_messages
                        
                        	ICMP Router Solicitations Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_router_advertisement_messages
                        
                        	ICMP Router Advertisements Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_neighbor_solicitation_messages
                        
                        	ICMP Neighbor Solicitations Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_neighbor_advertisement_messages
                        
                        	ICMP Neighbor Advertisements Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent_redirect_messages
                        
                        	ICMP Redirect Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_router_solicitation_messages
                        
                        	ICMP Router Solicitations Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_router_advertisement_messages
                        
                        	ICMP Router Advertisements Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_neighbor_solicitation_messages
                        
                        	ICMP Neighbor Solicitations Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_neighbor_advertisement_messages
                        
                        	ICMP Neighbor Advertisements Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_redirect_messages
                        
                        	ICMP Redirect Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-io-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6NodeDiscovery, self).__init__()

                            self.yang_name = "ipv6-node-discovery"
                            self.yang_parent_name = "traffic"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sent_router_solicitation_messages', YLeaf(YType.uint32, 'sent-router-solicitation-messages')),
                                ('sent_router_advertisement_messages', YLeaf(YType.uint32, 'sent-router-advertisement-messages')),
                                ('sent_neighbor_solicitation_messages', YLeaf(YType.uint32, 'sent-neighbor-solicitation-messages')),
                                ('sent_neighbor_advertisement_messages', YLeaf(YType.uint32, 'sent-neighbor-advertisement-messages')),
                                ('sent_redirect_messages', YLeaf(YType.uint32, 'sent-redirect-messages')),
                                ('received_router_solicitation_messages', YLeaf(YType.uint32, 'received-router-solicitation-messages')),
                                ('received_router_advertisement_messages', YLeaf(YType.uint32, 'received-router-advertisement-messages')),
                                ('received_neighbor_solicitation_messages', YLeaf(YType.uint32, 'received-neighbor-solicitation-messages')),
                                ('received_neighbor_advertisement_messages', YLeaf(YType.uint32, 'received-neighbor-advertisement-messages')),
                                ('received_redirect_messages', YLeaf(YType.uint32, 'received-redirect-messages')),
                            ])
                            self.sent_router_solicitation_messages = None
                            self.sent_router_advertisement_messages = None
                            self.sent_neighbor_solicitation_messages = None
                            self.sent_neighbor_advertisement_messages = None
                            self.sent_redirect_messages = None
                            self.received_router_solicitation_messages = None
                            self.received_router_advertisement_messages = None
                            self.received_neighbor_solicitation_messages = None
                            self.received_neighbor_advertisement_messages = None
                            self.received_redirect_messages = None
                            self._segment_path = lambda: "ipv6-node-discovery"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6NodeDiscovery, ['sent_router_solicitation_messages', 'sent_router_advertisement_messages', 'sent_neighbor_solicitation_messages', 'sent_neighbor_advertisement_messages', 'sent_redirect_messages', 'received_router_solicitation_messages', 'received_router_advertisement_messages', 'received_neighbor_solicitation_messages', 'received_neighbor_advertisement_messages', 'received_redirect_messages'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv6Io()
        return self._top_entity

