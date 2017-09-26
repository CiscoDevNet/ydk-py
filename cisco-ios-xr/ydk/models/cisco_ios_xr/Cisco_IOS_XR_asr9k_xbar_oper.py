""" Cisco_IOS_XR_asr9k_xbar_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-xbar package operational data.

This module contains definitions
for the following management objects\:
  cross\-bar\-stats\: Crossbar stats operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CrossBarStats(Entity):
    """
    Crossbar stats operational data
    
    .. attribute:: nodes
    
    	Table of Nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes>`
    
    

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
        self._child_container_classes = {"nodes" : ("nodes", CrossBarStats.Nodes)}
        self._child_list_classes = {}

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
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-xbar-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(CrossBarStats.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "cross-bar-stats"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", CrossBarStats.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-xbar-oper:cross-bar-stats/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CrossBarStats.Nodes, [], name, value)


        class Node(Entity):
            """
            Information about a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: cross_bar_table
            
            	Table of stats information
            	**type**\:   :py:class:`CrossBarTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable>`
            
            

            """

            _prefix = 'asr9k-xbar-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(CrossBarStats.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"cross-bar-table" : ("cross_bar_table", CrossBarStats.Nodes.Node.CrossBarTable)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.cross_bar_table = CrossBarStats.Nodes.Node.CrossBarTable()
                self.cross_bar_table.parent = self
                self._children_name_map["cross_bar_table"] = "cross-bar-table"
                self._children_yang_names.add("cross-bar-table")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-xbar-oper:cross-bar-stats/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CrossBarStats.Nodes.Node, ['node_name'], name, value)


            class CrossBarTable(Entity):
                """
                Table of stats information
                
                .. attribute:: pkt_stats
                
                	Table of packet stats
                	**type**\:   :py:class:`PktStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.PktStats>`
                
                .. attribute:: sm15_stats
                
                	Table of packet stats for SM15
                	**type**\:   :py:class:`Sm15Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats>`
                
                

                """

                _prefix = 'asr9k-xbar-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(CrossBarStats.Nodes.Node.CrossBarTable, self).__init__()

                    self.yang_name = "cross-bar-table"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"pkt-stats" : ("pkt_stats", CrossBarStats.Nodes.Node.CrossBarTable.PktStats), "sm15-stats" : ("sm15_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats)}
                    self._child_list_classes = {}

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
                    	**type**\: list of    :py:class:`PktStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.PktStats.PktStat>`
                    
                    

                    """

                    _prefix = 'asr9k-xbar-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CrossBarStats.Nodes.Node.CrossBarTable.PktStats, self).__init__()

                        self.yang_name = "pkt-stats"
                        self.yang_parent_name = "cross-bar-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"pkt-stat" : ("pkt_stat", CrossBarStats.Nodes.Node.CrossBarTable.PktStats.PktStat)}

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
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: diagnostic_packet_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: diagnostic_packet_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: egress_channel_utilization_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: egress_channel_utilization_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: egress_packet_count_since_last_read_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: egress_packet_count_since_last_read_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: fpoedb_correctable_ecc_error_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: fpoedb_correctable_ecc_error_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: fpoedb_uncorrectable_ecc_error_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: fpoedb_uncorrectable_ecc_error_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: header_crc_error_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: header_crc_error_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: holdrop_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: holdrop_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ingress_channel_utilization_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ingress_channel_utilization_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ingress_packet_count_since_last_read_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ingress_packet_count_since_last_read_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: input_buffer_back_pressure_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: input_buffer_back_pressure_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: input_buffer_correctable_ecc_error_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: input_buffer_correctable_ecc_error_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: input_buffer_queued_packet_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: input_buffer_queued_packet_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: input_buffer_uncorrectable_ecc_error_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: input_buffer_uncorrectable_ecc_error_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: internal_error_count
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: null_fpoe_drop_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: null_fpoe_drop_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: output_buffer_back_pressure_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: output_buffer_back_pressure_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: output_buffer_correctable_ecc_error_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: output_buffer_correctable_ecc_error_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: output_buffer_queued_packet_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: output_buffer_queued_packet_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: output_buffer_uncorrectable_ecc_error_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: output_buffer_uncorrectable_ecc_error_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: packet_crc_error_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: packet_crc_error_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: port
                        
                        	Port
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: short_input_header_error_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: short_input_header_error_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: short_packet_error_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: short_packet_error_count_low
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: xbar_timeout_drop_count_high
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: xbar_timeout_drop_count_low
                        
                        	
                        	**type**\:  int
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.asic_id = YLeaf(YType.str, "asic-id")

                            self.diagnostic_packet_count_high = YLeaf(YType.uint64, "diagnostic-packet-count-high")

                            self.diagnostic_packet_count_low = YLeaf(YType.uint64, "diagnostic-packet-count-low")

                            self.egress_channel_utilization_count_high = YLeaf(YType.uint64, "egress-channel-utilization-count-high")

                            self.egress_channel_utilization_count_low = YLeaf(YType.uint64, "egress-channel-utilization-count-low")

                            self.egress_packet_count_since_last_read_high = YLeaf(YType.uint64, "egress-packet-count-since-last-read-high")

                            self.egress_packet_count_since_last_read_low = YLeaf(YType.uint64, "egress-packet-count-since-last-read-low")

                            self.fpoedb_correctable_ecc_error_count_high = YLeaf(YType.uint64, "fpoedb-correctable-ecc-error-count-high")

                            self.fpoedb_correctable_ecc_error_count_low = YLeaf(YType.uint64, "fpoedb-correctable-ecc-error-count-low")

                            self.fpoedb_uncorrectable_ecc_error_count_high = YLeaf(YType.uint64, "fpoedb-uncorrectable-ecc-error-count-high")

                            self.fpoedb_uncorrectable_ecc_error_count_low = YLeaf(YType.uint64, "fpoedb-uncorrectable-ecc-error-count-low")

                            self.header_crc_error_count_high = YLeaf(YType.uint64, "header-crc-error-count-high")

                            self.header_crc_error_count_low = YLeaf(YType.uint64, "header-crc-error-count-low")

                            self.holdrop_count_high = YLeaf(YType.uint64, "holdrop-count-high")

                            self.holdrop_count_low = YLeaf(YType.uint64, "holdrop-count-low")

                            self.ingress_channel_utilization_count_high = YLeaf(YType.uint64, "ingress-channel-utilization-count-high")

                            self.ingress_channel_utilization_count_low = YLeaf(YType.uint64, "ingress-channel-utilization-count-low")

                            self.ingress_packet_count_since_last_read_high = YLeaf(YType.uint64, "ingress-packet-count-since-last-read-high")

                            self.ingress_packet_count_since_last_read_low = YLeaf(YType.uint64, "ingress-packet-count-since-last-read-low")

                            self.input_buffer_back_pressure_count_high = YLeaf(YType.uint64, "input-buffer-back-pressure-count-high")

                            self.input_buffer_back_pressure_count_low = YLeaf(YType.uint64, "input-buffer-back-pressure-count-low")

                            self.input_buffer_correctable_ecc_error_count_high = YLeaf(YType.uint64, "input-buffer-correctable-ecc-error-count-high")

                            self.input_buffer_correctable_ecc_error_count_low = YLeaf(YType.uint64, "input-buffer-correctable-ecc-error-count-low")

                            self.input_buffer_queued_packet_count_high = YLeaf(YType.uint64, "input-buffer-queued-packet-count-high")

                            self.input_buffer_queued_packet_count_low = YLeaf(YType.uint64, "input-buffer-queued-packet-count-low")

                            self.input_buffer_uncorrectable_ecc_error_count_high = YLeaf(YType.uint64, "input-buffer-uncorrectable-ecc-error-count-high")

                            self.input_buffer_uncorrectable_ecc_error_count_low = YLeaf(YType.uint64, "input-buffer-uncorrectable-ecc-error-count-low")

                            self.internal_error_count = YLeaf(YType.uint64, "internal-error-count")

                            self.null_fpoe_drop_count_high = YLeaf(YType.uint64, "null-fpoe-drop-count-high")

                            self.null_fpoe_drop_count_low = YLeaf(YType.uint64, "null-fpoe-drop-count-low")

                            self.output_buffer_back_pressure_count_high = YLeaf(YType.uint64, "output-buffer-back-pressure-count-high")

                            self.output_buffer_back_pressure_count_low = YLeaf(YType.uint64, "output-buffer-back-pressure-count-low")

                            self.output_buffer_correctable_ecc_error_count_high = YLeaf(YType.uint64, "output-buffer-correctable-ecc-error-count-high")

                            self.output_buffer_correctable_ecc_error_count_low = YLeaf(YType.uint64, "output-buffer-correctable-ecc-error-count-low")

                            self.output_buffer_queued_packet_count_high = YLeaf(YType.uint64, "output-buffer-queued-packet-count-high")

                            self.output_buffer_queued_packet_count_low = YLeaf(YType.uint64, "output-buffer-queued-packet-count-low")

                            self.output_buffer_uncorrectable_ecc_error_count_high = YLeaf(YType.uint64, "output-buffer-uncorrectable-ecc-error-count-high")

                            self.output_buffer_uncorrectable_ecc_error_count_low = YLeaf(YType.uint64, "output-buffer-uncorrectable-ecc-error-count-low")

                            self.packet_crc_error_count_high = YLeaf(YType.uint64, "packet-crc-error-count-high")

                            self.packet_crc_error_count_low = YLeaf(YType.uint64, "packet-crc-error-count-low")

                            self.port = YLeaf(YType.str, "port")

                            self.short_input_header_error_count_high = YLeaf(YType.uint64, "short-input-header-error-count-high")

                            self.short_input_header_error_count_low = YLeaf(YType.uint64, "short-input-header-error-count-low")

                            self.short_packet_error_count_high = YLeaf(YType.uint64, "short-packet-error-count-high")

                            self.short_packet_error_count_low = YLeaf(YType.uint64, "short-packet-error-count-low")

                            self.xbar_timeout_drop_count_high = YLeaf(YType.uint64, "xbar-timeout-drop-count-high")

                            self.xbar_timeout_drop_count_low = YLeaf(YType.uint64, "xbar-timeout-drop-count-low")
                            self._segment_path = lambda: "pkt-stat"

                        def __setattr__(self, name, value):
                            self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.PktStats.PktStat, ['asic_id', 'diagnostic_packet_count_high', 'diagnostic_packet_count_low', 'egress_channel_utilization_count_high', 'egress_channel_utilization_count_low', 'egress_packet_count_since_last_read_high', 'egress_packet_count_since_last_read_low', 'fpoedb_correctable_ecc_error_count_high', 'fpoedb_correctable_ecc_error_count_low', 'fpoedb_uncorrectable_ecc_error_count_high', 'fpoedb_uncorrectable_ecc_error_count_low', 'header_crc_error_count_high', 'header_crc_error_count_low', 'holdrop_count_high', 'holdrop_count_low', 'ingress_channel_utilization_count_high', 'ingress_channel_utilization_count_low', 'ingress_packet_count_since_last_read_high', 'ingress_packet_count_since_last_read_low', 'input_buffer_back_pressure_count_high', 'input_buffer_back_pressure_count_low', 'input_buffer_correctable_ecc_error_count_high', 'input_buffer_correctable_ecc_error_count_low', 'input_buffer_queued_packet_count_high', 'input_buffer_queued_packet_count_low', 'input_buffer_uncorrectable_ecc_error_count_high', 'input_buffer_uncorrectable_ecc_error_count_low', 'internal_error_count', 'null_fpoe_drop_count_high', 'null_fpoe_drop_count_low', 'output_buffer_back_pressure_count_high', 'output_buffer_back_pressure_count_low', 'output_buffer_correctable_ecc_error_count_high', 'output_buffer_correctable_ecc_error_count_low', 'output_buffer_queued_packet_count_high', 'output_buffer_queued_packet_count_low', 'output_buffer_uncorrectable_ecc_error_count_high', 'output_buffer_uncorrectable_ecc_error_count_low', 'packet_crc_error_count_high', 'packet_crc_error_count_low', 'port', 'short_input_header_error_count_high', 'short_input_header_error_count_low', 'short_packet_error_count_high', 'short_packet_error_count_low', 'xbar_timeout_drop_count_high', 'xbar_timeout_drop_count_low'], name, value)


                class Sm15Stats(Entity):
                    """
                    Table of packet stats for SM15
                    
                    .. attribute:: sm15_stat
                    
                    	Stats information for a particular asic type and port
                    	**type**\: list of    :py:class:`Sm15Stat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat>`
                    
                    

                    """

                    _prefix = 'asr9k-xbar-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats, self).__init__()

                        self.yang_name = "sm15-stats"
                        self.yang_parent_name = "cross-bar-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"sm15-stat" : ("sm15_stat", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat)}

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
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: ca_stats
                        
                        	ca stats
                        	**type**\:   :py:class:`CaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.CaStats>`
                        
                        .. attribute:: internal_err_cnt
                        
                        	internal err cnt
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ma_stats
                        
                        	ma stats
                        	**type**\:   :py:class:`MaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.MaStats>`
                        
                        .. attribute:: pe_cc_stats
                        
                        	pe cc stats
                        	**type**\:   :py:class:`PeCcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeCcStats>`
                        
                        .. attribute:: pe_mc_stats
                        
                        	pe mc stats
                        	**type**\:   :py:class:`PeMcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeMcStats>`
                        
                        .. attribute:: pe_stats
                        
                        	pe stats
                        	**type**\:   :py:class:`PeStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeStats>`
                        
                        .. attribute:: pe_uc_stats
                        
                        	pe uc stats
                        	**type**\:   :py:class:`PeUcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeUcStats>`
                        
                        .. attribute:: pi_cc_stats
                        
                        	pi cc stats
                        	**type**\:   :py:class:`PiCcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiCcStats>`
                        
                        .. attribute:: pi_mc_stats
                        
                        	pi mc stats
                        	**type**\:   :py:class:`PiMcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiMcStats>`
                        
                        .. attribute:: pi_stats
                        
                        	pi stats
                        	**type**\:   :py:class:`PiStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiStats>`
                        
                        .. attribute:: pi_uc_stats
                        
                        	pi uc stats
                        	**type**\:   :py:class:`PiUcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiUcStats>`
                        
                        .. attribute:: port
                        
                        	Port
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: ua0_stats
                        
                        	ua0 stats
                        	**type**\:   :py:class:`Ua0Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua0Stats>`
                        
                        .. attribute:: ua1_stats
                        
                        	ua1 stats
                        	**type**\:   :py:class:`Ua1Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua1Stats>`
                        
                        .. attribute:: ua2_stats
                        
                        	ua2 stats
                        	**type**\:   :py:class:`Ua2Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua2Stats>`
                        
                        

                        """

                        _prefix = 'asr9k-xbar-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat, self).__init__()

                            self.yang_name = "sm15-stat"
                            self.yang_parent_name = "sm15-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"ca-stats" : ("ca_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.CaStats), "ma-stats" : ("ma_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.MaStats), "pe-cc-stats" : ("pe_cc_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeCcStats), "pe-mc-stats" : ("pe_mc_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeMcStats), "pe-stats" : ("pe_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeStats), "pe-uc-stats" : ("pe_uc_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeUcStats), "pi-cc-stats" : ("pi_cc_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiCcStats), "pi-mc-stats" : ("pi_mc_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiMcStats), "pi-stats" : ("pi_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiStats), "pi-uc-stats" : ("pi_uc_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiUcStats), "ua0-stats" : ("ua0_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua0Stats), "ua1-stats" : ("ua1_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua1Stats), "ua2-stats" : ("ua2_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua2Stats)}
                            self._child_list_classes = {}

                            self.asic_id = YLeaf(YType.str, "asic-id")

                            self.internal_err_cnt = YLeaf(YType.uint64, "internal-err-cnt")

                            self.port = YLeaf(YType.str, "port")

                            self.ca_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.CaStats()
                            self.ca_stats.parent = self
                            self._children_name_map["ca_stats"] = "ca-stats"
                            self._children_yang_names.add("ca-stats")

                            self.ma_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.MaStats()
                            self.ma_stats.parent = self
                            self._children_name_map["ma_stats"] = "ma-stats"
                            self._children_yang_names.add("ma-stats")

                            self.pe_cc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeCcStats()
                            self.pe_cc_stats.parent = self
                            self._children_name_map["pe_cc_stats"] = "pe-cc-stats"
                            self._children_yang_names.add("pe-cc-stats")

                            self.pe_mc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeMcStats()
                            self.pe_mc_stats.parent = self
                            self._children_name_map["pe_mc_stats"] = "pe-mc-stats"
                            self._children_yang_names.add("pe-mc-stats")

                            self.pe_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeStats()
                            self.pe_stats.parent = self
                            self._children_name_map["pe_stats"] = "pe-stats"
                            self._children_yang_names.add("pe-stats")

                            self.pe_uc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeUcStats()
                            self.pe_uc_stats.parent = self
                            self._children_name_map["pe_uc_stats"] = "pe-uc-stats"
                            self._children_yang_names.add("pe-uc-stats")

                            self.pi_cc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiCcStats()
                            self.pi_cc_stats.parent = self
                            self._children_name_map["pi_cc_stats"] = "pi-cc-stats"
                            self._children_yang_names.add("pi-cc-stats")

                            self.pi_mc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiMcStats()
                            self.pi_mc_stats.parent = self
                            self._children_name_map["pi_mc_stats"] = "pi-mc-stats"
                            self._children_yang_names.add("pi-mc-stats")

                            self.pi_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiStats()
                            self.pi_stats.parent = self
                            self._children_name_map["pi_stats"] = "pi-stats"
                            self._children_yang_names.add("pi-stats")

                            self.pi_uc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiUcStats()
                            self.pi_uc_stats.parent = self
                            self._children_name_map["pi_uc_stats"] = "pi-uc-stats"
                            self._children_yang_names.add("pi-uc-stats")

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
                            self._segment_path = lambda: "sm15-stat"

                        def __setattr__(self, name, value):
                            self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat, ['asic_id', 'internal_err_cnt', 'port'], name, value)


                        class CaStats(Entity):
                            """
                            ca stats
                            
                            .. attribute:: dest_drop_pkt_cnt
                            
                            	DEST DROP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dest_src_pkt_cnt
                            
                            	DEST SRC PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rcv_pkt_cnt
                            
                            	RCV PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_drop_pkt_cnt
                            
                            	RX DROP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: src_dest_pkt_cnt
                            
                            	SRC DEST PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tx_pkt_cnt
                            
                            	TX PKT CNT
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.dest_drop_pkt_cnt = YLeaf(YType.uint64, "dest-drop-pkt-cnt")

                                self.dest_src_pkt_cnt = YLeaf(YType.uint64, "dest-src-pkt-cnt")

                                self.rcv_pkt_cnt = YLeaf(YType.uint64, "rcv-pkt-cnt")

                                self.rx_drop_pkt_cnt = YLeaf(YType.uint64, "rx-drop-pkt-cnt")

                                self.src_dest_pkt_cnt = YLeaf(YType.uint64, "src-dest-pkt-cnt")

                                self.tx_pkt_cnt = YLeaf(YType.uint64, "tx-pkt-cnt")
                                self._segment_path = lambda: "ca-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.CaStats, ['dest_drop_pkt_cnt', 'dest_src_pkt_cnt', 'rcv_pkt_cnt', 'rx_drop_pkt_cnt', 'src_dest_pkt_cnt', 'tx_pkt_cnt'], name, value)


                        class MaStats(Entity):
                            """
                            ma stats
                            
                            .. attribute:: dest_drop_pkt_cnt
                            
                            	DEST DROP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dest_src_pkt_cnt
                            
                            	DEST SRC PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rcv_pkt_cnt
                            
                            	RCV PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_drop_pkt_cnt
                            
                            	RX DROP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_fabric_to_cnt
                            
                            	RX FABRIC TO CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_hol_to_cnt
                            
                            	RX HOL TO CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_re_transmit_cnt
                            
                            	RX RETRANSMIT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: src_dest_pkt_cnt
                            
                            	SRC DEST PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tx_pkt_cnt
                            
                            	TX PKT CNT
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.dest_drop_pkt_cnt = YLeaf(YType.uint64, "dest-drop-pkt-cnt")

                                self.dest_src_pkt_cnt = YLeaf(YType.uint64, "dest-src-pkt-cnt")

                                self.rcv_pkt_cnt = YLeaf(YType.uint64, "rcv-pkt-cnt")

                                self.rx_drop_pkt_cnt = YLeaf(YType.uint64, "rx-drop-pkt-cnt")

                                self.rx_fabric_to_cnt = YLeaf(YType.uint64, "rx-fabric-to-cnt")

                                self.rx_hol_to_cnt = YLeaf(YType.uint64, "rx-hol-to-cnt")

                                self.rx_re_transmit_cnt = YLeaf(YType.uint64, "rx-re-transmit-cnt")

                                self.src_dest_pkt_cnt = YLeaf(YType.uint64, "src-dest-pkt-cnt")

                                self.tx_pkt_cnt = YLeaf(YType.uint64, "tx-pkt-cnt")
                                self._segment_path = lambda: "ma-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.MaStats, ['dest_drop_pkt_cnt', 'dest_src_pkt_cnt', 'rcv_pkt_cnt', 'rx_drop_pkt_cnt', 'rx_fabric_to_cnt', 'rx_hol_to_cnt', 'rx_re_transmit_cnt', 'src_dest_pkt_cnt', 'tx_pkt_cnt'], name, value)


                        class PeCcStats(Entity):
                            """
                            pe cc stats
                            
                            .. attribute:: calc_rate
                            
                            	calc rate
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: congn_pkt_cnt
                            
                            	CONGN PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fc_cc_0_1_trans_cnt
                            
                            	FC CC 0 1 TRANS CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_pkt_cnt
                            
                            	IN PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: mem0_drop_pkt_cnt
                            
                            	MEM0 DROP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: mem0_ecc_double_err_cnt
                            
                            	MEM0 ECC DOUBLE ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: mem0_ecc_single_err_cnt
                            
                            	MEM0 ECC SINGLE ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: mem1_drop_pkt_cnt
                            
                            	MEM1 DROP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: mem1_ecc_double_err_cnt
                            
                            	MEM1 ECC DOUBLE ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: mem1_ecc_single_err_cnt
                            
                            	MEM1 ECC SINGLE ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_path0_pkt_cnt
                            
                            	OUT PATH0 PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_path1_pkt_cnt
                            
                            	OUT PATH1 PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rate_cnt
                            
                            	RATE CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: xbar_ecc_double_err_cnt
                            
                            	XBAR ECC DOUBLE ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: xbar_ecc_drop_pkt_cnt
                            
                            	XBAR ECC DROP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: xbar_ecc_single_err_cnt
                            
                            	XBAR ECC SINGLE ERR CNT
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.calc_rate = YLeaf(YType.uint64, "calc-rate")

                                self.congn_pkt_cnt = YLeaf(YType.uint64, "congn-pkt-cnt")

                                self.fc_cc_0_1_trans_cnt = YLeaf(YType.uint64, "fc-cc-0-1-trans-cnt")

                                self.in_pkt_cnt = YLeaf(YType.uint64, "in-pkt-cnt")

                                self.mem0_drop_pkt_cnt = YLeaf(YType.uint64, "mem0-drop-pkt-cnt")

                                self.mem0_ecc_double_err_cnt = YLeaf(YType.uint64, "mem0-ecc-double-err-cnt")

                                self.mem0_ecc_single_err_cnt = YLeaf(YType.uint64, "mem0-ecc-single-err-cnt")

                                self.mem1_drop_pkt_cnt = YLeaf(YType.uint64, "mem1-drop-pkt-cnt")

                                self.mem1_ecc_double_err_cnt = YLeaf(YType.uint64, "mem1-ecc-double-err-cnt")

                                self.mem1_ecc_single_err_cnt = YLeaf(YType.uint64, "mem1-ecc-single-err-cnt")

                                self.out_path0_pkt_cnt = YLeaf(YType.uint64, "out-path0-pkt-cnt")

                                self.out_path1_pkt_cnt = YLeaf(YType.uint64, "out-path1-pkt-cnt")

                                self.rate_cnt = YLeaf(YType.uint64, "rate-cnt")

                                self.xbar_ecc_double_err_cnt = YLeaf(YType.uint64, "xbar-ecc-double-err-cnt")

                                self.xbar_ecc_drop_pkt_cnt = YLeaf(YType.uint64, "xbar-ecc-drop-pkt-cnt")

                                self.xbar_ecc_single_err_cnt = YLeaf(YType.uint64, "xbar-ecc-single-err-cnt")
                                self._segment_path = lambda: "pe-cc-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeCcStats, ['calc_rate', 'congn_pkt_cnt', 'fc_cc_0_1_trans_cnt', 'in_pkt_cnt', 'mem0_drop_pkt_cnt', 'mem0_ecc_double_err_cnt', 'mem0_ecc_single_err_cnt', 'mem1_drop_pkt_cnt', 'mem1_ecc_double_err_cnt', 'mem1_ecc_single_err_cnt', 'out_path0_pkt_cnt', 'out_path1_pkt_cnt', 'rate_cnt', 'xbar_ecc_double_err_cnt', 'xbar_ecc_drop_pkt_cnt', 'xbar_ecc_single_err_cnt'], name, value)


                        class PeMcStats(Entity):
                            """
                            pe mc stats
                            
                            .. attribute:: calc_rate
                            
                            	calc rate
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_1bit_err_mc0_cnt
                            
                            	ECC 1BIT ERR MC0 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_1bit_err_mc1_cnt
                            
                            	ECC 1BIT ERR MC1 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_1bit_err_mc2_cnt
                            
                            	ECC 1BIT ERR MC2 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_2bit_err_mc0_cnt
                            
                            	ECC 2BIT ERR MC0 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_2bit_err_mc1_cnt
                            
                            	ECC 2BIT ERR MC1 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_2bit_err_mc2_cnt
                            
                            	ECC 2BIT ERR MC2 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fc_mc_0_1_trans_cnt
                            
                            	FC MC 0 1 TRANS CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fe_mc_sop_eop_pack_cnt
                            
                            	FE MC SOP EOP PACK CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_full_line_mc_cnt
                            
                            	IN FULL LINE MC CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_pkt_mc_cnt
                            
                            	IN PKT MC CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_pkt_mc_cnt
                            
                            	OUT PKT MC CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_ecc_err_drop_mc_cnt
                            
                            	PKT ECC ERR DROP MC CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_ecc_err_trunc_cnt_mc_cnt
                            
                            	PKT ECC ERR TRUNC CNT MC CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_sop_drop_mc_cnt
                            
                            	PKT SOP DROP MC CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_trunc_eop_mc_cnt
                            
                            	PKT TRUNC EOP MC CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rate_cnt
                            
                            	RATE CNT
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.calc_rate = YLeaf(YType.uint64, "calc-rate")

                                self.ecc_1bit_err_mc0_cnt = YLeaf(YType.uint64, "ecc-1bit-err-mc0-cnt")

                                self.ecc_1bit_err_mc1_cnt = YLeaf(YType.uint64, "ecc-1bit-err-mc1-cnt")

                                self.ecc_1bit_err_mc2_cnt = YLeaf(YType.uint64, "ecc-1bit-err-mc2-cnt")

                                self.ecc_2bit_err_mc0_cnt = YLeaf(YType.uint64, "ecc-2bit-err-mc0-cnt")

                                self.ecc_2bit_err_mc1_cnt = YLeaf(YType.uint64, "ecc-2bit-err-mc1-cnt")

                                self.ecc_2bit_err_mc2_cnt = YLeaf(YType.uint64, "ecc-2bit-err-mc2-cnt")

                                self.fc_mc_0_1_trans_cnt = YLeaf(YType.uint64, "fc-mc-0-1-trans-cnt")

                                self.fe_mc_sop_eop_pack_cnt = YLeaf(YType.uint64, "fe-mc-sop-eop-pack-cnt")

                                self.in_full_line_mc_cnt = YLeaf(YType.uint64, "in-full-line-mc-cnt")

                                self.in_pkt_mc_cnt = YLeaf(YType.uint64, "in-pkt-mc-cnt")

                                self.out_pkt_mc_cnt = YLeaf(YType.uint64, "out-pkt-mc-cnt")

                                self.pkt_ecc_err_drop_mc_cnt = YLeaf(YType.uint64, "pkt-ecc-err-drop-mc-cnt")

                                self.pkt_ecc_err_trunc_cnt_mc_cnt = YLeaf(YType.uint64, "pkt-ecc-err-trunc-cnt-mc-cnt")

                                self.pkt_sop_drop_mc_cnt = YLeaf(YType.uint64, "pkt-sop-drop-mc-cnt")

                                self.pkt_trunc_eop_mc_cnt = YLeaf(YType.uint64, "pkt-trunc-eop-mc-cnt")

                                self.rate_cnt = YLeaf(YType.uint64, "rate-cnt")
                                self._segment_path = lambda: "pe-mc-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeMcStats, ['calc_rate', 'ecc_1bit_err_mc0_cnt', 'ecc_1bit_err_mc1_cnt', 'ecc_1bit_err_mc2_cnt', 'ecc_2bit_err_mc0_cnt', 'ecc_2bit_err_mc1_cnt', 'ecc_2bit_err_mc2_cnt', 'fc_mc_0_1_trans_cnt', 'fe_mc_sop_eop_pack_cnt', 'in_full_line_mc_cnt', 'in_pkt_mc_cnt', 'out_pkt_mc_cnt', 'pkt_ecc_err_drop_mc_cnt', 'pkt_ecc_err_trunc_cnt_mc_cnt', 'pkt_sop_drop_mc_cnt', 'pkt_trunc_eop_mc_cnt', 'rate_cnt'], name, value)


                        class PeStats(Entity):
                            """
                            pe stats
                            
                            .. attribute:: mc2uc_preempt_cnt
                            
                            	MC2UC PREEMPT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: total_calc_rate
                            
                            	total calc rate
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: total_rate1_cnt
                            
                            	TOTAL RATE1 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: total_rate2_cnt
                            
                            	TOTAL RATE2 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: total_rate3_cnt
                            
                            	TOTAL RATE3 CNT
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.mc2uc_preempt_cnt = YLeaf(YType.uint64, "mc2uc-preempt-cnt")

                                self.total_calc_rate = YLeaf(YType.uint64, "total-calc-rate")

                                self.total_rate1_cnt = YLeaf(YType.uint64, "total-rate1-cnt")

                                self.total_rate2_cnt = YLeaf(YType.uint64, "total-rate2-cnt")

                                self.total_rate3_cnt = YLeaf(YType.uint64, "total-rate3-cnt")
                                self._segment_path = lambda: "pe-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeStats, ['mc2uc_preempt_cnt', 'total_calc_rate', 'total_rate1_cnt', 'total_rate2_cnt', 'total_rate3_cnt'], name, value)


                        class PeUcStats(Entity):
                            """
                            pe uc stats
                            
                            .. attribute:: calc_rate
                            
                            	calc rate
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_1bit_err_uc0_0_cnt
                            
                            	ECC 1BIT ERR UC0 0 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_1bit_err_uc0_1_cnt
                            
                            	ECC 1BIT ERR UC0 1 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_1bit_err_uc1_0_cnt
                            
                            	ECC 1BIT ERR UC1 0 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_1bit_err_uc1_1_cnt
                            
                            	ECC 1BIT ERR UC1 1 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_1bit_err_uc2_0_cnt
                            
                            	ECC 1BIT ERR UC2 0 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_1bit_err_uc2_1_cnt
                            
                            	ECC 1BIT ERR UC2 1 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_2bit_err_uc0_0_cnt
                            
                            	ECC 2BIT ERR UC0 0 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_2bit_err_uc0_1_cnt
                            
                            	ECC 2BIT ERR UC0 1 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_2bit_err_uc1_0_cnt
                            
                            	ECC 2BIT ERR UC1 0 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_2bit_err_uc1_1_cnt
                            
                            	ECC 2BIT ERR UC1 1 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_2bit_err_uc2_0_cnt
                            
                            	ECC 2BIT ERR UC2 0 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: ecc_2bit_err_uc2_1_cnt
                            
                            	ECC 2BIT ERR UC2 1 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fc_uc_0_1_trans_cnt
                            
                            	FC UC 0 1 TRANS CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fe_uc_sop_eop_pack_cnt
                            
                            	FE UC SOP EOP PACK CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_full_line_uc0_cnt
                            
                            	IN FULL LINE UC0 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_full_line_uc1_cnt
                            
                            	IN FULL LINE UC1 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_full_line_uc2_cnt
                            
                            	IN FULL LINE UC2 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_pkt_uc0_cnt
                            
                            	IN PKT UC0 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_pkt_uc1_cnt
                            
                            	IN PKT UC1 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_pkt_uc2_cnt
                            
                            	IN PKT UC2 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_pkt_uc_cnt
                            
                            	OUT PKT UC CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_ecc_err_drop_uc_cnt
                            
                            	PKT ECC ERR DROP UC CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_ecc_trunc_cnt_uc_cnt
                            
                            	PKT ECC TRUNC CNT UC CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_sop_drop_uc0_cnt
                            
                            	PKT SOP DROP UC0 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_sop_drop_uc1_cnt
                            
                            	PKT SOP DROP UC1 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_sop_drop_uc2_cnt
                            
                            	PKT SOP DROP UC2 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_trunc_eop_uc0_cnt
                            
                            	PKT TRUNC EOP UC0 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_trunc_eop_uc1_cnt
                            
                            	PKT TRUNC EOP UC1 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_trunc_eop_uc2_cnt
                            
                            	PKT TRUNC EOP UC2 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rate_cnt
                            
                            	RATE CNT
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.calc_rate = YLeaf(YType.uint64, "calc-rate")

                                self.ecc_1bit_err_uc0_0_cnt = YLeaf(YType.uint64, "ecc-1bit-err-uc0-0-cnt")

                                self.ecc_1bit_err_uc0_1_cnt = YLeaf(YType.uint64, "ecc-1bit-err-uc0-1-cnt")

                                self.ecc_1bit_err_uc1_0_cnt = YLeaf(YType.uint64, "ecc-1bit-err-uc1-0-cnt")

                                self.ecc_1bit_err_uc1_1_cnt = YLeaf(YType.uint64, "ecc-1bit-err-uc1-1-cnt")

                                self.ecc_1bit_err_uc2_0_cnt = YLeaf(YType.uint64, "ecc-1bit-err-uc2-0-cnt")

                                self.ecc_1bit_err_uc2_1_cnt = YLeaf(YType.uint64, "ecc-1bit-err-uc2-1-cnt")

                                self.ecc_2bit_err_uc0_0_cnt = YLeaf(YType.uint64, "ecc-2bit-err-uc0-0-cnt")

                                self.ecc_2bit_err_uc0_1_cnt = YLeaf(YType.uint64, "ecc-2bit-err-uc0-1-cnt")

                                self.ecc_2bit_err_uc1_0_cnt = YLeaf(YType.uint64, "ecc-2bit-err-uc1-0-cnt")

                                self.ecc_2bit_err_uc1_1_cnt = YLeaf(YType.uint64, "ecc-2bit-err-uc1-1-cnt")

                                self.ecc_2bit_err_uc2_0_cnt = YLeaf(YType.uint64, "ecc-2bit-err-uc2-0-cnt")

                                self.ecc_2bit_err_uc2_1_cnt = YLeaf(YType.uint64, "ecc-2bit-err-uc2-1-cnt")

                                self.fc_uc_0_1_trans_cnt = YLeaf(YType.uint64, "fc-uc-0-1-trans-cnt")

                                self.fe_uc_sop_eop_pack_cnt = YLeaf(YType.uint64, "fe-uc-sop-eop-pack-cnt")

                                self.in_full_line_uc0_cnt = YLeaf(YType.uint64, "in-full-line-uc0-cnt")

                                self.in_full_line_uc1_cnt = YLeaf(YType.uint64, "in-full-line-uc1-cnt")

                                self.in_full_line_uc2_cnt = YLeaf(YType.uint64, "in-full-line-uc2-cnt")

                                self.in_pkt_uc0_cnt = YLeaf(YType.uint64, "in-pkt-uc0-cnt")

                                self.in_pkt_uc1_cnt = YLeaf(YType.uint64, "in-pkt-uc1-cnt")

                                self.in_pkt_uc2_cnt = YLeaf(YType.uint64, "in-pkt-uc2-cnt")

                                self.out_pkt_uc_cnt = YLeaf(YType.uint64, "out-pkt-uc-cnt")

                                self.pkt_ecc_err_drop_uc_cnt = YLeaf(YType.uint64, "pkt-ecc-err-drop-uc-cnt")

                                self.pkt_ecc_trunc_cnt_uc_cnt = YLeaf(YType.uint64, "pkt-ecc-trunc-cnt-uc-cnt")

                                self.pkt_sop_drop_uc0_cnt = YLeaf(YType.uint64, "pkt-sop-drop-uc0-cnt")

                                self.pkt_sop_drop_uc1_cnt = YLeaf(YType.uint64, "pkt-sop-drop-uc1-cnt")

                                self.pkt_sop_drop_uc2_cnt = YLeaf(YType.uint64, "pkt-sop-drop-uc2-cnt")

                                self.pkt_trunc_eop_uc0_cnt = YLeaf(YType.uint64, "pkt-trunc-eop-uc0-cnt")

                                self.pkt_trunc_eop_uc1_cnt = YLeaf(YType.uint64, "pkt-trunc-eop-uc1-cnt")

                                self.pkt_trunc_eop_uc2_cnt = YLeaf(YType.uint64, "pkt-trunc-eop-uc2-cnt")

                                self.rate_cnt = YLeaf(YType.uint64, "rate-cnt")
                                self._segment_path = lambda: "pe-uc-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeUcStats, ['calc_rate', 'ecc_1bit_err_uc0_0_cnt', 'ecc_1bit_err_uc0_1_cnt', 'ecc_1bit_err_uc1_0_cnt', 'ecc_1bit_err_uc1_1_cnt', 'ecc_1bit_err_uc2_0_cnt', 'ecc_1bit_err_uc2_1_cnt', 'ecc_2bit_err_uc0_0_cnt', 'ecc_2bit_err_uc0_1_cnt', 'ecc_2bit_err_uc1_0_cnt', 'ecc_2bit_err_uc1_1_cnt', 'ecc_2bit_err_uc2_0_cnt', 'ecc_2bit_err_uc2_1_cnt', 'fc_uc_0_1_trans_cnt', 'fe_uc_sop_eop_pack_cnt', 'in_full_line_uc0_cnt', 'in_full_line_uc1_cnt', 'in_full_line_uc2_cnt', 'in_pkt_uc0_cnt', 'in_pkt_uc1_cnt', 'in_pkt_uc2_cnt', 'out_pkt_uc_cnt', 'pkt_ecc_err_drop_uc_cnt', 'pkt_ecc_trunc_cnt_uc_cnt', 'pkt_sop_drop_uc0_cnt', 'pkt_sop_drop_uc1_cnt', 'pkt_sop_drop_uc2_cnt', 'pkt_trunc_eop_uc0_cnt', 'pkt_trunc_eop_uc1_cnt', 'pkt_trunc_eop_uc2_cnt', 'rate_cnt'], name, value)


                        class PiCcStats(Entity):
                            """
                            pi cc stats
                            
                            .. attribute:: calc_rate
                            
                            	calc rate
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem_ecc_derr_cnt
                            
                            	DATA MEM ECC DERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem_ecc_serr_cnt
                            
                            	DATA MEM ECC SERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem_ovf0_cnt
                            
                            	DATA MEM OVF0 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem_ovf1_cnt
                            
                            	DATA MEM OVF1 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dmem_rd_cnt
                            
                            	DMEM RD CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fpoe_mem_ecc_derr_cnt
                            
                            	FPOE MEM ECC DERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fpoe_mem_ecc_serr_cnt
                            
                            	FPOE MEM ECC SERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in0_cong_cnt
                            
                            	IN0 CONG CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in0_drop_cnt
                            
                            	IN0 DROP CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in0_ecc_derr_cnt
                            
                            	IN0 ECC DERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in0_ecc_serr_cnt
                            
                            	IN0 ECC SERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in0_fnc_err_cnt
                            
                            	IN0 FNC ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in0_pkt_cnt
                            
                            	IN0 PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in0_shut_cnt
                            
                            	IN0 SHUT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in1_cong_cnt
                            
                            	IN1 CONG CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in1_drop_cnt
                            
                            	IN1 DROP CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in1_ecc_derr_cnt
                            
                            	IN1 ECC DERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in1_ecc_serr_cnt
                            
                            	IN1 ECC SERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in1_fnc_err_cnt
                            
                            	IN1 FNC ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in1_pkt_cnt
                            
                            	IN1 PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in1_shut_cnt
                            
                            	IN1 SHUT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_dmem0_cnt
                            
                            	IN DMEM0 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_dmem1_cnt
                            
                            	IN DMEM1 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: null_poe_cnt
                            
                            	NULL POE CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_pkt_cnt
                            
                            	OUT PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rate_cnt
                            
                            	RATE CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: shut_ack_cnt
                            
                            	SHUT ACK CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: stop_thrsh_hit_cnt
                            
                            	STOP THRSH HIT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tail_drop_msg_cnt
                            
                            	TAIL DROP MSG CNT
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.calc_rate = YLeaf(YType.uint64, "calc-rate")

                                self.data_mem_ecc_derr_cnt = YLeaf(YType.uint64, "data-mem-ecc-derr-cnt")

                                self.data_mem_ecc_serr_cnt = YLeaf(YType.uint64, "data-mem-ecc-serr-cnt")

                                self.data_mem_ovf0_cnt = YLeaf(YType.uint64, "data-mem-ovf0-cnt")

                                self.data_mem_ovf1_cnt = YLeaf(YType.uint64, "data-mem-ovf1-cnt")

                                self.dmem_rd_cnt = YLeaf(YType.uint64, "dmem-rd-cnt")

                                self.fpoe_mem_ecc_derr_cnt = YLeaf(YType.uint64, "fpoe-mem-ecc-derr-cnt")

                                self.fpoe_mem_ecc_serr_cnt = YLeaf(YType.uint64, "fpoe-mem-ecc-serr-cnt")

                                self.in0_cong_cnt = YLeaf(YType.uint64, "in0-cong-cnt")

                                self.in0_drop_cnt = YLeaf(YType.uint64, "in0-drop-cnt")

                                self.in0_ecc_derr_cnt = YLeaf(YType.uint64, "in0-ecc-derr-cnt")

                                self.in0_ecc_serr_cnt = YLeaf(YType.uint64, "in0-ecc-serr-cnt")

                                self.in0_fnc_err_cnt = YLeaf(YType.uint64, "in0-fnc-err-cnt")

                                self.in0_pkt_cnt = YLeaf(YType.uint64, "in0-pkt-cnt")

                                self.in0_shut_cnt = YLeaf(YType.uint64, "in0-shut-cnt")

                                self.in1_cong_cnt = YLeaf(YType.uint64, "in1-cong-cnt")

                                self.in1_drop_cnt = YLeaf(YType.uint64, "in1-drop-cnt")

                                self.in1_ecc_derr_cnt = YLeaf(YType.uint64, "in1-ecc-derr-cnt")

                                self.in1_ecc_serr_cnt = YLeaf(YType.uint64, "in1-ecc-serr-cnt")

                                self.in1_fnc_err_cnt = YLeaf(YType.uint64, "in1-fnc-err-cnt")

                                self.in1_pkt_cnt = YLeaf(YType.uint64, "in1-pkt-cnt")

                                self.in1_shut_cnt = YLeaf(YType.uint64, "in1-shut-cnt")

                                self.in_dmem0_cnt = YLeaf(YType.uint64, "in-dmem0-cnt")

                                self.in_dmem1_cnt = YLeaf(YType.uint64, "in-dmem1-cnt")

                                self.null_poe_cnt = YLeaf(YType.uint64, "null-poe-cnt")

                                self.out_pkt_cnt = YLeaf(YType.uint64, "out-pkt-cnt")

                                self.rate_cnt = YLeaf(YType.uint64, "rate-cnt")

                                self.shut_ack_cnt = YLeaf(YType.uint64, "shut-ack-cnt")

                                self.stop_thrsh_hit_cnt = YLeaf(YType.uint64, "stop-thrsh-hit-cnt")

                                self.tail_drop_msg_cnt = YLeaf(YType.uint64, "tail-drop-msg-cnt")
                                self._segment_path = lambda: "pi-cc-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiCcStats, ['calc_rate', 'data_mem_ecc_derr_cnt', 'data_mem_ecc_serr_cnt', 'data_mem_ovf0_cnt', 'data_mem_ovf1_cnt', 'dmem_rd_cnt', 'fpoe_mem_ecc_derr_cnt', 'fpoe_mem_ecc_serr_cnt', 'in0_cong_cnt', 'in0_drop_cnt', 'in0_ecc_derr_cnt', 'in0_ecc_serr_cnt', 'in0_fnc_err_cnt', 'in0_pkt_cnt', 'in0_shut_cnt', 'in1_cong_cnt', 'in1_drop_cnt', 'in1_ecc_derr_cnt', 'in1_ecc_serr_cnt', 'in1_fnc_err_cnt', 'in1_pkt_cnt', 'in1_shut_cnt', 'in_dmem0_cnt', 'in_dmem1_cnt', 'null_poe_cnt', 'out_pkt_cnt', 'rate_cnt', 'shut_ack_cnt', 'stop_thrsh_hit_cnt', 'tail_drop_msg_cnt'], name, value)


                        class PiMcStats(Entity):
                            """
                            pi mc stats
                            
                            .. attribute:: calc_rate
                            
                            	calc rate
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: cpp_head_drop_pkt_from_ma_cnt
                            
                            	CPP HEAD DROP PKT FROM MA CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: crc_stomp_pkt_cnt
                            
                            	CRC STOMP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem0_ecc_1bit_err_cnt
                            
                            	DATA MEM0 ECC 1BIT ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem0_ecc_2bit_err_cnt
                            
                            	DATA MEM0 ECC 2BIT ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem1_ecc_1bit_err_cnt
                            
                            	DATA MEM1 ECC 1BIT ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem1_ecc_2bit_err_cnt
                            
                            	DATA MEM1 ECC 2BIT ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem2_ecc_1bit_err_cnt
                            
                            	DATA MEM2 ECC 1BIT ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_mem2_ecc_2bit_err_cnt
                            
                            	DATA MEM2 ECC 2BIT ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: di_err_pkt_cnt
                            
                            	DI ERR PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: di_hdr_len_err_pkt_cnt
                            
                            	DI HDR LEN ERR PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: diag_pkt_cnt
                            
                            	DIAG PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fpoe_mem_ecc_1bit_err_cnt
                            
                            	FPOE MEM ECC 1BIT ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fpoe_mem_ecc_2bit_err_cnt
                            
                            	FPOE MEM ECC 2BIT ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_coming_pkt_err_cnt
                            
                            	INCOMING PKT ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: line_err_drp_pkt
                            
                            	LINE ERR DRP PKT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: line_s_written_in_mem
                            
                            	LINES WRITTEN IN MEM
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: max_pkt_len_err_cnt
                            
                            	MAX PKT LEN ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: min_pkt_len_err_cnt
                            
                            	MIN PKT LEN ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_cfh_crc_err_cnt
                            
                            	PKT CFH CRC ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_crc_err_cnt
                            
                            	PKT CRC ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_fpoe_addr_rng_hit_cnt
                            
                            	PKT FPOE ADDR RNG HIT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_fpoe_match_hit_cnt
                            
                            	PKT FPOE MATCH HIT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_null_poe_sent_cnt
                            
                            	PKT NULL POE SENT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_rcv_cnt
                            
                            	PKT RCV CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_sent_to_disabled_port
                            
                            	PKT SENT TO DISABLED PORT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_seq_err_cnt
                            
                            	PKT SEQ ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkts_sent_to_mx_cnt
                            
                            	PKTS SENT TO MX CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rate_cnt
                            
                            	RATE CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: stop_thrsh_hit_cnt
                            
                            	STOP THRSH HIT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tail_drp_pkt_cnt
                            
                            	TAIL DRP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tr_head_drop_pkt_from_ma_cnt
                            
                            	TR HEAD DROP PKT FROM MA CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tr_pkt_sent_to_mx
                            
                            	TR PKT SENT TO MX
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.calc_rate = YLeaf(YType.uint64, "calc-rate")

                                self.cpp_head_drop_pkt_from_ma_cnt = YLeaf(YType.uint64, "cpp-head-drop-pkt-from-ma-cnt")

                                self.crc_stomp_pkt_cnt = YLeaf(YType.uint64, "crc-stomp-pkt-cnt")

                                self.data_mem0_ecc_1bit_err_cnt = YLeaf(YType.uint64, "data-mem0-ecc-1bit-err-cnt")

                                self.data_mem0_ecc_2bit_err_cnt = YLeaf(YType.uint64, "data-mem0-ecc-2bit-err-cnt")

                                self.data_mem1_ecc_1bit_err_cnt = YLeaf(YType.uint64, "data-mem1-ecc-1bit-err-cnt")

                                self.data_mem1_ecc_2bit_err_cnt = YLeaf(YType.uint64, "data-mem1-ecc-2bit-err-cnt")

                                self.data_mem2_ecc_1bit_err_cnt = YLeaf(YType.uint64, "data-mem2-ecc-1bit-err-cnt")

                                self.data_mem2_ecc_2bit_err_cnt = YLeaf(YType.uint64, "data-mem2-ecc-2bit-err-cnt")

                                self.di_err_pkt_cnt = YLeaf(YType.uint64, "di-err-pkt-cnt")

                                self.di_hdr_len_err_pkt_cnt = YLeaf(YType.uint64, "di-hdr-len-err-pkt-cnt")

                                self.diag_pkt_cnt = YLeaf(YType.uint64, "diag-pkt-cnt")

                                self.fpoe_mem_ecc_1bit_err_cnt = YLeaf(YType.uint64, "fpoe-mem-ecc-1bit-err-cnt")

                                self.fpoe_mem_ecc_2bit_err_cnt = YLeaf(YType.uint64, "fpoe-mem-ecc-2bit-err-cnt")

                                self.in_coming_pkt_err_cnt = YLeaf(YType.uint64, "in-coming-pkt-err-cnt")

                                self.line_err_drp_pkt = YLeaf(YType.uint64, "line-err-drp-pkt")

                                self.line_s_written_in_mem = YLeaf(YType.uint64, "line-s-written-in-mem")

                                self.max_pkt_len_err_cnt = YLeaf(YType.uint64, "max-pkt-len-err-cnt")

                                self.min_pkt_len_err_cnt = YLeaf(YType.uint64, "min-pkt-len-err-cnt")

                                self.pkt_cfh_crc_err_cnt = YLeaf(YType.uint64, "pkt-cfh-crc-err-cnt")

                                self.pkt_crc_err_cnt = YLeaf(YType.uint64, "pkt-crc-err-cnt")

                                self.pkt_fpoe_addr_rng_hit_cnt = YLeaf(YType.uint64, "pkt-fpoe-addr-rng-hit-cnt")

                                self.pkt_fpoe_match_hit_cnt = YLeaf(YType.uint64, "pkt-fpoe-match-hit-cnt")

                                self.pkt_null_poe_sent_cnt = YLeaf(YType.uint64, "pkt-null-poe-sent-cnt")

                                self.pkt_rcv_cnt = YLeaf(YType.uint64, "pkt-rcv-cnt")

                                self.pkt_sent_to_disabled_port = YLeaf(YType.uint64, "pkt-sent-to-disabled-port")

                                self.pkt_seq_err_cnt = YLeaf(YType.uint64, "pkt-seq-err-cnt")

                                self.pkts_sent_to_mx_cnt = YLeaf(YType.uint64, "pkts-sent-to-mx-cnt")

                                self.rate_cnt = YLeaf(YType.uint64, "rate-cnt")

                                self.stop_thrsh_hit_cnt = YLeaf(YType.uint64, "stop-thrsh-hit-cnt")

                                self.tail_drp_pkt_cnt = YLeaf(YType.uint64, "tail-drp-pkt-cnt")

                                self.tr_head_drop_pkt_from_ma_cnt = YLeaf(YType.uint64, "tr-head-drop-pkt-from-ma-cnt")

                                self.tr_pkt_sent_to_mx = YLeaf(YType.uint64, "tr-pkt-sent-to-mx")
                                self._segment_path = lambda: "pi-mc-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiMcStats, ['calc_rate', 'cpp_head_drop_pkt_from_ma_cnt', 'crc_stomp_pkt_cnt', 'data_mem0_ecc_1bit_err_cnt', 'data_mem0_ecc_2bit_err_cnt', 'data_mem1_ecc_1bit_err_cnt', 'data_mem1_ecc_2bit_err_cnt', 'data_mem2_ecc_1bit_err_cnt', 'data_mem2_ecc_2bit_err_cnt', 'di_err_pkt_cnt', 'di_hdr_len_err_pkt_cnt', 'diag_pkt_cnt', 'fpoe_mem_ecc_1bit_err_cnt', 'fpoe_mem_ecc_2bit_err_cnt', 'in_coming_pkt_err_cnt', 'line_err_drp_pkt', 'line_s_written_in_mem', 'max_pkt_len_err_cnt', 'min_pkt_len_err_cnt', 'pkt_cfh_crc_err_cnt', 'pkt_crc_err_cnt', 'pkt_fpoe_addr_rng_hit_cnt', 'pkt_fpoe_match_hit_cnt', 'pkt_null_poe_sent_cnt', 'pkt_rcv_cnt', 'pkt_sent_to_disabled_port', 'pkt_seq_err_cnt', 'pkts_sent_to_mx_cnt', 'rate_cnt', 'stop_thrsh_hit_cnt', 'tail_drp_pkt_cnt', 'tr_head_drop_pkt_from_ma_cnt', 'tr_pkt_sent_to_mx'], name, value)


                        class PiStats(Entity):
                            """
                            pi stats
                            
                            .. attribute:: total_calc_rate
                            
                            	total calc rate
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: total_rate1_cnt
                            
                            	TOTAL RATE1 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: total_rate2_cnt
                            
                            	TOTAL RATE2 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: total_rate3_cnt
                            
                            	TOTAL RATE3 CNT
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.total_calc_rate = YLeaf(YType.uint64, "total-calc-rate")

                                self.total_rate1_cnt = YLeaf(YType.uint64, "total-rate1-cnt")

                                self.total_rate2_cnt = YLeaf(YType.uint64, "total-rate2-cnt")

                                self.total_rate3_cnt = YLeaf(YType.uint64, "total-rate3-cnt")
                                self._segment_path = lambda: "pi-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiStats, ['total_calc_rate', 'total_rate1_cnt', 'total_rate2_cnt', 'total_rate3_cnt'], name, value)


                        class PiUcStats(Entity):
                            """
                            pi uc stats
                            
                            .. attribute:: calc_rate
                            
                            	calc rate
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: cpp_head_drop_pkt_cnt
                            
                            	CPP HEAD DROP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: crc_stomp_pkt_cnt
                            
                            	CRC STOMP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: diag_pkt_cnt
                            
                            	DIAG PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fpoe_mem_ecc_1bit_err_cnt
                            
                            	FPOE MEM ECC 1BIT ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: fpoe_mem_ecc_2bit_err_cnt
                            
                            	FPOE MEM ECC 2BIT ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_coming_pkt_err_cnt
                            
                            	INCOMING PKT ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: line_err_drp_pkt
                            
                            	LINE ERR DRP PKT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: line_s_written_in_mem0
                            
                            	LINES WRITTEN IN MEM0
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: line_s_written_in_mem1
                            
                            	LINES WRITTEN IN MEM1
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: line_s_written_in_mem2
                            
                            	LINES WRITTEN IN MEM2
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: max_pkt_len_err_cnt
                            
                            	MAX PKT LEN ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: min_pkt_len_err_cnt
                            
                            	MIN PKT LEN ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_cfh_crc_err_cnt
                            
                            	PKT CFH CRC ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_crc_err_cnt
                            
                            	PKT CRC ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_fpoe_addr_rng_hit_cnt
                            
                            	PKT FPOE ADDR RNG HIT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_null_poe_sent_ua0_cnt
                            
                            	PKT NULL POE SENT UA0 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_null_poe_sent_ua1_cnt
                            
                            	PKT NULL POE SENT UA1 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_null_poe_sent_ua2_cnt
                            
                            	PKT NULL POE SENT UA2 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_rcv_cnt
                            
                            	PKT RCV CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_sent_to_disabled_port_cnt
                            
                            	PKT SENT TO DISABLED PORT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkt_seq_err_cnt
                            
                            	PKT SEQ ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkts_sent_to_ux0_cnt
                            
                            	PKTS SENT TO UX0 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkts_sent_to_ux1_cnt
                            
                            	PKTS SENT TO UX1 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pkts_sent_to_ux2_cnt
                            
                            	PKTS SENT TO UX2 CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rate_cnt
                            
                            	RATE CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: stop_thrsh_hit_cnt
                            
                            	STOP THRSH HIT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tail_drp_pkt_cnt
                            
                            	TAIL DRP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tr_head_drop_pkt_cnt
                            
                            	TR HEAD DROP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tr_pkt_sent_to_ux
                            
                            	TR PKT SENT TO UX
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: uc0_data_mem_ecc_1bit_err_cnt
                            
                            	UC0 DATA MEM ECC 1BIT ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: uc0_data_mem_ecc_2bit_err_cnt
                            
                            	UC0 DATA MEM ECC 2BIT ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: uc1_data_mem_ecc_1bit_err_cnt
                            
                            	UC1 DATA MEM ECC 1BIT ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: uc1_data_mem_ecc_2bit_err_cnt
                            
                            	UC1 DATA MEM ECC 2BIT ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: uc2_data_mem_ecc_1bit_err_cnt
                            
                            	UC2 DATA MEM ECC 1BIT ERR CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: uc2_data_mem_ecc_2bit_err_cnt
                            
                            	UC2 DATA MEM ECC 2BIT ERR CNT
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.calc_rate = YLeaf(YType.uint64, "calc-rate")

                                self.cpp_head_drop_pkt_cnt = YLeaf(YType.uint64, "cpp-head-drop-pkt-cnt")

                                self.crc_stomp_pkt_cnt = YLeaf(YType.uint64, "crc-stomp-pkt-cnt")

                                self.diag_pkt_cnt = YLeaf(YType.uint64, "diag-pkt-cnt")

                                self.fpoe_mem_ecc_1bit_err_cnt = YLeaf(YType.uint64, "fpoe-mem-ecc-1bit-err-cnt")

                                self.fpoe_mem_ecc_2bit_err_cnt = YLeaf(YType.uint64, "fpoe-mem-ecc-2bit-err-cnt")

                                self.in_coming_pkt_err_cnt = YLeaf(YType.uint64, "in-coming-pkt-err-cnt")

                                self.line_err_drp_pkt = YLeaf(YType.uint64, "line-err-drp-pkt")

                                self.line_s_written_in_mem0 = YLeaf(YType.uint64, "line-s-written-in-mem0")

                                self.line_s_written_in_mem1 = YLeaf(YType.uint64, "line-s-written-in-mem1")

                                self.line_s_written_in_mem2 = YLeaf(YType.uint64, "line-s-written-in-mem2")

                                self.max_pkt_len_err_cnt = YLeaf(YType.uint64, "max-pkt-len-err-cnt")

                                self.min_pkt_len_err_cnt = YLeaf(YType.uint64, "min-pkt-len-err-cnt")

                                self.pkt_cfh_crc_err_cnt = YLeaf(YType.uint64, "pkt-cfh-crc-err-cnt")

                                self.pkt_crc_err_cnt = YLeaf(YType.uint64, "pkt-crc-err-cnt")

                                self.pkt_fpoe_addr_rng_hit_cnt = YLeaf(YType.uint64, "pkt-fpoe-addr-rng-hit-cnt")

                                self.pkt_null_poe_sent_ua0_cnt = YLeaf(YType.uint64, "pkt-null-poe-sent-ua0-cnt")

                                self.pkt_null_poe_sent_ua1_cnt = YLeaf(YType.uint64, "pkt-null-poe-sent-ua1-cnt")

                                self.pkt_null_poe_sent_ua2_cnt = YLeaf(YType.uint64, "pkt-null-poe-sent-ua2-cnt")

                                self.pkt_rcv_cnt = YLeaf(YType.uint64, "pkt-rcv-cnt")

                                self.pkt_sent_to_disabled_port_cnt = YLeaf(YType.uint64, "pkt-sent-to-disabled-port-cnt")

                                self.pkt_seq_err_cnt = YLeaf(YType.uint64, "pkt-seq-err-cnt")

                                self.pkts_sent_to_ux0_cnt = YLeaf(YType.uint64, "pkts-sent-to-ux0-cnt")

                                self.pkts_sent_to_ux1_cnt = YLeaf(YType.uint64, "pkts-sent-to-ux1-cnt")

                                self.pkts_sent_to_ux2_cnt = YLeaf(YType.uint64, "pkts-sent-to-ux2-cnt")

                                self.rate_cnt = YLeaf(YType.uint64, "rate-cnt")

                                self.stop_thrsh_hit_cnt = YLeaf(YType.uint64, "stop-thrsh-hit-cnt")

                                self.tail_drp_pkt_cnt = YLeaf(YType.uint64, "tail-drp-pkt-cnt")

                                self.tr_head_drop_pkt_cnt = YLeaf(YType.uint64, "tr-head-drop-pkt-cnt")

                                self.tr_pkt_sent_to_ux = YLeaf(YType.uint64, "tr-pkt-sent-to-ux")

                                self.uc0_data_mem_ecc_1bit_err_cnt = YLeaf(YType.uint64, "uc0-data-mem-ecc-1bit-err-cnt")

                                self.uc0_data_mem_ecc_2bit_err_cnt = YLeaf(YType.uint64, "uc0-data-mem-ecc-2bit-err-cnt")

                                self.uc1_data_mem_ecc_1bit_err_cnt = YLeaf(YType.uint64, "uc1-data-mem-ecc-1bit-err-cnt")

                                self.uc1_data_mem_ecc_2bit_err_cnt = YLeaf(YType.uint64, "uc1-data-mem-ecc-2bit-err-cnt")

                                self.uc2_data_mem_ecc_1bit_err_cnt = YLeaf(YType.uint64, "uc2-data-mem-ecc-1bit-err-cnt")

                                self.uc2_data_mem_ecc_2bit_err_cnt = YLeaf(YType.uint64, "uc2-data-mem-ecc-2bit-err-cnt")
                                self._segment_path = lambda: "pi-uc-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiUcStats, ['calc_rate', 'cpp_head_drop_pkt_cnt', 'crc_stomp_pkt_cnt', 'diag_pkt_cnt', 'fpoe_mem_ecc_1bit_err_cnt', 'fpoe_mem_ecc_2bit_err_cnt', 'in_coming_pkt_err_cnt', 'line_err_drp_pkt', 'line_s_written_in_mem0', 'line_s_written_in_mem1', 'line_s_written_in_mem2', 'max_pkt_len_err_cnt', 'min_pkt_len_err_cnt', 'pkt_cfh_crc_err_cnt', 'pkt_crc_err_cnt', 'pkt_fpoe_addr_rng_hit_cnt', 'pkt_null_poe_sent_ua0_cnt', 'pkt_null_poe_sent_ua1_cnt', 'pkt_null_poe_sent_ua2_cnt', 'pkt_rcv_cnt', 'pkt_sent_to_disabled_port_cnt', 'pkt_seq_err_cnt', 'pkts_sent_to_ux0_cnt', 'pkts_sent_to_ux1_cnt', 'pkts_sent_to_ux2_cnt', 'rate_cnt', 'stop_thrsh_hit_cnt', 'tail_drp_pkt_cnt', 'tr_head_drop_pkt_cnt', 'tr_pkt_sent_to_ux', 'uc0_data_mem_ecc_1bit_err_cnt', 'uc0_data_mem_ecc_2bit_err_cnt', 'uc1_data_mem_ecc_1bit_err_cnt', 'uc1_data_mem_ecc_2bit_err_cnt', 'uc2_data_mem_ecc_1bit_err_cnt', 'uc2_data_mem_ecc_2bit_err_cnt'], name, value)


                        class Ua0Stats(Entity):
                            """
                            ua0 stats
                            
                            .. attribute:: ack_wait_cnt
                            
                            	ACK WAIT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dest_drop_pkt_cnt
                            
                            	DEST DROP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dest_src_pkt_cnt
                            
                            	DEST SRC PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rcv_pkt_cnt
                            
                            	RCV PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_drop_pkt_cnt
                            
                            	RX DROP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_fabric_to_cnt
                            
                            	RX FABRIC TO CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: src_dest_pkt_cnt
                            
                            	SRC DEST PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tx_pkt_cnt
                            
                            	TX PKT CNT
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ack_wait_cnt = YLeaf(YType.uint64, "ack-wait-cnt")

                                self.dest_drop_pkt_cnt = YLeaf(YType.uint64, "dest-drop-pkt-cnt")

                                self.dest_src_pkt_cnt = YLeaf(YType.uint64, "dest-src-pkt-cnt")

                                self.rcv_pkt_cnt = YLeaf(YType.uint64, "rcv-pkt-cnt")

                                self.rx_drop_pkt_cnt = YLeaf(YType.uint64, "rx-drop-pkt-cnt")

                                self.rx_fabric_to_cnt = YLeaf(YType.uint64, "rx-fabric-to-cnt")

                                self.src_dest_pkt_cnt = YLeaf(YType.uint64, "src-dest-pkt-cnt")

                                self.tx_pkt_cnt = YLeaf(YType.uint64, "tx-pkt-cnt")
                                self._segment_path = lambda: "ua0-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua0Stats, ['ack_wait_cnt', 'dest_drop_pkt_cnt', 'dest_src_pkt_cnt', 'rcv_pkt_cnt', 'rx_drop_pkt_cnt', 'rx_fabric_to_cnt', 'src_dest_pkt_cnt', 'tx_pkt_cnt'], name, value)


                        class Ua1Stats(Entity):
                            """
                            ua1 stats
                            
                            .. attribute:: ack_wait_cnt
                            
                            	ACK WAIT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dest_drop_pkt_cnt
                            
                            	DEST DROP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dest_src_pkt_cnt
                            
                            	DEST SRC PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rcv_pkt_cnt
                            
                            	RCV PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_drop_pkt_cnt
                            
                            	RX DROP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_fabric_to_cnt
                            
                            	RX FABRIC TO CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: src_dest_pkt_cnt
                            
                            	SRC DEST PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tx_pkt_cnt
                            
                            	TX PKT CNT
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ack_wait_cnt = YLeaf(YType.uint64, "ack-wait-cnt")

                                self.dest_drop_pkt_cnt = YLeaf(YType.uint64, "dest-drop-pkt-cnt")

                                self.dest_src_pkt_cnt = YLeaf(YType.uint64, "dest-src-pkt-cnt")

                                self.rcv_pkt_cnt = YLeaf(YType.uint64, "rcv-pkt-cnt")

                                self.rx_drop_pkt_cnt = YLeaf(YType.uint64, "rx-drop-pkt-cnt")

                                self.rx_fabric_to_cnt = YLeaf(YType.uint64, "rx-fabric-to-cnt")

                                self.src_dest_pkt_cnt = YLeaf(YType.uint64, "src-dest-pkt-cnt")

                                self.tx_pkt_cnt = YLeaf(YType.uint64, "tx-pkt-cnt")
                                self._segment_path = lambda: "ua1-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua1Stats, ['ack_wait_cnt', 'dest_drop_pkt_cnt', 'dest_src_pkt_cnt', 'rcv_pkt_cnt', 'rx_drop_pkt_cnt', 'rx_fabric_to_cnt', 'src_dest_pkt_cnt', 'tx_pkt_cnt'], name, value)


                        class Ua2Stats(Entity):
                            """
                            ua2 stats
                            
                            .. attribute:: ack_wait_cnt
                            
                            	ACK WAIT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dest_drop_pkt_cnt
                            
                            	DEST DROP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dest_src_pkt_cnt
                            
                            	DEST SRC PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rcv_pkt_cnt
                            
                            	RCV PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_drop_pkt_cnt
                            
                            	RX DROP PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rx_fabric_to_cnt
                            
                            	RX FABRIC TO CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: src_dest_pkt_cnt
                            
                            	SRC DEST PKT CNT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tx_pkt_cnt
                            
                            	TX PKT CNT
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ack_wait_cnt = YLeaf(YType.uint64, "ack-wait-cnt")

                                self.dest_drop_pkt_cnt = YLeaf(YType.uint64, "dest-drop-pkt-cnt")

                                self.dest_src_pkt_cnt = YLeaf(YType.uint64, "dest-src-pkt-cnt")

                                self.rcv_pkt_cnt = YLeaf(YType.uint64, "rcv-pkt-cnt")

                                self.rx_drop_pkt_cnt = YLeaf(YType.uint64, "rx-drop-pkt-cnt")

                                self.rx_fabric_to_cnt = YLeaf(YType.uint64, "rx-fabric-to-cnt")

                                self.src_dest_pkt_cnt = YLeaf(YType.uint64, "src-dest-pkt-cnt")

                                self.tx_pkt_cnt = YLeaf(YType.uint64, "tx-pkt-cnt")
                                self._segment_path = lambda: "ua2-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua2Stats, ['ack_wait_cnt', 'dest_drop_pkt_cnt', 'dest_src_pkt_cnt', 'rcv_pkt_cnt', 'rx_drop_pkt_cnt', 'rx_fabric_to_cnt', 'src_dest_pkt_cnt', 'tx_pkt_cnt'], name, value)

    def clone_ptr(self):
        self._top_entity = CrossBarStats()
        return self._top_entity

