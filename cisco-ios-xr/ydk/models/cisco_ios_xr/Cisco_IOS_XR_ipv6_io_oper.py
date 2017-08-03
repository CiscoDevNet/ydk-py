""" Cisco_IOS_XR_ipv6_io_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-io package operational data.

This module contains definitions
for the following management objects\:
  ipv6\-io\: IPv6 IO Operational Data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ipv6Io(Entity):
    """
    IPv6 IO Operational Data
    
    .. attribute:: nodes
    
    	Node\-specific IPv6 IO operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper.Ipv6Io.Nodes>`
    
    

    """

    _prefix = 'ipv6-io-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ipv6Io, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6-io"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-io-oper"

        self.nodes = Ipv6Io.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Node\-specific IPv6 IO operational data
        
        .. attribute:: node
        
        	IPv6 network operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_oper.Ipv6Io.Nodes.Node>`
        
        

        """

        _prefix = 'ipv6-io-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv6Io.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ipv6-io"

            self.node = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ipv6Io.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv6Io.Nodes, self).__setattr__(name, value)


        class Node(Entity):
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
                super(Ipv6Io.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.statistics = Ipv6Io.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ipv6Io.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv6Io.Nodes.Node, self).__setattr__(name, value)


            class Statistics(Entity):
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
                    super(Ipv6Io.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"

                    self.traffic = Ipv6Io.Nodes.Node.Statistics.Traffic()
                    self.traffic.parent = self
                    self._children_name_map["traffic"] = "traffic"
                    self._children_yang_names.add("traffic")


                class Traffic(Entity):
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
                        super(Ipv6Io.Nodes.Node.Statistics.Traffic, self).__init__()

                        self.yang_name = "traffic"
                        self.yang_parent_name = "statistics"

                        self.icmp = Ipv6Io.Nodes.Node.Statistics.Traffic.Icmp()
                        self.icmp.parent = self
                        self._children_name_map["icmp"] = "icmp"
                        self._children_yang_names.add("icmp")

                        self.ipv6 = Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6()
                        self.ipv6.parent = self
                        self._children_name_map["ipv6"] = "ipv6"
                        self._children_yang_names.add("ipv6")

                        self.ipv6_node_discovery = Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6NodeDiscovery()
                        self.ipv6_node_discovery.parent = self
                        self._children_name_map["ipv6_node_discovery"] = "ipv6-node-discovery"
                        self._children_yang_names.add("ipv6-node-discovery")


                    class Ipv6(Entity):
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
                            super(Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6, self).__init__()

                            self.yang_name = "ipv6"
                            self.yang_parent_name = "traffic"

                            self.bad_header_packets = YLeaf(YType.uint32, "bad-header-packets")

                            self.bad_source_address_packets = YLeaf(YType.uint32, "bad-source-address-packets")

                            self.format_errors = YLeaf(YType.uint32, "format-errors")

                            self.forwarded_packets = YLeaf(YType.uint32, "forwarded-packets")

                            self.fragment_count = YLeaf(YType.uint32, "fragment-count")

                            self.fragment_failures = YLeaf(YType.uint32, "fragment-failures")

                            self.fragmented_packets = YLeaf(YType.uint32, "fragmented-packets")

                            self.fragments = YLeaf(YType.uint32, "fragments")

                            self.generated_packets = YLeaf(YType.uint32, "generated-packets")

                            self.hop_count_exceeded_packets = YLeaf(YType.uint32, "hop-count-exceeded-packets")

                            self.lisp_decap_errors = YLeaf(YType.uint32, "lisp-decap-errors")

                            self.lisp_encap_errors = YLeaf(YType.uint32, "lisp-encap-errors")

                            self.lisp_v4_decap_packets = YLeaf(YType.uint32, "lisp-v4-decap-packets")

                            self.lisp_v4_encap_packets = YLeaf(YType.uint32, "lisp-v4-encap-packets")

                            self.lisp_v6_decap_packets = YLeaf(YType.uint32, "lisp-v6-decap-packets")

                            self.lisp_v6_encap_packets = YLeaf(YType.uint32, "lisp-v6-encap-packets")

                            self.local_destination_packets = YLeaf(YType.uint32, "local-destination-packets")

                            self.miscellaneous_drops = YLeaf(YType.uint32, "miscellaneous-drops")

                            self.no_route_packets = YLeaf(YType.uint32, "no-route-packets")

                            self.reassembled_packets = YLeaf(YType.uint32, "reassembled-packets")

                            self.reassembly_failures = YLeaf(YType.uint32, "reassembly-failures")

                            self.reassembly_maximum_drops = YLeaf(YType.uint32, "reassembly-maximum-drops")

                            self.reassembly_timeouts = YLeaf(YType.uint32, "reassembly-timeouts")

                            self.received_multicast_packets = YLeaf(YType.uint32, "received-multicast-packets")

                            self.sent_multicast_packets = YLeaf(YType.uint32, "sent-multicast-packets")

                            self.source_routed_packets = YLeaf(YType.uint32, "source-routed-packets")

                            self.too_big_packets = YLeaf(YType.uint32, "too-big-packets")

                            self.total_packets = YLeaf(YType.uint32, "total-packets")

                            self.truncated_packets = YLeaf(YType.uint32, "truncated-packets")

                            self.unknown_option_type_packets = YLeaf(YType.uint32, "unknown-option-type-packets")

                            self.unknown_protocol_packets = YLeaf(YType.uint32, "unknown-protocol-packets")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("bad_header_packets",
                                            "bad_source_address_packets",
                                            "format_errors",
                                            "forwarded_packets",
                                            "fragment_count",
                                            "fragment_failures",
                                            "fragmented_packets",
                                            "fragments",
                                            "generated_packets",
                                            "hop_count_exceeded_packets",
                                            "lisp_decap_errors",
                                            "lisp_encap_errors",
                                            "lisp_v4_decap_packets",
                                            "lisp_v4_encap_packets",
                                            "lisp_v6_decap_packets",
                                            "lisp_v6_encap_packets",
                                            "local_destination_packets",
                                            "miscellaneous_drops",
                                            "no_route_packets",
                                            "reassembled_packets",
                                            "reassembly_failures",
                                            "reassembly_maximum_drops",
                                            "reassembly_timeouts",
                                            "received_multicast_packets",
                                            "sent_multicast_packets",
                                            "source_routed_packets",
                                            "too_big_packets",
                                            "total_packets",
                                            "truncated_packets",
                                            "unknown_option_type_packets",
                                            "unknown_protocol_packets") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.bad_header_packets.is_set or
                                self.bad_source_address_packets.is_set or
                                self.format_errors.is_set or
                                self.forwarded_packets.is_set or
                                self.fragment_count.is_set or
                                self.fragment_failures.is_set or
                                self.fragmented_packets.is_set or
                                self.fragments.is_set or
                                self.generated_packets.is_set or
                                self.hop_count_exceeded_packets.is_set or
                                self.lisp_decap_errors.is_set or
                                self.lisp_encap_errors.is_set or
                                self.lisp_v4_decap_packets.is_set or
                                self.lisp_v4_encap_packets.is_set or
                                self.lisp_v6_decap_packets.is_set or
                                self.lisp_v6_encap_packets.is_set or
                                self.local_destination_packets.is_set or
                                self.miscellaneous_drops.is_set or
                                self.no_route_packets.is_set or
                                self.reassembled_packets.is_set or
                                self.reassembly_failures.is_set or
                                self.reassembly_maximum_drops.is_set or
                                self.reassembly_timeouts.is_set or
                                self.received_multicast_packets.is_set or
                                self.sent_multicast_packets.is_set or
                                self.source_routed_packets.is_set or
                                self.too_big_packets.is_set or
                                self.total_packets.is_set or
                                self.truncated_packets.is_set or
                                self.unknown_option_type_packets.is_set or
                                self.unknown_protocol_packets.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.bad_header_packets.yfilter != YFilter.not_set or
                                self.bad_source_address_packets.yfilter != YFilter.not_set or
                                self.format_errors.yfilter != YFilter.not_set or
                                self.forwarded_packets.yfilter != YFilter.not_set or
                                self.fragment_count.yfilter != YFilter.not_set or
                                self.fragment_failures.yfilter != YFilter.not_set or
                                self.fragmented_packets.yfilter != YFilter.not_set or
                                self.fragments.yfilter != YFilter.not_set or
                                self.generated_packets.yfilter != YFilter.not_set or
                                self.hop_count_exceeded_packets.yfilter != YFilter.not_set or
                                self.lisp_decap_errors.yfilter != YFilter.not_set or
                                self.lisp_encap_errors.yfilter != YFilter.not_set or
                                self.lisp_v4_decap_packets.yfilter != YFilter.not_set or
                                self.lisp_v4_encap_packets.yfilter != YFilter.not_set or
                                self.lisp_v6_decap_packets.yfilter != YFilter.not_set or
                                self.lisp_v6_encap_packets.yfilter != YFilter.not_set or
                                self.local_destination_packets.yfilter != YFilter.not_set or
                                self.miscellaneous_drops.yfilter != YFilter.not_set or
                                self.no_route_packets.yfilter != YFilter.not_set or
                                self.reassembled_packets.yfilter != YFilter.not_set or
                                self.reassembly_failures.yfilter != YFilter.not_set or
                                self.reassembly_maximum_drops.yfilter != YFilter.not_set or
                                self.reassembly_timeouts.yfilter != YFilter.not_set or
                                self.received_multicast_packets.yfilter != YFilter.not_set or
                                self.sent_multicast_packets.yfilter != YFilter.not_set or
                                self.source_routed_packets.yfilter != YFilter.not_set or
                                self.too_big_packets.yfilter != YFilter.not_set or
                                self.total_packets.yfilter != YFilter.not_set or
                                self.truncated_packets.yfilter != YFilter.not_set or
                                self.unknown_option_type_packets.yfilter != YFilter.not_set or
                                self.unknown_protocol_packets.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv6" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.bad_header_packets.is_set or self.bad_header_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bad_header_packets.get_name_leafdata())
                            if (self.bad_source_address_packets.is_set or self.bad_source_address_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bad_source_address_packets.get_name_leafdata())
                            if (self.format_errors.is_set or self.format_errors.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.format_errors.get_name_leafdata())
                            if (self.forwarded_packets.is_set or self.forwarded_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.forwarded_packets.get_name_leafdata())
                            if (self.fragment_count.is_set or self.fragment_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fragment_count.get_name_leafdata())
                            if (self.fragment_failures.is_set or self.fragment_failures.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fragment_failures.get_name_leafdata())
                            if (self.fragmented_packets.is_set or self.fragmented_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fragmented_packets.get_name_leafdata())
                            if (self.fragments.is_set or self.fragments.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fragments.get_name_leafdata())
                            if (self.generated_packets.is_set or self.generated_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.generated_packets.get_name_leafdata())
                            if (self.hop_count_exceeded_packets.is_set or self.hop_count_exceeded_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hop_count_exceeded_packets.get_name_leafdata())
                            if (self.lisp_decap_errors.is_set or self.lisp_decap_errors.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.lisp_decap_errors.get_name_leafdata())
                            if (self.lisp_encap_errors.is_set or self.lisp_encap_errors.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.lisp_encap_errors.get_name_leafdata())
                            if (self.lisp_v4_decap_packets.is_set or self.lisp_v4_decap_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.lisp_v4_decap_packets.get_name_leafdata())
                            if (self.lisp_v4_encap_packets.is_set or self.lisp_v4_encap_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.lisp_v4_encap_packets.get_name_leafdata())
                            if (self.lisp_v6_decap_packets.is_set or self.lisp_v6_decap_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.lisp_v6_decap_packets.get_name_leafdata())
                            if (self.lisp_v6_encap_packets.is_set or self.lisp_v6_encap_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.lisp_v6_encap_packets.get_name_leafdata())
                            if (self.local_destination_packets.is_set or self.local_destination_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.local_destination_packets.get_name_leafdata())
                            if (self.miscellaneous_drops.is_set or self.miscellaneous_drops.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.miscellaneous_drops.get_name_leafdata())
                            if (self.no_route_packets.is_set or self.no_route_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_route_packets.get_name_leafdata())
                            if (self.reassembled_packets.is_set or self.reassembled_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reassembled_packets.get_name_leafdata())
                            if (self.reassembly_failures.is_set or self.reassembly_failures.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reassembly_failures.get_name_leafdata())
                            if (self.reassembly_maximum_drops.is_set or self.reassembly_maximum_drops.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reassembly_maximum_drops.get_name_leafdata())
                            if (self.reassembly_timeouts.is_set or self.reassembly_timeouts.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reassembly_timeouts.get_name_leafdata())
                            if (self.received_multicast_packets.is_set or self.received_multicast_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_multicast_packets.get_name_leafdata())
                            if (self.sent_multicast_packets.is_set or self.sent_multicast_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_multicast_packets.get_name_leafdata())
                            if (self.source_routed_packets.is_set or self.source_routed_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_routed_packets.get_name_leafdata())
                            if (self.too_big_packets.is_set or self.too_big_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.too_big_packets.get_name_leafdata())
                            if (self.total_packets.is_set or self.total_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_packets.get_name_leafdata())
                            if (self.truncated_packets.is_set or self.truncated_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.truncated_packets.get_name_leafdata())
                            if (self.unknown_option_type_packets.is_set or self.unknown_option_type_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.unknown_option_type_packets.get_name_leafdata())
                            if (self.unknown_protocol_packets.is_set or self.unknown_protocol_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.unknown_protocol_packets.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bad-header-packets" or name == "bad-source-address-packets" or name == "format-errors" or name == "forwarded-packets" or name == "fragment-count" or name == "fragment-failures" or name == "fragmented-packets" or name == "fragments" or name == "generated-packets" or name == "hop-count-exceeded-packets" or name == "lisp-decap-errors" or name == "lisp-encap-errors" or name == "lisp-v4-decap-packets" or name == "lisp-v4-encap-packets" or name == "lisp-v6-decap-packets" or name == "lisp-v6-encap-packets" or name == "local-destination-packets" or name == "miscellaneous-drops" or name == "no-route-packets" or name == "reassembled-packets" or name == "reassembly-failures" or name == "reassembly-maximum-drops" or name == "reassembly-timeouts" or name == "received-multicast-packets" or name == "sent-multicast-packets" or name == "source-routed-packets" or name == "too-big-packets" or name == "total-packets" or name == "truncated-packets" or name == "unknown-option-type-packets" or name == "unknown-protocol-packets"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "bad-header-packets"):
                                self.bad_header_packets = value
                                self.bad_header_packets.value_namespace = name_space
                                self.bad_header_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "bad-source-address-packets"):
                                self.bad_source_address_packets = value
                                self.bad_source_address_packets.value_namespace = name_space
                                self.bad_source_address_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "format-errors"):
                                self.format_errors = value
                                self.format_errors.value_namespace = name_space
                                self.format_errors.value_namespace_prefix = name_space_prefix
                            if(value_path == "forwarded-packets"):
                                self.forwarded_packets = value
                                self.forwarded_packets.value_namespace = name_space
                                self.forwarded_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "fragment-count"):
                                self.fragment_count = value
                                self.fragment_count.value_namespace = name_space
                                self.fragment_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "fragment-failures"):
                                self.fragment_failures = value
                                self.fragment_failures.value_namespace = name_space
                                self.fragment_failures.value_namespace_prefix = name_space_prefix
                            if(value_path == "fragmented-packets"):
                                self.fragmented_packets = value
                                self.fragmented_packets.value_namespace = name_space
                                self.fragmented_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "fragments"):
                                self.fragments = value
                                self.fragments.value_namespace = name_space
                                self.fragments.value_namespace_prefix = name_space_prefix
                            if(value_path == "generated-packets"):
                                self.generated_packets = value
                                self.generated_packets.value_namespace = name_space
                                self.generated_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "hop-count-exceeded-packets"):
                                self.hop_count_exceeded_packets = value
                                self.hop_count_exceeded_packets.value_namespace = name_space
                                self.hop_count_exceeded_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "lisp-decap-errors"):
                                self.lisp_decap_errors = value
                                self.lisp_decap_errors.value_namespace = name_space
                                self.lisp_decap_errors.value_namespace_prefix = name_space_prefix
                            if(value_path == "lisp-encap-errors"):
                                self.lisp_encap_errors = value
                                self.lisp_encap_errors.value_namespace = name_space
                                self.lisp_encap_errors.value_namespace_prefix = name_space_prefix
                            if(value_path == "lisp-v4-decap-packets"):
                                self.lisp_v4_decap_packets = value
                                self.lisp_v4_decap_packets.value_namespace = name_space
                                self.lisp_v4_decap_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "lisp-v4-encap-packets"):
                                self.lisp_v4_encap_packets = value
                                self.lisp_v4_encap_packets.value_namespace = name_space
                                self.lisp_v4_encap_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "lisp-v6-decap-packets"):
                                self.lisp_v6_decap_packets = value
                                self.lisp_v6_decap_packets.value_namespace = name_space
                                self.lisp_v6_decap_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "lisp-v6-encap-packets"):
                                self.lisp_v6_encap_packets = value
                                self.lisp_v6_encap_packets.value_namespace = name_space
                                self.lisp_v6_encap_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "local-destination-packets"):
                                self.local_destination_packets = value
                                self.local_destination_packets.value_namespace = name_space
                                self.local_destination_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "miscellaneous-drops"):
                                self.miscellaneous_drops = value
                                self.miscellaneous_drops.value_namespace = name_space
                                self.miscellaneous_drops.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-route-packets"):
                                self.no_route_packets = value
                                self.no_route_packets.value_namespace = name_space
                                self.no_route_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "reassembled-packets"):
                                self.reassembled_packets = value
                                self.reassembled_packets.value_namespace = name_space
                                self.reassembled_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "reassembly-failures"):
                                self.reassembly_failures = value
                                self.reassembly_failures.value_namespace = name_space
                                self.reassembly_failures.value_namespace_prefix = name_space_prefix
                            if(value_path == "reassembly-maximum-drops"):
                                self.reassembly_maximum_drops = value
                                self.reassembly_maximum_drops.value_namespace = name_space
                                self.reassembly_maximum_drops.value_namespace_prefix = name_space_prefix
                            if(value_path == "reassembly-timeouts"):
                                self.reassembly_timeouts = value
                                self.reassembly_timeouts.value_namespace = name_space
                                self.reassembly_timeouts.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-multicast-packets"):
                                self.received_multicast_packets = value
                                self.received_multicast_packets.value_namespace = name_space
                                self.received_multicast_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-multicast-packets"):
                                self.sent_multicast_packets = value
                                self.sent_multicast_packets.value_namespace = name_space
                                self.sent_multicast_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-routed-packets"):
                                self.source_routed_packets = value
                                self.source_routed_packets.value_namespace = name_space
                                self.source_routed_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "too-big-packets"):
                                self.too_big_packets = value
                                self.too_big_packets.value_namespace = name_space
                                self.too_big_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-packets"):
                                self.total_packets = value
                                self.total_packets.value_namespace = name_space
                                self.total_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "truncated-packets"):
                                self.truncated_packets = value
                                self.truncated_packets.value_namespace = name_space
                                self.truncated_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "unknown-option-type-packets"):
                                self.unknown_option_type_packets = value
                                self.unknown_option_type_packets.value_namespace = name_space
                                self.unknown_option_type_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "unknown-protocol-packets"):
                                self.unknown_protocol_packets = value
                                self.unknown_protocol_packets.value_namespace = name_space
                                self.unknown_protocol_packets.value_namespace_prefix = name_space_prefix


                    class Icmp(Entity):
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
                            super(Ipv6Io.Nodes.Node.Statistics.Traffic.Icmp, self).__init__()

                            self.yang_name = "icmp"
                            self.yang_parent_name = "traffic"

                            self.checksum_error_messages = YLeaf(YType.uint32, "checksum-error-messages")

                            self.output_messages = YLeaf(YType.uint32, "output-messages")

                            self.received_echo_reply_messages = YLeaf(YType.uint32, "received-echo-reply-messages")

                            self.received_echo_request_messages = YLeaf(YType.uint32, "received-echo-request-messages")

                            self.received_hop_count_expired_messages = YLeaf(YType.uint32, "received-hop-count-expired-messages")

                            self.received_parameter_error_messages = YLeaf(YType.uint32, "received-parameter-error-messages")

                            self.received_parameter_header_messages = YLeaf(YType.uint32, "received-parameter-header-messages")

                            self.received_parameter_option_messages = YLeaf(YType.uint32, "received-parameter-option-messages")

                            self.received_parameter_unknown_type_messages = YLeaf(YType.uint32, "received-parameter-unknown-type-messages")

                            self.received_reassembly_timeouts = YLeaf(YType.uint32, "received-reassembly-timeouts")

                            self.received_too_big_messages = YLeaf(YType.uint32, "received-too-big-messages")

                            self.received_unknown_timeout_messages = YLeaf(YType.uint32, "received-unknown-timeout-messages")

                            self.received_unreachable_address_messages = YLeaf(YType.uint32, "received-unreachable-address-messages")

                            self.received_unreachable_admin_messages = YLeaf(YType.uint32, "received-unreachable-admin-messages")

                            self.received_unreachable_neighbor_messages = YLeaf(YType.uint32, "received-unreachable-neighbor-messages")

                            self.received_unreachable_port_messages = YLeaf(YType.uint32, "received-unreachable-port-messages")

                            self.received_unreachable_routing_messages = YLeaf(YType.uint32, "received-unreachable-routing-messages")

                            self.received_unreachable_unknown_type_messages = YLeaf(YType.uint32, "received-unreachable-unknown-type-messages")

                            self.sent_echo_reply_messages = YLeaf(YType.uint32, "sent-echo-reply-messages")

                            self.sent_echo_request_messages = YLeaf(YType.uint32, "sent-echo-request-messages")

                            self.sent_hop_count_expired_messages = YLeaf(YType.uint32, "sent-hop-count-expired-messages")

                            self.sent_parameter_error_messages = YLeaf(YType.uint32, "sent-parameter-error-messages")

                            self.sent_parameter_header_messages = YLeaf(YType.uint32, "sent-parameter-header-messages")

                            self.sent_parameter_option_messages = YLeaf(YType.uint32, "sent-parameter-option-messages")

                            self.sent_parameter_unknown_type_messages = YLeaf(YType.uint32, "sent-parameter-unknown-type-messages")

                            self.sent_rate_limited_packets = YLeaf(YType.uint32, "sent-rate-limited-packets")

                            self.sent_reassembly_timeouts = YLeaf(YType.uint32, "sent-reassembly-timeouts")

                            self.sent_too_big_messages = YLeaf(YType.uint32, "sent-too-big-messages")

                            self.sent_unknown_timeout_messages = YLeaf(YType.uint32, "sent-unknown-timeout-messages")

                            self.sent_unreachable_address_messages = YLeaf(YType.uint32, "sent-unreachable-address-messages")

                            self.sent_unreachable_admin_messages = YLeaf(YType.uint32, "sent-unreachable-admin-messages")

                            self.sent_unreachable_neighbor_messages = YLeaf(YType.uint32, "sent-unreachable-neighbor-messages")

                            self.sent_unreachable_port_messages = YLeaf(YType.uint32, "sent-unreachable-port-messages")

                            self.sent_unreachable_routing_messages = YLeaf(YType.uint32, "sent-unreachable-routing-messages")

                            self.sent_unreachable_unknown_type_messages = YLeaf(YType.uint32, "sent-unreachable-unknown-type-messages")

                            self.too_short_error_messages = YLeaf(YType.uint32, "too-short-error-messages")

                            self.total_messages = YLeaf(YType.uint32, "total-messages")

                            self.unknown_error_type_messages = YLeaf(YType.uint32, "unknown-error-type-messages")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("checksum_error_messages",
                                            "output_messages",
                                            "received_echo_reply_messages",
                                            "received_echo_request_messages",
                                            "received_hop_count_expired_messages",
                                            "received_parameter_error_messages",
                                            "received_parameter_header_messages",
                                            "received_parameter_option_messages",
                                            "received_parameter_unknown_type_messages",
                                            "received_reassembly_timeouts",
                                            "received_too_big_messages",
                                            "received_unknown_timeout_messages",
                                            "received_unreachable_address_messages",
                                            "received_unreachable_admin_messages",
                                            "received_unreachable_neighbor_messages",
                                            "received_unreachable_port_messages",
                                            "received_unreachable_routing_messages",
                                            "received_unreachable_unknown_type_messages",
                                            "sent_echo_reply_messages",
                                            "sent_echo_request_messages",
                                            "sent_hop_count_expired_messages",
                                            "sent_parameter_error_messages",
                                            "sent_parameter_header_messages",
                                            "sent_parameter_option_messages",
                                            "sent_parameter_unknown_type_messages",
                                            "sent_rate_limited_packets",
                                            "sent_reassembly_timeouts",
                                            "sent_too_big_messages",
                                            "sent_unknown_timeout_messages",
                                            "sent_unreachable_address_messages",
                                            "sent_unreachable_admin_messages",
                                            "sent_unreachable_neighbor_messages",
                                            "sent_unreachable_port_messages",
                                            "sent_unreachable_routing_messages",
                                            "sent_unreachable_unknown_type_messages",
                                            "too_short_error_messages",
                                            "total_messages",
                                            "unknown_error_type_messages") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv6Io.Nodes.Node.Statistics.Traffic.Icmp, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv6Io.Nodes.Node.Statistics.Traffic.Icmp, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.checksum_error_messages.is_set or
                                self.output_messages.is_set or
                                self.received_echo_reply_messages.is_set or
                                self.received_echo_request_messages.is_set or
                                self.received_hop_count_expired_messages.is_set or
                                self.received_parameter_error_messages.is_set or
                                self.received_parameter_header_messages.is_set or
                                self.received_parameter_option_messages.is_set or
                                self.received_parameter_unknown_type_messages.is_set or
                                self.received_reassembly_timeouts.is_set or
                                self.received_too_big_messages.is_set or
                                self.received_unknown_timeout_messages.is_set or
                                self.received_unreachable_address_messages.is_set or
                                self.received_unreachable_admin_messages.is_set or
                                self.received_unreachable_neighbor_messages.is_set or
                                self.received_unreachable_port_messages.is_set or
                                self.received_unreachable_routing_messages.is_set or
                                self.received_unreachable_unknown_type_messages.is_set or
                                self.sent_echo_reply_messages.is_set or
                                self.sent_echo_request_messages.is_set or
                                self.sent_hop_count_expired_messages.is_set or
                                self.sent_parameter_error_messages.is_set or
                                self.sent_parameter_header_messages.is_set or
                                self.sent_parameter_option_messages.is_set or
                                self.sent_parameter_unknown_type_messages.is_set or
                                self.sent_rate_limited_packets.is_set or
                                self.sent_reassembly_timeouts.is_set or
                                self.sent_too_big_messages.is_set or
                                self.sent_unknown_timeout_messages.is_set or
                                self.sent_unreachable_address_messages.is_set or
                                self.sent_unreachable_admin_messages.is_set or
                                self.sent_unreachable_neighbor_messages.is_set or
                                self.sent_unreachable_port_messages.is_set or
                                self.sent_unreachable_routing_messages.is_set or
                                self.sent_unreachable_unknown_type_messages.is_set or
                                self.too_short_error_messages.is_set or
                                self.total_messages.is_set or
                                self.unknown_error_type_messages.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.checksum_error_messages.yfilter != YFilter.not_set or
                                self.output_messages.yfilter != YFilter.not_set or
                                self.received_echo_reply_messages.yfilter != YFilter.not_set or
                                self.received_echo_request_messages.yfilter != YFilter.not_set or
                                self.received_hop_count_expired_messages.yfilter != YFilter.not_set or
                                self.received_parameter_error_messages.yfilter != YFilter.not_set or
                                self.received_parameter_header_messages.yfilter != YFilter.not_set or
                                self.received_parameter_option_messages.yfilter != YFilter.not_set or
                                self.received_parameter_unknown_type_messages.yfilter != YFilter.not_set or
                                self.received_reassembly_timeouts.yfilter != YFilter.not_set or
                                self.received_too_big_messages.yfilter != YFilter.not_set or
                                self.received_unknown_timeout_messages.yfilter != YFilter.not_set or
                                self.received_unreachable_address_messages.yfilter != YFilter.not_set or
                                self.received_unreachable_admin_messages.yfilter != YFilter.not_set or
                                self.received_unreachable_neighbor_messages.yfilter != YFilter.not_set or
                                self.received_unreachable_port_messages.yfilter != YFilter.not_set or
                                self.received_unreachable_routing_messages.yfilter != YFilter.not_set or
                                self.received_unreachable_unknown_type_messages.yfilter != YFilter.not_set or
                                self.sent_echo_reply_messages.yfilter != YFilter.not_set or
                                self.sent_echo_request_messages.yfilter != YFilter.not_set or
                                self.sent_hop_count_expired_messages.yfilter != YFilter.not_set or
                                self.sent_parameter_error_messages.yfilter != YFilter.not_set or
                                self.sent_parameter_header_messages.yfilter != YFilter.not_set or
                                self.sent_parameter_option_messages.yfilter != YFilter.not_set or
                                self.sent_parameter_unknown_type_messages.yfilter != YFilter.not_set or
                                self.sent_rate_limited_packets.yfilter != YFilter.not_set or
                                self.sent_reassembly_timeouts.yfilter != YFilter.not_set or
                                self.sent_too_big_messages.yfilter != YFilter.not_set or
                                self.sent_unknown_timeout_messages.yfilter != YFilter.not_set or
                                self.sent_unreachable_address_messages.yfilter != YFilter.not_set or
                                self.sent_unreachable_admin_messages.yfilter != YFilter.not_set or
                                self.sent_unreachable_neighbor_messages.yfilter != YFilter.not_set or
                                self.sent_unreachable_port_messages.yfilter != YFilter.not_set or
                                self.sent_unreachable_routing_messages.yfilter != YFilter.not_set or
                                self.sent_unreachable_unknown_type_messages.yfilter != YFilter.not_set or
                                self.too_short_error_messages.yfilter != YFilter.not_set or
                                self.total_messages.yfilter != YFilter.not_set or
                                self.unknown_error_type_messages.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "icmp" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.checksum_error_messages.is_set or self.checksum_error_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.checksum_error_messages.get_name_leafdata())
                            if (self.output_messages.is_set or self.output_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.output_messages.get_name_leafdata())
                            if (self.received_echo_reply_messages.is_set or self.received_echo_reply_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_echo_reply_messages.get_name_leafdata())
                            if (self.received_echo_request_messages.is_set or self.received_echo_request_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_echo_request_messages.get_name_leafdata())
                            if (self.received_hop_count_expired_messages.is_set or self.received_hop_count_expired_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_hop_count_expired_messages.get_name_leafdata())
                            if (self.received_parameter_error_messages.is_set or self.received_parameter_error_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_parameter_error_messages.get_name_leafdata())
                            if (self.received_parameter_header_messages.is_set or self.received_parameter_header_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_parameter_header_messages.get_name_leafdata())
                            if (self.received_parameter_option_messages.is_set or self.received_parameter_option_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_parameter_option_messages.get_name_leafdata())
                            if (self.received_parameter_unknown_type_messages.is_set or self.received_parameter_unknown_type_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_parameter_unknown_type_messages.get_name_leafdata())
                            if (self.received_reassembly_timeouts.is_set or self.received_reassembly_timeouts.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_reassembly_timeouts.get_name_leafdata())
                            if (self.received_too_big_messages.is_set or self.received_too_big_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_too_big_messages.get_name_leafdata())
                            if (self.received_unknown_timeout_messages.is_set or self.received_unknown_timeout_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_unknown_timeout_messages.get_name_leafdata())
                            if (self.received_unreachable_address_messages.is_set or self.received_unreachable_address_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_unreachable_address_messages.get_name_leafdata())
                            if (self.received_unreachable_admin_messages.is_set or self.received_unreachable_admin_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_unreachable_admin_messages.get_name_leafdata())
                            if (self.received_unreachable_neighbor_messages.is_set or self.received_unreachable_neighbor_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_unreachable_neighbor_messages.get_name_leafdata())
                            if (self.received_unreachable_port_messages.is_set or self.received_unreachable_port_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_unreachable_port_messages.get_name_leafdata())
                            if (self.received_unreachable_routing_messages.is_set or self.received_unreachable_routing_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_unreachable_routing_messages.get_name_leafdata())
                            if (self.received_unreachable_unknown_type_messages.is_set or self.received_unreachable_unknown_type_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_unreachable_unknown_type_messages.get_name_leafdata())
                            if (self.sent_echo_reply_messages.is_set or self.sent_echo_reply_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_echo_reply_messages.get_name_leafdata())
                            if (self.sent_echo_request_messages.is_set or self.sent_echo_request_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_echo_request_messages.get_name_leafdata())
                            if (self.sent_hop_count_expired_messages.is_set or self.sent_hop_count_expired_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_hop_count_expired_messages.get_name_leafdata())
                            if (self.sent_parameter_error_messages.is_set or self.sent_parameter_error_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_parameter_error_messages.get_name_leafdata())
                            if (self.sent_parameter_header_messages.is_set or self.sent_parameter_header_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_parameter_header_messages.get_name_leafdata())
                            if (self.sent_parameter_option_messages.is_set or self.sent_parameter_option_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_parameter_option_messages.get_name_leafdata())
                            if (self.sent_parameter_unknown_type_messages.is_set or self.sent_parameter_unknown_type_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_parameter_unknown_type_messages.get_name_leafdata())
                            if (self.sent_rate_limited_packets.is_set or self.sent_rate_limited_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_rate_limited_packets.get_name_leafdata())
                            if (self.sent_reassembly_timeouts.is_set or self.sent_reassembly_timeouts.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_reassembly_timeouts.get_name_leafdata())
                            if (self.sent_too_big_messages.is_set or self.sent_too_big_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_too_big_messages.get_name_leafdata())
                            if (self.sent_unknown_timeout_messages.is_set or self.sent_unknown_timeout_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_unknown_timeout_messages.get_name_leafdata())
                            if (self.sent_unreachable_address_messages.is_set or self.sent_unreachable_address_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_unreachable_address_messages.get_name_leafdata())
                            if (self.sent_unreachable_admin_messages.is_set or self.sent_unreachable_admin_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_unreachable_admin_messages.get_name_leafdata())
                            if (self.sent_unreachable_neighbor_messages.is_set or self.sent_unreachable_neighbor_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_unreachable_neighbor_messages.get_name_leafdata())
                            if (self.sent_unreachable_port_messages.is_set or self.sent_unreachable_port_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_unreachable_port_messages.get_name_leafdata())
                            if (self.sent_unreachable_routing_messages.is_set or self.sent_unreachable_routing_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_unreachable_routing_messages.get_name_leafdata())
                            if (self.sent_unreachable_unknown_type_messages.is_set or self.sent_unreachable_unknown_type_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_unreachable_unknown_type_messages.get_name_leafdata())
                            if (self.too_short_error_messages.is_set or self.too_short_error_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.too_short_error_messages.get_name_leafdata())
                            if (self.total_messages.is_set or self.total_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_messages.get_name_leafdata())
                            if (self.unknown_error_type_messages.is_set or self.unknown_error_type_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.unknown_error_type_messages.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "checksum-error-messages" or name == "output-messages" or name == "received-echo-reply-messages" or name == "received-echo-request-messages" or name == "received-hop-count-expired-messages" or name == "received-parameter-error-messages" or name == "received-parameter-header-messages" or name == "received-parameter-option-messages" or name == "received-parameter-unknown-type-messages" or name == "received-reassembly-timeouts" or name == "received-too-big-messages" or name == "received-unknown-timeout-messages" or name == "received-unreachable-address-messages" or name == "received-unreachable-admin-messages" or name == "received-unreachable-neighbor-messages" or name == "received-unreachable-port-messages" or name == "received-unreachable-routing-messages" or name == "received-unreachable-unknown-type-messages" or name == "sent-echo-reply-messages" or name == "sent-echo-request-messages" or name == "sent-hop-count-expired-messages" or name == "sent-parameter-error-messages" or name == "sent-parameter-header-messages" or name == "sent-parameter-option-messages" or name == "sent-parameter-unknown-type-messages" or name == "sent-rate-limited-packets" or name == "sent-reassembly-timeouts" or name == "sent-too-big-messages" or name == "sent-unknown-timeout-messages" or name == "sent-unreachable-address-messages" or name == "sent-unreachable-admin-messages" or name == "sent-unreachable-neighbor-messages" or name == "sent-unreachable-port-messages" or name == "sent-unreachable-routing-messages" or name == "sent-unreachable-unknown-type-messages" or name == "too-short-error-messages" or name == "total-messages" or name == "unknown-error-type-messages"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "checksum-error-messages"):
                                self.checksum_error_messages = value
                                self.checksum_error_messages.value_namespace = name_space
                                self.checksum_error_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "output-messages"):
                                self.output_messages = value
                                self.output_messages.value_namespace = name_space
                                self.output_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-echo-reply-messages"):
                                self.received_echo_reply_messages = value
                                self.received_echo_reply_messages.value_namespace = name_space
                                self.received_echo_reply_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-echo-request-messages"):
                                self.received_echo_request_messages = value
                                self.received_echo_request_messages.value_namespace = name_space
                                self.received_echo_request_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-hop-count-expired-messages"):
                                self.received_hop_count_expired_messages = value
                                self.received_hop_count_expired_messages.value_namespace = name_space
                                self.received_hop_count_expired_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-parameter-error-messages"):
                                self.received_parameter_error_messages = value
                                self.received_parameter_error_messages.value_namespace = name_space
                                self.received_parameter_error_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-parameter-header-messages"):
                                self.received_parameter_header_messages = value
                                self.received_parameter_header_messages.value_namespace = name_space
                                self.received_parameter_header_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-parameter-option-messages"):
                                self.received_parameter_option_messages = value
                                self.received_parameter_option_messages.value_namespace = name_space
                                self.received_parameter_option_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-parameter-unknown-type-messages"):
                                self.received_parameter_unknown_type_messages = value
                                self.received_parameter_unknown_type_messages.value_namespace = name_space
                                self.received_parameter_unknown_type_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-reassembly-timeouts"):
                                self.received_reassembly_timeouts = value
                                self.received_reassembly_timeouts.value_namespace = name_space
                                self.received_reassembly_timeouts.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-too-big-messages"):
                                self.received_too_big_messages = value
                                self.received_too_big_messages.value_namespace = name_space
                                self.received_too_big_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-unknown-timeout-messages"):
                                self.received_unknown_timeout_messages = value
                                self.received_unknown_timeout_messages.value_namespace = name_space
                                self.received_unknown_timeout_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-unreachable-address-messages"):
                                self.received_unreachable_address_messages = value
                                self.received_unreachable_address_messages.value_namespace = name_space
                                self.received_unreachable_address_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-unreachable-admin-messages"):
                                self.received_unreachable_admin_messages = value
                                self.received_unreachable_admin_messages.value_namespace = name_space
                                self.received_unreachable_admin_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-unreachable-neighbor-messages"):
                                self.received_unreachable_neighbor_messages = value
                                self.received_unreachable_neighbor_messages.value_namespace = name_space
                                self.received_unreachable_neighbor_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-unreachable-port-messages"):
                                self.received_unreachable_port_messages = value
                                self.received_unreachable_port_messages.value_namespace = name_space
                                self.received_unreachable_port_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-unreachable-routing-messages"):
                                self.received_unreachable_routing_messages = value
                                self.received_unreachable_routing_messages.value_namespace = name_space
                                self.received_unreachable_routing_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-unreachable-unknown-type-messages"):
                                self.received_unreachable_unknown_type_messages = value
                                self.received_unreachable_unknown_type_messages.value_namespace = name_space
                                self.received_unreachable_unknown_type_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-echo-reply-messages"):
                                self.sent_echo_reply_messages = value
                                self.sent_echo_reply_messages.value_namespace = name_space
                                self.sent_echo_reply_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-echo-request-messages"):
                                self.sent_echo_request_messages = value
                                self.sent_echo_request_messages.value_namespace = name_space
                                self.sent_echo_request_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-hop-count-expired-messages"):
                                self.sent_hop_count_expired_messages = value
                                self.sent_hop_count_expired_messages.value_namespace = name_space
                                self.sent_hop_count_expired_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-parameter-error-messages"):
                                self.sent_parameter_error_messages = value
                                self.sent_parameter_error_messages.value_namespace = name_space
                                self.sent_parameter_error_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-parameter-header-messages"):
                                self.sent_parameter_header_messages = value
                                self.sent_parameter_header_messages.value_namespace = name_space
                                self.sent_parameter_header_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-parameter-option-messages"):
                                self.sent_parameter_option_messages = value
                                self.sent_parameter_option_messages.value_namespace = name_space
                                self.sent_parameter_option_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-parameter-unknown-type-messages"):
                                self.sent_parameter_unknown_type_messages = value
                                self.sent_parameter_unknown_type_messages.value_namespace = name_space
                                self.sent_parameter_unknown_type_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-rate-limited-packets"):
                                self.sent_rate_limited_packets = value
                                self.sent_rate_limited_packets.value_namespace = name_space
                                self.sent_rate_limited_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-reassembly-timeouts"):
                                self.sent_reassembly_timeouts = value
                                self.sent_reassembly_timeouts.value_namespace = name_space
                                self.sent_reassembly_timeouts.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-too-big-messages"):
                                self.sent_too_big_messages = value
                                self.sent_too_big_messages.value_namespace = name_space
                                self.sent_too_big_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-unknown-timeout-messages"):
                                self.sent_unknown_timeout_messages = value
                                self.sent_unknown_timeout_messages.value_namespace = name_space
                                self.sent_unknown_timeout_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-unreachable-address-messages"):
                                self.sent_unreachable_address_messages = value
                                self.sent_unreachable_address_messages.value_namespace = name_space
                                self.sent_unreachable_address_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-unreachable-admin-messages"):
                                self.sent_unreachable_admin_messages = value
                                self.sent_unreachable_admin_messages.value_namespace = name_space
                                self.sent_unreachable_admin_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-unreachable-neighbor-messages"):
                                self.sent_unreachable_neighbor_messages = value
                                self.sent_unreachable_neighbor_messages.value_namespace = name_space
                                self.sent_unreachable_neighbor_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-unreachable-port-messages"):
                                self.sent_unreachable_port_messages = value
                                self.sent_unreachable_port_messages.value_namespace = name_space
                                self.sent_unreachable_port_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-unreachable-routing-messages"):
                                self.sent_unreachable_routing_messages = value
                                self.sent_unreachable_routing_messages.value_namespace = name_space
                                self.sent_unreachable_routing_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-unreachable-unknown-type-messages"):
                                self.sent_unreachable_unknown_type_messages = value
                                self.sent_unreachable_unknown_type_messages.value_namespace = name_space
                                self.sent_unreachable_unknown_type_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "too-short-error-messages"):
                                self.too_short_error_messages = value
                                self.too_short_error_messages.value_namespace = name_space
                                self.too_short_error_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-messages"):
                                self.total_messages = value
                                self.total_messages.value_namespace = name_space
                                self.total_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "unknown-error-type-messages"):
                                self.unknown_error_type_messages = value
                                self.unknown_error_type_messages.value_namespace = name_space
                                self.unknown_error_type_messages.value_namespace_prefix = name_space_prefix


                    class Ipv6NodeDiscovery(Entity):
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
                            super(Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6NodeDiscovery, self).__init__()

                            self.yang_name = "ipv6-node-discovery"
                            self.yang_parent_name = "traffic"

                            self.received_neighbor_advertisement_messages = YLeaf(YType.uint32, "received-neighbor-advertisement-messages")

                            self.received_neighbor_solicitation_messages = YLeaf(YType.uint32, "received-neighbor-solicitation-messages")

                            self.received_redirect_messages = YLeaf(YType.uint32, "received-redirect-messages")

                            self.received_router_advertisement_messages = YLeaf(YType.uint32, "received-router-advertisement-messages")

                            self.received_router_solicitation_messages = YLeaf(YType.uint32, "received-router-solicitation-messages")

                            self.sent_neighbor_advertisement_messages = YLeaf(YType.uint32, "sent-neighbor-advertisement-messages")

                            self.sent_neighbor_solicitation_messages = YLeaf(YType.uint32, "sent-neighbor-solicitation-messages")

                            self.sent_redirect_messages = YLeaf(YType.uint32, "sent-redirect-messages")

                            self.sent_router_advertisement_messages = YLeaf(YType.uint32, "sent-router-advertisement-messages")

                            self.sent_router_solicitation_messages = YLeaf(YType.uint32, "sent-router-solicitation-messages")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("received_neighbor_advertisement_messages",
                                            "received_neighbor_solicitation_messages",
                                            "received_redirect_messages",
                                            "received_router_advertisement_messages",
                                            "received_router_solicitation_messages",
                                            "sent_neighbor_advertisement_messages",
                                            "sent_neighbor_solicitation_messages",
                                            "sent_redirect_messages",
                                            "sent_router_advertisement_messages",
                                            "sent_router_solicitation_messages") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6NodeDiscovery, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6NodeDiscovery, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.received_neighbor_advertisement_messages.is_set or
                                self.received_neighbor_solicitation_messages.is_set or
                                self.received_redirect_messages.is_set or
                                self.received_router_advertisement_messages.is_set or
                                self.received_router_solicitation_messages.is_set or
                                self.sent_neighbor_advertisement_messages.is_set or
                                self.sent_neighbor_solicitation_messages.is_set or
                                self.sent_redirect_messages.is_set or
                                self.sent_router_advertisement_messages.is_set or
                                self.sent_router_solicitation_messages.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.received_neighbor_advertisement_messages.yfilter != YFilter.not_set or
                                self.received_neighbor_solicitation_messages.yfilter != YFilter.not_set or
                                self.received_redirect_messages.yfilter != YFilter.not_set or
                                self.received_router_advertisement_messages.yfilter != YFilter.not_set or
                                self.received_router_solicitation_messages.yfilter != YFilter.not_set or
                                self.sent_neighbor_advertisement_messages.yfilter != YFilter.not_set or
                                self.sent_neighbor_solicitation_messages.yfilter != YFilter.not_set or
                                self.sent_redirect_messages.yfilter != YFilter.not_set or
                                self.sent_router_advertisement_messages.yfilter != YFilter.not_set or
                                self.sent_router_solicitation_messages.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv6-node-discovery" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.received_neighbor_advertisement_messages.is_set or self.received_neighbor_advertisement_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_neighbor_advertisement_messages.get_name_leafdata())
                            if (self.received_neighbor_solicitation_messages.is_set or self.received_neighbor_solicitation_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_neighbor_solicitation_messages.get_name_leafdata())
                            if (self.received_redirect_messages.is_set or self.received_redirect_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_redirect_messages.get_name_leafdata())
                            if (self.received_router_advertisement_messages.is_set or self.received_router_advertisement_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_router_advertisement_messages.get_name_leafdata())
                            if (self.received_router_solicitation_messages.is_set or self.received_router_solicitation_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_router_solicitation_messages.get_name_leafdata())
                            if (self.sent_neighbor_advertisement_messages.is_set or self.sent_neighbor_advertisement_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_neighbor_advertisement_messages.get_name_leafdata())
                            if (self.sent_neighbor_solicitation_messages.is_set or self.sent_neighbor_solicitation_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_neighbor_solicitation_messages.get_name_leafdata())
                            if (self.sent_redirect_messages.is_set or self.sent_redirect_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_redirect_messages.get_name_leafdata())
                            if (self.sent_router_advertisement_messages.is_set or self.sent_router_advertisement_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_router_advertisement_messages.get_name_leafdata())
                            if (self.sent_router_solicitation_messages.is_set or self.sent_router_solicitation_messages.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent_router_solicitation_messages.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "received-neighbor-advertisement-messages" or name == "received-neighbor-solicitation-messages" or name == "received-redirect-messages" or name == "received-router-advertisement-messages" or name == "received-router-solicitation-messages" or name == "sent-neighbor-advertisement-messages" or name == "sent-neighbor-solicitation-messages" or name == "sent-redirect-messages" or name == "sent-router-advertisement-messages" or name == "sent-router-solicitation-messages"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "received-neighbor-advertisement-messages"):
                                self.received_neighbor_advertisement_messages = value
                                self.received_neighbor_advertisement_messages.value_namespace = name_space
                                self.received_neighbor_advertisement_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-neighbor-solicitation-messages"):
                                self.received_neighbor_solicitation_messages = value
                                self.received_neighbor_solicitation_messages.value_namespace = name_space
                                self.received_neighbor_solicitation_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-redirect-messages"):
                                self.received_redirect_messages = value
                                self.received_redirect_messages.value_namespace = name_space
                                self.received_redirect_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-router-advertisement-messages"):
                                self.received_router_advertisement_messages = value
                                self.received_router_advertisement_messages.value_namespace = name_space
                                self.received_router_advertisement_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-router-solicitation-messages"):
                                self.received_router_solicitation_messages = value
                                self.received_router_solicitation_messages.value_namespace = name_space
                                self.received_router_solicitation_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-neighbor-advertisement-messages"):
                                self.sent_neighbor_advertisement_messages = value
                                self.sent_neighbor_advertisement_messages.value_namespace = name_space
                                self.sent_neighbor_advertisement_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-neighbor-solicitation-messages"):
                                self.sent_neighbor_solicitation_messages = value
                                self.sent_neighbor_solicitation_messages.value_namespace = name_space
                                self.sent_neighbor_solicitation_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-redirect-messages"):
                                self.sent_redirect_messages = value
                                self.sent_redirect_messages.value_namespace = name_space
                                self.sent_redirect_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-router-advertisement-messages"):
                                self.sent_router_advertisement_messages = value
                                self.sent_router_advertisement_messages.value_namespace = name_space
                                self.sent_router_advertisement_messages.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent-router-solicitation-messages"):
                                self.sent_router_solicitation_messages = value
                                self.sent_router_solicitation_messages.value_namespace = name_space
                                self.sent_router_solicitation_messages.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.icmp is not None and self.icmp.has_data()) or
                            (self.ipv6 is not None and self.ipv6.has_data()) or
                            (self.ipv6_node_discovery is not None and self.ipv6_node_discovery.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.icmp is not None and self.icmp.has_operation()) or
                            (self.ipv6 is not None and self.ipv6.has_operation()) or
                            (self.ipv6_node_discovery is not None and self.ipv6_node_discovery.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "traffic" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "icmp"):
                            if (self.icmp is None):
                                self.icmp = Ipv6Io.Nodes.Node.Statistics.Traffic.Icmp()
                                self.icmp.parent = self
                                self._children_name_map["icmp"] = "icmp"
                            return self.icmp

                        if (child_yang_name == "ipv6"):
                            if (self.ipv6 is None):
                                self.ipv6 = Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6()
                                self.ipv6.parent = self
                                self._children_name_map["ipv6"] = "ipv6"
                            return self.ipv6

                        if (child_yang_name == "ipv6-node-discovery"):
                            if (self.ipv6_node_discovery is None):
                                self.ipv6_node_discovery = Ipv6Io.Nodes.Node.Statistics.Traffic.Ipv6NodeDiscovery()
                                self.ipv6_node_discovery.parent = self
                                self._children_name_map["ipv6_node_discovery"] = "ipv6-node-discovery"
                            return self.ipv6_node_discovery

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "icmp" or name == "ipv6" or name == "ipv6-node-discovery"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.traffic is not None and self.traffic.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.traffic is not None and self.traffic.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "statistics" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "traffic"):
                        if (self.traffic is None):
                            self.traffic = Ipv6Io.Nodes.Node.Statistics.Traffic()
                            self.traffic.parent = self
                            self._children_name_map["traffic"] = "traffic"
                        return self.traffic

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "traffic"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.statistics is not None and self.statistics.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.statistics is not None and self.statistics.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv6-io-oper:ipv6-io/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "statistics"):
                    if (self.statistics is None):
                        self.statistics = Ipv6Io.Nodes.Node.Statistics()
                        self.statistics.parent = self
                        self._children_name_map["statistics"] = "statistics"
                    return self.statistics

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "statistics" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv6-io-oper:ipv6-io/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ipv6Io.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv6-io-oper:ipv6-io" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = Ipv6Io.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Ipv6Io()
        return self._top_entity

