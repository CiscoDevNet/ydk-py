""" Cisco_IOS_XR_asr9k_xbar_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-xbar package operational data.

This module contains definitions
for the following management objects\:
  cross\-bar\-stats\: Crossbar stats operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

        self.nodes = CrossBarStats.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


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
                        super(CrossBarStats.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CrossBarStats.Nodes, self).__setattr__(name, value)


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

                self.node_name = YLeaf(YType.str, "node-name")

                self.cross_bar_table = CrossBarStats.Nodes.Node.CrossBarTable()
                self.cross_bar_table.parent = self
                self._children_name_map["cross_bar_table"] = "cross-bar-table"
                self._children_yang_names.add("cross-bar-table")

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
                            super(CrossBarStats.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CrossBarStats.Nodes.Node, self).__setattr__(name, value)


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

                    self.pkt_stats = CrossBarStats.Nodes.Node.CrossBarTable.PktStats()
                    self.pkt_stats.parent = self
                    self._children_name_map["pkt_stats"] = "pkt-stats"
                    self._children_yang_names.add("pkt-stats")

                    self.sm15_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats()
                    self.sm15_stats.parent = self
                    self._children_name_map["sm15_stats"] = "sm15-stats"
                    self._children_yang_names.add("sm15-stats")


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

                        self.pkt_stat = YList(self)

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
                                    super(CrossBarStats.Nodes.Node.CrossBarTable.PktStats, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(CrossBarStats.Nodes.Node.CrossBarTable.PktStats, self).__setattr__(name, value)


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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("asic_id",
                                            "diagnostic_packet_count_high",
                                            "diagnostic_packet_count_low",
                                            "egress_channel_utilization_count_high",
                                            "egress_channel_utilization_count_low",
                                            "egress_packet_count_since_last_read_high",
                                            "egress_packet_count_since_last_read_low",
                                            "fpoedb_correctable_ecc_error_count_high",
                                            "fpoedb_correctable_ecc_error_count_low",
                                            "fpoedb_uncorrectable_ecc_error_count_high",
                                            "fpoedb_uncorrectable_ecc_error_count_low",
                                            "header_crc_error_count_high",
                                            "header_crc_error_count_low",
                                            "holdrop_count_high",
                                            "holdrop_count_low",
                                            "ingress_channel_utilization_count_high",
                                            "ingress_channel_utilization_count_low",
                                            "ingress_packet_count_since_last_read_high",
                                            "ingress_packet_count_since_last_read_low",
                                            "input_buffer_back_pressure_count_high",
                                            "input_buffer_back_pressure_count_low",
                                            "input_buffer_correctable_ecc_error_count_high",
                                            "input_buffer_correctable_ecc_error_count_low",
                                            "input_buffer_queued_packet_count_high",
                                            "input_buffer_queued_packet_count_low",
                                            "input_buffer_uncorrectable_ecc_error_count_high",
                                            "input_buffer_uncorrectable_ecc_error_count_low",
                                            "internal_error_count",
                                            "null_fpoe_drop_count_high",
                                            "null_fpoe_drop_count_low",
                                            "output_buffer_back_pressure_count_high",
                                            "output_buffer_back_pressure_count_low",
                                            "output_buffer_correctable_ecc_error_count_high",
                                            "output_buffer_correctable_ecc_error_count_low",
                                            "output_buffer_queued_packet_count_high",
                                            "output_buffer_queued_packet_count_low",
                                            "output_buffer_uncorrectable_ecc_error_count_high",
                                            "output_buffer_uncorrectable_ecc_error_count_low",
                                            "packet_crc_error_count_high",
                                            "packet_crc_error_count_low",
                                            "port",
                                            "short_input_header_error_count_high",
                                            "short_input_header_error_count_low",
                                            "short_packet_error_count_high",
                                            "short_packet_error_count_low",
                                            "xbar_timeout_drop_count_high",
                                            "xbar_timeout_drop_count_low") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.PktStats.PktStat, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(CrossBarStats.Nodes.Node.CrossBarTable.PktStats.PktStat, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.asic_id.is_set or
                                self.diagnostic_packet_count_high.is_set or
                                self.diagnostic_packet_count_low.is_set or
                                self.egress_channel_utilization_count_high.is_set or
                                self.egress_channel_utilization_count_low.is_set or
                                self.egress_packet_count_since_last_read_high.is_set or
                                self.egress_packet_count_since_last_read_low.is_set or
                                self.fpoedb_correctable_ecc_error_count_high.is_set or
                                self.fpoedb_correctable_ecc_error_count_low.is_set or
                                self.fpoedb_uncorrectable_ecc_error_count_high.is_set or
                                self.fpoedb_uncorrectable_ecc_error_count_low.is_set or
                                self.header_crc_error_count_high.is_set or
                                self.header_crc_error_count_low.is_set or
                                self.holdrop_count_high.is_set or
                                self.holdrop_count_low.is_set or
                                self.ingress_channel_utilization_count_high.is_set or
                                self.ingress_channel_utilization_count_low.is_set or
                                self.ingress_packet_count_since_last_read_high.is_set or
                                self.ingress_packet_count_since_last_read_low.is_set or
                                self.input_buffer_back_pressure_count_high.is_set or
                                self.input_buffer_back_pressure_count_low.is_set or
                                self.input_buffer_correctable_ecc_error_count_high.is_set or
                                self.input_buffer_correctable_ecc_error_count_low.is_set or
                                self.input_buffer_queued_packet_count_high.is_set or
                                self.input_buffer_queued_packet_count_low.is_set or
                                self.input_buffer_uncorrectable_ecc_error_count_high.is_set or
                                self.input_buffer_uncorrectable_ecc_error_count_low.is_set or
                                self.internal_error_count.is_set or
                                self.null_fpoe_drop_count_high.is_set or
                                self.null_fpoe_drop_count_low.is_set or
                                self.output_buffer_back_pressure_count_high.is_set or
                                self.output_buffer_back_pressure_count_low.is_set or
                                self.output_buffer_correctable_ecc_error_count_high.is_set or
                                self.output_buffer_correctable_ecc_error_count_low.is_set or
                                self.output_buffer_queued_packet_count_high.is_set or
                                self.output_buffer_queued_packet_count_low.is_set or
                                self.output_buffer_uncorrectable_ecc_error_count_high.is_set or
                                self.output_buffer_uncorrectable_ecc_error_count_low.is_set or
                                self.packet_crc_error_count_high.is_set or
                                self.packet_crc_error_count_low.is_set or
                                self.port.is_set or
                                self.short_input_header_error_count_high.is_set or
                                self.short_input_header_error_count_low.is_set or
                                self.short_packet_error_count_high.is_set or
                                self.short_packet_error_count_low.is_set or
                                self.xbar_timeout_drop_count_high.is_set or
                                self.xbar_timeout_drop_count_low.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.asic_id.yfilter != YFilter.not_set or
                                self.diagnostic_packet_count_high.yfilter != YFilter.not_set or
                                self.diagnostic_packet_count_low.yfilter != YFilter.not_set or
                                self.egress_channel_utilization_count_high.yfilter != YFilter.not_set or
                                self.egress_channel_utilization_count_low.yfilter != YFilter.not_set or
                                self.egress_packet_count_since_last_read_high.yfilter != YFilter.not_set or
                                self.egress_packet_count_since_last_read_low.yfilter != YFilter.not_set or
                                self.fpoedb_correctable_ecc_error_count_high.yfilter != YFilter.not_set or
                                self.fpoedb_correctable_ecc_error_count_low.yfilter != YFilter.not_set or
                                self.fpoedb_uncorrectable_ecc_error_count_high.yfilter != YFilter.not_set or
                                self.fpoedb_uncorrectable_ecc_error_count_low.yfilter != YFilter.not_set or
                                self.header_crc_error_count_high.yfilter != YFilter.not_set or
                                self.header_crc_error_count_low.yfilter != YFilter.not_set or
                                self.holdrop_count_high.yfilter != YFilter.not_set or
                                self.holdrop_count_low.yfilter != YFilter.not_set or
                                self.ingress_channel_utilization_count_high.yfilter != YFilter.not_set or
                                self.ingress_channel_utilization_count_low.yfilter != YFilter.not_set or
                                self.ingress_packet_count_since_last_read_high.yfilter != YFilter.not_set or
                                self.ingress_packet_count_since_last_read_low.yfilter != YFilter.not_set or
                                self.input_buffer_back_pressure_count_high.yfilter != YFilter.not_set or
                                self.input_buffer_back_pressure_count_low.yfilter != YFilter.not_set or
                                self.input_buffer_correctable_ecc_error_count_high.yfilter != YFilter.not_set or
                                self.input_buffer_correctable_ecc_error_count_low.yfilter != YFilter.not_set or
                                self.input_buffer_queued_packet_count_high.yfilter != YFilter.not_set or
                                self.input_buffer_queued_packet_count_low.yfilter != YFilter.not_set or
                                self.input_buffer_uncorrectable_ecc_error_count_high.yfilter != YFilter.not_set or
                                self.input_buffer_uncorrectable_ecc_error_count_low.yfilter != YFilter.not_set or
                                self.internal_error_count.yfilter != YFilter.not_set or
                                self.null_fpoe_drop_count_high.yfilter != YFilter.not_set or
                                self.null_fpoe_drop_count_low.yfilter != YFilter.not_set or
                                self.output_buffer_back_pressure_count_high.yfilter != YFilter.not_set or
                                self.output_buffer_back_pressure_count_low.yfilter != YFilter.not_set or
                                self.output_buffer_correctable_ecc_error_count_high.yfilter != YFilter.not_set or
                                self.output_buffer_correctable_ecc_error_count_low.yfilter != YFilter.not_set or
                                self.output_buffer_queued_packet_count_high.yfilter != YFilter.not_set or
                                self.output_buffer_queued_packet_count_low.yfilter != YFilter.not_set or
                                self.output_buffer_uncorrectable_ecc_error_count_high.yfilter != YFilter.not_set or
                                self.output_buffer_uncorrectable_ecc_error_count_low.yfilter != YFilter.not_set or
                                self.packet_crc_error_count_high.yfilter != YFilter.not_set or
                                self.packet_crc_error_count_low.yfilter != YFilter.not_set or
                                self.port.yfilter != YFilter.not_set or
                                self.short_input_header_error_count_high.yfilter != YFilter.not_set or
                                self.short_input_header_error_count_low.yfilter != YFilter.not_set or
                                self.short_packet_error_count_high.yfilter != YFilter.not_set or
                                self.short_packet_error_count_low.yfilter != YFilter.not_set or
                                self.xbar_timeout_drop_count_high.yfilter != YFilter.not_set or
                                self.xbar_timeout_drop_count_low.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pkt-stat" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.asic_id.is_set or self.asic_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.asic_id.get_name_leafdata())
                            if (self.diagnostic_packet_count_high.is_set or self.diagnostic_packet_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.diagnostic_packet_count_high.get_name_leafdata())
                            if (self.diagnostic_packet_count_low.is_set or self.diagnostic_packet_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.diagnostic_packet_count_low.get_name_leafdata())
                            if (self.egress_channel_utilization_count_high.is_set or self.egress_channel_utilization_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.egress_channel_utilization_count_high.get_name_leafdata())
                            if (self.egress_channel_utilization_count_low.is_set or self.egress_channel_utilization_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.egress_channel_utilization_count_low.get_name_leafdata())
                            if (self.egress_packet_count_since_last_read_high.is_set or self.egress_packet_count_since_last_read_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.egress_packet_count_since_last_read_high.get_name_leafdata())
                            if (self.egress_packet_count_since_last_read_low.is_set or self.egress_packet_count_since_last_read_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.egress_packet_count_since_last_read_low.get_name_leafdata())
                            if (self.fpoedb_correctable_ecc_error_count_high.is_set or self.fpoedb_correctable_ecc_error_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fpoedb_correctable_ecc_error_count_high.get_name_leafdata())
                            if (self.fpoedb_correctable_ecc_error_count_low.is_set or self.fpoedb_correctable_ecc_error_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fpoedb_correctable_ecc_error_count_low.get_name_leafdata())
                            if (self.fpoedb_uncorrectable_ecc_error_count_high.is_set or self.fpoedb_uncorrectable_ecc_error_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fpoedb_uncorrectable_ecc_error_count_high.get_name_leafdata())
                            if (self.fpoedb_uncorrectable_ecc_error_count_low.is_set or self.fpoedb_uncorrectable_ecc_error_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fpoedb_uncorrectable_ecc_error_count_low.get_name_leafdata())
                            if (self.header_crc_error_count_high.is_set or self.header_crc_error_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.header_crc_error_count_high.get_name_leafdata())
                            if (self.header_crc_error_count_low.is_set or self.header_crc_error_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.header_crc_error_count_low.get_name_leafdata())
                            if (self.holdrop_count_high.is_set or self.holdrop_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.holdrop_count_high.get_name_leafdata())
                            if (self.holdrop_count_low.is_set or self.holdrop_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.holdrop_count_low.get_name_leafdata())
                            if (self.ingress_channel_utilization_count_high.is_set or self.ingress_channel_utilization_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ingress_channel_utilization_count_high.get_name_leafdata())
                            if (self.ingress_channel_utilization_count_low.is_set or self.ingress_channel_utilization_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ingress_channel_utilization_count_low.get_name_leafdata())
                            if (self.ingress_packet_count_since_last_read_high.is_set or self.ingress_packet_count_since_last_read_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ingress_packet_count_since_last_read_high.get_name_leafdata())
                            if (self.ingress_packet_count_since_last_read_low.is_set or self.ingress_packet_count_since_last_read_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ingress_packet_count_since_last_read_low.get_name_leafdata())
                            if (self.input_buffer_back_pressure_count_high.is_set or self.input_buffer_back_pressure_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.input_buffer_back_pressure_count_high.get_name_leafdata())
                            if (self.input_buffer_back_pressure_count_low.is_set or self.input_buffer_back_pressure_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.input_buffer_back_pressure_count_low.get_name_leafdata())
                            if (self.input_buffer_correctable_ecc_error_count_high.is_set or self.input_buffer_correctable_ecc_error_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.input_buffer_correctable_ecc_error_count_high.get_name_leafdata())
                            if (self.input_buffer_correctable_ecc_error_count_low.is_set or self.input_buffer_correctable_ecc_error_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.input_buffer_correctable_ecc_error_count_low.get_name_leafdata())
                            if (self.input_buffer_queued_packet_count_high.is_set or self.input_buffer_queued_packet_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.input_buffer_queued_packet_count_high.get_name_leafdata())
                            if (self.input_buffer_queued_packet_count_low.is_set or self.input_buffer_queued_packet_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.input_buffer_queued_packet_count_low.get_name_leafdata())
                            if (self.input_buffer_uncorrectable_ecc_error_count_high.is_set or self.input_buffer_uncorrectable_ecc_error_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.input_buffer_uncorrectable_ecc_error_count_high.get_name_leafdata())
                            if (self.input_buffer_uncorrectable_ecc_error_count_low.is_set or self.input_buffer_uncorrectable_ecc_error_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.input_buffer_uncorrectable_ecc_error_count_low.get_name_leafdata())
                            if (self.internal_error_count.is_set or self.internal_error_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.internal_error_count.get_name_leafdata())
                            if (self.null_fpoe_drop_count_high.is_set or self.null_fpoe_drop_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.null_fpoe_drop_count_high.get_name_leafdata())
                            if (self.null_fpoe_drop_count_low.is_set or self.null_fpoe_drop_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.null_fpoe_drop_count_low.get_name_leafdata())
                            if (self.output_buffer_back_pressure_count_high.is_set or self.output_buffer_back_pressure_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.output_buffer_back_pressure_count_high.get_name_leafdata())
                            if (self.output_buffer_back_pressure_count_low.is_set or self.output_buffer_back_pressure_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.output_buffer_back_pressure_count_low.get_name_leafdata())
                            if (self.output_buffer_correctable_ecc_error_count_high.is_set or self.output_buffer_correctable_ecc_error_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.output_buffer_correctable_ecc_error_count_high.get_name_leafdata())
                            if (self.output_buffer_correctable_ecc_error_count_low.is_set or self.output_buffer_correctable_ecc_error_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.output_buffer_correctable_ecc_error_count_low.get_name_leafdata())
                            if (self.output_buffer_queued_packet_count_high.is_set or self.output_buffer_queued_packet_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.output_buffer_queued_packet_count_high.get_name_leafdata())
                            if (self.output_buffer_queued_packet_count_low.is_set or self.output_buffer_queued_packet_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.output_buffer_queued_packet_count_low.get_name_leafdata())
                            if (self.output_buffer_uncorrectable_ecc_error_count_high.is_set or self.output_buffer_uncorrectable_ecc_error_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.output_buffer_uncorrectable_ecc_error_count_high.get_name_leafdata())
                            if (self.output_buffer_uncorrectable_ecc_error_count_low.is_set or self.output_buffer_uncorrectable_ecc_error_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.output_buffer_uncorrectable_ecc_error_count_low.get_name_leafdata())
                            if (self.packet_crc_error_count_high.is_set or self.packet_crc_error_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packet_crc_error_count_high.get_name_leafdata())
                            if (self.packet_crc_error_count_low.is_set or self.packet_crc_error_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packet_crc_error_count_low.get_name_leafdata())
                            if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.port.get_name_leafdata())
                            if (self.short_input_header_error_count_high.is_set or self.short_input_header_error_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.short_input_header_error_count_high.get_name_leafdata())
                            if (self.short_input_header_error_count_low.is_set or self.short_input_header_error_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.short_input_header_error_count_low.get_name_leafdata())
                            if (self.short_packet_error_count_high.is_set or self.short_packet_error_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.short_packet_error_count_high.get_name_leafdata())
                            if (self.short_packet_error_count_low.is_set or self.short_packet_error_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.short_packet_error_count_low.get_name_leafdata())
                            if (self.xbar_timeout_drop_count_high.is_set or self.xbar_timeout_drop_count_high.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.xbar_timeout_drop_count_high.get_name_leafdata())
                            if (self.xbar_timeout_drop_count_low.is_set or self.xbar_timeout_drop_count_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.xbar_timeout_drop_count_low.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "asic-id" or name == "diagnostic-packet-count-high" or name == "diagnostic-packet-count-low" or name == "egress-channel-utilization-count-high" or name == "egress-channel-utilization-count-low" or name == "egress-packet-count-since-last-read-high" or name == "egress-packet-count-since-last-read-low" or name == "fpoedb-correctable-ecc-error-count-high" or name == "fpoedb-correctable-ecc-error-count-low" or name == "fpoedb-uncorrectable-ecc-error-count-high" or name == "fpoedb-uncorrectable-ecc-error-count-low" or name == "header-crc-error-count-high" or name == "header-crc-error-count-low" or name == "holdrop-count-high" or name == "holdrop-count-low" or name == "ingress-channel-utilization-count-high" or name == "ingress-channel-utilization-count-low" or name == "ingress-packet-count-since-last-read-high" or name == "ingress-packet-count-since-last-read-low" or name == "input-buffer-back-pressure-count-high" or name == "input-buffer-back-pressure-count-low" or name == "input-buffer-correctable-ecc-error-count-high" or name == "input-buffer-correctable-ecc-error-count-low" or name == "input-buffer-queued-packet-count-high" or name == "input-buffer-queued-packet-count-low" or name == "input-buffer-uncorrectable-ecc-error-count-high" or name == "input-buffer-uncorrectable-ecc-error-count-low" or name == "internal-error-count" or name == "null-fpoe-drop-count-high" or name == "null-fpoe-drop-count-low" or name == "output-buffer-back-pressure-count-high" or name == "output-buffer-back-pressure-count-low" or name == "output-buffer-correctable-ecc-error-count-high" or name == "output-buffer-correctable-ecc-error-count-low" or name == "output-buffer-queued-packet-count-high" or name == "output-buffer-queued-packet-count-low" or name == "output-buffer-uncorrectable-ecc-error-count-high" or name == "output-buffer-uncorrectable-ecc-error-count-low" or name == "packet-crc-error-count-high" or name == "packet-crc-error-count-low" or name == "port" or name == "short-input-header-error-count-high" or name == "short-input-header-error-count-low" or name == "short-packet-error-count-high" or name == "short-packet-error-count-low" or name == "xbar-timeout-drop-count-high" or name == "xbar-timeout-drop-count-low"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "asic-id"):
                                self.asic_id = value
                                self.asic_id.value_namespace = name_space
                                self.asic_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "diagnostic-packet-count-high"):
                                self.diagnostic_packet_count_high = value
                                self.diagnostic_packet_count_high.value_namespace = name_space
                                self.diagnostic_packet_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "diagnostic-packet-count-low"):
                                self.diagnostic_packet_count_low = value
                                self.diagnostic_packet_count_low.value_namespace = name_space
                                self.diagnostic_packet_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "egress-channel-utilization-count-high"):
                                self.egress_channel_utilization_count_high = value
                                self.egress_channel_utilization_count_high.value_namespace = name_space
                                self.egress_channel_utilization_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "egress-channel-utilization-count-low"):
                                self.egress_channel_utilization_count_low = value
                                self.egress_channel_utilization_count_low.value_namespace = name_space
                                self.egress_channel_utilization_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "egress-packet-count-since-last-read-high"):
                                self.egress_packet_count_since_last_read_high = value
                                self.egress_packet_count_since_last_read_high.value_namespace = name_space
                                self.egress_packet_count_since_last_read_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "egress-packet-count-since-last-read-low"):
                                self.egress_packet_count_since_last_read_low = value
                                self.egress_packet_count_since_last_read_low.value_namespace = name_space
                                self.egress_packet_count_since_last_read_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "fpoedb-correctable-ecc-error-count-high"):
                                self.fpoedb_correctable_ecc_error_count_high = value
                                self.fpoedb_correctable_ecc_error_count_high.value_namespace = name_space
                                self.fpoedb_correctable_ecc_error_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "fpoedb-correctable-ecc-error-count-low"):
                                self.fpoedb_correctable_ecc_error_count_low = value
                                self.fpoedb_correctable_ecc_error_count_low.value_namespace = name_space
                                self.fpoedb_correctable_ecc_error_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "fpoedb-uncorrectable-ecc-error-count-high"):
                                self.fpoedb_uncorrectable_ecc_error_count_high = value
                                self.fpoedb_uncorrectable_ecc_error_count_high.value_namespace = name_space
                                self.fpoedb_uncorrectable_ecc_error_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "fpoedb-uncorrectable-ecc-error-count-low"):
                                self.fpoedb_uncorrectable_ecc_error_count_low = value
                                self.fpoedb_uncorrectable_ecc_error_count_low.value_namespace = name_space
                                self.fpoedb_uncorrectable_ecc_error_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "header-crc-error-count-high"):
                                self.header_crc_error_count_high = value
                                self.header_crc_error_count_high.value_namespace = name_space
                                self.header_crc_error_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "header-crc-error-count-low"):
                                self.header_crc_error_count_low = value
                                self.header_crc_error_count_low.value_namespace = name_space
                                self.header_crc_error_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "holdrop-count-high"):
                                self.holdrop_count_high = value
                                self.holdrop_count_high.value_namespace = name_space
                                self.holdrop_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "holdrop-count-low"):
                                self.holdrop_count_low = value
                                self.holdrop_count_low.value_namespace = name_space
                                self.holdrop_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "ingress-channel-utilization-count-high"):
                                self.ingress_channel_utilization_count_high = value
                                self.ingress_channel_utilization_count_high.value_namespace = name_space
                                self.ingress_channel_utilization_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "ingress-channel-utilization-count-low"):
                                self.ingress_channel_utilization_count_low = value
                                self.ingress_channel_utilization_count_low.value_namespace = name_space
                                self.ingress_channel_utilization_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "ingress-packet-count-since-last-read-high"):
                                self.ingress_packet_count_since_last_read_high = value
                                self.ingress_packet_count_since_last_read_high.value_namespace = name_space
                                self.ingress_packet_count_since_last_read_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "ingress-packet-count-since-last-read-low"):
                                self.ingress_packet_count_since_last_read_low = value
                                self.ingress_packet_count_since_last_read_low.value_namespace = name_space
                                self.ingress_packet_count_since_last_read_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "input-buffer-back-pressure-count-high"):
                                self.input_buffer_back_pressure_count_high = value
                                self.input_buffer_back_pressure_count_high.value_namespace = name_space
                                self.input_buffer_back_pressure_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "input-buffer-back-pressure-count-low"):
                                self.input_buffer_back_pressure_count_low = value
                                self.input_buffer_back_pressure_count_low.value_namespace = name_space
                                self.input_buffer_back_pressure_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "input-buffer-correctable-ecc-error-count-high"):
                                self.input_buffer_correctable_ecc_error_count_high = value
                                self.input_buffer_correctable_ecc_error_count_high.value_namespace = name_space
                                self.input_buffer_correctable_ecc_error_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "input-buffer-correctable-ecc-error-count-low"):
                                self.input_buffer_correctable_ecc_error_count_low = value
                                self.input_buffer_correctable_ecc_error_count_low.value_namespace = name_space
                                self.input_buffer_correctable_ecc_error_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "input-buffer-queued-packet-count-high"):
                                self.input_buffer_queued_packet_count_high = value
                                self.input_buffer_queued_packet_count_high.value_namespace = name_space
                                self.input_buffer_queued_packet_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "input-buffer-queued-packet-count-low"):
                                self.input_buffer_queued_packet_count_low = value
                                self.input_buffer_queued_packet_count_low.value_namespace = name_space
                                self.input_buffer_queued_packet_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "input-buffer-uncorrectable-ecc-error-count-high"):
                                self.input_buffer_uncorrectable_ecc_error_count_high = value
                                self.input_buffer_uncorrectable_ecc_error_count_high.value_namespace = name_space
                                self.input_buffer_uncorrectable_ecc_error_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "input-buffer-uncorrectable-ecc-error-count-low"):
                                self.input_buffer_uncorrectable_ecc_error_count_low = value
                                self.input_buffer_uncorrectable_ecc_error_count_low.value_namespace = name_space
                                self.input_buffer_uncorrectable_ecc_error_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "internal-error-count"):
                                self.internal_error_count = value
                                self.internal_error_count.value_namespace = name_space
                                self.internal_error_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "null-fpoe-drop-count-high"):
                                self.null_fpoe_drop_count_high = value
                                self.null_fpoe_drop_count_high.value_namespace = name_space
                                self.null_fpoe_drop_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "null-fpoe-drop-count-low"):
                                self.null_fpoe_drop_count_low = value
                                self.null_fpoe_drop_count_low.value_namespace = name_space
                                self.null_fpoe_drop_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "output-buffer-back-pressure-count-high"):
                                self.output_buffer_back_pressure_count_high = value
                                self.output_buffer_back_pressure_count_high.value_namespace = name_space
                                self.output_buffer_back_pressure_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "output-buffer-back-pressure-count-low"):
                                self.output_buffer_back_pressure_count_low = value
                                self.output_buffer_back_pressure_count_low.value_namespace = name_space
                                self.output_buffer_back_pressure_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "output-buffer-correctable-ecc-error-count-high"):
                                self.output_buffer_correctable_ecc_error_count_high = value
                                self.output_buffer_correctable_ecc_error_count_high.value_namespace = name_space
                                self.output_buffer_correctable_ecc_error_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "output-buffer-correctable-ecc-error-count-low"):
                                self.output_buffer_correctable_ecc_error_count_low = value
                                self.output_buffer_correctable_ecc_error_count_low.value_namespace = name_space
                                self.output_buffer_correctable_ecc_error_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "output-buffer-queued-packet-count-high"):
                                self.output_buffer_queued_packet_count_high = value
                                self.output_buffer_queued_packet_count_high.value_namespace = name_space
                                self.output_buffer_queued_packet_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "output-buffer-queued-packet-count-low"):
                                self.output_buffer_queued_packet_count_low = value
                                self.output_buffer_queued_packet_count_low.value_namespace = name_space
                                self.output_buffer_queued_packet_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "output-buffer-uncorrectable-ecc-error-count-high"):
                                self.output_buffer_uncorrectable_ecc_error_count_high = value
                                self.output_buffer_uncorrectable_ecc_error_count_high.value_namespace = name_space
                                self.output_buffer_uncorrectable_ecc_error_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "output-buffer-uncorrectable-ecc-error-count-low"):
                                self.output_buffer_uncorrectable_ecc_error_count_low = value
                                self.output_buffer_uncorrectable_ecc_error_count_low.value_namespace = name_space
                                self.output_buffer_uncorrectable_ecc_error_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "packet-crc-error-count-high"):
                                self.packet_crc_error_count_high = value
                                self.packet_crc_error_count_high.value_namespace = name_space
                                self.packet_crc_error_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "packet-crc-error-count-low"):
                                self.packet_crc_error_count_low = value
                                self.packet_crc_error_count_low.value_namespace = name_space
                                self.packet_crc_error_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "port"):
                                self.port = value
                                self.port.value_namespace = name_space
                                self.port.value_namespace_prefix = name_space_prefix
                            if(value_path == "short-input-header-error-count-high"):
                                self.short_input_header_error_count_high = value
                                self.short_input_header_error_count_high.value_namespace = name_space
                                self.short_input_header_error_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "short-input-header-error-count-low"):
                                self.short_input_header_error_count_low = value
                                self.short_input_header_error_count_low.value_namespace = name_space
                                self.short_input_header_error_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "short-packet-error-count-high"):
                                self.short_packet_error_count_high = value
                                self.short_packet_error_count_high.value_namespace = name_space
                                self.short_packet_error_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "short-packet-error-count-low"):
                                self.short_packet_error_count_low = value
                                self.short_packet_error_count_low.value_namespace = name_space
                                self.short_packet_error_count_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "xbar-timeout-drop-count-high"):
                                self.xbar_timeout_drop_count_high = value
                                self.xbar_timeout_drop_count_high.value_namespace = name_space
                                self.xbar_timeout_drop_count_high.value_namespace_prefix = name_space_prefix
                            if(value_path == "xbar-timeout-drop-count-low"):
                                self.xbar_timeout_drop_count_low = value
                                self.xbar_timeout_drop_count_low.value_namespace = name_space
                                self.xbar_timeout_drop_count_low.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.pkt_stat:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.pkt_stat:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "pkt-stats" + path_buffer

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

                        if (child_yang_name == "pkt-stat"):
                            for c in self.pkt_stat:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = CrossBarStats.Nodes.Node.CrossBarTable.PktStats.PktStat()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.pkt_stat.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "pkt-stat"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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

                        self.sm15_stat = YList(self)

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
                                    super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats, self).__setattr__(name, value)


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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("asic_id",
                                            "internal_err_cnt",
                                            "port") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat, self).__setattr__(name, value)


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

                                self.ack_wait_cnt = YLeaf(YType.uint64, "ack-wait-cnt")

                                self.dest_drop_pkt_cnt = YLeaf(YType.uint64, "dest-drop-pkt-cnt")

                                self.dest_src_pkt_cnt = YLeaf(YType.uint64, "dest-src-pkt-cnt")

                                self.rcv_pkt_cnt = YLeaf(YType.uint64, "rcv-pkt-cnt")

                                self.rx_drop_pkt_cnt = YLeaf(YType.uint64, "rx-drop-pkt-cnt")

                                self.rx_fabric_to_cnt = YLeaf(YType.uint64, "rx-fabric-to-cnt")

                                self.src_dest_pkt_cnt = YLeaf(YType.uint64, "src-dest-pkt-cnt")

                                self.tx_pkt_cnt = YLeaf(YType.uint64, "tx-pkt-cnt")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ack_wait_cnt",
                                                "dest_drop_pkt_cnt",
                                                "dest_src_pkt_cnt",
                                                "rcv_pkt_cnt",
                                                "rx_drop_pkt_cnt",
                                                "rx_fabric_to_cnt",
                                                "src_dest_pkt_cnt",
                                                "tx_pkt_cnt") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua0Stats, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua0Stats, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ack_wait_cnt.is_set or
                                    self.dest_drop_pkt_cnt.is_set or
                                    self.dest_src_pkt_cnt.is_set or
                                    self.rcv_pkt_cnt.is_set or
                                    self.rx_drop_pkt_cnt.is_set or
                                    self.rx_fabric_to_cnt.is_set or
                                    self.src_dest_pkt_cnt.is_set or
                                    self.tx_pkt_cnt.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ack_wait_cnt.yfilter != YFilter.not_set or
                                    self.dest_drop_pkt_cnt.yfilter != YFilter.not_set or
                                    self.dest_src_pkt_cnt.yfilter != YFilter.not_set or
                                    self.rcv_pkt_cnt.yfilter != YFilter.not_set or
                                    self.rx_drop_pkt_cnt.yfilter != YFilter.not_set or
                                    self.rx_fabric_to_cnt.yfilter != YFilter.not_set or
                                    self.src_dest_pkt_cnt.yfilter != YFilter.not_set or
                                    self.tx_pkt_cnt.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ua0-stats" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ack_wait_cnt.is_set or self.ack_wait_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ack_wait_cnt.get_name_leafdata())
                                if (self.dest_drop_pkt_cnt.is_set or self.dest_drop_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dest_drop_pkt_cnt.get_name_leafdata())
                                if (self.dest_src_pkt_cnt.is_set or self.dest_src_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dest_src_pkt_cnt.get_name_leafdata())
                                if (self.rcv_pkt_cnt.is_set or self.rcv_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rcv_pkt_cnt.get_name_leafdata())
                                if (self.rx_drop_pkt_cnt.is_set or self.rx_drop_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_drop_pkt_cnt.get_name_leafdata())
                                if (self.rx_fabric_to_cnt.is_set or self.rx_fabric_to_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_fabric_to_cnt.get_name_leafdata())
                                if (self.src_dest_pkt_cnt.is_set or self.src_dest_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.src_dest_pkt_cnt.get_name_leafdata())
                                if (self.tx_pkt_cnt.is_set or self.tx_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_pkt_cnt.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ack-wait-cnt" or name == "dest-drop-pkt-cnt" or name == "dest-src-pkt-cnt" or name == "rcv-pkt-cnt" or name == "rx-drop-pkt-cnt" or name == "rx-fabric-to-cnt" or name == "src-dest-pkt-cnt" or name == "tx-pkt-cnt"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ack-wait-cnt"):
                                    self.ack_wait_cnt = value
                                    self.ack_wait_cnt.value_namespace = name_space
                                    self.ack_wait_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "dest-drop-pkt-cnt"):
                                    self.dest_drop_pkt_cnt = value
                                    self.dest_drop_pkt_cnt.value_namespace = name_space
                                    self.dest_drop_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "dest-src-pkt-cnt"):
                                    self.dest_src_pkt_cnt = value
                                    self.dest_src_pkt_cnt.value_namespace = name_space
                                    self.dest_src_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rcv-pkt-cnt"):
                                    self.rcv_pkt_cnt = value
                                    self.rcv_pkt_cnt.value_namespace = name_space
                                    self.rcv_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-drop-pkt-cnt"):
                                    self.rx_drop_pkt_cnt = value
                                    self.rx_drop_pkt_cnt.value_namespace = name_space
                                    self.rx_drop_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-fabric-to-cnt"):
                                    self.rx_fabric_to_cnt = value
                                    self.rx_fabric_to_cnt.value_namespace = name_space
                                    self.rx_fabric_to_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "src-dest-pkt-cnt"):
                                    self.src_dest_pkt_cnt = value
                                    self.src_dest_pkt_cnt.value_namespace = name_space
                                    self.src_dest_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-pkt-cnt"):
                                    self.tx_pkt_cnt = value
                                    self.tx_pkt_cnt.value_namespace = name_space
                                    self.tx_pkt_cnt.value_namespace_prefix = name_space_prefix


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

                                self.ack_wait_cnt = YLeaf(YType.uint64, "ack-wait-cnt")

                                self.dest_drop_pkt_cnt = YLeaf(YType.uint64, "dest-drop-pkt-cnt")

                                self.dest_src_pkt_cnt = YLeaf(YType.uint64, "dest-src-pkt-cnt")

                                self.rcv_pkt_cnt = YLeaf(YType.uint64, "rcv-pkt-cnt")

                                self.rx_drop_pkt_cnt = YLeaf(YType.uint64, "rx-drop-pkt-cnt")

                                self.rx_fabric_to_cnt = YLeaf(YType.uint64, "rx-fabric-to-cnt")

                                self.src_dest_pkt_cnt = YLeaf(YType.uint64, "src-dest-pkt-cnt")

                                self.tx_pkt_cnt = YLeaf(YType.uint64, "tx-pkt-cnt")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ack_wait_cnt",
                                                "dest_drop_pkt_cnt",
                                                "dest_src_pkt_cnt",
                                                "rcv_pkt_cnt",
                                                "rx_drop_pkt_cnt",
                                                "rx_fabric_to_cnt",
                                                "src_dest_pkt_cnt",
                                                "tx_pkt_cnt") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua1Stats, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua1Stats, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ack_wait_cnt.is_set or
                                    self.dest_drop_pkt_cnt.is_set or
                                    self.dest_src_pkt_cnt.is_set or
                                    self.rcv_pkt_cnt.is_set or
                                    self.rx_drop_pkt_cnt.is_set or
                                    self.rx_fabric_to_cnt.is_set or
                                    self.src_dest_pkt_cnt.is_set or
                                    self.tx_pkt_cnt.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ack_wait_cnt.yfilter != YFilter.not_set or
                                    self.dest_drop_pkt_cnt.yfilter != YFilter.not_set or
                                    self.dest_src_pkt_cnt.yfilter != YFilter.not_set or
                                    self.rcv_pkt_cnt.yfilter != YFilter.not_set or
                                    self.rx_drop_pkt_cnt.yfilter != YFilter.not_set or
                                    self.rx_fabric_to_cnt.yfilter != YFilter.not_set or
                                    self.src_dest_pkt_cnt.yfilter != YFilter.not_set or
                                    self.tx_pkt_cnt.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ua1-stats" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ack_wait_cnt.is_set or self.ack_wait_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ack_wait_cnt.get_name_leafdata())
                                if (self.dest_drop_pkt_cnt.is_set or self.dest_drop_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dest_drop_pkt_cnt.get_name_leafdata())
                                if (self.dest_src_pkt_cnt.is_set or self.dest_src_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dest_src_pkt_cnt.get_name_leafdata())
                                if (self.rcv_pkt_cnt.is_set or self.rcv_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rcv_pkt_cnt.get_name_leafdata())
                                if (self.rx_drop_pkt_cnt.is_set or self.rx_drop_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_drop_pkt_cnt.get_name_leafdata())
                                if (self.rx_fabric_to_cnt.is_set or self.rx_fabric_to_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_fabric_to_cnt.get_name_leafdata())
                                if (self.src_dest_pkt_cnt.is_set or self.src_dest_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.src_dest_pkt_cnt.get_name_leafdata())
                                if (self.tx_pkt_cnt.is_set or self.tx_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_pkt_cnt.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ack-wait-cnt" or name == "dest-drop-pkt-cnt" or name == "dest-src-pkt-cnt" or name == "rcv-pkt-cnt" or name == "rx-drop-pkt-cnt" or name == "rx-fabric-to-cnt" or name == "src-dest-pkt-cnt" or name == "tx-pkt-cnt"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ack-wait-cnt"):
                                    self.ack_wait_cnt = value
                                    self.ack_wait_cnt.value_namespace = name_space
                                    self.ack_wait_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "dest-drop-pkt-cnt"):
                                    self.dest_drop_pkt_cnt = value
                                    self.dest_drop_pkt_cnt.value_namespace = name_space
                                    self.dest_drop_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "dest-src-pkt-cnt"):
                                    self.dest_src_pkt_cnt = value
                                    self.dest_src_pkt_cnt.value_namespace = name_space
                                    self.dest_src_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rcv-pkt-cnt"):
                                    self.rcv_pkt_cnt = value
                                    self.rcv_pkt_cnt.value_namespace = name_space
                                    self.rcv_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-drop-pkt-cnt"):
                                    self.rx_drop_pkt_cnt = value
                                    self.rx_drop_pkt_cnt.value_namespace = name_space
                                    self.rx_drop_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-fabric-to-cnt"):
                                    self.rx_fabric_to_cnt = value
                                    self.rx_fabric_to_cnt.value_namespace = name_space
                                    self.rx_fabric_to_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "src-dest-pkt-cnt"):
                                    self.src_dest_pkt_cnt = value
                                    self.src_dest_pkt_cnt.value_namespace = name_space
                                    self.src_dest_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-pkt-cnt"):
                                    self.tx_pkt_cnt = value
                                    self.tx_pkt_cnt.value_namespace = name_space
                                    self.tx_pkt_cnt.value_namespace_prefix = name_space_prefix


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

                                self.ack_wait_cnt = YLeaf(YType.uint64, "ack-wait-cnt")

                                self.dest_drop_pkt_cnt = YLeaf(YType.uint64, "dest-drop-pkt-cnt")

                                self.dest_src_pkt_cnt = YLeaf(YType.uint64, "dest-src-pkt-cnt")

                                self.rcv_pkt_cnt = YLeaf(YType.uint64, "rcv-pkt-cnt")

                                self.rx_drop_pkt_cnt = YLeaf(YType.uint64, "rx-drop-pkt-cnt")

                                self.rx_fabric_to_cnt = YLeaf(YType.uint64, "rx-fabric-to-cnt")

                                self.src_dest_pkt_cnt = YLeaf(YType.uint64, "src-dest-pkt-cnt")

                                self.tx_pkt_cnt = YLeaf(YType.uint64, "tx-pkt-cnt")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ack_wait_cnt",
                                                "dest_drop_pkt_cnt",
                                                "dest_src_pkt_cnt",
                                                "rcv_pkt_cnt",
                                                "rx_drop_pkt_cnt",
                                                "rx_fabric_to_cnt",
                                                "src_dest_pkt_cnt",
                                                "tx_pkt_cnt") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua2Stats, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua2Stats, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ack_wait_cnt.is_set or
                                    self.dest_drop_pkt_cnt.is_set or
                                    self.dest_src_pkt_cnt.is_set or
                                    self.rcv_pkt_cnt.is_set or
                                    self.rx_drop_pkt_cnt.is_set or
                                    self.rx_fabric_to_cnt.is_set or
                                    self.src_dest_pkt_cnt.is_set or
                                    self.tx_pkt_cnt.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ack_wait_cnt.yfilter != YFilter.not_set or
                                    self.dest_drop_pkt_cnt.yfilter != YFilter.not_set or
                                    self.dest_src_pkt_cnt.yfilter != YFilter.not_set or
                                    self.rcv_pkt_cnt.yfilter != YFilter.not_set or
                                    self.rx_drop_pkt_cnt.yfilter != YFilter.not_set or
                                    self.rx_fabric_to_cnt.yfilter != YFilter.not_set or
                                    self.src_dest_pkt_cnt.yfilter != YFilter.not_set or
                                    self.tx_pkt_cnt.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ua2-stats" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ack_wait_cnt.is_set or self.ack_wait_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ack_wait_cnt.get_name_leafdata())
                                if (self.dest_drop_pkt_cnt.is_set or self.dest_drop_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dest_drop_pkt_cnt.get_name_leafdata())
                                if (self.dest_src_pkt_cnt.is_set or self.dest_src_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dest_src_pkt_cnt.get_name_leafdata())
                                if (self.rcv_pkt_cnt.is_set or self.rcv_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rcv_pkt_cnt.get_name_leafdata())
                                if (self.rx_drop_pkt_cnt.is_set or self.rx_drop_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_drop_pkt_cnt.get_name_leafdata())
                                if (self.rx_fabric_to_cnt.is_set or self.rx_fabric_to_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_fabric_to_cnt.get_name_leafdata())
                                if (self.src_dest_pkt_cnt.is_set or self.src_dest_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.src_dest_pkt_cnt.get_name_leafdata())
                                if (self.tx_pkt_cnt.is_set or self.tx_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_pkt_cnt.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ack-wait-cnt" or name == "dest-drop-pkt-cnt" or name == "dest-src-pkt-cnt" or name == "rcv-pkt-cnt" or name == "rx-drop-pkt-cnt" or name == "rx-fabric-to-cnt" or name == "src-dest-pkt-cnt" or name == "tx-pkt-cnt"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ack-wait-cnt"):
                                    self.ack_wait_cnt = value
                                    self.ack_wait_cnt.value_namespace = name_space
                                    self.ack_wait_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "dest-drop-pkt-cnt"):
                                    self.dest_drop_pkt_cnt = value
                                    self.dest_drop_pkt_cnt.value_namespace = name_space
                                    self.dest_drop_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "dest-src-pkt-cnt"):
                                    self.dest_src_pkt_cnt = value
                                    self.dest_src_pkt_cnt.value_namespace = name_space
                                    self.dest_src_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rcv-pkt-cnt"):
                                    self.rcv_pkt_cnt = value
                                    self.rcv_pkt_cnt.value_namespace = name_space
                                    self.rcv_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-drop-pkt-cnt"):
                                    self.rx_drop_pkt_cnt = value
                                    self.rx_drop_pkt_cnt.value_namespace = name_space
                                    self.rx_drop_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-fabric-to-cnt"):
                                    self.rx_fabric_to_cnt = value
                                    self.rx_fabric_to_cnt.value_namespace = name_space
                                    self.rx_fabric_to_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "src-dest-pkt-cnt"):
                                    self.src_dest_pkt_cnt = value
                                    self.src_dest_pkt_cnt.value_namespace = name_space
                                    self.src_dest_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-pkt-cnt"):
                                    self.tx_pkt_cnt = value
                                    self.tx_pkt_cnt.value_namespace = name_space
                                    self.tx_pkt_cnt.value_namespace_prefix = name_space_prefix


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

                                self.dest_drop_pkt_cnt = YLeaf(YType.uint64, "dest-drop-pkt-cnt")

                                self.dest_src_pkt_cnt = YLeaf(YType.uint64, "dest-src-pkt-cnt")

                                self.rcv_pkt_cnt = YLeaf(YType.uint64, "rcv-pkt-cnt")

                                self.rx_drop_pkt_cnt = YLeaf(YType.uint64, "rx-drop-pkt-cnt")

                                self.rx_fabric_to_cnt = YLeaf(YType.uint64, "rx-fabric-to-cnt")

                                self.rx_hol_to_cnt = YLeaf(YType.uint64, "rx-hol-to-cnt")

                                self.rx_re_transmit_cnt = YLeaf(YType.uint64, "rx-re-transmit-cnt")

                                self.src_dest_pkt_cnt = YLeaf(YType.uint64, "src-dest-pkt-cnt")

                                self.tx_pkt_cnt = YLeaf(YType.uint64, "tx-pkt-cnt")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("dest_drop_pkt_cnt",
                                                "dest_src_pkt_cnt",
                                                "rcv_pkt_cnt",
                                                "rx_drop_pkt_cnt",
                                                "rx_fabric_to_cnt",
                                                "rx_hol_to_cnt",
                                                "rx_re_transmit_cnt",
                                                "src_dest_pkt_cnt",
                                                "tx_pkt_cnt") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.MaStats, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.MaStats, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.dest_drop_pkt_cnt.is_set or
                                    self.dest_src_pkt_cnt.is_set or
                                    self.rcv_pkt_cnt.is_set or
                                    self.rx_drop_pkt_cnt.is_set or
                                    self.rx_fabric_to_cnt.is_set or
                                    self.rx_hol_to_cnt.is_set or
                                    self.rx_re_transmit_cnt.is_set or
                                    self.src_dest_pkt_cnt.is_set or
                                    self.tx_pkt_cnt.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.dest_drop_pkt_cnt.yfilter != YFilter.not_set or
                                    self.dest_src_pkt_cnt.yfilter != YFilter.not_set or
                                    self.rcv_pkt_cnt.yfilter != YFilter.not_set or
                                    self.rx_drop_pkt_cnt.yfilter != YFilter.not_set or
                                    self.rx_fabric_to_cnt.yfilter != YFilter.not_set or
                                    self.rx_hol_to_cnt.yfilter != YFilter.not_set or
                                    self.rx_re_transmit_cnt.yfilter != YFilter.not_set or
                                    self.src_dest_pkt_cnt.yfilter != YFilter.not_set or
                                    self.tx_pkt_cnt.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ma-stats" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.dest_drop_pkt_cnt.is_set or self.dest_drop_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dest_drop_pkt_cnt.get_name_leafdata())
                                if (self.dest_src_pkt_cnt.is_set or self.dest_src_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dest_src_pkt_cnt.get_name_leafdata())
                                if (self.rcv_pkt_cnt.is_set or self.rcv_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rcv_pkt_cnt.get_name_leafdata())
                                if (self.rx_drop_pkt_cnt.is_set or self.rx_drop_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_drop_pkt_cnt.get_name_leafdata())
                                if (self.rx_fabric_to_cnt.is_set or self.rx_fabric_to_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_fabric_to_cnt.get_name_leafdata())
                                if (self.rx_hol_to_cnt.is_set or self.rx_hol_to_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_hol_to_cnt.get_name_leafdata())
                                if (self.rx_re_transmit_cnt.is_set or self.rx_re_transmit_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_re_transmit_cnt.get_name_leafdata())
                                if (self.src_dest_pkt_cnt.is_set or self.src_dest_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.src_dest_pkt_cnt.get_name_leafdata())
                                if (self.tx_pkt_cnt.is_set or self.tx_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_pkt_cnt.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "dest-drop-pkt-cnt" or name == "dest-src-pkt-cnt" or name == "rcv-pkt-cnt" or name == "rx-drop-pkt-cnt" or name == "rx-fabric-to-cnt" or name == "rx-hol-to-cnt" or name == "rx-re-transmit-cnt" or name == "src-dest-pkt-cnt" or name == "tx-pkt-cnt"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "dest-drop-pkt-cnt"):
                                    self.dest_drop_pkt_cnt = value
                                    self.dest_drop_pkt_cnt.value_namespace = name_space
                                    self.dest_drop_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "dest-src-pkt-cnt"):
                                    self.dest_src_pkt_cnt = value
                                    self.dest_src_pkt_cnt.value_namespace = name_space
                                    self.dest_src_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rcv-pkt-cnt"):
                                    self.rcv_pkt_cnt = value
                                    self.rcv_pkt_cnt.value_namespace = name_space
                                    self.rcv_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-drop-pkt-cnt"):
                                    self.rx_drop_pkt_cnt = value
                                    self.rx_drop_pkt_cnt.value_namespace = name_space
                                    self.rx_drop_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-fabric-to-cnt"):
                                    self.rx_fabric_to_cnt = value
                                    self.rx_fabric_to_cnt.value_namespace = name_space
                                    self.rx_fabric_to_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-hol-to-cnt"):
                                    self.rx_hol_to_cnt = value
                                    self.rx_hol_to_cnt.value_namespace = name_space
                                    self.rx_hol_to_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-re-transmit-cnt"):
                                    self.rx_re_transmit_cnt = value
                                    self.rx_re_transmit_cnt.value_namespace = name_space
                                    self.rx_re_transmit_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "src-dest-pkt-cnt"):
                                    self.src_dest_pkt_cnt = value
                                    self.src_dest_pkt_cnt.value_namespace = name_space
                                    self.src_dest_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-pkt-cnt"):
                                    self.tx_pkt_cnt = value
                                    self.tx_pkt_cnt.value_namespace = name_space
                                    self.tx_pkt_cnt.value_namespace_prefix = name_space_prefix


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

                                self.dest_drop_pkt_cnt = YLeaf(YType.uint64, "dest-drop-pkt-cnt")

                                self.dest_src_pkt_cnt = YLeaf(YType.uint64, "dest-src-pkt-cnt")

                                self.rcv_pkt_cnt = YLeaf(YType.uint64, "rcv-pkt-cnt")

                                self.rx_drop_pkt_cnt = YLeaf(YType.uint64, "rx-drop-pkt-cnt")

                                self.src_dest_pkt_cnt = YLeaf(YType.uint64, "src-dest-pkt-cnt")

                                self.tx_pkt_cnt = YLeaf(YType.uint64, "tx-pkt-cnt")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("dest_drop_pkt_cnt",
                                                "dest_src_pkt_cnt",
                                                "rcv_pkt_cnt",
                                                "rx_drop_pkt_cnt",
                                                "src_dest_pkt_cnt",
                                                "tx_pkt_cnt") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.CaStats, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.CaStats, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.dest_drop_pkt_cnt.is_set or
                                    self.dest_src_pkt_cnt.is_set or
                                    self.rcv_pkt_cnt.is_set or
                                    self.rx_drop_pkt_cnt.is_set or
                                    self.src_dest_pkt_cnt.is_set or
                                    self.tx_pkt_cnt.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.dest_drop_pkt_cnt.yfilter != YFilter.not_set or
                                    self.dest_src_pkt_cnt.yfilter != YFilter.not_set or
                                    self.rcv_pkt_cnt.yfilter != YFilter.not_set or
                                    self.rx_drop_pkt_cnt.yfilter != YFilter.not_set or
                                    self.src_dest_pkt_cnt.yfilter != YFilter.not_set or
                                    self.tx_pkt_cnt.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ca-stats" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.dest_drop_pkt_cnt.is_set or self.dest_drop_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dest_drop_pkt_cnt.get_name_leafdata())
                                if (self.dest_src_pkt_cnt.is_set or self.dest_src_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dest_src_pkt_cnt.get_name_leafdata())
                                if (self.rcv_pkt_cnt.is_set or self.rcv_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rcv_pkt_cnt.get_name_leafdata())
                                if (self.rx_drop_pkt_cnt.is_set or self.rx_drop_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rx_drop_pkt_cnt.get_name_leafdata())
                                if (self.src_dest_pkt_cnt.is_set or self.src_dest_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.src_dest_pkt_cnt.get_name_leafdata())
                                if (self.tx_pkt_cnt.is_set or self.tx_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tx_pkt_cnt.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "dest-drop-pkt-cnt" or name == "dest-src-pkt-cnt" or name == "rcv-pkt-cnt" or name == "rx-drop-pkt-cnt" or name == "src-dest-pkt-cnt" or name == "tx-pkt-cnt"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "dest-drop-pkt-cnt"):
                                    self.dest_drop_pkt_cnt = value
                                    self.dest_drop_pkt_cnt.value_namespace = name_space
                                    self.dest_drop_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "dest-src-pkt-cnt"):
                                    self.dest_src_pkt_cnt = value
                                    self.dest_src_pkt_cnt.value_namespace = name_space
                                    self.dest_src_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rcv-pkt-cnt"):
                                    self.rcv_pkt_cnt = value
                                    self.rcv_pkt_cnt.value_namespace = name_space
                                    self.rcv_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rx-drop-pkt-cnt"):
                                    self.rx_drop_pkt_cnt = value
                                    self.rx_drop_pkt_cnt.value_namespace = name_space
                                    self.rx_drop_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "src-dest-pkt-cnt"):
                                    self.src_dest_pkt_cnt = value
                                    self.src_dest_pkt_cnt.value_namespace = name_space
                                    self.src_dest_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "tx-pkt-cnt"):
                                    self.tx_pkt_cnt = value
                                    self.tx_pkt_cnt.value_namespace = name_space
                                    self.tx_pkt_cnt.value_namespace_prefix = name_space_prefix


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

                                self.total_calc_rate = YLeaf(YType.uint64, "total-calc-rate")

                                self.total_rate1_cnt = YLeaf(YType.uint64, "total-rate1-cnt")

                                self.total_rate2_cnt = YLeaf(YType.uint64, "total-rate2-cnt")

                                self.total_rate3_cnt = YLeaf(YType.uint64, "total-rate3-cnt")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("total_calc_rate",
                                                "total_rate1_cnt",
                                                "total_rate2_cnt",
                                                "total_rate3_cnt") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiStats, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiStats, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.total_calc_rate.is_set or
                                    self.total_rate1_cnt.is_set or
                                    self.total_rate2_cnt.is_set or
                                    self.total_rate3_cnt.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.total_calc_rate.yfilter != YFilter.not_set or
                                    self.total_rate1_cnt.yfilter != YFilter.not_set or
                                    self.total_rate2_cnt.yfilter != YFilter.not_set or
                                    self.total_rate3_cnt.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pi-stats" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.total_calc_rate.is_set or self.total_calc_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total_calc_rate.get_name_leafdata())
                                if (self.total_rate1_cnt.is_set or self.total_rate1_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total_rate1_cnt.get_name_leafdata())
                                if (self.total_rate2_cnt.is_set or self.total_rate2_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total_rate2_cnt.get_name_leafdata())
                                if (self.total_rate3_cnt.is_set or self.total_rate3_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total_rate3_cnt.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "total-calc-rate" or name == "total-rate1-cnt" or name == "total-rate2-cnt" or name == "total-rate3-cnt"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "total-calc-rate"):
                                    self.total_calc_rate = value
                                    self.total_calc_rate.value_namespace = name_space
                                    self.total_calc_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "total-rate1-cnt"):
                                    self.total_rate1_cnt = value
                                    self.total_rate1_cnt.value_namespace = name_space
                                    self.total_rate1_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "total-rate2-cnt"):
                                    self.total_rate2_cnt = value
                                    self.total_rate2_cnt.value_namespace = name_space
                                    self.total_rate2_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "total-rate3-cnt"):
                                    self.total_rate3_cnt = value
                                    self.total_rate3_cnt.value_namespace = name_space
                                    self.total_rate3_cnt.value_namespace_prefix = name_space_prefix


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

                                self.mc2uc_preempt_cnt = YLeaf(YType.uint64, "mc2uc-preempt-cnt")

                                self.total_calc_rate = YLeaf(YType.uint64, "total-calc-rate")

                                self.total_rate1_cnt = YLeaf(YType.uint64, "total-rate1-cnt")

                                self.total_rate2_cnt = YLeaf(YType.uint64, "total-rate2-cnt")

                                self.total_rate3_cnt = YLeaf(YType.uint64, "total-rate3-cnt")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("mc2uc_preempt_cnt",
                                                "total_calc_rate",
                                                "total_rate1_cnt",
                                                "total_rate2_cnt",
                                                "total_rate3_cnt") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeStats, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeStats, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.mc2uc_preempt_cnt.is_set or
                                    self.total_calc_rate.is_set or
                                    self.total_rate1_cnt.is_set or
                                    self.total_rate2_cnt.is_set or
                                    self.total_rate3_cnt.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.mc2uc_preempt_cnt.yfilter != YFilter.not_set or
                                    self.total_calc_rate.yfilter != YFilter.not_set or
                                    self.total_rate1_cnt.yfilter != YFilter.not_set or
                                    self.total_rate2_cnt.yfilter != YFilter.not_set or
                                    self.total_rate3_cnt.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pe-stats" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.mc2uc_preempt_cnt.is_set or self.mc2uc_preempt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mc2uc_preempt_cnt.get_name_leafdata())
                                if (self.total_calc_rate.is_set or self.total_calc_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total_calc_rate.get_name_leafdata())
                                if (self.total_rate1_cnt.is_set or self.total_rate1_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total_rate1_cnt.get_name_leafdata())
                                if (self.total_rate2_cnt.is_set or self.total_rate2_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total_rate2_cnt.get_name_leafdata())
                                if (self.total_rate3_cnt.is_set or self.total_rate3_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total_rate3_cnt.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "mc2uc-preempt-cnt" or name == "total-calc-rate" or name == "total-rate1-cnt" or name == "total-rate2-cnt" or name == "total-rate3-cnt"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "mc2uc-preempt-cnt"):
                                    self.mc2uc_preempt_cnt = value
                                    self.mc2uc_preempt_cnt.value_namespace = name_space
                                    self.mc2uc_preempt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "total-calc-rate"):
                                    self.total_calc_rate = value
                                    self.total_calc_rate.value_namespace = name_space
                                    self.total_calc_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "total-rate1-cnt"):
                                    self.total_rate1_cnt = value
                                    self.total_rate1_cnt.value_namespace = name_space
                                    self.total_rate1_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "total-rate2-cnt"):
                                    self.total_rate2_cnt = value
                                    self.total_rate2_cnt.value_namespace = name_space
                                    self.total_rate2_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "total-rate3-cnt"):
                                    self.total_rate3_cnt = value
                                    self.total_rate3_cnt.value_namespace = name_space
                                    self.total_rate3_cnt.value_namespace_prefix = name_space_prefix


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("calc_rate",
                                                "cpp_head_drop_pkt_cnt",
                                                "crc_stomp_pkt_cnt",
                                                "diag_pkt_cnt",
                                                "fpoe_mem_ecc_1bit_err_cnt",
                                                "fpoe_mem_ecc_2bit_err_cnt",
                                                "in_coming_pkt_err_cnt",
                                                "line_err_drp_pkt",
                                                "line_s_written_in_mem0",
                                                "line_s_written_in_mem1",
                                                "line_s_written_in_mem2",
                                                "max_pkt_len_err_cnt",
                                                "min_pkt_len_err_cnt",
                                                "pkt_cfh_crc_err_cnt",
                                                "pkt_crc_err_cnt",
                                                "pkt_fpoe_addr_rng_hit_cnt",
                                                "pkt_null_poe_sent_ua0_cnt",
                                                "pkt_null_poe_sent_ua1_cnt",
                                                "pkt_null_poe_sent_ua2_cnt",
                                                "pkt_rcv_cnt",
                                                "pkt_sent_to_disabled_port_cnt",
                                                "pkt_seq_err_cnt",
                                                "pkts_sent_to_ux0_cnt",
                                                "pkts_sent_to_ux1_cnt",
                                                "pkts_sent_to_ux2_cnt",
                                                "rate_cnt",
                                                "stop_thrsh_hit_cnt",
                                                "tail_drp_pkt_cnt",
                                                "tr_head_drop_pkt_cnt",
                                                "tr_pkt_sent_to_ux",
                                                "uc0_data_mem_ecc_1bit_err_cnt",
                                                "uc0_data_mem_ecc_2bit_err_cnt",
                                                "uc1_data_mem_ecc_1bit_err_cnt",
                                                "uc1_data_mem_ecc_2bit_err_cnt",
                                                "uc2_data_mem_ecc_1bit_err_cnt",
                                                "uc2_data_mem_ecc_2bit_err_cnt") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiUcStats, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiUcStats, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.calc_rate.is_set or
                                    self.cpp_head_drop_pkt_cnt.is_set or
                                    self.crc_stomp_pkt_cnt.is_set or
                                    self.diag_pkt_cnt.is_set or
                                    self.fpoe_mem_ecc_1bit_err_cnt.is_set or
                                    self.fpoe_mem_ecc_2bit_err_cnt.is_set or
                                    self.in_coming_pkt_err_cnt.is_set or
                                    self.line_err_drp_pkt.is_set or
                                    self.line_s_written_in_mem0.is_set or
                                    self.line_s_written_in_mem1.is_set or
                                    self.line_s_written_in_mem2.is_set or
                                    self.max_pkt_len_err_cnt.is_set or
                                    self.min_pkt_len_err_cnt.is_set or
                                    self.pkt_cfh_crc_err_cnt.is_set or
                                    self.pkt_crc_err_cnt.is_set or
                                    self.pkt_fpoe_addr_rng_hit_cnt.is_set or
                                    self.pkt_null_poe_sent_ua0_cnt.is_set or
                                    self.pkt_null_poe_sent_ua1_cnt.is_set or
                                    self.pkt_null_poe_sent_ua2_cnt.is_set or
                                    self.pkt_rcv_cnt.is_set or
                                    self.pkt_sent_to_disabled_port_cnt.is_set or
                                    self.pkt_seq_err_cnt.is_set or
                                    self.pkts_sent_to_ux0_cnt.is_set or
                                    self.pkts_sent_to_ux1_cnt.is_set or
                                    self.pkts_sent_to_ux2_cnt.is_set or
                                    self.rate_cnt.is_set or
                                    self.stop_thrsh_hit_cnt.is_set or
                                    self.tail_drp_pkt_cnt.is_set or
                                    self.tr_head_drop_pkt_cnt.is_set or
                                    self.tr_pkt_sent_to_ux.is_set or
                                    self.uc0_data_mem_ecc_1bit_err_cnt.is_set or
                                    self.uc0_data_mem_ecc_2bit_err_cnt.is_set or
                                    self.uc1_data_mem_ecc_1bit_err_cnt.is_set or
                                    self.uc1_data_mem_ecc_2bit_err_cnt.is_set or
                                    self.uc2_data_mem_ecc_1bit_err_cnt.is_set or
                                    self.uc2_data_mem_ecc_2bit_err_cnt.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.calc_rate.yfilter != YFilter.not_set or
                                    self.cpp_head_drop_pkt_cnt.yfilter != YFilter.not_set or
                                    self.crc_stomp_pkt_cnt.yfilter != YFilter.not_set or
                                    self.diag_pkt_cnt.yfilter != YFilter.not_set or
                                    self.fpoe_mem_ecc_1bit_err_cnt.yfilter != YFilter.not_set or
                                    self.fpoe_mem_ecc_2bit_err_cnt.yfilter != YFilter.not_set or
                                    self.in_coming_pkt_err_cnt.yfilter != YFilter.not_set or
                                    self.line_err_drp_pkt.yfilter != YFilter.not_set or
                                    self.line_s_written_in_mem0.yfilter != YFilter.not_set or
                                    self.line_s_written_in_mem1.yfilter != YFilter.not_set or
                                    self.line_s_written_in_mem2.yfilter != YFilter.not_set or
                                    self.max_pkt_len_err_cnt.yfilter != YFilter.not_set or
                                    self.min_pkt_len_err_cnt.yfilter != YFilter.not_set or
                                    self.pkt_cfh_crc_err_cnt.yfilter != YFilter.not_set or
                                    self.pkt_crc_err_cnt.yfilter != YFilter.not_set or
                                    self.pkt_fpoe_addr_rng_hit_cnt.yfilter != YFilter.not_set or
                                    self.pkt_null_poe_sent_ua0_cnt.yfilter != YFilter.not_set or
                                    self.pkt_null_poe_sent_ua1_cnt.yfilter != YFilter.not_set or
                                    self.pkt_null_poe_sent_ua2_cnt.yfilter != YFilter.not_set or
                                    self.pkt_rcv_cnt.yfilter != YFilter.not_set or
                                    self.pkt_sent_to_disabled_port_cnt.yfilter != YFilter.not_set or
                                    self.pkt_seq_err_cnt.yfilter != YFilter.not_set or
                                    self.pkts_sent_to_ux0_cnt.yfilter != YFilter.not_set or
                                    self.pkts_sent_to_ux1_cnt.yfilter != YFilter.not_set or
                                    self.pkts_sent_to_ux2_cnt.yfilter != YFilter.not_set or
                                    self.rate_cnt.yfilter != YFilter.not_set or
                                    self.stop_thrsh_hit_cnt.yfilter != YFilter.not_set or
                                    self.tail_drp_pkt_cnt.yfilter != YFilter.not_set or
                                    self.tr_head_drop_pkt_cnt.yfilter != YFilter.not_set or
                                    self.tr_pkt_sent_to_ux.yfilter != YFilter.not_set or
                                    self.uc0_data_mem_ecc_1bit_err_cnt.yfilter != YFilter.not_set or
                                    self.uc0_data_mem_ecc_2bit_err_cnt.yfilter != YFilter.not_set or
                                    self.uc1_data_mem_ecc_1bit_err_cnt.yfilter != YFilter.not_set or
                                    self.uc1_data_mem_ecc_2bit_err_cnt.yfilter != YFilter.not_set or
                                    self.uc2_data_mem_ecc_1bit_err_cnt.yfilter != YFilter.not_set or
                                    self.uc2_data_mem_ecc_2bit_err_cnt.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pi-uc-stats" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.calc_rate.is_set or self.calc_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.calc_rate.get_name_leafdata())
                                if (self.cpp_head_drop_pkt_cnt.is_set or self.cpp_head_drop_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.cpp_head_drop_pkt_cnt.get_name_leafdata())
                                if (self.crc_stomp_pkt_cnt.is_set or self.crc_stomp_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.crc_stomp_pkt_cnt.get_name_leafdata())
                                if (self.diag_pkt_cnt.is_set or self.diag_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.diag_pkt_cnt.get_name_leafdata())
                                if (self.fpoe_mem_ecc_1bit_err_cnt.is_set or self.fpoe_mem_ecc_1bit_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fpoe_mem_ecc_1bit_err_cnt.get_name_leafdata())
                                if (self.fpoe_mem_ecc_2bit_err_cnt.is_set or self.fpoe_mem_ecc_2bit_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fpoe_mem_ecc_2bit_err_cnt.get_name_leafdata())
                                if (self.in_coming_pkt_err_cnt.is_set or self.in_coming_pkt_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_coming_pkt_err_cnt.get_name_leafdata())
                                if (self.line_err_drp_pkt.is_set or self.line_err_drp_pkt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.line_err_drp_pkt.get_name_leafdata())
                                if (self.line_s_written_in_mem0.is_set or self.line_s_written_in_mem0.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.line_s_written_in_mem0.get_name_leafdata())
                                if (self.line_s_written_in_mem1.is_set or self.line_s_written_in_mem1.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.line_s_written_in_mem1.get_name_leafdata())
                                if (self.line_s_written_in_mem2.is_set or self.line_s_written_in_mem2.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.line_s_written_in_mem2.get_name_leafdata())
                                if (self.max_pkt_len_err_cnt.is_set or self.max_pkt_len_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max_pkt_len_err_cnt.get_name_leafdata())
                                if (self.min_pkt_len_err_cnt.is_set or self.min_pkt_len_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.min_pkt_len_err_cnt.get_name_leafdata())
                                if (self.pkt_cfh_crc_err_cnt.is_set or self.pkt_cfh_crc_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_cfh_crc_err_cnt.get_name_leafdata())
                                if (self.pkt_crc_err_cnt.is_set or self.pkt_crc_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_crc_err_cnt.get_name_leafdata())
                                if (self.pkt_fpoe_addr_rng_hit_cnt.is_set or self.pkt_fpoe_addr_rng_hit_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_fpoe_addr_rng_hit_cnt.get_name_leafdata())
                                if (self.pkt_null_poe_sent_ua0_cnt.is_set or self.pkt_null_poe_sent_ua0_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_null_poe_sent_ua0_cnt.get_name_leafdata())
                                if (self.pkt_null_poe_sent_ua1_cnt.is_set or self.pkt_null_poe_sent_ua1_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_null_poe_sent_ua1_cnt.get_name_leafdata())
                                if (self.pkt_null_poe_sent_ua2_cnt.is_set or self.pkt_null_poe_sent_ua2_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_null_poe_sent_ua2_cnt.get_name_leafdata())
                                if (self.pkt_rcv_cnt.is_set or self.pkt_rcv_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_rcv_cnt.get_name_leafdata())
                                if (self.pkt_sent_to_disabled_port_cnt.is_set or self.pkt_sent_to_disabled_port_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_sent_to_disabled_port_cnt.get_name_leafdata())
                                if (self.pkt_seq_err_cnt.is_set or self.pkt_seq_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_seq_err_cnt.get_name_leafdata())
                                if (self.pkts_sent_to_ux0_cnt.is_set or self.pkts_sent_to_ux0_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkts_sent_to_ux0_cnt.get_name_leafdata())
                                if (self.pkts_sent_to_ux1_cnt.is_set or self.pkts_sent_to_ux1_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkts_sent_to_ux1_cnt.get_name_leafdata())
                                if (self.pkts_sent_to_ux2_cnt.is_set or self.pkts_sent_to_ux2_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkts_sent_to_ux2_cnt.get_name_leafdata())
                                if (self.rate_cnt.is_set or self.rate_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rate_cnt.get_name_leafdata())
                                if (self.stop_thrsh_hit_cnt.is_set or self.stop_thrsh_hit_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.stop_thrsh_hit_cnt.get_name_leafdata())
                                if (self.tail_drp_pkt_cnt.is_set or self.tail_drp_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tail_drp_pkt_cnt.get_name_leafdata())
                                if (self.tr_head_drop_pkt_cnt.is_set or self.tr_head_drop_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tr_head_drop_pkt_cnt.get_name_leafdata())
                                if (self.tr_pkt_sent_to_ux.is_set or self.tr_pkt_sent_to_ux.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tr_pkt_sent_to_ux.get_name_leafdata())
                                if (self.uc0_data_mem_ecc_1bit_err_cnt.is_set or self.uc0_data_mem_ecc_1bit_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.uc0_data_mem_ecc_1bit_err_cnt.get_name_leafdata())
                                if (self.uc0_data_mem_ecc_2bit_err_cnt.is_set or self.uc0_data_mem_ecc_2bit_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.uc0_data_mem_ecc_2bit_err_cnt.get_name_leafdata())
                                if (self.uc1_data_mem_ecc_1bit_err_cnt.is_set or self.uc1_data_mem_ecc_1bit_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.uc1_data_mem_ecc_1bit_err_cnt.get_name_leafdata())
                                if (self.uc1_data_mem_ecc_2bit_err_cnt.is_set or self.uc1_data_mem_ecc_2bit_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.uc1_data_mem_ecc_2bit_err_cnt.get_name_leafdata())
                                if (self.uc2_data_mem_ecc_1bit_err_cnt.is_set or self.uc2_data_mem_ecc_1bit_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.uc2_data_mem_ecc_1bit_err_cnt.get_name_leafdata())
                                if (self.uc2_data_mem_ecc_2bit_err_cnt.is_set or self.uc2_data_mem_ecc_2bit_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.uc2_data_mem_ecc_2bit_err_cnt.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "calc-rate" or name == "cpp-head-drop-pkt-cnt" or name == "crc-stomp-pkt-cnt" or name == "diag-pkt-cnt" or name == "fpoe-mem-ecc-1bit-err-cnt" or name == "fpoe-mem-ecc-2bit-err-cnt" or name == "in-coming-pkt-err-cnt" or name == "line-err-drp-pkt" or name == "line-s-written-in-mem0" or name == "line-s-written-in-mem1" or name == "line-s-written-in-mem2" or name == "max-pkt-len-err-cnt" or name == "min-pkt-len-err-cnt" or name == "pkt-cfh-crc-err-cnt" or name == "pkt-crc-err-cnt" or name == "pkt-fpoe-addr-rng-hit-cnt" or name == "pkt-null-poe-sent-ua0-cnt" or name == "pkt-null-poe-sent-ua1-cnt" or name == "pkt-null-poe-sent-ua2-cnt" or name == "pkt-rcv-cnt" or name == "pkt-sent-to-disabled-port-cnt" or name == "pkt-seq-err-cnt" or name == "pkts-sent-to-ux0-cnt" or name == "pkts-sent-to-ux1-cnt" or name == "pkts-sent-to-ux2-cnt" or name == "rate-cnt" or name == "stop-thrsh-hit-cnt" or name == "tail-drp-pkt-cnt" or name == "tr-head-drop-pkt-cnt" or name == "tr-pkt-sent-to-ux" or name == "uc0-data-mem-ecc-1bit-err-cnt" or name == "uc0-data-mem-ecc-2bit-err-cnt" or name == "uc1-data-mem-ecc-1bit-err-cnt" or name == "uc1-data-mem-ecc-2bit-err-cnt" or name == "uc2-data-mem-ecc-1bit-err-cnt" or name == "uc2-data-mem-ecc-2bit-err-cnt"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "calc-rate"):
                                    self.calc_rate = value
                                    self.calc_rate.value_namespace = name_space
                                    self.calc_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "cpp-head-drop-pkt-cnt"):
                                    self.cpp_head_drop_pkt_cnt = value
                                    self.cpp_head_drop_pkt_cnt.value_namespace = name_space
                                    self.cpp_head_drop_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "crc-stomp-pkt-cnt"):
                                    self.crc_stomp_pkt_cnt = value
                                    self.crc_stomp_pkt_cnt.value_namespace = name_space
                                    self.crc_stomp_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "diag-pkt-cnt"):
                                    self.diag_pkt_cnt = value
                                    self.diag_pkt_cnt.value_namespace = name_space
                                    self.diag_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "fpoe-mem-ecc-1bit-err-cnt"):
                                    self.fpoe_mem_ecc_1bit_err_cnt = value
                                    self.fpoe_mem_ecc_1bit_err_cnt.value_namespace = name_space
                                    self.fpoe_mem_ecc_1bit_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "fpoe-mem-ecc-2bit-err-cnt"):
                                    self.fpoe_mem_ecc_2bit_err_cnt = value
                                    self.fpoe_mem_ecc_2bit_err_cnt.value_namespace = name_space
                                    self.fpoe_mem_ecc_2bit_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-coming-pkt-err-cnt"):
                                    self.in_coming_pkt_err_cnt = value
                                    self.in_coming_pkt_err_cnt.value_namespace = name_space
                                    self.in_coming_pkt_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "line-err-drp-pkt"):
                                    self.line_err_drp_pkt = value
                                    self.line_err_drp_pkt.value_namespace = name_space
                                    self.line_err_drp_pkt.value_namespace_prefix = name_space_prefix
                                if(value_path == "line-s-written-in-mem0"):
                                    self.line_s_written_in_mem0 = value
                                    self.line_s_written_in_mem0.value_namespace = name_space
                                    self.line_s_written_in_mem0.value_namespace_prefix = name_space_prefix
                                if(value_path == "line-s-written-in-mem1"):
                                    self.line_s_written_in_mem1 = value
                                    self.line_s_written_in_mem1.value_namespace = name_space
                                    self.line_s_written_in_mem1.value_namespace_prefix = name_space_prefix
                                if(value_path == "line-s-written-in-mem2"):
                                    self.line_s_written_in_mem2 = value
                                    self.line_s_written_in_mem2.value_namespace = name_space
                                    self.line_s_written_in_mem2.value_namespace_prefix = name_space_prefix
                                if(value_path == "max-pkt-len-err-cnt"):
                                    self.max_pkt_len_err_cnt = value
                                    self.max_pkt_len_err_cnt.value_namespace = name_space
                                    self.max_pkt_len_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "min-pkt-len-err-cnt"):
                                    self.min_pkt_len_err_cnt = value
                                    self.min_pkt_len_err_cnt.value_namespace = name_space
                                    self.min_pkt_len_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-cfh-crc-err-cnt"):
                                    self.pkt_cfh_crc_err_cnt = value
                                    self.pkt_cfh_crc_err_cnt.value_namespace = name_space
                                    self.pkt_cfh_crc_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-crc-err-cnt"):
                                    self.pkt_crc_err_cnt = value
                                    self.pkt_crc_err_cnt.value_namespace = name_space
                                    self.pkt_crc_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-fpoe-addr-rng-hit-cnt"):
                                    self.pkt_fpoe_addr_rng_hit_cnt = value
                                    self.pkt_fpoe_addr_rng_hit_cnt.value_namespace = name_space
                                    self.pkt_fpoe_addr_rng_hit_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-null-poe-sent-ua0-cnt"):
                                    self.pkt_null_poe_sent_ua0_cnt = value
                                    self.pkt_null_poe_sent_ua0_cnt.value_namespace = name_space
                                    self.pkt_null_poe_sent_ua0_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-null-poe-sent-ua1-cnt"):
                                    self.pkt_null_poe_sent_ua1_cnt = value
                                    self.pkt_null_poe_sent_ua1_cnt.value_namespace = name_space
                                    self.pkt_null_poe_sent_ua1_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-null-poe-sent-ua2-cnt"):
                                    self.pkt_null_poe_sent_ua2_cnt = value
                                    self.pkt_null_poe_sent_ua2_cnt.value_namespace = name_space
                                    self.pkt_null_poe_sent_ua2_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-rcv-cnt"):
                                    self.pkt_rcv_cnt = value
                                    self.pkt_rcv_cnt.value_namespace = name_space
                                    self.pkt_rcv_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-sent-to-disabled-port-cnt"):
                                    self.pkt_sent_to_disabled_port_cnt = value
                                    self.pkt_sent_to_disabled_port_cnt.value_namespace = name_space
                                    self.pkt_sent_to_disabled_port_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-seq-err-cnt"):
                                    self.pkt_seq_err_cnt = value
                                    self.pkt_seq_err_cnt.value_namespace = name_space
                                    self.pkt_seq_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkts-sent-to-ux0-cnt"):
                                    self.pkts_sent_to_ux0_cnt = value
                                    self.pkts_sent_to_ux0_cnt.value_namespace = name_space
                                    self.pkts_sent_to_ux0_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkts-sent-to-ux1-cnt"):
                                    self.pkts_sent_to_ux1_cnt = value
                                    self.pkts_sent_to_ux1_cnt.value_namespace = name_space
                                    self.pkts_sent_to_ux1_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkts-sent-to-ux2-cnt"):
                                    self.pkts_sent_to_ux2_cnt = value
                                    self.pkts_sent_to_ux2_cnt.value_namespace = name_space
                                    self.pkts_sent_to_ux2_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rate-cnt"):
                                    self.rate_cnt = value
                                    self.rate_cnt.value_namespace = name_space
                                    self.rate_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "stop-thrsh-hit-cnt"):
                                    self.stop_thrsh_hit_cnt = value
                                    self.stop_thrsh_hit_cnt.value_namespace = name_space
                                    self.stop_thrsh_hit_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "tail-drp-pkt-cnt"):
                                    self.tail_drp_pkt_cnt = value
                                    self.tail_drp_pkt_cnt.value_namespace = name_space
                                    self.tail_drp_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "tr-head-drop-pkt-cnt"):
                                    self.tr_head_drop_pkt_cnt = value
                                    self.tr_head_drop_pkt_cnt.value_namespace = name_space
                                    self.tr_head_drop_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "tr-pkt-sent-to-ux"):
                                    self.tr_pkt_sent_to_ux = value
                                    self.tr_pkt_sent_to_ux.value_namespace = name_space
                                    self.tr_pkt_sent_to_ux.value_namespace_prefix = name_space_prefix
                                if(value_path == "uc0-data-mem-ecc-1bit-err-cnt"):
                                    self.uc0_data_mem_ecc_1bit_err_cnt = value
                                    self.uc0_data_mem_ecc_1bit_err_cnt.value_namespace = name_space
                                    self.uc0_data_mem_ecc_1bit_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "uc0-data-mem-ecc-2bit-err-cnt"):
                                    self.uc0_data_mem_ecc_2bit_err_cnt = value
                                    self.uc0_data_mem_ecc_2bit_err_cnt.value_namespace = name_space
                                    self.uc0_data_mem_ecc_2bit_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "uc1-data-mem-ecc-1bit-err-cnt"):
                                    self.uc1_data_mem_ecc_1bit_err_cnt = value
                                    self.uc1_data_mem_ecc_1bit_err_cnt.value_namespace = name_space
                                    self.uc1_data_mem_ecc_1bit_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "uc1-data-mem-ecc-2bit-err-cnt"):
                                    self.uc1_data_mem_ecc_2bit_err_cnt = value
                                    self.uc1_data_mem_ecc_2bit_err_cnt.value_namespace = name_space
                                    self.uc1_data_mem_ecc_2bit_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "uc2-data-mem-ecc-1bit-err-cnt"):
                                    self.uc2_data_mem_ecc_1bit_err_cnt = value
                                    self.uc2_data_mem_ecc_1bit_err_cnt.value_namespace = name_space
                                    self.uc2_data_mem_ecc_1bit_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "uc2-data-mem-ecc-2bit-err-cnt"):
                                    self.uc2_data_mem_ecc_2bit_err_cnt = value
                                    self.uc2_data_mem_ecc_2bit_err_cnt.value_namespace = name_space
                                    self.uc2_data_mem_ecc_2bit_err_cnt.value_namespace_prefix = name_space_prefix


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("calc_rate",
                                                "cpp_head_drop_pkt_from_ma_cnt",
                                                "crc_stomp_pkt_cnt",
                                                "data_mem0_ecc_1bit_err_cnt",
                                                "data_mem0_ecc_2bit_err_cnt",
                                                "data_mem1_ecc_1bit_err_cnt",
                                                "data_mem1_ecc_2bit_err_cnt",
                                                "data_mem2_ecc_1bit_err_cnt",
                                                "data_mem2_ecc_2bit_err_cnt",
                                                "di_err_pkt_cnt",
                                                "di_hdr_len_err_pkt_cnt",
                                                "diag_pkt_cnt",
                                                "fpoe_mem_ecc_1bit_err_cnt",
                                                "fpoe_mem_ecc_2bit_err_cnt",
                                                "in_coming_pkt_err_cnt",
                                                "line_err_drp_pkt",
                                                "line_s_written_in_mem",
                                                "max_pkt_len_err_cnt",
                                                "min_pkt_len_err_cnt",
                                                "pkt_cfh_crc_err_cnt",
                                                "pkt_crc_err_cnt",
                                                "pkt_fpoe_addr_rng_hit_cnt",
                                                "pkt_fpoe_match_hit_cnt",
                                                "pkt_null_poe_sent_cnt",
                                                "pkt_rcv_cnt",
                                                "pkt_sent_to_disabled_port",
                                                "pkt_seq_err_cnt",
                                                "pkts_sent_to_mx_cnt",
                                                "rate_cnt",
                                                "stop_thrsh_hit_cnt",
                                                "tail_drp_pkt_cnt",
                                                "tr_head_drop_pkt_from_ma_cnt",
                                                "tr_pkt_sent_to_mx") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiMcStats, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiMcStats, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.calc_rate.is_set or
                                    self.cpp_head_drop_pkt_from_ma_cnt.is_set or
                                    self.crc_stomp_pkt_cnt.is_set or
                                    self.data_mem0_ecc_1bit_err_cnt.is_set or
                                    self.data_mem0_ecc_2bit_err_cnt.is_set or
                                    self.data_mem1_ecc_1bit_err_cnt.is_set or
                                    self.data_mem1_ecc_2bit_err_cnt.is_set or
                                    self.data_mem2_ecc_1bit_err_cnt.is_set or
                                    self.data_mem2_ecc_2bit_err_cnt.is_set or
                                    self.di_err_pkt_cnt.is_set or
                                    self.di_hdr_len_err_pkt_cnt.is_set or
                                    self.diag_pkt_cnt.is_set or
                                    self.fpoe_mem_ecc_1bit_err_cnt.is_set or
                                    self.fpoe_mem_ecc_2bit_err_cnt.is_set or
                                    self.in_coming_pkt_err_cnt.is_set or
                                    self.line_err_drp_pkt.is_set or
                                    self.line_s_written_in_mem.is_set or
                                    self.max_pkt_len_err_cnt.is_set or
                                    self.min_pkt_len_err_cnt.is_set or
                                    self.pkt_cfh_crc_err_cnt.is_set or
                                    self.pkt_crc_err_cnt.is_set or
                                    self.pkt_fpoe_addr_rng_hit_cnt.is_set or
                                    self.pkt_fpoe_match_hit_cnt.is_set or
                                    self.pkt_null_poe_sent_cnt.is_set or
                                    self.pkt_rcv_cnt.is_set or
                                    self.pkt_sent_to_disabled_port.is_set or
                                    self.pkt_seq_err_cnt.is_set or
                                    self.pkts_sent_to_mx_cnt.is_set or
                                    self.rate_cnt.is_set or
                                    self.stop_thrsh_hit_cnt.is_set or
                                    self.tail_drp_pkt_cnt.is_set or
                                    self.tr_head_drop_pkt_from_ma_cnt.is_set or
                                    self.tr_pkt_sent_to_mx.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.calc_rate.yfilter != YFilter.not_set or
                                    self.cpp_head_drop_pkt_from_ma_cnt.yfilter != YFilter.not_set or
                                    self.crc_stomp_pkt_cnt.yfilter != YFilter.not_set or
                                    self.data_mem0_ecc_1bit_err_cnt.yfilter != YFilter.not_set or
                                    self.data_mem0_ecc_2bit_err_cnt.yfilter != YFilter.not_set or
                                    self.data_mem1_ecc_1bit_err_cnt.yfilter != YFilter.not_set or
                                    self.data_mem1_ecc_2bit_err_cnt.yfilter != YFilter.not_set or
                                    self.data_mem2_ecc_1bit_err_cnt.yfilter != YFilter.not_set or
                                    self.data_mem2_ecc_2bit_err_cnt.yfilter != YFilter.not_set or
                                    self.di_err_pkt_cnt.yfilter != YFilter.not_set or
                                    self.di_hdr_len_err_pkt_cnt.yfilter != YFilter.not_set or
                                    self.diag_pkt_cnt.yfilter != YFilter.not_set or
                                    self.fpoe_mem_ecc_1bit_err_cnt.yfilter != YFilter.not_set or
                                    self.fpoe_mem_ecc_2bit_err_cnt.yfilter != YFilter.not_set or
                                    self.in_coming_pkt_err_cnt.yfilter != YFilter.not_set or
                                    self.line_err_drp_pkt.yfilter != YFilter.not_set or
                                    self.line_s_written_in_mem.yfilter != YFilter.not_set or
                                    self.max_pkt_len_err_cnt.yfilter != YFilter.not_set or
                                    self.min_pkt_len_err_cnt.yfilter != YFilter.not_set or
                                    self.pkt_cfh_crc_err_cnt.yfilter != YFilter.not_set or
                                    self.pkt_crc_err_cnt.yfilter != YFilter.not_set or
                                    self.pkt_fpoe_addr_rng_hit_cnt.yfilter != YFilter.not_set or
                                    self.pkt_fpoe_match_hit_cnt.yfilter != YFilter.not_set or
                                    self.pkt_null_poe_sent_cnt.yfilter != YFilter.not_set or
                                    self.pkt_rcv_cnt.yfilter != YFilter.not_set or
                                    self.pkt_sent_to_disabled_port.yfilter != YFilter.not_set or
                                    self.pkt_seq_err_cnt.yfilter != YFilter.not_set or
                                    self.pkts_sent_to_mx_cnt.yfilter != YFilter.not_set or
                                    self.rate_cnt.yfilter != YFilter.not_set or
                                    self.stop_thrsh_hit_cnt.yfilter != YFilter.not_set or
                                    self.tail_drp_pkt_cnt.yfilter != YFilter.not_set or
                                    self.tr_head_drop_pkt_from_ma_cnt.yfilter != YFilter.not_set or
                                    self.tr_pkt_sent_to_mx.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pi-mc-stats" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.calc_rate.is_set or self.calc_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.calc_rate.get_name_leafdata())
                                if (self.cpp_head_drop_pkt_from_ma_cnt.is_set or self.cpp_head_drop_pkt_from_ma_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.cpp_head_drop_pkt_from_ma_cnt.get_name_leafdata())
                                if (self.crc_stomp_pkt_cnt.is_set or self.crc_stomp_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.crc_stomp_pkt_cnt.get_name_leafdata())
                                if (self.data_mem0_ecc_1bit_err_cnt.is_set or self.data_mem0_ecc_1bit_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_mem0_ecc_1bit_err_cnt.get_name_leafdata())
                                if (self.data_mem0_ecc_2bit_err_cnt.is_set or self.data_mem0_ecc_2bit_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_mem0_ecc_2bit_err_cnt.get_name_leafdata())
                                if (self.data_mem1_ecc_1bit_err_cnt.is_set or self.data_mem1_ecc_1bit_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_mem1_ecc_1bit_err_cnt.get_name_leafdata())
                                if (self.data_mem1_ecc_2bit_err_cnt.is_set or self.data_mem1_ecc_2bit_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_mem1_ecc_2bit_err_cnt.get_name_leafdata())
                                if (self.data_mem2_ecc_1bit_err_cnt.is_set or self.data_mem2_ecc_1bit_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_mem2_ecc_1bit_err_cnt.get_name_leafdata())
                                if (self.data_mem2_ecc_2bit_err_cnt.is_set or self.data_mem2_ecc_2bit_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_mem2_ecc_2bit_err_cnt.get_name_leafdata())
                                if (self.di_err_pkt_cnt.is_set or self.di_err_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.di_err_pkt_cnt.get_name_leafdata())
                                if (self.di_hdr_len_err_pkt_cnt.is_set or self.di_hdr_len_err_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.di_hdr_len_err_pkt_cnt.get_name_leafdata())
                                if (self.diag_pkt_cnt.is_set or self.diag_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.diag_pkt_cnt.get_name_leafdata())
                                if (self.fpoe_mem_ecc_1bit_err_cnt.is_set or self.fpoe_mem_ecc_1bit_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fpoe_mem_ecc_1bit_err_cnt.get_name_leafdata())
                                if (self.fpoe_mem_ecc_2bit_err_cnt.is_set or self.fpoe_mem_ecc_2bit_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fpoe_mem_ecc_2bit_err_cnt.get_name_leafdata())
                                if (self.in_coming_pkt_err_cnt.is_set or self.in_coming_pkt_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_coming_pkt_err_cnt.get_name_leafdata())
                                if (self.line_err_drp_pkt.is_set or self.line_err_drp_pkt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.line_err_drp_pkt.get_name_leafdata())
                                if (self.line_s_written_in_mem.is_set or self.line_s_written_in_mem.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.line_s_written_in_mem.get_name_leafdata())
                                if (self.max_pkt_len_err_cnt.is_set or self.max_pkt_len_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max_pkt_len_err_cnt.get_name_leafdata())
                                if (self.min_pkt_len_err_cnt.is_set or self.min_pkt_len_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.min_pkt_len_err_cnt.get_name_leafdata())
                                if (self.pkt_cfh_crc_err_cnt.is_set or self.pkt_cfh_crc_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_cfh_crc_err_cnt.get_name_leafdata())
                                if (self.pkt_crc_err_cnt.is_set or self.pkt_crc_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_crc_err_cnt.get_name_leafdata())
                                if (self.pkt_fpoe_addr_rng_hit_cnt.is_set or self.pkt_fpoe_addr_rng_hit_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_fpoe_addr_rng_hit_cnt.get_name_leafdata())
                                if (self.pkt_fpoe_match_hit_cnt.is_set or self.pkt_fpoe_match_hit_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_fpoe_match_hit_cnt.get_name_leafdata())
                                if (self.pkt_null_poe_sent_cnt.is_set or self.pkt_null_poe_sent_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_null_poe_sent_cnt.get_name_leafdata())
                                if (self.pkt_rcv_cnt.is_set or self.pkt_rcv_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_rcv_cnt.get_name_leafdata())
                                if (self.pkt_sent_to_disabled_port.is_set or self.pkt_sent_to_disabled_port.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_sent_to_disabled_port.get_name_leafdata())
                                if (self.pkt_seq_err_cnt.is_set or self.pkt_seq_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_seq_err_cnt.get_name_leafdata())
                                if (self.pkts_sent_to_mx_cnt.is_set or self.pkts_sent_to_mx_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkts_sent_to_mx_cnt.get_name_leafdata())
                                if (self.rate_cnt.is_set or self.rate_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rate_cnt.get_name_leafdata())
                                if (self.stop_thrsh_hit_cnt.is_set or self.stop_thrsh_hit_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.stop_thrsh_hit_cnt.get_name_leafdata())
                                if (self.tail_drp_pkt_cnt.is_set or self.tail_drp_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tail_drp_pkt_cnt.get_name_leafdata())
                                if (self.tr_head_drop_pkt_from_ma_cnt.is_set or self.tr_head_drop_pkt_from_ma_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tr_head_drop_pkt_from_ma_cnt.get_name_leafdata())
                                if (self.tr_pkt_sent_to_mx.is_set or self.tr_pkt_sent_to_mx.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tr_pkt_sent_to_mx.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "calc-rate" or name == "cpp-head-drop-pkt-from-ma-cnt" or name == "crc-stomp-pkt-cnt" or name == "data-mem0-ecc-1bit-err-cnt" or name == "data-mem0-ecc-2bit-err-cnt" or name == "data-mem1-ecc-1bit-err-cnt" or name == "data-mem1-ecc-2bit-err-cnt" or name == "data-mem2-ecc-1bit-err-cnt" or name == "data-mem2-ecc-2bit-err-cnt" or name == "di-err-pkt-cnt" or name == "di-hdr-len-err-pkt-cnt" or name == "diag-pkt-cnt" or name == "fpoe-mem-ecc-1bit-err-cnt" or name == "fpoe-mem-ecc-2bit-err-cnt" or name == "in-coming-pkt-err-cnt" or name == "line-err-drp-pkt" or name == "line-s-written-in-mem" or name == "max-pkt-len-err-cnt" or name == "min-pkt-len-err-cnt" or name == "pkt-cfh-crc-err-cnt" or name == "pkt-crc-err-cnt" or name == "pkt-fpoe-addr-rng-hit-cnt" or name == "pkt-fpoe-match-hit-cnt" or name == "pkt-null-poe-sent-cnt" or name == "pkt-rcv-cnt" or name == "pkt-sent-to-disabled-port" or name == "pkt-seq-err-cnt" or name == "pkts-sent-to-mx-cnt" or name == "rate-cnt" or name == "stop-thrsh-hit-cnt" or name == "tail-drp-pkt-cnt" or name == "tr-head-drop-pkt-from-ma-cnt" or name == "tr-pkt-sent-to-mx"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "calc-rate"):
                                    self.calc_rate = value
                                    self.calc_rate.value_namespace = name_space
                                    self.calc_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "cpp-head-drop-pkt-from-ma-cnt"):
                                    self.cpp_head_drop_pkt_from_ma_cnt = value
                                    self.cpp_head_drop_pkt_from_ma_cnt.value_namespace = name_space
                                    self.cpp_head_drop_pkt_from_ma_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "crc-stomp-pkt-cnt"):
                                    self.crc_stomp_pkt_cnt = value
                                    self.crc_stomp_pkt_cnt.value_namespace = name_space
                                    self.crc_stomp_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "data-mem0-ecc-1bit-err-cnt"):
                                    self.data_mem0_ecc_1bit_err_cnt = value
                                    self.data_mem0_ecc_1bit_err_cnt.value_namespace = name_space
                                    self.data_mem0_ecc_1bit_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "data-mem0-ecc-2bit-err-cnt"):
                                    self.data_mem0_ecc_2bit_err_cnt = value
                                    self.data_mem0_ecc_2bit_err_cnt.value_namespace = name_space
                                    self.data_mem0_ecc_2bit_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "data-mem1-ecc-1bit-err-cnt"):
                                    self.data_mem1_ecc_1bit_err_cnt = value
                                    self.data_mem1_ecc_1bit_err_cnt.value_namespace = name_space
                                    self.data_mem1_ecc_1bit_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "data-mem1-ecc-2bit-err-cnt"):
                                    self.data_mem1_ecc_2bit_err_cnt = value
                                    self.data_mem1_ecc_2bit_err_cnt.value_namespace = name_space
                                    self.data_mem1_ecc_2bit_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "data-mem2-ecc-1bit-err-cnt"):
                                    self.data_mem2_ecc_1bit_err_cnt = value
                                    self.data_mem2_ecc_1bit_err_cnt.value_namespace = name_space
                                    self.data_mem2_ecc_1bit_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "data-mem2-ecc-2bit-err-cnt"):
                                    self.data_mem2_ecc_2bit_err_cnt = value
                                    self.data_mem2_ecc_2bit_err_cnt.value_namespace = name_space
                                    self.data_mem2_ecc_2bit_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "di-err-pkt-cnt"):
                                    self.di_err_pkt_cnt = value
                                    self.di_err_pkt_cnt.value_namespace = name_space
                                    self.di_err_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "di-hdr-len-err-pkt-cnt"):
                                    self.di_hdr_len_err_pkt_cnt = value
                                    self.di_hdr_len_err_pkt_cnt.value_namespace = name_space
                                    self.di_hdr_len_err_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "diag-pkt-cnt"):
                                    self.diag_pkt_cnt = value
                                    self.diag_pkt_cnt.value_namespace = name_space
                                    self.diag_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "fpoe-mem-ecc-1bit-err-cnt"):
                                    self.fpoe_mem_ecc_1bit_err_cnt = value
                                    self.fpoe_mem_ecc_1bit_err_cnt.value_namespace = name_space
                                    self.fpoe_mem_ecc_1bit_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "fpoe-mem-ecc-2bit-err-cnt"):
                                    self.fpoe_mem_ecc_2bit_err_cnt = value
                                    self.fpoe_mem_ecc_2bit_err_cnt.value_namespace = name_space
                                    self.fpoe_mem_ecc_2bit_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-coming-pkt-err-cnt"):
                                    self.in_coming_pkt_err_cnt = value
                                    self.in_coming_pkt_err_cnt.value_namespace = name_space
                                    self.in_coming_pkt_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "line-err-drp-pkt"):
                                    self.line_err_drp_pkt = value
                                    self.line_err_drp_pkt.value_namespace = name_space
                                    self.line_err_drp_pkt.value_namespace_prefix = name_space_prefix
                                if(value_path == "line-s-written-in-mem"):
                                    self.line_s_written_in_mem = value
                                    self.line_s_written_in_mem.value_namespace = name_space
                                    self.line_s_written_in_mem.value_namespace_prefix = name_space_prefix
                                if(value_path == "max-pkt-len-err-cnt"):
                                    self.max_pkt_len_err_cnt = value
                                    self.max_pkt_len_err_cnt.value_namespace = name_space
                                    self.max_pkt_len_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "min-pkt-len-err-cnt"):
                                    self.min_pkt_len_err_cnt = value
                                    self.min_pkt_len_err_cnt.value_namespace = name_space
                                    self.min_pkt_len_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-cfh-crc-err-cnt"):
                                    self.pkt_cfh_crc_err_cnt = value
                                    self.pkt_cfh_crc_err_cnt.value_namespace = name_space
                                    self.pkt_cfh_crc_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-crc-err-cnt"):
                                    self.pkt_crc_err_cnt = value
                                    self.pkt_crc_err_cnt.value_namespace = name_space
                                    self.pkt_crc_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-fpoe-addr-rng-hit-cnt"):
                                    self.pkt_fpoe_addr_rng_hit_cnt = value
                                    self.pkt_fpoe_addr_rng_hit_cnt.value_namespace = name_space
                                    self.pkt_fpoe_addr_rng_hit_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-fpoe-match-hit-cnt"):
                                    self.pkt_fpoe_match_hit_cnt = value
                                    self.pkt_fpoe_match_hit_cnt.value_namespace = name_space
                                    self.pkt_fpoe_match_hit_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-null-poe-sent-cnt"):
                                    self.pkt_null_poe_sent_cnt = value
                                    self.pkt_null_poe_sent_cnt.value_namespace = name_space
                                    self.pkt_null_poe_sent_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-rcv-cnt"):
                                    self.pkt_rcv_cnt = value
                                    self.pkt_rcv_cnt.value_namespace = name_space
                                    self.pkt_rcv_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-sent-to-disabled-port"):
                                    self.pkt_sent_to_disabled_port = value
                                    self.pkt_sent_to_disabled_port.value_namespace = name_space
                                    self.pkt_sent_to_disabled_port.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-seq-err-cnt"):
                                    self.pkt_seq_err_cnt = value
                                    self.pkt_seq_err_cnt.value_namespace = name_space
                                    self.pkt_seq_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkts-sent-to-mx-cnt"):
                                    self.pkts_sent_to_mx_cnt = value
                                    self.pkts_sent_to_mx_cnt.value_namespace = name_space
                                    self.pkts_sent_to_mx_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rate-cnt"):
                                    self.rate_cnt = value
                                    self.rate_cnt.value_namespace = name_space
                                    self.rate_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "stop-thrsh-hit-cnt"):
                                    self.stop_thrsh_hit_cnt = value
                                    self.stop_thrsh_hit_cnt.value_namespace = name_space
                                    self.stop_thrsh_hit_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "tail-drp-pkt-cnt"):
                                    self.tail_drp_pkt_cnt = value
                                    self.tail_drp_pkt_cnt.value_namespace = name_space
                                    self.tail_drp_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "tr-head-drop-pkt-from-ma-cnt"):
                                    self.tr_head_drop_pkt_from_ma_cnt = value
                                    self.tr_head_drop_pkt_from_ma_cnt.value_namespace = name_space
                                    self.tr_head_drop_pkt_from_ma_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "tr-pkt-sent-to-mx"):
                                    self.tr_pkt_sent_to_mx = value
                                    self.tr_pkt_sent_to_mx.value_namespace = name_space
                                    self.tr_pkt_sent_to_mx.value_namespace_prefix = name_space_prefix


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("calc_rate",
                                                "data_mem_ecc_derr_cnt",
                                                "data_mem_ecc_serr_cnt",
                                                "data_mem_ovf0_cnt",
                                                "data_mem_ovf1_cnt",
                                                "dmem_rd_cnt",
                                                "fpoe_mem_ecc_derr_cnt",
                                                "fpoe_mem_ecc_serr_cnt",
                                                "in0_cong_cnt",
                                                "in0_drop_cnt",
                                                "in0_ecc_derr_cnt",
                                                "in0_ecc_serr_cnt",
                                                "in0_fnc_err_cnt",
                                                "in0_pkt_cnt",
                                                "in0_shut_cnt",
                                                "in1_cong_cnt",
                                                "in1_drop_cnt",
                                                "in1_ecc_derr_cnt",
                                                "in1_ecc_serr_cnt",
                                                "in1_fnc_err_cnt",
                                                "in1_pkt_cnt",
                                                "in1_shut_cnt",
                                                "in_dmem0_cnt",
                                                "in_dmem1_cnt",
                                                "null_poe_cnt",
                                                "out_pkt_cnt",
                                                "rate_cnt",
                                                "shut_ack_cnt",
                                                "stop_thrsh_hit_cnt",
                                                "tail_drop_msg_cnt") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiCcStats, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiCcStats, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.calc_rate.is_set or
                                    self.data_mem_ecc_derr_cnt.is_set or
                                    self.data_mem_ecc_serr_cnt.is_set or
                                    self.data_mem_ovf0_cnt.is_set or
                                    self.data_mem_ovf1_cnt.is_set or
                                    self.dmem_rd_cnt.is_set or
                                    self.fpoe_mem_ecc_derr_cnt.is_set or
                                    self.fpoe_mem_ecc_serr_cnt.is_set or
                                    self.in0_cong_cnt.is_set or
                                    self.in0_drop_cnt.is_set or
                                    self.in0_ecc_derr_cnt.is_set or
                                    self.in0_ecc_serr_cnt.is_set or
                                    self.in0_fnc_err_cnt.is_set or
                                    self.in0_pkt_cnt.is_set or
                                    self.in0_shut_cnt.is_set or
                                    self.in1_cong_cnt.is_set or
                                    self.in1_drop_cnt.is_set or
                                    self.in1_ecc_derr_cnt.is_set or
                                    self.in1_ecc_serr_cnt.is_set or
                                    self.in1_fnc_err_cnt.is_set or
                                    self.in1_pkt_cnt.is_set or
                                    self.in1_shut_cnt.is_set or
                                    self.in_dmem0_cnt.is_set or
                                    self.in_dmem1_cnt.is_set or
                                    self.null_poe_cnt.is_set or
                                    self.out_pkt_cnt.is_set or
                                    self.rate_cnt.is_set or
                                    self.shut_ack_cnt.is_set or
                                    self.stop_thrsh_hit_cnt.is_set or
                                    self.tail_drop_msg_cnt.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.calc_rate.yfilter != YFilter.not_set or
                                    self.data_mem_ecc_derr_cnt.yfilter != YFilter.not_set or
                                    self.data_mem_ecc_serr_cnt.yfilter != YFilter.not_set or
                                    self.data_mem_ovf0_cnt.yfilter != YFilter.not_set or
                                    self.data_mem_ovf1_cnt.yfilter != YFilter.not_set or
                                    self.dmem_rd_cnt.yfilter != YFilter.not_set or
                                    self.fpoe_mem_ecc_derr_cnt.yfilter != YFilter.not_set or
                                    self.fpoe_mem_ecc_serr_cnt.yfilter != YFilter.not_set or
                                    self.in0_cong_cnt.yfilter != YFilter.not_set or
                                    self.in0_drop_cnt.yfilter != YFilter.not_set or
                                    self.in0_ecc_derr_cnt.yfilter != YFilter.not_set or
                                    self.in0_ecc_serr_cnt.yfilter != YFilter.not_set or
                                    self.in0_fnc_err_cnt.yfilter != YFilter.not_set or
                                    self.in0_pkt_cnt.yfilter != YFilter.not_set or
                                    self.in0_shut_cnt.yfilter != YFilter.not_set or
                                    self.in1_cong_cnt.yfilter != YFilter.not_set or
                                    self.in1_drop_cnt.yfilter != YFilter.not_set or
                                    self.in1_ecc_derr_cnt.yfilter != YFilter.not_set or
                                    self.in1_ecc_serr_cnt.yfilter != YFilter.not_set or
                                    self.in1_fnc_err_cnt.yfilter != YFilter.not_set or
                                    self.in1_pkt_cnt.yfilter != YFilter.not_set or
                                    self.in1_shut_cnt.yfilter != YFilter.not_set or
                                    self.in_dmem0_cnt.yfilter != YFilter.not_set or
                                    self.in_dmem1_cnt.yfilter != YFilter.not_set or
                                    self.null_poe_cnt.yfilter != YFilter.not_set or
                                    self.out_pkt_cnt.yfilter != YFilter.not_set or
                                    self.rate_cnt.yfilter != YFilter.not_set or
                                    self.shut_ack_cnt.yfilter != YFilter.not_set or
                                    self.stop_thrsh_hit_cnt.yfilter != YFilter.not_set or
                                    self.tail_drop_msg_cnt.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pi-cc-stats" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.calc_rate.is_set or self.calc_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.calc_rate.get_name_leafdata())
                                if (self.data_mem_ecc_derr_cnt.is_set or self.data_mem_ecc_derr_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_mem_ecc_derr_cnt.get_name_leafdata())
                                if (self.data_mem_ecc_serr_cnt.is_set or self.data_mem_ecc_serr_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_mem_ecc_serr_cnt.get_name_leafdata())
                                if (self.data_mem_ovf0_cnt.is_set or self.data_mem_ovf0_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_mem_ovf0_cnt.get_name_leafdata())
                                if (self.data_mem_ovf1_cnt.is_set or self.data_mem_ovf1_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_mem_ovf1_cnt.get_name_leafdata())
                                if (self.dmem_rd_cnt.is_set or self.dmem_rd_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dmem_rd_cnt.get_name_leafdata())
                                if (self.fpoe_mem_ecc_derr_cnt.is_set or self.fpoe_mem_ecc_derr_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fpoe_mem_ecc_derr_cnt.get_name_leafdata())
                                if (self.fpoe_mem_ecc_serr_cnt.is_set or self.fpoe_mem_ecc_serr_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fpoe_mem_ecc_serr_cnt.get_name_leafdata())
                                if (self.in0_cong_cnt.is_set or self.in0_cong_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in0_cong_cnt.get_name_leafdata())
                                if (self.in0_drop_cnt.is_set or self.in0_drop_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in0_drop_cnt.get_name_leafdata())
                                if (self.in0_ecc_derr_cnt.is_set or self.in0_ecc_derr_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in0_ecc_derr_cnt.get_name_leafdata())
                                if (self.in0_ecc_serr_cnt.is_set or self.in0_ecc_serr_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in0_ecc_serr_cnt.get_name_leafdata())
                                if (self.in0_fnc_err_cnt.is_set or self.in0_fnc_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in0_fnc_err_cnt.get_name_leafdata())
                                if (self.in0_pkt_cnt.is_set or self.in0_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in0_pkt_cnt.get_name_leafdata())
                                if (self.in0_shut_cnt.is_set or self.in0_shut_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in0_shut_cnt.get_name_leafdata())
                                if (self.in1_cong_cnt.is_set or self.in1_cong_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in1_cong_cnt.get_name_leafdata())
                                if (self.in1_drop_cnt.is_set or self.in1_drop_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in1_drop_cnt.get_name_leafdata())
                                if (self.in1_ecc_derr_cnt.is_set or self.in1_ecc_derr_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in1_ecc_derr_cnt.get_name_leafdata())
                                if (self.in1_ecc_serr_cnt.is_set or self.in1_ecc_serr_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in1_ecc_serr_cnt.get_name_leafdata())
                                if (self.in1_fnc_err_cnt.is_set or self.in1_fnc_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in1_fnc_err_cnt.get_name_leafdata())
                                if (self.in1_pkt_cnt.is_set or self.in1_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in1_pkt_cnt.get_name_leafdata())
                                if (self.in1_shut_cnt.is_set or self.in1_shut_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in1_shut_cnt.get_name_leafdata())
                                if (self.in_dmem0_cnt.is_set or self.in_dmem0_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_dmem0_cnt.get_name_leafdata())
                                if (self.in_dmem1_cnt.is_set or self.in_dmem1_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_dmem1_cnt.get_name_leafdata())
                                if (self.null_poe_cnt.is_set or self.null_poe_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.null_poe_cnt.get_name_leafdata())
                                if (self.out_pkt_cnt.is_set or self.out_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_pkt_cnt.get_name_leafdata())
                                if (self.rate_cnt.is_set or self.rate_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rate_cnt.get_name_leafdata())
                                if (self.shut_ack_cnt.is_set or self.shut_ack_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.shut_ack_cnt.get_name_leafdata())
                                if (self.stop_thrsh_hit_cnt.is_set or self.stop_thrsh_hit_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.stop_thrsh_hit_cnt.get_name_leafdata())
                                if (self.tail_drop_msg_cnt.is_set or self.tail_drop_msg_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tail_drop_msg_cnt.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "calc-rate" or name == "data-mem-ecc-derr-cnt" or name == "data-mem-ecc-serr-cnt" or name == "data-mem-ovf0-cnt" or name == "data-mem-ovf1-cnt" or name == "dmem-rd-cnt" or name == "fpoe-mem-ecc-derr-cnt" or name == "fpoe-mem-ecc-serr-cnt" or name == "in0-cong-cnt" or name == "in0-drop-cnt" or name == "in0-ecc-derr-cnt" or name == "in0-ecc-serr-cnt" or name == "in0-fnc-err-cnt" or name == "in0-pkt-cnt" or name == "in0-shut-cnt" or name == "in1-cong-cnt" or name == "in1-drop-cnt" or name == "in1-ecc-derr-cnt" or name == "in1-ecc-serr-cnt" or name == "in1-fnc-err-cnt" or name == "in1-pkt-cnt" or name == "in1-shut-cnt" or name == "in-dmem0-cnt" or name == "in-dmem1-cnt" or name == "null-poe-cnt" or name == "out-pkt-cnt" or name == "rate-cnt" or name == "shut-ack-cnt" or name == "stop-thrsh-hit-cnt" or name == "tail-drop-msg-cnt"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "calc-rate"):
                                    self.calc_rate = value
                                    self.calc_rate.value_namespace = name_space
                                    self.calc_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "data-mem-ecc-derr-cnt"):
                                    self.data_mem_ecc_derr_cnt = value
                                    self.data_mem_ecc_derr_cnt.value_namespace = name_space
                                    self.data_mem_ecc_derr_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "data-mem-ecc-serr-cnt"):
                                    self.data_mem_ecc_serr_cnt = value
                                    self.data_mem_ecc_serr_cnt.value_namespace = name_space
                                    self.data_mem_ecc_serr_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "data-mem-ovf0-cnt"):
                                    self.data_mem_ovf0_cnt = value
                                    self.data_mem_ovf0_cnt.value_namespace = name_space
                                    self.data_mem_ovf0_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "data-mem-ovf1-cnt"):
                                    self.data_mem_ovf1_cnt = value
                                    self.data_mem_ovf1_cnt.value_namespace = name_space
                                    self.data_mem_ovf1_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "dmem-rd-cnt"):
                                    self.dmem_rd_cnt = value
                                    self.dmem_rd_cnt.value_namespace = name_space
                                    self.dmem_rd_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "fpoe-mem-ecc-derr-cnt"):
                                    self.fpoe_mem_ecc_derr_cnt = value
                                    self.fpoe_mem_ecc_derr_cnt.value_namespace = name_space
                                    self.fpoe_mem_ecc_derr_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "fpoe-mem-ecc-serr-cnt"):
                                    self.fpoe_mem_ecc_serr_cnt = value
                                    self.fpoe_mem_ecc_serr_cnt.value_namespace = name_space
                                    self.fpoe_mem_ecc_serr_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in0-cong-cnt"):
                                    self.in0_cong_cnt = value
                                    self.in0_cong_cnt.value_namespace = name_space
                                    self.in0_cong_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in0-drop-cnt"):
                                    self.in0_drop_cnt = value
                                    self.in0_drop_cnt.value_namespace = name_space
                                    self.in0_drop_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in0-ecc-derr-cnt"):
                                    self.in0_ecc_derr_cnt = value
                                    self.in0_ecc_derr_cnt.value_namespace = name_space
                                    self.in0_ecc_derr_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in0-ecc-serr-cnt"):
                                    self.in0_ecc_serr_cnt = value
                                    self.in0_ecc_serr_cnt.value_namespace = name_space
                                    self.in0_ecc_serr_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in0-fnc-err-cnt"):
                                    self.in0_fnc_err_cnt = value
                                    self.in0_fnc_err_cnt.value_namespace = name_space
                                    self.in0_fnc_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in0-pkt-cnt"):
                                    self.in0_pkt_cnt = value
                                    self.in0_pkt_cnt.value_namespace = name_space
                                    self.in0_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in0-shut-cnt"):
                                    self.in0_shut_cnt = value
                                    self.in0_shut_cnt.value_namespace = name_space
                                    self.in0_shut_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in1-cong-cnt"):
                                    self.in1_cong_cnt = value
                                    self.in1_cong_cnt.value_namespace = name_space
                                    self.in1_cong_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in1-drop-cnt"):
                                    self.in1_drop_cnt = value
                                    self.in1_drop_cnt.value_namespace = name_space
                                    self.in1_drop_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in1-ecc-derr-cnt"):
                                    self.in1_ecc_derr_cnt = value
                                    self.in1_ecc_derr_cnt.value_namespace = name_space
                                    self.in1_ecc_derr_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in1-ecc-serr-cnt"):
                                    self.in1_ecc_serr_cnt = value
                                    self.in1_ecc_serr_cnt.value_namespace = name_space
                                    self.in1_ecc_serr_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in1-fnc-err-cnt"):
                                    self.in1_fnc_err_cnt = value
                                    self.in1_fnc_err_cnt.value_namespace = name_space
                                    self.in1_fnc_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in1-pkt-cnt"):
                                    self.in1_pkt_cnt = value
                                    self.in1_pkt_cnt.value_namespace = name_space
                                    self.in1_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in1-shut-cnt"):
                                    self.in1_shut_cnt = value
                                    self.in1_shut_cnt.value_namespace = name_space
                                    self.in1_shut_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-dmem0-cnt"):
                                    self.in_dmem0_cnt = value
                                    self.in_dmem0_cnt.value_namespace = name_space
                                    self.in_dmem0_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-dmem1-cnt"):
                                    self.in_dmem1_cnt = value
                                    self.in_dmem1_cnt.value_namespace = name_space
                                    self.in_dmem1_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "null-poe-cnt"):
                                    self.null_poe_cnt = value
                                    self.null_poe_cnt.value_namespace = name_space
                                    self.null_poe_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-pkt-cnt"):
                                    self.out_pkt_cnt = value
                                    self.out_pkt_cnt.value_namespace = name_space
                                    self.out_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rate-cnt"):
                                    self.rate_cnt = value
                                    self.rate_cnt.value_namespace = name_space
                                    self.rate_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "shut-ack-cnt"):
                                    self.shut_ack_cnt = value
                                    self.shut_ack_cnt.value_namespace = name_space
                                    self.shut_ack_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "stop-thrsh-hit-cnt"):
                                    self.stop_thrsh_hit_cnt = value
                                    self.stop_thrsh_hit_cnt.value_namespace = name_space
                                    self.stop_thrsh_hit_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "tail-drop-msg-cnt"):
                                    self.tail_drop_msg_cnt = value
                                    self.tail_drop_msg_cnt.value_namespace = name_space
                                    self.tail_drop_msg_cnt.value_namespace_prefix = name_space_prefix


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("calc_rate",
                                                "ecc_1bit_err_uc0_0_cnt",
                                                "ecc_1bit_err_uc0_1_cnt",
                                                "ecc_1bit_err_uc1_0_cnt",
                                                "ecc_1bit_err_uc1_1_cnt",
                                                "ecc_1bit_err_uc2_0_cnt",
                                                "ecc_1bit_err_uc2_1_cnt",
                                                "ecc_2bit_err_uc0_0_cnt",
                                                "ecc_2bit_err_uc0_1_cnt",
                                                "ecc_2bit_err_uc1_0_cnt",
                                                "ecc_2bit_err_uc1_1_cnt",
                                                "ecc_2bit_err_uc2_0_cnt",
                                                "ecc_2bit_err_uc2_1_cnt",
                                                "fc_uc_0_1_trans_cnt",
                                                "fe_uc_sop_eop_pack_cnt",
                                                "in_full_line_uc0_cnt",
                                                "in_full_line_uc1_cnt",
                                                "in_full_line_uc2_cnt",
                                                "in_pkt_uc0_cnt",
                                                "in_pkt_uc1_cnt",
                                                "in_pkt_uc2_cnt",
                                                "out_pkt_uc_cnt",
                                                "pkt_ecc_err_drop_uc_cnt",
                                                "pkt_ecc_trunc_cnt_uc_cnt",
                                                "pkt_sop_drop_uc0_cnt",
                                                "pkt_sop_drop_uc1_cnt",
                                                "pkt_sop_drop_uc2_cnt",
                                                "pkt_trunc_eop_uc0_cnt",
                                                "pkt_trunc_eop_uc1_cnt",
                                                "pkt_trunc_eop_uc2_cnt",
                                                "rate_cnt") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeUcStats, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeUcStats, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.calc_rate.is_set or
                                    self.ecc_1bit_err_uc0_0_cnt.is_set or
                                    self.ecc_1bit_err_uc0_1_cnt.is_set or
                                    self.ecc_1bit_err_uc1_0_cnt.is_set or
                                    self.ecc_1bit_err_uc1_1_cnt.is_set or
                                    self.ecc_1bit_err_uc2_0_cnt.is_set or
                                    self.ecc_1bit_err_uc2_1_cnt.is_set or
                                    self.ecc_2bit_err_uc0_0_cnt.is_set or
                                    self.ecc_2bit_err_uc0_1_cnt.is_set or
                                    self.ecc_2bit_err_uc1_0_cnt.is_set or
                                    self.ecc_2bit_err_uc1_1_cnt.is_set or
                                    self.ecc_2bit_err_uc2_0_cnt.is_set or
                                    self.ecc_2bit_err_uc2_1_cnt.is_set or
                                    self.fc_uc_0_1_trans_cnt.is_set or
                                    self.fe_uc_sop_eop_pack_cnt.is_set or
                                    self.in_full_line_uc0_cnt.is_set or
                                    self.in_full_line_uc1_cnt.is_set or
                                    self.in_full_line_uc2_cnt.is_set or
                                    self.in_pkt_uc0_cnt.is_set or
                                    self.in_pkt_uc1_cnt.is_set or
                                    self.in_pkt_uc2_cnt.is_set or
                                    self.out_pkt_uc_cnt.is_set or
                                    self.pkt_ecc_err_drop_uc_cnt.is_set or
                                    self.pkt_ecc_trunc_cnt_uc_cnt.is_set or
                                    self.pkt_sop_drop_uc0_cnt.is_set or
                                    self.pkt_sop_drop_uc1_cnt.is_set or
                                    self.pkt_sop_drop_uc2_cnt.is_set or
                                    self.pkt_trunc_eop_uc0_cnt.is_set or
                                    self.pkt_trunc_eop_uc1_cnt.is_set or
                                    self.pkt_trunc_eop_uc2_cnt.is_set or
                                    self.rate_cnt.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.calc_rate.yfilter != YFilter.not_set or
                                    self.ecc_1bit_err_uc0_0_cnt.yfilter != YFilter.not_set or
                                    self.ecc_1bit_err_uc0_1_cnt.yfilter != YFilter.not_set or
                                    self.ecc_1bit_err_uc1_0_cnt.yfilter != YFilter.not_set or
                                    self.ecc_1bit_err_uc1_1_cnt.yfilter != YFilter.not_set or
                                    self.ecc_1bit_err_uc2_0_cnt.yfilter != YFilter.not_set or
                                    self.ecc_1bit_err_uc2_1_cnt.yfilter != YFilter.not_set or
                                    self.ecc_2bit_err_uc0_0_cnt.yfilter != YFilter.not_set or
                                    self.ecc_2bit_err_uc0_1_cnt.yfilter != YFilter.not_set or
                                    self.ecc_2bit_err_uc1_0_cnt.yfilter != YFilter.not_set or
                                    self.ecc_2bit_err_uc1_1_cnt.yfilter != YFilter.not_set or
                                    self.ecc_2bit_err_uc2_0_cnt.yfilter != YFilter.not_set or
                                    self.ecc_2bit_err_uc2_1_cnt.yfilter != YFilter.not_set or
                                    self.fc_uc_0_1_trans_cnt.yfilter != YFilter.not_set or
                                    self.fe_uc_sop_eop_pack_cnt.yfilter != YFilter.not_set or
                                    self.in_full_line_uc0_cnt.yfilter != YFilter.not_set or
                                    self.in_full_line_uc1_cnt.yfilter != YFilter.not_set or
                                    self.in_full_line_uc2_cnt.yfilter != YFilter.not_set or
                                    self.in_pkt_uc0_cnt.yfilter != YFilter.not_set or
                                    self.in_pkt_uc1_cnt.yfilter != YFilter.not_set or
                                    self.in_pkt_uc2_cnt.yfilter != YFilter.not_set or
                                    self.out_pkt_uc_cnt.yfilter != YFilter.not_set or
                                    self.pkt_ecc_err_drop_uc_cnt.yfilter != YFilter.not_set or
                                    self.pkt_ecc_trunc_cnt_uc_cnt.yfilter != YFilter.not_set or
                                    self.pkt_sop_drop_uc0_cnt.yfilter != YFilter.not_set or
                                    self.pkt_sop_drop_uc1_cnt.yfilter != YFilter.not_set or
                                    self.pkt_sop_drop_uc2_cnt.yfilter != YFilter.not_set or
                                    self.pkt_trunc_eop_uc0_cnt.yfilter != YFilter.not_set or
                                    self.pkt_trunc_eop_uc1_cnt.yfilter != YFilter.not_set or
                                    self.pkt_trunc_eop_uc2_cnt.yfilter != YFilter.not_set or
                                    self.rate_cnt.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pe-uc-stats" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.calc_rate.is_set or self.calc_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.calc_rate.get_name_leafdata())
                                if (self.ecc_1bit_err_uc0_0_cnt.is_set or self.ecc_1bit_err_uc0_0_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ecc_1bit_err_uc0_0_cnt.get_name_leafdata())
                                if (self.ecc_1bit_err_uc0_1_cnt.is_set or self.ecc_1bit_err_uc0_1_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ecc_1bit_err_uc0_1_cnt.get_name_leafdata())
                                if (self.ecc_1bit_err_uc1_0_cnt.is_set or self.ecc_1bit_err_uc1_0_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ecc_1bit_err_uc1_0_cnt.get_name_leafdata())
                                if (self.ecc_1bit_err_uc1_1_cnt.is_set or self.ecc_1bit_err_uc1_1_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ecc_1bit_err_uc1_1_cnt.get_name_leafdata())
                                if (self.ecc_1bit_err_uc2_0_cnt.is_set or self.ecc_1bit_err_uc2_0_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ecc_1bit_err_uc2_0_cnt.get_name_leafdata())
                                if (self.ecc_1bit_err_uc2_1_cnt.is_set or self.ecc_1bit_err_uc2_1_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ecc_1bit_err_uc2_1_cnt.get_name_leafdata())
                                if (self.ecc_2bit_err_uc0_0_cnt.is_set or self.ecc_2bit_err_uc0_0_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ecc_2bit_err_uc0_0_cnt.get_name_leafdata())
                                if (self.ecc_2bit_err_uc0_1_cnt.is_set or self.ecc_2bit_err_uc0_1_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ecc_2bit_err_uc0_1_cnt.get_name_leafdata())
                                if (self.ecc_2bit_err_uc1_0_cnt.is_set or self.ecc_2bit_err_uc1_0_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ecc_2bit_err_uc1_0_cnt.get_name_leafdata())
                                if (self.ecc_2bit_err_uc1_1_cnt.is_set or self.ecc_2bit_err_uc1_1_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ecc_2bit_err_uc1_1_cnt.get_name_leafdata())
                                if (self.ecc_2bit_err_uc2_0_cnt.is_set or self.ecc_2bit_err_uc2_0_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ecc_2bit_err_uc2_0_cnt.get_name_leafdata())
                                if (self.ecc_2bit_err_uc2_1_cnt.is_set or self.ecc_2bit_err_uc2_1_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ecc_2bit_err_uc2_1_cnt.get_name_leafdata())
                                if (self.fc_uc_0_1_trans_cnt.is_set or self.fc_uc_0_1_trans_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fc_uc_0_1_trans_cnt.get_name_leafdata())
                                if (self.fe_uc_sop_eop_pack_cnt.is_set or self.fe_uc_sop_eop_pack_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fe_uc_sop_eop_pack_cnt.get_name_leafdata())
                                if (self.in_full_line_uc0_cnt.is_set or self.in_full_line_uc0_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_full_line_uc0_cnt.get_name_leafdata())
                                if (self.in_full_line_uc1_cnt.is_set or self.in_full_line_uc1_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_full_line_uc1_cnt.get_name_leafdata())
                                if (self.in_full_line_uc2_cnt.is_set or self.in_full_line_uc2_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_full_line_uc2_cnt.get_name_leafdata())
                                if (self.in_pkt_uc0_cnt.is_set or self.in_pkt_uc0_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_pkt_uc0_cnt.get_name_leafdata())
                                if (self.in_pkt_uc1_cnt.is_set or self.in_pkt_uc1_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_pkt_uc1_cnt.get_name_leafdata())
                                if (self.in_pkt_uc2_cnt.is_set or self.in_pkt_uc2_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_pkt_uc2_cnt.get_name_leafdata())
                                if (self.out_pkt_uc_cnt.is_set or self.out_pkt_uc_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_pkt_uc_cnt.get_name_leafdata())
                                if (self.pkt_ecc_err_drop_uc_cnt.is_set or self.pkt_ecc_err_drop_uc_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_ecc_err_drop_uc_cnt.get_name_leafdata())
                                if (self.pkt_ecc_trunc_cnt_uc_cnt.is_set or self.pkt_ecc_trunc_cnt_uc_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_ecc_trunc_cnt_uc_cnt.get_name_leafdata())
                                if (self.pkt_sop_drop_uc0_cnt.is_set or self.pkt_sop_drop_uc0_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_sop_drop_uc0_cnt.get_name_leafdata())
                                if (self.pkt_sop_drop_uc1_cnt.is_set or self.pkt_sop_drop_uc1_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_sop_drop_uc1_cnt.get_name_leafdata())
                                if (self.pkt_sop_drop_uc2_cnt.is_set or self.pkt_sop_drop_uc2_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_sop_drop_uc2_cnt.get_name_leafdata())
                                if (self.pkt_trunc_eop_uc0_cnt.is_set or self.pkt_trunc_eop_uc0_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_trunc_eop_uc0_cnt.get_name_leafdata())
                                if (self.pkt_trunc_eop_uc1_cnt.is_set or self.pkt_trunc_eop_uc1_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_trunc_eop_uc1_cnt.get_name_leafdata())
                                if (self.pkt_trunc_eop_uc2_cnt.is_set or self.pkt_trunc_eop_uc2_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_trunc_eop_uc2_cnt.get_name_leafdata())
                                if (self.rate_cnt.is_set or self.rate_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rate_cnt.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "calc-rate" or name == "ecc-1bit-err-uc0-0-cnt" or name == "ecc-1bit-err-uc0-1-cnt" or name == "ecc-1bit-err-uc1-0-cnt" or name == "ecc-1bit-err-uc1-1-cnt" or name == "ecc-1bit-err-uc2-0-cnt" or name == "ecc-1bit-err-uc2-1-cnt" or name == "ecc-2bit-err-uc0-0-cnt" or name == "ecc-2bit-err-uc0-1-cnt" or name == "ecc-2bit-err-uc1-0-cnt" or name == "ecc-2bit-err-uc1-1-cnt" or name == "ecc-2bit-err-uc2-0-cnt" or name == "ecc-2bit-err-uc2-1-cnt" or name == "fc-uc-0-1-trans-cnt" or name == "fe-uc-sop-eop-pack-cnt" or name == "in-full-line-uc0-cnt" or name == "in-full-line-uc1-cnt" or name == "in-full-line-uc2-cnt" or name == "in-pkt-uc0-cnt" or name == "in-pkt-uc1-cnt" or name == "in-pkt-uc2-cnt" or name == "out-pkt-uc-cnt" or name == "pkt-ecc-err-drop-uc-cnt" or name == "pkt-ecc-trunc-cnt-uc-cnt" or name == "pkt-sop-drop-uc0-cnt" or name == "pkt-sop-drop-uc1-cnt" or name == "pkt-sop-drop-uc2-cnt" or name == "pkt-trunc-eop-uc0-cnt" or name == "pkt-trunc-eop-uc1-cnt" or name == "pkt-trunc-eop-uc2-cnt" or name == "rate-cnt"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "calc-rate"):
                                    self.calc_rate = value
                                    self.calc_rate.value_namespace = name_space
                                    self.calc_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "ecc-1bit-err-uc0-0-cnt"):
                                    self.ecc_1bit_err_uc0_0_cnt = value
                                    self.ecc_1bit_err_uc0_0_cnt.value_namespace = name_space
                                    self.ecc_1bit_err_uc0_0_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "ecc-1bit-err-uc0-1-cnt"):
                                    self.ecc_1bit_err_uc0_1_cnt = value
                                    self.ecc_1bit_err_uc0_1_cnt.value_namespace = name_space
                                    self.ecc_1bit_err_uc0_1_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "ecc-1bit-err-uc1-0-cnt"):
                                    self.ecc_1bit_err_uc1_0_cnt = value
                                    self.ecc_1bit_err_uc1_0_cnt.value_namespace = name_space
                                    self.ecc_1bit_err_uc1_0_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "ecc-1bit-err-uc1-1-cnt"):
                                    self.ecc_1bit_err_uc1_1_cnt = value
                                    self.ecc_1bit_err_uc1_1_cnt.value_namespace = name_space
                                    self.ecc_1bit_err_uc1_1_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "ecc-1bit-err-uc2-0-cnt"):
                                    self.ecc_1bit_err_uc2_0_cnt = value
                                    self.ecc_1bit_err_uc2_0_cnt.value_namespace = name_space
                                    self.ecc_1bit_err_uc2_0_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "ecc-1bit-err-uc2-1-cnt"):
                                    self.ecc_1bit_err_uc2_1_cnt = value
                                    self.ecc_1bit_err_uc2_1_cnt.value_namespace = name_space
                                    self.ecc_1bit_err_uc2_1_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "ecc-2bit-err-uc0-0-cnt"):
                                    self.ecc_2bit_err_uc0_0_cnt = value
                                    self.ecc_2bit_err_uc0_0_cnt.value_namespace = name_space
                                    self.ecc_2bit_err_uc0_0_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "ecc-2bit-err-uc0-1-cnt"):
                                    self.ecc_2bit_err_uc0_1_cnt = value
                                    self.ecc_2bit_err_uc0_1_cnt.value_namespace = name_space
                                    self.ecc_2bit_err_uc0_1_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "ecc-2bit-err-uc1-0-cnt"):
                                    self.ecc_2bit_err_uc1_0_cnt = value
                                    self.ecc_2bit_err_uc1_0_cnt.value_namespace = name_space
                                    self.ecc_2bit_err_uc1_0_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "ecc-2bit-err-uc1-1-cnt"):
                                    self.ecc_2bit_err_uc1_1_cnt = value
                                    self.ecc_2bit_err_uc1_1_cnt.value_namespace = name_space
                                    self.ecc_2bit_err_uc1_1_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "ecc-2bit-err-uc2-0-cnt"):
                                    self.ecc_2bit_err_uc2_0_cnt = value
                                    self.ecc_2bit_err_uc2_0_cnt.value_namespace = name_space
                                    self.ecc_2bit_err_uc2_0_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "ecc-2bit-err-uc2-1-cnt"):
                                    self.ecc_2bit_err_uc2_1_cnt = value
                                    self.ecc_2bit_err_uc2_1_cnt.value_namespace = name_space
                                    self.ecc_2bit_err_uc2_1_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "fc-uc-0-1-trans-cnt"):
                                    self.fc_uc_0_1_trans_cnt = value
                                    self.fc_uc_0_1_trans_cnt.value_namespace = name_space
                                    self.fc_uc_0_1_trans_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "fe-uc-sop-eop-pack-cnt"):
                                    self.fe_uc_sop_eop_pack_cnt = value
                                    self.fe_uc_sop_eop_pack_cnt.value_namespace = name_space
                                    self.fe_uc_sop_eop_pack_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-full-line-uc0-cnt"):
                                    self.in_full_line_uc0_cnt = value
                                    self.in_full_line_uc0_cnt.value_namespace = name_space
                                    self.in_full_line_uc0_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-full-line-uc1-cnt"):
                                    self.in_full_line_uc1_cnt = value
                                    self.in_full_line_uc1_cnt.value_namespace = name_space
                                    self.in_full_line_uc1_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-full-line-uc2-cnt"):
                                    self.in_full_line_uc2_cnt = value
                                    self.in_full_line_uc2_cnt.value_namespace = name_space
                                    self.in_full_line_uc2_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-pkt-uc0-cnt"):
                                    self.in_pkt_uc0_cnt = value
                                    self.in_pkt_uc0_cnt.value_namespace = name_space
                                    self.in_pkt_uc0_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-pkt-uc1-cnt"):
                                    self.in_pkt_uc1_cnt = value
                                    self.in_pkt_uc1_cnt.value_namespace = name_space
                                    self.in_pkt_uc1_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-pkt-uc2-cnt"):
                                    self.in_pkt_uc2_cnt = value
                                    self.in_pkt_uc2_cnt.value_namespace = name_space
                                    self.in_pkt_uc2_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-pkt-uc-cnt"):
                                    self.out_pkt_uc_cnt = value
                                    self.out_pkt_uc_cnt.value_namespace = name_space
                                    self.out_pkt_uc_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-ecc-err-drop-uc-cnt"):
                                    self.pkt_ecc_err_drop_uc_cnt = value
                                    self.pkt_ecc_err_drop_uc_cnt.value_namespace = name_space
                                    self.pkt_ecc_err_drop_uc_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-ecc-trunc-cnt-uc-cnt"):
                                    self.pkt_ecc_trunc_cnt_uc_cnt = value
                                    self.pkt_ecc_trunc_cnt_uc_cnt.value_namespace = name_space
                                    self.pkt_ecc_trunc_cnt_uc_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-sop-drop-uc0-cnt"):
                                    self.pkt_sop_drop_uc0_cnt = value
                                    self.pkt_sop_drop_uc0_cnt.value_namespace = name_space
                                    self.pkt_sop_drop_uc0_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-sop-drop-uc1-cnt"):
                                    self.pkt_sop_drop_uc1_cnt = value
                                    self.pkt_sop_drop_uc1_cnt.value_namespace = name_space
                                    self.pkt_sop_drop_uc1_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-sop-drop-uc2-cnt"):
                                    self.pkt_sop_drop_uc2_cnt = value
                                    self.pkt_sop_drop_uc2_cnt.value_namespace = name_space
                                    self.pkt_sop_drop_uc2_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-trunc-eop-uc0-cnt"):
                                    self.pkt_trunc_eop_uc0_cnt = value
                                    self.pkt_trunc_eop_uc0_cnt.value_namespace = name_space
                                    self.pkt_trunc_eop_uc0_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-trunc-eop-uc1-cnt"):
                                    self.pkt_trunc_eop_uc1_cnt = value
                                    self.pkt_trunc_eop_uc1_cnt.value_namespace = name_space
                                    self.pkt_trunc_eop_uc1_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-trunc-eop-uc2-cnt"):
                                    self.pkt_trunc_eop_uc2_cnt = value
                                    self.pkt_trunc_eop_uc2_cnt.value_namespace = name_space
                                    self.pkt_trunc_eop_uc2_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rate-cnt"):
                                    self.rate_cnt = value
                                    self.rate_cnt.value_namespace = name_space
                                    self.rate_cnt.value_namespace_prefix = name_space_prefix


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("calc_rate",
                                                "ecc_1bit_err_mc0_cnt",
                                                "ecc_1bit_err_mc1_cnt",
                                                "ecc_1bit_err_mc2_cnt",
                                                "ecc_2bit_err_mc0_cnt",
                                                "ecc_2bit_err_mc1_cnt",
                                                "ecc_2bit_err_mc2_cnt",
                                                "fc_mc_0_1_trans_cnt",
                                                "fe_mc_sop_eop_pack_cnt",
                                                "in_full_line_mc_cnt",
                                                "in_pkt_mc_cnt",
                                                "out_pkt_mc_cnt",
                                                "pkt_ecc_err_drop_mc_cnt",
                                                "pkt_ecc_err_trunc_cnt_mc_cnt",
                                                "pkt_sop_drop_mc_cnt",
                                                "pkt_trunc_eop_mc_cnt",
                                                "rate_cnt") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeMcStats, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeMcStats, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.calc_rate.is_set or
                                    self.ecc_1bit_err_mc0_cnt.is_set or
                                    self.ecc_1bit_err_mc1_cnt.is_set or
                                    self.ecc_1bit_err_mc2_cnt.is_set or
                                    self.ecc_2bit_err_mc0_cnt.is_set or
                                    self.ecc_2bit_err_mc1_cnt.is_set or
                                    self.ecc_2bit_err_mc2_cnt.is_set or
                                    self.fc_mc_0_1_trans_cnt.is_set or
                                    self.fe_mc_sop_eop_pack_cnt.is_set or
                                    self.in_full_line_mc_cnt.is_set or
                                    self.in_pkt_mc_cnt.is_set or
                                    self.out_pkt_mc_cnt.is_set or
                                    self.pkt_ecc_err_drop_mc_cnt.is_set or
                                    self.pkt_ecc_err_trunc_cnt_mc_cnt.is_set or
                                    self.pkt_sop_drop_mc_cnt.is_set or
                                    self.pkt_trunc_eop_mc_cnt.is_set or
                                    self.rate_cnt.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.calc_rate.yfilter != YFilter.not_set or
                                    self.ecc_1bit_err_mc0_cnt.yfilter != YFilter.not_set or
                                    self.ecc_1bit_err_mc1_cnt.yfilter != YFilter.not_set or
                                    self.ecc_1bit_err_mc2_cnt.yfilter != YFilter.not_set or
                                    self.ecc_2bit_err_mc0_cnt.yfilter != YFilter.not_set or
                                    self.ecc_2bit_err_mc1_cnt.yfilter != YFilter.not_set or
                                    self.ecc_2bit_err_mc2_cnt.yfilter != YFilter.not_set or
                                    self.fc_mc_0_1_trans_cnt.yfilter != YFilter.not_set or
                                    self.fe_mc_sop_eop_pack_cnt.yfilter != YFilter.not_set or
                                    self.in_full_line_mc_cnt.yfilter != YFilter.not_set or
                                    self.in_pkt_mc_cnt.yfilter != YFilter.not_set or
                                    self.out_pkt_mc_cnt.yfilter != YFilter.not_set or
                                    self.pkt_ecc_err_drop_mc_cnt.yfilter != YFilter.not_set or
                                    self.pkt_ecc_err_trunc_cnt_mc_cnt.yfilter != YFilter.not_set or
                                    self.pkt_sop_drop_mc_cnt.yfilter != YFilter.not_set or
                                    self.pkt_trunc_eop_mc_cnt.yfilter != YFilter.not_set or
                                    self.rate_cnt.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pe-mc-stats" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.calc_rate.is_set or self.calc_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.calc_rate.get_name_leafdata())
                                if (self.ecc_1bit_err_mc0_cnt.is_set or self.ecc_1bit_err_mc0_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ecc_1bit_err_mc0_cnt.get_name_leafdata())
                                if (self.ecc_1bit_err_mc1_cnt.is_set or self.ecc_1bit_err_mc1_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ecc_1bit_err_mc1_cnt.get_name_leafdata())
                                if (self.ecc_1bit_err_mc2_cnt.is_set or self.ecc_1bit_err_mc2_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ecc_1bit_err_mc2_cnt.get_name_leafdata())
                                if (self.ecc_2bit_err_mc0_cnt.is_set or self.ecc_2bit_err_mc0_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ecc_2bit_err_mc0_cnt.get_name_leafdata())
                                if (self.ecc_2bit_err_mc1_cnt.is_set or self.ecc_2bit_err_mc1_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ecc_2bit_err_mc1_cnt.get_name_leafdata())
                                if (self.ecc_2bit_err_mc2_cnt.is_set or self.ecc_2bit_err_mc2_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ecc_2bit_err_mc2_cnt.get_name_leafdata())
                                if (self.fc_mc_0_1_trans_cnt.is_set or self.fc_mc_0_1_trans_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fc_mc_0_1_trans_cnt.get_name_leafdata())
                                if (self.fe_mc_sop_eop_pack_cnt.is_set or self.fe_mc_sop_eop_pack_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fe_mc_sop_eop_pack_cnt.get_name_leafdata())
                                if (self.in_full_line_mc_cnt.is_set or self.in_full_line_mc_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_full_line_mc_cnt.get_name_leafdata())
                                if (self.in_pkt_mc_cnt.is_set or self.in_pkt_mc_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_pkt_mc_cnt.get_name_leafdata())
                                if (self.out_pkt_mc_cnt.is_set or self.out_pkt_mc_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_pkt_mc_cnt.get_name_leafdata())
                                if (self.pkt_ecc_err_drop_mc_cnt.is_set or self.pkt_ecc_err_drop_mc_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_ecc_err_drop_mc_cnt.get_name_leafdata())
                                if (self.pkt_ecc_err_trunc_cnt_mc_cnt.is_set or self.pkt_ecc_err_trunc_cnt_mc_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_ecc_err_trunc_cnt_mc_cnt.get_name_leafdata())
                                if (self.pkt_sop_drop_mc_cnt.is_set or self.pkt_sop_drop_mc_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_sop_drop_mc_cnt.get_name_leafdata())
                                if (self.pkt_trunc_eop_mc_cnt.is_set or self.pkt_trunc_eop_mc_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pkt_trunc_eop_mc_cnt.get_name_leafdata())
                                if (self.rate_cnt.is_set or self.rate_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rate_cnt.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "calc-rate" or name == "ecc-1bit-err-mc0-cnt" or name == "ecc-1bit-err-mc1-cnt" or name == "ecc-1bit-err-mc2-cnt" or name == "ecc-2bit-err-mc0-cnt" or name == "ecc-2bit-err-mc1-cnt" or name == "ecc-2bit-err-mc2-cnt" or name == "fc-mc-0-1-trans-cnt" or name == "fe-mc-sop-eop-pack-cnt" or name == "in-full-line-mc-cnt" or name == "in-pkt-mc-cnt" or name == "out-pkt-mc-cnt" or name == "pkt-ecc-err-drop-mc-cnt" or name == "pkt-ecc-err-trunc-cnt-mc-cnt" or name == "pkt-sop-drop-mc-cnt" or name == "pkt-trunc-eop-mc-cnt" or name == "rate-cnt"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "calc-rate"):
                                    self.calc_rate = value
                                    self.calc_rate.value_namespace = name_space
                                    self.calc_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "ecc-1bit-err-mc0-cnt"):
                                    self.ecc_1bit_err_mc0_cnt = value
                                    self.ecc_1bit_err_mc0_cnt.value_namespace = name_space
                                    self.ecc_1bit_err_mc0_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "ecc-1bit-err-mc1-cnt"):
                                    self.ecc_1bit_err_mc1_cnt = value
                                    self.ecc_1bit_err_mc1_cnt.value_namespace = name_space
                                    self.ecc_1bit_err_mc1_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "ecc-1bit-err-mc2-cnt"):
                                    self.ecc_1bit_err_mc2_cnt = value
                                    self.ecc_1bit_err_mc2_cnt.value_namespace = name_space
                                    self.ecc_1bit_err_mc2_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "ecc-2bit-err-mc0-cnt"):
                                    self.ecc_2bit_err_mc0_cnt = value
                                    self.ecc_2bit_err_mc0_cnt.value_namespace = name_space
                                    self.ecc_2bit_err_mc0_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "ecc-2bit-err-mc1-cnt"):
                                    self.ecc_2bit_err_mc1_cnt = value
                                    self.ecc_2bit_err_mc1_cnt.value_namespace = name_space
                                    self.ecc_2bit_err_mc1_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "ecc-2bit-err-mc2-cnt"):
                                    self.ecc_2bit_err_mc2_cnt = value
                                    self.ecc_2bit_err_mc2_cnt.value_namespace = name_space
                                    self.ecc_2bit_err_mc2_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "fc-mc-0-1-trans-cnt"):
                                    self.fc_mc_0_1_trans_cnt = value
                                    self.fc_mc_0_1_trans_cnt.value_namespace = name_space
                                    self.fc_mc_0_1_trans_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "fe-mc-sop-eop-pack-cnt"):
                                    self.fe_mc_sop_eop_pack_cnt = value
                                    self.fe_mc_sop_eop_pack_cnt.value_namespace = name_space
                                    self.fe_mc_sop_eop_pack_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-full-line-mc-cnt"):
                                    self.in_full_line_mc_cnt = value
                                    self.in_full_line_mc_cnt.value_namespace = name_space
                                    self.in_full_line_mc_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-pkt-mc-cnt"):
                                    self.in_pkt_mc_cnt = value
                                    self.in_pkt_mc_cnt.value_namespace = name_space
                                    self.in_pkt_mc_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-pkt-mc-cnt"):
                                    self.out_pkt_mc_cnt = value
                                    self.out_pkt_mc_cnt.value_namespace = name_space
                                    self.out_pkt_mc_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-ecc-err-drop-mc-cnt"):
                                    self.pkt_ecc_err_drop_mc_cnt = value
                                    self.pkt_ecc_err_drop_mc_cnt.value_namespace = name_space
                                    self.pkt_ecc_err_drop_mc_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-ecc-err-trunc-cnt-mc-cnt"):
                                    self.pkt_ecc_err_trunc_cnt_mc_cnt = value
                                    self.pkt_ecc_err_trunc_cnt_mc_cnt.value_namespace = name_space
                                    self.pkt_ecc_err_trunc_cnt_mc_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-sop-drop-mc-cnt"):
                                    self.pkt_sop_drop_mc_cnt = value
                                    self.pkt_sop_drop_mc_cnt.value_namespace = name_space
                                    self.pkt_sop_drop_mc_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "pkt-trunc-eop-mc-cnt"):
                                    self.pkt_trunc_eop_mc_cnt = value
                                    self.pkt_trunc_eop_mc_cnt.value_namespace = name_space
                                    self.pkt_trunc_eop_mc_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rate-cnt"):
                                    self.rate_cnt = value
                                    self.rate_cnt.value_namespace = name_space
                                    self.rate_cnt.value_namespace_prefix = name_space_prefix


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("calc_rate",
                                                "congn_pkt_cnt",
                                                "fc_cc_0_1_trans_cnt",
                                                "in_pkt_cnt",
                                                "mem0_drop_pkt_cnt",
                                                "mem0_ecc_double_err_cnt",
                                                "mem0_ecc_single_err_cnt",
                                                "mem1_drop_pkt_cnt",
                                                "mem1_ecc_double_err_cnt",
                                                "mem1_ecc_single_err_cnt",
                                                "out_path0_pkt_cnt",
                                                "out_path1_pkt_cnt",
                                                "rate_cnt",
                                                "xbar_ecc_double_err_cnt",
                                                "xbar_ecc_drop_pkt_cnt",
                                                "xbar_ecc_single_err_cnt") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeCcStats, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeCcStats, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.calc_rate.is_set or
                                    self.congn_pkt_cnt.is_set or
                                    self.fc_cc_0_1_trans_cnt.is_set or
                                    self.in_pkt_cnt.is_set or
                                    self.mem0_drop_pkt_cnt.is_set or
                                    self.mem0_ecc_double_err_cnt.is_set or
                                    self.mem0_ecc_single_err_cnt.is_set or
                                    self.mem1_drop_pkt_cnt.is_set or
                                    self.mem1_ecc_double_err_cnt.is_set or
                                    self.mem1_ecc_single_err_cnt.is_set or
                                    self.out_path0_pkt_cnt.is_set or
                                    self.out_path1_pkt_cnt.is_set or
                                    self.rate_cnt.is_set or
                                    self.xbar_ecc_double_err_cnt.is_set or
                                    self.xbar_ecc_drop_pkt_cnt.is_set or
                                    self.xbar_ecc_single_err_cnt.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.calc_rate.yfilter != YFilter.not_set or
                                    self.congn_pkt_cnt.yfilter != YFilter.not_set or
                                    self.fc_cc_0_1_trans_cnt.yfilter != YFilter.not_set or
                                    self.in_pkt_cnt.yfilter != YFilter.not_set or
                                    self.mem0_drop_pkt_cnt.yfilter != YFilter.not_set or
                                    self.mem0_ecc_double_err_cnt.yfilter != YFilter.not_set or
                                    self.mem0_ecc_single_err_cnt.yfilter != YFilter.not_set or
                                    self.mem1_drop_pkt_cnt.yfilter != YFilter.not_set or
                                    self.mem1_ecc_double_err_cnt.yfilter != YFilter.not_set or
                                    self.mem1_ecc_single_err_cnt.yfilter != YFilter.not_set or
                                    self.out_path0_pkt_cnt.yfilter != YFilter.not_set or
                                    self.out_path1_pkt_cnt.yfilter != YFilter.not_set or
                                    self.rate_cnt.yfilter != YFilter.not_set or
                                    self.xbar_ecc_double_err_cnt.yfilter != YFilter.not_set or
                                    self.xbar_ecc_drop_pkt_cnt.yfilter != YFilter.not_set or
                                    self.xbar_ecc_single_err_cnt.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pe-cc-stats" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.calc_rate.is_set or self.calc_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.calc_rate.get_name_leafdata())
                                if (self.congn_pkt_cnt.is_set or self.congn_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.congn_pkt_cnt.get_name_leafdata())
                                if (self.fc_cc_0_1_trans_cnt.is_set or self.fc_cc_0_1_trans_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fc_cc_0_1_trans_cnt.get_name_leafdata())
                                if (self.in_pkt_cnt.is_set or self.in_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_pkt_cnt.get_name_leafdata())
                                if (self.mem0_drop_pkt_cnt.is_set or self.mem0_drop_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mem0_drop_pkt_cnt.get_name_leafdata())
                                if (self.mem0_ecc_double_err_cnt.is_set or self.mem0_ecc_double_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mem0_ecc_double_err_cnt.get_name_leafdata())
                                if (self.mem0_ecc_single_err_cnt.is_set or self.mem0_ecc_single_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mem0_ecc_single_err_cnt.get_name_leafdata())
                                if (self.mem1_drop_pkt_cnt.is_set or self.mem1_drop_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mem1_drop_pkt_cnt.get_name_leafdata())
                                if (self.mem1_ecc_double_err_cnt.is_set or self.mem1_ecc_double_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mem1_ecc_double_err_cnt.get_name_leafdata())
                                if (self.mem1_ecc_single_err_cnt.is_set or self.mem1_ecc_single_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mem1_ecc_single_err_cnt.get_name_leafdata())
                                if (self.out_path0_pkt_cnt.is_set or self.out_path0_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_path0_pkt_cnt.get_name_leafdata())
                                if (self.out_path1_pkt_cnt.is_set or self.out_path1_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_path1_pkt_cnt.get_name_leafdata())
                                if (self.rate_cnt.is_set or self.rate_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rate_cnt.get_name_leafdata())
                                if (self.xbar_ecc_double_err_cnt.is_set or self.xbar_ecc_double_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.xbar_ecc_double_err_cnt.get_name_leafdata())
                                if (self.xbar_ecc_drop_pkt_cnt.is_set or self.xbar_ecc_drop_pkt_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.xbar_ecc_drop_pkt_cnt.get_name_leafdata())
                                if (self.xbar_ecc_single_err_cnt.is_set or self.xbar_ecc_single_err_cnt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.xbar_ecc_single_err_cnt.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "calc-rate" or name == "congn-pkt-cnt" or name == "fc-cc-0-1-trans-cnt" or name == "in-pkt-cnt" or name == "mem0-drop-pkt-cnt" or name == "mem0-ecc-double-err-cnt" or name == "mem0-ecc-single-err-cnt" or name == "mem1-drop-pkt-cnt" or name == "mem1-ecc-double-err-cnt" or name == "mem1-ecc-single-err-cnt" or name == "out-path0-pkt-cnt" or name == "out-path1-pkt-cnt" or name == "rate-cnt" or name == "xbar-ecc-double-err-cnt" or name == "xbar-ecc-drop-pkt-cnt" or name == "xbar-ecc-single-err-cnt"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "calc-rate"):
                                    self.calc_rate = value
                                    self.calc_rate.value_namespace = name_space
                                    self.calc_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "congn-pkt-cnt"):
                                    self.congn_pkt_cnt = value
                                    self.congn_pkt_cnt.value_namespace = name_space
                                    self.congn_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "fc-cc-0-1-trans-cnt"):
                                    self.fc_cc_0_1_trans_cnt = value
                                    self.fc_cc_0_1_trans_cnt.value_namespace = name_space
                                    self.fc_cc_0_1_trans_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-pkt-cnt"):
                                    self.in_pkt_cnt = value
                                    self.in_pkt_cnt.value_namespace = name_space
                                    self.in_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "mem0-drop-pkt-cnt"):
                                    self.mem0_drop_pkt_cnt = value
                                    self.mem0_drop_pkt_cnt.value_namespace = name_space
                                    self.mem0_drop_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "mem0-ecc-double-err-cnt"):
                                    self.mem0_ecc_double_err_cnt = value
                                    self.mem0_ecc_double_err_cnt.value_namespace = name_space
                                    self.mem0_ecc_double_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "mem0-ecc-single-err-cnt"):
                                    self.mem0_ecc_single_err_cnt = value
                                    self.mem0_ecc_single_err_cnt.value_namespace = name_space
                                    self.mem0_ecc_single_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "mem1-drop-pkt-cnt"):
                                    self.mem1_drop_pkt_cnt = value
                                    self.mem1_drop_pkt_cnt.value_namespace = name_space
                                    self.mem1_drop_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "mem1-ecc-double-err-cnt"):
                                    self.mem1_ecc_double_err_cnt = value
                                    self.mem1_ecc_double_err_cnt.value_namespace = name_space
                                    self.mem1_ecc_double_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "mem1-ecc-single-err-cnt"):
                                    self.mem1_ecc_single_err_cnt = value
                                    self.mem1_ecc_single_err_cnt.value_namespace = name_space
                                    self.mem1_ecc_single_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-path0-pkt-cnt"):
                                    self.out_path0_pkt_cnt = value
                                    self.out_path0_pkt_cnt.value_namespace = name_space
                                    self.out_path0_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-path1-pkt-cnt"):
                                    self.out_path1_pkt_cnt = value
                                    self.out_path1_pkt_cnt.value_namespace = name_space
                                    self.out_path1_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "rate-cnt"):
                                    self.rate_cnt = value
                                    self.rate_cnt.value_namespace = name_space
                                    self.rate_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "xbar-ecc-double-err-cnt"):
                                    self.xbar_ecc_double_err_cnt = value
                                    self.xbar_ecc_double_err_cnt.value_namespace = name_space
                                    self.xbar_ecc_double_err_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "xbar-ecc-drop-pkt-cnt"):
                                    self.xbar_ecc_drop_pkt_cnt = value
                                    self.xbar_ecc_drop_pkt_cnt.value_namespace = name_space
                                    self.xbar_ecc_drop_pkt_cnt.value_namespace_prefix = name_space_prefix
                                if(value_path == "xbar-ecc-single-err-cnt"):
                                    self.xbar_ecc_single_err_cnt = value
                                    self.xbar_ecc_single_err_cnt.value_namespace = name_space
                                    self.xbar_ecc_single_err_cnt.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.asic_id.is_set or
                                self.internal_err_cnt.is_set or
                                self.port.is_set or
                                (self.ca_stats is not None and self.ca_stats.has_data()) or
                                (self.ma_stats is not None and self.ma_stats.has_data()) or
                                (self.pe_cc_stats is not None and self.pe_cc_stats.has_data()) or
                                (self.pe_mc_stats is not None and self.pe_mc_stats.has_data()) or
                                (self.pe_stats is not None and self.pe_stats.has_data()) or
                                (self.pe_uc_stats is not None and self.pe_uc_stats.has_data()) or
                                (self.pi_cc_stats is not None and self.pi_cc_stats.has_data()) or
                                (self.pi_mc_stats is not None and self.pi_mc_stats.has_data()) or
                                (self.pi_stats is not None and self.pi_stats.has_data()) or
                                (self.pi_uc_stats is not None and self.pi_uc_stats.has_data()) or
                                (self.ua0_stats is not None and self.ua0_stats.has_data()) or
                                (self.ua1_stats is not None and self.ua1_stats.has_data()) or
                                (self.ua2_stats is not None and self.ua2_stats.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.asic_id.yfilter != YFilter.not_set or
                                self.internal_err_cnt.yfilter != YFilter.not_set or
                                self.port.yfilter != YFilter.not_set or
                                (self.ca_stats is not None and self.ca_stats.has_operation()) or
                                (self.ma_stats is not None and self.ma_stats.has_operation()) or
                                (self.pe_cc_stats is not None and self.pe_cc_stats.has_operation()) or
                                (self.pe_mc_stats is not None and self.pe_mc_stats.has_operation()) or
                                (self.pe_stats is not None and self.pe_stats.has_operation()) or
                                (self.pe_uc_stats is not None and self.pe_uc_stats.has_operation()) or
                                (self.pi_cc_stats is not None and self.pi_cc_stats.has_operation()) or
                                (self.pi_mc_stats is not None and self.pi_mc_stats.has_operation()) or
                                (self.pi_stats is not None and self.pi_stats.has_operation()) or
                                (self.pi_uc_stats is not None and self.pi_uc_stats.has_operation()) or
                                (self.ua0_stats is not None and self.ua0_stats.has_operation()) or
                                (self.ua1_stats is not None and self.ua1_stats.has_operation()) or
                                (self.ua2_stats is not None and self.ua2_stats.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sm15-stat" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.asic_id.is_set or self.asic_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.asic_id.get_name_leafdata())
                            if (self.internal_err_cnt.is_set or self.internal_err_cnt.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.internal_err_cnt.get_name_leafdata())
                            if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.port.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "ca-stats"):
                                if (self.ca_stats is None):
                                    self.ca_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.CaStats()
                                    self.ca_stats.parent = self
                                    self._children_name_map["ca_stats"] = "ca-stats"
                                return self.ca_stats

                            if (child_yang_name == "ma-stats"):
                                if (self.ma_stats is None):
                                    self.ma_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.MaStats()
                                    self.ma_stats.parent = self
                                    self._children_name_map["ma_stats"] = "ma-stats"
                                return self.ma_stats

                            if (child_yang_name == "pe-cc-stats"):
                                if (self.pe_cc_stats is None):
                                    self.pe_cc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeCcStats()
                                    self.pe_cc_stats.parent = self
                                    self._children_name_map["pe_cc_stats"] = "pe-cc-stats"
                                return self.pe_cc_stats

                            if (child_yang_name == "pe-mc-stats"):
                                if (self.pe_mc_stats is None):
                                    self.pe_mc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeMcStats()
                                    self.pe_mc_stats.parent = self
                                    self._children_name_map["pe_mc_stats"] = "pe-mc-stats"
                                return self.pe_mc_stats

                            if (child_yang_name == "pe-stats"):
                                if (self.pe_stats is None):
                                    self.pe_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeStats()
                                    self.pe_stats.parent = self
                                    self._children_name_map["pe_stats"] = "pe-stats"
                                return self.pe_stats

                            if (child_yang_name == "pe-uc-stats"):
                                if (self.pe_uc_stats is None):
                                    self.pe_uc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeUcStats()
                                    self.pe_uc_stats.parent = self
                                    self._children_name_map["pe_uc_stats"] = "pe-uc-stats"
                                return self.pe_uc_stats

                            if (child_yang_name == "pi-cc-stats"):
                                if (self.pi_cc_stats is None):
                                    self.pi_cc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiCcStats()
                                    self.pi_cc_stats.parent = self
                                    self._children_name_map["pi_cc_stats"] = "pi-cc-stats"
                                return self.pi_cc_stats

                            if (child_yang_name == "pi-mc-stats"):
                                if (self.pi_mc_stats is None):
                                    self.pi_mc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiMcStats()
                                    self.pi_mc_stats.parent = self
                                    self._children_name_map["pi_mc_stats"] = "pi-mc-stats"
                                return self.pi_mc_stats

                            if (child_yang_name == "pi-stats"):
                                if (self.pi_stats is None):
                                    self.pi_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiStats()
                                    self.pi_stats.parent = self
                                    self._children_name_map["pi_stats"] = "pi-stats"
                                return self.pi_stats

                            if (child_yang_name == "pi-uc-stats"):
                                if (self.pi_uc_stats is None):
                                    self.pi_uc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiUcStats()
                                    self.pi_uc_stats.parent = self
                                    self._children_name_map["pi_uc_stats"] = "pi-uc-stats"
                                return self.pi_uc_stats

                            if (child_yang_name == "ua0-stats"):
                                if (self.ua0_stats is None):
                                    self.ua0_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua0Stats()
                                    self.ua0_stats.parent = self
                                    self._children_name_map["ua0_stats"] = "ua0-stats"
                                return self.ua0_stats

                            if (child_yang_name == "ua1-stats"):
                                if (self.ua1_stats is None):
                                    self.ua1_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua1Stats()
                                    self.ua1_stats.parent = self
                                    self._children_name_map["ua1_stats"] = "ua1-stats"
                                return self.ua1_stats

                            if (child_yang_name == "ua2-stats"):
                                if (self.ua2_stats is None):
                                    self.ua2_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua2Stats()
                                    self.ua2_stats.parent = self
                                    self._children_name_map["ua2_stats"] = "ua2-stats"
                                return self.ua2_stats

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ca-stats" or name == "ma-stats" or name == "pe-cc-stats" or name == "pe-mc-stats" or name == "pe-stats" or name == "pe-uc-stats" or name == "pi-cc-stats" or name == "pi-mc-stats" or name == "pi-stats" or name == "pi-uc-stats" or name == "ua0-stats" or name == "ua1-stats" or name == "ua2-stats" or name == "asic-id" or name == "internal-err-cnt" or name == "port"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "asic-id"):
                                self.asic_id = value
                                self.asic_id.value_namespace = name_space
                                self.asic_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "internal-err-cnt"):
                                self.internal_err_cnt = value
                                self.internal_err_cnt.value_namespace = name_space
                                self.internal_err_cnt.value_namespace_prefix = name_space_prefix
                            if(value_path == "port"):
                                self.port = value
                                self.port.value_namespace = name_space
                                self.port.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.sm15_stat:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.sm15_stat:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sm15-stats" + path_buffer

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

                        if (child_yang_name == "sm15-stat"):
                            for c in self.sm15_stat:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.sm15_stat.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "sm15-stat"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.pkt_stats is not None and self.pkt_stats.has_data()) or
                        (self.sm15_stats is not None and self.sm15_stats.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.pkt_stats is not None and self.pkt_stats.has_operation()) or
                        (self.sm15_stats is not None and self.sm15_stats.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cross-bar-table" + path_buffer

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

                    if (child_yang_name == "pkt-stats"):
                        if (self.pkt_stats is None):
                            self.pkt_stats = CrossBarStats.Nodes.Node.CrossBarTable.PktStats()
                            self.pkt_stats.parent = self
                            self._children_name_map["pkt_stats"] = "pkt-stats"
                        return self.pkt_stats

                    if (child_yang_name == "sm15-stats"):
                        if (self.sm15_stats is None):
                            self.sm15_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats()
                            self.sm15_stats.parent = self
                            self._children_name_map["sm15_stats"] = "sm15-stats"
                        return self.sm15_stats

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "pkt-stats" or name == "sm15-stats"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.cross_bar_table is not None and self.cross_bar_table.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.cross_bar_table is not None and self.cross_bar_table.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-xbar-oper:cross-bar-stats/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "cross-bar-table"):
                    if (self.cross_bar_table is None):
                        self.cross_bar_table = CrossBarStats.Nodes.Node.CrossBarTable()
                        self.cross_bar_table.parent = self
                        self._children_name_map["cross_bar_table"] = "cross-bar-table"
                    return self.cross_bar_table

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cross-bar-table" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-asr9k-xbar-oper:cross-bar-stats/%s" % self.get_segment_path()
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
                c = CrossBarStats.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-asr9k-xbar-oper:cross-bar-stats" + path_buffer

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
                self.nodes = CrossBarStats.Nodes()
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
        self._top_entity = CrossBarStats()
        return self._top_entity

