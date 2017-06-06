""" Cisco_IOS_XR_asr9k_netflow_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-netflow package operational data.

This module contains definitions
for the following management objects\:
  net\-flow\: NetFlow operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class NetFlow(object):
    """
    NetFlow operational data
    
    .. attribute:: statistics
    
    	Node\-specific NetFlow statistics information
    	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics>`
    
    

    """

    _prefix = 'asr9k-netflow-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.statistics = NetFlow.Statistics()
        self.statistics.parent = self


    class Statistics(object):
        """
        Node\-specific NetFlow statistics information
        
        .. attribute:: statistic
        
        	NetFlow statistics information for a particular node
        	**type**\: list of    :py:class:`Statistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic>`
        
        

        """

        _prefix = 'asr9k-netflow-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.statistic = YList()
            self.statistic.parent = self
            self.statistic.name = 'statistic'


        class Statistic(object):
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
                self.parent = None
                self.node = None
                self.producer = NetFlow.Statistics.Statistic.Producer()
                self.producer.parent = self
                self.server = NetFlow.Statistics.Statistic.Server()
                self.server.parent = self


            class Producer(object):
                """
                NetFlow producer statistics
                
                .. attribute:: statistics
                
                	Statistics information
                	**type**\:   :py:class:`Statistics_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Producer.Statistics_>`
                
                

                """

                _prefix = 'asr9k-netflow-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.statistics = NetFlow.Statistics.Statistic.Producer.Statistics_()
                    self.statistics.parent = self


                class Statistics_(object):
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
                        self.parent = None
                        self.drops_no_space = None
                        self.drops_others = None
                        self.flow_packet_counts = None
                        self.ipv4_egress_flows = None
                        self.ipv4_ingress_flows = None
                        self.ipv6_egress_flows = None
                        self.ipv6_ingress_flows = None
                        self.last_cleared = None
                        self.mpls_egress_flows = None
                        self.mpls_ingress_flows = None
                        self.spp_rx_counts = None
                        self.unknown_egress_flows = None
                        self.unknown_ingress_flows = None
                        self.waiting_servers = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.drops_no_space is not None:
                            return True

                        if self.drops_others is not None:
                            return True

                        if self.flow_packet_counts is not None:
                            return True

                        if self.ipv4_egress_flows is not None:
                            return True

                        if self.ipv4_ingress_flows is not None:
                            return True

                        if self.ipv6_egress_flows is not None:
                            return True

                        if self.ipv6_ingress_flows is not None:
                            return True

                        if self.last_cleared is not None:
                            return True

                        if self.mpls_egress_flows is not None:
                            return True

                        if self.mpls_ingress_flows is not None:
                            return True

                        if self.spp_rx_counts is not None:
                            return True

                        if self.unknown_egress_flows is not None:
                            return True

                        if self.unknown_ingress_flows is not None:
                            return True

                        if self.waiting_servers is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                        return meta._meta_table['NetFlow.Statistics.Statistic.Producer.Statistics_']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:producer'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.statistics is not None and self.statistics._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                    return meta._meta_table['NetFlow.Statistics.Statistic.Producer']['meta_info']


            class Server(object):
                """
                NetFlow server statistics
                
                .. attribute:: flow_exporters
                
                	Flow exporter information
                	**type**\:   :py:class:`FlowExporters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters>`
                
                

                """

                _prefix = 'asr9k-netflow-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.flow_exporters = NetFlow.Statistics.Statistic.Server.FlowExporters()
                    self.flow_exporters.parent = self


                class FlowExporters(object):
                    """
                    Flow exporter information
                    
                    .. attribute:: flow_exporter
                    
                    	Exporter information
                    	**type**\: list of    :py:class:`FlowExporter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter>`
                    
                    

                    """

                    _prefix = 'asr9k-netflow-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.flow_exporter = YList()
                        self.flow_exporter.parent = self
                        self.flow_exporter.name = 'flow_exporter'


                    class FlowExporter(object):
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
                            self.parent = None
                            self.exporter_name = None
                            self.exporter = NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter()
                            self.exporter.parent = self


                        class Exporter(object):
                            """
                            Statistics information for the exporter
                            
                            .. attribute:: statistic
                            
                            	Array of flow exporters
                            	**type**\: list of    :py:class:`Statistic_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic_>`
                            
                            

                            """

                            _prefix = 'asr9k-netflow-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.statistic = YList()
                                self.statistic.parent = self
                                self.statistic.name = 'statistic'


                            class Statistic_(object):
                                """
                                Array of flow exporters
                                
                                .. attribute:: collector
                                
                                	Statistics of all collectors
                                	**type**\: list of    :py:class:`Collector <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic_.Collector>`
                                
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
                                    self.parent = None
                                    self.collector = YList()
                                    self.collector.parent = self
                                    self.collector.name = 'collector'
                                    self.memory_usage = None
                                    self.name = None
                                    self.used_by_flow_monitor = YLeafList()
                                    self.used_by_flow_monitor.parent = self
                                    self.used_by_flow_monitor.name = 'used_by_flow_monitor'


                                class Collector(object):
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
                                        self.parent = None
                                        self.bytes_dropped = None
                                        self.bytes_sent = None
                                        self.destination_address = None
                                        self.destination_port = None
                                        self.exporter_state = None
                                        self.flow_bytes_dropped = None
                                        self.flow_bytes_sent = None
                                        self.flows_dropped = None
                                        self.flows_sent = None
                                        self.last_hour_bytes_sent = None
                                        self.last_hour_flows_sent = None
                                        self.last_hour_packest_sent = None
                                        self.last_minute_bytes_sent = None
                                        self.last_minute_flows_sent = None
                                        self.last_minute_packets = None
                                        self.last_second_bytes_sent = None
                                        self.last_second_flows_sent = None
                                        self.last_second_packets_sent = None
                                        self.option_data_bytes_dropped = None
                                        self.option_data_bytes_sent = None
                                        self.option_data_dropped = None
                                        self.option_data_sent = None
                                        self.option_template_bytes_dropped = None
                                        self.option_template_bytes_sent = None
                                        self.option_templates_dropped = None
                                        self.option_templates_sent = None
                                        self.packets_dropped = None
                                        self.packets_sent = None
                                        self.souce_port = None
                                        self.source_address = None
                                        self.template_bytes_dropped = None
                                        self.template_bytes_sent = None
                                        self.templates_dropped = None
                                        self.templates_sent = None
                                        self.transport_protocol = None
                                        self.vrf_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:collector'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.bytes_dropped is not None:
                                            return True

                                        if self.bytes_sent is not None:
                                            return True

                                        if self.destination_address is not None:
                                            return True

                                        if self.destination_port is not None:
                                            return True

                                        if self.exporter_state is not None:
                                            return True

                                        if self.flow_bytes_dropped is not None:
                                            return True

                                        if self.flow_bytes_sent is not None:
                                            return True

                                        if self.flows_dropped is not None:
                                            return True

                                        if self.flows_sent is not None:
                                            return True

                                        if self.last_hour_bytes_sent is not None:
                                            return True

                                        if self.last_hour_flows_sent is not None:
                                            return True

                                        if self.last_hour_packest_sent is not None:
                                            return True

                                        if self.last_minute_bytes_sent is not None:
                                            return True

                                        if self.last_minute_flows_sent is not None:
                                            return True

                                        if self.last_minute_packets is not None:
                                            return True

                                        if self.last_second_bytes_sent is not None:
                                            return True

                                        if self.last_second_flows_sent is not None:
                                            return True

                                        if self.last_second_packets_sent is not None:
                                            return True

                                        if self.option_data_bytes_dropped is not None:
                                            return True

                                        if self.option_data_bytes_sent is not None:
                                            return True

                                        if self.option_data_dropped is not None:
                                            return True

                                        if self.option_data_sent is not None:
                                            return True

                                        if self.option_template_bytes_dropped is not None:
                                            return True

                                        if self.option_template_bytes_sent is not None:
                                            return True

                                        if self.option_templates_dropped is not None:
                                            return True

                                        if self.option_templates_sent is not None:
                                            return True

                                        if self.packets_dropped is not None:
                                            return True

                                        if self.packets_sent is not None:
                                            return True

                                        if self.souce_port is not None:
                                            return True

                                        if self.source_address is not None:
                                            return True

                                        if self.template_bytes_dropped is not None:
                                            return True

                                        if self.template_bytes_sent is not None:
                                            return True

                                        if self.templates_dropped is not None:
                                            return True

                                        if self.templates_sent is not None:
                                            return True

                                        if self.transport_protocol is not None:
                                            return True

                                        if self.vrf_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                                        return meta._meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic_.Collector']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:statistic'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.collector is not None:
                                        for child_ref in self.collector:
                                            if child_ref._has_data():
                                                return True

                                    if self.memory_usage is not None:
                                        return True

                                    if self.name is not None:
                                        return True

                                    if self.used_by_flow_monitor is not None:
                                        for child in self.used_by_flow_monitor:
                                            if child is not None:
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                                    return meta._meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic_']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:exporter'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.statistic is not None:
                                    for child_ref in self.statistic:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                                return meta._meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.exporter_name is None:
                                raise YPYModelError('Key property exporter_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:flow-exporter[Cisco-IOS-XR-asr9k-netflow-oper:exporter-name = ' + str(self.exporter_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.exporter_name is not None:
                                return True

                            if self.exporter is not None and self.exporter._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                            return meta._meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:flow-exporters'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.flow_exporter is not None:
                            for child_ref in self.flow_exporter:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                        return meta._meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:server'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.flow_exporters is not None and self.flow_exporters._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                    return meta._meta_table['NetFlow.Statistics.Statistic.Server']['meta_info']

            @property
            def _common_path(self):
                if self.node is None:
                    raise YPYModelError('Key property node is None')

                return '/Cisco-IOS-XR-asr9k-netflow-oper:net-flow/Cisco-IOS-XR-asr9k-netflow-oper:statistics/Cisco-IOS-XR-asr9k-netflow-oper:statistic[Cisco-IOS-XR-asr9k-netflow-oper:node = ' + str(self.node) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node is not None:
                    return True

                if self.producer is not None and self.producer._has_data():
                    return True

                if self.server is not None and self.server._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                return meta._meta_table['NetFlow.Statistics.Statistic']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-netflow-oper:net-flow/Cisco-IOS-XR-asr9k-netflow-oper:statistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.statistic is not None:
                for child_ref in self.statistic:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
            return meta._meta_table['NetFlow.Statistics']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-netflow-oper:net-flow'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.statistics is not None and self.statistics._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
        return meta._meta_table['NetFlow']['meta_info']


