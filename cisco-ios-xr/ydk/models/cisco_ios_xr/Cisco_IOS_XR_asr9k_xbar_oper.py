""" Cisco_IOS_XR_asr9k_xbar_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-xbar package operational data.

This module contains definitions
for the following management objects\:
  cross\-bar\-stats\: Crossbar stats operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CrossBarStats(Entity):
    """
    Crossbar stats operational data
    
    .. attribute:: nodes
    
    	Table of Nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes>`
    
    

    """

    _prefix = 'asr9k-xbar-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(CrossBarStats, self).__init__()
        self._top_entity = None

        self.yang_name = "cross-bar-stats"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-xbar-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", CrossBarStats.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = CrossBarStats.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-xbar-oper:cross-bar-stats"


    class Nodes(Entity):
        """
        Table of Nodes
        
        .. attribute:: node
        
        	Information about a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-xbar-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(CrossBarStats.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "cross-bar-stats"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", CrossBarStats.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-xbar-oper:cross-bar-stats/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CrossBarStats.Nodes, [], name, value)


        class Node(Entity):
            """
            Information about a particular node
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: cross_bar_table
            
            	Table of stats information
            	**type**\:  :py:class:`CrossBarTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable>`
            
            

            """

            _prefix = 'asr9k-xbar-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(CrossBarStats.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_container_classes = OrderedDict([("cross-bar-table", ("cross_bar_table", CrossBarStats.Nodes.Node.CrossBarTable))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                ])
                self.node_name = None

                self.cross_bar_table = CrossBarStats.Nodes.Node.CrossBarTable()
                self.cross_bar_table.parent = self
                self._children_name_map["cross_bar_table"] = "cross-bar-table"
                self._children_yang_names.add("cross-bar-table")
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-xbar-oper:cross-bar-stats/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CrossBarStats.Nodes.Node, ['node_name'], name, value)


            class CrossBarTable(Entity):
                """
                Table of stats information
                
                .. attribute:: pkt_stats
                
                	Table of packet stats
                	**type**\:  :py:class:`PktStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.PktStats>`
                
                .. attribute:: sm15_stats
                
                	Table of packet stats for SM15
                	**type**\:  :py:class:`Sm15Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats>`
                
                

                """

                _prefix = 'asr9k-xbar-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(CrossBarStats.Nodes.Node.CrossBarTable, self).__init__()

                    self.yang_name = "cross-bar-table"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("pkt-stats", ("pkt_stats", CrossBarStats.Nodes.Node.CrossBarTable.PktStats)), ("sm15-stats", ("sm15_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.pkt_stats = CrossBarStats.Nodes.Node.CrossBarTable.PktStats()
                    self.pkt_stats.parent = self
                    self._children_name_map["pkt_stats"] = "pkt-stats"
                    self._children_yang_names.add("pkt-stats")

                    self.sm15_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats()
                    self.sm15_stats.parent = self
                    self._children_name_map["sm15_stats"] = "sm15-stats"
                    self._children_yang_names.add("sm15-stats")
                    self._segment_path = lambda: "cross-bar-table"


                class PktStats(Entity):
                    """
                    Table of packet stats
                    
                    .. attribute:: pkt_stat
                    
                    	Stats information for a particular asic type and port
                    	**type**\: list of  		 :py:class:`PktStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.PktStats.PktStat>`
                    
                    

                    """

                    _prefix = 'asr9k-xbar-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CrossBarStats.Nodes.Node.CrossBarTable.PktStats, self).__init__()

                        self.yang_name = "pkt-stats"
                        self.yang_parent_name = "cross-bar-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("pkt-stat", ("pkt_stat", CrossBarStats.Nodes.Node.CrossBarTable.PktStats.PktStat))])
                        self._leafs = OrderedDict()

                        self.pkt_stat = YList(self)
                        self._segment_path = lambda: "pkt-stats"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.PktStats, [], name, value)


                    class PktStat(Entity):
                        """
                        Stats information for a particular asic type
                        and port
                        
                        .. attribute:: asic_id
                        
                        	Asic ID
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: port
                        
                        	Port
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: internal_error_count
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: input_buffer_queued_packet_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ingress_packet_count_since_last_read_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ingress_channel_utilization_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: input_buffer_back_pressure_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: xbar_timeout_drop_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: holdrop_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: null_fpoe_drop_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: diagnostic_packet_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: input_buffer_correctable_ecc_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: input_buffer_uncorrectable_ecc_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: header_crc_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: short_input_header_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: packet_crc_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: short_packet_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: output_buffer_queued_packet_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: egress_packet_count_since_last_read_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: egress_channel_utilization_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: output_buffer_back_pressure_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: output_buffer_correctable_ecc_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: output_buffer_uncorrectable_ecc_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: fpoedb_correctable_ecc_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: fpoedb_uncorrectable_ecc_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: input_buffer_queued_packet_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ingress_packet_count_since_last_read_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ingress_channel_utilization_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: input_buffer_back_pressure_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: xbar_timeout_drop_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: holdrop_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: null_fpoe_drop_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: diagnostic_packet_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: input_buffer_correctable_ecc_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: input_buffer_uncorrectable_ecc_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: header_crc_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: short_input_header_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: packet_crc_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: short_packet_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: output_buffer_queued_packet_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: egress_packet_count_since_last_read_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: egress_channel_utilization_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: output_buffer_back_pressure_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: output_buffer_correctable_ecc_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: output_buffer_uncorrectable_ecc_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: fpoedb_correctable_ecc_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: fpoedb_uncorrectable_ecc_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'asr9k-xbar-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(CrossBarStats.Nodes.Node.CrossBarTable.PktStats.PktStat, self).__init__()

                            self.yang_name = "pkt-stat"
                            self.yang_parent_name = "pkt-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('asic_id', YLeaf(YType.str, 'asic-id')),
                                ('port', YLeaf(YType.str, 'port')),
                                ('internal_error_count', YLeaf(YType.uint64, 'internal-error-count')),
                                ('input_buffer_queued_packet_count_high', YLeaf(YType.uint64, 'input-buffer-queued-packet-count-high')),
                                ('ingress_packet_count_since_last_read_high', YLeaf(YType.uint64, 'ingress-packet-count-since-last-read-high')),
                                ('ingress_channel_utilization_count_high', YLeaf(YType.uint64, 'ingress-channel-utilization-count-high')),
                                ('input_buffer_back_pressure_count_high', YLeaf(YType.uint64, 'input-buffer-back-pressure-count-high')),
                                ('xbar_timeout_drop_count_high', YLeaf(YType.uint64, 'xbar-timeout-drop-count-high')),
                                ('holdrop_count_high', YLeaf(YType.uint64, 'holdrop-count-high')),
                                ('null_fpoe_drop_count_high', YLeaf(YType.uint64, 'null-fpoe-drop-count-high')),
                                ('diagnostic_packet_count_high', YLeaf(YType.uint64, 'diagnostic-packet-count-high')),
                                ('input_buffer_correctable_ecc_error_count_high', YLeaf(YType.uint64, 'input-buffer-correctable-ecc-error-count-high')),
                                ('input_buffer_uncorrectable_ecc_error_count_high', YLeaf(YType.uint64, 'input-buffer-uncorrectable-ecc-error-count-high')),
                                ('header_crc_error_count_high', YLeaf(YType.uint64, 'header-crc-error-count-high')),
                                ('short_input_header_error_count_high', YLeaf(YType.uint64, 'short-input-header-error-count-high')),
                                ('packet_crc_error_count_high', YLeaf(YType.uint64, 'packet-crc-error-count-high')),
                                ('short_packet_error_count_high', YLeaf(YType.uint64, 'short-packet-error-count-high')),
                                ('output_buffer_queued_packet_count_high', YLeaf(YType.uint64, 'output-buffer-queued-packet-count-high')),
                                ('egress_packet_count_since_last_read_high', YLeaf(YType.uint64, 'egress-packet-count-since-last-read-high')),
                                ('egress_channel_utilization_count_high', YLeaf(YType.uint64, 'egress-channel-utilization-count-high')),
                                ('output_buffer_back_pressure_count_high', YLeaf(YType.uint64, 'output-buffer-back-pressure-count-high')),
                                ('output_buffer_correctable_ecc_error_count_high', YLeaf(YType.uint64, 'output-buffer-correctable-ecc-error-count-high')),
                                ('output_buffer_uncorrectable_ecc_error_count_high', YLeaf(YType.uint64, 'output-buffer-uncorrectable-ecc-error-count-high')),
                                ('fpoedb_correctable_ecc_error_count_high', YLeaf(YType.uint64, 'fpoedb-correctable-ecc-error-count-high')),
                                ('fpoedb_uncorrectable_ecc_error_count_high', YLeaf(YType.uint64, 'fpoedb-uncorrectable-ecc-error-count-high')),
                                ('input_buffer_queued_packet_count_low', YLeaf(YType.uint64, 'input-buffer-queued-packet-count-low')),
                                ('ingress_packet_count_since_last_read_low', YLeaf(YType.uint64, 'ingress-packet-count-since-last-read-low')),
                                ('ingress_channel_utilization_count_low', YLeaf(YType.uint64, 'ingress-channel-utilization-count-low')),
                                ('input_buffer_back_pressure_count_low', YLeaf(YType.uint64, 'input-buffer-back-pressure-count-low')),
                                ('xbar_timeout_drop_count_low', YLeaf(YType.uint64, 'xbar-timeout-drop-count-low')),
                                ('holdrop_count_low', YLeaf(YType.uint64, 'holdrop-count-low')),
                                ('null_fpoe_drop_count_low', YLeaf(YType.uint64, 'null-fpoe-drop-count-low')),
                                ('diagnostic_packet_count_low', YLeaf(YType.uint64, 'diagnostic-packet-count-low')),
                                ('input_buffer_correctable_ecc_error_count_low', YLeaf(YType.uint64, 'input-buffer-correctable-ecc-error-count-low')),
                                ('input_buffer_uncorrectable_ecc_error_count_low', YLeaf(YType.uint64, 'input-buffer-uncorrectable-ecc-error-count-low')),
                                ('header_crc_error_count_low', YLeaf(YType.uint64, 'header-crc-error-count-low')),
                                ('short_input_header_error_count_low', YLeaf(YType.uint64, 'short-input-header-error-count-low')),
                                ('packet_crc_error_count_low', YLeaf(YType.uint64, 'packet-crc-error-count-low')),
                                ('short_packet_error_count_low', YLeaf(YType.uint64, 'short-packet-error-count-low')),
                                ('output_buffer_queued_packet_count_low', YLeaf(YType.uint64, 'output-buffer-queued-packet-count-low')),
                                ('egress_packet_count_since_last_read_low', YLeaf(YType.uint64, 'egress-packet-count-since-last-read-low')),
                                ('egress_channel_utilization_count_low', YLeaf(YType.uint64, 'egress-channel-utilization-count-low')),
                                ('output_buffer_back_pressure_count_low', YLeaf(YType.uint64, 'output-buffer-back-pressure-count-low')),
                                ('output_buffer_correctable_ecc_error_count_low', YLeaf(YType.uint64, 'output-buffer-correctable-ecc-error-count-low')),
                                ('output_buffer_uncorrectable_ecc_error_count_low', YLeaf(YType.uint64, 'output-buffer-uncorrectable-ecc-error-count-low')),
                                ('fpoedb_correctable_ecc_error_count_low', YLeaf(YType.uint64, 'fpoedb-correctable-ecc-error-count-low')),
                                ('fpoedb_uncorrectable_ecc_error_count_low', YLeaf(YType.uint64, 'fpoedb-uncorrectable-ecc-error-count-low')),
                            ])
                            self.asic_id = None
                            self.port = None
                            self.internal_error_count = None
                            self.input_buffer_queued_packet_count_high = None
                            self.ingress_packet_count_since_last_read_high = None
                            self.ingress_channel_utilization_count_high = None
                            self.input_buffer_back_pressure_count_high = None
                            self.xbar_timeout_drop_count_high = None
                            self.holdrop_count_high = None
                            self.null_fpoe_drop_count_high = None
                            self.diagnostic_packet_count_high = None
                            self.input_buffer_correctable_ecc_error_count_high = None
                            self.input_buffer_uncorrectable_ecc_error_count_high = None
                            self.header_crc_error_count_high = None
                            self.short_input_header_error_count_high = None
                            self.packet_crc_error_count_high = None
                            self.short_packet_error_count_high = None
                            self.output_buffer_queued_packet_count_high = None
                            self.egress_packet_count_since_last_read_high = None
                            self.egress_channel_utilization_count_high = None
                            self.output_buffer_back_pressure_count_high = None
                            self.output_buffer_correctable_ecc_error_count_high = None
                            self.output_buffer_uncorrectable_ecc_error_count_high = None
                            self.fpoedb_correctable_ecc_error_count_high = None
                            self.fpoedb_uncorrectable_ecc_error_count_high = None
                            self.input_buffer_queued_packet_count_low = None
                            self.ingress_packet_count_since_last_read_low = None
                            self.ingress_channel_utilization_count_low = None
                            self.input_buffer_back_pressure_count_low = None
                            self.xbar_timeout_drop_count_low = None
                            self.holdrop_count_low = None
                            self.null_fpoe_drop_count_low = None
                            self.diagnostic_packet_count_low = None
                            self.input_buffer_correctable_ecc_error_count_low = None
                            self.input_buffer_uncorrectable_ecc_error_count_low = None
                            self.header_crc_error_count_low = None
                            self.short_input_header_error_count_low = None
                            self.packet_crc_error_count_low = None
                            self.short_packet_error_count_low = None
                            self.output_buffer_queued_packet_count_low = None
                            self.egress_packet_count_since_last_read_low = None
                            self.egress_channel_utilization_count_low = None
                            self.output_buffer_back_pressure_count_low = None
                            self.output_buffer_correctable_ecc_error_count_low = None
                            self.output_buffer_uncorrectable_ecc_error_count_low = None
                            self.fpoedb_correctable_ecc_error_count_low = None
                            self.fpoedb_uncorrectable_ecc_error_count_low = None
                            self._segment_path = lambda: "pkt-stat"

                        def __setattr__(self, name, value):
                            self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.PktStats.PktStat, ['asic_id', 'port', 'internal_error_count', 'input_buffer_queued_packet_count_high', 'ingress_packet_count_since_last_read_high', 'ingress_channel_utilization_count_high', 'input_buffer_back_pressure_count_high', 'xbar_timeout_drop_count_high', 'holdrop_count_high', 'null_fpoe_drop_count_high', 'diagnostic_packet_count_high', 'input_buffer_correctable_ecc_error_count_high', 'input_buffer_uncorrectable_ecc_error_count_high', 'header_crc_error_count_high', 'short_input_header_error_count_high', 'packet_crc_error_count_high', 'short_packet_error_count_high', 'output_buffer_queued_packet_count_high', 'egress_packet_count_since_last_read_high', 'egress_channel_utilization_count_high', 'output_buffer_back_pressure_count_high', 'output_buffer_correctable_ecc_error_count_high', 'output_buffer_uncorrectable_ecc_error_count_high', 'fpoedb_correctable_ecc_error_count_high', 'fpoedb_uncorrectable_ecc_error_count_high', 'input_buffer_queued_packet_count_low', 'ingress_packet_count_since_last_read_low', 'ingress_channel_utilization_count_low', 'input_buffer_back_pressure_count_low', 'xbar_timeout_drop_count_low', 'holdrop_count_low', 'null_fpoe_drop_count_low', 'diagnostic_packet_count_low', 'input_buffer_correctable_ecc_error_count_low', 'input_buffer_uncorrectable_ecc_error_count_low', 'header_crc_error_count_low', 'short_input_header_error_count_low', 'packet_crc_error_count_low', 'short_packet_error_count_low', 'output_buffer_queued_packet_count_low', 'egress_packet_count_since_last_read_low', 'egress_channel_utilization_count_low', 'output_buffer_back_pressure_count_low', 'output_buffer_correctable_ecc_error_count_low', 'output_buffer_uncorrectable_ecc_error_count_low', 'fpoedb_correctable_ecc_error_count_low', 'fpoedb_uncorrectable_ecc_error_count_low'], name, value)


                class Sm15Stats(Entity):
                    """
                    Table of packet stats for SM15
                    
                    .. attribute:: sm15_stat
                    
                    	Stats information for a particular asic type and port
                    	**type**\: list of  		 :py:class:`Sm15Stat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat>`
                    
                    

                    """

                    _prefix = 'asr9k-xbar-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats, self).__init__()

                        self.yang_name = "sm15-stats"
                        self.yang_parent_name = "cross-bar-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("sm15-stat", ("sm15_stat", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat))])
                        self._leafs = OrderedDict()

                        self.sm15_stat = YList(self)
                        self._segment_path = lambda: "sm15-stats"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats, [], name, value)


                    class Sm15Stat(Entity):
                        """
                        Stats information for a particular asic type
                        and port
                        
                        .. attribute:: asic_id
                        
                        	Asic ID
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: port
                        
                        	Port
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: ua0_stats
                        
                        	ua0 stats
                        	**type**\:  :py:class:`Ua0Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua0Stats>`
                        
                        .. attribute:: ua1_stats
                        
                        	ua1 stats
                        	**type**\:  :py:class:`Ua1Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua1Stats>`
                        
                        .. attribute:: ua2_stats
                        
                        	ua2 stats
                        	**type**\:  :py:class:`Ua2Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua2Stats>`
                        
                        .. attribute:: ma_stats
                        
                        	ma stats
                        	**type**\:  :py:class:`MaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.MaStats>`
                        
                        .. attribute:: ca_stats
                        
                        	ca stats
                        	**type**\:  :py:class:`CaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.CaStats>`
                        
                        .. attribute:: pi_stats
                        
                        	pi stats
                        	**type**\:  :py:class:`PiStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiStats>`
                        
                        .. attribute:: pe_stats
                        
                        	pe stats
                        	**type**\:  :py:class:`PeStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeStats>`
                        
                        .. attribute:: pi_uc_stats
                        
                        	pi uc stats
                        	**type**\:  :py:class:`PiUcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiUcStats>`
                        
                        .. attribute:: pi_mc_stats
                        
                        	pi mc stats
                        	**type**\:  :py:class:`PiMcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiMcStats>`
                        
                        .. attribute:: pi_cc_stats
                        
                        	pi cc stats
                        	**type**\:  :py:class:`PiCcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiCcStats>`
                        
                        .. attribute:: pe_uc_stats
                        
                        	pe uc stats
                        	**type**\:  :py:class:`PeUcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeUcStats>`
                        
                        .. attribute:: pe_mc_stats
                        
                        	pe mc stats
                        	**type**\:  :py:class:`PeMcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeMcStats>`
                        
                        .. attribute:: pe_cc_stats
                        
                        	pe cc stats
                        	**type**\:  :py:class:`PeCcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeCcStats>`
                        
                        .. attribute:: internal_err_cnt
                        
                        	internal err cnt
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'asr9k-xbar-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat, self).__init__()

                            self.yang_name = "sm15-stat"
                            self.yang_parent_name = "sm15-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("ua0-stats", ("ua0_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua0Stats)), ("ua1-stats", ("ua1_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua1Stats)), ("ua2-stats", ("ua2_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua2Stats)), ("ma-stats", ("ma_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.MaStats)), ("ca-stats", ("ca_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.CaStats)), ("pi-stats", ("pi_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiStats)), ("pe-stats", ("pe_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeStats)), ("pi-uc-stats", ("pi_uc_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiUcStats)), ("pi-mc-stats", ("pi_mc_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiMcStats)), ("pi-cc-stats", ("pi_cc_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiCcStats)), ("pe-uc-stats", ("pe_uc_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeUcStats)), ("pe-mc-stats", ("pe_mc_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeMcStats)), ("pe-cc-stats", ("pe_cc_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeCcStats))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('asic_id', YLeaf(YType.str, 'asic-id')),
                                ('port', YLeaf(YType.str, 'port')),
                                ('internal_err_cnt', YLeaf(YType.uint64, 'internal-err-cnt')),
                            ])
                            self.asic_id = None
                            self.port = None
                            self.internal_err_cnt = None

                            self.ua0_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua0Stats()
                            self.ua0_stats.parent = self
                            self._children_name_map["ua0_stats"] = "ua0-stats"
                            self._children_yang_names.add("ua0-stats")

                            self.ua1_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua1Stats()
                            self.ua1_stats.parent = self
                            self._children_name_map["ua1_stats"] = "ua1-stats"
                            self._children_yang_names.add("ua1-stats")

                            self.ua2_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua2Stats()
                            self.ua2_stats.parent = self
                            self._children_name_map["ua2_stats"] = "ua2-stats"
                            self._children_yang_names.add("ua2-stats")

                            self.ma_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.MaStats()
                            self.ma_stats.parent = self
                            self._children_name_map["ma_stats"] = "ma-stats"
                            self._children_yang_names.add("ma-stats")

                            self.ca_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.CaStats()
                            self.ca_stats.parent = self
                            self._children_name_map["ca_stats"] = "ca-stats"
                            self._children_yang_names.add("ca-stats")

                            self.pi_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiStats()
                            self.pi_stats.parent = self
                            self._children_name_map["pi_stats"] = "pi-stats"
                            self._children_yang_names.add("pi-stats")

                            self.pe_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeStats()
                            self.pe_stats.parent = self
                            self._children_name_map["pe_stats"] = "pe-stats"
                            self._children_yang_names.add("pe-stats")

                            self.pi_uc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiUcStats()
                            self.pi_uc_stats.parent = self
                            self._children_name_map["pi_uc_stats"] = "pi-uc-stats"
                            self._children_yang_names.add("pi-uc-stats")

                            self.pi_mc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiMcStats()
                            self.pi_mc_stats.parent = self
                            self._children_name_map["pi_mc_stats"] = "pi-mc-stats"
                            self._children_yang_names.add("pi-mc-stats")

                            self.pi_cc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiCcStats()
                            self.pi_cc_stats.parent = self
                            self._children_name_map["pi_cc_stats"] = "pi-cc-stats"
                            self._children_yang_names.add("pi-cc-stats")

                            self.pe_uc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeUcStats()
                            self.pe_uc_stats.parent = self
                            self._children_name_map["pe_uc_stats"] = "pe-uc-stats"
                            self._children_yang_names.add("pe-uc-stats")

                            self.pe_mc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeMcStats()
                            self.pe_mc_stats.parent = self
                            self._children_name_map["pe_mc_stats"] = "pe-mc-stats"
                            self._children_yang_names.add("pe-mc-stats")

                            self.pe_cc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeCcStats()
                            self.pe_cc_stats.parent = self
                            self._children_name_map["pe_cc_stats"] = "pe-cc-stats"
                            self._children_yang_names.add("pe-cc-stats")
                            self._segment_path = lambda: "sm15-stat"

                        def __setattr__(self, name, value):
                            self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat, ['asic_id', 'port', 'internal_err_cnt'], name, value)


                        class Ua0Stats(Entity):
                            """
                            ua0 stats
                            
                            .. attribute:: dest_drop_pkt_cnt
                            
                            	DEST DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: src_dest_pkt_cnt
                            
                            	SRC DEST PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dest_src_pkt_cnt
                            
                            	DEST SRC PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rcv_pkt_cnt
                            
                            	RCV PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tx_pkt_cnt
                            
                            	TX PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_drop_pkt_cnt
                            
                            	RX DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_fabric_to_cnt
                            
                            	RX FABRIC TO CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ack_wait_cnt
                            
                            	ACK WAIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'asr9k-xbar-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua0Stats, self).__init__()

                                self.yang_name = "ua0-stats"
                                self.yang_parent_name = "sm15-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('dest_drop_pkt_cnt', YLeaf(YType.uint64, 'dest-drop-pkt-cnt')),
                                    ('src_dest_pkt_cnt', YLeaf(YType.uint64, 'src-dest-pkt-cnt')),
                                    ('dest_src_pkt_cnt', YLeaf(YType.uint64, 'dest-src-pkt-cnt')),
                                    ('rcv_pkt_cnt', YLeaf(YType.uint64, 'rcv-pkt-cnt')),
                                    ('tx_pkt_cnt', YLeaf(YType.uint64, 'tx-pkt-cnt')),
                                    ('rx_drop_pkt_cnt', YLeaf(YType.uint64, 'rx-drop-pkt-cnt')),
                                    ('rx_fabric_to_cnt', YLeaf(YType.uint64, 'rx-fabric-to-cnt')),
                                    ('ack_wait_cnt', YLeaf(YType.uint64, 'ack-wait-cnt')),
                                ])
                                self.dest_drop_pkt_cnt = None
                                self.src_dest_pkt_cnt = None
                                self.dest_src_pkt_cnt = None
                                self.rcv_pkt_cnt = None
                                self.tx_pkt_cnt = None
                                self.rx_drop_pkt_cnt = None
                                self.rx_fabric_to_cnt = None
                                self.ack_wait_cnt = None
                                self._segment_path = lambda: "ua0-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua0Stats, ['dest_drop_pkt_cnt', 'src_dest_pkt_cnt', 'dest_src_pkt_cnt', 'rcv_pkt_cnt', 'tx_pkt_cnt', 'rx_drop_pkt_cnt', 'rx_fabric_to_cnt', 'ack_wait_cnt'], name, value)


                        class Ua1Stats(Entity):
                            """
                            ua1 stats
                            
                            .. attribute:: dest_drop_pkt_cnt
                            
                            	DEST DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: src_dest_pkt_cnt
                            
                            	SRC DEST PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dest_src_pkt_cnt
                            
                            	DEST SRC PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rcv_pkt_cnt
                            
                            	RCV PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tx_pkt_cnt
                            
                            	TX PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_drop_pkt_cnt
                            
                            	RX DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_fabric_to_cnt
                            
                            	RX FABRIC TO CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ack_wait_cnt
                            
                            	ACK WAIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'asr9k-xbar-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua1Stats, self).__init__()

                                self.yang_name = "ua1-stats"
                                self.yang_parent_name = "sm15-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('dest_drop_pkt_cnt', YLeaf(YType.uint64, 'dest-drop-pkt-cnt')),
                                    ('src_dest_pkt_cnt', YLeaf(YType.uint64, 'src-dest-pkt-cnt')),
                                    ('dest_src_pkt_cnt', YLeaf(YType.uint64, 'dest-src-pkt-cnt')),
                                    ('rcv_pkt_cnt', YLeaf(YType.uint64, 'rcv-pkt-cnt')),
                                    ('tx_pkt_cnt', YLeaf(YType.uint64, 'tx-pkt-cnt')),
                                    ('rx_drop_pkt_cnt', YLeaf(YType.uint64, 'rx-drop-pkt-cnt')),
                                    ('rx_fabric_to_cnt', YLeaf(YType.uint64, 'rx-fabric-to-cnt')),
                                    ('ack_wait_cnt', YLeaf(YType.uint64, 'ack-wait-cnt')),
                                ])
                                self.dest_drop_pkt_cnt = None
                                self.src_dest_pkt_cnt = None
                                self.dest_src_pkt_cnt = None
                                self.rcv_pkt_cnt = None
                                self.tx_pkt_cnt = None
                                self.rx_drop_pkt_cnt = None
                                self.rx_fabric_to_cnt = None
                                self.ack_wait_cnt = None
                                self._segment_path = lambda: "ua1-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua1Stats, ['dest_drop_pkt_cnt', 'src_dest_pkt_cnt', 'dest_src_pkt_cnt', 'rcv_pkt_cnt', 'tx_pkt_cnt', 'rx_drop_pkt_cnt', 'rx_fabric_to_cnt', 'ack_wait_cnt'], name, value)


                        class Ua2Stats(Entity):
                            """
                            ua2 stats
                            
                            .. attribute:: dest_drop_pkt_cnt
                            
                            	DEST DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: src_dest_pkt_cnt
                            
                            	SRC DEST PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dest_src_pkt_cnt
                            
                            	DEST SRC PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rcv_pkt_cnt
                            
                            	RCV PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tx_pkt_cnt
                            
                            	TX PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_drop_pkt_cnt
                            
                            	RX DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_fabric_to_cnt
                            
                            	RX FABRIC TO CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ack_wait_cnt
                            
                            	ACK WAIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'asr9k-xbar-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua2Stats, self).__init__()

                                self.yang_name = "ua2-stats"
                                self.yang_parent_name = "sm15-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('dest_drop_pkt_cnt', YLeaf(YType.uint64, 'dest-drop-pkt-cnt')),
                                    ('src_dest_pkt_cnt', YLeaf(YType.uint64, 'src-dest-pkt-cnt')),
                                    ('dest_src_pkt_cnt', YLeaf(YType.uint64, 'dest-src-pkt-cnt')),
                                    ('rcv_pkt_cnt', YLeaf(YType.uint64, 'rcv-pkt-cnt')),
                                    ('tx_pkt_cnt', YLeaf(YType.uint64, 'tx-pkt-cnt')),
                                    ('rx_drop_pkt_cnt', YLeaf(YType.uint64, 'rx-drop-pkt-cnt')),
                                    ('rx_fabric_to_cnt', YLeaf(YType.uint64, 'rx-fabric-to-cnt')),
                                    ('ack_wait_cnt', YLeaf(YType.uint64, 'ack-wait-cnt')),
                                ])
                                self.dest_drop_pkt_cnt = None
                                self.src_dest_pkt_cnt = None
                                self.dest_src_pkt_cnt = None
                                self.rcv_pkt_cnt = None
                                self.tx_pkt_cnt = None
                                self.rx_drop_pkt_cnt = None
                                self.rx_fabric_to_cnt = None
                                self.ack_wait_cnt = None
                                self._segment_path = lambda: "ua2-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua2Stats, ['dest_drop_pkt_cnt', 'src_dest_pkt_cnt', 'dest_src_pkt_cnt', 'rcv_pkt_cnt', 'tx_pkt_cnt', 'rx_drop_pkt_cnt', 'rx_fabric_to_cnt', 'ack_wait_cnt'], name, value)


                        class MaStats(Entity):
                            """
                            ma stats
                            
                            .. attribute:: dest_drop_pkt_cnt
                            
                            	DEST DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: src_dest_pkt_cnt
                            
                            	SRC DEST PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dest_src_pkt_cnt
                            
                            	DEST SRC PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rcv_pkt_cnt
                            
                            	RCV PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tx_pkt_cnt
                            
                            	TX PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_drop_pkt_cnt
                            
                            	RX DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_re_transmit_cnt
                            
                            	RX RETRANSMIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_fabric_to_cnt
                            
                            	RX FABRIC TO CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_hol_to_cnt
                            
                            	RX HOL TO CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'asr9k-xbar-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.MaStats, self).__init__()

                                self.yang_name = "ma-stats"
                                self.yang_parent_name = "sm15-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('dest_drop_pkt_cnt', YLeaf(YType.uint64, 'dest-drop-pkt-cnt')),
                                    ('src_dest_pkt_cnt', YLeaf(YType.uint64, 'src-dest-pkt-cnt')),
                                    ('dest_src_pkt_cnt', YLeaf(YType.uint64, 'dest-src-pkt-cnt')),
                                    ('rcv_pkt_cnt', YLeaf(YType.uint64, 'rcv-pkt-cnt')),
                                    ('tx_pkt_cnt', YLeaf(YType.uint64, 'tx-pkt-cnt')),
                                    ('rx_drop_pkt_cnt', YLeaf(YType.uint64, 'rx-drop-pkt-cnt')),
                                    ('rx_re_transmit_cnt', YLeaf(YType.uint64, 'rx-re-transmit-cnt')),
                                    ('rx_fabric_to_cnt', YLeaf(YType.uint64, 'rx-fabric-to-cnt')),
                                    ('rx_hol_to_cnt', YLeaf(YType.uint64, 'rx-hol-to-cnt')),
                                ])
                                self.dest_drop_pkt_cnt = None
                                self.src_dest_pkt_cnt = None
                                self.dest_src_pkt_cnt = None
                                self.rcv_pkt_cnt = None
                                self.tx_pkt_cnt = None
                                self.rx_drop_pkt_cnt = None
                                self.rx_re_transmit_cnt = None
                                self.rx_fabric_to_cnt = None
                                self.rx_hol_to_cnt = None
                                self._segment_path = lambda: "ma-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.MaStats, ['dest_drop_pkt_cnt', 'src_dest_pkt_cnt', 'dest_src_pkt_cnt', 'rcv_pkt_cnt', 'tx_pkt_cnt', 'rx_drop_pkt_cnt', 'rx_re_transmit_cnt', 'rx_fabric_to_cnt', 'rx_hol_to_cnt'], name, value)


                        class CaStats(Entity):
                            """
                            ca stats
                            
                            .. attribute:: dest_drop_pkt_cnt
                            
                            	DEST DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: src_dest_pkt_cnt
                            
                            	SRC DEST PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dest_src_pkt_cnt
                            
                            	DEST SRC PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rcv_pkt_cnt
                            
                            	RCV PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tx_pkt_cnt
                            
                            	TX PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_drop_pkt_cnt
                            
                            	RX DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'asr9k-xbar-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.CaStats, self).__init__()

                                self.yang_name = "ca-stats"
                                self.yang_parent_name = "sm15-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('dest_drop_pkt_cnt', YLeaf(YType.uint64, 'dest-drop-pkt-cnt')),
                                    ('src_dest_pkt_cnt', YLeaf(YType.uint64, 'src-dest-pkt-cnt')),
                                    ('dest_src_pkt_cnt', YLeaf(YType.uint64, 'dest-src-pkt-cnt')),
                                    ('rcv_pkt_cnt', YLeaf(YType.uint64, 'rcv-pkt-cnt')),
                                    ('tx_pkt_cnt', YLeaf(YType.uint64, 'tx-pkt-cnt')),
                                    ('rx_drop_pkt_cnt', YLeaf(YType.uint64, 'rx-drop-pkt-cnt')),
                                ])
                                self.dest_drop_pkt_cnt = None
                                self.src_dest_pkt_cnt = None
                                self.dest_src_pkt_cnt = None
                                self.rcv_pkt_cnt = None
                                self.tx_pkt_cnt = None
                                self.rx_drop_pkt_cnt = None
                                self._segment_path = lambda: "ca-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.CaStats, ['dest_drop_pkt_cnt', 'src_dest_pkt_cnt', 'dest_src_pkt_cnt', 'rcv_pkt_cnt', 'tx_pkt_cnt', 'rx_drop_pkt_cnt'], name, value)


                        class PiStats(Entity):
                            """
                            pi stats
                            
                            .. attribute:: total_rate1_cnt
                            
                            	TOTAL RATE1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: total_rate2_cnt
                            
                            	TOTAL RATE2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: total_rate3_cnt
                            
                            	TOTAL RATE3 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: total_calc_rate
                            
                            	total calc rate
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'asr9k-xbar-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiStats, self).__init__()

                                self.yang_name = "pi-stats"
                                self.yang_parent_name = "sm15-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('total_rate1_cnt', YLeaf(YType.uint64, 'total-rate1-cnt')),
                                    ('total_rate2_cnt', YLeaf(YType.uint64, 'total-rate2-cnt')),
                                    ('total_rate3_cnt', YLeaf(YType.uint64, 'total-rate3-cnt')),
                                    ('total_calc_rate', YLeaf(YType.uint64, 'total-calc-rate')),
                                ])
                                self.total_rate1_cnt = None
                                self.total_rate2_cnt = None
                                self.total_rate3_cnt = None
                                self.total_calc_rate = None
                                self._segment_path = lambda: "pi-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiStats, ['total_rate1_cnt', 'total_rate2_cnt', 'total_rate3_cnt', 'total_calc_rate'], name, value)


                        class PeStats(Entity):
                            """
                            pe stats
                            
                            .. attribute:: total_rate1_cnt
                            
                            	TOTAL RATE1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: total_rate2_cnt
                            
                            	TOTAL RATE2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: total_rate3_cnt
                            
                            	TOTAL RATE3 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: total_calc_rate
                            
                            	total calc rate
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: mc2uc_preempt_cnt
                            
                            	MC2UC PREEMPT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'asr9k-xbar-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeStats, self).__init__()

                                self.yang_name = "pe-stats"
                                self.yang_parent_name = "sm15-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('total_rate1_cnt', YLeaf(YType.uint64, 'total-rate1-cnt')),
                                    ('total_rate2_cnt', YLeaf(YType.uint64, 'total-rate2-cnt')),
                                    ('total_rate3_cnt', YLeaf(YType.uint64, 'total-rate3-cnt')),
                                    ('total_calc_rate', YLeaf(YType.uint64, 'total-calc-rate')),
                                    ('mc2uc_preempt_cnt', YLeaf(YType.uint64, 'mc2uc-preempt-cnt')),
                                ])
                                self.total_rate1_cnt = None
                                self.total_rate2_cnt = None
                                self.total_rate3_cnt = None
                                self.total_calc_rate = None
                                self.mc2uc_preempt_cnt = None
                                self._segment_path = lambda: "pe-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeStats, ['total_rate1_cnt', 'total_rate2_cnt', 'total_rate3_cnt', 'total_calc_rate', 'mc2uc_preempt_cnt'], name, value)


                        class PiUcStats(Entity):
                            """
                            pi uc stats
                            
                            .. attribute:: pkt_rcv_cnt
                            
                            	PKT RCV CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_seq_err_cnt
                            
                            	PKT SEQ ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_coming_pkt_err_cnt
                            
                            	INCOMING PKT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: min_pkt_len_err_cnt
                            
                            	MIN PKT LEN ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: max_pkt_len_err_cnt
                            
                            	MAX PKT LEN ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: line_err_drp_pkt
                            
                            	LINE ERR DRP PKT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_crc_err_cnt
                            
                            	PKT CRC ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_cfh_crc_err_cnt
                            
                            	PKT CFH CRC ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: line_s_written_in_mem0
                            
                            	LINES WRITTEN IN MEM0
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: line_s_written_in_mem1
                            
                            	LINES WRITTEN IN MEM1
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: line_s_written_in_mem2
                            
                            	LINES WRITTEN IN MEM2
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tail_drp_pkt_cnt
                            
                            	TAIL DRP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: uc0_data_mem_ecc_1bit_err_cnt
                            
                            	UC0 DATA MEM ECC 1BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: uc1_data_mem_ecc_1bit_err_cnt
                            
                            	UC1 DATA MEM ECC 1BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: uc2_data_mem_ecc_1bit_err_cnt
                            
                            	UC2 DATA MEM ECC 1BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: uc0_data_mem_ecc_2bit_err_cnt
                            
                            	UC0 DATA MEM ECC 2BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: uc1_data_mem_ecc_2bit_err_cnt
                            
                            	UC1 DATA MEM ECC 2BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: uc2_data_mem_ecc_2bit_err_cnt
                            
                            	UC2 DATA MEM ECC 2BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: diag_pkt_cnt
                            
                            	DIAG PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_sent_to_disabled_port_cnt
                            
                            	PKT SENT TO DISABLED PORT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_null_poe_sent_ua0_cnt
                            
                            	PKT NULL POE SENT UA0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_null_poe_sent_ua1_cnt
                            
                            	PKT NULL POE SENT UA1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_null_poe_sent_ua2_cnt
                            
                            	PKT NULL POE SENT UA2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_fpoe_addr_rng_hit_cnt
                            
                            	PKT FPOE ADDR RNG HIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fpoe_mem_ecc_1bit_err_cnt
                            
                            	FPOE MEM ECC 1BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fpoe_mem_ecc_2bit_err_cnt
                            
                            	FPOE MEM ECC 2BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkts_sent_to_ux0_cnt
                            
                            	PKTS SENT TO UX0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkts_sent_to_ux1_cnt
                            
                            	PKTS SENT TO UX1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkts_sent_to_ux2_cnt
                            
                            	PKTS SENT TO UX2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: cpp_head_drop_pkt_cnt
                            
                            	CPP HEAD DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tr_head_drop_pkt_cnt
                            
                            	TR HEAD DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tr_pkt_sent_to_ux
                            
                            	TR PKT SENT TO UX
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: stop_thrsh_hit_cnt
                            
                            	STOP THRSH HIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rate_cnt
                            
                            	RATE CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: calc_rate
                            
                            	calc rate
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: crc_stomp_pkt_cnt
                            
                            	CRC STOMP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'asr9k-xbar-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiUcStats, self).__init__()

                                self.yang_name = "pi-uc-stats"
                                self.yang_parent_name = "sm15-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('pkt_rcv_cnt', YLeaf(YType.uint64, 'pkt-rcv-cnt')),
                                    ('pkt_seq_err_cnt', YLeaf(YType.uint64, 'pkt-seq-err-cnt')),
                                    ('in_coming_pkt_err_cnt', YLeaf(YType.uint64, 'in-coming-pkt-err-cnt')),
                                    ('min_pkt_len_err_cnt', YLeaf(YType.uint64, 'min-pkt-len-err-cnt')),
                                    ('max_pkt_len_err_cnt', YLeaf(YType.uint64, 'max-pkt-len-err-cnt')),
                                    ('line_err_drp_pkt', YLeaf(YType.uint64, 'line-err-drp-pkt')),
                                    ('pkt_crc_err_cnt', YLeaf(YType.uint64, 'pkt-crc-err-cnt')),
                                    ('pkt_cfh_crc_err_cnt', YLeaf(YType.uint64, 'pkt-cfh-crc-err-cnt')),
                                    ('line_s_written_in_mem0', YLeaf(YType.uint64, 'line-s-written-in-mem0')),
                                    ('line_s_written_in_mem1', YLeaf(YType.uint64, 'line-s-written-in-mem1')),
                                    ('line_s_written_in_mem2', YLeaf(YType.uint64, 'line-s-written-in-mem2')),
                                    ('tail_drp_pkt_cnt', YLeaf(YType.uint64, 'tail-drp-pkt-cnt')),
                                    ('uc0_data_mem_ecc_1bit_err_cnt', YLeaf(YType.uint64, 'uc0-data-mem-ecc-1bit-err-cnt')),
                                    ('uc1_data_mem_ecc_1bit_err_cnt', YLeaf(YType.uint64, 'uc1-data-mem-ecc-1bit-err-cnt')),
                                    ('uc2_data_mem_ecc_1bit_err_cnt', YLeaf(YType.uint64, 'uc2-data-mem-ecc-1bit-err-cnt')),
                                    ('uc0_data_mem_ecc_2bit_err_cnt', YLeaf(YType.uint64, 'uc0-data-mem-ecc-2bit-err-cnt')),
                                    ('uc1_data_mem_ecc_2bit_err_cnt', YLeaf(YType.uint64, 'uc1-data-mem-ecc-2bit-err-cnt')),
                                    ('uc2_data_mem_ecc_2bit_err_cnt', YLeaf(YType.uint64, 'uc2-data-mem-ecc-2bit-err-cnt')),
                                    ('diag_pkt_cnt', YLeaf(YType.uint64, 'diag-pkt-cnt')),
                                    ('pkt_sent_to_disabled_port_cnt', YLeaf(YType.uint64, 'pkt-sent-to-disabled-port-cnt')),
                                    ('pkt_null_poe_sent_ua0_cnt', YLeaf(YType.uint64, 'pkt-null-poe-sent-ua0-cnt')),
                                    ('pkt_null_poe_sent_ua1_cnt', YLeaf(YType.uint64, 'pkt-null-poe-sent-ua1-cnt')),
                                    ('pkt_null_poe_sent_ua2_cnt', YLeaf(YType.uint64, 'pkt-null-poe-sent-ua2-cnt')),
                                    ('pkt_fpoe_addr_rng_hit_cnt', YLeaf(YType.uint64, 'pkt-fpoe-addr-rng-hit-cnt')),
                                    ('fpoe_mem_ecc_1bit_err_cnt', YLeaf(YType.uint64, 'fpoe-mem-ecc-1bit-err-cnt')),
                                    ('fpoe_mem_ecc_2bit_err_cnt', YLeaf(YType.uint64, 'fpoe-mem-ecc-2bit-err-cnt')),
                                    ('pkts_sent_to_ux0_cnt', YLeaf(YType.uint64, 'pkts-sent-to-ux0-cnt')),
                                    ('pkts_sent_to_ux1_cnt', YLeaf(YType.uint64, 'pkts-sent-to-ux1-cnt')),
                                    ('pkts_sent_to_ux2_cnt', YLeaf(YType.uint64, 'pkts-sent-to-ux2-cnt')),
                                    ('cpp_head_drop_pkt_cnt', YLeaf(YType.uint64, 'cpp-head-drop-pkt-cnt')),
                                    ('tr_head_drop_pkt_cnt', YLeaf(YType.uint64, 'tr-head-drop-pkt-cnt')),
                                    ('tr_pkt_sent_to_ux', YLeaf(YType.uint64, 'tr-pkt-sent-to-ux')),
                                    ('stop_thrsh_hit_cnt', YLeaf(YType.uint64, 'stop-thrsh-hit-cnt')),
                                    ('rate_cnt', YLeaf(YType.uint64, 'rate-cnt')),
                                    ('calc_rate', YLeaf(YType.uint64, 'calc-rate')),
                                    ('crc_stomp_pkt_cnt', YLeaf(YType.uint64, 'crc-stomp-pkt-cnt')),
                                ])
                                self.pkt_rcv_cnt = None
                                self.pkt_seq_err_cnt = None
                                self.in_coming_pkt_err_cnt = None
                                self.min_pkt_len_err_cnt = None
                                self.max_pkt_len_err_cnt = None
                                self.line_err_drp_pkt = None
                                self.pkt_crc_err_cnt = None
                                self.pkt_cfh_crc_err_cnt = None
                                self.line_s_written_in_mem0 = None
                                self.line_s_written_in_mem1 = None
                                self.line_s_written_in_mem2 = None
                                self.tail_drp_pkt_cnt = None
                                self.uc0_data_mem_ecc_1bit_err_cnt = None
                                self.uc1_data_mem_ecc_1bit_err_cnt = None
                                self.uc2_data_mem_ecc_1bit_err_cnt = None
                                self.uc0_data_mem_ecc_2bit_err_cnt = None
                                self.uc1_data_mem_ecc_2bit_err_cnt = None
                                self.uc2_data_mem_ecc_2bit_err_cnt = None
                                self.diag_pkt_cnt = None
                                self.pkt_sent_to_disabled_port_cnt = None
                                self.pkt_null_poe_sent_ua0_cnt = None
                                self.pkt_null_poe_sent_ua1_cnt = None
                                self.pkt_null_poe_sent_ua2_cnt = None
                                self.pkt_fpoe_addr_rng_hit_cnt = None
                                self.fpoe_mem_ecc_1bit_err_cnt = None
                                self.fpoe_mem_ecc_2bit_err_cnt = None
                                self.pkts_sent_to_ux0_cnt = None
                                self.pkts_sent_to_ux1_cnt = None
                                self.pkts_sent_to_ux2_cnt = None
                                self.cpp_head_drop_pkt_cnt = None
                                self.tr_head_drop_pkt_cnt = None
                                self.tr_pkt_sent_to_ux = None
                                self.stop_thrsh_hit_cnt = None
                                self.rate_cnt = None
                                self.calc_rate = None
                                self.crc_stomp_pkt_cnt = None
                                self._segment_path = lambda: "pi-uc-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiUcStats, ['pkt_rcv_cnt', 'pkt_seq_err_cnt', 'in_coming_pkt_err_cnt', 'min_pkt_len_err_cnt', 'max_pkt_len_err_cnt', 'line_err_drp_pkt', 'pkt_crc_err_cnt', 'pkt_cfh_crc_err_cnt', 'line_s_written_in_mem0', 'line_s_written_in_mem1', 'line_s_written_in_mem2', 'tail_drp_pkt_cnt', 'uc0_data_mem_ecc_1bit_err_cnt', 'uc1_data_mem_ecc_1bit_err_cnt', 'uc2_data_mem_ecc_1bit_err_cnt', 'uc0_data_mem_ecc_2bit_err_cnt', 'uc1_data_mem_ecc_2bit_err_cnt', 'uc2_data_mem_ecc_2bit_err_cnt', 'diag_pkt_cnt', 'pkt_sent_to_disabled_port_cnt', 'pkt_null_poe_sent_ua0_cnt', 'pkt_null_poe_sent_ua1_cnt', 'pkt_null_poe_sent_ua2_cnt', 'pkt_fpoe_addr_rng_hit_cnt', 'fpoe_mem_ecc_1bit_err_cnt', 'fpoe_mem_ecc_2bit_err_cnt', 'pkts_sent_to_ux0_cnt', 'pkts_sent_to_ux1_cnt', 'pkts_sent_to_ux2_cnt', 'cpp_head_drop_pkt_cnt', 'tr_head_drop_pkt_cnt', 'tr_pkt_sent_to_ux', 'stop_thrsh_hit_cnt', 'rate_cnt', 'calc_rate', 'crc_stomp_pkt_cnt'], name, value)


                        class PiMcStats(Entity):
                            """
                            pi mc stats
                            
                            .. attribute:: pkt_rcv_cnt
                            
                            	PKT RCV CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_seq_err_cnt
                            
                            	PKT SEQ ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_coming_pkt_err_cnt
                            
                            	INCOMING PKT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: min_pkt_len_err_cnt
                            
                            	MIN PKT LEN ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: max_pkt_len_err_cnt
                            
                            	MAX PKT LEN ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: line_err_drp_pkt
                            
                            	LINE ERR DRP PKT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_crc_err_cnt
                            
                            	PKT CRC ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_cfh_crc_err_cnt
                            
                            	PKT CFH CRC ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: line_s_written_in_mem
                            
                            	LINES WRITTEN IN MEM
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tail_drp_pkt_cnt
                            
                            	TAIL DRP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem0_ecc_1bit_err_cnt
                            
                            	DATA MEM0 ECC 1BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem1_ecc_1bit_err_cnt
                            
                            	DATA MEM1 ECC 1BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem2_ecc_1bit_err_cnt
                            
                            	DATA MEM2 ECC 1BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem0_ecc_2bit_err_cnt
                            
                            	DATA MEM0 ECC 2BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem1_ecc_2bit_err_cnt
                            
                            	DATA MEM1 ECC 2BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem2_ecc_2bit_err_cnt
                            
                            	DATA MEM2 ECC 2BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: diag_pkt_cnt
                            
                            	DIAG PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_sent_to_disabled_port
                            
                            	PKT SENT TO DISABLED PORT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_fpoe_match_hit_cnt
                            
                            	PKT FPOE MATCH HIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_null_poe_sent_cnt
                            
                            	PKT NULL POE SENT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_fpoe_addr_rng_hit_cnt
                            
                            	PKT FPOE ADDR RNG HIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: di_hdr_len_err_pkt_cnt
                            
                            	DI HDR LEN ERR PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: di_err_pkt_cnt
                            
                            	DI ERR PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fpoe_mem_ecc_1bit_err_cnt
                            
                            	FPOE MEM ECC 1BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fpoe_mem_ecc_2bit_err_cnt
                            
                            	FPOE MEM ECC 2BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkts_sent_to_mx_cnt
                            
                            	PKTS SENT TO MX CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: cpp_head_drop_pkt_from_ma_cnt
                            
                            	CPP HEAD DROP PKT FROM MA CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tr_head_drop_pkt_from_ma_cnt
                            
                            	TR HEAD DROP PKT FROM MA CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tr_pkt_sent_to_mx
                            
                            	TR PKT SENT TO MX
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: stop_thrsh_hit_cnt
                            
                            	STOP THRSH HIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rate_cnt
                            
                            	RATE CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: calc_rate
                            
                            	calc rate
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: crc_stomp_pkt_cnt
                            
                            	CRC STOMP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'asr9k-xbar-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiMcStats, self).__init__()

                                self.yang_name = "pi-mc-stats"
                                self.yang_parent_name = "sm15-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('pkt_rcv_cnt', YLeaf(YType.uint64, 'pkt-rcv-cnt')),
                                    ('pkt_seq_err_cnt', YLeaf(YType.uint64, 'pkt-seq-err-cnt')),
                                    ('in_coming_pkt_err_cnt', YLeaf(YType.uint64, 'in-coming-pkt-err-cnt')),
                                    ('min_pkt_len_err_cnt', YLeaf(YType.uint64, 'min-pkt-len-err-cnt')),
                                    ('max_pkt_len_err_cnt', YLeaf(YType.uint64, 'max-pkt-len-err-cnt')),
                                    ('line_err_drp_pkt', YLeaf(YType.uint64, 'line-err-drp-pkt')),
                                    ('pkt_crc_err_cnt', YLeaf(YType.uint64, 'pkt-crc-err-cnt')),
                                    ('pkt_cfh_crc_err_cnt', YLeaf(YType.uint64, 'pkt-cfh-crc-err-cnt')),
                                    ('line_s_written_in_mem', YLeaf(YType.uint64, 'line-s-written-in-mem')),
                                    ('tail_drp_pkt_cnt', YLeaf(YType.uint64, 'tail-drp-pkt-cnt')),
                                    ('data_mem0_ecc_1bit_err_cnt', YLeaf(YType.uint64, 'data-mem0-ecc-1bit-err-cnt')),
                                    ('data_mem1_ecc_1bit_err_cnt', YLeaf(YType.uint64, 'data-mem1-ecc-1bit-err-cnt')),
                                    ('data_mem2_ecc_1bit_err_cnt', YLeaf(YType.uint64, 'data-mem2-ecc-1bit-err-cnt')),
                                    ('data_mem0_ecc_2bit_err_cnt', YLeaf(YType.uint64, 'data-mem0-ecc-2bit-err-cnt')),
                                    ('data_mem1_ecc_2bit_err_cnt', YLeaf(YType.uint64, 'data-mem1-ecc-2bit-err-cnt')),
                                    ('data_mem2_ecc_2bit_err_cnt', YLeaf(YType.uint64, 'data-mem2-ecc-2bit-err-cnt')),
                                    ('diag_pkt_cnt', YLeaf(YType.uint64, 'diag-pkt-cnt')),
                                    ('pkt_sent_to_disabled_port', YLeaf(YType.uint64, 'pkt-sent-to-disabled-port')),
                                    ('pkt_fpoe_match_hit_cnt', YLeaf(YType.uint64, 'pkt-fpoe-match-hit-cnt')),
                                    ('pkt_null_poe_sent_cnt', YLeaf(YType.uint64, 'pkt-null-poe-sent-cnt')),
                                    ('pkt_fpoe_addr_rng_hit_cnt', YLeaf(YType.uint64, 'pkt-fpoe-addr-rng-hit-cnt')),
                                    ('di_hdr_len_err_pkt_cnt', YLeaf(YType.uint64, 'di-hdr-len-err-pkt-cnt')),
                                    ('di_err_pkt_cnt', YLeaf(YType.uint64, 'di-err-pkt-cnt')),
                                    ('fpoe_mem_ecc_1bit_err_cnt', YLeaf(YType.uint64, 'fpoe-mem-ecc-1bit-err-cnt')),
                                    ('fpoe_mem_ecc_2bit_err_cnt', YLeaf(YType.uint64, 'fpoe-mem-ecc-2bit-err-cnt')),
                                    ('pkts_sent_to_mx_cnt', YLeaf(YType.uint64, 'pkts-sent-to-mx-cnt')),
                                    ('cpp_head_drop_pkt_from_ma_cnt', YLeaf(YType.uint64, 'cpp-head-drop-pkt-from-ma-cnt')),
                                    ('tr_head_drop_pkt_from_ma_cnt', YLeaf(YType.uint64, 'tr-head-drop-pkt-from-ma-cnt')),
                                    ('tr_pkt_sent_to_mx', YLeaf(YType.uint64, 'tr-pkt-sent-to-mx')),
                                    ('stop_thrsh_hit_cnt', YLeaf(YType.uint64, 'stop-thrsh-hit-cnt')),
                                    ('rate_cnt', YLeaf(YType.uint64, 'rate-cnt')),
                                    ('calc_rate', YLeaf(YType.uint64, 'calc-rate')),
                                    ('crc_stomp_pkt_cnt', YLeaf(YType.uint64, 'crc-stomp-pkt-cnt')),
                                ])
                                self.pkt_rcv_cnt = None
                                self.pkt_seq_err_cnt = None
                                self.in_coming_pkt_err_cnt = None
                                self.min_pkt_len_err_cnt = None
                                self.max_pkt_len_err_cnt = None
                                self.line_err_drp_pkt = None
                                self.pkt_crc_err_cnt = None
                                self.pkt_cfh_crc_err_cnt = None
                                self.line_s_written_in_mem = None
                                self.tail_drp_pkt_cnt = None
                                self.data_mem0_ecc_1bit_err_cnt = None
                                self.data_mem1_ecc_1bit_err_cnt = None
                                self.data_mem2_ecc_1bit_err_cnt = None
                                self.data_mem0_ecc_2bit_err_cnt = None
                                self.data_mem1_ecc_2bit_err_cnt = None
                                self.data_mem2_ecc_2bit_err_cnt = None
                                self.diag_pkt_cnt = None
                                self.pkt_sent_to_disabled_port = None
                                self.pkt_fpoe_match_hit_cnt = None
                                self.pkt_null_poe_sent_cnt = None
                                self.pkt_fpoe_addr_rng_hit_cnt = None
                                self.di_hdr_len_err_pkt_cnt = None
                                self.di_err_pkt_cnt = None
                                self.fpoe_mem_ecc_1bit_err_cnt = None
                                self.fpoe_mem_ecc_2bit_err_cnt = None
                                self.pkts_sent_to_mx_cnt = None
                                self.cpp_head_drop_pkt_from_ma_cnt = None
                                self.tr_head_drop_pkt_from_ma_cnt = None
                                self.tr_pkt_sent_to_mx = None
                                self.stop_thrsh_hit_cnt = None
                                self.rate_cnt = None
                                self.calc_rate = None
                                self.crc_stomp_pkt_cnt = None
                                self._segment_path = lambda: "pi-mc-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiMcStats, ['pkt_rcv_cnt', 'pkt_seq_err_cnt', 'in_coming_pkt_err_cnt', 'min_pkt_len_err_cnt', 'max_pkt_len_err_cnt', 'line_err_drp_pkt', 'pkt_crc_err_cnt', 'pkt_cfh_crc_err_cnt', 'line_s_written_in_mem', 'tail_drp_pkt_cnt', 'data_mem0_ecc_1bit_err_cnt', 'data_mem1_ecc_1bit_err_cnt', 'data_mem2_ecc_1bit_err_cnt', 'data_mem0_ecc_2bit_err_cnt', 'data_mem1_ecc_2bit_err_cnt', 'data_mem2_ecc_2bit_err_cnt', 'diag_pkt_cnt', 'pkt_sent_to_disabled_port', 'pkt_fpoe_match_hit_cnt', 'pkt_null_poe_sent_cnt', 'pkt_fpoe_addr_rng_hit_cnt', 'di_hdr_len_err_pkt_cnt', 'di_err_pkt_cnt', 'fpoe_mem_ecc_1bit_err_cnt', 'fpoe_mem_ecc_2bit_err_cnt', 'pkts_sent_to_mx_cnt', 'cpp_head_drop_pkt_from_ma_cnt', 'tr_head_drop_pkt_from_ma_cnt', 'tr_pkt_sent_to_mx', 'stop_thrsh_hit_cnt', 'rate_cnt', 'calc_rate', 'crc_stomp_pkt_cnt'], name, value)


                        class PiCcStats(Entity):
                            """
                            pi cc stats
                            
                            .. attribute:: in0_ecc_serr_cnt
                            
                            	IN0 ECC SERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in0_ecc_derr_cnt
                            
                            	IN0 ECC DERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in1_ecc_serr_cnt
                            
                            	IN1 ECC SERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in1_ecc_derr_cnt
                            
                            	IN1 ECC DERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem_ecc_serr_cnt
                            
                            	DATA MEM ECC SERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem_ecc_derr_cnt
                            
                            	DATA MEM ECC DERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem_ovf0_cnt
                            
                            	DATA MEM OVF0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem_ovf1_cnt
                            
                            	DATA MEM OVF1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fpoe_mem_ecc_serr_cnt
                            
                            	FPOE MEM ECC SERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fpoe_mem_ecc_derr_cnt
                            
                            	FPOE MEM ECC DERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: null_poe_cnt
                            
                            	NULL POE CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: shut_ack_cnt
                            
                            	SHUT ACK CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in0_fnc_err_cnt
                            
                            	IN0 FNC ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in1_fnc_err_cnt
                            
                            	IN1 FNC ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in0_drop_cnt
                            
                            	IN0 DROP CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in1_drop_cnt
                            
                            	IN1 DROP CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in0_cong_cnt
                            
                            	IN0 CONG CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in1_cong_cnt
                            
                            	IN1 CONG CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in0_shut_cnt
                            
                            	IN0 SHUT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in1_shut_cnt
                            
                            	IN1 SHUT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tail_drop_msg_cnt
                            
                            	TAIL DROP MSG CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in0_pkt_cnt
                            
                            	IN0 PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in1_pkt_cnt
                            
                            	IN1 PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dmem_rd_cnt
                            
                            	DMEM RD CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_dmem0_cnt
                            
                            	IN DMEM0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_dmem1_cnt
                            
                            	IN DMEM1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_pkt_cnt
                            
                            	OUT PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: stop_thrsh_hit_cnt
                            
                            	STOP THRSH HIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rate_cnt
                            
                            	RATE CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: calc_rate
                            
                            	calc rate
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'asr9k-xbar-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiCcStats, self).__init__()

                                self.yang_name = "pi-cc-stats"
                                self.yang_parent_name = "sm15-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('in0_ecc_serr_cnt', YLeaf(YType.uint64, 'in0-ecc-serr-cnt')),
                                    ('in0_ecc_derr_cnt', YLeaf(YType.uint64, 'in0-ecc-derr-cnt')),
                                    ('in1_ecc_serr_cnt', YLeaf(YType.uint64, 'in1-ecc-serr-cnt')),
                                    ('in1_ecc_derr_cnt', YLeaf(YType.uint64, 'in1-ecc-derr-cnt')),
                                    ('data_mem_ecc_serr_cnt', YLeaf(YType.uint64, 'data-mem-ecc-serr-cnt')),
                                    ('data_mem_ecc_derr_cnt', YLeaf(YType.uint64, 'data-mem-ecc-derr-cnt')),
                                    ('data_mem_ovf0_cnt', YLeaf(YType.uint64, 'data-mem-ovf0-cnt')),
                                    ('data_mem_ovf1_cnt', YLeaf(YType.uint64, 'data-mem-ovf1-cnt')),
                                    ('fpoe_mem_ecc_serr_cnt', YLeaf(YType.uint64, 'fpoe-mem-ecc-serr-cnt')),
                                    ('fpoe_mem_ecc_derr_cnt', YLeaf(YType.uint64, 'fpoe-mem-ecc-derr-cnt')),
                                    ('null_poe_cnt', YLeaf(YType.uint64, 'null-poe-cnt')),
                                    ('shut_ack_cnt', YLeaf(YType.uint64, 'shut-ack-cnt')),
                                    ('in0_fnc_err_cnt', YLeaf(YType.uint64, 'in0-fnc-err-cnt')),
                                    ('in1_fnc_err_cnt', YLeaf(YType.uint64, 'in1-fnc-err-cnt')),
                                    ('in0_drop_cnt', YLeaf(YType.uint64, 'in0-drop-cnt')),
                                    ('in1_drop_cnt', YLeaf(YType.uint64, 'in1-drop-cnt')),
                                    ('in0_cong_cnt', YLeaf(YType.uint64, 'in0-cong-cnt')),
                                    ('in1_cong_cnt', YLeaf(YType.uint64, 'in1-cong-cnt')),
                                    ('in0_shut_cnt', YLeaf(YType.uint64, 'in0-shut-cnt')),
                                    ('in1_shut_cnt', YLeaf(YType.uint64, 'in1-shut-cnt')),
                                    ('tail_drop_msg_cnt', YLeaf(YType.uint64, 'tail-drop-msg-cnt')),
                                    ('in0_pkt_cnt', YLeaf(YType.uint64, 'in0-pkt-cnt')),
                                    ('in1_pkt_cnt', YLeaf(YType.uint64, 'in1-pkt-cnt')),
                                    ('dmem_rd_cnt', YLeaf(YType.uint64, 'dmem-rd-cnt')),
                                    ('in_dmem0_cnt', YLeaf(YType.uint64, 'in-dmem0-cnt')),
                                    ('in_dmem1_cnt', YLeaf(YType.uint64, 'in-dmem1-cnt')),
                                    ('out_pkt_cnt', YLeaf(YType.uint64, 'out-pkt-cnt')),
                                    ('stop_thrsh_hit_cnt', YLeaf(YType.uint64, 'stop-thrsh-hit-cnt')),
                                    ('rate_cnt', YLeaf(YType.uint64, 'rate-cnt')),
                                    ('calc_rate', YLeaf(YType.uint64, 'calc-rate')),
                                ])
                                self.in0_ecc_serr_cnt = None
                                self.in0_ecc_derr_cnt = None
                                self.in1_ecc_serr_cnt = None
                                self.in1_ecc_derr_cnt = None
                                self.data_mem_ecc_serr_cnt = None
                                self.data_mem_ecc_derr_cnt = None
                                self.data_mem_ovf0_cnt = None
                                self.data_mem_ovf1_cnt = None
                                self.fpoe_mem_ecc_serr_cnt = None
                                self.fpoe_mem_ecc_derr_cnt = None
                                self.null_poe_cnt = None
                                self.shut_ack_cnt = None
                                self.in0_fnc_err_cnt = None
                                self.in1_fnc_err_cnt = None
                                self.in0_drop_cnt = None
                                self.in1_drop_cnt = None
                                self.in0_cong_cnt = None
                                self.in1_cong_cnt = None
                                self.in0_shut_cnt = None
                                self.in1_shut_cnt = None
                                self.tail_drop_msg_cnt = None
                                self.in0_pkt_cnt = None
                                self.in1_pkt_cnt = None
                                self.dmem_rd_cnt = None
                                self.in_dmem0_cnt = None
                                self.in_dmem1_cnt = None
                                self.out_pkt_cnt = None
                                self.stop_thrsh_hit_cnt = None
                                self.rate_cnt = None
                                self.calc_rate = None
                                self._segment_path = lambda: "pi-cc-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiCcStats, ['in0_ecc_serr_cnt', 'in0_ecc_derr_cnt', 'in1_ecc_serr_cnt', 'in1_ecc_derr_cnt', 'data_mem_ecc_serr_cnt', 'data_mem_ecc_derr_cnt', 'data_mem_ovf0_cnt', 'data_mem_ovf1_cnt', 'fpoe_mem_ecc_serr_cnt', 'fpoe_mem_ecc_derr_cnt', 'null_poe_cnt', 'shut_ack_cnt', 'in0_fnc_err_cnt', 'in1_fnc_err_cnt', 'in0_drop_cnt', 'in1_drop_cnt', 'in0_cong_cnt', 'in1_cong_cnt', 'in0_shut_cnt', 'in1_shut_cnt', 'tail_drop_msg_cnt', 'in0_pkt_cnt', 'in1_pkt_cnt', 'dmem_rd_cnt', 'in_dmem0_cnt', 'in_dmem1_cnt', 'out_pkt_cnt', 'stop_thrsh_hit_cnt', 'rate_cnt', 'calc_rate'], name, value)


                        class PeUcStats(Entity):
                            """
                            pe uc stats
                            
                            .. attribute:: in_pkt_uc0_cnt
                            
                            	IN PKT UC0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_pkt_uc1_cnt
                            
                            	IN PKT UC1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_pkt_uc2_cnt
                            
                            	IN PKT UC2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_full_line_uc0_cnt
                            
                            	IN FULL LINE UC0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_full_line_uc1_cnt
                            
                            	IN FULL LINE UC1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_full_line_uc2_cnt
                            
                            	IN FULL LINE UC2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_trunc_eop_uc0_cnt
                            
                            	PKT TRUNC EOP UC0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_trunc_eop_uc1_cnt
                            
                            	PKT TRUNC EOP UC1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_trunc_eop_uc2_cnt
                            
                            	PKT TRUNC EOP UC2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_sop_drop_uc0_cnt
                            
                            	PKT SOP DROP UC0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_sop_drop_uc1_cnt
                            
                            	PKT SOP DROP UC1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_sop_drop_uc2_cnt
                            
                            	PKT SOP DROP UC2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_ecc_err_drop_uc_cnt
                            
                            	PKT ECC ERR DROP UC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_ecc_trunc_cnt_uc_cnt
                            
                            	PKT ECC TRUNC CNT UC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_1bit_err_uc0_0_cnt
                            
                            	ECC 1BIT ERR UC0 0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_1bit_err_uc0_1_cnt
                            
                            	ECC 1BIT ERR UC0 1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_1bit_err_uc1_0_cnt
                            
                            	ECC 1BIT ERR UC1 0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_1bit_err_uc1_1_cnt
                            
                            	ECC 1BIT ERR UC1 1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_1bit_err_uc2_0_cnt
                            
                            	ECC 1BIT ERR UC2 0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_1bit_err_uc2_1_cnt
                            
                            	ECC 1BIT ERR UC2 1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_2bit_err_uc0_0_cnt
                            
                            	ECC 2BIT ERR UC0 0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_2bit_err_uc0_1_cnt
                            
                            	ECC 2BIT ERR UC0 1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_2bit_err_uc1_0_cnt
                            
                            	ECC 2BIT ERR UC1 0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_2bit_err_uc1_1_cnt
                            
                            	ECC 2BIT ERR UC1 1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_2bit_err_uc2_0_cnt
                            
                            	ECC 2BIT ERR UC2 0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_2bit_err_uc2_1_cnt
                            
                            	ECC 2BIT ERR UC2 1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_pkt_uc_cnt
                            
                            	OUT PKT UC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fe_uc_sop_eop_pack_cnt
                            
                            	FE UC SOP EOP PACK CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fc_uc_0_1_trans_cnt
                            
                            	FC UC 0 1 TRANS CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rate_cnt
                            
                            	RATE CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: calc_rate
                            
                            	calc rate
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'asr9k-xbar-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeUcStats, self).__init__()

                                self.yang_name = "pe-uc-stats"
                                self.yang_parent_name = "sm15-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('in_pkt_uc0_cnt', YLeaf(YType.uint64, 'in-pkt-uc0-cnt')),
                                    ('in_pkt_uc1_cnt', YLeaf(YType.uint64, 'in-pkt-uc1-cnt')),
                                    ('in_pkt_uc2_cnt', YLeaf(YType.uint64, 'in-pkt-uc2-cnt')),
                                    ('in_full_line_uc0_cnt', YLeaf(YType.uint64, 'in-full-line-uc0-cnt')),
                                    ('in_full_line_uc1_cnt', YLeaf(YType.uint64, 'in-full-line-uc1-cnt')),
                                    ('in_full_line_uc2_cnt', YLeaf(YType.uint64, 'in-full-line-uc2-cnt')),
                                    ('pkt_trunc_eop_uc0_cnt', YLeaf(YType.uint64, 'pkt-trunc-eop-uc0-cnt')),
                                    ('pkt_trunc_eop_uc1_cnt', YLeaf(YType.uint64, 'pkt-trunc-eop-uc1-cnt')),
                                    ('pkt_trunc_eop_uc2_cnt', YLeaf(YType.uint64, 'pkt-trunc-eop-uc2-cnt')),
                                    ('pkt_sop_drop_uc0_cnt', YLeaf(YType.uint64, 'pkt-sop-drop-uc0-cnt')),
                                    ('pkt_sop_drop_uc1_cnt', YLeaf(YType.uint64, 'pkt-sop-drop-uc1-cnt')),
                                    ('pkt_sop_drop_uc2_cnt', YLeaf(YType.uint64, 'pkt-sop-drop-uc2-cnt')),
                                    ('pkt_ecc_err_drop_uc_cnt', YLeaf(YType.uint64, 'pkt-ecc-err-drop-uc-cnt')),
                                    ('pkt_ecc_trunc_cnt_uc_cnt', YLeaf(YType.uint64, 'pkt-ecc-trunc-cnt-uc-cnt')),
                                    ('ecc_1bit_err_uc0_0_cnt', YLeaf(YType.uint64, 'ecc-1bit-err-uc0-0-cnt')),
                                    ('ecc_1bit_err_uc0_1_cnt', YLeaf(YType.uint64, 'ecc-1bit-err-uc0-1-cnt')),
                                    ('ecc_1bit_err_uc1_0_cnt', YLeaf(YType.uint64, 'ecc-1bit-err-uc1-0-cnt')),
                                    ('ecc_1bit_err_uc1_1_cnt', YLeaf(YType.uint64, 'ecc-1bit-err-uc1-1-cnt')),
                                    ('ecc_1bit_err_uc2_0_cnt', YLeaf(YType.uint64, 'ecc-1bit-err-uc2-0-cnt')),
                                    ('ecc_1bit_err_uc2_1_cnt', YLeaf(YType.uint64, 'ecc-1bit-err-uc2-1-cnt')),
                                    ('ecc_2bit_err_uc0_0_cnt', YLeaf(YType.uint64, 'ecc-2bit-err-uc0-0-cnt')),
                                    ('ecc_2bit_err_uc0_1_cnt', YLeaf(YType.uint64, 'ecc-2bit-err-uc0-1-cnt')),
                                    ('ecc_2bit_err_uc1_0_cnt', YLeaf(YType.uint64, 'ecc-2bit-err-uc1-0-cnt')),
                                    ('ecc_2bit_err_uc1_1_cnt', YLeaf(YType.uint64, 'ecc-2bit-err-uc1-1-cnt')),
                                    ('ecc_2bit_err_uc2_0_cnt', YLeaf(YType.uint64, 'ecc-2bit-err-uc2-0-cnt')),
                                    ('ecc_2bit_err_uc2_1_cnt', YLeaf(YType.uint64, 'ecc-2bit-err-uc2-1-cnt')),
                                    ('out_pkt_uc_cnt', YLeaf(YType.uint64, 'out-pkt-uc-cnt')),
                                    ('fe_uc_sop_eop_pack_cnt', YLeaf(YType.uint64, 'fe-uc-sop-eop-pack-cnt')),
                                    ('fc_uc_0_1_trans_cnt', YLeaf(YType.uint64, 'fc-uc-0-1-trans-cnt')),
                                    ('rate_cnt', YLeaf(YType.uint64, 'rate-cnt')),
                                    ('calc_rate', YLeaf(YType.uint64, 'calc-rate')),
                                ])
                                self.in_pkt_uc0_cnt = None
                                self.in_pkt_uc1_cnt = None
                                self.in_pkt_uc2_cnt = None
                                self.in_full_line_uc0_cnt = None
                                self.in_full_line_uc1_cnt = None
                                self.in_full_line_uc2_cnt = None
                                self.pkt_trunc_eop_uc0_cnt = None
                                self.pkt_trunc_eop_uc1_cnt = None
                                self.pkt_trunc_eop_uc2_cnt = None
                                self.pkt_sop_drop_uc0_cnt = None
                                self.pkt_sop_drop_uc1_cnt = None
                                self.pkt_sop_drop_uc2_cnt = None
                                self.pkt_ecc_err_drop_uc_cnt = None
                                self.pkt_ecc_trunc_cnt_uc_cnt = None
                                self.ecc_1bit_err_uc0_0_cnt = None
                                self.ecc_1bit_err_uc0_1_cnt = None
                                self.ecc_1bit_err_uc1_0_cnt = None
                                self.ecc_1bit_err_uc1_1_cnt = None
                                self.ecc_1bit_err_uc2_0_cnt = None
                                self.ecc_1bit_err_uc2_1_cnt = None
                                self.ecc_2bit_err_uc0_0_cnt = None
                                self.ecc_2bit_err_uc0_1_cnt = None
                                self.ecc_2bit_err_uc1_0_cnt = None
                                self.ecc_2bit_err_uc1_1_cnt = None
                                self.ecc_2bit_err_uc2_0_cnt = None
                                self.ecc_2bit_err_uc2_1_cnt = None
                                self.out_pkt_uc_cnt = None
                                self.fe_uc_sop_eop_pack_cnt = None
                                self.fc_uc_0_1_trans_cnt = None
                                self.rate_cnt = None
                                self.calc_rate = None
                                self._segment_path = lambda: "pe-uc-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeUcStats, ['in_pkt_uc0_cnt', 'in_pkt_uc1_cnt', 'in_pkt_uc2_cnt', 'in_full_line_uc0_cnt', 'in_full_line_uc1_cnt', 'in_full_line_uc2_cnt', 'pkt_trunc_eop_uc0_cnt', 'pkt_trunc_eop_uc1_cnt', 'pkt_trunc_eop_uc2_cnt', 'pkt_sop_drop_uc0_cnt', 'pkt_sop_drop_uc1_cnt', 'pkt_sop_drop_uc2_cnt', 'pkt_ecc_err_drop_uc_cnt', 'pkt_ecc_trunc_cnt_uc_cnt', 'ecc_1bit_err_uc0_0_cnt', 'ecc_1bit_err_uc0_1_cnt', 'ecc_1bit_err_uc1_0_cnt', 'ecc_1bit_err_uc1_1_cnt', 'ecc_1bit_err_uc2_0_cnt', 'ecc_1bit_err_uc2_1_cnt', 'ecc_2bit_err_uc0_0_cnt', 'ecc_2bit_err_uc0_1_cnt', 'ecc_2bit_err_uc1_0_cnt', 'ecc_2bit_err_uc1_1_cnt', 'ecc_2bit_err_uc2_0_cnt', 'ecc_2bit_err_uc2_1_cnt', 'out_pkt_uc_cnt', 'fe_uc_sop_eop_pack_cnt', 'fc_uc_0_1_trans_cnt', 'rate_cnt', 'calc_rate'], name, value)


                        class PeMcStats(Entity):
                            """
                            pe mc stats
                            
                            .. attribute:: in_pkt_mc_cnt
                            
                            	IN PKT MC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_full_line_mc_cnt
                            
                            	IN FULL LINE MC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_trunc_eop_mc_cnt
                            
                            	PKT TRUNC EOP MC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_sop_drop_mc_cnt
                            
                            	PKT SOP DROP MC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_ecc_err_drop_mc_cnt
                            
                            	PKT ECC ERR DROP MC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_ecc_err_trunc_cnt_mc_cnt
                            
                            	PKT ECC ERR TRUNC CNT MC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_1bit_err_mc0_cnt
                            
                            	ECC 1BIT ERR MC0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_1bit_err_mc1_cnt
                            
                            	ECC 1BIT ERR MC1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_1bit_err_mc2_cnt
                            
                            	ECC 1BIT ERR MC2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_2bit_err_mc0_cnt
                            
                            	ECC 2BIT ERR MC0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_2bit_err_mc1_cnt
                            
                            	ECC 2BIT ERR MC1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_2bit_err_mc2_cnt
                            
                            	ECC 2BIT ERR MC2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_pkt_mc_cnt
                            
                            	OUT PKT MC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fe_mc_sop_eop_pack_cnt
                            
                            	FE MC SOP EOP PACK CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fc_mc_0_1_trans_cnt
                            
                            	FC MC 0 1 TRANS CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rate_cnt
                            
                            	RATE CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: calc_rate
                            
                            	calc rate
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'asr9k-xbar-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeMcStats, self).__init__()

                                self.yang_name = "pe-mc-stats"
                                self.yang_parent_name = "sm15-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('in_pkt_mc_cnt', YLeaf(YType.uint64, 'in-pkt-mc-cnt')),
                                    ('in_full_line_mc_cnt', YLeaf(YType.uint64, 'in-full-line-mc-cnt')),
                                    ('pkt_trunc_eop_mc_cnt', YLeaf(YType.uint64, 'pkt-trunc-eop-mc-cnt')),
                                    ('pkt_sop_drop_mc_cnt', YLeaf(YType.uint64, 'pkt-sop-drop-mc-cnt')),
                                    ('pkt_ecc_err_drop_mc_cnt', YLeaf(YType.uint64, 'pkt-ecc-err-drop-mc-cnt')),
                                    ('pkt_ecc_err_trunc_cnt_mc_cnt', YLeaf(YType.uint64, 'pkt-ecc-err-trunc-cnt-mc-cnt')),
                                    ('ecc_1bit_err_mc0_cnt', YLeaf(YType.uint64, 'ecc-1bit-err-mc0-cnt')),
                                    ('ecc_1bit_err_mc1_cnt', YLeaf(YType.uint64, 'ecc-1bit-err-mc1-cnt')),
                                    ('ecc_1bit_err_mc2_cnt', YLeaf(YType.uint64, 'ecc-1bit-err-mc2-cnt')),
                                    ('ecc_2bit_err_mc0_cnt', YLeaf(YType.uint64, 'ecc-2bit-err-mc0-cnt')),
                                    ('ecc_2bit_err_mc1_cnt', YLeaf(YType.uint64, 'ecc-2bit-err-mc1-cnt')),
                                    ('ecc_2bit_err_mc2_cnt', YLeaf(YType.uint64, 'ecc-2bit-err-mc2-cnt')),
                                    ('out_pkt_mc_cnt', YLeaf(YType.uint64, 'out-pkt-mc-cnt')),
                                    ('fe_mc_sop_eop_pack_cnt', YLeaf(YType.uint64, 'fe-mc-sop-eop-pack-cnt')),
                                    ('fc_mc_0_1_trans_cnt', YLeaf(YType.uint64, 'fc-mc-0-1-trans-cnt')),
                                    ('rate_cnt', YLeaf(YType.uint64, 'rate-cnt')),
                                    ('calc_rate', YLeaf(YType.uint64, 'calc-rate')),
                                ])
                                self.in_pkt_mc_cnt = None
                                self.in_full_line_mc_cnt = None
                                self.pkt_trunc_eop_mc_cnt = None
                                self.pkt_sop_drop_mc_cnt = None
                                self.pkt_ecc_err_drop_mc_cnt = None
                                self.pkt_ecc_err_trunc_cnt_mc_cnt = None
                                self.ecc_1bit_err_mc0_cnt = None
                                self.ecc_1bit_err_mc1_cnt = None
                                self.ecc_1bit_err_mc2_cnt = None
                                self.ecc_2bit_err_mc0_cnt = None
                                self.ecc_2bit_err_mc1_cnt = None
                                self.ecc_2bit_err_mc2_cnt = None
                                self.out_pkt_mc_cnt = None
                                self.fe_mc_sop_eop_pack_cnt = None
                                self.fc_mc_0_1_trans_cnt = None
                                self.rate_cnt = None
                                self.calc_rate = None
                                self._segment_path = lambda: "pe-mc-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeMcStats, ['in_pkt_mc_cnt', 'in_full_line_mc_cnt', 'pkt_trunc_eop_mc_cnt', 'pkt_sop_drop_mc_cnt', 'pkt_ecc_err_drop_mc_cnt', 'pkt_ecc_err_trunc_cnt_mc_cnt', 'ecc_1bit_err_mc0_cnt', 'ecc_1bit_err_mc1_cnt', 'ecc_1bit_err_mc2_cnt', 'ecc_2bit_err_mc0_cnt', 'ecc_2bit_err_mc1_cnt', 'ecc_2bit_err_mc2_cnt', 'out_pkt_mc_cnt', 'fe_mc_sop_eop_pack_cnt', 'fc_mc_0_1_trans_cnt', 'rate_cnt', 'calc_rate'], name, value)


                        class PeCcStats(Entity):
                            """
                            pe cc stats
                            
                            .. attribute:: in_pkt_cnt
                            
                            	IN PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_path0_pkt_cnt
                            
                            	OUT PATH0 PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_path1_pkt_cnt
                            
                            	OUT PATH1 PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: xbar_ecc_drop_pkt_cnt
                            
                            	XBAR ECC DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: mem0_drop_pkt_cnt
                            
                            	MEM0 DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: mem1_drop_pkt_cnt
                            
                            	MEM1 DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: congn_pkt_cnt
                            
                            	CONGN PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: xbar_ecc_single_err_cnt
                            
                            	XBAR ECC SINGLE ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: xbar_ecc_double_err_cnt
                            
                            	XBAR ECC DOUBLE ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: mem0_ecc_single_err_cnt
                            
                            	MEM0 ECC SINGLE ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: mem0_ecc_double_err_cnt
                            
                            	MEM0 ECC DOUBLE ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: mem1_ecc_single_err_cnt
                            
                            	MEM1 ECC SINGLE ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: mem1_ecc_double_err_cnt
                            
                            	MEM1 ECC DOUBLE ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fc_cc_0_1_trans_cnt
                            
                            	FC CC 0 1 TRANS CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rate_cnt
                            
                            	RATE CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: calc_rate
                            
                            	calc rate
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'asr9k-xbar-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeCcStats, self).__init__()

                                self.yang_name = "pe-cc-stats"
                                self.yang_parent_name = "sm15-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('in_pkt_cnt', YLeaf(YType.uint64, 'in-pkt-cnt')),
                                    ('out_path0_pkt_cnt', YLeaf(YType.uint64, 'out-path0-pkt-cnt')),
                                    ('out_path1_pkt_cnt', YLeaf(YType.uint64, 'out-path1-pkt-cnt')),
                                    ('xbar_ecc_drop_pkt_cnt', YLeaf(YType.uint64, 'xbar-ecc-drop-pkt-cnt')),
                                    ('mem0_drop_pkt_cnt', YLeaf(YType.uint64, 'mem0-drop-pkt-cnt')),
                                    ('mem1_drop_pkt_cnt', YLeaf(YType.uint64, 'mem1-drop-pkt-cnt')),
                                    ('congn_pkt_cnt', YLeaf(YType.uint64, 'congn-pkt-cnt')),
                                    ('xbar_ecc_single_err_cnt', YLeaf(YType.uint64, 'xbar-ecc-single-err-cnt')),
                                    ('xbar_ecc_double_err_cnt', YLeaf(YType.uint64, 'xbar-ecc-double-err-cnt')),
                                    ('mem0_ecc_single_err_cnt', YLeaf(YType.uint64, 'mem0-ecc-single-err-cnt')),
                                    ('mem0_ecc_double_err_cnt', YLeaf(YType.uint64, 'mem0-ecc-double-err-cnt')),
                                    ('mem1_ecc_single_err_cnt', YLeaf(YType.uint64, 'mem1-ecc-single-err-cnt')),
                                    ('mem1_ecc_double_err_cnt', YLeaf(YType.uint64, 'mem1-ecc-double-err-cnt')),
                                    ('fc_cc_0_1_trans_cnt', YLeaf(YType.uint64, 'fc-cc-0-1-trans-cnt')),
                                    ('rate_cnt', YLeaf(YType.uint64, 'rate-cnt')),
                                    ('calc_rate', YLeaf(YType.uint64, 'calc-rate')),
                                ])
                                self.in_pkt_cnt = None
                                self.out_path0_pkt_cnt = None
                                self.out_path1_pkt_cnt = None
                                self.xbar_ecc_drop_pkt_cnt = None
                                self.mem0_drop_pkt_cnt = None
                                self.mem1_drop_pkt_cnt = None
                                self.congn_pkt_cnt = None
                                self.xbar_ecc_single_err_cnt = None
                                self.xbar_ecc_double_err_cnt = None
                                self.mem0_ecc_single_err_cnt = None
                                self.mem0_ecc_double_err_cnt = None
                                self.mem1_ecc_single_err_cnt = None
                                self.mem1_ecc_double_err_cnt = None
                                self.fc_cc_0_1_trans_cnt = None
                                self.rate_cnt = None
                                self.calc_rate = None
                                self._segment_path = lambda: "pe-cc-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeCcStats, ['in_pkt_cnt', 'out_path0_pkt_cnt', 'out_path1_pkt_cnt', 'xbar_ecc_drop_pkt_cnt', 'mem0_drop_pkt_cnt', 'mem1_drop_pkt_cnt', 'congn_pkt_cnt', 'xbar_ecc_single_err_cnt', 'xbar_ecc_double_err_cnt', 'mem0_ecc_single_err_cnt', 'mem0_ecc_double_err_cnt', 'mem1_ecc_single_err_cnt', 'mem1_ecc_double_err_cnt', 'fc_cc_0_1_trans_cnt', 'rate_cnt', 'calc_rate'], name, value)

    def clone_ptr(self):
        self._top_entity = CrossBarStats()
        return self._top_entity

