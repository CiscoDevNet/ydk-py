""" Cisco_IOS_XR_asr9k_netflow_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-netflow package operational data.

This module contains definitions
for the following management objects\:
  net\-flow\: NetFlow operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class NetFlow(Entity):
    """
    NetFlow operational data
    
    .. attribute:: statistics
    
    	Node\-specific NetFlow statistics information
    	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics>`
    
    

    """

    _prefix = 'asr9k-netflow-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(NetFlow, self).__init__()
        self._top_entity = None

        self.yang_name = "net-flow"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-netflow-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"statistics" : ("statistics", NetFlow.Statistics)}
        self._child_list_classes = {}

        self.statistics = NetFlow.Statistics()
        self.statistics.parent = self
        self._children_name_map["statistics"] = "statistics"
        self._children_yang_names.add("statistics")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-netflow-oper:net-flow"


    class Statistics(Entity):
        """
        Node\-specific NetFlow statistics information
        
        .. attribute:: statistic
        
        	NetFlow statistics information for a particular node
        	**type**\: list of    :py:class:`Statistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic>`
        
        

        """

        _prefix = 'asr9k-netflow-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(NetFlow.Statistics, self).__init__()

            self.yang_name = "statistics"
            self.yang_parent_name = "net-flow"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"statistic" : ("statistic", NetFlow.Statistics.Statistic)}

            self.statistic = YList(self)
            self._segment_path = lambda: "statistics"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-netflow-oper:net-flow/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NetFlow.Statistics, [], name, value)


        class Statistic(Entity):
            """
            NetFlow statistics information for a particular
            node
            
            .. attribute:: node  <key>
            
            	Node location
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: producer
            
            	NetFlow producer statistics
            	**type**\:   :py:class:`Producer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Producer>`
            
            .. attribute:: server
            
            	NetFlow server statistics
            	**type**\:   :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server>`
            
            

            """

            _prefix = 'asr9k-netflow-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(NetFlow.Statistics.Statistic, self).__init__()

                self.yang_name = "statistic"
                self.yang_parent_name = "statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"producer" : ("producer", NetFlow.Statistics.Statistic.Producer), "server" : ("server", NetFlow.Statistics.Statistic.Server)}
                self._child_list_classes = {}

                self.node = YLeaf(YType.str, "node")

                self.producer = NetFlow.Statistics.Statistic.Producer()
                self.producer.parent = self
                self._children_name_map["producer"] = "producer"
                self._children_yang_names.add("producer")

                self.server = NetFlow.Statistics.Statistic.Server()
                self.server.parent = self
                self._children_name_map["server"] = "server"
                self._children_yang_names.add("server")
                self._segment_path = lambda: "statistic" + "[node='" + self.node.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-netflow-oper:net-flow/statistics/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetFlow.Statistics.Statistic, ['node'], name, value)


            class Producer(Entity):
                """
                NetFlow producer statistics
                
                .. attribute:: statistics
                
                	Statistics information
                	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Producer.Statistics>`
                
                

                """

                _prefix = 'asr9k-netflow-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NetFlow.Statistics.Statistic.Producer, self).__init__()

                    self.yang_name = "producer"
                    self.yang_parent_name = "statistic"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"statistics" : ("statistics", NetFlow.Statistics.Statistic.Producer.Statistics)}
                    self._child_list_classes = {}

                    self.statistics = NetFlow.Statistics.Statistic.Producer.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._children_yang_names.add("statistics")
                    self._segment_path = lambda: "producer"


                class Statistics(Entity):
                    """
                    Statistics information
                    
                    .. attribute:: drops_no_space
                    
                    	Drops (no space)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: drops_others
                    
                    	Drops (others)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: flow_packet_counts
                    
                    	Number of Rxed Flow Packets
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ipv4_egress_flows
                    
                    	IPv4 egress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ipv4_ingress_flows
                    
                    	IPv4 ingress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ipv6_egress_flows
                    
                    	IPv6 egress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ipv6_ingress_flows
                    
                    	IPv6 ingress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: last_cleared
                    
                    	Last time Statistics cleared in 'Mon Jan 1 12\:00 \:00 2xxx' format
                    	**type**\:  str
                    
                    .. attribute:: mpls_egress_flows
                    
                    	MPLS egress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: mpls_ingress_flows
                    
                    	MPLS ingress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: spp_rx_counts
                    
                    	Number of Rxed SPP Packets
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: unknown_egress_flows
                    
                    	Unknown egress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: unknown_ingress_flows
                    
                    	Unknown ingress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: waiting_servers
                    
                    	Number of waiting servers
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'asr9k-netflow-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NetFlow.Statistics.Statistic.Producer.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "producer"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.drops_no_space = YLeaf(YType.uint64, "drops-no-space")

                        self.drops_others = YLeaf(YType.uint64, "drops-others")

                        self.flow_packet_counts = YLeaf(YType.uint64, "flow-packet-counts")

                        self.ipv4_egress_flows = YLeaf(YType.uint64, "ipv4-egress-flows")

                        self.ipv4_ingress_flows = YLeaf(YType.uint64, "ipv4-ingress-flows")

                        self.ipv6_egress_flows = YLeaf(YType.uint64, "ipv6-egress-flows")

                        self.ipv6_ingress_flows = YLeaf(YType.uint64, "ipv6-ingress-flows")

                        self.last_cleared = YLeaf(YType.str, "last-cleared")

                        self.mpls_egress_flows = YLeaf(YType.uint64, "mpls-egress-flows")

                        self.mpls_ingress_flows = YLeaf(YType.uint64, "mpls-ingress-flows")

                        self.spp_rx_counts = YLeaf(YType.uint64, "spp-rx-counts")

                        self.unknown_egress_flows = YLeaf(YType.uint64, "unknown-egress-flows")

                        self.unknown_ingress_flows = YLeaf(YType.uint64, "unknown-ingress-flows")

                        self.waiting_servers = YLeaf(YType.uint64, "waiting-servers")
                        self._segment_path = lambda: "statistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NetFlow.Statistics.Statistic.Producer.Statistics, ['drops_no_space', 'drops_others', 'flow_packet_counts', 'ipv4_egress_flows', 'ipv4_ingress_flows', 'ipv6_egress_flows', 'ipv6_ingress_flows', 'last_cleared', 'mpls_egress_flows', 'mpls_ingress_flows', 'spp_rx_counts', 'unknown_egress_flows', 'unknown_ingress_flows', 'waiting_servers'], name, value)


            class Server(Entity):
                """
                NetFlow server statistics
                
                .. attribute:: flow_exporters
                
                	Flow exporter information
                	**type**\:   :py:class:`FlowExporters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters>`
                
                

                """

                _prefix = 'asr9k-netflow-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NetFlow.Statistics.Statistic.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "statistic"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"flow-exporters" : ("flow_exporters", NetFlow.Statistics.Statistic.Server.FlowExporters)}
                    self._child_list_classes = {}

                    self.flow_exporters = NetFlow.Statistics.Statistic.Server.FlowExporters()
                    self.flow_exporters.parent = self
                    self._children_name_map["flow_exporters"] = "flow-exporters"
                    self._children_yang_names.add("flow-exporters")
                    self._segment_path = lambda: "server"


                class FlowExporters(Entity):
                    """
                    Flow exporter information
                    
                    .. attribute:: flow_exporter
                    
                    	Exporter information
                    	**type**\: list of    :py:class:`FlowExporter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter>`
                    
                    

                    """

                    _prefix = 'asr9k-netflow-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(NetFlow.Statistics.Statistic.Server.FlowExporters, self).__init__()

                        self.yang_name = "flow-exporters"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"flow-exporter" : ("flow_exporter", NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter)}

                        self.flow_exporter = YList(self)
                        self._segment_path = lambda: "flow-exporters"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NetFlow.Statistics.Statistic.Server.FlowExporters, [], name, value)


                    class FlowExporter(Entity):
                        """
                        Exporter information
                        
                        .. attribute:: exporter_name  <key>
                        
                        	Exporter name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: exporter
                        
                        	Statistics information for the exporter
                        	**type**\:   :py:class:`Exporter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter>`
                        
                        

                        """

                        _prefix = 'asr9k-netflow-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter, self).__init__()

                            self.yang_name = "flow-exporter"
                            self.yang_parent_name = "flow-exporters"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"exporter" : ("exporter", NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter)}
                            self._child_list_classes = {}

                            self.exporter_name = YLeaf(YType.str, "exporter-name")

                            self.exporter = NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter()
                            self.exporter.parent = self
                            self._children_name_map["exporter"] = "exporter"
                            self._children_yang_names.add("exporter")
                            self._segment_path = lambda: "flow-exporter" + "[exporter-name='" + self.exporter_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter, ['exporter_name'], name, value)


                        class Exporter(Entity):
                            """
                            Statistics information for the exporter
                            
                            .. attribute:: statistic
                            
                            	Array of flow exporters
                            	**type**\: list of    :py:class:`Statistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic>`
                            
                            

                            """

                            _prefix = 'asr9k-netflow-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter, self).__init__()

                                self.yang_name = "exporter"
                                self.yang_parent_name = "flow-exporter"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"statistic" : ("statistic", NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic)}

                                self.statistic = YList(self)
                                self._segment_path = lambda: "exporter"

                            def __setattr__(self, name, value):
                                self._perform_setattr(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter, [], name, value)


                            class Statistic(Entity):
                                """
                                Array of flow exporters
                                
                                .. attribute:: collector
                                
                                	Statistics of all collectors
                                	**type**\: list of    :py:class:`Collector <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic.Collector>`
                                
                                .. attribute:: memory_usage
                                
                                	Memory usage
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: name
                                
                                	Exporter name
                                	**type**\:  str
                                
                                .. attribute:: used_by_flow_monitor
                                
                                	List of flow monitors that use the exporter
                                	**type**\:  list of str
                                
                                

                                """

                                _prefix = 'asr9k-netflow-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic, self).__init__()

                                    self.yang_name = "statistic"
                                    self.yang_parent_name = "exporter"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"collector" : ("collector", NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic.Collector)}

                                    self.memory_usage = YLeaf(YType.uint32, "memory-usage")

                                    self.name = YLeaf(YType.str, "name")

                                    self.used_by_flow_monitor = YLeafList(YType.str, "used-by-flow-monitor")

                                    self.collector = YList(self)
                                    self._segment_path = lambda: "statistic"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic, ['memory_usage', 'name', 'used_by_flow_monitor'], name, value)


                                class Collector(Entity):
                                    """
                                    Statistics of all collectors
                                    
                                    .. attribute:: bytes_dropped
                                    
                                    	Bytes dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: bytes_sent
                                    
                                    	Bytes sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: destination_address
                                    
                                    	Destination IPv4 address in AAA.BBB.CCC.DDD format
                                    	**type**\:  str
                                    
                                    .. attribute:: destination_port
                                    
                                    	Destination port number
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: exporter_state
                                    
                                    	Exporter state
                                    	**type**\:  str
                                    
                                    .. attribute:: flow_bytes_dropped
                                    
                                    	Flow bytes dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: flow_bytes_sent
                                    
                                    	Flow bytes sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: flows_dropped
                                    
                                    	Flows dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: flows_sent
                                    
                                    	Flows sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_hour_bytes_sent
                                    
                                    	Total bytes exported over the last one hour
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: last_hour_flows_sent
                                    
                                    	Total flows exported over the of last one hour
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_hour_packest_sent
                                    
                                    	Total packets exported over the last one hour
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_minute_bytes_sent
                                    
                                    	Total bytes exported over the last one minute
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: last_minute_flows_sent
                                    
                                    	Total flows exported over the last one minute
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_minute_packets
                                    
                                    	Total packets exported over the last one minute
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_second_bytes_sent
                                    
                                    	Total bytes exported over the last one second
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: last_second_flows_sent
                                    
                                    	Total flows exported over the last one second
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_second_packets_sent
                                    
                                    	Total packets exported over the last one second
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: option_data_bytes_dropped
                                    
                                    	Option data dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: option_data_bytes_sent
                                    
                                    	Option data bytes sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: option_data_dropped
                                    
                                    	Option data dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: option_data_sent
                                    
                                    	Option data sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: option_template_bytes_dropped
                                    
                                    	Option template bytes dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: option_template_bytes_sent
                                    
                                    	Option template bytes sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: option_templates_dropped
                                    
                                    	Option templates dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: option_templates_sent
                                    
                                    	Option templates sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: packets_dropped
                                    
                                    	Packets dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: packets_sent
                                    
                                    	Packets sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: souce_port
                                    
                                    	Source port number
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: source_address
                                    
                                    	Source IPv4 address in AAA.BBB.CCC.DDD format
                                    	**type**\:  str
                                    
                                    .. attribute:: template_bytes_dropped
                                    
                                    	Template bytes dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: template_bytes_sent
                                    
                                    	Template bytes sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: templates_dropped
                                    
                                    	Templates dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: templates_sent
                                    
                                    	Templates sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: transport_protocol
                                    
                                    	Transport protocol
                                    	**type**\:  str
                                    
                                    .. attribute:: vrf_name
                                    
                                    	VRF Name
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'asr9k-netflow-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic.Collector, self).__init__()

                                        self.yang_name = "collector"
                                        self.yang_parent_name = "statistic"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.bytes_dropped = YLeaf(YType.uint64, "bytes-dropped")

                                        self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                                        self.destination_address = YLeaf(YType.str, "destination-address")

                                        self.destination_port = YLeaf(YType.uint16, "destination-port")

                                        self.exporter_state = YLeaf(YType.str, "exporter-state")

                                        self.flow_bytes_dropped = YLeaf(YType.uint64, "flow-bytes-dropped")

                                        self.flow_bytes_sent = YLeaf(YType.uint64, "flow-bytes-sent")

                                        self.flows_dropped = YLeaf(YType.uint64, "flows-dropped")

                                        self.flows_sent = YLeaf(YType.uint64, "flows-sent")

                                        self.last_hour_bytes_sent = YLeaf(YType.uint64, "last-hour-bytes-sent")

                                        self.last_hour_flows_sent = YLeaf(YType.uint64, "last-hour-flows-sent")

                                        self.last_hour_packest_sent = YLeaf(YType.uint64, "last-hour-packest-sent")

                                        self.last_minute_bytes_sent = YLeaf(YType.uint64, "last-minute-bytes-sent")

                                        self.last_minute_flows_sent = YLeaf(YType.uint64, "last-minute-flows-sent")

                                        self.last_minute_packets = YLeaf(YType.uint64, "last-minute-packets")

                                        self.last_second_bytes_sent = YLeaf(YType.uint64, "last-second-bytes-sent")

                                        self.last_second_flows_sent = YLeaf(YType.uint64, "last-second-flows-sent")

                                        self.last_second_packets_sent = YLeaf(YType.uint64, "last-second-packets-sent")

                                        self.option_data_bytes_dropped = YLeaf(YType.uint64, "option-data-bytes-dropped")

                                        self.option_data_bytes_sent = YLeaf(YType.uint64, "option-data-bytes-sent")

                                        self.option_data_dropped = YLeaf(YType.uint64, "option-data-dropped")

                                        self.option_data_sent = YLeaf(YType.uint64, "option-data-sent")

                                        self.option_template_bytes_dropped = YLeaf(YType.uint64, "option-template-bytes-dropped")

                                        self.option_template_bytes_sent = YLeaf(YType.uint64, "option-template-bytes-sent")

                                        self.option_templates_dropped = YLeaf(YType.uint64, "option-templates-dropped")

                                        self.option_templates_sent = YLeaf(YType.uint64, "option-templates-sent")

                                        self.packets_dropped = YLeaf(YType.uint64, "packets-dropped")

                                        self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                                        self.souce_port = YLeaf(YType.uint16, "souce-port")

                                        self.source_address = YLeaf(YType.str, "source-address")

                                        self.template_bytes_dropped = YLeaf(YType.uint64, "template-bytes-dropped")

                                        self.template_bytes_sent = YLeaf(YType.uint64, "template-bytes-sent")

                                        self.templates_dropped = YLeaf(YType.uint64, "templates-dropped")

                                        self.templates_sent = YLeaf(YType.uint64, "templates-sent")

                                        self.transport_protocol = YLeaf(YType.str, "transport-protocol")

                                        self.vrf_name = YLeaf(YType.str, "vrf-name")
                                        self._segment_path = lambda: "collector"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic.Collector, ['bytes_dropped', 'bytes_sent', 'destination_address', 'destination_port', 'exporter_state', 'flow_bytes_dropped', 'flow_bytes_sent', 'flows_dropped', 'flows_sent', 'last_hour_bytes_sent', 'last_hour_flows_sent', 'last_hour_packest_sent', 'last_minute_bytes_sent', 'last_minute_flows_sent', 'last_minute_packets', 'last_second_bytes_sent', 'last_second_flows_sent', 'last_second_packets_sent', 'option_data_bytes_dropped', 'option_data_bytes_sent', 'option_data_dropped', 'option_data_sent', 'option_template_bytes_dropped', 'option_template_bytes_sent', 'option_templates_dropped', 'option_templates_sent', 'packets_dropped', 'packets_sent', 'souce_port', 'source_address', 'template_bytes_dropped', 'template_bytes_sent', 'templates_dropped', 'templates_sent', 'transport_protocol', 'vrf_name'], name, value)

    def clone_ptr(self):
        self._top_entity = NetFlow()
        return self._top_entity

