""" Cisco_IOS_XR_asr9k_xbar_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-xbar package operational data.

This module contains definitions
for the following management objects\:
  cross\-bar\-stats\: Crossbar stats operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CrossBarStats(object):
    """
    Crossbar stats operational data
    
    .. attribute:: nodes
    
    	Table of Nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes>`
    
    

    """

    _prefix = 'asr9k-xbar-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = CrossBarStats.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Table of Nodes
        
        .. attribute:: node
        
        	Information about a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-xbar-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
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
                self.parent = None
                self.node_name = None
                self.cross_bar_table = CrossBarStats.Nodes.Node.CrossBarTable()
                self.cross_bar_table.parent = self


            class CrossBarTable(object):
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
                    self.parent = None
                    self.pkt_stats = CrossBarStats.Nodes.Node.CrossBarTable.PktStats()
                    self.pkt_stats.parent = self
                    self.sm15_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats()
                    self.sm15_stats.parent = self


                class PktStats(object):
                    """
                    Table of packet stats
                    
                    .. attribute:: pkt_stat
                    
                    	Stats information for a particular asic type and port
                    	**type**\: list of    :py:class:`PktStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.PktStats.PktStat>`
                    
                    

                    """

                    _prefix = 'asr9k-xbar-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.pkt_stat = YList()
                        self.pkt_stat.parent = self
                        self.pkt_stat.name = 'pkt_stat'


                    class PktStat(object):
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
                            self.parent = None
                            self.asic_id = None
                            self.diagnostic_packet_count_high = None
                            self.diagnostic_packet_count_low = None
                            self.egress_channel_utilization_count_high = None
                            self.egress_channel_utilization_count_low = None
                            self.egress_packet_count_since_last_read_high = None
                            self.egress_packet_count_since_last_read_low = None
                            self.fpoedb_correctable_ecc_error_count_high = None
                            self.fpoedb_correctable_ecc_error_count_low = None
                            self.fpoedb_uncorrectable_ecc_error_count_high = None
                            self.fpoedb_uncorrectable_ecc_error_count_low = None
                            self.header_crc_error_count_high = None
                            self.header_crc_error_count_low = None
                            self.holdrop_count_high = None
                            self.holdrop_count_low = None
                            self.ingress_channel_utilization_count_high = None
                            self.ingress_channel_utilization_count_low = None
                            self.ingress_packet_count_since_last_read_high = None
                            self.ingress_packet_count_since_last_read_low = None
                            self.input_buffer_back_pressure_count_high = None
                            self.input_buffer_back_pressure_count_low = None
                            self.input_buffer_correctable_ecc_error_count_high = None
                            self.input_buffer_correctable_ecc_error_count_low = None
                            self.input_buffer_queued_packet_count_high = None
                            self.input_buffer_queued_packet_count_low = None
                            self.input_buffer_uncorrectable_ecc_error_count_high = None
                            self.input_buffer_uncorrectable_ecc_error_count_low = None
                            self.internal_error_count = None
                            self.null_fpoe_drop_count_high = None
                            self.null_fpoe_drop_count_low = None
                            self.output_buffer_back_pressure_count_high = None
                            self.output_buffer_back_pressure_count_low = None
                            self.output_buffer_correctable_ecc_error_count_high = None
                            self.output_buffer_correctable_ecc_error_count_low = None
                            self.output_buffer_queued_packet_count_high = None
                            self.output_buffer_queued_packet_count_low = None
                            self.output_buffer_uncorrectable_ecc_error_count_high = None
                            self.output_buffer_uncorrectable_ecc_error_count_low = None
                            self.packet_crc_error_count_high = None
                            self.packet_crc_error_count_low = None
                            self.port = None
                            self.short_input_header_error_count_high = None
                            self.short_input_header_error_count_low = None
                            self.short_packet_error_count_high = None
                            self.short_packet_error_count_low = None
                            self.xbar_timeout_drop_count_high = None
                            self.xbar_timeout_drop_count_low = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-xbar-oper:pkt-stat'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.asic_id is not None:
                                return True

                            if self.diagnostic_packet_count_high is not None:
                                return True

                            if self.diagnostic_packet_count_low is not None:
                                return True

                            if self.egress_channel_utilization_count_high is not None:
                                return True

                            if self.egress_channel_utilization_count_low is not None:
                                return True

                            if self.egress_packet_count_since_last_read_high is not None:
                                return True

                            if self.egress_packet_count_since_last_read_low is not None:
                                return True

                            if self.fpoedb_correctable_ecc_error_count_high is not None:
                                return True

                            if self.fpoedb_correctable_ecc_error_count_low is not None:
                                return True

                            if self.fpoedb_uncorrectable_ecc_error_count_high is not None:
                                return True

                            if self.fpoedb_uncorrectable_ecc_error_count_low is not None:
                                return True

                            if self.header_crc_error_count_high is not None:
                                return True

                            if self.header_crc_error_count_low is not None:
                                return True

                            if self.holdrop_count_high is not None:
                                return True

                            if self.holdrop_count_low is not None:
                                return True

                            if self.ingress_channel_utilization_count_high is not None:
                                return True

                            if self.ingress_channel_utilization_count_low is not None:
                                return True

                            if self.ingress_packet_count_since_last_read_high is not None:
                                return True

                            if self.ingress_packet_count_since_last_read_low is not None:
                                return True

                            if self.input_buffer_back_pressure_count_high is not None:
                                return True

                            if self.input_buffer_back_pressure_count_low is not None:
                                return True

                            if self.input_buffer_correctable_ecc_error_count_high is not None:
                                return True

                            if self.input_buffer_correctable_ecc_error_count_low is not None:
                                return True

                            if self.input_buffer_queued_packet_count_high is not None:
                                return True

                            if self.input_buffer_queued_packet_count_low is not None:
                                return True

                            if self.input_buffer_uncorrectable_ecc_error_count_high is not None:
                                return True

                            if self.input_buffer_uncorrectable_ecc_error_count_low is not None:
                                return True

                            if self.internal_error_count is not None:
                                return True

                            if self.null_fpoe_drop_count_high is not None:
                                return True

                            if self.null_fpoe_drop_count_low is not None:
                                return True

                            if self.output_buffer_back_pressure_count_high is not None:
                                return True

                            if self.output_buffer_back_pressure_count_low is not None:
                                return True

                            if self.output_buffer_correctable_ecc_error_count_high is not None:
                                return True

                            if self.output_buffer_correctable_ecc_error_count_low is not None:
                                return True

                            if self.output_buffer_queued_packet_count_high is not None:
                                return True

                            if self.output_buffer_queued_packet_count_low is not None:
                                return True

                            if self.output_buffer_uncorrectable_ecc_error_count_high is not None:
                                return True

                            if self.output_buffer_uncorrectable_ecc_error_count_low is not None:
                                return True

                            if self.packet_crc_error_count_high is not None:
                                return True

                            if self.packet_crc_error_count_low is not None:
                                return True

                            if self.port is not None:
                                return True

                            if self.short_input_header_error_count_high is not None:
                                return True

                            if self.short_input_header_error_count_low is not None:
                                return True

                            if self.short_packet_error_count_high is not None:
                                return True

                            if self.short_packet_error_count_low is not None:
                                return True

                            if self.xbar_timeout_drop_count_high is not None:
                                return True

                            if self.xbar_timeout_drop_count_low is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                            return meta._meta_table['CrossBarStats.Nodes.Node.CrossBarTable.PktStats.PktStat']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-xbar-oper:pkt-stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.pkt_stat is not None:
                            for child_ref in self.pkt_stat:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                        return meta._meta_table['CrossBarStats.Nodes.Node.CrossBarTable.PktStats']['meta_info']


                class Sm15Stats(object):
                    """
                    Table of packet stats for SM15
                    
                    .. attribute:: sm15_stat
                    
                    	Stats information for a particular asic type and port
                    	**type**\: list of    :py:class:`Sm15Stat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat>`
                    
                    

                    """

                    _prefix = 'asr9k-xbar-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.sm15_stat = YList()
                        self.sm15_stat.parent = self
                        self.sm15_stat.name = 'sm15_stat'


                    class Sm15Stat(object):
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
                            self.parent = None
                            self.asic_id = None
                            self.ca_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.CaStats()
                            self.ca_stats.parent = self
                            self.internal_err_cnt = None
                            self.ma_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.MaStats()
                            self.ma_stats.parent = self
                            self.pe_cc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeCcStats()
                            self.pe_cc_stats.parent = self
                            self.pe_mc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeMcStats()
                            self.pe_mc_stats.parent = self
                            self.pe_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeStats()
                            self.pe_stats.parent = self
                            self.pe_uc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeUcStats()
                            self.pe_uc_stats.parent = self
                            self.pi_cc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiCcStats()
                            self.pi_cc_stats.parent = self
                            self.pi_mc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiMcStats()
                            self.pi_mc_stats.parent = self
                            self.pi_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiStats()
                            self.pi_stats.parent = self
                            self.pi_uc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiUcStats()
                            self.pi_uc_stats.parent = self
                            self.port = None
                            self.ua0_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua0Stats()
                            self.ua0_stats.parent = self
                            self.ua1_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua1Stats()
                            self.ua1_stats.parent = self
                            self.ua2_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua2Stats()
                            self.ua2_stats.parent = self


                        class Ua0Stats(object):
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
                                self.parent = None
                                self.ack_wait_cnt = None
                                self.dest_drop_pkt_cnt = None
                                self.dest_src_pkt_cnt = None
                                self.rcv_pkt_cnt = None
                                self.rx_drop_pkt_cnt = None
                                self.rx_fabric_to_cnt = None
                                self.src_dest_pkt_cnt = None
                                self.tx_pkt_cnt = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-xbar-oper:ua0-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ack_wait_cnt is not None:
                                    return True

                                if self.dest_drop_pkt_cnt is not None:
                                    return True

                                if self.dest_src_pkt_cnt is not None:
                                    return True

                                if self.rcv_pkt_cnt is not None:
                                    return True

                                if self.rx_drop_pkt_cnt is not None:
                                    return True

                                if self.rx_fabric_to_cnt is not None:
                                    return True

                                if self.src_dest_pkt_cnt is not None:
                                    return True

                                if self.tx_pkt_cnt is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                                return meta._meta_table['CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua0Stats']['meta_info']


                        class Ua1Stats(object):
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
                                self.parent = None
                                self.ack_wait_cnt = None
                                self.dest_drop_pkt_cnt = None
                                self.dest_src_pkt_cnt = None
                                self.rcv_pkt_cnt = None
                                self.rx_drop_pkt_cnt = None
                                self.rx_fabric_to_cnt = None
                                self.src_dest_pkt_cnt = None
                                self.tx_pkt_cnt = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-xbar-oper:ua1-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ack_wait_cnt is not None:
                                    return True

                                if self.dest_drop_pkt_cnt is not None:
                                    return True

                                if self.dest_src_pkt_cnt is not None:
                                    return True

                                if self.rcv_pkt_cnt is not None:
                                    return True

                                if self.rx_drop_pkt_cnt is not None:
                                    return True

                                if self.rx_fabric_to_cnt is not None:
                                    return True

                                if self.src_dest_pkt_cnt is not None:
                                    return True

                                if self.tx_pkt_cnt is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                                return meta._meta_table['CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua1Stats']['meta_info']


                        class Ua2Stats(object):
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
                                self.parent = None
                                self.ack_wait_cnt = None
                                self.dest_drop_pkt_cnt = None
                                self.dest_src_pkt_cnt = None
                                self.rcv_pkt_cnt = None
                                self.rx_drop_pkt_cnt = None
                                self.rx_fabric_to_cnt = None
                                self.src_dest_pkt_cnt = None
                                self.tx_pkt_cnt = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-xbar-oper:ua2-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ack_wait_cnt is not None:
                                    return True

                                if self.dest_drop_pkt_cnt is not None:
                                    return True

                                if self.dest_src_pkt_cnt is not None:
                                    return True

                                if self.rcv_pkt_cnt is not None:
                                    return True

                                if self.rx_drop_pkt_cnt is not None:
                                    return True

                                if self.rx_fabric_to_cnt is not None:
                                    return True

                                if self.src_dest_pkt_cnt is not None:
                                    return True

                                if self.tx_pkt_cnt is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                                return meta._meta_table['CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua2Stats']['meta_info']


                        class MaStats(object):
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
                                self.parent = None
                                self.dest_drop_pkt_cnt = None
                                self.dest_src_pkt_cnt = None
                                self.rcv_pkt_cnt = None
                                self.rx_drop_pkt_cnt = None
                                self.rx_fabric_to_cnt = None
                                self.rx_hol_to_cnt = None
                                self.rx_re_transmit_cnt = None
                                self.src_dest_pkt_cnt = None
                                self.tx_pkt_cnt = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-xbar-oper:ma-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.dest_drop_pkt_cnt is not None:
                                    return True

                                if self.dest_src_pkt_cnt is not None:
                                    return True

                                if self.rcv_pkt_cnt is not None:
                                    return True

                                if self.rx_drop_pkt_cnt is not None:
                                    return True

                                if self.rx_fabric_to_cnt is not None:
                                    return True

                                if self.rx_hol_to_cnt is not None:
                                    return True

                                if self.rx_re_transmit_cnt is not None:
                                    return True

                                if self.src_dest_pkt_cnt is not None:
                                    return True

                                if self.tx_pkt_cnt is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                                return meta._meta_table['CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.MaStats']['meta_info']


                        class CaStats(object):
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
                                self.parent = None
                                self.dest_drop_pkt_cnt = None
                                self.dest_src_pkt_cnt = None
                                self.rcv_pkt_cnt = None
                                self.rx_drop_pkt_cnt = None
                                self.src_dest_pkt_cnt = None
                                self.tx_pkt_cnt = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-xbar-oper:ca-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.dest_drop_pkt_cnt is not None:
                                    return True

                                if self.dest_src_pkt_cnt is not None:
                                    return True

                                if self.rcv_pkt_cnt is not None:
                                    return True

                                if self.rx_drop_pkt_cnt is not None:
                                    return True

                                if self.src_dest_pkt_cnt is not None:
                                    return True

                                if self.tx_pkt_cnt is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                                return meta._meta_table['CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.CaStats']['meta_info']


                        class PiStats(object):
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
                                self.parent = None
                                self.total_calc_rate = None
                                self.total_rate1_cnt = None
                                self.total_rate2_cnt = None
                                self.total_rate3_cnt = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-xbar-oper:pi-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.total_calc_rate is not None:
                                    return True

                                if self.total_rate1_cnt is not None:
                                    return True

                                if self.total_rate2_cnt is not None:
                                    return True

                                if self.total_rate3_cnt is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                                return meta._meta_table['CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiStats']['meta_info']


                        class PeStats(object):
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
                                self.parent = None
                                self.mc2uc_preempt_cnt = None
                                self.total_calc_rate = None
                                self.total_rate1_cnt = None
                                self.total_rate2_cnt = None
                                self.total_rate3_cnt = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-xbar-oper:pe-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.mc2uc_preempt_cnt is not None:
                                    return True

                                if self.total_calc_rate is not None:
                                    return True

                                if self.total_rate1_cnt is not None:
                                    return True

                                if self.total_rate2_cnt is not None:
                                    return True

                                if self.total_rate3_cnt is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                                return meta._meta_table['CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeStats']['meta_info']


                        class PiUcStats(object):
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
                                self.parent = None
                                self.calc_rate = None
                                self.cpp_head_drop_pkt_cnt = None
                                self.crc_stomp_pkt_cnt = None
                                self.diag_pkt_cnt = None
                                self.fpoe_mem_ecc_1bit_err_cnt = None
                                self.fpoe_mem_ecc_2bit_err_cnt = None
                                self.in_coming_pkt_err_cnt = None
                                self.line_err_drp_pkt = None
                                self.line_s_written_in_mem0 = None
                                self.line_s_written_in_mem1 = None
                                self.line_s_written_in_mem2 = None
                                self.max_pkt_len_err_cnt = None
                                self.min_pkt_len_err_cnt = None
                                self.pkt_cfh_crc_err_cnt = None
                                self.pkt_crc_err_cnt = None
                                self.pkt_fpoe_addr_rng_hit_cnt = None
                                self.pkt_null_poe_sent_ua0_cnt = None
                                self.pkt_null_poe_sent_ua1_cnt = None
                                self.pkt_null_poe_sent_ua2_cnt = None
                                self.pkt_rcv_cnt = None
                                self.pkt_sent_to_disabled_port_cnt = None
                                self.pkt_seq_err_cnt = None
                                self.pkts_sent_to_ux0_cnt = None
                                self.pkts_sent_to_ux1_cnt = None
                                self.pkts_sent_to_ux2_cnt = None
                                self.rate_cnt = None
                                self.stop_thrsh_hit_cnt = None
                                self.tail_drp_pkt_cnt = None
                                self.tr_head_drop_pkt_cnt = None
                                self.tr_pkt_sent_to_ux = None
                                self.uc0_data_mem_ecc_1bit_err_cnt = None
                                self.uc0_data_mem_ecc_2bit_err_cnt = None
                                self.uc1_data_mem_ecc_1bit_err_cnt = None
                                self.uc1_data_mem_ecc_2bit_err_cnt = None
                                self.uc2_data_mem_ecc_1bit_err_cnt = None
                                self.uc2_data_mem_ecc_2bit_err_cnt = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-xbar-oper:pi-uc-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.calc_rate is not None:
                                    return True

                                if self.cpp_head_drop_pkt_cnt is not None:
                                    return True

                                if self.crc_stomp_pkt_cnt is not None:
                                    return True

                                if self.diag_pkt_cnt is not None:
                                    return True

                                if self.fpoe_mem_ecc_1bit_err_cnt is not None:
                                    return True

                                if self.fpoe_mem_ecc_2bit_err_cnt is not None:
                                    return True

                                if self.in_coming_pkt_err_cnt is not None:
                                    return True

                                if self.line_err_drp_pkt is not None:
                                    return True

                                if self.line_s_written_in_mem0 is not None:
                                    return True

                                if self.line_s_written_in_mem1 is not None:
                                    return True

                                if self.line_s_written_in_mem2 is not None:
                                    return True

                                if self.max_pkt_len_err_cnt is not None:
                                    return True

                                if self.min_pkt_len_err_cnt is not None:
                                    return True

                                if self.pkt_cfh_crc_err_cnt is not None:
                                    return True

                                if self.pkt_crc_err_cnt is not None:
                                    return True

                                if self.pkt_fpoe_addr_rng_hit_cnt is not None:
                                    return True

                                if self.pkt_null_poe_sent_ua0_cnt is not None:
                                    return True

                                if self.pkt_null_poe_sent_ua1_cnt is not None:
                                    return True

                                if self.pkt_null_poe_sent_ua2_cnt is not None:
                                    return True

                                if self.pkt_rcv_cnt is not None:
                                    return True

                                if self.pkt_sent_to_disabled_port_cnt is not None:
                                    return True

                                if self.pkt_seq_err_cnt is not None:
                                    return True

                                if self.pkts_sent_to_ux0_cnt is not None:
                                    return True

                                if self.pkts_sent_to_ux1_cnt is not None:
                                    return True

                                if self.pkts_sent_to_ux2_cnt is not None:
                                    return True

                                if self.rate_cnt is not None:
                                    return True

                                if self.stop_thrsh_hit_cnt is not None:
                                    return True

                                if self.tail_drp_pkt_cnt is not None:
                                    return True

                                if self.tr_head_drop_pkt_cnt is not None:
                                    return True

                                if self.tr_pkt_sent_to_ux is not None:
                                    return True

                                if self.uc0_data_mem_ecc_1bit_err_cnt is not None:
                                    return True

                                if self.uc0_data_mem_ecc_2bit_err_cnt is not None:
                                    return True

                                if self.uc1_data_mem_ecc_1bit_err_cnt is not None:
                                    return True

                                if self.uc1_data_mem_ecc_2bit_err_cnt is not None:
                                    return True

                                if self.uc2_data_mem_ecc_1bit_err_cnt is not None:
                                    return True

                                if self.uc2_data_mem_ecc_2bit_err_cnt is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                                return meta._meta_table['CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiUcStats']['meta_info']


                        class PiMcStats(object):
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
                                self.parent = None
                                self.calc_rate = None
                                self.cpp_head_drop_pkt_from_ma_cnt = None
                                self.crc_stomp_pkt_cnt = None
                                self.data_mem0_ecc_1bit_err_cnt = None
                                self.data_mem0_ecc_2bit_err_cnt = None
                                self.data_mem1_ecc_1bit_err_cnt = None
                                self.data_mem1_ecc_2bit_err_cnt = None
                                self.data_mem2_ecc_1bit_err_cnt = None
                                self.data_mem2_ecc_2bit_err_cnt = None
                                self.di_err_pkt_cnt = None
                                self.di_hdr_len_err_pkt_cnt = None
                                self.diag_pkt_cnt = None
                                self.fpoe_mem_ecc_1bit_err_cnt = None
                                self.fpoe_mem_ecc_2bit_err_cnt = None
                                self.in_coming_pkt_err_cnt = None
                                self.line_err_drp_pkt = None
                                self.line_s_written_in_mem = None
                                self.max_pkt_len_err_cnt = None
                                self.min_pkt_len_err_cnt = None
                                self.pkt_cfh_crc_err_cnt = None
                                self.pkt_crc_err_cnt = None
                                self.pkt_fpoe_addr_rng_hit_cnt = None
                                self.pkt_fpoe_match_hit_cnt = None
                                self.pkt_null_poe_sent_cnt = None
                                self.pkt_rcv_cnt = None
                                self.pkt_sent_to_disabled_port = None
                                self.pkt_seq_err_cnt = None
                                self.pkts_sent_to_mx_cnt = None
                                self.rate_cnt = None
                                self.stop_thrsh_hit_cnt = None
                                self.tail_drp_pkt_cnt = None
                                self.tr_head_drop_pkt_from_ma_cnt = None
                                self.tr_pkt_sent_to_mx = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-xbar-oper:pi-mc-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.calc_rate is not None:
                                    return True

                                if self.cpp_head_drop_pkt_from_ma_cnt is not None:
                                    return True

                                if self.crc_stomp_pkt_cnt is not None:
                                    return True

                                if self.data_mem0_ecc_1bit_err_cnt is not None:
                                    return True

                                if self.data_mem0_ecc_2bit_err_cnt is not None:
                                    return True

                                if self.data_mem1_ecc_1bit_err_cnt is not None:
                                    return True

                                if self.data_mem1_ecc_2bit_err_cnt is not None:
                                    return True

                                if self.data_mem2_ecc_1bit_err_cnt is not None:
                                    return True

                                if self.data_mem2_ecc_2bit_err_cnt is not None:
                                    return True

                                if self.di_err_pkt_cnt is not None:
                                    return True

                                if self.di_hdr_len_err_pkt_cnt is not None:
                                    return True

                                if self.diag_pkt_cnt is not None:
                                    return True

                                if self.fpoe_mem_ecc_1bit_err_cnt is not None:
                                    return True

                                if self.fpoe_mem_ecc_2bit_err_cnt is not None:
                                    return True

                                if self.in_coming_pkt_err_cnt is not None:
                                    return True

                                if self.line_err_drp_pkt is not None:
                                    return True

                                if self.line_s_written_in_mem is not None:
                                    return True

                                if self.max_pkt_len_err_cnt is not None:
                                    return True

                                if self.min_pkt_len_err_cnt is not None:
                                    return True

                                if self.pkt_cfh_crc_err_cnt is not None:
                                    return True

                                if self.pkt_crc_err_cnt is not None:
                                    return True

                                if self.pkt_fpoe_addr_rng_hit_cnt is not None:
                                    return True

                                if self.pkt_fpoe_match_hit_cnt is not None:
                                    return True

                                if self.pkt_null_poe_sent_cnt is not None:
                                    return True

                                if self.pkt_rcv_cnt is not None:
                                    return True

                                if self.pkt_sent_to_disabled_port is not None:
                                    return True

                                if self.pkt_seq_err_cnt is not None:
                                    return True

                                if self.pkts_sent_to_mx_cnt is not None:
                                    return True

                                if self.rate_cnt is not None:
                                    return True

                                if self.stop_thrsh_hit_cnt is not None:
                                    return True

                                if self.tail_drp_pkt_cnt is not None:
                                    return True

                                if self.tr_head_drop_pkt_from_ma_cnt is not None:
                                    return True

                                if self.tr_pkt_sent_to_mx is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                                return meta._meta_table['CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiMcStats']['meta_info']


                        class PiCcStats(object):
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
                                self.parent = None
                                self.calc_rate = None
                                self.data_mem_ecc_derr_cnt = None
                                self.data_mem_ecc_serr_cnt = None
                                self.data_mem_ovf0_cnt = None
                                self.data_mem_ovf1_cnt = None
                                self.dmem_rd_cnt = None
                                self.fpoe_mem_ecc_derr_cnt = None
                                self.fpoe_mem_ecc_serr_cnt = None
                                self.in0_cong_cnt = None
                                self.in0_drop_cnt = None
                                self.in0_ecc_derr_cnt = None
                                self.in0_ecc_serr_cnt = None
                                self.in0_fnc_err_cnt = None
                                self.in0_pkt_cnt = None
                                self.in0_shut_cnt = None
                                self.in1_cong_cnt = None
                                self.in1_drop_cnt = None
                                self.in1_ecc_derr_cnt = None
                                self.in1_ecc_serr_cnt = None
                                self.in1_fnc_err_cnt = None
                                self.in1_pkt_cnt = None
                                self.in1_shut_cnt = None
                                self.in_dmem0_cnt = None
                                self.in_dmem1_cnt = None
                                self.null_poe_cnt = None
                                self.out_pkt_cnt = None
                                self.rate_cnt = None
                                self.shut_ack_cnt = None
                                self.stop_thrsh_hit_cnt = None
                                self.tail_drop_msg_cnt = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-xbar-oper:pi-cc-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.calc_rate is not None:
                                    return True

                                if self.data_mem_ecc_derr_cnt is not None:
                                    return True

                                if self.data_mem_ecc_serr_cnt is not None:
                                    return True

                                if self.data_mem_ovf0_cnt is not None:
                                    return True

                                if self.data_mem_ovf1_cnt is not None:
                                    return True

                                if self.dmem_rd_cnt is not None:
                                    return True

                                if self.fpoe_mem_ecc_derr_cnt is not None:
                                    return True

                                if self.fpoe_mem_ecc_serr_cnt is not None:
                                    return True

                                if self.in0_cong_cnt is not None:
                                    return True

                                if self.in0_drop_cnt is not None:
                                    return True

                                if self.in0_ecc_derr_cnt is not None:
                                    return True

                                if self.in0_ecc_serr_cnt is not None:
                                    return True

                                if self.in0_fnc_err_cnt is not None:
                                    return True

                                if self.in0_pkt_cnt is not None:
                                    return True

                                if self.in0_shut_cnt is not None:
                                    return True

                                if self.in1_cong_cnt is not None:
                                    return True

                                if self.in1_drop_cnt is not None:
                                    return True

                                if self.in1_ecc_derr_cnt is not None:
                                    return True

                                if self.in1_ecc_serr_cnt is not None:
                                    return True

                                if self.in1_fnc_err_cnt is not None:
                                    return True

                                if self.in1_pkt_cnt is not None:
                                    return True

                                if self.in1_shut_cnt is not None:
                                    return True

                                if self.in_dmem0_cnt is not None:
                                    return True

                                if self.in_dmem1_cnt is not None:
                                    return True

                                if self.null_poe_cnt is not None:
                                    return True

                                if self.out_pkt_cnt is not None:
                                    return True

                                if self.rate_cnt is not None:
                                    return True

                                if self.shut_ack_cnt is not None:
                                    return True

                                if self.stop_thrsh_hit_cnt is not None:
                                    return True

                                if self.tail_drop_msg_cnt is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                                return meta._meta_table['CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiCcStats']['meta_info']


                        class PeUcStats(object):
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
                                self.parent = None
                                self.calc_rate = None
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
                                self.fc_uc_0_1_trans_cnt = None
                                self.fe_uc_sop_eop_pack_cnt = None
                                self.in_full_line_uc0_cnt = None
                                self.in_full_line_uc1_cnt = None
                                self.in_full_line_uc2_cnt = None
                                self.in_pkt_uc0_cnt = None
                                self.in_pkt_uc1_cnt = None
                                self.in_pkt_uc2_cnt = None
                                self.out_pkt_uc_cnt = None
                                self.pkt_ecc_err_drop_uc_cnt = None
                                self.pkt_ecc_trunc_cnt_uc_cnt = None
                                self.pkt_sop_drop_uc0_cnt = None
                                self.pkt_sop_drop_uc1_cnt = None
                                self.pkt_sop_drop_uc2_cnt = None
                                self.pkt_trunc_eop_uc0_cnt = None
                                self.pkt_trunc_eop_uc1_cnt = None
                                self.pkt_trunc_eop_uc2_cnt = None
                                self.rate_cnt = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-xbar-oper:pe-uc-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.calc_rate is not None:
                                    return True

                                if self.ecc_1bit_err_uc0_0_cnt is not None:
                                    return True

                                if self.ecc_1bit_err_uc0_1_cnt is not None:
                                    return True

                                if self.ecc_1bit_err_uc1_0_cnt is not None:
                                    return True

                                if self.ecc_1bit_err_uc1_1_cnt is not None:
                                    return True

                                if self.ecc_1bit_err_uc2_0_cnt is not None:
                                    return True

                                if self.ecc_1bit_err_uc2_1_cnt is not None:
                                    return True

                                if self.ecc_2bit_err_uc0_0_cnt is not None:
                                    return True

                                if self.ecc_2bit_err_uc0_1_cnt is not None:
                                    return True

                                if self.ecc_2bit_err_uc1_0_cnt is not None:
                                    return True

                                if self.ecc_2bit_err_uc1_1_cnt is not None:
                                    return True

                                if self.ecc_2bit_err_uc2_0_cnt is not None:
                                    return True

                                if self.ecc_2bit_err_uc2_1_cnt is not None:
                                    return True

                                if self.fc_uc_0_1_trans_cnt is not None:
                                    return True

                                if self.fe_uc_sop_eop_pack_cnt is not None:
                                    return True

                                if self.in_full_line_uc0_cnt is not None:
                                    return True

                                if self.in_full_line_uc1_cnt is not None:
                                    return True

                                if self.in_full_line_uc2_cnt is not None:
                                    return True

                                if self.in_pkt_uc0_cnt is not None:
                                    return True

                                if self.in_pkt_uc1_cnt is not None:
                                    return True

                                if self.in_pkt_uc2_cnt is not None:
                                    return True

                                if self.out_pkt_uc_cnt is not None:
                                    return True

                                if self.pkt_ecc_err_drop_uc_cnt is not None:
                                    return True

                                if self.pkt_ecc_trunc_cnt_uc_cnt is not None:
                                    return True

                                if self.pkt_sop_drop_uc0_cnt is not None:
                                    return True

                                if self.pkt_sop_drop_uc1_cnt is not None:
                                    return True

                                if self.pkt_sop_drop_uc2_cnt is not None:
                                    return True

                                if self.pkt_trunc_eop_uc0_cnt is not None:
                                    return True

                                if self.pkt_trunc_eop_uc1_cnt is not None:
                                    return True

                                if self.pkt_trunc_eop_uc2_cnt is not None:
                                    return True

                                if self.rate_cnt is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                                return meta._meta_table['CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeUcStats']['meta_info']


                        class PeMcStats(object):
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
                                self.parent = None
                                self.calc_rate = None
                                self.ecc_1bit_err_mc0_cnt = None
                                self.ecc_1bit_err_mc1_cnt = None
                                self.ecc_1bit_err_mc2_cnt = None
                                self.ecc_2bit_err_mc0_cnt = None
                                self.ecc_2bit_err_mc1_cnt = None
                                self.ecc_2bit_err_mc2_cnt = None
                                self.fc_mc_0_1_trans_cnt = None
                                self.fe_mc_sop_eop_pack_cnt = None
                                self.in_full_line_mc_cnt = None
                                self.in_pkt_mc_cnt = None
                                self.out_pkt_mc_cnt = None
                                self.pkt_ecc_err_drop_mc_cnt = None
                                self.pkt_ecc_err_trunc_cnt_mc_cnt = None
                                self.pkt_sop_drop_mc_cnt = None
                                self.pkt_trunc_eop_mc_cnt = None
                                self.rate_cnt = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-xbar-oper:pe-mc-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.calc_rate is not None:
                                    return True

                                if self.ecc_1bit_err_mc0_cnt is not None:
                                    return True

                                if self.ecc_1bit_err_mc1_cnt is not None:
                                    return True

                                if self.ecc_1bit_err_mc2_cnt is not None:
                                    return True

                                if self.ecc_2bit_err_mc0_cnt is not None:
                                    return True

                                if self.ecc_2bit_err_mc1_cnt is not None:
                                    return True

                                if self.ecc_2bit_err_mc2_cnt is not None:
                                    return True

                                if self.fc_mc_0_1_trans_cnt is not None:
                                    return True

                                if self.fe_mc_sop_eop_pack_cnt is not None:
                                    return True

                                if self.in_full_line_mc_cnt is not None:
                                    return True

                                if self.in_pkt_mc_cnt is not None:
                                    return True

                                if self.out_pkt_mc_cnt is not None:
                                    return True

                                if self.pkt_ecc_err_drop_mc_cnt is not None:
                                    return True

                                if self.pkt_ecc_err_trunc_cnt_mc_cnt is not None:
                                    return True

                                if self.pkt_sop_drop_mc_cnt is not None:
                                    return True

                                if self.pkt_trunc_eop_mc_cnt is not None:
                                    return True

                                if self.rate_cnt is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                                return meta._meta_table['CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeMcStats']['meta_info']


                        class PeCcStats(object):
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
                                self.parent = None
                                self.calc_rate = None
                                self.congn_pkt_cnt = None
                                self.fc_cc_0_1_trans_cnt = None
                                self.in_pkt_cnt = None
                                self.mem0_drop_pkt_cnt = None
                                self.mem0_ecc_double_err_cnt = None
                                self.mem0_ecc_single_err_cnt = None
                                self.mem1_drop_pkt_cnt = None
                                self.mem1_ecc_double_err_cnt = None
                                self.mem1_ecc_single_err_cnt = None
                                self.out_path0_pkt_cnt = None
                                self.out_path1_pkt_cnt = None
                                self.rate_cnt = None
                                self.xbar_ecc_double_err_cnt = None
                                self.xbar_ecc_drop_pkt_cnt = None
                                self.xbar_ecc_single_err_cnt = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-xbar-oper:pe-cc-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.calc_rate is not None:
                                    return True

                                if self.congn_pkt_cnt is not None:
                                    return True

                                if self.fc_cc_0_1_trans_cnt is not None:
                                    return True

                                if self.in_pkt_cnt is not None:
                                    return True

                                if self.mem0_drop_pkt_cnt is not None:
                                    return True

                                if self.mem0_ecc_double_err_cnt is not None:
                                    return True

                                if self.mem0_ecc_single_err_cnt is not None:
                                    return True

                                if self.mem1_drop_pkt_cnt is not None:
                                    return True

                                if self.mem1_ecc_double_err_cnt is not None:
                                    return True

                                if self.mem1_ecc_single_err_cnt is not None:
                                    return True

                                if self.out_path0_pkt_cnt is not None:
                                    return True

                                if self.out_path1_pkt_cnt is not None:
                                    return True

                                if self.rate_cnt is not None:
                                    return True

                                if self.xbar_ecc_double_err_cnt is not None:
                                    return True

                                if self.xbar_ecc_drop_pkt_cnt is not None:
                                    return True

                                if self.xbar_ecc_single_err_cnt is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                                return meta._meta_table['CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeCcStats']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-xbar-oper:sm15-stat'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.asic_id is not None:
                                return True

                            if self.ca_stats is not None and self.ca_stats._has_data():
                                return True

                            if self.internal_err_cnt is not None:
                                return True

                            if self.ma_stats is not None and self.ma_stats._has_data():
                                return True

                            if self.pe_cc_stats is not None and self.pe_cc_stats._has_data():
                                return True

                            if self.pe_mc_stats is not None and self.pe_mc_stats._has_data():
                                return True

                            if self.pe_stats is not None and self.pe_stats._has_data():
                                return True

                            if self.pe_uc_stats is not None and self.pe_uc_stats._has_data():
                                return True

                            if self.pi_cc_stats is not None and self.pi_cc_stats._has_data():
                                return True

                            if self.pi_mc_stats is not None and self.pi_mc_stats._has_data():
                                return True

                            if self.pi_stats is not None and self.pi_stats._has_data():
                                return True

                            if self.pi_uc_stats is not None and self.pi_uc_stats._has_data():
                                return True

                            if self.port is not None:
                                return True

                            if self.ua0_stats is not None and self.ua0_stats._has_data():
                                return True

                            if self.ua1_stats is not None and self.ua1_stats._has_data():
                                return True

                            if self.ua2_stats is not None and self.ua2_stats._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                            return meta._meta_table['CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-xbar-oper:sm15-stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.sm15_stat is not None:
                            for child_ref in self.sm15_stat:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                        return meta._meta_table['CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-xbar-oper:cross-bar-table'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.pkt_stats is not None and self.pkt_stats._has_data():
                        return True

                    if self.sm15_stats is not None and self.sm15_stats._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                    return meta._meta_table['CrossBarStats.Nodes.Node.CrossBarTable']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-asr9k-xbar-oper:cross-bar-stats/Cisco-IOS-XR-asr9k-xbar-oper:nodes/Cisco-IOS-XR-asr9k-xbar-oper:node[Cisco-IOS-XR-asr9k-xbar-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.cross_bar_table is not None and self.cross_bar_table._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
                return meta._meta_table['CrossBarStats.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-xbar-oper:cross-bar-stats/Cisco-IOS-XR-asr9k-xbar-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
            return meta._meta_table['CrossBarStats.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-xbar-oper:cross-bar-stats'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_xbar_oper as meta
        return meta._meta_table['CrossBarStats']['meta_info']


