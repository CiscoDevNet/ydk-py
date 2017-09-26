""" Cisco_IOS_XR_fretta_bcm_dpa_resources_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fretta\-bcm\-dpa\-resources package operational data.

This module contains definitions
for the following management objects\:
  dpa\: Stats Data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Dpa(Entity):
    """
    Stats Data
    
    .. attribute:: resources
    
    	DPA Resources Data
    	**type**\:   :py:class:`Resources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources>`
    
    .. attribute:: stats
    
    	Voq or Trap Data
    	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats>`
    
    

    """

    _prefix = 'fretta-bcm-dpa-resources-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Dpa, self).__init__()
        self._top_entity = None

        self.yang_name = "dpa"
        self.yang_parent_name = "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"resources" : ("resources", Dpa.Resources), "stats" : ("stats", Dpa.Stats)}
        self._child_list_classes = {}

        self.resources = Dpa.Resources()
        self.resources.parent = self
        self._children_name_map["resources"] = "resources"
        self._children_yang_names.add("resources")

        self.stats = Dpa.Stats()
        self.stats.parent = self
        self._children_name_map["stats"] = "stats"
        self._children_yang_names.add("stats")
        self._segment_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa"


    class Resources(Entity):
        """
        DPA Resources Data
        
        .. attribute:: nodes
        
        	DPA data for available nodes
        	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes>`
        
        

        """

        _prefix = 'fretta-bcm-dpa-resources-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Dpa.Resources, self).__init__()

            self.yang_name = "resources"
            self.yang_parent_name = "dpa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"nodes" : ("nodes", Dpa.Resources.Nodes)}
            self._child_list_classes = {}

            self.nodes = Dpa.Resources.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"
            self._children_yang_names.add("nodes")
            self._segment_path = lambda: "resources"
            self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/%s" % self._segment_path()


        class Nodes(Entity):
            """
            DPA data for available nodes
            
            .. attribute:: node
            
            	DPA operational data for a particular node
            	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes.Node>`
            
            

            """

            _prefix = 'fretta-bcm-dpa-resources-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Dpa.Resources.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "resources"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"node" : ("node", Dpa.Resources.Nodes.Node)}

                self.node = YList(self)
                self._segment_path = lambda: "nodes"
                self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/resources/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Dpa.Resources.Nodes, [], name, value)


            class Node(Entity):
                """
                DPA operational data for a particular node
                
                .. attribute:: node_name  <key>
                
                	Node ID
                	**type**\:  str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: table_datas
                
                	DPA Resources table
                	**type**\:   :py:class:`TableDatas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes.Node.TableDatas>`
                
                

                """

                _prefix = 'fretta-bcm-dpa-resources-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dpa.Resources.Nodes.Node, self).__init__()

                    self.yang_name = "node"
                    self.yang_parent_name = "nodes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"table-datas" : ("table_datas", Dpa.Resources.Nodes.Node.TableDatas)}
                    self._child_list_classes = {}

                    self.node_name = YLeaf(YType.str, "node-name")

                    self.table_datas = Dpa.Resources.Nodes.Node.TableDatas()
                    self.table_datas.parent = self
                    self._children_name_map["table_datas"] = "table-datas"
                    self._children_yang_names.add("table-datas")
                    self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/resources/nodes/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Dpa.Resources.Nodes.Node, ['node_name'], name, value)


                class TableDatas(Entity):
                    """
                    DPA Resources table
                    
                    .. attribute:: table_data
                    
                    	Resources table
                    	**type**\: list of    :py:class:`TableData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes.Node.TableDatas.TableData>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dpa.Resources.Nodes.Node.TableDatas, self).__init__()

                        self.yang_name = "table-datas"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"table-data" : ("table_data", Dpa.Resources.Nodes.Node.TableDatas.TableData)}

                        self.table_data = YList(self)
                        self._segment_path = lambda: "table-datas"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dpa.Resources.Nodes.Node.TableDatas, [], name, value)


                    class TableData(Entity):
                        """
                        Resources table
                        
                        .. attribute:: resource  <key>
                        
                        	Resource type
                        	**type**\:  int
                        
                        	**range:** 0..124
                        
                        .. attribute:: is_global
                        
                        	is global
                        	**type**\:  bool
                        
                        .. attribute:: name
                        
                        	name
                        	**type**\:  str
                        
                        	**length:** 0..64
                        
                        .. attribute:: npu_tblr
                        
                        	npu tblr
                        	**type**\: list of    :py:class:`NpuTblr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes.Node.TableDatas.TableData.NpuTblr>`
                        
                        .. attribute:: num_npus
                        
                        	num npus
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: table_id
                        
                        	table id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: table_specific_list
                        
                        	table specific list
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dpa.Resources.Nodes.Node.TableDatas.TableData, self).__init__()

                            self.yang_name = "table-data"
                            self.yang_parent_name = "table-datas"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"npu-tblr" : ("npu_tblr", Dpa.Resources.Nodes.Node.TableDatas.TableData.NpuTblr)}

                            self.resource = YLeaf(YType.uint32, "resource")

                            self.is_global = YLeaf(YType.boolean, "is-global")

                            self.name = YLeaf(YType.str, "name")

                            self.num_npus = YLeaf(YType.uint32, "num-npus")

                            self.table_id = YLeaf(YType.uint32, "table-id")

                            self.table_specific_list = YLeaf(YType.str, "table-specific-list")

                            self.npu_tblr = YList(self)
                            self._segment_path = lambda: "table-data" + "[resource='" + self.resource.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dpa.Resources.Nodes.Node.TableDatas.TableData, ['resource', 'is_global', 'name', 'num_npus', 'table_id', 'table_specific_list'], name, value)


                        class NpuTblr(Entity):
                            """
                            npu tblr
                            
                            .. attribute:: create_ok
                            
                            	create ok
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: create_req
                            
                            	create req
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: delete_ok
                            
                            	delete ok
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: delete_req
                            
                            	delete req
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: eod_ok
                            
                            	eod ok
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: eod_req
                            
                            	eod req
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: err_db_exists
                            
                            	err db exists
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: err_db_nomem
                            
                            	err db nomem
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: err_db_notfound
                            
                            	err db notfound
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: err_hw_fail
                            
                            	err hw fail
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: err_ref_resolve
                            
                            	err ref resolve
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: npu_id
                            
                            	npu id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: num_objs
                            
                            	num objs
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: update_ok
                            
                            	update ok
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: update_req
                            
                            	update req
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dpa.Resources.Nodes.Node.TableDatas.TableData.NpuTblr, self).__init__()

                                self.yang_name = "npu-tblr"
                                self.yang_parent_name = "table-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.create_ok = YLeaf(YType.uint32, "create-ok")

                                self.create_req = YLeaf(YType.uint32, "create-req")

                                self.delete_ok = YLeaf(YType.uint32, "delete-ok")

                                self.delete_req = YLeaf(YType.uint32, "delete-req")

                                self.eod_ok = YLeaf(YType.uint32, "eod-ok")

                                self.eod_req = YLeaf(YType.uint32, "eod-req")

                                self.err_db_exists = YLeaf(YType.uint32, "err-db-exists")

                                self.err_db_nomem = YLeaf(YType.uint32, "err-db-nomem")

                                self.err_db_notfound = YLeaf(YType.uint32, "err-db-notfound")

                                self.err_hw_fail = YLeaf(YType.uint32, "err-hw-fail")

                                self.err_ref_resolve = YLeaf(YType.uint32, "err-ref-resolve")

                                self.npu_id = YLeaf(YType.uint32, "npu-id")

                                self.num_objs = YLeaf(YType.uint32, "num-objs")

                                self.update_ok = YLeaf(YType.uint32, "update-ok")

                                self.update_req = YLeaf(YType.uint32, "update-req")
                                self._segment_path = lambda: "npu-tblr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dpa.Resources.Nodes.Node.TableDatas.TableData.NpuTblr, ['create_ok', 'create_req', 'delete_ok', 'delete_req', 'eod_ok', 'eod_req', 'err_db_exists', 'err_db_nomem', 'err_db_notfound', 'err_hw_fail', 'err_ref_resolve', 'npu_id', 'num_objs', 'update_ok', 'update_req'], name, value)


    class Stats(Entity):
        """
        Voq or Trap Data
        
        .. attribute:: nodes
        
        	DPA data for available nodes
        	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes>`
        
        

        """

        _prefix = 'fretta-bcm-dpa-resources-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Dpa.Stats, self).__init__()

            self.yang_name = "stats"
            self.yang_parent_name = "dpa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"nodes" : ("nodes", Dpa.Stats.Nodes)}
            self._child_list_classes = {}

            self.nodes = Dpa.Stats.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"
            self._children_yang_names.add("nodes")
            self._segment_path = lambda: "stats"
            self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/%s" % self._segment_path()


        class Nodes(Entity):
            """
            DPA data for available nodes
            
            .. attribute:: node
            
            	DPA operational data for a particular node
            	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node>`
            
            

            """

            _prefix = 'fretta-bcm-dpa-resources-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Dpa.Stats.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "stats"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"node" : ("node", Dpa.Stats.Nodes.Node)}

                self.node = YList(self)
                self._segment_path = lambda: "nodes"
                self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/stats/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Dpa.Stats.Nodes, [], name, value)


            class Node(Entity):
                """
                DPA operational data for a particular node
                
                .. attribute:: node_name  <key>
                
                	Node ID
                	**type**\:  str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: asic_statistics
                
                	ASIC statistics table
                	**type**\:   :py:class:`AsicStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics>`
                
                .. attribute:: npu_numbers
                
                	Ingress Stats
                	**type**\:   :py:class:`NpuNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers>`
                
                

                """

                _prefix = 'fretta-bcm-dpa-resources-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dpa.Stats.Nodes.Node, self).__init__()

                    self.yang_name = "node"
                    self.yang_parent_name = "nodes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"asic-statistics" : ("asic_statistics", Dpa.Stats.Nodes.Node.AsicStatistics), "npu-numbers" : ("npu_numbers", Dpa.Stats.Nodes.Node.NpuNumbers)}
                    self._child_list_classes = {}

                    self.node_name = YLeaf(YType.str, "node-name")

                    self.asic_statistics = Dpa.Stats.Nodes.Node.AsicStatistics()
                    self.asic_statistics.parent = self
                    self._children_name_map["asic_statistics"] = "asic-statistics"
                    self._children_yang_names.add("asic-statistics")

                    self.npu_numbers = Dpa.Stats.Nodes.Node.NpuNumbers()
                    self.npu_numbers.parent = self
                    self._children_name_map["npu_numbers"] = "npu-numbers"
                    self._children_yang_names.add("npu-numbers")
                    self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/stats/nodes/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Dpa.Stats.Nodes.Node, ['node_name'], name, value)


                class AsicStatistics(Entity):
                    """
                    ASIC statistics table
                    
                    .. attribute:: asic_statistics_detail_for_npu_ids
                    
                    	Detailed ASIC statistics
                    	**type**\:   :py:class:`AsicStatisticsDetailForNpuIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds>`
                    
                    .. attribute:: asic_statistics_for_npu_ids
                    
                    	ASIC statistics
                    	**type**\:   :py:class:`AsicStatisticsForNpuIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dpa.Stats.Nodes.Node.AsicStatistics, self).__init__()

                        self.yang_name = "asic-statistics"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"asic-statistics-detail-for-npu-ids" : ("asic_statistics_detail_for_npu_ids", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds), "asic-statistics-for-npu-ids" : ("asic_statistics_for_npu_ids", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds)}
                        self._child_list_classes = {}

                        self.asic_statistics_detail_for_npu_ids = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds()
                        self.asic_statistics_detail_for_npu_ids.parent = self
                        self._children_name_map["asic_statistics_detail_for_npu_ids"] = "asic-statistics-detail-for-npu-ids"
                        self._children_yang_names.add("asic-statistics-detail-for-npu-ids")

                        self.asic_statistics_for_npu_ids = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds()
                        self.asic_statistics_for_npu_ids.parent = self
                        self._children_name_map["asic_statistics_for_npu_ids"] = "asic-statistics-for-npu-ids"
                        self._children_yang_names.add("asic-statistics-for-npu-ids")
                        self._segment_path = lambda: "asic-statistics"


                    class AsicStatisticsDetailForNpuIds(Entity):
                        """
                        Detailed ASIC statistics
                        
                        .. attribute:: asic_statistics_detail_for_npu_id
                        
                        	Detailed ASIC statistics for a particular NPU
                        	**type**\: list of    :py:class:`AsicStatisticsDetailForNpuId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId>`
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds, self).__init__()

                            self.yang_name = "asic-statistics-detail-for-npu-ids"
                            self.yang_parent_name = "asic-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"asic-statistics-detail-for-npu-id" : ("asic_statistics_detail_for_npu_id", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId)}

                            self.asic_statistics_detail_for_npu_id = YList(self)
                            self._segment_path = lambda: "asic-statistics-detail-for-npu-ids"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds, [], name, value)


                        class AsicStatisticsDetailForNpuId(Entity):
                            """
                            Detailed ASIC statistics for a particular
                            NPU
                            
                            .. attribute:: npu_id  <key>
                            
                            	NPU number
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: asic_instance
                            
                            	ASIC instance
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: chip_version
                            
                            	Chip version
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: rack_number
                            
                            	Rack number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: slot_number
                            
                            	Slot number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: statistics
                            
                            	Statistics
                            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics>`
                            
                            .. attribute:: valid
                            
                            	Flag to indicate if data is valid
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId, self).__init__()

                                self.yang_name = "asic-statistics-detail-for-npu-id"
                                self.yang_parent_name = "asic-statistics-detail-for-npu-ids"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"statistics" : ("statistics", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics)}
                                self._child_list_classes = {}

                                self.npu_id = YLeaf(YType.int32, "npu-id")

                                self.asic_instance = YLeaf(YType.uint32, "asic-instance")

                                self.chip_version = YLeaf(YType.uint16, "chip-version")

                                self.rack_number = YLeaf(YType.uint32, "rack-number")

                                self.slot_number = YLeaf(YType.uint32, "slot-number")

                                self.valid = YLeaf(YType.boolean, "valid")

                                self.statistics = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics()
                                self.statistics.parent = self
                                self._children_name_map["statistics"] = "statistics"
                                self._children_yang_names.add("statistics")
                                self._segment_path = lambda: "asic-statistics-detail-for-npu-id" + "[npu-id='" + self.npu_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId, ['npu_id', 'asic_instance', 'chip_version', 'rack_number', 'slot_number', 'valid'], name, value)


                            class Statistics(Entity):
                                """
                                Statistics
                                
                                .. attribute:: block_info
                                
                                	Block information
                                	**type**\: list of    :py:class:`BlockInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo>`
                                
                                .. attribute:: num_blocks
                                
                                	Number of blocks
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics, self).__init__()

                                    self.yang_name = "statistics"
                                    self.yang_parent_name = "asic-statistics-detail-for-npu-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"block-info" : ("block_info", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo)}

                                    self.num_blocks = YLeaf(YType.uint8, "num-blocks")

                                    self.block_info = YList(self)
                                    self._segment_path = lambda: "statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics, ['num_blocks'], name, value)


                                class BlockInfo(Entity):
                                    """
                                    Block information
                                    
                                    .. attribute:: block_name
                                    
                                    	Block name
                                    	**type**\:  str
                                    
                                    	**length:** 0..10
                                    
                                    .. attribute:: field_info
                                    
                                    	Field information
                                    	**type**\: list of    :py:class:`FieldInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo>`
                                    
                                    .. attribute:: num_fields
                                    
                                    	Number of fields
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'fretta-bcm-dpa-resources-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo, self).__init__()

                                        self.yang_name = "block-info"
                                        self.yang_parent_name = "statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"field-info" : ("field_info", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo)}

                                        self.block_name = YLeaf(YType.str, "block-name")

                                        self.num_fields = YLeaf(YType.uint8, "num-fields")

                                        self.field_info = YList(self)
                                        self._segment_path = lambda: "block-info"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo, ['block_name', 'num_fields'], name, value)


                                    class FieldInfo(Entity):
                                        """
                                        Field information
                                        
                                        .. attribute:: field_name
                                        
                                        	Field name
                                        	**type**\:  str
                                        
                                        	**length:** 0..80
                                        
                                        .. attribute:: field_value
                                        
                                        	Field value
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: is_overflow
                                        
                                        	Flag to indicate overflow
                                        	**type**\:  bool
                                        
                                        

                                        """

                                        _prefix = 'fretta-bcm-dpa-resources-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo, self).__init__()

                                            self.yang_name = "field-info"
                                            self.yang_parent_name = "block-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.field_name = YLeaf(YType.str, "field-name")

                                            self.field_value = YLeaf(YType.uint64, "field-value")

                                            self.is_overflow = YLeaf(YType.boolean, "is-overflow")
                                            self._segment_path = lambda: "field-info"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo, ['field_name', 'field_value', 'is_overflow'], name, value)


                    class AsicStatisticsForNpuIds(Entity):
                        """
                        ASIC statistics
                        
                        .. attribute:: asic_statistics_for_npu_id
                        
                        	ASIC statistics for a particular NPU
                        	**type**\: list of    :py:class:`AsicStatisticsForNpuId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId>`
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds, self).__init__()

                            self.yang_name = "asic-statistics-for-npu-ids"
                            self.yang_parent_name = "asic-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"asic-statistics-for-npu-id" : ("asic_statistics_for_npu_id", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId)}

                            self.asic_statistics_for_npu_id = YList(self)
                            self._segment_path = lambda: "asic-statistics-for-npu-ids"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds, [], name, value)


                        class AsicStatisticsForNpuId(Entity):
                            """
                            ASIC statistics for a particular NPU
                            
                            .. attribute:: npu_id  <key>
                            
                            	NPU number
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: asic_instance
                            
                            	ASIC instance
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: chip_version
                            
                            	Chip version
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: rack_number
                            
                            	Rack number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: slot_number
                            
                            	Slot number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: statistics
                            
                            	Statistics
                            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics>`
                            
                            .. attribute:: valid
                            
                            	Flag to indicate if data is valid
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId, self).__init__()

                                self.yang_name = "asic-statistics-for-npu-id"
                                self.yang_parent_name = "asic-statistics-for-npu-ids"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"statistics" : ("statistics", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics)}
                                self._child_list_classes = {}

                                self.npu_id = YLeaf(YType.int32, "npu-id")

                                self.asic_instance = YLeaf(YType.uint32, "asic-instance")

                                self.chip_version = YLeaf(YType.uint16, "chip-version")

                                self.rack_number = YLeaf(YType.uint32, "rack-number")

                                self.slot_number = YLeaf(YType.uint32, "slot-number")

                                self.valid = YLeaf(YType.boolean, "valid")

                                self.statistics = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics()
                                self.statistics.parent = self
                                self._children_name_map["statistics"] = "statistics"
                                self._children_yang_names.add("statistics")
                                self._segment_path = lambda: "asic-statistics-for-npu-id" + "[npu-id='" + self.npu_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId, ['npu_id', 'asic_instance', 'chip_version', 'rack_number', 'slot_number', 'valid'], name, value)


                            class Statistics(Entity):
                                """
                                Statistics
                                
                                .. attribute:: egq_deleted_pkt_cnt
                                
                                	EHP2PQP discarded packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_ehp_mc_high_discard_cnt
                                
                                	Number of multicast high packets discarded because multicast FIFO is full
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_ehp_mc_high_pkt_cnt
                                
                                	EHP2PQP multicast high packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_ehp_mc_low_discard_cnt
                                
                                	Number of multicast low packets discarded because multicast FIFO is full
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_ehp_mc_low_pkt_cnt
                                
                                	EHP2PQP multicast low packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_ehp_uc_pkt_cnt
                                
                                	EHP2PQP unicast packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_erpp_lag_pruning_discard_cnt
                                
                                	Number of packet descriptors discarded due to LAG multicast pruning
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_erpp_pmf_discard_cnt
                                
                                	Number of packet descriptors discarded due to ERPP PMF
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_erpp_vlan_mbr_discard_cnt
                                
                                	Number of packet descriptors discarded because of egress VLAN membership
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_fqp_pkt_cnt
                                
                                	FQP2EPE packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_pqp_discard_mc_pkt_cnt
                                
                                	PQP discarded multicast packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_pqp_discard_uc_pkt_cnt
                                
                                	PQP discarded unicast packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_pqp_mc_bytes_cnt
                                
                                	PQP2FQP multicast bytes counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: egq_pqp_mc_pkt_cnt
                                
                                	PQP2FQP multicast packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_pqp_uc_bytes_cnt
                                
                                	PQP2FQP unicast bytes counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: egq_pqp_uc_pkt_cnt
                                
                                	PQP2FQP unicast packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: epni_epe_byte_cnt
                                
                                	EPE2PNI bytes counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: epni_epe_discard_cnt
                                
                                	EPE discarded packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: epni_epe_pkt_cnt
                                
                                	EPE2PNI packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_in_cnt_p1
                                
                                	FDA input cell counter P1
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_in_cnt_p2
                                
                                	FDA input cell counter P2
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_in_cnt_p3
                                
                                	FDA input cell counter P3
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_in_ipt_cnt
                                
                                	FDA input cell counter IPT
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_in_meshmc_cnt
                                
                                	FDA input cell counter MESHMC
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_in_tdm_cnt
                                
                                	FDA input cell counter TDM
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_out_cnt_p1
                                
                                	FDA output cell counter P1
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_out_cnt_p2
                                
                                	FDA output cell counter P2
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_out_cnt_p3
                                
                                	FDA output cell counter P3
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_out_ipt_cnt
                                
                                	FDA output cell counter IPT
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_out_meshmc_cnt
                                
                                	FDA output cell counter MESHMC
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_out_tdm_cnt
                                
                                	FDA output cell counter TDM
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_egq_drop_cnt
                                
                                	FDA EGQ drop counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_egq_meshmc_drop_cnt
                                
                                	FDA EGQ MESHMC drop counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdr_cell_in_cnt_total
                                
                                	FDR total incoming cell counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdr_p1_cell_in_cnt
                                
                                	FDR total incoming cell counter at pipe 1
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdr_p2_cell_in_cnt
                                
                                	FDR total incoming cell counter at pipe 2
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdr_p3_cell_in_cnt
                                
                                	FDR total incoming cell counter at pipe 3
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdt_ipt_desc_cell_cnt
                                
                                	Descriptor cell counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdt_ire_desc_cell_cnt
                                
                                	IRE internal descriptor cell counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdt_transmitted_data_cells_cnt
                                
                                	Counts all transmitted data cells
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: idr_mmu_if_cnt
                                
                                	Performance counter of the MMU interface
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: idr_ocb_if_cnt
                                
                                	Performance counter of the OCB interface
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ipt_cfg_byte_cnt
                                
                                	Configurable bytes counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: ipt_cfg_event_cnt
                                
                                	Configurable event counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ipt_egq_pkt_cnt
                                
                                	EGQ packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ipt_enq_pkt_cnt
                                
                                	ENQ packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ipt_fdt_pkt_cnt
                                
                                	FDT packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: iqm_deleted_pkt_cnt
                                
                                	Counts matched packets discarded in the DEQ process
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: iqm_dequeue_pkt_cnt
                                
                                	Counts dequeued packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: iqm_enq_discarded_pkt_cnt
                                
                                	Counts all packets discarded at the ENQ pipe
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: iqm_enqueue_pkt_cnt
                                
                                	Counts enqueued packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ire_cpu_pkt_cnt
                                
                                	CPU ingress received packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ire_fdt_if_cnt
                                
                                	Performance counter of the FDT interface
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ire_nif_pkt_cnt
                                
                                	NIF received packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ire_oamp_pkt_cnt
                                
                                	OAMP ingress received packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ire_olp_pkt_cnt
                                
                                	OLP ingress received packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ire_rcy_pkt_cnt
                                
                                	Recycling ingress received packet counter
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: nbi_rx_total_byte_cnt
                                
                                	Total bytes sent from NIF to IRE
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: nbi_rx_total_pkt_cnt
                                
                                	Total packets sent from NIF to IRE
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: nbi_tx_total_byte_cnt
                                
                                	Total bytes sent from EGQ to NIF
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: nbi_tx_total_pkt_cnt
                                
                                	Total packets sent from EGQ to NIF
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics, self).__init__()

                                    self.yang_name = "statistics"
                                    self.yang_parent_name = "asic-statistics-for-npu-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.egq_deleted_pkt_cnt = YLeaf(YType.uint64, "egq-deleted-pkt-cnt")

                                    self.egq_ehp_mc_high_discard_cnt = YLeaf(YType.uint64, "egq-ehp-mc-high-discard-cnt")

                                    self.egq_ehp_mc_high_pkt_cnt = YLeaf(YType.uint64, "egq-ehp-mc-high-pkt-cnt")

                                    self.egq_ehp_mc_low_discard_cnt = YLeaf(YType.uint64, "egq-ehp-mc-low-discard-cnt")

                                    self.egq_ehp_mc_low_pkt_cnt = YLeaf(YType.uint64, "egq-ehp-mc-low-pkt-cnt")

                                    self.egq_ehp_uc_pkt_cnt = YLeaf(YType.uint64, "egq-ehp-uc-pkt-cnt")

                                    self.egq_erpp_lag_pruning_discard_cnt = YLeaf(YType.uint64, "egq-erpp-lag-pruning-discard-cnt")

                                    self.egq_erpp_pmf_discard_cnt = YLeaf(YType.uint64, "egq-erpp-pmf-discard-cnt")

                                    self.egq_erpp_vlan_mbr_discard_cnt = YLeaf(YType.uint64, "egq-erpp-vlan-mbr-discard-cnt")

                                    self.egq_fqp_pkt_cnt = YLeaf(YType.uint64, "egq-fqp-pkt-cnt")

                                    self.egq_pqp_discard_mc_pkt_cnt = YLeaf(YType.uint64, "egq-pqp-discard-mc-pkt-cnt")

                                    self.egq_pqp_discard_uc_pkt_cnt = YLeaf(YType.uint64, "egq-pqp-discard-uc-pkt-cnt")

                                    self.egq_pqp_mc_bytes_cnt = YLeaf(YType.uint64, "egq-pqp-mc-bytes-cnt")

                                    self.egq_pqp_mc_pkt_cnt = YLeaf(YType.uint64, "egq-pqp-mc-pkt-cnt")

                                    self.egq_pqp_uc_bytes_cnt = YLeaf(YType.uint64, "egq-pqp-uc-bytes-cnt")

                                    self.egq_pqp_uc_pkt_cnt = YLeaf(YType.uint64, "egq-pqp-uc-pkt-cnt")

                                    self.epni_epe_byte_cnt = YLeaf(YType.uint64, "epni-epe-byte-cnt")

                                    self.epni_epe_discard_cnt = YLeaf(YType.uint64, "epni-epe-discard-cnt")

                                    self.epni_epe_pkt_cnt = YLeaf(YType.uint64, "epni-epe-pkt-cnt")

                                    self.fda_cells_in_cnt_p1 = YLeaf(YType.uint64, "fda-cells-in-cnt-p1")

                                    self.fda_cells_in_cnt_p2 = YLeaf(YType.uint64, "fda-cells-in-cnt-p2")

                                    self.fda_cells_in_cnt_p3 = YLeaf(YType.uint64, "fda-cells-in-cnt-p3")

                                    self.fda_cells_in_ipt_cnt = YLeaf(YType.uint64, "fda-cells-in-ipt-cnt")

                                    self.fda_cells_in_meshmc_cnt = YLeaf(YType.uint64, "fda-cells-in-meshmc-cnt")

                                    self.fda_cells_in_tdm_cnt = YLeaf(YType.uint64, "fda-cells-in-tdm-cnt")

                                    self.fda_cells_out_cnt_p1 = YLeaf(YType.uint64, "fda-cells-out-cnt-p1")

                                    self.fda_cells_out_cnt_p2 = YLeaf(YType.uint64, "fda-cells-out-cnt-p2")

                                    self.fda_cells_out_cnt_p3 = YLeaf(YType.uint64, "fda-cells-out-cnt-p3")

                                    self.fda_cells_out_ipt_cnt = YLeaf(YType.uint64, "fda-cells-out-ipt-cnt")

                                    self.fda_cells_out_meshmc_cnt = YLeaf(YType.uint64, "fda-cells-out-meshmc-cnt")

                                    self.fda_cells_out_tdm_cnt = YLeaf(YType.uint64, "fda-cells-out-tdm-cnt")

                                    self.fda_egq_drop_cnt = YLeaf(YType.uint64, "fda-egq-drop-cnt")

                                    self.fda_egq_meshmc_drop_cnt = YLeaf(YType.uint64, "fda-egq-meshmc-drop-cnt")

                                    self.fdr_cell_in_cnt_total = YLeaf(YType.uint64, "fdr-cell-in-cnt-total")

                                    self.fdr_p1_cell_in_cnt = YLeaf(YType.uint64, "fdr-p1-cell-in-cnt")

                                    self.fdr_p2_cell_in_cnt = YLeaf(YType.uint64, "fdr-p2-cell-in-cnt")

                                    self.fdr_p3_cell_in_cnt = YLeaf(YType.uint64, "fdr-p3-cell-in-cnt")

                                    self.fdt_ipt_desc_cell_cnt = YLeaf(YType.uint64, "fdt-ipt-desc-cell-cnt")

                                    self.fdt_ire_desc_cell_cnt = YLeaf(YType.uint64, "fdt-ire-desc-cell-cnt")

                                    self.fdt_transmitted_data_cells_cnt = YLeaf(YType.uint64, "fdt-transmitted-data-cells-cnt")

                                    self.idr_mmu_if_cnt = YLeaf(YType.uint64, "idr-mmu-if-cnt")

                                    self.idr_ocb_if_cnt = YLeaf(YType.uint64, "idr-ocb-if-cnt")

                                    self.ipt_cfg_byte_cnt = YLeaf(YType.uint64, "ipt-cfg-byte-cnt")

                                    self.ipt_cfg_event_cnt = YLeaf(YType.uint64, "ipt-cfg-event-cnt")

                                    self.ipt_egq_pkt_cnt = YLeaf(YType.uint64, "ipt-egq-pkt-cnt")

                                    self.ipt_enq_pkt_cnt = YLeaf(YType.uint64, "ipt-enq-pkt-cnt")

                                    self.ipt_fdt_pkt_cnt = YLeaf(YType.uint64, "ipt-fdt-pkt-cnt")

                                    self.iqm_deleted_pkt_cnt = YLeaf(YType.uint64, "iqm-deleted-pkt-cnt")

                                    self.iqm_dequeue_pkt_cnt = YLeaf(YType.uint64, "iqm-dequeue-pkt-cnt")

                                    self.iqm_enq_discarded_pkt_cnt = YLeaf(YType.uint64, "iqm-enq-discarded-pkt-cnt")

                                    self.iqm_enqueue_pkt_cnt = YLeaf(YType.uint64, "iqm-enqueue-pkt-cnt")

                                    self.ire_cpu_pkt_cnt = YLeaf(YType.uint64, "ire-cpu-pkt-cnt")

                                    self.ire_fdt_if_cnt = YLeaf(YType.uint64, "ire-fdt-if-cnt")

                                    self.ire_nif_pkt_cnt = YLeaf(YType.uint64, "ire-nif-pkt-cnt")

                                    self.ire_oamp_pkt_cnt = YLeaf(YType.uint64, "ire-oamp-pkt-cnt")

                                    self.ire_olp_pkt_cnt = YLeaf(YType.uint64, "ire-olp-pkt-cnt")

                                    self.ire_rcy_pkt_cnt = YLeaf(YType.uint64, "ire-rcy-pkt-cnt")

                                    self.nbi_rx_total_byte_cnt = YLeaf(YType.uint64, "nbi-rx-total-byte-cnt")

                                    self.nbi_rx_total_pkt_cnt = YLeaf(YType.uint64, "nbi-rx-total-pkt-cnt")

                                    self.nbi_tx_total_byte_cnt = YLeaf(YType.uint64, "nbi-tx-total-byte-cnt")

                                    self.nbi_tx_total_pkt_cnt = YLeaf(YType.uint64, "nbi-tx-total-pkt-cnt")
                                    self._segment_path = lambda: "statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics, ['egq_deleted_pkt_cnt', 'egq_ehp_mc_high_discard_cnt', 'egq_ehp_mc_high_pkt_cnt', 'egq_ehp_mc_low_discard_cnt', 'egq_ehp_mc_low_pkt_cnt', 'egq_ehp_uc_pkt_cnt', 'egq_erpp_lag_pruning_discard_cnt', 'egq_erpp_pmf_discard_cnt', 'egq_erpp_vlan_mbr_discard_cnt', 'egq_fqp_pkt_cnt', 'egq_pqp_discard_mc_pkt_cnt', 'egq_pqp_discard_uc_pkt_cnt', 'egq_pqp_mc_bytes_cnt', 'egq_pqp_mc_pkt_cnt', 'egq_pqp_uc_bytes_cnt', 'egq_pqp_uc_pkt_cnt', 'epni_epe_byte_cnt', 'epni_epe_discard_cnt', 'epni_epe_pkt_cnt', 'fda_cells_in_cnt_p1', 'fda_cells_in_cnt_p2', 'fda_cells_in_cnt_p3', 'fda_cells_in_ipt_cnt', 'fda_cells_in_meshmc_cnt', 'fda_cells_in_tdm_cnt', 'fda_cells_out_cnt_p1', 'fda_cells_out_cnt_p2', 'fda_cells_out_cnt_p3', 'fda_cells_out_ipt_cnt', 'fda_cells_out_meshmc_cnt', 'fda_cells_out_tdm_cnt', 'fda_egq_drop_cnt', 'fda_egq_meshmc_drop_cnt', 'fdr_cell_in_cnt_total', 'fdr_p1_cell_in_cnt', 'fdr_p2_cell_in_cnt', 'fdr_p3_cell_in_cnt', 'fdt_ipt_desc_cell_cnt', 'fdt_ire_desc_cell_cnt', 'fdt_transmitted_data_cells_cnt', 'idr_mmu_if_cnt', 'idr_ocb_if_cnt', 'ipt_cfg_byte_cnt', 'ipt_cfg_event_cnt', 'ipt_egq_pkt_cnt', 'ipt_enq_pkt_cnt', 'ipt_fdt_pkt_cnt', 'iqm_deleted_pkt_cnt', 'iqm_dequeue_pkt_cnt', 'iqm_enq_discarded_pkt_cnt', 'iqm_enqueue_pkt_cnt', 'ire_cpu_pkt_cnt', 'ire_fdt_if_cnt', 'ire_nif_pkt_cnt', 'ire_oamp_pkt_cnt', 'ire_olp_pkt_cnt', 'ire_rcy_pkt_cnt', 'nbi_rx_total_byte_cnt', 'nbi_rx_total_pkt_cnt', 'nbi_tx_total_byte_cnt', 'nbi_tx_total_pkt_cnt'], name, value)


                class NpuNumbers(Entity):
                    """
                    Ingress Stats
                    
                    .. attribute:: npu_number
                    
                    	Stats for a particular npu
                    	**type**\: list of    :py:class:`NpuNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber>`
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dpa.Stats.Nodes.Node.NpuNumbers, self).__init__()

                        self.yang_name = "npu-numbers"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"npu-number" : ("npu_number", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber)}

                        self.npu_number = YList(self)
                        self._segment_path = lambda: "npu-numbers"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers, [], name, value)


                    class NpuNumber(Entity):
                        """
                        Stats for a particular npu
                        
                        .. attribute:: npu_id  <key>
                        
                        	Npu number
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: display
                        
                        	show npu specific voq or trap stats
                        	**type**\:   :py:class:`Display <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display>`
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber, self).__init__()

                            self.yang_name = "npu-number"
                            self.yang_parent_name = "npu-numbers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"display" : ("display", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display)}
                            self._child_list_classes = {}

                            self.npu_id = YLeaf(YType.int32, "npu-id")

                            self.display = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display()
                            self.display.parent = self
                            self._children_name_map["display"] = "display"
                            self._children_yang_names.add("display")
                            self._segment_path = lambda: "npu-number" + "[npu-id='" + self.npu_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber, ['npu_id'], name, value)


                        class Display(Entity):
                            """
                            show npu specific voq or trap stats
                            
                            .. attribute:: base_numbers
                            
                            	Voq stats grouped by voq base numbers
                            	**type**\:   :py:class:`BaseNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers>`
                            
                            .. attribute:: interface_handles
                            
                            	Voq stats grouped by interface handle
                            	**type**\:   :py:class:`InterfaceHandles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles>`
                            
                            .. attribute:: trap_ids
                            
                            	Trap stats for a particular npu
                            	**type**\:   :py:class:`TrapIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds>`
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display, self).__init__()

                                self.yang_name = "display"
                                self.yang_parent_name = "npu-number"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"base-numbers" : ("base_numbers", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers), "interface-handles" : ("interface_handles", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles), "trap-ids" : ("trap_ids", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds)}
                                self._child_list_classes = {}

                                self.base_numbers = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers()
                                self.base_numbers.parent = self
                                self._children_name_map["base_numbers"] = "base-numbers"
                                self._children_yang_names.add("base-numbers")

                                self.interface_handles = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles()
                                self.interface_handles.parent = self
                                self._children_name_map["interface_handles"] = "interface-handles"
                                self._children_yang_names.add("interface-handles")

                                self.trap_ids = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds()
                                self.trap_ids.parent = self
                                self._children_name_map["trap_ids"] = "trap-ids"
                                self._children_yang_names.add("trap-ids")
                                self._segment_path = lambda: "display"


                            class BaseNumbers(Entity):
                                """
                                Voq stats grouped by voq base numbers
                                
                                .. attribute:: base_number
                                
                                	Voq Base Number for a particular voq
                                	**type**\: list of    :py:class:`BaseNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber>`
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers, self).__init__()

                                    self.yang_name = "base-numbers"
                                    self.yang_parent_name = "display"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"base-number" : ("base_number", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber)}

                                    self.base_number = YList(self)
                                    self._segment_path = lambda: "base-numbers"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers, [], name, value)


                                class BaseNumber(Entity):
                                    """
                                    Voq Base Number for a particular voq
                                    
                                    .. attribute:: base_number  <key>
                                    
                                    	Interface handle
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: connector_id
                                    
                                    	Connector id of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: if_handle
                                    
                                    	IfHandle of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: in_use
                                    
                                    	Flag to indicate if port is in use
                                    	**type**\:  bool
                                    
                                    .. attribute:: is_local_port
                                    
                                    	Flag to indicate if port is local to the node
                                    	**type**\:  bool
                                    
                                    .. attribute:: npu_core
                                    
                                    	NPU core of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: npu_num
                                    
                                    	NPU of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: port_num
                                    
                                    	Port Number of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: port_speed
                                    
                                    	Port speed of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: pp_port
                                    
                                    	PP Port number of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: rack_num
                                    
                                    	Rack of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: slot_num
                                    
                                    	Slot of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: sys_port
                                    
                                    	System port of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: voq_base
                                    
                                    	Voq Base number of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: voq_stat
                                    
                                    	Keeps a record of the received and dropped packets and bytes on the port
                                    	**type**\: list of    :py:class:`VoqStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat>`
                                    
                                    

                                    """

                                    _prefix = 'fretta-bcm-dpa-resources-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber, self).__init__()

                                        self.yang_name = "base-number"
                                        self.yang_parent_name = "base-numbers"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"voq-stat" : ("voq_stat", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat)}

                                        self.base_number = YLeaf(YType.uint32, "base-number")

                                        self.connector_id = YLeaf(YType.uint32, "connector-id")

                                        self.if_handle = YLeaf(YType.uint32, "if-handle")

                                        self.in_use = YLeaf(YType.boolean, "in-use")

                                        self.is_local_port = YLeaf(YType.boolean, "is-local-port")

                                        self.npu_core = YLeaf(YType.uint8, "npu-core")

                                        self.npu_num = YLeaf(YType.uint8, "npu-num")

                                        self.port_num = YLeaf(YType.uint8, "port-num")

                                        self.port_speed = YLeaf(YType.uint32, "port-speed")

                                        self.pp_port = YLeaf(YType.uint32, "pp-port")

                                        self.rack_num = YLeaf(YType.uint8, "rack-num")

                                        self.slot_num = YLeaf(YType.uint8, "slot-num")

                                        self.sys_port = YLeaf(YType.uint32, "sys-port")

                                        self.voq_base = YLeaf(YType.uint32, "voq-base")

                                        self.voq_stat = YList(self)
                                        self._segment_path = lambda: "base-number" + "[base-number='" + self.base_number.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber, ['base_number', 'connector_id', 'if_handle', 'in_use', 'is_local_port', 'npu_core', 'npu_num', 'port_num', 'port_speed', 'pp_port', 'rack_num', 'slot_num', 'sys_port', 'voq_base'], name, value)


                                    class VoqStat(Entity):
                                        """
                                        Keeps a record of the received and dropped
                                        packets and bytes on the port
                                        
                                        .. attribute:: dropped_bytes
                                        
                                        	Bytes Dropped on the port
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: dropped_packets
                                        
                                        	Packets Dropeed on the port
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: received_bytes
                                        
                                        	Bytes Received on the port
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: received_packets
                                        
                                        	Packets Received on the port
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'fretta-bcm-dpa-resources-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat, self).__init__()

                                            self.yang_name = "voq-stat"
                                            self.yang_parent_name = "base-number"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.dropped_bytes = YLeaf(YType.uint64, "dropped-bytes")

                                            self.dropped_packets = YLeaf(YType.uint64, "dropped-packets")

                                            self.received_bytes = YLeaf(YType.uint64, "received-bytes")

                                            self.received_packets = YLeaf(YType.uint64, "received-packets")
                                            self._segment_path = lambda: "voq-stat"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat, ['dropped_bytes', 'dropped_packets', 'received_bytes', 'received_packets'], name, value)


                            class InterfaceHandles(Entity):
                                """
                                Voq stats grouped by interface handle
                                
                                .. attribute:: interface_handle
                                
                                	Voq stats for a particular interface handle
                                	**type**\: list of    :py:class:`InterfaceHandle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle>`
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles, self).__init__()

                                    self.yang_name = "interface-handles"
                                    self.yang_parent_name = "display"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"interface-handle" : ("interface_handle", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle)}

                                    self.interface_handle = YList(self)
                                    self._segment_path = lambda: "interface-handles"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles, [], name, value)


                                class InterfaceHandle(Entity):
                                    """
                                    Voq stats for a particular interface
                                    handle
                                    
                                    .. attribute:: interface_handle  <key>
                                    
                                    	Interface Handle
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: connector_id
                                    
                                    	Connector id of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: if_handle
                                    
                                    	IfHandle of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: in_use
                                    
                                    	Flag to indicate if port is in use
                                    	**type**\:  bool
                                    
                                    .. attribute:: is_local_port
                                    
                                    	Flag to indicate if port is local to the node
                                    	**type**\:  bool
                                    
                                    .. attribute:: npu_core
                                    
                                    	NPU core of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: npu_num
                                    
                                    	NPU of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: port_num
                                    
                                    	Port Number of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: port_speed
                                    
                                    	Port speed of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: pp_port
                                    
                                    	PP Port number of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: rack_num
                                    
                                    	Rack of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: slot_num
                                    
                                    	Slot of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: sys_port
                                    
                                    	System port of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: voq_base
                                    
                                    	Voq Base number of port
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: voq_stat
                                    
                                    	Keeps a record of the received and dropped packets and bytes on the port
                                    	**type**\: list of    :py:class:`VoqStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat>`
                                    
                                    

                                    """

                                    _prefix = 'fretta-bcm-dpa-resources-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle, self).__init__()

                                        self.yang_name = "interface-handle"
                                        self.yang_parent_name = "interface-handles"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"voq-stat" : ("voq_stat", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat)}

                                        self.interface_handle = YLeaf(YType.uint32, "interface-handle")

                                        self.connector_id = YLeaf(YType.uint32, "connector-id")

                                        self.if_handle = YLeaf(YType.uint32, "if-handle")

                                        self.in_use = YLeaf(YType.boolean, "in-use")

                                        self.is_local_port = YLeaf(YType.boolean, "is-local-port")

                                        self.npu_core = YLeaf(YType.uint8, "npu-core")

                                        self.npu_num = YLeaf(YType.uint8, "npu-num")

                                        self.port_num = YLeaf(YType.uint8, "port-num")

                                        self.port_speed = YLeaf(YType.uint32, "port-speed")

                                        self.pp_port = YLeaf(YType.uint32, "pp-port")

                                        self.rack_num = YLeaf(YType.uint8, "rack-num")

                                        self.slot_num = YLeaf(YType.uint8, "slot-num")

                                        self.sys_port = YLeaf(YType.uint32, "sys-port")

                                        self.voq_base = YLeaf(YType.uint32, "voq-base")

                                        self.voq_stat = YList(self)
                                        self._segment_path = lambda: "interface-handle" + "[interface-handle='" + self.interface_handle.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle, ['interface_handle', 'connector_id', 'if_handle', 'in_use', 'is_local_port', 'npu_core', 'npu_num', 'port_num', 'port_speed', 'pp_port', 'rack_num', 'slot_num', 'sys_port', 'voq_base'], name, value)


                                    class VoqStat(Entity):
                                        """
                                        Keeps a record of the received and dropped
                                        packets and bytes on the port
                                        
                                        .. attribute:: dropped_bytes
                                        
                                        	Bytes Dropped on the port
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: dropped_packets
                                        
                                        	Packets Dropeed on the port
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: received_bytes
                                        
                                        	Bytes Received on the port
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: received_packets
                                        
                                        	Packets Received on the port
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'fretta-bcm-dpa-resources-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat, self).__init__()

                                            self.yang_name = "voq-stat"
                                            self.yang_parent_name = "interface-handle"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.dropped_bytes = YLeaf(YType.uint64, "dropped-bytes")

                                            self.dropped_packets = YLeaf(YType.uint64, "dropped-packets")

                                            self.received_bytes = YLeaf(YType.uint64, "received-bytes")

                                            self.received_packets = YLeaf(YType.uint64, "received-packets")
                                            self._segment_path = lambda: "voq-stat"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat, ['dropped_bytes', 'dropped_packets', 'received_bytes', 'received_packets'], name, value)


                            class TrapIds(Entity):
                                """
                                Trap stats for a particular npu
                                
                                .. attribute:: trap_id
                                
                                	Filter by specific trap id
                                	**type**\: list of    :py:class:`TrapId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId>`
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds, self).__init__()

                                    self.yang_name = "trap-ids"
                                    self.yang_parent_name = "display"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"trap-id" : ("trap_id", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId)}

                                    self.trap_id = YList(self)
                                    self._segment_path = lambda: "trap-ids"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds, [], name, value)


                                class TrapId(Entity):
                                    """
                                    Filter by specific trap id
                                    
                                    .. attribute:: trap_id  <key>
                                    
                                    	Trap ID
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: encap_id
                                    
                                    	Encap Id of the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: fec_id
                                    
                                    	Fec id of the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: gport
                                    
                                    	Gport of the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: id
                                    
                                    	Id for internal use
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: mc_group
                                    
                                    	McGroup of the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: npu_id
                                    
                                    	NpuId on which trap is enabled
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: offset
                                    
                                    	Offset for internal use
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: packet_accepted
                                    
                                    	Number of packets accepted after hitting the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: packet_dropped
                                    
                                    	Number of packets dropped after hitting the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: policer_id
                                    
                                    	Id of the policer on the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: priority
                                    
                                    	Priority of the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: stats_id
                                    
                                    	Stats Id of the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: trap_id_xr
                                    
                                    	Id of the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: trap_strength
                                    
                                    	Trap Strength of the trap
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: trap_string
                                    
                                    	Name String of the trap
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'fretta-bcm-dpa-resources-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId, self).__init__()

                                        self.yang_name = "trap-id"
                                        self.yang_parent_name = "trap-ids"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.trap_id = YLeaf(YType.uint32, "trap-id")

                                        self.encap_id = YLeaf(YType.uint32, "encap-id")

                                        self.fec_id = YLeaf(YType.uint32, "fec-id")

                                        self.gport = YLeaf(YType.uint32, "gport")

                                        self.id = YLeaf(YType.uint32, "id")

                                        self.mc_group = YLeaf(YType.uint32, "mc-group")

                                        self.npu_id = YLeaf(YType.uint64, "npu-id")

                                        self.offset = YLeaf(YType.uint64, "offset")

                                        self.packet_accepted = YLeaf(YType.uint64, "packet-accepted")

                                        self.packet_dropped = YLeaf(YType.uint64, "packet-dropped")

                                        self.policer_id = YLeaf(YType.uint32, "policer-id")

                                        self.priority = YLeaf(YType.uint32, "priority")

                                        self.stats_id = YLeaf(YType.uint32, "stats-id")

                                        self.trap_id_xr = YLeaf(YType.uint32, "trap-id-xr")

                                        self.trap_strength = YLeaf(YType.uint32, "trap-strength")

                                        self.trap_string = YLeaf(YType.str, "trap-string")
                                        self._segment_path = lambda: "trap-id" + "[trap-id='" + self.trap_id.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId, ['trap_id', 'encap_id', 'fec_id', 'gport', 'id', 'mc_group', 'npu_id', 'offset', 'packet_accepted', 'packet_dropped', 'policer_id', 'priority', 'stats_id', 'trap_id_xr', 'trap_strength', 'trap_string'], name, value)

    def clone_ptr(self):
        self._top_entity = Dpa()
        return self._top_entity

