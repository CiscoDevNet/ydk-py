""" Cisco_IOS_XR_asr9k_fsi_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-fsi package operational data.

This module contains definitions
for the following management objects\:
  fabric\-stats\: Fabric stats operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FabricStats(Entity):
    """
    Fabric stats operational data
    
    .. attribute:: nodes
    
    	Table of Nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper.FabricStats.Nodes>`
    
    

    """

    _prefix = 'asr9k-fsi-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(FabricStats, self).__init__()
        self._top_entity = None

        self.yang_name = "fabric-stats"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-fsi-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", FabricStats.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = FabricStats.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-fsi-oper:fabric-stats"


    class Nodes(Entity):
        """
        Table of Nodes
        
        .. attribute:: node
        
        	Information about a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper.FabricStats.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-fsi-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(FabricStats.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "fabric-stats"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", FabricStats.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-fsi-oper:fabric-stats/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(FabricStats.Nodes, [], name, value)


        class Node(Entity):
            """
            Information about a particular node
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: statses
            
            	Table of stats information
            	**type**\:  :py:class:`Statses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper.FabricStats.Nodes.Node.Statses>`
            
            

            """

            _prefix = 'asr9k-fsi-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(FabricStats.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_container_classes = OrderedDict([("statses", ("statses", FabricStats.Nodes.Node.Statses))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                ])
                self.node_name = None

                self.statses = FabricStats.Nodes.Node.Statses()
                self.statses.parent = self
                self._children_name_map["statses"] = "statses"
                self._children_yang_names.add("statses")
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-fsi-oper:fabric-stats/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(FabricStats.Nodes.Node, ['node_name'], name, value)


            class Statses(Entity):
                """
                Table of stats information
                
                .. attribute:: stats
                
                	Stats information for a particular type
                	**type**\: list of  		 :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper.FabricStats.Nodes.Node.Statses.Stats>`
                
                

                """

                _prefix = 'asr9k-fsi-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FabricStats.Nodes.Node.Statses, self).__init__()

                    self.yang_name = "statses"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("stats", ("stats", FabricStats.Nodes.Node.Statses.Stats))])
                    self._leafs = OrderedDict()

                    self.stats = YList(self)
                    self._segment_path = lambda: "statses"

                def __setattr__(self, name, value):
                    self._perform_setattr(FabricStats.Nodes.Node.Statses, [], name, value)


                class Stats(Entity):
                    """
                    Stats information for a particular type
                    
                    .. attribute:: type  (key)
                    
                    	Fabric asic type
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: last_clear_time
                    
                    	Last Clear Time
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: stat_table_name
                    
                    	Stat Table Name
                    	**type**\: str
                    
                    .. attribute:: stats_table
                    
                    	Array of counters 
                    	**type**\: list of  		 :py:class:`StatsTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper.FabricStats.Nodes.Node.Statses.Stats.StatsTable>`
                    
                    

                    """

                    _prefix = 'asr9k-fsi-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FabricStats.Nodes.Node.Statses.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "statses"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['type']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("stats-table", ("stats_table", FabricStats.Nodes.Node.Statses.Stats.StatsTable))])
                        self._leafs = OrderedDict([
                            ('type', YLeaf(YType.str, 'type')),
                            ('last_clear_time', YLeaf(YType.uint64, 'last-clear-time')),
                            ('stat_table_name', YLeaf(YType.str, 'stat-table-name')),
                        ])
                        self.type = None
                        self.last_clear_time = None
                        self.stat_table_name = None

                        self.stats_table = YList(self)
                        self._segment_path = lambda: "stats" + "[type='" + str(self.type) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(FabricStats.Nodes.Node.Statses.Stats, ['type', 'last_clear_time', 'stat_table_name'], name, value)


                    class StatsTable(Entity):
                        """
                        Array of counters 
                        
                        .. attribute:: fsi_stat
                        
                        	Stats Table
                        	**type**\: list of  		 :py:class:`FsiStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper.FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat>`
                        
                        

                        """

                        _prefix = 'asr9k-fsi-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FabricStats.Nodes.Node.Statses.Stats.StatsTable, self).__init__()

                            self.yang_name = "stats-table"
                            self.yang_parent_name = "stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("fsi-stat", ("fsi_stat", FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat))])
                            self._leafs = OrderedDict()

                            self.fsi_stat = YList(self)
                            self._segment_path = lambda: "stats-table"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FabricStats.Nodes.Node.Statses.Stats.StatsTable, [], name, value)


                        class FsiStat(Entity):
                            """
                            Stats Table
                            
                            .. attribute:: count
                            
                            	Counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: counter_name
                            
                            	Counter Name
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'asr9k-fsi-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat, self).__init__()

                                self.yang_name = "fsi-stat"
                                self.yang_parent_name = "stats-table"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('count', YLeaf(YType.uint64, 'count')),
                                    ('counter_name', YLeaf(YType.str, 'counter-name')),
                                ])
                                self.count = None
                                self.counter_name = None
                                self._segment_path = lambda: "fsi-stat"

                            def __setattr__(self, name, value):
                                self._perform_setattr(FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat, ['count', 'counter_name'], name, value)

    def clone_ptr(self):
        self._top_entity = FabricStats()
        return self._top_entity

