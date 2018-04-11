""" Cisco_IOS_XR_asr9k_asic_errors_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-asic\-errors package operational data.

This module contains definitions
for the following management objects\:
  asic\-error\-stats\: Asic error stats operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AsicErrorStats(Entity):
    """
    Asic error stats operational data
    
    .. attribute:: racks
    
    	Table of racks
    	**type**\:  :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper.AsicErrorStats.Racks>`
    
    

    """

    _prefix = 'asr9k-asic-errors-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(AsicErrorStats, self).__init__()
        self._top_entity = None

        self.yang_name = "asic-error-stats"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-asic-errors-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("racks", ("racks", AsicErrorStats.Racks))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.racks = AsicErrorStats.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"
        self._children_yang_names.add("racks")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-asic-errors-oper:asic-error-stats"


    class Racks(Entity):
        """
        Table of racks
        
        .. attribute:: rack
        
        	Number
        	**type**\: list of  		 :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper.AsicErrorStats.Racks.Rack>`
        
        

        """

        _prefix = 'asr9k-asic-errors-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(AsicErrorStats.Racks, self).__init__()

            self.yang_name = "racks"
            self.yang_parent_name = "asic-error-stats"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rack", ("rack", AsicErrorStats.Racks.Rack))])
            self._leafs = OrderedDict()

            self.rack = YList(self)
            self._segment_path = lambda: "racks"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-asic-errors-oper:asic-error-stats/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(AsicErrorStats.Racks, [], name, value)


        class Rack(Entity):
            """
            Number
            
            .. attribute:: rack  (key)
            
            	Rack number
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: nodes
            
            	Table of Nodes
            	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper.AsicErrorStats.Racks.Rack.Nodes>`
            
            

            """

            _prefix = 'asr9k-asic-errors-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(AsicErrorStats.Racks.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "racks"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rack']
                self._child_container_classes = OrderedDict([("nodes", ("nodes", AsicErrorStats.Racks.Rack.Nodes))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rack', YLeaf(YType.int32, 'rack')),
                ])
                self.rack = None

                self.nodes = AsicErrorStats.Racks.Rack.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
                self._children_yang_names.add("nodes")
                self._segment_path = lambda: "rack" + "[rack='" + str(self.rack) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-asic-errors-oper:asic-error-stats/racks/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrorStats.Racks.Rack, ['rack'], name, value)


            class Nodes(Entity):
                """
                Table of Nodes
                
                .. attribute:: node
                
                	Information about a particular node
                	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper.AsicErrorStats.Racks.Rack.Nodes.Node>`
                
                

                """

                _prefix = 'asr9k-asic-errors-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AsicErrorStats.Racks.Rack.Nodes, self).__init__()

                    self.yang_name = "nodes"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("node", ("node", AsicErrorStats.Racks.Rack.Nodes.Node))])
                    self._leafs = OrderedDict()

                    self.node = YList(self)
                    self._segment_path = lambda: "nodes"

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrorStats.Racks.Rack.Nodes, [], name, value)


                class Node(Entity):
                    """
                    Information about a particular node
                    
                    .. attribute:: node_name  (key)
                    
                    	Node name
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: counts
                    
                    	Table of all Asic Types information on a node
                    	**type**\:  :py:class:`Counts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper.AsicErrorStats.Racks.Rack.Nodes.Node.Counts>`
                    
                    

                    """

                    _prefix = 'asr9k-asic-errors-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AsicErrorStats.Racks.Rack.Nodes.Node, self).__init__()

                        self.yang_name = "node"
                        self.yang_parent_name = "nodes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['node_name']
                        self._child_container_classes = OrderedDict([("counts", ("counts", AsicErrorStats.Racks.Rack.Nodes.Node.Counts))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('node_name', YLeaf(YType.str, 'node-name')),
                        ])
                        self.node_name = None

                        self.counts = AsicErrorStats.Racks.Rack.Nodes.Node.Counts()
                        self.counts.parent = self
                        self._children_name_map["counts"] = "counts"
                        self._children_yang_names.add("counts")
                        self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrorStats.Racks.Rack.Nodes.Node, ['node_name'], name, value)


                    class Counts(Entity):
                        """
                        Table of all Asic Types information on a
                        node
                        
                        .. attribute:: count
                        
                        	Summary Asic error counts for a Asic Type
                        	**type**\: list of  		 :py:class:`Count <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper.AsicErrorStats.Racks.Rack.Nodes.Node.Counts.Count>`
                        
                        

                        """

                        _prefix = 'asr9k-asic-errors-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AsicErrorStats.Racks.Rack.Nodes.Node.Counts, self).__init__()

                            self.yang_name = "counts"
                            self.yang_parent_name = "node"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("count", ("count", AsicErrorStats.Racks.Rack.Nodes.Node.Counts.Count))])
                            self._leafs = OrderedDict()

                            self.count = YList(self)
                            self._segment_path = lambda: "counts"

                        def __setattr__(self, name, value):
                            self._perform_setattr(AsicErrorStats.Racks.Rack.Nodes.Node.Counts, [], name, value)


                        class Count(Entity):
                            """
                            Summary Asic error counts for a Asic Type
                            
                            .. attribute:: type  (key)
                            
                            	Asic Type
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: sum_data
                            
                            	sum data
                            	**type**\: list of  		 :py:class:`SumData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper.AsicErrorStats.Racks.Rack.Nodes.Node.Counts.Count.SumData>`
                            
                            

                            """

                            _prefix = 'asr9k-asic-errors-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AsicErrorStats.Racks.Rack.Nodes.Node.Counts.Count, self).__init__()

                                self.yang_name = "count"
                                self.yang_parent_name = "counts"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['type']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("sum-data", ("sum_data", AsicErrorStats.Racks.Rack.Nodes.Node.Counts.Count.SumData))])
                                self._leafs = OrderedDict([
                                    ('type', YLeaf(YType.str, 'type')),
                                ])
                                self.type = None

                                self.sum_data = YList(self)
                                self._segment_path = lambda: "count" + "[type='" + str(self.type) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(AsicErrorStats.Racks.Rack.Nodes.Node.Counts.Count, ['type'], name, value)


                            class SumData(Entity):
                                """
                                sum data
                                
                                .. attribute:: instance
                                
                                	instance
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: num_nodes
                                
                                	num nodes
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: crc_err_count
                                
                                	crc err count
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: sbe_err_count
                                
                                	sbe err count
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: mbe_err_count
                                
                                	mbe err count
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: par_err_count
                                
                                	par err count
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: gen_err_count
                                
                                	gen err count
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: reset_err_count
                                
                                	reset err count
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: node_key
                                
                                	node key
                                	**type**\: list of int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-asic-errors-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AsicErrorStats.Racks.Rack.Nodes.Node.Counts.Count.SumData, self).__init__()

                                    self.yang_name = "sum-data"
                                    self.yang_parent_name = "count"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('instance', YLeaf(YType.uint32, 'instance')),
                                        ('num_nodes', YLeaf(YType.uint32, 'num-nodes')),
                                        ('crc_err_count', YLeaf(YType.uint32, 'crc-err-count')),
                                        ('sbe_err_count', YLeaf(YType.uint32, 'sbe-err-count')),
                                        ('mbe_err_count', YLeaf(YType.uint32, 'mbe-err-count')),
                                        ('par_err_count', YLeaf(YType.uint32, 'par-err-count')),
                                        ('gen_err_count', YLeaf(YType.uint32, 'gen-err-count')),
                                        ('reset_err_count', YLeaf(YType.uint32, 'reset-err-count')),
                                        ('node_key', YLeafList(YType.uint32, 'node-key')),
                                    ])
                                    self.instance = None
                                    self.num_nodes = None
                                    self.crc_err_count = None
                                    self.sbe_err_count = None
                                    self.mbe_err_count = None
                                    self.par_err_count = None
                                    self.gen_err_count = None
                                    self.reset_err_count = None
                                    self.node_key = []
                                    self._segment_path = lambda: "sum-data"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrorStats.Racks.Rack.Nodes.Node.Counts.Count.SumData, ['instance', 'num_nodes', 'crc_err_count', 'sbe_err_count', 'mbe_err_count', 'par_err_count', 'gen_err_count', 'reset_err_count', 'node_key'], name, value)

    def clone_ptr(self):
        self._top_entity = AsicErrorStats()
        return self._top_entity

