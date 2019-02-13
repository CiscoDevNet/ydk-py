""" Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fretta\-bcm\-dpa\-hw\-resources package operational data.

This module contains definitions
for the following management objects\:
  dpa\: Stats Data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Resource(Enum):
    """
    Resource (Enum Class)

    Resource

    .. data:: lem = 0

    	lem

    .. data:: lpm = 1

    	lpm

    .. data:: encap = 2

    	encap

    .. data:: ext_tcam_ipv4 = 3

    	ext tcam ipv4

    .. data:: ext_tcam_ipv6_short = 4

    	ext tcam ipv6 short

    .. data:: ext_tcam_ipv6_long = 5

    	ext tcam ipv6 long

    .. data:: fec = 6

    	fec

    .. data:: ecmpfec = 7

    	ecmp fec

    .. data:: ext_tcam_ipv6 = 8

    	ext tcam ipv6

    """

    lem = Enum.YLeaf(0, "lem")

    lpm = Enum.YLeaf(1, "lpm")

    encap = Enum.YLeaf(2, "encap")

    ext_tcam_ipv4 = Enum.YLeaf(3, "ext-tcam-ipv4")

    ext_tcam_ipv6_short = Enum.YLeaf(4, "ext-tcam-ipv6-short")

    ext_tcam_ipv6_long = Enum.YLeaf(5, "ext-tcam-ipv6-long")

    fec = Enum.YLeaf(6, "fec")

    ecmpfec = Enum.YLeaf(7, "ecmpfec")

    ext_tcam_ipv6 = Enum.YLeaf(8, "ext-tcam-ipv6")



class Dpa(Entity):
    """
    Stats Data
    
    .. attribute:: stats
    
    	Voq or Trap Data
    	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats>`
    
    	**config**\: False
    
    

    """

    _prefix = 'fretta-bcm-dpa-hw-resources-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Dpa, self).__init__()
        self._top_entity = None

        self.yang_name = "dpa"
        self.yang_parent_name = "Cisco-IOS-XR-fretta-bcm-dpa-hw-resources-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("stats", ("stats", Dpa.Stats))])
        self._leafs = OrderedDict()

        self.stats = Dpa.Stats()
        self.stats.parent = self
        self._children_name_map["stats"] = "stats"
        self._segment_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-hw-resources-oper:dpa"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Dpa, [], name, value)


    class Stats(Entity):
        """
        Voq or Trap Data
        
        .. attribute:: nodes
        
        	DPA data for available nodes
        	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes>`
        
        	**config**\: False
        
        

        """

        _prefix = 'fretta-bcm-dpa-hw-resources-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Dpa.Stats, self).__init__()

            self.yang_name = "stats"
            self.yang_parent_name = "dpa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("nodes", ("nodes", Dpa.Stats.Nodes))])
            self._leafs = OrderedDict()

            self.nodes = Dpa.Stats.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"
            self._segment_path = lambda: "stats"
            self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-hw-resources-oper:dpa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Dpa.Stats, [], name, value)


        class Nodes(Entity):
            """
            DPA data for available nodes
            
            .. attribute:: node
            
            	DPA operational data for a particular node
            	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node>`
            
            	**config**\: False
            
            

            """

            _prefix = 'fretta-bcm-dpa-hw-resources-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Dpa.Stats.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "stats"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("node", ("node", Dpa.Stats.Nodes.Node))])
                self._leafs = OrderedDict()

                self.node = YList(self)
                self._segment_path = lambda: "nodes"
                self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-hw-resources-oper:dpa/stats/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Dpa.Stats.Nodes, [], name, value)


            class Node(Entity):
                """
                DPA operational data for a particular node
                
                .. attribute:: node_name  (key)
                
                	Node ID
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                	**config**\: False
                
                .. attribute:: asic_statistics
                
                	ASIC statistics table
                	**type**\:  :py:class:`AsicStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics>`
                
                	**config**\: False
                
                .. attribute:: npu_numbers
                
                	Ingress Stats
                	**type**\:  :py:class:`NpuNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers>`
                
                	**config**\: False
                
                .. attribute:: stats_resources_datas
                
                	OFA stats hw resources info 
                	**type**\:  :py:class:`StatsResourcesDatas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.StatsResourcesDatas>`
                
                	**config**\: False
                
                .. attribute:: hw_resources_datas
                
                	OFA hw resources stats 
                	**type**\:  :py:class:`HwResourcesDatas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.HwResourcesDatas>`
                
                	**config**\: False
                
                

                """

                _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dpa.Stats.Nodes.Node, self).__init__()

                    self.yang_name = "node"
                    self.yang_parent_name = "nodes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['node_name']
                    self._child_classes = OrderedDict([("asic-statistics", ("asic_statistics", Dpa.Stats.Nodes.Node.AsicStatistics)), ("npu-numbers", ("npu_numbers", Dpa.Stats.Nodes.Node.NpuNumbers)), ("stats-resources-datas", ("stats_resources_datas", Dpa.Stats.Nodes.Node.StatsResourcesDatas)), ("hw-resources-datas", ("hw_resources_datas", Dpa.Stats.Nodes.Node.HwResourcesDatas))])
                    self._leafs = OrderedDict([
                        ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                    ])
                    self.node_name = None

                    self.asic_statistics = Dpa.Stats.Nodes.Node.AsicStatistics()
                    self.asic_statistics.parent = self
                    self._children_name_map["asic_statistics"] = "asic-statistics"

                    self.npu_numbers = Dpa.Stats.Nodes.Node.NpuNumbers()
                    self.npu_numbers.parent = self
                    self._children_name_map["npu_numbers"] = "npu-numbers"

                    self.stats_resources_datas = Dpa.Stats.Nodes.Node.StatsResourcesDatas()
                    self.stats_resources_datas.parent = self
                    self._children_name_map["stats_resources_datas"] = "stats-resources-datas"

                    self.hw_resources_datas = Dpa.Stats.Nodes.Node.HwResourcesDatas()
                    self.hw_resources_datas.parent = self
                    self._children_name_map["hw_resources_datas"] = "hw-resources-datas"
                    self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-hw-resources-oper:dpa/stats/nodes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dpa.Stats.Nodes.Node, ['node_name'], name, value)


                class AsicStatistics(Entity):
                    """
                    ASIC statistics table
                    
                    .. attribute:: asic_statistics_detail_for_npu_ids
                    
                    	Detailed ASIC statistics
                    	**type**\:  :py:class:`AsicStatisticsDetailForNpuIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds>`
                    
                    	**config**\: False
                    
                    .. attribute:: asic_statistics_for_npu_ids
                    
                    	ASIC statistics
                    	**type**\:  :py:class:`AsicStatisticsForNpuIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dpa.Stats.Nodes.Node.AsicStatistics, self).__init__()

                        self.yang_name = "asic-statistics"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("asic-statistics-detail-for-npu-ids", ("asic_statistics_detail_for_npu_ids", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds)), ("asic-statistics-for-npu-ids", ("asic_statistics_for_npu_ids", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds))])
                        self._leafs = OrderedDict()

                        self.asic_statistics_detail_for_npu_ids = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds()
                        self.asic_statistics_detail_for_npu_ids.parent = self
                        self._children_name_map["asic_statistics_detail_for_npu_ids"] = "asic-statistics-detail-for-npu-ids"

                        self.asic_statistics_for_npu_ids = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds()
                        self.asic_statistics_for_npu_ids.parent = self
                        self._children_name_map["asic_statistics_for_npu_ids"] = "asic-statistics-for-npu-ids"
                        self._segment_path = lambda: "asic-statistics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics, [], name, value)


                    class AsicStatisticsDetailForNpuIds(Entity):
                        """
                        Detailed ASIC statistics
                        
                        .. attribute:: asic_statistics_detail_for_npu_id
                        
                        	Detailed ASIC statistics for a particular NPU
                        	**type**\: list of  		 :py:class:`AsicStatisticsDetailForNpuId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds, self).__init__()

                            self.yang_name = "asic-statistics-detail-for-npu-ids"
                            self.yang_parent_name = "asic-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("asic-statistics-detail-for-npu-id", ("asic_statistics_detail_for_npu_id", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId))])
                            self._leafs = OrderedDict()

                            self.asic_statistics_detail_for_npu_id = YList(self)
                            self._segment_path = lambda: "asic-statistics-detail-for-npu-ids"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds, [], name, value)


                        class AsicStatisticsDetailForNpuId(Entity):
                            """
                            Detailed ASIC statistics for a particular
                            NPU
                            
                            .. attribute:: npu_id  (key)
                            
                            	NPU number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: statistics
                            
                            	Statistics
                            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics>`
                            
                            	**config**\: False
                            
                            .. attribute:: valid
                            
                            	Flag to indicate if data is valid
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: rack_number
                            
                            	Rack number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: slot_number
                            
                            	Slot number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: asic_instance
                            
                            	ASIC instance
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: chip_version
                            
                            	Chip version
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId, self).__init__()

                                self.yang_name = "asic-statistics-detail-for-npu-id"
                                self.yang_parent_name = "asic-statistics-detail-for-npu-ids"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['npu_id']
                                self._child_classes = OrderedDict([("statistics", ("statistics", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics))])
                                self._leafs = OrderedDict([
                                    ('npu_id', (YLeaf(YType.uint32, 'npu-id'), ['int'])),
                                    ('valid', (YLeaf(YType.boolean, 'valid'), ['bool'])),
                                    ('rack_number', (YLeaf(YType.uint32, 'rack-number'), ['int'])),
                                    ('slot_number', (YLeaf(YType.uint32, 'slot-number'), ['int'])),
                                    ('asic_instance', (YLeaf(YType.uint32, 'asic-instance'), ['int'])),
                                    ('chip_version', (YLeaf(YType.uint16, 'chip-version'), ['int'])),
                                ])
                                self.npu_id = None
                                self.valid = None
                                self.rack_number = None
                                self.slot_number = None
                                self.asic_instance = None
                                self.chip_version = None

                                self.statistics = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics()
                                self.statistics.parent = self
                                self._children_name_map["statistics"] = "statistics"
                                self._segment_path = lambda: "asic-statistics-detail-for-npu-id" + "[npu-id='" + str(self.npu_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId, ['npu_id', 'valid', 'rack_number', 'slot_number', 'asic_instance', 'chip_version'], name, value)


                            class Statistics(Entity):
                                """
                                Statistics
                                
                                .. attribute:: num_blocks
                                
                                	Number of blocks
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: block_info
                                
                                	Block information
                                	**type**\: list of  		 :py:class:`BlockInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics, self).__init__()

                                    self.yang_name = "statistics"
                                    self.yang_parent_name = "asic-statistics-detail-for-npu-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("block-info", ("block_info", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo))])
                                    self._leafs = OrderedDict([
                                        ('num_blocks', (YLeaf(YType.uint8, 'num-blocks'), ['int'])),
                                    ])
                                    self.num_blocks = None

                                    self.block_info = YList(self)
                                    self._segment_path = lambda: "statistics"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics, ['num_blocks'], name, value)


                                class BlockInfo(Entity):
                                    """
                                    Block information
                                    
                                    .. attribute:: block_name
                                    
                                    	Block name
                                    	**type**\: str
                                    
                                    	**length:** 0..10
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_fields
                                    
                                    	Number of fields
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: field_info
                                    
                                    	Field information
                                    	**type**\: list of  		 :py:class:`FieldInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo, self).__init__()

                                        self.yang_name = "block-info"
                                        self.yang_parent_name = "statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("field-info", ("field_info", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo))])
                                        self._leafs = OrderedDict([
                                            ('block_name', (YLeaf(YType.str, 'block-name'), ['str'])),
                                            ('num_fields', (YLeaf(YType.uint8, 'num-fields'), ['int'])),
                                        ])
                                        self.block_name = None
                                        self.num_fields = None

                                        self.field_info = YList(self)
                                        self._segment_path = lambda: "block-info"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo, ['block_name', 'num_fields'], name, value)


                                    class FieldInfo(Entity):
                                        """
                                        Field information
                                        
                                        .. attribute:: field_name
                                        
                                        	Field name
                                        	**type**\: str
                                        
                                        	**length:** 0..80
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: field_value
                                        
                                        	Field value
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: is_overflow
                                        
                                        	Flag to indicate overflow
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo, self).__init__()

                                            self.yang_name = "field-info"
                                            self.yang_parent_name = "block-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('field_name', (YLeaf(YType.str, 'field-name'), ['str'])),
                                                ('field_value', (YLeaf(YType.uint64, 'field-value'), ['int'])),
                                                ('is_overflow', (YLeaf(YType.boolean, 'is-overflow'), ['bool'])),
                                            ])
                                            self.field_name = None
                                            self.field_value = None
                                            self.is_overflow = None
                                            self._segment_path = lambda: "field-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo, ['field_name', 'field_value', 'is_overflow'], name, value)







                    class AsicStatisticsForNpuIds(Entity):
                        """
                        ASIC statistics
                        
                        .. attribute:: asic_statistics_for_npu_id
                        
                        	ASIC statistics for a particular NPU
                        	**type**\: list of  		 :py:class:`AsicStatisticsForNpuId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds, self).__init__()

                            self.yang_name = "asic-statistics-for-npu-ids"
                            self.yang_parent_name = "asic-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("asic-statistics-for-npu-id", ("asic_statistics_for_npu_id", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId))])
                            self._leafs = OrderedDict()

                            self.asic_statistics_for_npu_id = YList(self)
                            self._segment_path = lambda: "asic-statistics-for-npu-ids"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds, [], name, value)


                        class AsicStatisticsForNpuId(Entity):
                            """
                            ASIC statistics for a particular NPU
                            
                            .. attribute:: npu_id  (key)
                            
                            	NPU number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: statistics
                            
                            	Statistics
                            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics>`
                            
                            	**config**\: False
                            
                            .. attribute:: valid
                            
                            	Flag to indicate if data is valid
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: rack_number
                            
                            	Rack number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: slot_number
                            
                            	Slot number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: asic_instance
                            
                            	ASIC instance
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: chip_version
                            
                            	Chip version
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId, self).__init__()

                                self.yang_name = "asic-statistics-for-npu-id"
                                self.yang_parent_name = "asic-statistics-for-npu-ids"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['npu_id']
                                self._child_classes = OrderedDict([("statistics", ("statistics", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics))])
                                self._leafs = OrderedDict([
                                    ('npu_id', (YLeaf(YType.uint32, 'npu-id'), ['int'])),
                                    ('valid', (YLeaf(YType.boolean, 'valid'), ['bool'])),
                                    ('rack_number', (YLeaf(YType.uint32, 'rack-number'), ['int'])),
                                    ('slot_number', (YLeaf(YType.uint32, 'slot-number'), ['int'])),
                                    ('asic_instance', (YLeaf(YType.uint32, 'asic-instance'), ['int'])),
                                    ('chip_version', (YLeaf(YType.uint16, 'chip-version'), ['int'])),
                                ])
                                self.npu_id = None
                                self.valid = None
                                self.rack_number = None
                                self.slot_number = None
                                self.asic_instance = None
                                self.chip_version = None

                                self.statistics = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics()
                                self.statistics.parent = self
                                self._children_name_map["statistics"] = "statistics"
                                self._segment_path = lambda: "asic-statistics-for-npu-id" + "[npu-id='" + str(self.npu_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId, ['npu_id', 'valid', 'rack_number', 'slot_number', 'asic_instance', 'chip_version'], name, value)


                            class Statistics(Entity):
                                """
                                Statistics
                                
                                .. attribute:: nbi_rx_total_byte_cnt
                                
                                	Total bytes sent from NIF to IRE
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                .. attribute:: nbi_rx_total_pkt_cnt
                                
                                	Total packets sent from NIF to IRE
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ire_cpu_pkt_cnt
                                
                                	CPU ingress received packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ire_nif_pkt_cnt
                                
                                	NIF received packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ire_oamp_pkt_cnt
                                
                                	OAMP ingress received packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ire_olp_pkt_cnt
                                
                                	OLP ingress received packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ire_rcy_pkt_cnt
                                
                                	Recycling ingress received packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ire_fdt_if_cnt
                                
                                	Performance counter of the FDT interface
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: idr_mmu_if_cnt
                                
                                	Performance counter of the MMU interface
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: idr_ocb_if_cnt
                                
                                	Performance counter of the OCB interface
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: iqm_enqueue_pkt_cnt
                                
                                	Counts enqueued packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: iqm_dequeue_pkt_cnt
                                
                                	Counts dequeued packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: iqm_deleted_pkt_cnt
                                
                                	Counts matched packets discarded in the DEQ process
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: iqm_enq_discarded_pkt_cnt
                                
                                	Counts all packets discarded at the ENQ pipe
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipt_egq_pkt_cnt
                                
                                	EGQ packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipt_enq_pkt_cnt
                                
                                	ENQ packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipt_fdt_pkt_cnt
                                
                                	FDT packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipt_cfg_event_cnt
                                
                                	Configurable event counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipt_cfg_byte_cnt
                                
                                	Configurable bytes counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                .. attribute:: fdt_ipt_desc_cell_cnt
                                
                                	Descriptor cell counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fdt_ire_desc_cell_cnt
                                
                                	IRE internal descriptor cell counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fdt_transmitted_data_cells_cnt
                                
                                	Counts all transmitted data cells
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fdr_p1_cell_in_cnt
                                
                                	FDR total incoming cell counter at pipe 1
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fdr_p2_cell_in_cnt
                                
                                	FDR total incoming cell counter at pipe 2
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fdr_p3_cell_in_cnt
                                
                                	FDR total incoming cell counter at pipe 3
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fdr_cell_in_cnt_total
                                
                                	FDR total incoming cell counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_in_cnt_p1
                                
                                	FDA input cell counter P1
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_in_cnt_p2
                                
                                	FDA input cell counter P2
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_in_cnt_p3
                                
                                	FDA input cell counter P3
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_in_tdm_cnt
                                
                                	FDA input cell counter TDM
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_in_meshmc_cnt
                                
                                	FDA input cell counter MESHMC
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_in_ipt_cnt
                                
                                	FDA input cell counter IPT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_out_cnt_p1
                                
                                	FDA output cell counter P1
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_out_cnt_p2
                                
                                	FDA output cell counter P2
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_out_cnt_p3
                                
                                	FDA output cell counter P3
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_out_tdm_cnt
                                
                                	FDA output cell counter TDM
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_out_meshmc_cnt
                                
                                	FDA output cell counter MESHMC
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_out_ipt_cnt
                                
                                	FDA output cell counter IPT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_egq_drop_cnt
                                
                                	FDA EGQ drop counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_egq_meshmc_drop_cnt
                                
                                	FDA EGQ MESHMC drop counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_fqp_pkt_cnt
                                
                                	FQP2EPE packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_pqp_uc_pkt_cnt
                                
                                	PQP2FQP unicast packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_pqp_discard_uc_pkt_cnt
                                
                                	PQP discarded unicast packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_pqp_uc_bytes_cnt
                                
                                	PQP2FQP unicast bytes counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                .. attribute:: egq_pqp_mc_pkt_cnt
                                
                                	PQP2FQP multicast packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_pqp_discard_mc_pkt_cnt
                                
                                	PQP discarded multicast packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_pqp_mc_bytes_cnt
                                
                                	PQP2FQP multicast bytes counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                .. attribute:: egq_ehp_uc_pkt_cnt
                                
                                	EHP2PQP unicast packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_ehp_mc_high_pkt_cnt
                                
                                	EHP2PQP multicast high packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_ehp_mc_low_pkt_cnt
                                
                                	EHP2PQP multicast low packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_deleted_pkt_cnt
                                
                                	EHP2PQP discarded packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_ehp_mc_high_discard_cnt
                                
                                	Number of multicast high packets discarded because multicast FIFO is full
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_ehp_mc_low_discard_cnt
                                
                                	Number of multicast low packets discarded because multicast FIFO is full
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_erpp_lag_pruning_discard_cnt
                                
                                	Number of packet descriptors discarded due to LAG multicast pruning
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_erpp_pmf_discard_cnt
                                
                                	Number of packet descriptors discarded due to ERPP PMF
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_erpp_vlan_mbr_discard_cnt
                                
                                	Number of packet descriptors discarded because of egress VLAN membership
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: epni_epe_byte_cnt
                                
                                	EPE2PNI bytes counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                .. attribute:: epni_epe_pkt_cnt
                                
                                	EPE2PNI packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: epni_epe_discard_cnt
                                
                                	EPE discarded packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: nbi_tx_total_byte_cnt
                                
                                	Total bytes sent from EGQ to NIF
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                .. attribute:: nbi_tx_total_pkt_cnt
                                
                                	Total packets sent from EGQ to NIF
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics, self).__init__()

                                    self.yang_name = "statistics"
                                    self.yang_parent_name = "asic-statistics-for-npu-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('nbi_rx_total_byte_cnt', (YLeaf(YType.uint64, 'nbi-rx-total-byte-cnt'), ['int'])),
                                        ('nbi_rx_total_pkt_cnt', (YLeaf(YType.uint64, 'nbi-rx-total-pkt-cnt'), ['int'])),
                                        ('ire_cpu_pkt_cnt', (YLeaf(YType.uint64, 'ire-cpu-pkt-cnt'), ['int'])),
                                        ('ire_nif_pkt_cnt', (YLeaf(YType.uint64, 'ire-nif-pkt-cnt'), ['int'])),
                                        ('ire_oamp_pkt_cnt', (YLeaf(YType.uint64, 'ire-oamp-pkt-cnt'), ['int'])),
                                        ('ire_olp_pkt_cnt', (YLeaf(YType.uint64, 'ire-olp-pkt-cnt'), ['int'])),
                                        ('ire_rcy_pkt_cnt', (YLeaf(YType.uint64, 'ire-rcy-pkt-cnt'), ['int'])),
                                        ('ire_fdt_if_cnt', (YLeaf(YType.uint64, 'ire-fdt-if-cnt'), ['int'])),
                                        ('idr_mmu_if_cnt', (YLeaf(YType.uint64, 'idr-mmu-if-cnt'), ['int'])),
                                        ('idr_ocb_if_cnt', (YLeaf(YType.uint64, 'idr-ocb-if-cnt'), ['int'])),
                                        ('iqm_enqueue_pkt_cnt', (YLeaf(YType.uint64, 'iqm-enqueue-pkt-cnt'), ['int'])),
                                        ('iqm_dequeue_pkt_cnt', (YLeaf(YType.uint64, 'iqm-dequeue-pkt-cnt'), ['int'])),
                                        ('iqm_deleted_pkt_cnt', (YLeaf(YType.uint64, 'iqm-deleted-pkt-cnt'), ['int'])),
                                        ('iqm_enq_discarded_pkt_cnt', (YLeaf(YType.uint64, 'iqm-enq-discarded-pkt-cnt'), ['int'])),
                                        ('ipt_egq_pkt_cnt', (YLeaf(YType.uint64, 'ipt-egq-pkt-cnt'), ['int'])),
                                        ('ipt_enq_pkt_cnt', (YLeaf(YType.uint64, 'ipt-enq-pkt-cnt'), ['int'])),
                                        ('ipt_fdt_pkt_cnt', (YLeaf(YType.uint64, 'ipt-fdt-pkt-cnt'), ['int'])),
                                        ('ipt_cfg_event_cnt', (YLeaf(YType.uint64, 'ipt-cfg-event-cnt'), ['int'])),
                                        ('ipt_cfg_byte_cnt', (YLeaf(YType.uint64, 'ipt-cfg-byte-cnt'), ['int'])),
                                        ('fdt_ipt_desc_cell_cnt', (YLeaf(YType.uint64, 'fdt-ipt-desc-cell-cnt'), ['int'])),
                                        ('fdt_ire_desc_cell_cnt', (YLeaf(YType.uint64, 'fdt-ire-desc-cell-cnt'), ['int'])),
                                        ('fdt_transmitted_data_cells_cnt', (YLeaf(YType.uint64, 'fdt-transmitted-data-cells-cnt'), ['int'])),
                                        ('fdr_p1_cell_in_cnt', (YLeaf(YType.uint64, 'fdr-p1-cell-in-cnt'), ['int'])),
                                        ('fdr_p2_cell_in_cnt', (YLeaf(YType.uint64, 'fdr-p2-cell-in-cnt'), ['int'])),
                                        ('fdr_p3_cell_in_cnt', (YLeaf(YType.uint64, 'fdr-p3-cell-in-cnt'), ['int'])),
                                        ('fdr_cell_in_cnt_total', (YLeaf(YType.uint64, 'fdr-cell-in-cnt-total'), ['int'])),
                                        ('fda_cells_in_cnt_p1', (YLeaf(YType.uint64, 'fda-cells-in-cnt-p1'), ['int'])),
                                        ('fda_cells_in_cnt_p2', (YLeaf(YType.uint64, 'fda-cells-in-cnt-p2'), ['int'])),
                                        ('fda_cells_in_cnt_p3', (YLeaf(YType.uint64, 'fda-cells-in-cnt-p3'), ['int'])),
                                        ('fda_cells_in_tdm_cnt', (YLeaf(YType.uint64, 'fda-cells-in-tdm-cnt'), ['int'])),
                                        ('fda_cells_in_meshmc_cnt', (YLeaf(YType.uint64, 'fda-cells-in-meshmc-cnt'), ['int'])),
                                        ('fda_cells_in_ipt_cnt', (YLeaf(YType.uint64, 'fda-cells-in-ipt-cnt'), ['int'])),
                                        ('fda_cells_out_cnt_p1', (YLeaf(YType.uint64, 'fda-cells-out-cnt-p1'), ['int'])),
                                        ('fda_cells_out_cnt_p2', (YLeaf(YType.uint64, 'fda-cells-out-cnt-p2'), ['int'])),
                                        ('fda_cells_out_cnt_p3', (YLeaf(YType.uint64, 'fda-cells-out-cnt-p3'), ['int'])),
                                        ('fda_cells_out_tdm_cnt', (YLeaf(YType.uint64, 'fda-cells-out-tdm-cnt'), ['int'])),
                                        ('fda_cells_out_meshmc_cnt', (YLeaf(YType.uint64, 'fda-cells-out-meshmc-cnt'), ['int'])),
                                        ('fda_cells_out_ipt_cnt', (YLeaf(YType.uint64, 'fda-cells-out-ipt-cnt'), ['int'])),
                                        ('fda_egq_drop_cnt', (YLeaf(YType.uint64, 'fda-egq-drop-cnt'), ['int'])),
                                        ('fda_egq_meshmc_drop_cnt', (YLeaf(YType.uint64, 'fda-egq-meshmc-drop-cnt'), ['int'])),
                                        ('egq_fqp_pkt_cnt', (YLeaf(YType.uint64, 'egq-fqp-pkt-cnt'), ['int'])),
                                        ('egq_pqp_uc_pkt_cnt', (YLeaf(YType.uint64, 'egq-pqp-uc-pkt-cnt'), ['int'])),
                                        ('egq_pqp_discard_uc_pkt_cnt', (YLeaf(YType.uint64, 'egq-pqp-discard-uc-pkt-cnt'), ['int'])),
                                        ('egq_pqp_uc_bytes_cnt', (YLeaf(YType.uint64, 'egq-pqp-uc-bytes-cnt'), ['int'])),
                                        ('egq_pqp_mc_pkt_cnt', (YLeaf(YType.uint64, 'egq-pqp-mc-pkt-cnt'), ['int'])),
                                        ('egq_pqp_discard_mc_pkt_cnt', (YLeaf(YType.uint64, 'egq-pqp-discard-mc-pkt-cnt'), ['int'])),
                                        ('egq_pqp_mc_bytes_cnt', (YLeaf(YType.uint64, 'egq-pqp-mc-bytes-cnt'), ['int'])),
                                        ('egq_ehp_uc_pkt_cnt', (YLeaf(YType.uint64, 'egq-ehp-uc-pkt-cnt'), ['int'])),
                                        ('egq_ehp_mc_high_pkt_cnt', (YLeaf(YType.uint64, 'egq-ehp-mc-high-pkt-cnt'), ['int'])),
                                        ('egq_ehp_mc_low_pkt_cnt', (YLeaf(YType.uint64, 'egq-ehp-mc-low-pkt-cnt'), ['int'])),
                                        ('egq_deleted_pkt_cnt', (YLeaf(YType.uint64, 'egq-deleted-pkt-cnt'), ['int'])),
                                        ('egq_ehp_mc_high_discard_cnt', (YLeaf(YType.uint64, 'egq-ehp-mc-high-discard-cnt'), ['int'])),
                                        ('egq_ehp_mc_low_discard_cnt', (YLeaf(YType.uint64, 'egq-ehp-mc-low-discard-cnt'), ['int'])),
                                        ('egq_erpp_lag_pruning_discard_cnt', (YLeaf(YType.uint64, 'egq-erpp-lag-pruning-discard-cnt'), ['int'])),
                                        ('egq_erpp_pmf_discard_cnt', (YLeaf(YType.uint64, 'egq-erpp-pmf-discard-cnt'), ['int'])),
                                        ('egq_erpp_vlan_mbr_discard_cnt', (YLeaf(YType.uint64, 'egq-erpp-vlan-mbr-discard-cnt'), ['int'])),
                                        ('epni_epe_byte_cnt', (YLeaf(YType.uint64, 'epni-epe-byte-cnt'), ['int'])),
                                        ('epni_epe_pkt_cnt', (YLeaf(YType.uint64, 'epni-epe-pkt-cnt'), ['int'])),
                                        ('epni_epe_discard_cnt', (YLeaf(YType.uint64, 'epni-epe-discard-cnt'), ['int'])),
                                        ('nbi_tx_total_byte_cnt', (YLeaf(YType.uint64, 'nbi-tx-total-byte-cnt'), ['int'])),
                                        ('nbi_tx_total_pkt_cnt', (YLeaf(YType.uint64, 'nbi-tx-total-pkt-cnt'), ['int'])),
                                    ])
                                    self.nbi_rx_total_byte_cnt = None
                                    self.nbi_rx_total_pkt_cnt = None
                                    self.ire_cpu_pkt_cnt = None
                                    self.ire_nif_pkt_cnt = None
                                    self.ire_oamp_pkt_cnt = None
                                    self.ire_olp_pkt_cnt = None
                                    self.ire_rcy_pkt_cnt = None
                                    self.ire_fdt_if_cnt = None
                                    self.idr_mmu_if_cnt = None
                                    self.idr_ocb_if_cnt = None
                                    self.iqm_enqueue_pkt_cnt = None
                                    self.iqm_dequeue_pkt_cnt = None
                                    self.iqm_deleted_pkt_cnt = None
                                    self.iqm_enq_discarded_pkt_cnt = None
                                    self.ipt_egq_pkt_cnt = None
                                    self.ipt_enq_pkt_cnt = None
                                    self.ipt_fdt_pkt_cnt = None
                                    self.ipt_cfg_event_cnt = None
                                    self.ipt_cfg_byte_cnt = None
                                    self.fdt_ipt_desc_cell_cnt = None
                                    self.fdt_ire_desc_cell_cnt = None
                                    self.fdt_transmitted_data_cells_cnt = None
                                    self.fdr_p1_cell_in_cnt = None
                                    self.fdr_p2_cell_in_cnt = None
                                    self.fdr_p3_cell_in_cnt = None
                                    self.fdr_cell_in_cnt_total = None
                                    self.fda_cells_in_cnt_p1 = None
                                    self.fda_cells_in_cnt_p2 = None
                                    self.fda_cells_in_cnt_p3 = None
                                    self.fda_cells_in_tdm_cnt = None
                                    self.fda_cells_in_meshmc_cnt = None
                                    self.fda_cells_in_ipt_cnt = None
                                    self.fda_cells_out_cnt_p1 = None
                                    self.fda_cells_out_cnt_p2 = None
                                    self.fda_cells_out_cnt_p3 = None
                                    self.fda_cells_out_tdm_cnt = None
                                    self.fda_cells_out_meshmc_cnt = None
                                    self.fda_cells_out_ipt_cnt = None
                                    self.fda_egq_drop_cnt = None
                                    self.fda_egq_meshmc_drop_cnt = None
                                    self.egq_fqp_pkt_cnt = None
                                    self.egq_pqp_uc_pkt_cnt = None
                                    self.egq_pqp_discard_uc_pkt_cnt = None
                                    self.egq_pqp_uc_bytes_cnt = None
                                    self.egq_pqp_mc_pkt_cnt = None
                                    self.egq_pqp_discard_mc_pkt_cnt = None
                                    self.egq_pqp_mc_bytes_cnt = None
                                    self.egq_ehp_uc_pkt_cnt = None
                                    self.egq_ehp_mc_high_pkt_cnt = None
                                    self.egq_ehp_mc_low_pkt_cnt = None
                                    self.egq_deleted_pkt_cnt = None
                                    self.egq_ehp_mc_high_discard_cnt = None
                                    self.egq_ehp_mc_low_discard_cnt = None
                                    self.egq_erpp_lag_pruning_discard_cnt = None
                                    self.egq_erpp_pmf_discard_cnt = None
                                    self.egq_erpp_vlan_mbr_discard_cnt = None
                                    self.epni_epe_byte_cnt = None
                                    self.epni_epe_pkt_cnt = None
                                    self.epni_epe_discard_cnt = None
                                    self.nbi_tx_total_byte_cnt = None
                                    self.nbi_tx_total_pkt_cnt = None
                                    self._segment_path = lambda: "statistics"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics, ['nbi_rx_total_byte_cnt', 'nbi_rx_total_pkt_cnt', 'ire_cpu_pkt_cnt', 'ire_nif_pkt_cnt', 'ire_oamp_pkt_cnt', 'ire_olp_pkt_cnt', 'ire_rcy_pkt_cnt', 'ire_fdt_if_cnt', 'idr_mmu_if_cnt', 'idr_ocb_if_cnt', 'iqm_enqueue_pkt_cnt', 'iqm_dequeue_pkt_cnt', 'iqm_deleted_pkt_cnt', 'iqm_enq_discarded_pkt_cnt', 'ipt_egq_pkt_cnt', 'ipt_enq_pkt_cnt', 'ipt_fdt_pkt_cnt', 'ipt_cfg_event_cnt', 'ipt_cfg_byte_cnt', 'fdt_ipt_desc_cell_cnt', 'fdt_ire_desc_cell_cnt', 'fdt_transmitted_data_cells_cnt', 'fdr_p1_cell_in_cnt', 'fdr_p2_cell_in_cnt', 'fdr_p3_cell_in_cnt', 'fdr_cell_in_cnt_total', 'fda_cells_in_cnt_p1', 'fda_cells_in_cnt_p2', 'fda_cells_in_cnt_p3', 'fda_cells_in_tdm_cnt', 'fda_cells_in_meshmc_cnt', 'fda_cells_in_ipt_cnt', 'fda_cells_out_cnt_p1', 'fda_cells_out_cnt_p2', 'fda_cells_out_cnt_p3', 'fda_cells_out_tdm_cnt', 'fda_cells_out_meshmc_cnt', 'fda_cells_out_ipt_cnt', 'fda_egq_drop_cnt', 'fda_egq_meshmc_drop_cnt', 'egq_fqp_pkt_cnt', 'egq_pqp_uc_pkt_cnt', 'egq_pqp_discard_uc_pkt_cnt', 'egq_pqp_uc_bytes_cnt', 'egq_pqp_mc_pkt_cnt', 'egq_pqp_discard_mc_pkt_cnt', 'egq_pqp_mc_bytes_cnt', 'egq_ehp_uc_pkt_cnt', 'egq_ehp_mc_high_pkt_cnt', 'egq_ehp_mc_low_pkt_cnt', 'egq_deleted_pkt_cnt', 'egq_ehp_mc_high_discard_cnt', 'egq_ehp_mc_low_discard_cnt', 'egq_erpp_lag_pruning_discard_cnt', 'egq_erpp_pmf_discard_cnt', 'egq_erpp_vlan_mbr_discard_cnt', 'epni_epe_byte_cnt', 'epni_epe_pkt_cnt', 'epni_epe_discard_cnt', 'nbi_tx_total_byte_cnt', 'nbi_tx_total_pkt_cnt'], name, value)






                class NpuNumbers(Entity):
                    """
                    Ingress Stats
                    
                    .. attribute:: npu_number
                    
                    	Stats for a particular npu
                    	**type**\: list of  		 :py:class:`NpuNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dpa.Stats.Nodes.Node.NpuNumbers, self).__init__()

                        self.yang_name = "npu-numbers"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("npu-number", ("npu_number", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber))])
                        self._leafs = OrderedDict()

                        self.npu_number = YList(self)
                        self._segment_path = lambda: "npu-numbers"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers, [], name, value)


                    class NpuNumber(Entity):
                        """
                        Stats for a particular npu
                        
                        .. attribute:: npu_id  (key)
                        
                        	Npu number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: display
                        
                        	show npu specific voq or trap stats
                        	**type**\:  :py:class:`Display <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber, self).__init__()

                            self.yang_name = "npu-number"
                            self.yang_parent_name = "npu-numbers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['npu_id']
                            self._child_classes = OrderedDict([("display", ("display", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display))])
                            self._leafs = OrderedDict([
                                ('npu_id', (YLeaf(YType.uint32, 'npu-id'), ['int'])),
                            ])
                            self.npu_id = None

                            self.display = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display()
                            self.display.parent = self
                            self._children_name_map["display"] = "display"
                            self._segment_path = lambda: "npu-number" + "[npu-id='" + str(self.npu_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber, ['npu_id'], name, value)


                        class Display(Entity):
                            """
                            show npu specific voq or trap stats
                            
                            .. attribute:: trap_ids
                            
                            	Trap stats for a particular npu
                            	**type**\:  :py:class:`TrapIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds>`
                            
                            	**config**\: False
                            
                            .. attribute:: interface_handles
                            
                            	Voq stats grouped by interface handle
                            	**type**\:  :py:class:`InterfaceHandles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles>`
                            
                            	**config**\: False
                            
                            .. attribute:: base_numbers
                            
                            	Voq stats grouped by voq base numbers
                            	**type**\:  :py:class:`BaseNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display, self).__init__()

                                self.yang_name = "display"
                                self.yang_parent_name = "npu-number"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("trap-ids", ("trap_ids", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds)), ("interface-handles", ("interface_handles", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles)), ("base-numbers", ("base_numbers", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers))])
                                self._leafs = OrderedDict()

                                self.trap_ids = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds()
                                self.trap_ids.parent = self
                                self._children_name_map["trap_ids"] = "trap-ids"

                                self.interface_handles = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles()
                                self.interface_handles.parent = self
                                self._children_name_map["interface_handles"] = "interface-handles"

                                self.base_numbers = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers()
                                self.base_numbers.parent = self
                                self._children_name_map["base_numbers"] = "base-numbers"
                                self._segment_path = lambda: "display"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display, [], name, value)


                            class TrapIds(Entity):
                                """
                                Trap stats for a particular npu
                                
                                .. attribute:: trap_id
                                
                                	Filter by specific trap id
                                	**type**\: list of  		 :py:class:`TrapId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds, self).__init__()

                                    self.yang_name = "trap-ids"
                                    self.yang_parent_name = "display"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("trap-id", ("trap_id", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId))])
                                    self._leafs = OrderedDict()

                                    self.trap_id = YList(self)
                                    self._segment_path = lambda: "trap-ids"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds, [], name, value)


                                class TrapId(Entity):
                                    """
                                    Filter by specific trap id
                                    
                                    .. attribute:: trap_id  (key)
                                    
                                    	Trap ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: trap_strength
                                    
                                    	Trap Strength of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: priority
                                    
                                    	Priority of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: trap_id_xr
                                    
                                    	Id of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: gport
                                    
                                    	Gport of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fec_id
                                    
                                    	Fec id of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: policer_id
                                    
                                    	Id of the policer on the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: stats_id
                                    
                                    	Stats Id of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: encap_id
                                    
                                    	Encap Id of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: mc_group
                                    
                                    	McGroup of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: trap_string
                                    
                                    	Name String of the trap
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: id
                                    
                                    	Id for internal use
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: offset
                                    
                                    	Offset for internal use
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: npu_id
                                    
                                    	NpuId on which trap is enabled
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: packet_dropped
                                    
                                    	Number of packets dropped after hitting the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: packet_accepted
                                    
                                    	Number of packets accepted after hitting the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId, self).__init__()

                                        self.yang_name = "trap-id"
                                        self.yang_parent_name = "trap-ids"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['trap_id']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('trap_id', (YLeaf(YType.uint32, 'trap-id'), ['int'])),
                                            ('trap_strength', (YLeaf(YType.uint32, 'trap-strength'), ['int'])),
                                            ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                            ('trap_id_xr', (YLeaf(YType.uint32, 'trap-id-xr'), ['int'])),
                                            ('gport', (YLeaf(YType.uint32, 'gport'), ['int'])),
                                            ('fec_id', (YLeaf(YType.uint32, 'fec-id'), ['int'])),
                                            ('policer_id', (YLeaf(YType.uint32, 'policer-id'), ['int'])),
                                            ('stats_id', (YLeaf(YType.uint32, 'stats-id'), ['int'])),
                                            ('encap_id', (YLeaf(YType.uint32, 'encap-id'), ['int'])),
                                            ('mc_group', (YLeaf(YType.uint32, 'mc-group'), ['int'])),
                                            ('trap_string', (YLeaf(YType.str, 'trap-string'), ['str'])),
                                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                            ('offset', (YLeaf(YType.uint64, 'offset'), ['int'])),
                                            ('npu_id', (YLeaf(YType.uint64, 'npu-id'), ['int'])),
                                            ('packet_dropped', (YLeaf(YType.uint64, 'packet-dropped'), ['int'])),
                                            ('packet_accepted', (YLeaf(YType.uint64, 'packet-accepted'), ['int'])),
                                        ])
                                        self.trap_id = None
                                        self.trap_strength = None
                                        self.priority = None
                                        self.trap_id_xr = None
                                        self.gport = None
                                        self.fec_id = None
                                        self.policer_id = None
                                        self.stats_id = None
                                        self.encap_id = None
                                        self.mc_group = None
                                        self.trap_string = None
                                        self.id = None
                                        self.offset = None
                                        self.npu_id = None
                                        self.packet_dropped = None
                                        self.packet_accepted = None
                                        self._segment_path = lambda: "trap-id" + "[trap-id='" + str(self.trap_id) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId, ['trap_id', 'trap_strength', 'priority', 'trap_id_xr', 'gport', 'fec_id', 'policer_id', 'stats_id', 'encap_id', 'mc_group', 'trap_string', 'id', 'offset', 'npu_id', 'packet_dropped', 'packet_accepted'], name, value)




                            class InterfaceHandles(Entity):
                                """
                                Voq stats grouped by interface handle
                                
                                .. attribute:: interface_handle
                                
                                	Voq stats for a particular interface handle
                                	**type**\: list of  		 :py:class:`InterfaceHandle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles, self).__init__()

                                    self.yang_name = "interface-handles"
                                    self.yang_parent_name = "display"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("interface-handle", ("interface_handle", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle))])
                                    self._leafs = OrderedDict()

                                    self.interface_handle = YList(self)
                                    self._segment_path = lambda: "interface-handles"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles, [], name, value)


                                class InterfaceHandle(Entity):
                                    """
                                    Voq stats for a particular interface
                                    handle
                                    
                                    .. attribute:: interface_handle  (key)
                                    
                                    	Interface Handle
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: in_use
                                    
                                    	Flag to indicate if port is in use
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rack_num
                                    
                                    	Rack of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: slot_num
                                    
                                    	Slot of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: npu_num
                                    
                                    	NPU of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: npu_core
                                    
                                    	NPU core of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: port_num
                                    
                                    	Port Number of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: if_handle
                                    
                                    	IfHandle of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: sys_port
                                    
                                    	System port of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: pp_port
                                    
                                    	PP Port number of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: port_speed
                                    
                                    	Port speed of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: voq_base
                                    
                                    	Voq Base number of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: connector_id
                                    
                                    	Connector id of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: is_local_port
                                    
                                    	Flag to indicate if port is local to the node
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: voq_stat
                                    
                                    	Keeps a record of the received and dropped packets and bytes on the port
                                    	**type**\: list of  		 :py:class:`VoqStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle, self).__init__()

                                        self.yang_name = "interface-handle"
                                        self.yang_parent_name = "interface-handles"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['interface_handle']
                                        self._child_classes = OrderedDict([("voq-stat", ("voq_stat", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat))])
                                        self._leafs = OrderedDict([
                                            ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                                            ('in_use', (YLeaf(YType.boolean, 'in-use'), ['bool'])),
                                            ('rack_num', (YLeaf(YType.uint8, 'rack-num'), ['int'])),
                                            ('slot_num', (YLeaf(YType.uint8, 'slot-num'), ['int'])),
                                            ('npu_num', (YLeaf(YType.uint8, 'npu-num'), ['int'])),
                                            ('npu_core', (YLeaf(YType.uint8, 'npu-core'), ['int'])),
                                            ('port_num', (YLeaf(YType.uint8, 'port-num'), ['int'])),
                                            ('if_handle', (YLeaf(YType.uint32, 'if-handle'), ['int'])),
                                            ('sys_port', (YLeaf(YType.uint32, 'sys-port'), ['int'])),
                                            ('pp_port', (YLeaf(YType.uint32, 'pp-port'), ['int'])),
                                            ('port_speed', (YLeaf(YType.uint32, 'port-speed'), ['int'])),
                                            ('voq_base', (YLeaf(YType.uint32, 'voq-base'), ['int'])),
                                            ('connector_id', (YLeaf(YType.uint32, 'connector-id'), ['int'])),
                                            ('is_local_port', (YLeaf(YType.boolean, 'is-local-port'), ['bool'])),
                                        ])
                                        self.interface_handle = None
                                        self.in_use = None
                                        self.rack_num = None
                                        self.slot_num = None
                                        self.npu_num = None
                                        self.npu_core = None
                                        self.port_num = None
                                        self.if_handle = None
                                        self.sys_port = None
                                        self.pp_port = None
                                        self.port_speed = None
                                        self.voq_base = None
                                        self.connector_id = None
                                        self.is_local_port = None

                                        self.voq_stat = YList(self)
                                        self._segment_path = lambda: "interface-handle" + "[interface-handle='" + str(self.interface_handle) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle, ['interface_handle', 'in_use', 'rack_num', 'slot_num', 'npu_num', 'npu_core', 'port_num', 'if_handle', 'sys_port', 'pp_port', 'port_speed', 'voq_base', 'connector_id', 'is_local_port'], name, value)


                                    class VoqStat(Entity):
                                        """
                                        Keeps a record of the received and dropped
                                        packets and bytes on the port
                                        
                                        .. attribute:: received_bytes
                                        
                                        	Bytes Received on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: received_packets
                                        
                                        	Packets Received on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: dropped_bytes
                                        
                                        	Bytes Dropped on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: dropped_packets
                                        
                                        	Packets Dropeed on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat, self).__init__()

                                            self.yang_name = "voq-stat"
                                            self.yang_parent_name = "interface-handle"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('received_bytes', (YLeaf(YType.uint64, 'received-bytes'), ['int'])),
                                                ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                                ('dropped_bytes', (YLeaf(YType.uint64, 'dropped-bytes'), ['int'])),
                                                ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                            ])
                                            self.received_bytes = None
                                            self.received_packets = None
                                            self.dropped_bytes = None
                                            self.dropped_packets = None
                                            self._segment_path = lambda: "voq-stat"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat, ['received_bytes', 'received_packets', 'dropped_bytes', 'dropped_packets'], name, value)





                            class BaseNumbers(Entity):
                                """
                                Voq stats grouped by voq base numbers
                                
                                .. attribute:: base_number
                                
                                	Voq Base Number for a particular voq
                                	**type**\: list of  		 :py:class:`BaseNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers, self).__init__()

                                    self.yang_name = "base-numbers"
                                    self.yang_parent_name = "display"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("base-number", ("base_number", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber))])
                                    self._leafs = OrderedDict()

                                    self.base_number = YList(self)
                                    self._segment_path = lambda: "base-numbers"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers, [], name, value)


                                class BaseNumber(Entity):
                                    """
                                    Voq Base Number for a particular voq
                                    
                                    .. attribute:: base_number  (key)
                                    
                                    	Interface handle
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: in_use
                                    
                                    	Flag to indicate if port is in use
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rack_num
                                    
                                    	Rack of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: slot_num
                                    
                                    	Slot of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: npu_num
                                    
                                    	NPU of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: npu_core
                                    
                                    	NPU core of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: port_num
                                    
                                    	Port Number of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: if_handle
                                    
                                    	IfHandle of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: sys_port
                                    
                                    	System port of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: pp_port
                                    
                                    	PP Port number of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: port_speed
                                    
                                    	Port speed of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: voq_base
                                    
                                    	Voq Base number of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: connector_id
                                    
                                    	Connector id of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: is_local_port
                                    
                                    	Flag to indicate if port is local to the node
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: voq_stat
                                    
                                    	Keeps a record of the received and dropped packets and bytes on the port
                                    	**type**\: list of  		 :py:class:`VoqStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber, self).__init__()

                                        self.yang_name = "base-number"
                                        self.yang_parent_name = "base-numbers"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['base_number']
                                        self._child_classes = OrderedDict([("voq-stat", ("voq_stat", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat))])
                                        self._leafs = OrderedDict([
                                            ('base_number', (YLeaf(YType.uint32, 'base-number'), ['int'])),
                                            ('in_use', (YLeaf(YType.boolean, 'in-use'), ['bool'])),
                                            ('rack_num', (YLeaf(YType.uint8, 'rack-num'), ['int'])),
                                            ('slot_num', (YLeaf(YType.uint8, 'slot-num'), ['int'])),
                                            ('npu_num', (YLeaf(YType.uint8, 'npu-num'), ['int'])),
                                            ('npu_core', (YLeaf(YType.uint8, 'npu-core'), ['int'])),
                                            ('port_num', (YLeaf(YType.uint8, 'port-num'), ['int'])),
                                            ('if_handle', (YLeaf(YType.uint32, 'if-handle'), ['int'])),
                                            ('sys_port', (YLeaf(YType.uint32, 'sys-port'), ['int'])),
                                            ('pp_port', (YLeaf(YType.uint32, 'pp-port'), ['int'])),
                                            ('port_speed', (YLeaf(YType.uint32, 'port-speed'), ['int'])),
                                            ('voq_base', (YLeaf(YType.uint32, 'voq-base'), ['int'])),
                                            ('connector_id', (YLeaf(YType.uint32, 'connector-id'), ['int'])),
                                            ('is_local_port', (YLeaf(YType.boolean, 'is-local-port'), ['bool'])),
                                        ])
                                        self.base_number = None
                                        self.in_use = None
                                        self.rack_num = None
                                        self.slot_num = None
                                        self.npu_num = None
                                        self.npu_core = None
                                        self.port_num = None
                                        self.if_handle = None
                                        self.sys_port = None
                                        self.pp_port = None
                                        self.port_speed = None
                                        self.voq_base = None
                                        self.connector_id = None
                                        self.is_local_port = None

                                        self.voq_stat = YList(self)
                                        self._segment_path = lambda: "base-number" + "[base-number='" + str(self.base_number) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber, ['base_number', 'in_use', 'rack_num', 'slot_num', 'npu_num', 'npu_core', 'port_num', 'if_handle', 'sys_port', 'pp_port', 'port_speed', 'voq_base', 'connector_id', 'is_local_port'], name, value)


                                    class VoqStat(Entity):
                                        """
                                        Keeps a record of the received and dropped
                                        packets and bytes on the port
                                        
                                        .. attribute:: received_bytes
                                        
                                        	Bytes Received on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: received_packets
                                        
                                        	Packets Received on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: dropped_bytes
                                        
                                        	Bytes Dropped on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: dropped_packets
                                        
                                        	Packets Dropeed on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat, self).__init__()

                                            self.yang_name = "voq-stat"
                                            self.yang_parent_name = "base-number"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('received_bytes', (YLeaf(YType.uint64, 'received-bytes'), ['int'])),
                                                ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                                ('dropped_bytes', (YLeaf(YType.uint64, 'dropped-bytes'), ['int'])),
                                                ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                            ])
                                            self.received_bytes = None
                                            self.received_packets = None
                                            self.dropped_bytes = None
                                            self.dropped_packets = None
                                            self._segment_path = lambda: "voq-stat"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat, ['received_bytes', 'received_packets', 'dropped_bytes', 'dropped_packets'], name, value)








                class StatsResourcesDatas(Entity):
                    """
                    OFA stats hw resources info 
                    
                    .. attribute:: stats_resources_data
                    
                    	Stats Hardware resources table
                    	**type**\: list of  		 :py:class:`StatsResourcesData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.StatsResourcesDatas.StatsResourcesData>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dpa.Stats.Nodes.Node.StatsResourcesDatas, self).__init__()

                        self.yang_name = "stats-resources-datas"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("stats-resources-data", ("stats_resources_data", Dpa.Stats.Nodes.Node.StatsResourcesDatas.StatsResourcesData))])
                        self._leafs = OrderedDict()

                        self.stats_resources_data = YList(self)
                        self._segment_path = lambda: "stats-resources-datas"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dpa.Stats.Nodes.Node.StatsResourcesDatas, [], name, value)


                    class StatsResourcesData(Entity):
                        """
                        Stats Hardware resources table
                        
                        .. attribute:: resource  (key)
                        
                        	Resource type
                        	**type**\:  :py:class:`Resource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Resource>`
                        
                        	**config**\: False
                        
                        .. attribute:: sys_cp_cnfg_prof
                        
                        	sys cp cnfg prof
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: next_avail_cp_id
                        
                        	next avail cp id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: num_cntr_engines
                        
                        	num cntr engines
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: cntr_engine
                        
                        	cntr engine
                        	**type**\: list of  		 :py:class:`CntrEngine <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.StatsResourcesDatas.StatsResourcesData.CntrEngine>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dpa.Stats.Nodes.Node.StatsResourcesDatas.StatsResourcesData, self).__init__()

                            self.yang_name = "stats-resources-data"
                            self.yang_parent_name = "stats-resources-datas"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['resource']
                            self._child_classes = OrderedDict([("cntr-engine", ("cntr_engine", Dpa.Stats.Nodes.Node.StatsResourcesDatas.StatsResourcesData.CntrEngine))])
                            self._leafs = OrderedDict([
                                ('resource', (YLeaf(YType.enumeration, 'resource'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper', 'Resource', '')])),
                                ('sys_cp_cnfg_prof', (YLeaf(YType.uint32, 'sys-cp-cnfg-prof'), ['int'])),
                                ('next_avail_cp_id', (YLeaf(YType.uint32, 'next-avail-cp-id'), ['int'])),
                                ('num_cntr_engines', (YLeaf(YType.uint32, 'num-cntr-engines'), ['int'])),
                            ])
                            self.resource = None
                            self.sys_cp_cnfg_prof = None
                            self.next_avail_cp_id = None
                            self.num_cntr_engines = None

                            self.cntr_engine = YList(self)
                            self._segment_path = lambda: "stats-resources-data" + "[resource='" + str(self.resource) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dpa.Stats.Nodes.Node.StatsResourcesDatas.StatsResourcesData, ['resource', u'sys_cp_cnfg_prof', u'next_avail_cp_id', u'num_cntr_engines'], name, value)


                        class CntrEngine(Entity):
                            """
                            cntr engine
                            
                            .. attribute:: state
                            
                            	state
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: core_id
                            
                            	core id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: apps_info
                            
                            	apps info
                            	**type**\: list of  		 :py:class:`AppsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.StatsResourcesDatas.StatsResourcesData.CntrEngine.AppsInfo>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dpa.Stats.Nodes.Node.StatsResourcesDatas.StatsResourcesData.CntrEngine, self).__init__()

                                self.yang_name = "cntr-engine"
                                self.yang_parent_name = "stats-resources-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("apps-info", ("apps_info", Dpa.Stats.Nodes.Node.StatsResourcesDatas.StatsResourcesData.CntrEngine.AppsInfo))])
                                self._leafs = OrderedDict([
                                    ('state', (YLeaf(YType.str, 'state'), ['str'])),
                                    ('core_id', (YLeaf(YType.uint32, 'core-id'), ['int'])),
                                ])
                                self.state = None
                                self.core_id = None

                                self.apps_info = YList(self)
                                self._segment_path = lambda: "cntr-engine"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dpa.Stats.Nodes.Node.StatsResourcesDatas.StatsResourcesData.CntrEngine, [u'state', u'core_id'], name, value)


                            class AppsInfo(Entity):
                                """
                                apps info
                                
                                .. attribute:: app_type
                                
                                	app type
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: num_cntrs_for_app
                                
                                	num cntrs for app
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: num_cntrs_used
                                
                                	num cntrs used
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.StatsResourcesDatas.StatsResourcesData.CntrEngine.AppsInfo, self).__init__()

                                    self.yang_name = "apps-info"
                                    self.yang_parent_name = "cntr-engine"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('app_type', (YLeaf(YType.str, 'app-type'), ['str'])),
                                        ('num_cntrs_for_app', (YLeaf(YType.uint32, 'num-cntrs-for-app'), ['int'])),
                                        ('num_cntrs_used', (YLeaf(YType.uint32, 'num-cntrs-used'), ['int'])),
                                    ])
                                    self.app_type = None
                                    self.num_cntrs_for_app = None
                                    self.num_cntrs_used = None
                                    self._segment_path = lambda: "apps-info"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.StatsResourcesDatas.StatsResourcesData.CntrEngine.AppsInfo, [u'app_type', u'num_cntrs_for_app', u'num_cntrs_used'], name, value)






                class HwResourcesDatas(Entity):
                    """
                    OFA hw resources stats 
                    
                    .. attribute:: hw_resources_data
                    
                    	Hardware resources table
                    	**type**\: list of  		 :py:class:`HwResourcesData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dpa.Stats.Nodes.Node.HwResourcesDatas, self).__init__()

                        self.yang_name = "hw-resources-datas"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("hw-resources-data", ("hw_resources_data", Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData))])
                        self._leafs = OrderedDict()

                        self.hw_resources_data = YList(self)
                        self._segment_path = lambda: "hw-resources-datas"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dpa.Stats.Nodes.Node.HwResourcesDatas, [], name, value)


                    class HwResourcesData(Entity):
                        """
                        Hardware resources table
                        
                        .. attribute:: resource  (key)
                        
                        	Resource type
                        	**type**\:  :py:class:`Resource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Resource>`
                        
                        	**config**\: False
                        
                        .. attribute:: resource_id
                        
                        	resource id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: name
                        
                        	name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: num_npus
                        
                        	num npus
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: cmd_invalid
                        
                        	cmd invalid
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: npu_hwr
                        
                        	npu hwr
                        	**type**\: list of  		 :py:class:`NpuHwr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData.NpuHwr>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData, self).__init__()

                            self.yang_name = "hw-resources-data"
                            self.yang_parent_name = "hw-resources-datas"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['resource']
                            self._child_classes = OrderedDict([("npu-hwr", ("npu_hwr", Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData.NpuHwr))])
                            self._leafs = OrderedDict([
                                ('resource', (YLeaf(YType.enumeration, 'resource'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper', 'Resource', '')])),
                                ('resource_id', (YLeaf(YType.uint32, 'resource-id'), ['int'])),
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('num_npus', (YLeaf(YType.uint32, 'num-npus'), ['int'])),
                                ('cmd_invalid', (YLeaf(YType.boolean, 'cmd-invalid'), ['bool'])),
                            ])
                            self.resource = None
                            self.resource_id = None
                            self.name = None
                            self.num_npus = None
                            self.cmd_invalid = None

                            self.npu_hwr = YList(self)
                            self._segment_path = lambda: "hw-resources-data" + "[resource='" + str(self.resource) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData, ['resource', u'resource_id', u'name', u'num_npus', u'cmd_invalid'], name, value)


                        class NpuHwr(Entity):
                            """
                            npu hwr
                            
                            .. attribute:: max_allowed
                            
                            	max allowed
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: npu_id
                            
                            	npu id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: max_entries
                            
                            	max entries
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: red_oor_threshold
                            
                            	red oor threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: red_oor_threshold_percent
                            
                            	red oor threshold percent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: yellow_oor_threshold
                            
                            	yellow oor threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: yellow_oor_threshold_percent
                            
                            	yellow oor threshold percent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: inuse_objects
                            
                            	inuse objects
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: num_lt
                            
                            	num lt
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: oor_change_count
                            
                            	oor change count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: oor_state_change_time1
                            
                            	oor state change time1
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: oor_state_change_time2
                            
                            	oor state change time2
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: oor_state
                            
                            	oor state
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: lt_hwr
                            
                            	lt hwr
                            	**type**\: list of  		 :py:class:`LtHwr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_hw_resources_oper.Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData.NpuHwr.LtHwr>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData.NpuHwr, self).__init__()

                                self.yang_name = "npu-hwr"
                                self.yang_parent_name = "hw-resources-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("lt-hwr", ("lt_hwr", Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData.NpuHwr.LtHwr))])
                                self._leafs = OrderedDict([
                                    ('max_allowed', (YLeaf(YType.uint32, 'max-allowed'), ['int'])),
                                    ('npu_id', (YLeaf(YType.uint32, 'npu-id'), ['int'])),
                                    ('max_entries', (YLeaf(YType.uint32, 'max-entries'), ['int'])),
                                    ('red_oor_threshold', (YLeaf(YType.uint32, 'red-oor-threshold'), ['int'])),
                                    ('red_oor_threshold_percent', (YLeaf(YType.uint32, 'red-oor-threshold-percent'), ['int'])),
                                    ('yellow_oor_threshold', (YLeaf(YType.uint32, 'yellow-oor-threshold'), ['int'])),
                                    ('yellow_oor_threshold_percent', (YLeaf(YType.uint32, 'yellow-oor-threshold-percent'), ['int'])),
                                    ('inuse_objects', (YLeaf(YType.uint32, 'inuse-objects'), ['int'])),
                                    ('num_lt', (YLeaf(YType.uint32, 'num-lt'), ['int'])),
                                    ('oor_change_count', (YLeaf(YType.uint32, 'oor-change-count'), ['int'])),
                                    ('oor_state_change_time1', (YLeaf(YType.str, 'oor-state-change-time1'), ['str'])),
                                    ('oor_state_change_time2', (YLeaf(YType.str, 'oor-state-change-time2'), ['str'])),
                                    ('oor_state', (YLeaf(YType.str, 'oor-state'), ['str'])),
                                ])
                                self.max_allowed = None
                                self.npu_id = None
                                self.max_entries = None
                                self.red_oor_threshold = None
                                self.red_oor_threshold_percent = None
                                self.yellow_oor_threshold = None
                                self.yellow_oor_threshold_percent = None
                                self.inuse_objects = None
                                self.num_lt = None
                                self.oor_change_count = None
                                self.oor_state_change_time1 = None
                                self.oor_state_change_time2 = None
                                self.oor_state = None

                                self.lt_hwr = YList(self)
                                self._segment_path = lambda: "npu-hwr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData.NpuHwr, [u'max_allowed', u'npu_id', u'max_entries', u'red_oor_threshold', u'red_oor_threshold_percent', u'yellow_oor_threshold', u'yellow_oor_threshold_percent', u'inuse_objects', u'num_lt', u'oor_change_count', u'oor_state_change_time1', u'oor_state_change_time2', u'oor_state'], name, value)


                            class LtHwr(Entity):
                                """
                                lt hwr
                                
                                .. attribute:: lt_id
                                
                                	lt id
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: name
                                
                                	name
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: hw_entries
                                
                                	hw entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: sw_entries
                                
                                	sw entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-hw-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData.NpuHwr.LtHwr, self).__init__()

                                    self.yang_name = "lt-hwr"
                                    self.yang_parent_name = "npu-hwr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('lt_id', (YLeaf(YType.uint32, 'lt-id'), ['int'])),
                                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                        ('hw_entries', (YLeaf(YType.uint32, 'hw-entries'), ['int'])),
                                        ('sw_entries', (YLeaf(YType.uint32, 'sw-entries'), ['int'])),
                                    ])
                                    self.lt_id = None
                                    self.name = None
                                    self.hw_entries = None
                                    self.sw_entries = None
                                    self._segment_path = lambda: "lt-hwr"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.HwResourcesDatas.HwResourcesData.NpuHwr.LtHwr, [u'lt_id', u'name', u'hw_entries', u'sw_entries'], name, value)








    def clone_ptr(self):
        self._top_entity = Dpa()
        return self._top_entity



