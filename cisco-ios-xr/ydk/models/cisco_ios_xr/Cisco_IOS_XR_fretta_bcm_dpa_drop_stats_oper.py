""" Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fretta\-bcm\-dpa\-drop\-stats package operational data.

This module contains definitions
for the following management objects\:
  drop\: Drop stats data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Drop(Entity):
    """
    Drop stats data
    
    .. attribute:: nodes
    
    	Drop data per node
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper.Drop.Nodes>`
    
    

    """

    _prefix = 'fretta-bcm-dpa-drop-stats-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Drop, self).__init__()
        self._top_entity = None

        self.yang_name = "drop"
        self.yang_parent_name = "Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Drop.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Drop.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper:drop"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Drop, [], name, value)


    class Nodes(Entity):
        """
        Drop data per node
        
        .. attribute:: node
        
        	Drop stats data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper.Drop.Nodes.Node>`
        
        

        """

        _prefix = 'fretta-bcm-dpa-drop-stats-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Drop.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "drop"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Drop.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper:drop/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Drop.Nodes, [], name, value)


        class Node(Entity):
            """
            Drop stats data for a particular node
            
            .. attribute:: node_name  (key)
            
            	Node ID
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: npu_number_for_drop_stats
            
            	NPU drop stats
            	**type**\:  :py:class:`NpuNumberForDropStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper.Drop.Nodes.Node.NpuNumberForDropStats>`
            
            

            """

            _prefix = 'fretta-bcm-dpa-drop-stats-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Drop.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("npu-number-for-drop-stats", ("npu_number_for_drop_stats", Drop.Nodes.Node.NpuNumberForDropStats))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.npu_number_for_drop_stats = Drop.Nodes.Node.NpuNumberForDropStats()
                self.npu_number_for_drop_stats.parent = self
                self._children_name_map["npu_number_for_drop_stats"] = "npu-number-for-drop-stats"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper:drop/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Drop.Nodes.Node, ['node_name'], name, value)


            class NpuNumberForDropStats(Entity):
                """
                NPU drop stats
                
                .. attribute:: npu_number_for_drop_stat
                
                	All drop stats for a particular NPU
                	**type**\: list of  		 :py:class:`NpuNumberForDropStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper.Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat>`
                
                

                """

                _prefix = 'fretta-bcm-dpa-drop-stats-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Drop.Nodes.Node.NpuNumberForDropStats, self).__init__()

                    self.yang_name = "npu-number-for-drop-stats"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("npu-number-for-drop-stat", ("npu_number_for_drop_stat", Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat))])
                    self._leafs = OrderedDict()

                    self.npu_number_for_drop_stat = YList(self)
                    self._segment_path = lambda: "npu-number-for-drop-stats"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Drop.Nodes.Node.NpuNumberForDropStats, [], name, value)


                class NpuNumberForDropStat(Entity):
                    """
                    All drop stats for a particular NPU
                    
                    .. attribute:: npu_id  (key)
                    
                    	NPU number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: drop_specific_stats_data
                    
                    	Second argument to the module
                    	**type**\: list of  		 :py:class:`DropSpecificStatsData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper.Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat.DropSpecificStatsData>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-drop-stats-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat, self).__init__()

                        self.yang_name = "npu-number-for-drop-stat"
                        self.yang_parent_name = "npu-number-for-drop-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['npu_id']
                        self._child_classes = OrderedDict([("drop-specific-stats-data", ("drop_specific_stats_data", Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat.DropSpecificStatsData))])
                        self._leafs = OrderedDict([
                            ('npu_id', (YLeaf(YType.uint32, 'npu-id'), ['int'])),
                        ])
                        self.npu_id = None

                        self.drop_specific_stats_data = YList(self)
                        self._segment_path = lambda: "npu-number-for-drop-stat" + "[npu-id='" + str(self.npu_id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat, ['npu_id'], name, value)


                    class DropSpecificStatsData(Entity):
                        """
                        Second argument to the module
                        
                        .. attribute:: drop_data  (key)
                        
                        	Drop ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: id
                        
                        	id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	name
                        	**type**\: str
                        
                        .. attribute:: count
                        
                        	count
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-drop-stats-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat.DropSpecificStatsData, self).__init__()

                            self.yang_name = "drop-specific-stats-data"
                            self.yang_parent_name = "npu-number-for-drop-stat"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['drop_data']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('drop_data', (YLeaf(YType.uint32, 'drop-data'), ['int'])),
                                ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('count', (YLeaf(YType.uint64, 'count'), ['int'])),
                            ])
                            self.drop_data = None
                            self.id = None
                            self.name = None
                            self.count = None
                            self._segment_path = lambda: "drop-specific-stats-data" + "[drop-data='" + str(self.drop_data) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat.DropSpecificStatsData, ['drop_data', 'id', 'name', 'count'], name, value)

    def clone_ptr(self):
        self._top_entity = Drop()
        return self._top_entity

