""" Cisco_IOS_XR_asr9k_xbar_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-xbar package operational data.

This module contains definitions
for the following management objects\:
  cross\-bar\-stats\: Crossbar stats operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
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
    
    	**config**\: False
    
    

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
        self._child_classes = OrderedDict([("nodes", ("nodes", CrossBarStats.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = CrossBarStats.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-xbar-oper:cross-bar-stats"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CrossBarStats, [], name, value)


    class Nodes(Entity):
        """
        Table of Nodes
        
        .. attribute:: node
        
        	Information about a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node>`
        
        	**config**\: False
        
        

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
            self._child_classes = OrderedDict([("node", ("node", CrossBarStats.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-xbar-oper:cross-bar-stats/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CrossBarStats.Nodes, [], name, value)


        class Node(Entity):
            """
            Information about a particular node
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: cross_bar_table
            
            	Table of stats information
            	**type**\:  :py:class:`CrossBarTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable>`
            
            	**config**\: False
            
            

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
                self._child_classes = OrderedDict([("cross-bar-table", ("cross_bar_table", CrossBarStats.Nodes.Node.CrossBarTable))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.cross_bar_table = CrossBarStats.Nodes.Node.CrossBarTable()
                self.cross_bar_table.parent = self
                self._children_name_map["cross_bar_table"] = "cross-bar-table"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-xbar-oper:cross-bar-stats/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CrossBarStats.Nodes.Node, ['node_name'], name, value)


            class CrossBarTable(Entity):
                """
                Table of stats information
                
                .. attribute:: skb_stats
                
                	Table of packet stats for SKB
                	**type**\:  :py:class:`SkbStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats>`
                
                	**config**\: False
                
                .. attribute:: pkt_stats
                
                	Table of packet stats
                	**type**\:  :py:class:`PktStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.PktStats>`
                
                	**config**\: False
                
                .. attribute:: sm15_stats
                
                	Table of packet stats for SM15
                	**type**\:  :py:class:`Sm15Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats>`
                
                	**config**\: False
                
                

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
                    self._child_classes = OrderedDict([("skb-stats", ("skb_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats)), ("pkt-stats", ("pkt_stats", CrossBarStats.Nodes.Node.CrossBarTable.PktStats)), ("sm15-stats", ("sm15_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats))])
                    self._leafs = OrderedDict()

                    self.skb_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats()
                    self.skb_stats.parent = self
                    self._children_name_map["skb_stats"] = "skb-stats"

                    self.pkt_stats = CrossBarStats.Nodes.Node.CrossBarTable.PktStats()
                    self.pkt_stats.parent = self
                    self._children_name_map["pkt_stats"] = "pkt-stats"

                    self.sm15_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats()
                    self.sm15_stats.parent = self
                    self._children_name_map["sm15_stats"] = "sm15-stats"
                    self._segment_path = lambda: "cross-bar-table"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable, [], name, value)


                class SkbStats(Entity):
                    """
                    Table of packet stats for SKB
                    
                    .. attribute:: skb_stat
                    
                    	Stats information for a particular asic type and port
                    	**type**\: list of  		 :py:class:`SkbStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'asr9k-xbar-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats, self).__init__()

                        self.yang_name = "skb-stats"
                        self.yang_parent_name = "cross-bar-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("skb-stat", ("skb_stat", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat))])
                        self._leafs = OrderedDict()

                        self.skb_stat = YList(self)
                        self._segment_path = lambda: "skb-stats"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats, [], name, value)


                    class SkbStat(Entity):
                        """
                        Stats information for a particular asic type
                        and port
                        
                        .. attribute:: asic_id
                        
                        	Asic ID
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        	**config**\: False
                        
                        .. attribute:: port
                        
                        	Port
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        	**config**\: False
                        
                        .. attribute:: in_stats
                        
                        	in stats
                        	**type**\:  :py:class:`InStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats>`
                        
                        	**config**\: False
                        
                        .. attribute:: eg_stats
                        
                        	eg stats
                        	**type**\:  :py:class:`EgStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats>`
                        
                        	**config**\: False
                        
                        .. attribute:: xps_stats
                        
                        	xps stats
                        	**type**\:  :py:class:`XpsStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.XpsStats>`
                        
                        	**config**\: False
                        
                        .. attribute:: internal_err_cnt
                        
                        	internal err cnt
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'asr9k-xbar-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat, self).__init__()

                            self.yang_name = "skb-stat"
                            self.yang_parent_name = "skb-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("in-stats", ("in_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats)), ("eg-stats", ("eg_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats)), ("xps-stats", ("xps_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.XpsStats))])
                            self._leafs = OrderedDict([
                                ('asic_id', (YLeaf(YType.str, 'asic-id'), ['str'])),
                                ('port', (YLeaf(YType.str, 'port'), ['str'])),
                                ('internal_err_cnt', (YLeaf(YType.uint64, 'internal-err-cnt'), ['int'])),
                            ])
                            self.asic_id = None
                            self.port = None
                            self.internal_err_cnt = None

                            self.in_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats()
                            self.in_stats.parent = self
                            self._children_name_map["in_stats"] = "in-stats"

                            self.eg_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats()
                            self.eg_stats.parent = self
                            self._children_name_map["eg_stats"] = "eg-stats"

                            self.xps_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.XpsStats()
                            self.xps_stats.parent = self
                            self._children_name_map["xps_stats"] = "xps-stats"
                            self._segment_path = lambda: "skb-stat"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat, ['asic_id', 'port', u'internal_err_cnt'], name, value)


                        class InStats(Entity):
                            """
                            in stats
                            
                            .. attribute:: ibb_stats
                            
                            	ibb stats
                            	**type**\:  :py:class:`IbbStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbbStats>`
                            
                            	**config**\: False
                            
                            .. attribute:: ibf_stats
                            
                            	ibf stats
                            	**type**\:  :py:class:`IbfStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbfStats>`
                            
                            	**config**\: False
                            
                            .. attribute:: ibb_uc_stats
                            
                            	ibb uc stats
                            	**type**\:  :py:class:`IbbUcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbbUcStats>`
                            
                            	**config**\: False
                            
                            .. attribute:: ibf_uc_stats
                            
                            	ibf uc stats
                            	**type**\:  :py:class:`IbfUcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbfUcStats>`
                            
                            	**config**\: False
                            
                            .. attribute:: ibb_mc_stats
                            
                            	ibb mc stats
                            	**type**\:  :py:class:`IbbMcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbbMcStats>`
                            
                            	**config**\: False
                            
                            .. attribute:: ibf_mc_stats
                            
                            	ibf mc stats
                            	**type**\:  :py:class:`IbfMcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbfMcStats>`
                            
                            	**config**\: False
                            
                            .. attribute:: cfl_stats
                            
                            	cfl stats
                            	**type**\:  :py:class:`CflStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'asr9k-xbar-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats, self).__init__()

                                self.yang_name = "in-stats"
                                self.yang_parent_name = "skb-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("ibb-stats", ("ibb_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbbStats)), ("ibf-stats", ("ibf_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbfStats)), ("ibb-uc-stats", ("ibb_uc_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbbUcStats)), ("ibf-uc-stats", ("ibf_uc_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbfUcStats)), ("ibb-mc-stats", ("ibb_mc_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbbMcStats)), ("ibf-mc-stats", ("ibf_mc_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbfMcStats)), ("cfl-stats", ("cfl_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats))])
                                self._leafs = OrderedDict()

                                self.ibb_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbbStats()
                                self.ibb_stats.parent = self
                                self._children_name_map["ibb_stats"] = "ibb-stats"

                                self.ibf_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbfStats()
                                self.ibf_stats.parent = self
                                self._children_name_map["ibf_stats"] = "ibf-stats"

                                self.ibb_uc_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbbUcStats()
                                self.ibb_uc_stats.parent = self
                                self._children_name_map["ibb_uc_stats"] = "ibb-uc-stats"

                                self.ibf_uc_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbfUcStats()
                                self.ibf_uc_stats.parent = self
                                self._children_name_map["ibf_uc_stats"] = "ibf-uc-stats"

                                self.ibb_mc_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbbMcStats()
                                self.ibb_mc_stats.parent = self
                                self._children_name_map["ibb_mc_stats"] = "ibb-mc-stats"

                                self.ibf_mc_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbfMcStats()
                                self.ibf_mc_stats.parent = self
                                self._children_name_map["ibf_mc_stats"] = "ibf-mc-stats"

                                self.cfl_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats()
                                self.cfl_stats.parent = self
                                self._children_name_map["cfl_stats"] = "cfl-stats"
                                self._segment_path = lambda: "in-stats"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats, [], name, value)


                            class IbbStats(Entity):
                                """
                                ibb stats
                                
                                .. attribute:: ipcicmtail_drop
                                
                                	IPCICMTAILDROP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: dhe_diag_pkt
                                
                                	DHEDIAGPKT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ibmdnouttot
                                
                                	IBMDNOUTTOT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: icmdnenq
                                
                                	ICMDNENQ
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: icmdndeq
                                
                                	ICMDNDEQ
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ibmcsrccouttot
                                
                                	IBMCSRCCOUTTOT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-xbar-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbbStats, self).__init__()

                                    self.yang_name = "ibb-stats"
                                    self.yang_parent_name = "in-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ipcicmtail_drop', (YLeaf(YType.uint64, 'ipcicmtail-drop'), ['int'])),
                                        ('dhe_diag_pkt', (YLeaf(YType.uint64, 'dhe-diag-pkt'), ['int'])),
                                        ('ibmdnouttot', (YLeaf(YType.uint64, 'ibmdnouttot'), ['int'])),
                                        ('icmdnenq', (YLeaf(YType.uint64, 'icmdnenq'), ['int'])),
                                        ('icmdndeq', (YLeaf(YType.uint64, 'icmdndeq'), ['int'])),
                                        ('ibmcsrccouttot', (YLeaf(YType.uint64, 'ibmcsrccouttot'), ['int'])),
                                    ])
                                    self.ipcicmtail_drop = None
                                    self.dhe_diag_pkt = None
                                    self.ibmdnouttot = None
                                    self.icmdnenq = None
                                    self.icmdndeq = None
                                    self.ibmcsrccouttot = None
                                    self._segment_path = lambda: "ibb-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbbStats, [u'ipcicmtail_drop', u'dhe_diag_pkt', u'ibmdnouttot', u'icmdnenq', u'icmdndeq', u'ibmcsrccouttot'], name, value)



                            class IbfStats(Entity):
                                """
                                ibf stats
                                
                                .. attribute:: unused
                                
                                	unused
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-xbar-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbfStats, self).__init__()

                                    self.yang_name = "ibf-stats"
                                    self.yang_parent_name = "in-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('unused', (YLeaf(YType.uint64, 'unused'), ['int'])),
                                    ])
                                    self.unused = None
                                    self._segment_path = lambda: "ibf-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbfStats, [u'unused'], name, value)



                            class IbbUcStats(Entity):
                                """
                                ibb uc stats
                                
                                .. attribute:: ipc_data_tot
                                
                                	IPCDATATOT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipc_data_totsz
                                
                                	IPCDATATOTSZ
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipcrunt
                                
                                	IPCRUNT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipcgiant
                                
                                	IPCGIANT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipc_data_err
                                
                                	IPCDATAERR
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipclinkerr
                                
                                	IPCLINKERR
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipcptcerr
                                
                                	IPCPTCERR
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipcpkt_drop
                                
                                	IPCPKTDROP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipcdes_drop
                                
                                	IPCDESDROP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: dhetail_drop
                                
                                	DHETAILDROP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ibmoutsop
                                
                                	IBMOUTSOP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ibmouteop
                                
                                	IBMOUTEOP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ibmoutbyte
                                
                                	IBMOUTBYTE
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: icmenq
                                
                                	ICMENQ
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: icmdeq
                                
                                	ICMDEQ
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: icmfcxoff
                                
                                	ICMFCXOFF
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: icmfcxon
                                
                                	ICMFCXON
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-xbar-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbbUcStats, self).__init__()

                                    self.yang_name = "ibb-uc-stats"
                                    self.yang_parent_name = "in-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ipc_data_tot', (YLeaf(YType.uint64, 'ipc-data-tot'), ['int'])),
                                        ('ipc_data_totsz', (YLeaf(YType.uint64, 'ipc-data-totsz'), ['int'])),
                                        ('ipcrunt', (YLeaf(YType.uint64, 'ipcrunt'), ['int'])),
                                        ('ipcgiant', (YLeaf(YType.uint64, 'ipcgiant'), ['int'])),
                                        ('ipc_data_err', (YLeaf(YType.uint64, 'ipc-data-err'), ['int'])),
                                        ('ipclinkerr', (YLeaf(YType.uint64, 'ipclinkerr'), ['int'])),
                                        ('ipcptcerr', (YLeaf(YType.uint64, 'ipcptcerr'), ['int'])),
                                        ('ipcpkt_drop', (YLeaf(YType.uint64, 'ipcpkt-drop'), ['int'])),
                                        ('ipcdes_drop', (YLeaf(YType.uint64, 'ipcdes-drop'), ['int'])),
                                        ('dhetail_drop', (YLeaf(YType.uint64, 'dhetail-drop'), ['int'])),
                                        ('ibmoutsop', (YLeaf(YType.uint64, 'ibmoutsop'), ['int'])),
                                        ('ibmouteop', (YLeaf(YType.uint64, 'ibmouteop'), ['int'])),
                                        ('ibmoutbyte', (YLeaf(YType.uint64, 'ibmoutbyte'), ['int'])),
                                        ('icmenq', (YLeaf(YType.uint64, 'icmenq'), ['int'])),
                                        ('icmdeq', (YLeaf(YType.uint64, 'icmdeq'), ['int'])),
                                        ('icmfcxoff', (YLeaf(YType.uint64, 'icmfcxoff'), ['int'])),
                                        ('icmfcxon', (YLeaf(YType.uint64, 'icmfcxon'), ['int'])),
                                    ])
                                    self.ipc_data_tot = None
                                    self.ipc_data_totsz = None
                                    self.ipcrunt = None
                                    self.ipcgiant = None
                                    self.ipc_data_err = None
                                    self.ipclinkerr = None
                                    self.ipcptcerr = None
                                    self.ipcpkt_drop = None
                                    self.ipcdes_drop = None
                                    self.dhetail_drop = None
                                    self.ibmoutsop = None
                                    self.ibmouteop = None
                                    self.ibmoutbyte = None
                                    self.icmenq = None
                                    self.icmdeq = None
                                    self.icmfcxoff = None
                                    self.icmfcxon = None
                                    self._segment_path = lambda: "ibb-uc-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbbUcStats, [u'ipc_data_tot', u'ipc_data_totsz', u'ipcrunt', u'ipcgiant', u'ipc_data_err', u'ipclinkerr', u'ipcptcerr', u'ipcpkt_drop', u'ipcdes_drop', u'dhetail_drop', u'ibmoutsop', u'ibmouteop', u'ibmoutbyte', u'icmenq', u'icmdeq', u'icmfcxoff', u'icmfcxon'], name, value)



                            class IbfUcStats(Entity):
                                """
                                ibf uc stats
                                
                                .. attribute:: pktcnt
                                
                                	PKTCNT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pktoutp0cnt
                                
                                	PKTOUTP0CNT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pktoutp1cnt
                                
                                	PKTOUTP1CNT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pkt_input_err_drop
                                
                                	PKTINPUTERRDROP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pkthwerr_drop
                                
                                	PKTHWERRDROP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pkt_null_poe_drop
                                
                                	PKTNULLPOEDROP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pkt_disp_oe_drop
                                
                                	PKTDISPOEDROP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-xbar-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbfUcStats, self).__init__()

                                    self.yang_name = "ibf-uc-stats"
                                    self.yang_parent_name = "in-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('pktcnt', (YLeaf(YType.uint64, 'pktcnt'), ['int'])),
                                        ('pktoutp0cnt', (YLeaf(YType.uint64, 'pktoutp0cnt'), ['int'])),
                                        ('pktoutp1cnt', (YLeaf(YType.uint64, 'pktoutp1cnt'), ['int'])),
                                        ('pkt_input_err_drop', (YLeaf(YType.uint64, 'pkt-input-err-drop'), ['int'])),
                                        ('pkthwerr_drop', (YLeaf(YType.uint64, 'pkthwerr-drop'), ['int'])),
                                        ('pkt_null_poe_drop', (YLeaf(YType.uint64, 'pkt-null-poe-drop'), ['int'])),
                                        ('pkt_disp_oe_drop', (YLeaf(YType.uint64, 'pkt-disp-oe-drop'), ['int'])),
                                    ])
                                    self.pktcnt = None
                                    self.pktoutp0cnt = None
                                    self.pktoutp1cnt = None
                                    self.pkt_input_err_drop = None
                                    self.pkthwerr_drop = None
                                    self.pkt_null_poe_drop = None
                                    self.pkt_disp_oe_drop = None
                                    self._segment_path = lambda: "ibf-uc-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbfUcStats, [u'pktcnt', u'pktoutp0cnt', u'pktoutp1cnt', u'pkt_input_err_drop', u'pkthwerr_drop', u'pkt_null_poe_drop', u'pkt_disp_oe_drop'], name, value)



                            class IbbMcStats(Entity):
                                """
                                ibb mc stats
                                
                                .. attribute:: ipc_data_tot
                                
                                	IPCDATATOT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipc_data_totsz
                                
                                	IPCDATATOTSZ
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipcrunt
                                
                                	IPCRUNT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipcgiant
                                
                                	IPCGIANT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipc_data_err
                                
                                	IPCDATAERR
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipclinkerr
                                
                                	IPCLINKERR
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipcptcerr
                                
                                	IPCPTCERR
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipcpkt_drop
                                
                                	IPCPKTDROP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipcdes_drop
                                
                                	IPCDESDROP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: dhehitail_drop
                                
                                	DHEHITAILDROP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: dhelotail_drop
                                
                                	DHELOTAILDROP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ibmoutsop
                                
                                	IBMOUTSOP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ibmouteop
                                
                                	IBMOUTEOP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ibmoutbyte
                                
                                	IBMOUTBYTE
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: icmenq
                                
                                	ICMENQ
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: icmdeq
                                
                                	ICMDEQ
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: icmfcxoff
                                
                                	ICMFCXOFF
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: icmfcxon
                                
                                	ICMFCXON
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-xbar-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbbMcStats, self).__init__()

                                    self.yang_name = "ibb-mc-stats"
                                    self.yang_parent_name = "in-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ipc_data_tot', (YLeaf(YType.uint64, 'ipc-data-tot'), ['int'])),
                                        ('ipc_data_totsz', (YLeaf(YType.uint64, 'ipc-data-totsz'), ['int'])),
                                        ('ipcrunt', (YLeaf(YType.uint64, 'ipcrunt'), ['int'])),
                                        ('ipcgiant', (YLeaf(YType.uint64, 'ipcgiant'), ['int'])),
                                        ('ipc_data_err', (YLeaf(YType.uint64, 'ipc-data-err'), ['int'])),
                                        ('ipclinkerr', (YLeaf(YType.uint64, 'ipclinkerr'), ['int'])),
                                        ('ipcptcerr', (YLeaf(YType.uint64, 'ipcptcerr'), ['int'])),
                                        ('ipcpkt_drop', (YLeaf(YType.uint64, 'ipcpkt-drop'), ['int'])),
                                        ('ipcdes_drop', (YLeaf(YType.uint64, 'ipcdes-drop'), ['int'])),
                                        ('dhehitail_drop', (YLeaf(YType.uint64, 'dhehitail-drop'), ['int'])),
                                        ('dhelotail_drop', (YLeaf(YType.uint64, 'dhelotail-drop'), ['int'])),
                                        ('ibmoutsop', (YLeaf(YType.uint64, 'ibmoutsop'), ['int'])),
                                        ('ibmouteop', (YLeaf(YType.uint64, 'ibmouteop'), ['int'])),
                                        ('ibmoutbyte', (YLeaf(YType.uint64, 'ibmoutbyte'), ['int'])),
                                        ('icmenq', (YLeaf(YType.uint64, 'icmenq'), ['int'])),
                                        ('icmdeq', (YLeaf(YType.uint64, 'icmdeq'), ['int'])),
                                        ('icmfcxoff', (YLeaf(YType.uint64, 'icmfcxoff'), ['int'])),
                                        ('icmfcxon', (YLeaf(YType.uint64, 'icmfcxon'), ['int'])),
                                    ])
                                    self.ipc_data_tot = None
                                    self.ipc_data_totsz = None
                                    self.ipcrunt = None
                                    self.ipcgiant = None
                                    self.ipc_data_err = None
                                    self.ipclinkerr = None
                                    self.ipcptcerr = None
                                    self.ipcpkt_drop = None
                                    self.ipcdes_drop = None
                                    self.dhehitail_drop = None
                                    self.dhelotail_drop = None
                                    self.ibmoutsop = None
                                    self.ibmouteop = None
                                    self.ibmoutbyte = None
                                    self.icmenq = None
                                    self.icmdeq = None
                                    self.icmfcxoff = None
                                    self.icmfcxon = None
                                    self._segment_path = lambda: "ibb-mc-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbbMcStats, [u'ipc_data_tot', u'ipc_data_totsz', u'ipcrunt', u'ipcgiant', u'ipc_data_err', u'ipclinkerr', u'ipcptcerr', u'ipcpkt_drop', u'ipcdes_drop', u'dhehitail_drop', u'dhelotail_drop', u'ibmoutsop', u'ibmouteop', u'ibmoutbyte', u'icmenq', u'icmdeq', u'icmfcxoff', u'icmfcxon'], name, value)



                            class IbfMcStats(Entity):
                                """
                                ibf mc stats
                                
                                .. attribute:: pktcnt
                                
                                	PKTCNT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pktoutcnt
                                
                                	PKTOUTCNT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pkthi_copy_sup_event
                                
                                	PKTHICOPYSUPEVENT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pktlo_copy_sup_event
                                
                                	PKTLOCOPYSUPEVENT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pkt_input_err_drop
                                
                                	PKTINPUTERRDROP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pktfgid_addr_err_drop
                                
                                	PKTFGIDADDRERRDROP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pktfgidlkuperr_drop
                                
                                	PKTFGIDLKUPERRDROP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pkt_null_poe_drop
                                
                                	PKTNULLPOEDROP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pkt_copy_sup_drop
                                
                                	PKTCOPYSUPDROP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pkt_disp_oe_drop
                                
                                	PKTDISPOEDROP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pktto_drop_cnt
                                
                                	PKTTODROPCNT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-xbar-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbfMcStats, self).__init__()

                                    self.yang_name = "ibf-mc-stats"
                                    self.yang_parent_name = "in-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('pktcnt', (YLeaf(YType.uint64, 'pktcnt'), ['int'])),
                                        ('pktoutcnt', (YLeaf(YType.uint64, 'pktoutcnt'), ['int'])),
                                        ('pkthi_copy_sup_event', (YLeaf(YType.uint64, 'pkthi-copy-sup-event'), ['int'])),
                                        ('pktlo_copy_sup_event', (YLeaf(YType.uint64, 'pktlo-copy-sup-event'), ['int'])),
                                        ('pkt_input_err_drop', (YLeaf(YType.uint64, 'pkt-input-err-drop'), ['int'])),
                                        ('pktfgid_addr_err_drop', (YLeaf(YType.uint64, 'pktfgid-addr-err-drop'), ['int'])),
                                        ('pktfgidlkuperr_drop', (YLeaf(YType.uint64, 'pktfgidlkuperr-drop'), ['int'])),
                                        ('pkt_null_poe_drop', (YLeaf(YType.uint64, 'pkt-null-poe-drop'), ['int'])),
                                        ('pkt_copy_sup_drop', (YLeaf(YType.uint64, 'pkt-copy-sup-drop'), ['int'])),
                                        ('pkt_disp_oe_drop', (YLeaf(YType.uint64, 'pkt-disp-oe-drop'), ['int'])),
                                        ('pktto_drop_cnt', (YLeaf(YType.uint64, 'pktto-drop-cnt'), ['int'])),
                                    ])
                                    self.pktcnt = None
                                    self.pktoutcnt = None
                                    self.pkthi_copy_sup_event = None
                                    self.pktlo_copy_sup_event = None
                                    self.pkt_input_err_drop = None
                                    self.pktfgid_addr_err_drop = None
                                    self.pktfgidlkuperr_drop = None
                                    self.pkt_null_poe_drop = None
                                    self.pkt_copy_sup_drop = None
                                    self.pkt_disp_oe_drop = None
                                    self.pktto_drop_cnt = None
                                    self._segment_path = lambda: "ibf-mc-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.IbfMcStats, [u'pktcnt', u'pktoutcnt', u'pkthi_copy_sup_event', u'pktlo_copy_sup_event', u'pkt_input_err_drop', u'pktfgid_addr_err_drop', u'pktfgidlkuperr_drop', u'pkt_null_poe_drop', u'pkt_copy_sup_drop', u'pkt_disp_oe_drop', u'pktto_drop_cnt'], name, value)



                            class CflStats(Entity):
                                """
                                cfl stats
                                
                                .. attribute:: cfl_uc_stats
                                
                                	cfl uc stats
                                	**type**\:  :py:class:`CflUcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats.CflUcStats>`
                                
                                	**config**\: False
                                
                                .. attribute:: cfl_mc_stats
                                
                                	cfl mc stats
                                	**type**\:  :py:class:`CflMcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats.CflMcStats>`
                                
                                	**config**\: False
                                
                                .. attribute:: cfl_misc_stats
                                
                                	cfl misc stats
                                	**type**\:  :py:class:`CflMiscStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats.CflMiscStats>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-xbar-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats, self).__init__()

                                    self.yang_name = "cfl-stats"
                                    self.yang_parent_name = "in-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("cfl-uc-stats", ("cfl_uc_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats.CflUcStats)), ("cfl-mc-stats", ("cfl_mc_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats.CflMcStats)), ("cfl-misc-stats", ("cfl_misc_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats.CflMiscStats))])
                                    self._leafs = OrderedDict()

                                    self.cfl_uc_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats.CflUcStats()
                                    self.cfl_uc_stats.parent = self
                                    self._children_name_map["cfl_uc_stats"] = "cfl-uc-stats"

                                    self.cfl_mc_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats.CflMcStats()
                                    self.cfl_mc_stats.parent = self
                                    self._children_name_map["cfl_mc_stats"] = "cfl-mc-stats"

                                    self.cfl_misc_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats.CflMiscStats()
                                    self.cfl_misc_stats.parent = self
                                    self._children_name_map["cfl_misc_stats"] = "cfl-misc-stats"
                                    self._segment_path = lambda: "cfl-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats, [], name, value)


                                class CflUcStats(Entity):
                                    """
                                    cfl uc stats
                                    
                                    .. attribute:: crc_match_pattern
                                    
                                    	CRC MATCH PATTERN
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: pkts_rcvd
                                    
                                    	PKTS RCVD
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: packed_pkts_rcvd
                                    
                                    	PACKED PKTS RCVD
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: pkts_flushed
                                    
                                    	PKTS FLUSHED
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: runt_pkts_drop_ped
                                    
                                    	RUNT PKTS DROPPED
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: small_pkts_drop_ped
                                    
                                    	SMALL PKTS DROPPED
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: pkts_to_ib_from_port
                                    
                                    	PKTS TO IB FROM PORT
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: in_uc_rate
                                    
                                    	in uc rate
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'asr9k-xbar-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats.CflUcStats, self).__init__()

                                        self.yang_name = "cfl-uc-stats"
                                        self.yang_parent_name = "cfl-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('crc_match_pattern', (YLeaf(YType.uint64, 'crc-match-pattern'), ['int'])),
                                            ('pkts_rcvd', (YLeaf(YType.uint64, 'pkts-rcvd'), ['int'])),
                                            ('packed_pkts_rcvd', (YLeaf(YType.uint64, 'packed-pkts-rcvd'), ['int'])),
                                            ('pkts_flushed', (YLeaf(YType.uint64, 'pkts-flushed'), ['int'])),
                                            ('runt_pkts_drop_ped', (YLeaf(YType.uint64, 'runt-pkts-drop-ped'), ['int'])),
                                            ('small_pkts_drop_ped', (YLeaf(YType.uint64, 'small-pkts-drop-ped'), ['int'])),
                                            ('pkts_to_ib_from_port', (YLeaf(YType.uint64, 'pkts-to-ib-from-port'), ['int'])),
                                            ('in_uc_rate', (YLeaf(YType.uint64, 'in-uc-rate'), ['int'])),
                                        ])
                                        self.crc_match_pattern = None
                                        self.pkts_rcvd = None
                                        self.packed_pkts_rcvd = None
                                        self.pkts_flushed = None
                                        self.runt_pkts_drop_ped = None
                                        self.small_pkts_drop_ped = None
                                        self.pkts_to_ib_from_port = None
                                        self.in_uc_rate = None
                                        self._segment_path = lambda: "cfl-uc-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats.CflUcStats, [u'crc_match_pattern', u'pkts_rcvd', u'packed_pkts_rcvd', u'pkts_flushed', u'runt_pkts_drop_ped', u'small_pkts_drop_ped', u'pkts_to_ib_from_port', u'in_uc_rate'], name, value)



                                class CflMcStats(Entity):
                                    """
                                    cfl mc stats
                                    
                                    .. attribute:: crc_match_pattern
                                    
                                    	CRC MATCH PATTERN
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: pkts_rcvd
                                    
                                    	PKTS RCVD
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: packed_pkts_rcvd
                                    
                                    	PACKED PKTS RCVD
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: pkts_flushed
                                    
                                    	PKTS FLUSHED
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: runt_pkts_drop_ped
                                    
                                    	RUNT PKTS DROPPED
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: small_pkts_drop_ped
                                    
                                    	SMALL PKTS DROPPED
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: pkts_to_ib_from_port
                                    
                                    	PKTS TO IB FROM PORT
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: in_mc_rate
                                    
                                    	in mc rate
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'asr9k-xbar-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats.CflMcStats, self).__init__()

                                        self.yang_name = "cfl-mc-stats"
                                        self.yang_parent_name = "cfl-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('crc_match_pattern', (YLeaf(YType.uint64, 'crc-match-pattern'), ['int'])),
                                            ('pkts_rcvd', (YLeaf(YType.uint64, 'pkts-rcvd'), ['int'])),
                                            ('packed_pkts_rcvd', (YLeaf(YType.uint64, 'packed-pkts-rcvd'), ['int'])),
                                            ('pkts_flushed', (YLeaf(YType.uint64, 'pkts-flushed'), ['int'])),
                                            ('runt_pkts_drop_ped', (YLeaf(YType.uint64, 'runt-pkts-drop-ped'), ['int'])),
                                            ('small_pkts_drop_ped', (YLeaf(YType.uint64, 'small-pkts-drop-ped'), ['int'])),
                                            ('pkts_to_ib_from_port', (YLeaf(YType.uint64, 'pkts-to-ib-from-port'), ['int'])),
                                            ('in_mc_rate', (YLeaf(YType.uint64, 'in-mc-rate'), ['int'])),
                                        ])
                                        self.crc_match_pattern = None
                                        self.pkts_rcvd = None
                                        self.packed_pkts_rcvd = None
                                        self.pkts_flushed = None
                                        self.runt_pkts_drop_ped = None
                                        self.small_pkts_drop_ped = None
                                        self.pkts_to_ib_from_port = None
                                        self.in_mc_rate = None
                                        self._segment_path = lambda: "cfl-mc-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats.CflMcStats, [u'crc_match_pattern', u'pkts_rcvd', u'packed_pkts_rcvd', u'pkts_flushed', u'runt_pkts_drop_ped', u'small_pkts_drop_ped', u'pkts_to_ib_from_port', u'in_mc_rate'], name, value)



                                class CflMiscStats(Entity):
                                    """
                                    cfl misc stats
                                    
                                    .. attribute:: crc_stomp
                                    
                                    	CRC STOMP
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: crc_new_err
                                    
                                    	CRC NEW ERR
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: in_total_rate
                                    
                                    	in total rate
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'asr9k-xbar-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats.CflMiscStats, self).__init__()

                                        self.yang_name = "cfl-misc-stats"
                                        self.yang_parent_name = "cfl-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('crc_stomp', (YLeaf(YType.uint64, 'crc-stomp'), ['int'])),
                                            ('crc_new_err', (YLeaf(YType.uint64, 'crc-new-err'), ['int'])),
                                            ('in_total_rate', (YLeaf(YType.uint64, 'in-total-rate'), ['int'])),
                                        ])
                                        self.crc_stomp = None
                                        self.crc_new_err = None
                                        self.in_total_rate = None
                                        self._segment_path = lambda: "cfl-misc-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.InStats.CflStats.CflMiscStats, [u'crc_stomp', u'crc_new_err', u'in_total_rate'], name, value)





                        class EgStats(Entity):
                            """
                            eg stats
                            
                            .. attribute:: obu_stats
                            
                            	obu stats
                            	**type**\:  :py:class:`ObuStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.ObuStats>`
                            
                            	**config**\: False
                            
                            .. attribute:: obu_uc_stats
                            
                            	obu uc stats
                            	**type**\:  :py:class:`ObuUcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.ObuUcStats>`
                            
                            	**config**\: False
                            
                            .. attribute:: obu_mc_stats
                            
                            	obu mc stats
                            	**type**\:  :py:class:`ObuMcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.ObuMcStats>`
                            
                            	**config**\: False
                            
                            .. attribute:: cfl_stats
                            
                            	cfl stats
                            	**type**\:  :py:class:`CflStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'asr9k-xbar-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats, self).__init__()

                                self.yang_name = "eg-stats"
                                self.yang_parent_name = "skb-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("obu-stats", ("obu_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.ObuStats)), ("obu-uc-stats", ("obu_uc_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.ObuUcStats)), ("obu-mc-stats", ("obu_mc_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.ObuMcStats)), ("cfl-stats", ("cfl_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats))])
                                self._leafs = OrderedDict()

                                self.obu_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.ObuStats()
                                self.obu_stats.parent = self
                                self._children_name_map["obu_stats"] = "obu-stats"

                                self.obu_uc_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.ObuUcStats()
                                self.obu_uc_stats.parent = self
                                self._children_name_map["obu_uc_stats"] = "obu-uc-stats"

                                self.obu_mc_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.ObuMcStats()
                                self.obu_mc_stats.parent = self
                                self._children_name_map["obu_mc_stats"] = "obu-mc-stats"

                                self.cfl_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats()
                                self.cfl_stats.parent = self
                                self._children_name_map["cfl_stats"] = "cfl-stats"
                                self._segment_path = lambda: "eg-stats"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats, [], name, value)


                            class ObuStats(Entity):
                                """
                                obu stats
                                
                                .. attribute:: data_queque
                                
                                	data queque
                                	**type**\: list of int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-xbar-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.ObuStats, self).__init__()

                                    self.yang_name = "obu-stats"
                                    self.yang_parent_name = "eg-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('data_queque', (YLeafList(YType.uint32, 'data-queque'), ['int'])),
                                    ])
                                    self.data_queque = []
                                    self._segment_path = lambda: "obu-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.ObuStats, [u'data_queque'], name, value)



                            class ObuUcStats(Entity):
                                """
                                obu uc stats
                                
                                .. attribute:: pktin
                                
                                	PKTIN
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pktout
                                
                                	PKTOUT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: bytein
                                
                                	BYTEIN
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: byteout
                                
                                	BYTEOUT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pkttrunc
                                
                                	PKTTRUNC
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-xbar-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.ObuUcStats, self).__init__()

                                    self.yang_name = "obu-uc-stats"
                                    self.yang_parent_name = "eg-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('pktin', (YLeaf(YType.uint64, 'pktin'), ['int'])),
                                        ('pktout', (YLeaf(YType.uint64, 'pktout'), ['int'])),
                                        ('bytein', (YLeaf(YType.uint64, 'bytein'), ['int'])),
                                        ('byteout', (YLeaf(YType.uint64, 'byteout'), ['int'])),
                                        ('pkttrunc', (YLeaf(YType.uint64, 'pkttrunc'), ['int'])),
                                    ])
                                    self.pktin = None
                                    self.pktout = None
                                    self.bytein = None
                                    self.byteout = None
                                    self.pkttrunc = None
                                    self._segment_path = lambda: "obu-uc-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.ObuUcStats, [u'pktin', u'pktout', u'bytein', u'byteout', u'pkttrunc'], name, value)



                            class ObuMcStats(Entity):
                                """
                                obu mc stats
                                
                                .. attribute:: pktin
                                
                                	PKTIN
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pktout
                                
                                	PKTOUT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: bytein
                                
                                	BYTEIN
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: byteout
                                
                                	BYTEOUT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: pkttrunc
                                
                                	PKTTRUNC
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-xbar-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.ObuMcStats, self).__init__()

                                    self.yang_name = "obu-mc-stats"
                                    self.yang_parent_name = "eg-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('pktin', (YLeaf(YType.uint64, 'pktin'), ['int'])),
                                        ('pktout', (YLeaf(YType.uint64, 'pktout'), ['int'])),
                                        ('bytein', (YLeaf(YType.uint64, 'bytein'), ['int'])),
                                        ('byteout', (YLeaf(YType.uint64, 'byteout'), ['int'])),
                                        ('pkttrunc', (YLeaf(YType.uint64, 'pkttrunc'), ['int'])),
                                    ])
                                    self.pktin = None
                                    self.pktout = None
                                    self.bytein = None
                                    self.byteout = None
                                    self.pkttrunc = None
                                    self._segment_path = lambda: "obu-mc-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.ObuMcStats, [u'pktin', u'pktout', u'bytein', u'byteout', u'pkttrunc'], name, value)



                            class CflStats(Entity):
                                """
                                cfl stats
                                
                                .. attribute:: cfl_uc_stats
                                
                                	cfl uc stats
                                	**type**\:  :py:class:`CflUcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats.CflUcStats>`
                                
                                	**config**\: False
                                
                                .. attribute:: cfl_mc_stats
                                
                                	cfl mc stats
                                	**type**\:  :py:class:`CflMcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats.CflMcStats>`
                                
                                	**config**\: False
                                
                                .. attribute:: cfl_misc_stats
                                
                                	cfl misc stats
                                	**type**\:  :py:class:`CflMiscStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats.CflMiscStats>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-xbar-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats, self).__init__()

                                    self.yang_name = "cfl-stats"
                                    self.yang_parent_name = "eg-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("cfl-uc-stats", ("cfl_uc_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats.CflUcStats)), ("cfl-mc-stats", ("cfl_mc_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats.CflMcStats)), ("cfl-misc-stats", ("cfl_misc_stats", CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats.CflMiscStats))])
                                    self._leafs = OrderedDict()

                                    self.cfl_uc_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats.CflUcStats()
                                    self.cfl_uc_stats.parent = self
                                    self._children_name_map["cfl_uc_stats"] = "cfl-uc-stats"

                                    self.cfl_mc_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats.CflMcStats()
                                    self.cfl_mc_stats.parent = self
                                    self._children_name_map["cfl_mc_stats"] = "cfl-mc-stats"

                                    self.cfl_misc_stats = CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats.CflMiscStats()
                                    self.cfl_misc_stats.parent = self
                                    self._children_name_map["cfl_misc_stats"] = "cfl-misc-stats"
                                    self._segment_path = lambda: "cfl-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats, [], name, value)


                                class CflUcStats(Entity):
                                    """
                                    cfl uc stats
                                    
                                    .. attribute:: pkts_truncated
                                    
                                    	PKTS TRUNCATED
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: pkts_from_ob_to_port
                                    
                                    	PKTS FROM OB TO PORT
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: eg_uc_rate
                                    
                                    	eg uc rate
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'asr9k-xbar-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats.CflUcStats, self).__init__()

                                        self.yang_name = "cfl-uc-stats"
                                        self.yang_parent_name = "cfl-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('pkts_truncated', (YLeaf(YType.uint64, 'pkts-truncated'), ['int'])),
                                            ('pkts_from_ob_to_port', (YLeaf(YType.uint64, 'pkts-from-ob-to-port'), ['int'])),
                                            ('eg_uc_rate', (YLeaf(YType.uint64, 'eg-uc-rate'), ['int'])),
                                        ])
                                        self.pkts_truncated = None
                                        self.pkts_from_ob_to_port = None
                                        self.eg_uc_rate = None
                                        self._segment_path = lambda: "cfl-uc-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats.CflUcStats, [u'pkts_truncated', u'pkts_from_ob_to_port', u'eg_uc_rate'], name, value)



                                class CflMcStats(Entity):
                                    """
                                    cfl mc stats
                                    
                                    .. attribute:: pkts_truncated
                                    
                                    	PKTS TRUNCATED
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: pkts_from_ob_to_port
                                    
                                    	PKTS FROM OB TO PORT
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: eg_mc_rate
                                    
                                    	eg mc rate
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'asr9k-xbar-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats.CflMcStats, self).__init__()

                                        self.yang_name = "cfl-mc-stats"
                                        self.yang_parent_name = "cfl-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('pkts_truncated', (YLeaf(YType.uint64, 'pkts-truncated'), ['int'])),
                                            ('pkts_from_ob_to_port', (YLeaf(YType.uint64, 'pkts-from-ob-to-port'), ['int'])),
                                            ('eg_mc_rate', (YLeaf(YType.uint64, 'eg-mc-rate'), ['int'])),
                                        ])
                                        self.pkts_truncated = None
                                        self.pkts_from_ob_to_port = None
                                        self.eg_mc_rate = None
                                        self._segment_path = lambda: "cfl-mc-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats.CflMcStats, [u'pkts_truncated', u'pkts_from_ob_to_port', u'eg_mc_rate'], name, value)



                                class CflMiscStats(Entity):
                                    """
                                    cfl misc stats
                                    
                                    .. attribute:: ecc_corr_err
                                    
                                    	ECC CORR ERR
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ecc_uncorr_err
                                    
                                    	ECC UNCORR ERR
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ecc_raw_corr_err
                                    
                                    	ECC RAW CORR ERR
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ecc_raw_uncorr_err
                                    
                                    	ECC RAW UNCORR ERR
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: eg_total_rate
                                    
                                    	eg total rate
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'asr9k-xbar-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats.CflMiscStats, self).__init__()

                                        self.yang_name = "cfl-misc-stats"
                                        self.yang_parent_name = "cfl-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('ecc_corr_err', (YLeaf(YType.uint64, 'ecc-corr-err'), ['int'])),
                                            ('ecc_uncorr_err', (YLeaf(YType.uint64, 'ecc-uncorr-err'), ['int'])),
                                            ('ecc_raw_corr_err', (YLeaf(YType.uint64, 'ecc-raw-corr-err'), ['int'])),
                                            ('ecc_raw_uncorr_err', (YLeaf(YType.uint64, 'ecc-raw-uncorr-err'), ['int'])),
                                            ('eg_total_rate', (YLeaf(YType.uint64, 'eg-total-rate'), ['int'])),
                                        ])
                                        self.ecc_corr_err = None
                                        self.ecc_uncorr_err = None
                                        self.ecc_raw_corr_err = None
                                        self.ecc_raw_uncorr_err = None
                                        self.eg_total_rate = None
                                        self._segment_path = lambda: "cfl-misc-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.EgStats.CflStats.CflMiscStats, [u'ecc_corr_err', u'ecc_uncorr_err', u'ecc_raw_corr_err', u'ecc_raw_uncorr_err', u'eg_total_rate'], name, value)





                        class XpsStats(Entity):
                            """
                            xps stats
                            
                            .. attribute:: uc_timer_drop
                            
                            	UC TIMERDROP
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: uc_timer_truncate
                            
                            	UC TIMERTRUNCATE
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: mc_timer_drop
                            
                            	MC TIMERDROP
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: mc_timer_truncate
                            
                            	MC TIMERTRUNCATE
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'asr9k-xbar-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.XpsStats, self).__init__()

                                self.yang_name = "xps-stats"
                                self.yang_parent_name = "skb-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('uc_timer_drop', (YLeaf(YType.uint64, 'uc-timer-drop'), ['int'])),
                                    ('uc_timer_truncate', (YLeaf(YType.uint64, 'uc-timer-truncate'), ['int'])),
                                    ('mc_timer_drop', (YLeaf(YType.uint64, 'mc-timer-drop'), ['int'])),
                                    ('mc_timer_truncate', (YLeaf(YType.uint64, 'mc-timer-truncate'), ['int'])),
                                ])
                                self.uc_timer_drop = None
                                self.uc_timer_truncate = None
                                self.mc_timer_drop = None
                                self.mc_timer_truncate = None
                                self._segment_path = lambda: "xps-stats"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.SkbStats.SkbStat.XpsStats, [u'uc_timer_drop', u'uc_timer_truncate', u'mc_timer_drop', u'mc_timer_truncate'], name, value)





                class PktStats(Entity):
                    """
                    Table of packet stats
                    
                    .. attribute:: pkt_stat
                    
                    	Stats information for a particular asic type and port
                    	**type**\: list of  		 :py:class:`PktStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.PktStats.PktStat>`
                    
                    	**config**\: False
                    
                    

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
                        self._child_classes = OrderedDict([("pkt-stat", ("pkt_stat", CrossBarStats.Nodes.Node.CrossBarTable.PktStats.PktStat))])
                        self._leafs = OrderedDict()

                        self.pkt_stat = YList(self)
                        self._segment_path = lambda: "pkt-stats"
                        self._is_frozen = True

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
                        
                        	**config**\: False
                        
                        .. attribute:: port
                        
                        	Port
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        	**config**\: False
                        
                        .. attribute:: internal_error_count
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: input_buffer_queued_packet_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: ingress_packet_count_since_last_read_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: ingress_channel_utilization_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: input_buffer_back_pressure_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: xbar_timeout_drop_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: holdrop_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: null_fpoe_drop_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: diagnostic_packet_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: input_buffer_correctable_ecc_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: input_buffer_uncorrectable_ecc_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: header_crc_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: short_input_header_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: packet_crc_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: short_packet_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: output_buffer_queued_packet_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: egress_packet_count_since_last_read_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: egress_channel_utilization_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: output_buffer_back_pressure_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: output_buffer_correctable_ecc_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: output_buffer_uncorrectable_ecc_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: fpoedb_correctable_ecc_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: fpoedb_uncorrectable_ecc_error_count_high
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: input_buffer_queued_packet_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: ingress_packet_count_since_last_read_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: ingress_channel_utilization_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: input_buffer_back_pressure_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: xbar_timeout_drop_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: holdrop_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: null_fpoe_drop_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: diagnostic_packet_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: input_buffer_correctable_ecc_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: input_buffer_uncorrectable_ecc_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: header_crc_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: short_input_header_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: packet_crc_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: short_packet_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: output_buffer_queued_packet_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: egress_packet_count_since_last_read_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: egress_channel_utilization_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: output_buffer_back_pressure_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: output_buffer_correctable_ecc_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: output_buffer_uncorrectable_ecc_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: fpoedb_correctable_ecc_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: fpoedb_uncorrectable_ecc_error_count_low
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

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
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('asic_id', (YLeaf(YType.str, 'asic-id'), ['str'])),
                                ('port', (YLeaf(YType.str, 'port'), ['str'])),
                                ('internal_error_count', (YLeaf(YType.uint64, 'internal-error-count'), ['int'])),
                                ('input_buffer_queued_packet_count_high', (YLeaf(YType.uint64, 'input-buffer-queued-packet-count-high'), ['int'])),
                                ('ingress_packet_count_since_last_read_high', (YLeaf(YType.uint64, 'ingress-packet-count-since-last-read-high'), ['int'])),
                                ('ingress_channel_utilization_count_high', (YLeaf(YType.uint64, 'ingress-channel-utilization-count-high'), ['int'])),
                                ('input_buffer_back_pressure_count_high', (YLeaf(YType.uint64, 'input-buffer-back-pressure-count-high'), ['int'])),
                                ('xbar_timeout_drop_count_high', (YLeaf(YType.uint64, 'xbar-timeout-drop-count-high'), ['int'])),
                                ('holdrop_count_high', (YLeaf(YType.uint64, 'holdrop-count-high'), ['int'])),
                                ('null_fpoe_drop_count_high', (YLeaf(YType.uint64, 'null-fpoe-drop-count-high'), ['int'])),
                                ('diagnostic_packet_count_high', (YLeaf(YType.uint64, 'diagnostic-packet-count-high'), ['int'])),
                                ('input_buffer_correctable_ecc_error_count_high', (YLeaf(YType.uint64, 'input-buffer-correctable-ecc-error-count-high'), ['int'])),
                                ('input_buffer_uncorrectable_ecc_error_count_high', (YLeaf(YType.uint64, 'input-buffer-uncorrectable-ecc-error-count-high'), ['int'])),
                                ('header_crc_error_count_high', (YLeaf(YType.uint64, 'header-crc-error-count-high'), ['int'])),
                                ('short_input_header_error_count_high', (YLeaf(YType.uint64, 'short-input-header-error-count-high'), ['int'])),
                                ('packet_crc_error_count_high', (YLeaf(YType.uint64, 'packet-crc-error-count-high'), ['int'])),
                                ('short_packet_error_count_high', (YLeaf(YType.uint64, 'short-packet-error-count-high'), ['int'])),
                                ('output_buffer_queued_packet_count_high', (YLeaf(YType.uint64, 'output-buffer-queued-packet-count-high'), ['int'])),
                                ('egress_packet_count_since_last_read_high', (YLeaf(YType.uint64, 'egress-packet-count-since-last-read-high'), ['int'])),
                                ('egress_channel_utilization_count_high', (YLeaf(YType.uint64, 'egress-channel-utilization-count-high'), ['int'])),
                                ('output_buffer_back_pressure_count_high', (YLeaf(YType.uint64, 'output-buffer-back-pressure-count-high'), ['int'])),
                                ('output_buffer_correctable_ecc_error_count_high', (YLeaf(YType.uint64, 'output-buffer-correctable-ecc-error-count-high'), ['int'])),
                                ('output_buffer_uncorrectable_ecc_error_count_high', (YLeaf(YType.uint64, 'output-buffer-uncorrectable-ecc-error-count-high'), ['int'])),
                                ('fpoedb_correctable_ecc_error_count_high', (YLeaf(YType.uint64, 'fpoedb-correctable-ecc-error-count-high'), ['int'])),
                                ('fpoedb_uncorrectable_ecc_error_count_high', (YLeaf(YType.uint64, 'fpoedb-uncorrectable-ecc-error-count-high'), ['int'])),
                                ('input_buffer_queued_packet_count_low', (YLeaf(YType.uint64, 'input-buffer-queued-packet-count-low'), ['int'])),
                                ('ingress_packet_count_since_last_read_low', (YLeaf(YType.uint64, 'ingress-packet-count-since-last-read-low'), ['int'])),
                                ('ingress_channel_utilization_count_low', (YLeaf(YType.uint64, 'ingress-channel-utilization-count-low'), ['int'])),
                                ('input_buffer_back_pressure_count_low', (YLeaf(YType.uint64, 'input-buffer-back-pressure-count-low'), ['int'])),
                                ('xbar_timeout_drop_count_low', (YLeaf(YType.uint64, 'xbar-timeout-drop-count-low'), ['int'])),
                                ('holdrop_count_low', (YLeaf(YType.uint64, 'holdrop-count-low'), ['int'])),
                                ('null_fpoe_drop_count_low', (YLeaf(YType.uint64, 'null-fpoe-drop-count-low'), ['int'])),
                                ('diagnostic_packet_count_low', (YLeaf(YType.uint64, 'diagnostic-packet-count-low'), ['int'])),
                                ('input_buffer_correctable_ecc_error_count_low', (YLeaf(YType.uint64, 'input-buffer-correctable-ecc-error-count-low'), ['int'])),
                                ('input_buffer_uncorrectable_ecc_error_count_low', (YLeaf(YType.uint64, 'input-buffer-uncorrectable-ecc-error-count-low'), ['int'])),
                                ('header_crc_error_count_low', (YLeaf(YType.uint64, 'header-crc-error-count-low'), ['int'])),
                                ('short_input_header_error_count_low', (YLeaf(YType.uint64, 'short-input-header-error-count-low'), ['int'])),
                                ('packet_crc_error_count_low', (YLeaf(YType.uint64, 'packet-crc-error-count-low'), ['int'])),
                                ('short_packet_error_count_low', (YLeaf(YType.uint64, 'short-packet-error-count-low'), ['int'])),
                                ('output_buffer_queued_packet_count_low', (YLeaf(YType.uint64, 'output-buffer-queued-packet-count-low'), ['int'])),
                                ('egress_packet_count_since_last_read_low', (YLeaf(YType.uint64, 'egress-packet-count-since-last-read-low'), ['int'])),
                                ('egress_channel_utilization_count_low', (YLeaf(YType.uint64, 'egress-channel-utilization-count-low'), ['int'])),
                                ('output_buffer_back_pressure_count_low', (YLeaf(YType.uint64, 'output-buffer-back-pressure-count-low'), ['int'])),
                                ('output_buffer_correctable_ecc_error_count_low', (YLeaf(YType.uint64, 'output-buffer-correctable-ecc-error-count-low'), ['int'])),
                                ('output_buffer_uncorrectable_ecc_error_count_low', (YLeaf(YType.uint64, 'output-buffer-uncorrectable-ecc-error-count-low'), ['int'])),
                                ('fpoedb_correctable_ecc_error_count_low', (YLeaf(YType.uint64, 'fpoedb-correctable-ecc-error-count-low'), ['int'])),
                                ('fpoedb_uncorrectable_ecc_error_count_low', (YLeaf(YType.uint64, 'fpoedb-uncorrectable-ecc-error-count-low'), ['int'])),
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
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.PktStats.PktStat, ['asic_id', 'port', u'internal_error_count', u'input_buffer_queued_packet_count_high', u'ingress_packet_count_since_last_read_high', u'ingress_channel_utilization_count_high', u'input_buffer_back_pressure_count_high', u'xbar_timeout_drop_count_high', u'holdrop_count_high', u'null_fpoe_drop_count_high', u'diagnostic_packet_count_high', u'input_buffer_correctable_ecc_error_count_high', u'input_buffer_uncorrectable_ecc_error_count_high', u'header_crc_error_count_high', u'short_input_header_error_count_high', u'packet_crc_error_count_high', u'short_packet_error_count_high', u'output_buffer_queued_packet_count_high', u'egress_packet_count_since_last_read_high', u'egress_channel_utilization_count_high', u'output_buffer_back_pressure_count_high', u'output_buffer_correctable_ecc_error_count_high', u'output_buffer_uncorrectable_ecc_error_count_high', u'fpoedb_correctable_ecc_error_count_high', u'fpoedb_uncorrectable_ecc_error_count_high', u'input_buffer_queued_packet_count_low', u'ingress_packet_count_since_last_read_low', u'ingress_channel_utilization_count_low', u'input_buffer_back_pressure_count_low', u'xbar_timeout_drop_count_low', u'holdrop_count_low', u'null_fpoe_drop_count_low', u'diagnostic_packet_count_low', u'input_buffer_correctable_ecc_error_count_low', u'input_buffer_uncorrectable_ecc_error_count_low', u'header_crc_error_count_low', u'short_input_header_error_count_low', u'packet_crc_error_count_low', u'short_packet_error_count_low', u'output_buffer_queued_packet_count_low', u'egress_packet_count_since_last_read_low', u'egress_channel_utilization_count_low', u'output_buffer_back_pressure_count_low', u'output_buffer_correctable_ecc_error_count_low', u'output_buffer_uncorrectable_ecc_error_count_low', u'fpoedb_correctable_ecc_error_count_low', u'fpoedb_uncorrectable_ecc_error_count_low'], name, value)




                class Sm15Stats(Entity):
                    """
                    Table of packet stats for SM15
                    
                    .. attribute:: sm15_stat
                    
                    	Stats information for a particular asic type and port
                    	**type**\: list of  		 :py:class:`Sm15Stat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat>`
                    
                    	**config**\: False
                    
                    

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
                        self._child_classes = OrderedDict([("sm15-stat", ("sm15_stat", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat))])
                        self._leafs = OrderedDict()

                        self.sm15_stat = YList(self)
                        self._segment_path = lambda: "sm15-stats"
                        self._is_frozen = True

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
                        
                        	**config**\: False
                        
                        .. attribute:: port
                        
                        	Port
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        	**config**\: False
                        
                        .. attribute:: ua0_stats
                        
                        	ua0 stats
                        	**type**\:  :py:class:`Ua0Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua0Stats>`
                        
                        	**config**\: False
                        
                        .. attribute:: ua1_stats
                        
                        	ua1 stats
                        	**type**\:  :py:class:`Ua1Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua1Stats>`
                        
                        	**config**\: False
                        
                        .. attribute:: ua2_stats
                        
                        	ua2 stats
                        	**type**\:  :py:class:`Ua2Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua2Stats>`
                        
                        	**config**\: False
                        
                        .. attribute:: ma_stats
                        
                        	ma stats
                        	**type**\:  :py:class:`MaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.MaStats>`
                        
                        	**config**\: False
                        
                        .. attribute:: ca_stats
                        
                        	ca stats
                        	**type**\:  :py:class:`CaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.CaStats>`
                        
                        	**config**\: False
                        
                        .. attribute:: pi_stats
                        
                        	pi stats
                        	**type**\:  :py:class:`PiStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiStats>`
                        
                        	**config**\: False
                        
                        .. attribute:: pe_stats
                        
                        	pe stats
                        	**type**\:  :py:class:`PeStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeStats>`
                        
                        	**config**\: False
                        
                        .. attribute:: pi_uc_stats
                        
                        	pi uc stats
                        	**type**\:  :py:class:`PiUcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiUcStats>`
                        
                        	**config**\: False
                        
                        .. attribute:: pi_mc_stats
                        
                        	pi mc stats
                        	**type**\:  :py:class:`PiMcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiMcStats>`
                        
                        	**config**\: False
                        
                        .. attribute:: pi_cc_stats
                        
                        	pi cc stats
                        	**type**\:  :py:class:`PiCcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiCcStats>`
                        
                        	**config**\: False
                        
                        .. attribute:: pe_uc_stats
                        
                        	pe uc stats
                        	**type**\:  :py:class:`PeUcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeUcStats>`
                        
                        	**config**\: False
                        
                        .. attribute:: pe_mc_stats
                        
                        	pe mc stats
                        	**type**\:  :py:class:`PeMcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeMcStats>`
                        
                        	**config**\: False
                        
                        .. attribute:: pe_cc_stats
                        
                        	pe cc stats
                        	**type**\:  :py:class:`PeCcStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_xbar_oper.CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeCcStats>`
                        
                        	**config**\: False
                        
                        .. attribute:: internal_err_cnt
                        
                        	internal err cnt
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

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
                            self._child_classes = OrderedDict([("ua0-stats", ("ua0_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua0Stats)), ("ua1-stats", ("ua1_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua1Stats)), ("ua2-stats", ("ua2_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua2Stats)), ("ma-stats", ("ma_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.MaStats)), ("ca-stats", ("ca_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.CaStats)), ("pi-stats", ("pi_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiStats)), ("pe-stats", ("pe_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeStats)), ("pi-uc-stats", ("pi_uc_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiUcStats)), ("pi-mc-stats", ("pi_mc_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiMcStats)), ("pi-cc-stats", ("pi_cc_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiCcStats)), ("pe-uc-stats", ("pe_uc_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeUcStats)), ("pe-mc-stats", ("pe_mc_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeMcStats)), ("pe-cc-stats", ("pe_cc_stats", CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeCcStats))])
                            self._leafs = OrderedDict([
                                ('asic_id', (YLeaf(YType.str, 'asic-id'), ['str'])),
                                ('port', (YLeaf(YType.str, 'port'), ['str'])),
                                ('internal_err_cnt', (YLeaf(YType.uint64, 'internal-err-cnt'), ['int'])),
                            ])
                            self.asic_id = None
                            self.port = None
                            self.internal_err_cnt = None

                            self.ua0_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua0Stats()
                            self.ua0_stats.parent = self
                            self._children_name_map["ua0_stats"] = "ua0-stats"

                            self.ua1_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua1Stats()
                            self.ua1_stats.parent = self
                            self._children_name_map["ua1_stats"] = "ua1-stats"

                            self.ua2_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua2Stats()
                            self.ua2_stats.parent = self
                            self._children_name_map["ua2_stats"] = "ua2-stats"

                            self.ma_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.MaStats()
                            self.ma_stats.parent = self
                            self._children_name_map["ma_stats"] = "ma-stats"

                            self.ca_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.CaStats()
                            self.ca_stats.parent = self
                            self._children_name_map["ca_stats"] = "ca-stats"

                            self.pi_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiStats()
                            self.pi_stats.parent = self
                            self._children_name_map["pi_stats"] = "pi-stats"

                            self.pe_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeStats()
                            self.pe_stats.parent = self
                            self._children_name_map["pe_stats"] = "pe-stats"

                            self.pi_uc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiUcStats()
                            self.pi_uc_stats.parent = self
                            self._children_name_map["pi_uc_stats"] = "pi-uc-stats"

                            self.pi_mc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiMcStats()
                            self.pi_mc_stats.parent = self
                            self._children_name_map["pi_mc_stats"] = "pi-mc-stats"

                            self.pi_cc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiCcStats()
                            self.pi_cc_stats.parent = self
                            self._children_name_map["pi_cc_stats"] = "pi-cc-stats"

                            self.pe_uc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeUcStats()
                            self.pe_uc_stats.parent = self
                            self._children_name_map["pe_uc_stats"] = "pe-uc-stats"

                            self.pe_mc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeMcStats()
                            self.pe_mc_stats.parent = self
                            self._children_name_map["pe_mc_stats"] = "pe-mc-stats"

                            self.pe_cc_stats = CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeCcStats()
                            self.pe_cc_stats.parent = self
                            self._children_name_map["pe_cc_stats"] = "pe-cc-stats"
                            self._segment_path = lambda: "sm15-stat"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat, ['asic_id', 'port', u'internal_err_cnt'], name, value)


                        class Ua0Stats(Entity):
                            """
                            ua0 stats
                            
                            .. attribute:: dest_drop_pkt_cnt
                            
                            	DEST DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: src_dest_pkt_cnt
                            
                            	SRC DEST PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: dest_src_pkt_cnt
                            
                            	DEST SRC PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rcv_pkt_cnt
                            
                            	RCV PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: tx_pkt_cnt
                            
                            	TX PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rx_drop_pkt_cnt
                            
                            	RX DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rx_fabric_to_cnt
                            
                            	RX FABRIC TO CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ack_wait_cnt
                            
                            	ACK WAIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('dest_drop_pkt_cnt', (YLeaf(YType.uint64, 'dest-drop-pkt-cnt'), ['int'])),
                                    ('src_dest_pkt_cnt', (YLeaf(YType.uint64, 'src-dest-pkt-cnt'), ['int'])),
                                    ('dest_src_pkt_cnt', (YLeaf(YType.uint64, 'dest-src-pkt-cnt'), ['int'])),
                                    ('rcv_pkt_cnt', (YLeaf(YType.uint64, 'rcv-pkt-cnt'), ['int'])),
                                    ('tx_pkt_cnt', (YLeaf(YType.uint64, 'tx-pkt-cnt'), ['int'])),
                                    ('rx_drop_pkt_cnt', (YLeaf(YType.uint64, 'rx-drop-pkt-cnt'), ['int'])),
                                    ('rx_fabric_to_cnt', (YLeaf(YType.uint64, 'rx-fabric-to-cnt'), ['int'])),
                                    ('ack_wait_cnt', (YLeaf(YType.uint64, 'ack-wait-cnt'), ['int'])),
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
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua0Stats, [u'dest_drop_pkt_cnt', u'src_dest_pkt_cnt', u'dest_src_pkt_cnt', u'rcv_pkt_cnt', u'tx_pkt_cnt', u'rx_drop_pkt_cnt', u'rx_fabric_to_cnt', u'ack_wait_cnt'], name, value)



                        class Ua1Stats(Entity):
                            """
                            ua1 stats
                            
                            .. attribute:: dest_drop_pkt_cnt
                            
                            	DEST DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: src_dest_pkt_cnt
                            
                            	SRC DEST PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: dest_src_pkt_cnt
                            
                            	DEST SRC PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rcv_pkt_cnt
                            
                            	RCV PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: tx_pkt_cnt
                            
                            	TX PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rx_drop_pkt_cnt
                            
                            	RX DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rx_fabric_to_cnt
                            
                            	RX FABRIC TO CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ack_wait_cnt
                            
                            	ACK WAIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('dest_drop_pkt_cnt', (YLeaf(YType.uint64, 'dest-drop-pkt-cnt'), ['int'])),
                                    ('src_dest_pkt_cnt', (YLeaf(YType.uint64, 'src-dest-pkt-cnt'), ['int'])),
                                    ('dest_src_pkt_cnt', (YLeaf(YType.uint64, 'dest-src-pkt-cnt'), ['int'])),
                                    ('rcv_pkt_cnt', (YLeaf(YType.uint64, 'rcv-pkt-cnt'), ['int'])),
                                    ('tx_pkt_cnt', (YLeaf(YType.uint64, 'tx-pkt-cnt'), ['int'])),
                                    ('rx_drop_pkt_cnt', (YLeaf(YType.uint64, 'rx-drop-pkt-cnt'), ['int'])),
                                    ('rx_fabric_to_cnt', (YLeaf(YType.uint64, 'rx-fabric-to-cnt'), ['int'])),
                                    ('ack_wait_cnt', (YLeaf(YType.uint64, 'ack-wait-cnt'), ['int'])),
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
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua1Stats, [u'dest_drop_pkt_cnt', u'src_dest_pkt_cnt', u'dest_src_pkt_cnt', u'rcv_pkt_cnt', u'tx_pkt_cnt', u'rx_drop_pkt_cnt', u'rx_fabric_to_cnt', u'ack_wait_cnt'], name, value)



                        class Ua2Stats(Entity):
                            """
                            ua2 stats
                            
                            .. attribute:: dest_drop_pkt_cnt
                            
                            	DEST DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: src_dest_pkt_cnt
                            
                            	SRC DEST PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: dest_src_pkt_cnt
                            
                            	DEST SRC PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rcv_pkt_cnt
                            
                            	RCV PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: tx_pkt_cnt
                            
                            	TX PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rx_drop_pkt_cnt
                            
                            	RX DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rx_fabric_to_cnt
                            
                            	RX FABRIC TO CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ack_wait_cnt
                            
                            	ACK WAIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('dest_drop_pkt_cnt', (YLeaf(YType.uint64, 'dest-drop-pkt-cnt'), ['int'])),
                                    ('src_dest_pkt_cnt', (YLeaf(YType.uint64, 'src-dest-pkt-cnt'), ['int'])),
                                    ('dest_src_pkt_cnt', (YLeaf(YType.uint64, 'dest-src-pkt-cnt'), ['int'])),
                                    ('rcv_pkt_cnt', (YLeaf(YType.uint64, 'rcv-pkt-cnt'), ['int'])),
                                    ('tx_pkt_cnt', (YLeaf(YType.uint64, 'tx-pkt-cnt'), ['int'])),
                                    ('rx_drop_pkt_cnt', (YLeaf(YType.uint64, 'rx-drop-pkt-cnt'), ['int'])),
                                    ('rx_fabric_to_cnt', (YLeaf(YType.uint64, 'rx-fabric-to-cnt'), ['int'])),
                                    ('ack_wait_cnt', (YLeaf(YType.uint64, 'ack-wait-cnt'), ['int'])),
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
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.Ua2Stats, [u'dest_drop_pkt_cnt', u'src_dest_pkt_cnt', u'dest_src_pkt_cnt', u'rcv_pkt_cnt', u'tx_pkt_cnt', u'rx_drop_pkt_cnt', u'rx_fabric_to_cnt', u'ack_wait_cnt'], name, value)



                        class MaStats(Entity):
                            """
                            ma stats
                            
                            .. attribute:: dest_drop_pkt_cnt
                            
                            	DEST DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: src_dest_pkt_cnt
                            
                            	SRC DEST PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: dest_src_pkt_cnt
                            
                            	DEST SRC PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rcv_pkt_cnt
                            
                            	RCV PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: tx_pkt_cnt
                            
                            	TX PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rx_drop_pkt_cnt
                            
                            	RX DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rx_re_transmit_cnt
                            
                            	RX RETRANSMIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rx_fabric_to_cnt
                            
                            	RX FABRIC TO CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rx_hol_to_cnt
                            
                            	RX HOL TO CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('dest_drop_pkt_cnt', (YLeaf(YType.uint64, 'dest-drop-pkt-cnt'), ['int'])),
                                    ('src_dest_pkt_cnt', (YLeaf(YType.uint64, 'src-dest-pkt-cnt'), ['int'])),
                                    ('dest_src_pkt_cnt', (YLeaf(YType.uint64, 'dest-src-pkt-cnt'), ['int'])),
                                    ('rcv_pkt_cnt', (YLeaf(YType.uint64, 'rcv-pkt-cnt'), ['int'])),
                                    ('tx_pkt_cnt', (YLeaf(YType.uint64, 'tx-pkt-cnt'), ['int'])),
                                    ('rx_drop_pkt_cnt', (YLeaf(YType.uint64, 'rx-drop-pkt-cnt'), ['int'])),
                                    ('rx_re_transmit_cnt', (YLeaf(YType.uint64, 'rx-re-transmit-cnt'), ['int'])),
                                    ('rx_fabric_to_cnt', (YLeaf(YType.uint64, 'rx-fabric-to-cnt'), ['int'])),
                                    ('rx_hol_to_cnt', (YLeaf(YType.uint64, 'rx-hol-to-cnt'), ['int'])),
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
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.MaStats, [u'dest_drop_pkt_cnt', u'src_dest_pkt_cnt', u'dest_src_pkt_cnt', u'rcv_pkt_cnt', u'tx_pkt_cnt', u'rx_drop_pkt_cnt', u'rx_re_transmit_cnt', u'rx_fabric_to_cnt', u'rx_hol_to_cnt'], name, value)



                        class CaStats(Entity):
                            """
                            ca stats
                            
                            .. attribute:: dest_drop_pkt_cnt
                            
                            	DEST DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: src_dest_pkt_cnt
                            
                            	SRC DEST PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: dest_src_pkt_cnt
                            
                            	DEST SRC PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rcv_pkt_cnt
                            
                            	RCV PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: tx_pkt_cnt
                            
                            	TX PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rx_drop_pkt_cnt
                            
                            	RX DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('dest_drop_pkt_cnt', (YLeaf(YType.uint64, 'dest-drop-pkt-cnt'), ['int'])),
                                    ('src_dest_pkt_cnt', (YLeaf(YType.uint64, 'src-dest-pkt-cnt'), ['int'])),
                                    ('dest_src_pkt_cnt', (YLeaf(YType.uint64, 'dest-src-pkt-cnt'), ['int'])),
                                    ('rcv_pkt_cnt', (YLeaf(YType.uint64, 'rcv-pkt-cnt'), ['int'])),
                                    ('tx_pkt_cnt', (YLeaf(YType.uint64, 'tx-pkt-cnt'), ['int'])),
                                    ('rx_drop_pkt_cnt', (YLeaf(YType.uint64, 'rx-drop-pkt-cnt'), ['int'])),
                                ])
                                self.dest_drop_pkt_cnt = None
                                self.src_dest_pkt_cnt = None
                                self.dest_src_pkt_cnt = None
                                self.rcv_pkt_cnt = None
                                self.tx_pkt_cnt = None
                                self.rx_drop_pkt_cnt = None
                                self._segment_path = lambda: "ca-stats"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.CaStats, [u'dest_drop_pkt_cnt', u'src_dest_pkt_cnt', u'dest_src_pkt_cnt', u'rcv_pkt_cnt', u'tx_pkt_cnt', u'rx_drop_pkt_cnt'], name, value)



                        class PiStats(Entity):
                            """
                            pi stats
                            
                            .. attribute:: total_rate1_cnt
                            
                            	TOTAL RATE1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: total_rate2_cnt
                            
                            	TOTAL RATE2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: total_rate3_cnt
                            
                            	TOTAL RATE3 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: total_calc_rate
                            
                            	total calc rate
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('total_rate1_cnt', (YLeaf(YType.uint64, 'total-rate1-cnt'), ['int'])),
                                    ('total_rate2_cnt', (YLeaf(YType.uint64, 'total-rate2-cnt'), ['int'])),
                                    ('total_rate3_cnt', (YLeaf(YType.uint64, 'total-rate3-cnt'), ['int'])),
                                    ('total_calc_rate', (YLeaf(YType.uint64, 'total-calc-rate'), ['int'])),
                                ])
                                self.total_rate1_cnt = None
                                self.total_rate2_cnt = None
                                self.total_rate3_cnt = None
                                self.total_calc_rate = None
                                self._segment_path = lambda: "pi-stats"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiStats, [u'total_rate1_cnt', u'total_rate2_cnt', u'total_rate3_cnt', u'total_calc_rate'], name, value)



                        class PeStats(Entity):
                            """
                            pe stats
                            
                            .. attribute:: total_rate1_cnt
                            
                            	TOTAL RATE1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: total_rate2_cnt
                            
                            	TOTAL RATE2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: total_rate3_cnt
                            
                            	TOTAL RATE3 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: total_calc_rate
                            
                            	total calc rate
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: mc2uc_preempt_cnt
                            
                            	MC2UC PREEMPT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('total_rate1_cnt', (YLeaf(YType.uint64, 'total-rate1-cnt'), ['int'])),
                                    ('total_rate2_cnt', (YLeaf(YType.uint64, 'total-rate2-cnt'), ['int'])),
                                    ('total_rate3_cnt', (YLeaf(YType.uint64, 'total-rate3-cnt'), ['int'])),
                                    ('total_calc_rate', (YLeaf(YType.uint64, 'total-calc-rate'), ['int'])),
                                    ('mc2uc_preempt_cnt', (YLeaf(YType.uint64, 'mc2uc-preempt-cnt'), ['int'])),
                                ])
                                self.total_rate1_cnt = None
                                self.total_rate2_cnt = None
                                self.total_rate3_cnt = None
                                self.total_calc_rate = None
                                self.mc2uc_preempt_cnt = None
                                self._segment_path = lambda: "pe-stats"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeStats, [u'total_rate1_cnt', u'total_rate2_cnt', u'total_rate3_cnt', u'total_calc_rate', u'mc2uc_preempt_cnt'], name, value)



                        class PiUcStats(Entity):
                            """
                            pi uc stats
                            
                            .. attribute:: pkt_rcv_cnt
                            
                            	PKT RCV CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_seq_err_cnt
                            
                            	PKT SEQ ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_coming_pkt_err_cnt
                            
                            	INCOMING PKT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: min_pkt_len_err_cnt
                            
                            	MIN PKT LEN ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: max_pkt_len_err_cnt
                            
                            	MAX PKT LEN ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: line_err_drp_pkt
                            
                            	LINE ERR DRP PKT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_crc_err_cnt
                            
                            	PKT CRC ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_cfh_crc_err_cnt
                            
                            	PKT CFH CRC ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: line_s_written_in_mem0
                            
                            	LINES WRITTEN IN MEM0
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: line_s_written_in_mem1
                            
                            	LINES WRITTEN IN MEM1
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: line_s_written_in_mem2
                            
                            	LINES WRITTEN IN MEM2
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: tail_drp_pkt_cnt
                            
                            	TAIL DRP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: uc0_data_mem_ecc_1bit_err_cnt
                            
                            	UC0 DATA MEM ECC 1BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: uc1_data_mem_ecc_1bit_err_cnt
                            
                            	UC1 DATA MEM ECC 1BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: uc2_data_mem_ecc_1bit_err_cnt
                            
                            	UC2 DATA MEM ECC 1BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: uc0_data_mem_ecc_2bit_err_cnt
                            
                            	UC0 DATA MEM ECC 2BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: uc1_data_mem_ecc_2bit_err_cnt
                            
                            	UC1 DATA MEM ECC 2BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: uc2_data_mem_ecc_2bit_err_cnt
                            
                            	UC2 DATA MEM ECC 2BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: diag_pkt_cnt
                            
                            	DIAG PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_sent_to_disabled_port_cnt
                            
                            	PKT SENT TO DISABLED PORT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_null_poe_sent_ua0_cnt
                            
                            	PKT NULL POE SENT UA0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_null_poe_sent_ua1_cnt
                            
                            	PKT NULL POE SENT UA1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_null_poe_sent_ua2_cnt
                            
                            	PKT NULL POE SENT UA2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_fpoe_addr_rng_hit_cnt
                            
                            	PKT FPOE ADDR RNG HIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: fpoe_mem_ecc_1bit_err_cnt
                            
                            	FPOE MEM ECC 1BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: fpoe_mem_ecc_2bit_err_cnt
                            
                            	FPOE MEM ECC 2BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkts_sent_to_ux0_cnt
                            
                            	PKTS SENT TO UX0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkts_sent_to_ux1_cnt
                            
                            	PKTS SENT TO UX1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkts_sent_to_ux2_cnt
                            
                            	PKTS SENT TO UX2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: cpp_head_drop_pkt_cnt
                            
                            	CPP HEAD DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: tr_head_drop_pkt_cnt
                            
                            	TR HEAD DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: tr_pkt_sent_to_ux
                            
                            	TR PKT SENT TO UX
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: stop_thrsh_hit_cnt
                            
                            	STOP THRSH HIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rate_cnt
                            
                            	RATE CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: calc_rate
                            
                            	calc rate
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: crc_stomp_pkt_cnt
                            
                            	CRC STOMP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('pkt_rcv_cnt', (YLeaf(YType.uint64, 'pkt-rcv-cnt'), ['int'])),
                                    ('pkt_seq_err_cnt', (YLeaf(YType.uint64, 'pkt-seq-err-cnt'), ['int'])),
                                    ('in_coming_pkt_err_cnt', (YLeaf(YType.uint64, 'in-coming-pkt-err-cnt'), ['int'])),
                                    ('min_pkt_len_err_cnt', (YLeaf(YType.uint64, 'min-pkt-len-err-cnt'), ['int'])),
                                    ('max_pkt_len_err_cnt', (YLeaf(YType.uint64, 'max-pkt-len-err-cnt'), ['int'])),
                                    ('line_err_drp_pkt', (YLeaf(YType.uint64, 'line-err-drp-pkt'), ['int'])),
                                    ('pkt_crc_err_cnt', (YLeaf(YType.uint64, 'pkt-crc-err-cnt'), ['int'])),
                                    ('pkt_cfh_crc_err_cnt', (YLeaf(YType.uint64, 'pkt-cfh-crc-err-cnt'), ['int'])),
                                    ('line_s_written_in_mem0', (YLeaf(YType.uint64, 'line-s-written-in-mem0'), ['int'])),
                                    ('line_s_written_in_mem1', (YLeaf(YType.uint64, 'line-s-written-in-mem1'), ['int'])),
                                    ('line_s_written_in_mem2', (YLeaf(YType.uint64, 'line-s-written-in-mem2'), ['int'])),
                                    ('tail_drp_pkt_cnt', (YLeaf(YType.uint64, 'tail-drp-pkt-cnt'), ['int'])),
                                    ('uc0_data_mem_ecc_1bit_err_cnt', (YLeaf(YType.uint64, 'uc0-data-mem-ecc-1bit-err-cnt'), ['int'])),
                                    ('uc1_data_mem_ecc_1bit_err_cnt', (YLeaf(YType.uint64, 'uc1-data-mem-ecc-1bit-err-cnt'), ['int'])),
                                    ('uc2_data_mem_ecc_1bit_err_cnt', (YLeaf(YType.uint64, 'uc2-data-mem-ecc-1bit-err-cnt'), ['int'])),
                                    ('uc0_data_mem_ecc_2bit_err_cnt', (YLeaf(YType.uint64, 'uc0-data-mem-ecc-2bit-err-cnt'), ['int'])),
                                    ('uc1_data_mem_ecc_2bit_err_cnt', (YLeaf(YType.uint64, 'uc1-data-mem-ecc-2bit-err-cnt'), ['int'])),
                                    ('uc2_data_mem_ecc_2bit_err_cnt', (YLeaf(YType.uint64, 'uc2-data-mem-ecc-2bit-err-cnt'), ['int'])),
                                    ('diag_pkt_cnt', (YLeaf(YType.uint64, 'diag-pkt-cnt'), ['int'])),
                                    ('pkt_sent_to_disabled_port_cnt', (YLeaf(YType.uint64, 'pkt-sent-to-disabled-port-cnt'), ['int'])),
                                    ('pkt_null_poe_sent_ua0_cnt', (YLeaf(YType.uint64, 'pkt-null-poe-sent-ua0-cnt'), ['int'])),
                                    ('pkt_null_poe_sent_ua1_cnt', (YLeaf(YType.uint64, 'pkt-null-poe-sent-ua1-cnt'), ['int'])),
                                    ('pkt_null_poe_sent_ua2_cnt', (YLeaf(YType.uint64, 'pkt-null-poe-sent-ua2-cnt'), ['int'])),
                                    ('pkt_fpoe_addr_rng_hit_cnt', (YLeaf(YType.uint64, 'pkt-fpoe-addr-rng-hit-cnt'), ['int'])),
                                    ('fpoe_mem_ecc_1bit_err_cnt', (YLeaf(YType.uint64, 'fpoe-mem-ecc-1bit-err-cnt'), ['int'])),
                                    ('fpoe_mem_ecc_2bit_err_cnt', (YLeaf(YType.uint64, 'fpoe-mem-ecc-2bit-err-cnt'), ['int'])),
                                    ('pkts_sent_to_ux0_cnt', (YLeaf(YType.uint64, 'pkts-sent-to-ux0-cnt'), ['int'])),
                                    ('pkts_sent_to_ux1_cnt', (YLeaf(YType.uint64, 'pkts-sent-to-ux1-cnt'), ['int'])),
                                    ('pkts_sent_to_ux2_cnt', (YLeaf(YType.uint64, 'pkts-sent-to-ux2-cnt'), ['int'])),
                                    ('cpp_head_drop_pkt_cnt', (YLeaf(YType.uint64, 'cpp-head-drop-pkt-cnt'), ['int'])),
                                    ('tr_head_drop_pkt_cnt', (YLeaf(YType.uint64, 'tr-head-drop-pkt-cnt'), ['int'])),
                                    ('tr_pkt_sent_to_ux', (YLeaf(YType.uint64, 'tr-pkt-sent-to-ux'), ['int'])),
                                    ('stop_thrsh_hit_cnt', (YLeaf(YType.uint64, 'stop-thrsh-hit-cnt'), ['int'])),
                                    ('rate_cnt', (YLeaf(YType.uint64, 'rate-cnt'), ['int'])),
                                    ('calc_rate', (YLeaf(YType.uint64, 'calc-rate'), ['int'])),
                                    ('crc_stomp_pkt_cnt', (YLeaf(YType.uint64, 'crc-stomp-pkt-cnt'), ['int'])),
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
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiUcStats, [u'pkt_rcv_cnt', u'pkt_seq_err_cnt', u'in_coming_pkt_err_cnt', u'min_pkt_len_err_cnt', u'max_pkt_len_err_cnt', u'line_err_drp_pkt', u'pkt_crc_err_cnt', u'pkt_cfh_crc_err_cnt', u'line_s_written_in_mem0', u'line_s_written_in_mem1', u'line_s_written_in_mem2', u'tail_drp_pkt_cnt', u'uc0_data_mem_ecc_1bit_err_cnt', u'uc1_data_mem_ecc_1bit_err_cnt', u'uc2_data_mem_ecc_1bit_err_cnt', u'uc0_data_mem_ecc_2bit_err_cnt', u'uc1_data_mem_ecc_2bit_err_cnt', u'uc2_data_mem_ecc_2bit_err_cnt', u'diag_pkt_cnt', u'pkt_sent_to_disabled_port_cnt', u'pkt_null_poe_sent_ua0_cnt', u'pkt_null_poe_sent_ua1_cnt', u'pkt_null_poe_sent_ua2_cnt', u'pkt_fpoe_addr_rng_hit_cnt', u'fpoe_mem_ecc_1bit_err_cnt', u'fpoe_mem_ecc_2bit_err_cnt', u'pkts_sent_to_ux0_cnt', u'pkts_sent_to_ux1_cnt', u'pkts_sent_to_ux2_cnt', u'cpp_head_drop_pkt_cnt', u'tr_head_drop_pkt_cnt', u'tr_pkt_sent_to_ux', u'stop_thrsh_hit_cnt', u'rate_cnt', u'calc_rate', u'crc_stomp_pkt_cnt'], name, value)



                        class PiMcStats(Entity):
                            """
                            pi mc stats
                            
                            .. attribute:: pkt_rcv_cnt
                            
                            	PKT RCV CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_seq_err_cnt
                            
                            	PKT SEQ ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_coming_pkt_err_cnt
                            
                            	INCOMING PKT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: min_pkt_len_err_cnt
                            
                            	MIN PKT LEN ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: max_pkt_len_err_cnt
                            
                            	MAX PKT LEN ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: line_err_drp_pkt
                            
                            	LINE ERR DRP PKT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_crc_err_cnt
                            
                            	PKT CRC ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_cfh_crc_err_cnt
                            
                            	PKT CFH CRC ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: line_s_written_in_mem
                            
                            	LINES WRITTEN IN MEM
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: tail_drp_pkt_cnt
                            
                            	TAIL DRP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: data_mem0_ecc_1bit_err_cnt
                            
                            	DATA MEM0 ECC 1BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: data_mem1_ecc_1bit_err_cnt
                            
                            	DATA MEM1 ECC 1BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: data_mem2_ecc_1bit_err_cnt
                            
                            	DATA MEM2 ECC 1BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: data_mem0_ecc_2bit_err_cnt
                            
                            	DATA MEM0 ECC 2BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: data_mem1_ecc_2bit_err_cnt
                            
                            	DATA MEM1 ECC 2BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: data_mem2_ecc_2bit_err_cnt
                            
                            	DATA MEM2 ECC 2BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: diag_pkt_cnt
                            
                            	DIAG PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_sent_to_disabled_port
                            
                            	PKT SENT TO DISABLED PORT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_fpoe_match_hit_cnt
                            
                            	PKT FPOE MATCH HIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_null_poe_sent_cnt
                            
                            	PKT NULL POE SENT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_fpoe_addr_rng_hit_cnt
                            
                            	PKT FPOE ADDR RNG HIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: di_hdr_len_err_pkt_cnt
                            
                            	DI HDR LEN ERR PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: di_err_pkt_cnt
                            
                            	DI ERR PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: fpoe_mem_ecc_1bit_err_cnt
                            
                            	FPOE MEM ECC 1BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: fpoe_mem_ecc_2bit_err_cnt
                            
                            	FPOE MEM ECC 2BIT ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkts_sent_to_mx_cnt
                            
                            	PKTS SENT TO MX CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: cpp_head_drop_pkt_from_ma_cnt
                            
                            	CPP HEAD DROP PKT FROM MA CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: tr_head_drop_pkt_from_ma_cnt
                            
                            	TR HEAD DROP PKT FROM MA CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: tr_pkt_sent_to_mx
                            
                            	TR PKT SENT TO MX
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: stop_thrsh_hit_cnt
                            
                            	STOP THRSH HIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rate_cnt
                            
                            	RATE CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: calc_rate
                            
                            	calc rate
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: crc_stomp_pkt_cnt
                            
                            	CRC STOMP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('pkt_rcv_cnt', (YLeaf(YType.uint64, 'pkt-rcv-cnt'), ['int'])),
                                    ('pkt_seq_err_cnt', (YLeaf(YType.uint64, 'pkt-seq-err-cnt'), ['int'])),
                                    ('in_coming_pkt_err_cnt', (YLeaf(YType.uint64, 'in-coming-pkt-err-cnt'), ['int'])),
                                    ('min_pkt_len_err_cnt', (YLeaf(YType.uint64, 'min-pkt-len-err-cnt'), ['int'])),
                                    ('max_pkt_len_err_cnt', (YLeaf(YType.uint64, 'max-pkt-len-err-cnt'), ['int'])),
                                    ('line_err_drp_pkt', (YLeaf(YType.uint64, 'line-err-drp-pkt'), ['int'])),
                                    ('pkt_crc_err_cnt', (YLeaf(YType.uint64, 'pkt-crc-err-cnt'), ['int'])),
                                    ('pkt_cfh_crc_err_cnt', (YLeaf(YType.uint64, 'pkt-cfh-crc-err-cnt'), ['int'])),
                                    ('line_s_written_in_mem', (YLeaf(YType.uint64, 'line-s-written-in-mem'), ['int'])),
                                    ('tail_drp_pkt_cnt', (YLeaf(YType.uint64, 'tail-drp-pkt-cnt'), ['int'])),
                                    ('data_mem0_ecc_1bit_err_cnt', (YLeaf(YType.uint64, 'data-mem0-ecc-1bit-err-cnt'), ['int'])),
                                    ('data_mem1_ecc_1bit_err_cnt', (YLeaf(YType.uint64, 'data-mem1-ecc-1bit-err-cnt'), ['int'])),
                                    ('data_mem2_ecc_1bit_err_cnt', (YLeaf(YType.uint64, 'data-mem2-ecc-1bit-err-cnt'), ['int'])),
                                    ('data_mem0_ecc_2bit_err_cnt', (YLeaf(YType.uint64, 'data-mem0-ecc-2bit-err-cnt'), ['int'])),
                                    ('data_mem1_ecc_2bit_err_cnt', (YLeaf(YType.uint64, 'data-mem1-ecc-2bit-err-cnt'), ['int'])),
                                    ('data_mem2_ecc_2bit_err_cnt', (YLeaf(YType.uint64, 'data-mem2-ecc-2bit-err-cnt'), ['int'])),
                                    ('diag_pkt_cnt', (YLeaf(YType.uint64, 'diag-pkt-cnt'), ['int'])),
                                    ('pkt_sent_to_disabled_port', (YLeaf(YType.uint64, 'pkt-sent-to-disabled-port'), ['int'])),
                                    ('pkt_fpoe_match_hit_cnt', (YLeaf(YType.uint64, 'pkt-fpoe-match-hit-cnt'), ['int'])),
                                    ('pkt_null_poe_sent_cnt', (YLeaf(YType.uint64, 'pkt-null-poe-sent-cnt'), ['int'])),
                                    ('pkt_fpoe_addr_rng_hit_cnt', (YLeaf(YType.uint64, 'pkt-fpoe-addr-rng-hit-cnt'), ['int'])),
                                    ('di_hdr_len_err_pkt_cnt', (YLeaf(YType.uint64, 'di-hdr-len-err-pkt-cnt'), ['int'])),
                                    ('di_err_pkt_cnt', (YLeaf(YType.uint64, 'di-err-pkt-cnt'), ['int'])),
                                    ('fpoe_mem_ecc_1bit_err_cnt', (YLeaf(YType.uint64, 'fpoe-mem-ecc-1bit-err-cnt'), ['int'])),
                                    ('fpoe_mem_ecc_2bit_err_cnt', (YLeaf(YType.uint64, 'fpoe-mem-ecc-2bit-err-cnt'), ['int'])),
                                    ('pkts_sent_to_mx_cnt', (YLeaf(YType.uint64, 'pkts-sent-to-mx-cnt'), ['int'])),
                                    ('cpp_head_drop_pkt_from_ma_cnt', (YLeaf(YType.uint64, 'cpp-head-drop-pkt-from-ma-cnt'), ['int'])),
                                    ('tr_head_drop_pkt_from_ma_cnt', (YLeaf(YType.uint64, 'tr-head-drop-pkt-from-ma-cnt'), ['int'])),
                                    ('tr_pkt_sent_to_mx', (YLeaf(YType.uint64, 'tr-pkt-sent-to-mx'), ['int'])),
                                    ('stop_thrsh_hit_cnt', (YLeaf(YType.uint64, 'stop-thrsh-hit-cnt'), ['int'])),
                                    ('rate_cnt', (YLeaf(YType.uint64, 'rate-cnt'), ['int'])),
                                    ('calc_rate', (YLeaf(YType.uint64, 'calc-rate'), ['int'])),
                                    ('crc_stomp_pkt_cnt', (YLeaf(YType.uint64, 'crc-stomp-pkt-cnt'), ['int'])),
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
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiMcStats, [u'pkt_rcv_cnt', u'pkt_seq_err_cnt', u'in_coming_pkt_err_cnt', u'min_pkt_len_err_cnt', u'max_pkt_len_err_cnt', u'line_err_drp_pkt', u'pkt_crc_err_cnt', u'pkt_cfh_crc_err_cnt', u'line_s_written_in_mem', u'tail_drp_pkt_cnt', u'data_mem0_ecc_1bit_err_cnt', u'data_mem1_ecc_1bit_err_cnt', u'data_mem2_ecc_1bit_err_cnt', u'data_mem0_ecc_2bit_err_cnt', u'data_mem1_ecc_2bit_err_cnt', u'data_mem2_ecc_2bit_err_cnt', u'diag_pkt_cnt', u'pkt_sent_to_disabled_port', u'pkt_fpoe_match_hit_cnt', u'pkt_null_poe_sent_cnt', u'pkt_fpoe_addr_rng_hit_cnt', u'di_hdr_len_err_pkt_cnt', u'di_err_pkt_cnt', u'fpoe_mem_ecc_1bit_err_cnt', u'fpoe_mem_ecc_2bit_err_cnt', u'pkts_sent_to_mx_cnt', u'cpp_head_drop_pkt_from_ma_cnt', u'tr_head_drop_pkt_from_ma_cnt', u'tr_pkt_sent_to_mx', u'stop_thrsh_hit_cnt', u'rate_cnt', u'calc_rate', u'crc_stomp_pkt_cnt'], name, value)



                        class PiCcStats(Entity):
                            """
                            pi cc stats
                            
                            .. attribute:: in0_ecc_serr_cnt
                            
                            	IN0 ECC SERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in0_ecc_derr_cnt
                            
                            	IN0 ECC DERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in1_ecc_serr_cnt
                            
                            	IN1 ECC SERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in1_ecc_derr_cnt
                            
                            	IN1 ECC DERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: data_mem_ecc_serr_cnt
                            
                            	DATA MEM ECC SERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: data_mem_ecc_derr_cnt
                            
                            	DATA MEM ECC DERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: data_mem_ovf0_cnt
                            
                            	DATA MEM OVF0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: data_mem_ovf1_cnt
                            
                            	DATA MEM OVF1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: fpoe_mem_ecc_serr_cnt
                            
                            	FPOE MEM ECC SERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: fpoe_mem_ecc_derr_cnt
                            
                            	FPOE MEM ECC DERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: null_poe_cnt
                            
                            	NULL POE CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: shut_ack_cnt
                            
                            	SHUT ACK CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in0_fnc_err_cnt
                            
                            	IN0 FNC ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in1_fnc_err_cnt
                            
                            	IN1 FNC ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in0_drop_cnt
                            
                            	IN0 DROP CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in1_drop_cnt
                            
                            	IN1 DROP CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in0_cong_cnt
                            
                            	IN0 CONG CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in1_cong_cnt
                            
                            	IN1 CONG CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in0_shut_cnt
                            
                            	IN0 SHUT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in1_shut_cnt
                            
                            	IN1 SHUT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: tail_drop_msg_cnt
                            
                            	TAIL DROP MSG CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in0_pkt_cnt
                            
                            	IN0 PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in1_pkt_cnt
                            
                            	IN1 PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: dmem_rd_cnt
                            
                            	DMEM RD CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_dmem0_cnt
                            
                            	IN DMEM0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_dmem1_cnt
                            
                            	IN DMEM1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: out_pkt_cnt
                            
                            	OUT PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: stop_thrsh_hit_cnt
                            
                            	STOP THRSH HIT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rate_cnt
                            
                            	RATE CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: calc_rate
                            
                            	calc rate
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('in0_ecc_serr_cnt', (YLeaf(YType.uint64, 'in0-ecc-serr-cnt'), ['int'])),
                                    ('in0_ecc_derr_cnt', (YLeaf(YType.uint64, 'in0-ecc-derr-cnt'), ['int'])),
                                    ('in1_ecc_serr_cnt', (YLeaf(YType.uint64, 'in1-ecc-serr-cnt'), ['int'])),
                                    ('in1_ecc_derr_cnt', (YLeaf(YType.uint64, 'in1-ecc-derr-cnt'), ['int'])),
                                    ('data_mem_ecc_serr_cnt', (YLeaf(YType.uint64, 'data-mem-ecc-serr-cnt'), ['int'])),
                                    ('data_mem_ecc_derr_cnt', (YLeaf(YType.uint64, 'data-mem-ecc-derr-cnt'), ['int'])),
                                    ('data_mem_ovf0_cnt', (YLeaf(YType.uint64, 'data-mem-ovf0-cnt'), ['int'])),
                                    ('data_mem_ovf1_cnt', (YLeaf(YType.uint64, 'data-mem-ovf1-cnt'), ['int'])),
                                    ('fpoe_mem_ecc_serr_cnt', (YLeaf(YType.uint64, 'fpoe-mem-ecc-serr-cnt'), ['int'])),
                                    ('fpoe_mem_ecc_derr_cnt', (YLeaf(YType.uint64, 'fpoe-mem-ecc-derr-cnt'), ['int'])),
                                    ('null_poe_cnt', (YLeaf(YType.uint64, 'null-poe-cnt'), ['int'])),
                                    ('shut_ack_cnt', (YLeaf(YType.uint64, 'shut-ack-cnt'), ['int'])),
                                    ('in0_fnc_err_cnt', (YLeaf(YType.uint64, 'in0-fnc-err-cnt'), ['int'])),
                                    ('in1_fnc_err_cnt', (YLeaf(YType.uint64, 'in1-fnc-err-cnt'), ['int'])),
                                    ('in0_drop_cnt', (YLeaf(YType.uint64, 'in0-drop-cnt'), ['int'])),
                                    ('in1_drop_cnt', (YLeaf(YType.uint64, 'in1-drop-cnt'), ['int'])),
                                    ('in0_cong_cnt', (YLeaf(YType.uint64, 'in0-cong-cnt'), ['int'])),
                                    ('in1_cong_cnt', (YLeaf(YType.uint64, 'in1-cong-cnt'), ['int'])),
                                    ('in0_shut_cnt', (YLeaf(YType.uint64, 'in0-shut-cnt'), ['int'])),
                                    ('in1_shut_cnt', (YLeaf(YType.uint64, 'in1-shut-cnt'), ['int'])),
                                    ('tail_drop_msg_cnt', (YLeaf(YType.uint64, 'tail-drop-msg-cnt'), ['int'])),
                                    ('in0_pkt_cnt', (YLeaf(YType.uint64, 'in0-pkt-cnt'), ['int'])),
                                    ('in1_pkt_cnt', (YLeaf(YType.uint64, 'in1-pkt-cnt'), ['int'])),
                                    ('dmem_rd_cnt', (YLeaf(YType.uint64, 'dmem-rd-cnt'), ['int'])),
                                    ('in_dmem0_cnt', (YLeaf(YType.uint64, 'in-dmem0-cnt'), ['int'])),
                                    ('in_dmem1_cnt', (YLeaf(YType.uint64, 'in-dmem1-cnt'), ['int'])),
                                    ('out_pkt_cnt', (YLeaf(YType.uint64, 'out-pkt-cnt'), ['int'])),
                                    ('stop_thrsh_hit_cnt', (YLeaf(YType.uint64, 'stop-thrsh-hit-cnt'), ['int'])),
                                    ('rate_cnt', (YLeaf(YType.uint64, 'rate-cnt'), ['int'])),
                                    ('calc_rate', (YLeaf(YType.uint64, 'calc-rate'), ['int'])),
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
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PiCcStats, [u'in0_ecc_serr_cnt', u'in0_ecc_derr_cnt', u'in1_ecc_serr_cnt', u'in1_ecc_derr_cnt', u'data_mem_ecc_serr_cnt', u'data_mem_ecc_derr_cnt', u'data_mem_ovf0_cnt', u'data_mem_ovf1_cnt', u'fpoe_mem_ecc_serr_cnt', u'fpoe_mem_ecc_derr_cnt', u'null_poe_cnt', u'shut_ack_cnt', u'in0_fnc_err_cnt', u'in1_fnc_err_cnt', u'in0_drop_cnt', u'in1_drop_cnt', u'in0_cong_cnt', u'in1_cong_cnt', u'in0_shut_cnt', u'in1_shut_cnt', u'tail_drop_msg_cnt', u'in0_pkt_cnt', u'in1_pkt_cnt', u'dmem_rd_cnt', u'in_dmem0_cnt', u'in_dmem1_cnt', u'out_pkt_cnt', u'stop_thrsh_hit_cnt', u'rate_cnt', u'calc_rate'], name, value)



                        class PeUcStats(Entity):
                            """
                            pe uc stats
                            
                            .. attribute:: in_pkt_uc0_cnt
                            
                            	IN PKT UC0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_pkt_uc1_cnt
                            
                            	IN PKT UC1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_pkt_uc2_cnt
                            
                            	IN PKT UC2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_full_line_uc0_cnt
                            
                            	IN FULL LINE UC0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_full_line_uc1_cnt
                            
                            	IN FULL LINE UC1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_full_line_uc2_cnt
                            
                            	IN FULL LINE UC2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_trunc_eop_uc0_cnt
                            
                            	PKT TRUNC EOP UC0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_trunc_eop_uc1_cnt
                            
                            	PKT TRUNC EOP UC1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_trunc_eop_uc2_cnt
                            
                            	PKT TRUNC EOP UC2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_sop_drop_uc0_cnt
                            
                            	PKT SOP DROP UC0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_sop_drop_uc1_cnt
                            
                            	PKT SOP DROP UC1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_sop_drop_uc2_cnt
                            
                            	PKT SOP DROP UC2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_ecc_err_drop_uc_cnt
                            
                            	PKT ECC ERR DROP UC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_ecc_trunc_cnt_uc_cnt
                            
                            	PKT ECC TRUNC CNT UC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ecc_1bit_err_uc0_0_cnt
                            
                            	ECC 1BIT ERR UC0 0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ecc_1bit_err_uc0_1_cnt
                            
                            	ECC 1BIT ERR UC0 1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ecc_1bit_err_uc1_0_cnt
                            
                            	ECC 1BIT ERR UC1 0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ecc_1bit_err_uc1_1_cnt
                            
                            	ECC 1BIT ERR UC1 1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ecc_1bit_err_uc2_0_cnt
                            
                            	ECC 1BIT ERR UC2 0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ecc_1bit_err_uc2_1_cnt
                            
                            	ECC 1BIT ERR UC2 1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ecc_2bit_err_uc0_0_cnt
                            
                            	ECC 2BIT ERR UC0 0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ecc_2bit_err_uc0_1_cnt
                            
                            	ECC 2BIT ERR UC0 1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ecc_2bit_err_uc1_0_cnt
                            
                            	ECC 2BIT ERR UC1 0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ecc_2bit_err_uc1_1_cnt
                            
                            	ECC 2BIT ERR UC1 1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ecc_2bit_err_uc2_0_cnt
                            
                            	ECC 2BIT ERR UC2 0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ecc_2bit_err_uc2_1_cnt
                            
                            	ECC 2BIT ERR UC2 1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: out_pkt_uc_cnt
                            
                            	OUT PKT UC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: fe_uc_sop_eop_pack_cnt
                            
                            	FE UC SOP EOP PACK CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: fc_uc_0_1_trans_cnt
                            
                            	FC UC 0 1 TRANS CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rate_cnt
                            
                            	RATE CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: calc_rate
                            
                            	calc rate
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('in_pkt_uc0_cnt', (YLeaf(YType.uint64, 'in-pkt-uc0-cnt'), ['int'])),
                                    ('in_pkt_uc1_cnt', (YLeaf(YType.uint64, 'in-pkt-uc1-cnt'), ['int'])),
                                    ('in_pkt_uc2_cnt', (YLeaf(YType.uint64, 'in-pkt-uc2-cnt'), ['int'])),
                                    ('in_full_line_uc0_cnt', (YLeaf(YType.uint64, 'in-full-line-uc0-cnt'), ['int'])),
                                    ('in_full_line_uc1_cnt', (YLeaf(YType.uint64, 'in-full-line-uc1-cnt'), ['int'])),
                                    ('in_full_line_uc2_cnt', (YLeaf(YType.uint64, 'in-full-line-uc2-cnt'), ['int'])),
                                    ('pkt_trunc_eop_uc0_cnt', (YLeaf(YType.uint64, 'pkt-trunc-eop-uc0-cnt'), ['int'])),
                                    ('pkt_trunc_eop_uc1_cnt', (YLeaf(YType.uint64, 'pkt-trunc-eop-uc1-cnt'), ['int'])),
                                    ('pkt_trunc_eop_uc2_cnt', (YLeaf(YType.uint64, 'pkt-trunc-eop-uc2-cnt'), ['int'])),
                                    ('pkt_sop_drop_uc0_cnt', (YLeaf(YType.uint64, 'pkt-sop-drop-uc0-cnt'), ['int'])),
                                    ('pkt_sop_drop_uc1_cnt', (YLeaf(YType.uint64, 'pkt-sop-drop-uc1-cnt'), ['int'])),
                                    ('pkt_sop_drop_uc2_cnt', (YLeaf(YType.uint64, 'pkt-sop-drop-uc2-cnt'), ['int'])),
                                    ('pkt_ecc_err_drop_uc_cnt', (YLeaf(YType.uint64, 'pkt-ecc-err-drop-uc-cnt'), ['int'])),
                                    ('pkt_ecc_trunc_cnt_uc_cnt', (YLeaf(YType.uint64, 'pkt-ecc-trunc-cnt-uc-cnt'), ['int'])),
                                    ('ecc_1bit_err_uc0_0_cnt', (YLeaf(YType.uint64, 'ecc-1bit-err-uc0-0-cnt'), ['int'])),
                                    ('ecc_1bit_err_uc0_1_cnt', (YLeaf(YType.uint64, 'ecc-1bit-err-uc0-1-cnt'), ['int'])),
                                    ('ecc_1bit_err_uc1_0_cnt', (YLeaf(YType.uint64, 'ecc-1bit-err-uc1-0-cnt'), ['int'])),
                                    ('ecc_1bit_err_uc1_1_cnt', (YLeaf(YType.uint64, 'ecc-1bit-err-uc1-1-cnt'), ['int'])),
                                    ('ecc_1bit_err_uc2_0_cnt', (YLeaf(YType.uint64, 'ecc-1bit-err-uc2-0-cnt'), ['int'])),
                                    ('ecc_1bit_err_uc2_1_cnt', (YLeaf(YType.uint64, 'ecc-1bit-err-uc2-1-cnt'), ['int'])),
                                    ('ecc_2bit_err_uc0_0_cnt', (YLeaf(YType.uint64, 'ecc-2bit-err-uc0-0-cnt'), ['int'])),
                                    ('ecc_2bit_err_uc0_1_cnt', (YLeaf(YType.uint64, 'ecc-2bit-err-uc0-1-cnt'), ['int'])),
                                    ('ecc_2bit_err_uc1_0_cnt', (YLeaf(YType.uint64, 'ecc-2bit-err-uc1-0-cnt'), ['int'])),
                                    ('ecc_2bit_err_uc1_1_cnt', (YLeaf(YType.uint64, 'ecc-2bit-err-uc1-1-cnt'), ['int'])),
                                    ('ecc_2bit_err_uc2_0_cnt', (YLeaf(YType.uint64, 'ecc-2bit-err-uc2-0-cnt'), ['int'])),
                                    ('ecc_2bit_err_uc2_1_cnt', (YLeaf(YType.uint64, 'ecc-2bit-err-uc2-1-cnt'), ['int'])),
                                    ('out_pkt_uc_cnt', (YLeaf(YType.uint64, 'out-pkt-uc-cnt'), ['int'])),
                                    ('fe_uc_sop_eop_pack_cnt', (YLeaf(YType.uint64, 'fe-uc-sop-eop-pack-cnt'), ['int'])),
                                    ('fc_uc_0_1_trans_cnt', (YLeaf(YType.uint64, 'fc-uc-0-1-trans-cnt'), ['int'])),
                                    ('rate_cnt', (YLeaf(YType.uint64, 'rate-cnt'), ['int'])),
                                    ('calc_rate', (YLeaf(YType.uint64, 'calc-rate'), ['int'])),
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
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeUcStats, [u'in_pkt_uc0_cnt', u'in_pkt_uc1_cnt', u'in_pkt_uc2_cnt', u'in_full_line_uc0_cnt', u'in_full_line_uc1_cnt', u'in_full_line_uc2_cnt', u'pkt_trunc_eop_uc0_cnt', u'pkt_trunc_eop_uc1_cnt', u'pkt_trunc_eop_uc2_cnt', u'pkt_sop_drop_uc0_cnt', u'pkt_sop_drop_uc1_cnt', u'pkt_sop_drop_uc2_cnt', u'pkt_ecc_err_drop_uc_cnt', u'pkt_ecc_trunc_cnt_uc_cnt', u'ecc_1bit_err_uc0_0_cnt', u'ecc_1bit_err_uc0_1_cnt', u'ecc_1bit_err_uc1_0_cnt', u'ecc_1bit_err_uc1_1_cnt', u'ecc_1bit_err_uc2_0_cnt', u'ecc_1bit_err_uc2_1_cnt', u'ecc_2bit_err_uc0_0_cnt', u'ecc_2bit_err_uc0_1_cnt', u'ecc_2bit_err_uc1_0_cnt', u'ecc_2bit_err_uc1_1_cnt', u'ecc_2bit_err_uc2_0_cnt', u'ecc_2bit_err_uc2_1_cnt', u'out_pkt_uc_cnt', u'fe_uc_sop_eop_pack_cnt', u'fc_uc_0_1_trans_cnt', u'rate_cnt', u'calc_rate'], name, value)



                        class PeMcStats(Entity):
                            """
                            pe mc stats
                            
                            .. attribute:: in_pkt_mc_cnt
                            
                            	IN PKT MC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_full_line_mc_cnt
                            
                            	IN FULL LINE MC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_trunc_eop_mc_cnt
                            
                            	PKT TRUNC EOP MC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_sop_drop_mc_cnt
                            
                            	PKT SOP DROP MC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_ecc_err_drop_mc_cnt
                            
                            	PKT ECC ERR DROP MC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: pkt_ecc_err_trunc_cnt_mc_cnt
                            
                            	PKT ECC ERR TRUNC CNT MC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ecc_1bit_err_mc0_cnt
                            
                            	ECC 1BIT ERR MC0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ecc_1bit_err_mc1_cnt
                            
                            	ECC 1BIT ERR MC1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ecc_1bit_err_mc2_cnt
                            
                            	ECC 1BIT ERR MC2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ecc_2bit_err_mc0_cnt
                            
                            	ECC 2BIT ERR MC0 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ecc_2bit_err_mc1_cnt
                            
                            	ECC 2BIT ERR MC1 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: ecc_2bit_err_mc2_cnt
                            
                            	ECC 2BIT ERR MC2 CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: out_pkt_mc_cnt
                            
                            	OUT PKT MC CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: fe_mc_sop_eop_pack_cnt
                            
                            	FE MC SOP EOP PACK CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: fc_mc_0_1_trans_cnt
                            
                            	FC MC 0 1 TRANS CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rate_cnt
                            
                            	RATE CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: calc_rate
                            
                            	calc rate
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('in_pkt_mc_cnt', (YLeaf(YType.uint64, 'in-pkt-mc-cnt'), ['int'])),
                                    ('in_full_line_mc_cnt', (YLeaf(YType.uint64, 'in-full-line-mc-cnt'), ['int'])),
                                    ('pkt_trunc_eop_mc_cnt', (YLeaf(YType.uint64, 'pkt-trunc-eop-mc-cnt'), ['int'])),
                                    ('pkt_sop_drop_mc_cnt', (YLeaf(YType.uint64, 'pkt-sop-drop-mc-cnt'), ['int'])),
                                    ('pkt_ecc_err_drop_mc_cnt', (YLeaf(YType.uint64, 'pkt-ecc-err-drop-mc-cnt'), ['int'])),
                                    ('pkt_ecc_err_trunc_cnt_mc_cnt', (YLeaf(YType.uint64, 'pkt-ecc-err-trunc-cnt-mc-cnt'), ['int'])),
                                    ('ecc_1bit_err_mc0_cnt', (YLeaf(YType.uint64, 'ecc-1bit-err-mc0-cnt'), ['int'])),
                                    ('ecc_1bit_err_mc1_cnt', (YLeaf(YType.uint64, 'ecc-1bit-err-mc1-cnt'), ['int'])),
                                    ('ecc_1bit_err_mc2_cnt', (YLeaf(YType.uint64, 'ecc-1bit-err-mc2-cnt'), ['int'])),
                                    ('ecc_2bit_err_mc0_cnt', (YLeaf(YType.uint64, 'ecc-2bit-err-mc0-cnt'), ['int'])),
                                    ('ecc_2bit_err_mc1_cnt', (YLeaf(YType.uint64, 'ecc-2bit-err-mc1-cnt'), ['int'])),
                                    ('ecc_2bit_err_mc2_cnt', (YLeaf(YType.uint64, 'ecc-2bit-err-mc2-cnt'), ['int'])),
                                    ('out_pkt_mc_cnt', (YLeaf(YType.uint64, 'out-pkt-mc-cnt'), ['int'])),
                                    ('fe_mc_sop_eop_pack_cnt', (YLeaf(YType.uint64, 'fe-mc-sop-eop-pack-cnt'), ['int'])),
                                    ('fc_mc_0_1_trans_cnt', (YLeaf(YType.uint64, 'fc-mc-0-1-trans-cnt'), ['int'])),
                                    ('rate_cnt', (YLeaf(YType.uint64, 'rate-cnt'), ['int'])),
                                    ('calc_rate', (YLeaf(YType.uint64, 'calc-rate'), ['int'])),
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
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeMcStats, [u'in_pkt_mc_cnt', u'in_full_line_mc_cnt', u'pkt_trunc_eop_mc_cnt', u'pkt_sop_drop_mc_cnt', u'pkt_ecc_err_drop_mc_cnt', u'pkt_ecc_err_trunc_cnt_mc_cnt', u'ecc_1bit_err_mc0_cnt', u'ecc_1bit_err_mc1_cnt', u'ecc_1bit_err_mc2_cnt', u'ecc_2bit_err_mc0_cnt', u'ecc_2bit_err_mc1_cnt', u'ecc_2bit_err_mc2_cnt', u'out_pkt_mc_cnt', u'fe_mc_sop_eop_pack_cnt', u'fc_mc_0_1_trans_cnt', u'rate_cnt', u'calc_rate'], name, value)



                        class PeCcStats(Entity):
                            """
                            pe cc stats
                            
                            .. attribute:: in_pkt_cnt
                            
                            	IN PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: out_path0_pkt_cnt
                            
                            	OUT PATH0 PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: out_path1_pkt_cnt
                            
                            	OUT PATH1 PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: xbar_ecc_drop_pkt_cnt
                            
                            	XBAR ECC DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: mem0_drop_pkt_cnt
                            
                            	MEM0 DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: mem1_drop_pkt_cnt
                            
                            	MEM1 DROP PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: congn_pkt_cnt
                            
                            	CONGN PKT CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: xbar_ecc_single_err_cnt
                            
                            	XBAR ECC SINGLE ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: xbar_ecc_double_err_cnt
                            
                            	XBAR ECC DOUBLE ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: mem0_ecc_single_err_cnt
                            
                            	MEM0 ECC SINGLE ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: mem0_ecc_double_err_cnt
                            
                            	MEM0 ECC DOUBLE ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: mem1_ecc_single_err_cnt
                            
                            	MEM1 ECC SINGLE ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: mem1_ecc_double_err_cnt
                            
                            	MEM1 ECC DOUBLE ERR CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: fc_cc_0_1_trans_cnt
                            
                            	FC CC 0 1 TRANS CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rate_cnt
                            
                            	RATE CNT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: calc_rate
                            
                            	calc rate
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('in_pkt_cnt', (YLeaf(YType.uint64, 'in-pkt-cnt'), ['int'])),
                                    ('out_path0_pkt_cnt', (YLeaf(YType.uint64, 'out-path0-pkt-cnt'), ['int'])),
                                    ('out_path1_pkt_cnt', (YLeaf(YType.uint64, 'out-path1-pkt-cnt'), ['int'])),
                                    ('xbar_ecc_drop_pkt_cnt', (YLeaf(YType.uint64, 'xbar-ecc-drop-pkt-cnt'), ['int'])),
                                    ('mem0_drop_pkt_cnt', (YLeaf(YType.uint64, 'mem0-drop-pkt-cnt'), ['int'])),
                                    ('mem1_drop_pkt_cnt', (YLeaf(YType.uint64, 'mem1-drop-pkt-cnt'), ['int'])),
                                    ('congn_pkt_cnt', (YLeaf(YType.uint64, 'congn-pkt-cnt'), ['int'])),
                                    ('xbar_ecc_single_err_cnt', (YLeaf(YType.uint64, 'xbar-ecc-single-err-cnt'), ['int'])),
                                    ('xbar_ecc_double_err_cnt', (YLeaf(YType.uint64, 'xbar-ecc-double-err-cnt'), ['int'])),
                                    ('mem0_ecc_single_err_cnt', (YLeaf(YType.uint64, 'mem0-ecc-single-err-cnt'), ['int'])),
                                    ('mem0_ecc_double_err_cnt', (YLeaf(YType.uint64, 'mem0-ecc-double-err-cnt'), ['int'])),
                                    ('mem1_ecc_single_err_cnt', (YLeaf(YType.uint64, 'mem1-ecc-single-err-cnt'), ['int'])),
                                    ('mem1_ecc_double_err_cnt', (YLeaf(YType.uint64, 'mem1-ecc-double-err-cnt'), ['int'])),
                                    ('fc_cc_0_1_trans_cnt', (YLeaf(YType.uint64, 'fc-cc-0-1-trans-cnt'), ['int'])),
                                    ('rate_cnt', (YLeaf(YType.uint64, 'rate-cnt'), ['int'])),
                                    ('calc_rate', (YLeaf(YType.uint64, 'calc-rate'), ['int'])),
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
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(CrossBarStats.Nodes.Node.CrossBarTable.Sm15Stats.Sm15Stat.PeCcStats, [u'in_pkt_cnt', u'out_path0_pkt_cnt', u'out_path1_pkt_cnt', u'xbar_ecc_drop_pkt_cnt', u'mem0_drop_pkt_cnt', u'mem1_drop_pkt_cnt', u'congn_pkt_cnt', u'xbar_ecc_single_err_cnt', u'xbar_ecc_double_err_cnt', u'mem0_ecc_single_err_cnt', u'mem0_ecc_double_err_cnt', u'mem1_ecc_single_err_cnt', u'mem1_ecc_double_err_cnt', u'fc_cc_0_1_trans_cnt', u'rate_cnt', u'calc_rate'], name, value)







    def clone_ptr(self):
        self._top_entity = CrossBarStats()
        return self._top_entity



