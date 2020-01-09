""" Cisco_IOS_XR_pbr_vservice_mgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pbr\-vservice\-mgr package operational data.

This module contains definitions
for the following management objects\:
  global\-service\-function\-chaining\: NSH Service Function
    Chaining global operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class VsNshStats(Enum):
    """
    VsNshStats (Enum Class)

    Vs nsh stats

    .. data:: vs_nsh_stats_spi_si = 0

    	vs nsh stats spi si

    .. data:: vs_nsh_stats_ter_min_ate = 1

    	vs nsh stats ter min ate

    .. data:: vs_nsh_stats_sf = 2

    	vs nsh stats sf

    .. data:: vs_nsh_stats_sff = 3

    	vs nsh stats sff

    .. data:: vs_nsh_stats_sff_local = 4

    	vs nsh stats sff local

    .. data:: vs_nsh_stats_sfp = 5

    	vs nsh stats sfp

    .. data:: vs_nsh_stats_sfp_detail = 6

    	vs nsh stats sfp detail

    .. data:: vs_nsh_stats_max = 7

    	vs nsh stats max

    """

    vs_nsh_stats_spi_si = Enum.YLeaf(0, "vs-nsh-stats-spi-si")

    vs_nsh_stats_ter_min_ate = Enum.YLeaf(1, "vs-nsh-stats-ter-min-ate")

    vs_nsh_stats_sf = Enum.YLeaf(2, "vs-nsh-stats-sf")

    vs_nsh_stats_sff = Enum.YLeaf(3, "vs-nsh-stats-sff")

    vs_nsh_stats_sff_local = Enum.YLeaf(4, "vs-nsh-stats-sff-local")

    vs_nsh_stats_sfp = Enum.YLeaf(5, "vs-nsh-stats-sfp")

    vs_nsh_stats_sfp_detail = Enum.YLeaf(6, "vs-nsh-stats-sfp-detail")

    vs_nsh_stats_max = Enum.YLeaf(7, "vs-nsh-stats-max")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
        return meta._meta_table['VsNshStats']



class GlobalServiceFunctionChaining(_Entity_):
    """
    NSH Service Function Chaining global operational
    data
    
    .. attribute:: service_function_path
    
    	Service Function Path operational data
    	**type**\:  :py:class:`ServiceFunctionPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath>`
    
    	**config**\: False
    
    .. attribute:: service_function
    
    	Service Function operational data
    	**type**\:  :py:class:`ServiceFunction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunction>`
    
    	**config**\: False
    
    .. attribute:: service_function_forwarder
    
    	Service Function Forwarder operational data
    	**type**\:  :py:class:`ServiceFunctionForwarder <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder>`
    
    	**config**\: False
    
    

    """

    _prefix = 'pbr-vservice-mgr-oper'
    _revision = '2017-05-01'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(GlobalServiceFunctionChaining, self).__init__()
        self._top_entity = None

        self.yang_name = "global-service-function-chaining"
        self.yang_parent_name = "Cisco-IOS-XR-pbr-vservice-mgr-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("service-function-path", ("service_function_path", GlobalServiceFunctionChaining.ServiceFunctionPath)), ("service-function", ("service_function", GlobalServiceFunctionChaining.ServiceFunction)), ("service-function-forwarder", ("service_function_forwarder", GlobalServiceFunctionChaining.ServiceFunctionForwarder))])
        self._leafs = OrderedDict()

        self.service_function_path = GlobalServiceFunctionChaining.ServiceFunctionPath()
        self.service_function_path.parent = self
        self._children_name_map["service_function_path"] = "service-function-path"

        self.service_function = GlobalServiceFunctionChaining.ServiceFunction()
        self.service_function.parent = self
        self._children_name_map["service_function"] = "service-function"

        self.service_function_forwarder = GlobalServiceFunctionChaining.ServiceFunctionForwarder()
        self.service_function_forwarder.parent = self
        self._children_name_map["service_function_forwarder"] = "service-function-forwarder"
        self._segment_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(GlobalServiceFunctionChaining, [], name, value)


    class ServiceFunctionPath(_Entity_):
        """
        Service Function Path operational data
        
        .. attribute:: path_ids
        
        	Service Function Path Id 
        	**type**\:  :py:class:`PathIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds>`
        
        	**config**\: False
        
        

        """

        _prefix = 'pbr-vservice-mgr-oper'
        _revision = '2017-05-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(GlobalServiceFunctionChaining.ServiceFunctionPath, self).__init__()

            self.yang_name = "service-function-path"
            self.yang_parent_name = "global-service-function-chaining"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("path-ids", ("path_ids", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds))])
            self._leafs = OrderedDict()

            self.path_ids = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds()
            self.path_ids.parent = self
            self._children_name_map["path_ids"] = "path-ids"
            self._segment_path = lambda: "service-function-path"
            self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath, [], name, value)


        class PathIds(_Entity_):
            """
            Service Function Path Id 
            
            .. attribute:: path_id
            
            	Specific Service\-Function\-Path identifier 
            	**type**\: list of  		 :py:class:`PathId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId>`
            
            	**config**\: False
            
            

            """

            _prefix = 'pbr-vservice-mgr-oper'
            _revision = '2017-05-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds, self).__init__()

                self.yang_name = "path-ids"
                self.yang_parent_name = "service-function-path"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("path-id", ("path_id", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId))])
                self._leafs = OrderedDict()

                self.path_id = YList(self)
                self._segment_path = lambda: "path-ids"
                self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-path/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds, [], name, value)


            class PathId(_Entity_):
                """
                Specific Service\-Function\-Path identifier 
                
                .. attribute:: id  (key)
                
                	Specific Service\-Function\-Path identifier
                	**type**\: int
                
                	**range:** 1..16777215
                
                	**config**\: False
                
                .. attribute:: stats
                
                	SFP Statistics
                	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats>`
                
                	**config**\: False
                
                .. attribute:: service_indexes
                
                	Service Index Belonging to Path
                	**type**\:  :py:class:`ServiceIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes>`
                
                	**config**\: False
                
                

                """

                _prefix = 'pbr-vservice-mgr-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId, self).__init__()

                    self.yang_name = "path-id"
                    self.yang_parent_name = "path-ids"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['id']
                    self._child_classes = OrderedDict([("stats", ("stats", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats)), ("service-indexes", ("service_indexes", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes))])
                    self._leafs = OrderedDict([
                        ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                    ])
                    self.id = None

                    self.stats = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats()
                    self.stats.parent = self
                    self._children_name_map["stats"] = "stats"

                    self.service_indexes = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes()
                    self.service_indexes.parent = self
                    self._children_name_map["service_indexes"] = "service-indexes"
                    self._segment_path = lambda: "path-id" + "[id='" + str(self.id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-path/path-ids/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId, ['id'], name, value)


                class Stats(_Entity_):
                    """
                    SFP Statistics
                    
                    .. attribute:: detail
                    
                    	Detail statistics per service index 
                    	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail>`
                    
                    	**config**\: False
                    
                    .. attribute:: summarized
                    
                    	Combined statistics of all service index in service functionpath
                    	**type**\:  :py:class:`Summarized <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'pbr-vservice-mgr-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "path-id"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("detail", ("detail", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail)), ("summarized", ("summarized", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized))])
                        self._leafs = OrderedDict()

                        self.detail = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail()
                        self.detail.parent = self
                        self._children_name_map["detail"] = "detail"

                        self.summarized = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized()
                        self.summarized.parent = self
                        self._children_name_map["summarized"] = "summarized"
                        self._segment_path = lambda: "stats"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats, [], name, value)


                    class Detail(_Entity_):
                        """
                        Detail statistics per service index 
                        
                        .. attribute:: data
                        
                        	Statistics data
                        	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data>`
                        
                        	**config**\: False
                        
                        .. attribute:: si_arr
                        
                        	SI array in case of detail stats
                        	**type**\: list of  		 :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail, self).__init__()

                            self.yang_name = "detail"
                            self.yang_parent_name = "stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("data", ("data", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data)), ("si-arr", ("si_arr", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr))])
                            self._leafs = OrderedDict()

                            self.data = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data()
                            self.data.parent = self
                            self._children_name_map["data"] = "data"

                            self.si_arr = YList(self)
                            self._segment_path = lambda: "detail"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail, [], name, value)


                        class Data(_Entity_):
                            """
                            Statistics data
                            
                            .. attribute:: sfp
                            
                            	SFP stats
                            	**type**\:  :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp>`
                            
                            	**config**\: False
                            
                            .. attribute:: spi_si
                            
                            	SPI SI stats
                            	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi>`
                            
                            	**config**\: False
                            
                            .. attribute:: term
                            
                            	Terminate stats
                            	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term>`
                            
                            	**config**\: False
                            
                            .. attribute:: sf
                            
                            	Service function stats
                            	**type**\:  :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf>`
                            
                            	**config**\: False
                            
                            .. attribute:: sff
                            
                            	Service function forwarder stats
                            	**type**\:  :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff>`
                            
                            	**config**\: False
                            
                            .. attribute:: sff_local
                            
                            	Local service function forwarder stats
                            	**type**\:  :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal>`
                            
                            	**config**\: False
                            
                            .. attribute:: type
                            
                            	type
                            	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.VsNshStats>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'pbr-vservice-mgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data, self).__init__()

                                self.yang_name = "data"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("sfp", ("sfp", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp)), ("spi-si", ("spi_si", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi)), ("term", ("term", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term)), ("sf", ("sf", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf)), ("sff", ("sff", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff)), ("sff-local", ("sff_local", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal))])
                                self._leafs = OrderedDict([
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStats', '')])),
                                ])
                                self.type = None

                                self.sfp = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp()
                                self.sfp.parent = self
                                self._children_name_map["sfp"] = "sfp"

                                self.spi_si = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi()
                                self.spi_si.parent = self
                                self._children_name_map["spi_si"] = "spi-si"

                                self.term = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term()
                                self.term.parent = self
                                self._children_name_map["term"] = "term"

                                self.sf = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf()
                                self.sf.parent = self
                                self._children_name_map["sf"] = "sf"

                                self.sff = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff()
                                self.sff.parent = self
                                self._children_name_map["sff"] = "sff"

                                self.sff_local = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal()
                                self.sff_local.parent = self
                                self._children_name_map["sff_local"] = "sff-local"
                                self._segment_path = lambda: "data"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data, ['type'], name, value)


                            class Sfp(_Entity_):
                                """
                                SFP stats
                                
                                .. attribute:: spi_si
                                
                                	Service index counters
                                	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi>`
                                
                                	**config**\: False
                                
                                .. attribute:: term
                                
                                	Terminate counters
                                	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp, self).__init__()

                                    self.yang_name = "sfp"
                                    self.yang_parent_name = "data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("spi-si", ("spi_si", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi)), ("term", ("term", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term))])
                                    self._leafs = OrderedDict()

                                    self.spi_si = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi()
                                    self.spi_si.parent = self
                                    self._children_name_map["spi_si"] = "spi-si"

                                    self.term = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term()
                                    self.term.parent = self
                                    self._children_name_map["term"] = "term"
                                    self._segment_path = lambda: "sfp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp, [], name, value)


                                class SpiSi(_Entity_):
                                    """
                                    Service index counters
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-mgr-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi, self).__init__()

                                        self.yang_name = "spi-si"
                                        self.yang_parent_name = "sfp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                            ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                        ])
                                        self.processed_pkts = None
                                        self.processed_bytes = None
                                        self._segment_path = lambda: "spi-si"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi']['meta_info']


                                class Term(_Entity_):
                                    """
                                    Terminate counters
                                    
                                    .. attribute:: terminated_pkts
                                    
                                    	Number of terminated packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: terminated_bytes
                                    
                                    	Total bytes terminated
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-mgr-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term, self).__init__()

                                        self.yang_name = "term"
                                        self.yang_parent_name = "sfp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('terminated_pkts', (YLeaf(YType.uint64, 'terminated-pkts'), ['int'])),
                                            ('terminated_bytes', (YLeaf(YType.uint64, 'terminated-bytes'), ['int'])),
                                        ])
                                        self.terminated_pkts = None
                                        self.terminated_bytes = None
                                        self._segment_path = lambda: "term"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp']['meta_info']


                            class SpiSi(_Entity_):
                                """
                                SPI SI stats
                                
                                .. attribute:: processed_pkts
                                
                                	Number of packets processed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: processed_bytes
                                
                                	Total bytes processed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi, self).__init__()

                                    self.yang_name = "spi-si"
                                    self.yang_parent_name = "data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                        ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                    ])
                                    self.processed_pkts = None
                                    self.processed_bytes = None
                                    self._segment_path = lambda: "spi-si"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi']['meta_info']


                            class Term(_Entity_):
                                """
                                Terminate stats
                                
                                .. attribute:: terminated_pkts
                                
                                	Number of terminated packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: terminated_bytes
                                
                                	Total bytes terminated
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term, self).__init__()

                                    self.yang_name = "term"
                                    self.yang_parent_name = "data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('terminated_pkts', (YLeaf(YType.uint64, 'terminated-pkts'), ['int'])),
                                        ('terminated_bytes', (YLeaf(YType.uint64, 'terminated-bytes'), ['int'])),
                                    ])
                                    self.terminated_pkts = None
                                    self.terminated_bytes = None
                                    self._segment_path = lambda: "term"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term']['meta_info']


                            class Sf(_Entity_):
                                """
                                Service function stats
                                
                                .. attribute:: processed_pkts
                                
                                	Number of packets processed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: processed_bytes
                                
                                	Total bytes processed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf, self).__init__()

                                    self.yang_name = "sf"
                                    self.yang_parent_name = "data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                        ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                    ])
                                    self.processed_pkts = None
                                    self.processed_bytes = None
                                    self._segment_path = lambda: "sf"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf, ['processed_pkts', 'processed_bytes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf']['meta_info']


                            class Sff(_Entity_):
                                """
                                Service function forwarder stats
                                
                                .. attribute:: processed_pkts
                                
                                	Number of packets processed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: processed_bytes
                                
                                	Total bytes processed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff, self).__init__()

                                    self.yang_name = "sff"
                                    self.yang_parent_name = "data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                        ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                    ])
                                    self.processed_pkts = None
                                    self.processed_bytes = None
                                    self._segment_path = lambda: "sff"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff, ['processed_pkts', 'processed_bytes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff']['meta_info']


                            class SffLocal(_Entity_):
                                """
                                Local service function forwarder stats
                                
                                .. attribute:: malformed_err_pkts
                                
                                	Number of packets with invalid NSH header
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: lookup_err_pkts
                                
                                	Number of packets with unknown spi\-si
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: malformed_err_bytes
                                
                                	Total bytes with invalid NSH header
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                .. attribute:: lookup_err_bytes
                                
                                	Total bytes with unknown spi\-si
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal, self).__init__()

                                    self.yang_name = "sff-local"
                                    self.yang_parent_name = "data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('malformed_err_pkts', (YLeaf(YType.uint64, 'malformed-err-pkts'), ['int'])),
                                        ('lookup_err_pkts', (YLeaf(YType.uint64, 'lookup-err-pkts'), ['int'])),
                                        ('malformed_err_bytes', (YLeaf(YType.uint64, 'malformed-err-bytes'), ['int'])),
                                        ('lookup_err_bytes', (YLeaf(YType.uint64, 'lookup-err-bytes'), ['int'])),
                                    ])
                                    self.malformed_err_pkts = None
                                    self.lookup_err_pkts = None
                                    self.malformed_err_bytes = None
                                    self.lookup_err_bytes = None
                                    self._segment_path = lambda: "sff-local"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal, ['malformed_err_pkts', 'lookup_err_pkts', 'malformed_err_bytes', 'lookup_err_bytes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data']['meta_info']


                        class SiArr(_Entity_):
                            """
                            SI array in case of detail stats
                            
                            .. attribute:: data
                            
                            	Stats counter for this index
                            	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data>`
                            
                            	**config**\: False
                            
                            .. attribute:: si
                            
                            	Service index
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'pbr-vservice-mgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr, self).__init__()

                                self.yang_name = "si-arr"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("data", ("data", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data))])
                                self._leafs = OrderedDict([
                                    ('si', (YLeaf(YType.uint8, 'si'), ['int'])),
                                ])
                                self.si = None

                                self.data = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data()
                                self.data.parent = self
                                self._children_name_map["data"] = "data"
                                self._segment_path = lambda: "si-arr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr, ['si'], name, value)


                            class Data(_Entity_):
                                """
                                Stats counter for this index
                                
                                .. attribute:: spi_si
                                
                                	SF/SFF stats
                                	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi>`
                                
                                	**config**\: False
                                
                                .. attribute:: term
                                
                                	Terminate stats
                                	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term>`
                                
                                	**config**\: False
                                
                                .. attribute:: type
                                
                                	type
                                	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.VsNshStats>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data, self).__init__()

                                    self.yang_name = "data"
                                    self.yang_parent_name = "si-arr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("spi-si", ("spi_si", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi)), ("term", ("term", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term))])
                                    self._leafs = OrderedDict([
                                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStats', '')])),
                                    ])
                                    self.type = None

                                    self.spi_si = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi()
                                    self.spi_si.parent = self
                                    self._children_name_map["spi_si"] = "spi-si"

                                    self.term = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term()
                                    self.term.parent = self
                                    self._children_name_map["term"] = "term"
                                    self._segment_path = lambda: "data"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data, ['type'], name, value)


                                class SpiSi(_Entity_):
                                    """
                                    SF/SFF stats
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-mgr-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi, self).__init__()

                                        self.yang_name = "spi-si"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                            ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                        ])
                                        self.processed_pkts = None
                                        self.processed_bytes = None
                                        self._segment_path = lambda: "spi-si"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi']['meta_info']


                                class Term(_Entity_):
                                    """
                                    Terminate stats
                                    
                                    .. attribute:: terminated_pkts
                                    
                                    	Number of terminated packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: terminated_bytes
                                    
                                    	Total bytes terminated
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-mgr-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term, self).__init__()

                                        self.yang_name = "term"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('terminated_pkts', (YLeaf(YType.uint64, 'terminated-pkts'), ['int'])),
                                            ('terminated_bytes', (YLeaf(YType.uint64, 'terminated-bytes'), ['int'])),
                                        ])
                                        self.terminated_pkts = None
                                        self.terminated_bytes = None
                                        self._segment_path = lambda: "term"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail']['meta_info']


                    class Summarized(_Entity_):
                        """
                        Combined statistics of all service index in
                        service functionpath
                        
                        .. attribute:: data
                        
                        	Statistics data
                        	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data>`
                        
                        	**config**\: False
                        
                        .. attribute:: si_arr
                        
                        	SI array in case of detail stats
                        	**type**\: list of  		 :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized, self).__init__()

                            self.yang_name = "summarized"
                            self.yang_parent_name = "stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("data", ("data", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data)), ("si-arr", ("si_arr", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr))])
                            self._leafs = OrderedDict()

                            self.data = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data()
                            self.data.parent = self
                            self._children_name_map["data"] = "data"

                            self.si_arr = YList(self)
                            self._segment_path = lambda: "summarized"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized, [], name, value)


                        class Data(_Entity_):
                            """
                            Statistics data
                            
                            .. attribute:: sfp
                            
                            	SFP stats
                            	**type**\:  :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp>`
                            
                            	**config**\: False
                            
                            .. attribute:: spi_si
                            
                            	SPI SI stats
                            	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi>`
                            
                            	**config**\: False
                            
                            .. attribute:: term
                            
                            	Terminate stats
                            	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term>`
                            
                            	**config**\: False
                            
                            .. attribute:: sf
                            
                            	Service function stats
                            	**type**\:  :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf>`
                            
                            	**config**\: False
                            
                            .. attribute:: sff
                            
                            	Service function forwarder stats
                            	**type**\:  :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff>`
                            
                            	**config**\: False
                            
                            .. attribute:: sff_local
                            
                            	Local service function forwarder stats
                            	**type**\:  :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal>`
                            
                            	**config**\: False
                            
                            .. attribute:: type
                            
                            	type
                            	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.VsNshStats>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'pbr-vservice-mgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data, self).__init__()

                                self.yang_name = "data"
                                self.yang_parent_name = "summarized"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("sfp", ("sfp", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp)), ("spi-si", ("spi_si", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi)), ("term", ("term", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term)), ("sf", ("sf", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf)), ("sff", ("sff", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff)), ("sff-local", ("sff_local", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal))])
                                self._leafs = OrderedDict([
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStats', '')])),
                                ])
                                self.type = None

                                self.sfp = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp()
                                self.sfp.parent = self
                                self._children_name_map["sfp"] = "sfp"

                                self.spi_si = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi()
                                self.spi_si.parent = self
                                self._children_name_map["spi_si"] = "spi-si"

                                self.term = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term()
                                self.term.parent = self
                                self._children_name_map["term"] = "term"

                                self.sf = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf()
                                self.sf.parent = self
                                self._children_name_map["sf"] = "sf"

                                self.sff = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff()
                                self.sff.parent = self
                                self._children_name_map["sff"] = "sff"

                                self.sff_local = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal()
                                self.sff_local.parent = self
                                self._children_name_map["sff_local"] = "sff-local"
                                self._segment_path = lambda: "data"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data, ['type'], name, value)


                            class Sfp(_Entity_):
                                """
                                SFP stats
                                
                                .. attribute:: spi_si
                                
                                	Service index counters
                                	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi>`
                                
                                	**config**\: False
                                
                                .. attribute:: term
                                
                                	Terminate counters
                                	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp, self).__init__()

                                    self.yang_name = "sfp"
                                    self.yang_parent_name = "data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("spi-si", ("spi_si", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi)), ("term", ("term", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term))])
                                    self._leafs = OrderedDict()

                                    self.spi_si = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi()
                                    self.spi_si.parent = self
                                    self._children_name_map["spi_si"] = "spi-si"

                                    self.term = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term()
                                    self.term.parent = self
                                    self._children_name_map["term"] = "term"
                                    self._segment_path = lambda: "sfp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp, [], name, value)


                                class SpiSi(_Entity_):
                                    """
                                    Service index counters
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-mgr-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi, self).__init__()

                                        self.yang_name = "spi-si"
                                        self.yang_parent_name = "sfp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                            ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                        ])
                                        self.processed_pkts = None
                                        self.processed_bytes = None
                                        self._segment_path = lambda: "spi-si"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi']['meta_info']


                                class Term(_Entity_):
                                    """
                                    Terminate counters
                                    
                                    .. attribute:: terminated_pkts
                                    
                                    	Number of terminated packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: terminated_bytes
                                    
                                    	Total bytes terminated
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-mgr-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term, self).__init__()

                                        self.yang_name = "term"
                                        self.yang_parent_name = "sfp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('terminated_pkts', (YLeaf(YType.uint64, 'terminated-pkts'), ['int'])),
                                            ('terminated_bytes', (YLeaf(YType.uint64, 'terminated-bytes'), ['int'])),
                                        ])
                                        self.terminated_pkts = None
                                        self.terminated_bytes = None
                                        self._segment_path = lambda: "term"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp']['meta_info']


                            class SpiSi(_Entity_):
                                """
                                SPI SI stats
                                
                                .. attribute:: processed_pkts
                                
                                	Number of packets processed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: processed_bytes
                                
                                	Total bytes processed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi, self).__init__()

                                    self.yang_name = "spi-si"
                                    self.yang_parent_name = "data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                        ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                    ])
                                    self.processed_pkts = None
                                    self.processed_bytes = None
                                    self._segment_path = lambda: "spi-si"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi']['meta_info']


                            class Term(_Entity_):
                                """
                                Terminate stats
                                
                                .. attribute:: terminated_pkts
                                
                                	Number of terminated packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: terminated_bytes
                                
                                	Total bytes terminated
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term, self).__init__()

                                    self.yang_name = "term"
                                    self.yang_parent_name = "data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('terminated_pkts', (YLeaf(YType.uint64, 'terminated-pkts'), ['int'])),
                                        ('terminated_bytes', (YLeaf(YType.uint64, 'terminated-bytes'), ['int'])),
                                    ])
                                    self.terminated_pkts = None
                                    self.terminated_bytes = None
                                    self._segment_path = lambda: "term"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term']['meta_info']


                            class Sf(_Entity_):
                                """
                                Service function stats
                                
                                .. attribute:: processed_pkts
                                
                                	Number of packets processed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: processed_bytes
                                
                                	Total bytes processed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf, self).__init__()

                                    self.yang_name = "sf"
                                    self.yang_parent_name = "data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                        ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                    ])
                                    self.processed_pkts = None
                                    self.processed_bytes = None
                                    self._segment_path = lambda: "sf"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf, ['processed_pkts', 'processed_bytes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf']['meta_info']


                            class Sff(_Entity_):
                                """
                                Service function forwarder stats
                                
                                .. attribute:: processed_pkts
                                
                                	Number of packets processed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: processed_bytes
                                
                                	Total bytes processed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff, self).__init__()

                                    self.yang_name = "sff"
                                    self.yang_parent_name = "data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                        ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                    ])
                                    self.processed_pkts = None
                                    self.processed_bytes = None
                                    self._segment_path = lambda: "sff"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff, ['processed_pkts', 'processed_bytes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff']['meta_info']


                            class SffLocal(_Entity_):
                                """
                                Local service function forwarder stats
                                
                                .. attribute:: malformed_err_pkts
                                
                                	Number of packets with invalid NSH header
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: lookup_err_pkts
                                
                                	Number of packets with unknown spi\-si
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: malformed_err_bytes
                                
                                	Total bytes with invalid NSH header
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                .. attribute:: lookup_err_bytes
                                
                                	Total bytes with unknown spi\-si
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal, self).__init__()

                                    self.yang_name = "sff-local"
                                    self.yang_parent_name = "data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('malformed_err_pkts', (YLeaf(YType.uint64, 'malformed-err-pkts'), ['int'])),
                                        ('lookup_err_pkts', (YLeaf(YType.uint64, 'lookup-err-pkts'), ['int'])),
                                        ('malformed_err_bytes', (YLeaf(YType.uint64, 'malformed-err-bytes'), ['int'])),
                                        ('lookup_err_bytes', (YLeaf(YType.uint64, 'lookup-err-bytes'), ['int'])),
                                    ])
                                    self.malformed_err_pkts = None
                                    self.lookup_err_pkts = None
                                    self.malformed_err_bytes = None
                                    self.lookup_err_bytes = None
                                    self._segment_path = lambda: "sff-local"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal, ['malformed_err_pkts', 'lookup_err_pkts', 'malformed_err_bytes', 'lookup_err_bytes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data']['meta_info']


                        class SiArr(_Entity_):
                            """
                            SI array in case of detail stats
                            
                            .. attribute:: data
                            
                            	Stats counter for this index
                            	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data>`
                            
                            	**config**\: False
                            
                            .. attribute:: si
                            
                            	Service index
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'pbr-vservice-mgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr, self).__init__()

                                self.yang_name = "si-arr"
                                self.yang_parent_name = "summarized"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("data", ("data", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data))])
                                self._leafs = OrderedDict([
                                    ('si', (YLeaf(YType.uint8, 'si'), ['int'])),
                                ])
                                self.si = None

                                self.data = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data()
                                self.data.parent = self
                                self._children_name_map["data"] = "data"
                                self._segment_path = lambda: "si-arr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr, ['si'], name, value)


                            class Data(_Entity_):
                                """
                                Stats counter for this index
                                
                                .. attribute:: spi_si
                                
                                	SF/SFF stats
                                	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi>`
                                
                                	**config**\: False
                                
                                .. attribute:: term
                                
                                	Terminate stats
                                	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term>`
                                
                                	**config**\: False
                                
                                .. attribute:: type
                                
                                	type
                                	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.VsNshStats>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data, self).__init__()

                                    self.yang_name = "data"
                                    self.yang_parent_name = "si-arr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("spi-si", ("spi_si", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi)), ("term", ("term", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term))])
                                    self._leafs = OrderedDict([
                                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStats', '')])),
                                    ])
                                    self.type = None

                                    self.spi_si = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi()
                                    self.spi_si.parent = self
                                    self._children_name_map["spi_si"] = "spi-si"

                                    self.term = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term()
                                    self.term.parent = self
                                    self._children_name_map["term"] = "term"
                                    self._segment_path = lambda: "data"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data, ['type'], name, value)


                                class SpiSi(_Entity_):
                                    """
                                    SF/SFF stats
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-mgr-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi, self).__init__()

                                        self.yang_name = "spi-si"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                            ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                        ])
                                        self.processed_pkts = None
                                        self.processed_bytes = None
                                        self._segment_path = lambda: "spi-si"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi']['meta_info']


                                class Term(_Entity_):
                                    """
                                    Terminate stats
                                    
                                    .. attribute:: terminated_pkts
                                    
                                    	Number of terminated packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: terminated_bytes
                                    
                                    	Total bytes terminated
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-mgr-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term, self).__init__()

                                        self.yang_name = "term"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('terminated_pkts', (YLeaf(YType.uint64, 'terminated-pkts'), ['int'])),
                                            ('terminated_bytes', (YLeaf(YType.uint64, 'terminated-bytes'), ['int'])),
                                        ])
                                        self.terminated_pkts = None
                                        self.terminated_bytes = None
                                        self._segment_path = lambda: "term"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats']['meta_info']


                class ServiceIndexes(_Entity_):
                    """
                    Service Index Belonging to Path
                    
                    .. attribute:: service_index
                    
                    	Service index operational data belonging to this path
                    	**type**\: list of  		 :py:class:`ServiceIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'pbr-vservice-mgr-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes, self).__init__()

                        self.yang_name = "service-indexes"
                        self.yang_parent_name = "path-id"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("service-index", ("service_index", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex))])
                        self._leafs = OrderedDict()

                        self.service_index = YList(self)
                        self._segment_path = lambda: "service-indexes"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes, [], name, value)


                    class ServiceIndex(_Entity_):
                        """
                        Service index operational data belonging to
                        this path
                        
                        .. attribute:: index  (key)
                        
                        	Service Index
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        	**config**\: False
                        
                        .. attribute:: data
                        
                        	Statistics data
                        	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data>`
                        
                        	**config**\: False
                        
                        .. attribute:: si_arr
                        
                        	SI array in case of detail stats
                        	**type**\: list of  		 :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex, self).__init__()

                            self.yang_name = "service-index"
                            self.yang_parent_name = "service-indexes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['index']
                            self._child_classes = OrderedDict([("data", ("data", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data)), ("si-arr", ("si_arr", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr))])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                            ])
                            self.index = None

                            self.data = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data()
                            self.data.parent = self
                            self._children_name_map["data"] = "data"

                            self.si_arr = YList(self)
                            self._segment_path = lambda: "service-index" + "[index='" + str(self.index) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex, ['index'], name, value)


                        class Data(_Entity_):
                            """
                            Statistics data
                            
                            .. attribute:: sfp
                            
                            	SFP stats
                            	**type**\:  :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp>`
                            
                            	**config**\: False
                            
                            .. attribute:: spi_si
                            
                            	SPI SI stats
                            	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi>`
                            
                            	**config**\: False
                            
                            .. attribute:: term
                            
                            	Terminate stats
                            	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term>`
                            
                            	**config**\: False
                            
                            .. attribute:: sf
                            
                            	Service function stats
                            	**type**\:  :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf>`
                            
                            	**config**\: False
                            
                            .. attribute:: sff
                            
                            	Service function forwarder stats
                            	**type**\:  :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff>`
                            
                            	**config**\: False
                            
                            .. attribute:: sff_local
                            
                            	Local service function forwarder stats
                            	**type**\:  :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal>`
                            
                            	**config**\: False
                            
                            .. attribute:: type
                            
                            	type
                            	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.VsNshStats>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'pbr-vservice-mgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data, self).__init__()

                                self.yang_name = "data"
                                self.yang_parent_name = "service-index"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("sfp", ("sfp", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp)), ("spi-si", ("spi_si", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi)), ("term", ("term", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term)), ("sf", ("sf", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf)), ("sff", ("sff", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff)), ("sff-local", ("sff_local", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal))])
                                self._leafs = OrderedDict([
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStats', '')])),
                                ])
                                self.type = None

                                self.sfp = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp()
                                self.sfp.parent = self
                                self._children_name_map["sfp"] = "sfp"

                                self.spi_si = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi()
                                self.spi_si.parent = self
                                self._children_name_map["spi_si"] = "spi-si"

                                self.term = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term()
                                self.term.parent = self
                                self._children_name_map["term"] = "term"

                                self.sf = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf()
                                self.sf.parent = self
                                self._children_name_map["sf"] = "sf"

                                self.sff = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff()
                                self.sff.parent = self
                                self._children_name_map["sff"] = "sff"

                                self.sff_local = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal()
                                self.sff_local.parent = self
                                self._children_name_map["sff_local"] = "sff-local"
                                self._segment_path = lambda: "data"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data, ['type'], name, value)


                            class Sfp(_Entity_):
                                """
                                SFP stats
                                
                                .. attribute:: spi_si
                                
                                	Service index counters
                                	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi>`
                                
                                	**config**\: False
                                
                                .. attribute:: term
                                
                                	Terminate counters
                                	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp, self).__init__()

                                    self.yang_name = "sfp"
                                    self.yang_parent_name = "data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("spi-si", ("spi_si", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi)), ("term", ("term", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term))])
                                    self._leafs = OrderedDict()

                                    self.spi_si = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi()
                                    self.spi_si.parent = self
                                    self._children_name_map["spi_si"] = "spi-si"

                                    self.term = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term()
                                    self.term.parent = self
                                    self._children_name_map["term"] = "term"
                                    self._segment_path = lambda: "sfp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp, [], name, value)


                                class SpiSi(_Entity_):
                                    """
                                    Service index counters
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-mgr-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi, self).__init__()

                                        self.yang_name = "spi-si"
                                        self.yang_parent_name = "sfp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                            ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                        ])
                                        self.processed_pkts = None
                                        self.processed_bytes = None
                                        self._segment_path = lambda: "spi-si"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi']['meta_info']


                                class Term(_Entity_):
                                    """
                                    Terminate counters
                                    
                                    .. attribute:: terminated_pkts
                                    
                                    	Number of terminated packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: terminated_bytes
                                    
                                    	Total bytes terminated
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-mgr-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term, self).__init__()

                                        self.yang_name = "term"
                                        self.yang_parent_name = "sfp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('terminated_pkts', (YLeaf(YType.uint64, 'terminated-pkts'), ['int'])),
                                            ('terminated_bytes', (YLeaf(YType.uint64, 'terminated-bytes'), ['int'])),
                                        ])
                                        self.terminated_pkts = None
                                        self.terminated_bytes = None
                                        self._segment_path = lambda: "term"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp']['meta_info']


                            class SpiSi(_Entity_):
                                """
                                SPI SI stats
                                
                                .. attribute:: processed_pkts
                                
                                	Number of packets processed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: processed_bytes
                                
                                	Total bytes processed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi, self).__init__()

                                    self.yang_name = "spi-si"
                                    self.yang_parent_name = "data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                        ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                    ])
                                    self.processed_pkts = None
                                    self.processed_bytes = None
                                    self._segment_path = lambda: "spi-si"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi']['meta_info']


                            class Term(_Entity_):
                                """
                                Terminate stats
                                
                                .. attribute:: terminated_pkts
                                
                                	Number of terminated packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: terminated_bytes
                                
                                	Total bytes terminated
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term, self).__init__()

                                    self.yang_name = "term"
                                    self.yang_parent_name = "data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('terminated_pkts', (YLeaf(YType.uint64, 'terminated-pkts'), ['int'])),
                                        ('terminated_bytes', (YLeaf(YType.uint64, 'terminated-bytes'), ['int'])),
                                    ])
                                    self.terminated_pkts = None
                                    self.terminated_bytes = None
                                    self._segment_path = lambda: "term"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term']['meta_info']


                            class Sf(_Entity_):
                                """
                                Service function stats
                                
                                .. attribute:: processed_pkts
                                
                                	Number of packets processed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: processed_bytes
                                
                                	Total bytes processed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf, self).__init__()

                                    self.yang_name = "sf"
                                    self.yang_parent_name = "data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                        ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                    ])
                                    self.processed_pkts = None
                                    self.processed_bytes = None
                                    self._segment_path = lambda: "sf"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf, ['processed_pkts', 'processed_bytes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf']['meta_info']


                            class Sff(_Entity_):
                                """
                                Service function forwarder stats
                                
                                .. attribute:: processed_pkts
                                
                                	Number of packets processed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: processed_bytes
                                
                                	Total bytes processed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff, self).__init__()

                                    self.yang_name = "sff"
                                    self.yang_parent_name = "data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                        ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                    ])
                                    self.processed_pkts = None
                                    self.processed_bytes = None
                                    self._segment_path = lambda: "sff"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff, ['processed_pkts', 'processed_bytes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff']['meta_info']


                            class SffLocal(_Entity_):
                                """
                                Local service function forwarder stats
                                
                                .. attribute:: malformed_err_pkts
                                
                                	Number of packets with invalid NSH header
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: lookup_err_pkts
                                
                                	Number of packets with unknown spi\-si
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: malformed_err_bytes
                                
                                	Total bytes with invalid NSH header
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                .. attribute:: lookup_err_bytes
                                
                                	Total bytes with unknown spi\-si
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal, self).__init__()

                                    self.yang_name = "sff-local"
                                    self.yang_parent_name = "data"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('malformed_err_pkts', (YLeaf(YType.uint64, 'malformed-err-pkts'), ['int'])),
                                        ('lookup_err_pkts', (YLeaf(YType.uint64, 'lookup-err-pkts'), ['int'])),
                                        ('malformed_err_bytes', (YLeaf(YType.uint64, 'malformed-err-bytes'), ['int'])),
                                        ('lookup_err_bytes', (YLeaf(YType.uint64, 'lookup-err-bytes'), ['int'])),
                                    ])
                                    self.malformed_err_pkts = None
                                    self.lookup_err_pkts = None
                                    self.malformed_err_bytes = None
                                    self.lookup_err_bytes = None
                                    self._segment_path = lambda: "sff-local"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal, ['malformed_err_pkts', 'lookup_err_pkts', 'malformed_err_bytes', 'lookup_err_bytes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data']['meta_info']


                        class SiArr(_Entity_):
                            """
                            SI array in case of detail stats
                            
                            .. attribute:: data
                            
                            	Stats counter for this index
                            	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data>`
                            
                            	**config**\: False
                            
                            .. attribute:: si
                            
                            	Service index
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'pbr-vservice-mgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr, self).__init__()

                                self.yang_name = "si-arr"
                                self.yang_parent_name = "service-index"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("data", ("data", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data))])
                                self._leafs = OrderedDict([
                                    ('si', (YLeaf(YType.uint8, 'si'), ['int'])),
                                ])
                                self.si = None

                                self.data = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data()
                                self.data.parent = self
                                self._children_name_map["data"] = "data"
                                self._segment_path = lambda: "si-arr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr, ['si'], name, value)


                            class Data(_Entity_):
                                """
                                Stats counter for this index
                                
                                .. attribute:: spi_si
                                
                                	SF/SFF stats
                                	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi>`
                                
                                	**config**\: False
                                
                                .. attribute:: term
                                
                                	Terminate stats
                                	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term>`
                                
                                	**config**\: False
                                
                                .. attribute:: type
                                
                                	type
                                	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.VsNshStats>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'pbr-vservice-mgr-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data, self).__init__()

                                    self.yang_name = "data"
                                    self.yang_parent_name = "si-arr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("spi-si", ("spi_si", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi)), ("term", ("term", GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term))])
                                    self._leafs = OrderedDict([
                                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStats', '')])),
                                    ])
                                    self.type = None

                                    self.spi_si = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi()
                                    self.spi_si.parent = self
                                    self._children_name_map["spi_si"] = "spi-si"

                                    self.term = GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term()
                                    self.term.parent = self
                                    self._children_name_map["term"] = "term"
                                    self._segment_path = lambda: "data"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data, ['type'], name, value)


                                class SpiSi(_Entity_):
                                    """
                                    SF/SFF stats
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-mgr-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi, self).__init__()

                                        self.yang_name = "spi-si"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                            ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                        ])
                                        self.processed_pkts = None
                                        self.processed_bytes = None
                                        self._segment_path = lambda: "spi-si"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi']['meta_info']


                                class Term(_Entity_):
                                    """
                                    Terminate stats
                                    
                                    .. attribute:: terminated_pkts
                                    
                                    	Number of terminated packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: terminated_bytes
                                    
                                    	Total bytes terminated
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-mgr-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term, self).__init__()

                                        self.yang_name = "term"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('terminated_pkts', (YLeaf(YType.uint64, 'terminated-pkts'), ['int'])),
                                            ('terminated_bytes', (YLeaf(YType.uint64, 'terminated-bytes'), ['int'])),
                                        ])
                                        self.terminated_pkts = None
                                        self.terminated_bytes = None
                                        self._segment_path = lambda: "term"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath']['meta_info']


    class ServiceFunction(_Entity_):
        """
        Service Function operational data
        
        .. attribute:: sf_names
        
        	List of Service Function Names
        	**type**\:  :py:class:`SfNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunction.SfNames>`
        
        	**config**\: False
        
        

        """

        _prefix = 'pbr-vservice-mgr-oper'
        _revision = '2017-05-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(GlobalServiceFunctionChaining.ServiceFunction, self).__init__()

            self.yang_name = "service-function"
            self.yang_parent_name = "global-service-function-chaining"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("sf-names", ("sf_names", GlobalServiceFunctionChaining.ServiceFunction.SfNames))])
            self._leafs = OrderedDict()

            self.sf_names = GlobalServiceFunctionChaining.ServiceFunction.SfNames()
            self.sf_names.parent = self
            self._children_name_map["sf_names"] = "sf-names"
            self._segment_path = lambda: "service-function"
            self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunction, [], name, value)


        class SfNames(_Entity_):
            """
            List of Service Function Names
            
            .. attribute:: sf_name
            
            	Name of Service Function
            	**type**\: list of  		 :py:class:`SfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName>`
            
            	**config**\: False
            
            

            """

            _prefix = 'pbr-vservice-mgr-oper'
            _revision = '2017-05-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(GlobalServiceFunctionChaining.ServiceFunction.SfNames, self).__init__()

                self.yang_name = "sf-names"
                self.yang_parent_name = "service-function"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("sf-name", ("sf_name", GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName))])
                self._leafs = OrderedDict()

                self.sf_name = YList(self)
                self._segment_path = lambda: "sf-names"
                self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunction.SfNames, [], name, value)


            class SfName(_Entity_):
                """
                Name of Service Function
                
                .. attribute:: name  (key)
                
                	Name
                	**type**\: str
                
                	**length:** 1..32
                
                	**config**\: False
                
                .. attribute:: data
                
                	Statistics data
                	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data>`
                
                	**config**\: False
                
                .. attribute:: si_arr
                
                	SI array in case of detail stats
                	**type**\: list of  		 :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr>`
                
                	**config**\: False
                
                

                """

                _prefix = 'pbr-vservice-mgr-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName, self).__init__()

                    self.yang_name = "sf-name"
                    self.yang_parent_name = "sf-names"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("data", ("data", GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data)), ("si-arr", ("si_arr", GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.data = GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data()
                    self.data.parent = self
                    self._children_name_map["data"] = "data"

                    self.si_arr = YList(self)
                    self._segment_path = lambda: "sf-name" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function/sf-names/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName, ['name'], name, value)


                class Data(_Entity_):
                    """
                    Statistics data
                    
                    .. attribute:: sfp
                    
                    	SFP stats
                    	**type**\:  :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp>`
                    
                    	**config**\: False
                    
                    .. attribute:: spi_si
                    
                    	SPI SI stats
                    	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SpiSi>`
                    
                    	**config**\: False
                    
                    .. attribute:: term
                    
                    	Terminate stats
                    	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Term>`
                    
                    	**config**\: False
                    
                    .. attribute:: sf
                    
                    	Service function stats
                    	**type**\:  :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sf>`
                    
                    	**config**\: False
                    
                    .. attribute:: sff
                    
                    	Service function forwarder stats
                    	**type**\:  :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sff>`
                    
                    	**config**\: False
                    
                    .. attribute:: sff_local
                    
                    	Local service function forwarder stats
                    	**type**\:  :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SffLocal>`
                    
                    	**config**\: False
                    
                    .. attribute:: type
                    
                    	type
                    	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.VsNshStats>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'pbr-vservice-mgr-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data, self).__init__()

                        self.yang_name = "data"
                        self.yang_parent_name = "sf-name"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sfp", ("sfp", GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp)), ("spi-si", ("spi_si", GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SpiSi)), ("term", ("term", GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Term)), ("sf", ("sf", GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sf)), ("sff", ("sff", GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sff)), ("sff-local", ("sff_local", GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SffLocal))])
                        self._leafs = OrderedDict([
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStats', '')])),
                        ])
                        self.type = None

                        self.sfp = GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp()
                        self.sfp.parent = self
                        self._children_name_map["sfp"] = "sfp"

                        self.spi_si = GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SpiSi()
                        self.spi_si.parent = self
                        self._children_name_map["spi_si"] = "spi-si"

                        self.term = GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Term()
                        self.term.parent = self
                        self._children_name_map["term"] = "term"

                        self.sf = GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sf()
                        self.sf.parent = self
                        self._children_name_map["sf"] = "sf"

                        self.sff = GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sff()
                        self.sff.parent = self
                        self._children_name_map["sff"] = "sff"

                        self.sff_local = GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SffLocal()
                        self.sff_local.parent = self
                        self._children_name_map["sff_local"] = "sff-local"
                        self._segment_path = lambda: "data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data, ['type'], name, value)


                    class Sfp(_Entity_):
                        """
                        SFP stats
                        
                        .. attribute:: spi_si
                        
                        	Service index counters
                        	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi>`
                        
                        	**config**\: False
                        
                        .. attribute:: term
                        
                        	Terminate counters
                        	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.Term>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp, self).__init__()

                            self.yang_name = "sfp"
                            self.yang_parent_name = "data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("spi-si", ("spi_si", GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi)), ("term", ("term", GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.Term))])
                            self._leafs = OrderedDict()

                            self.spi_si = GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi()
                            self.spi_si.parent = self
                            self._children_name_map["spi_si"] = "spi-si"

                            self.term = GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.Term()
                            self.term.parent = self
                            self._children_name_map["term"] = "term"
                            self._segment_path = lambda: "sfp"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp, [], name, value)


                        class SpiSi(_Entity_):
                            """
                            Service index counters
                            
                            .. attribute:: processed_pkts
                            
                            	Number of packets processed
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: processed_bytes
                            
                            	Total bytes processed
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'pbr-vservice-mgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi, self).__init__()

                                self.yang_name = "spi-si"
                                self.yang_parent_name = "sfp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                    ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                ])
                                self.processed_pkts = None
                                self.processed_bytes = None
                                self._segment_path = lambda: "spi-si"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi']['meta_info']


                        class Term(_Entity_):
                            """
                            Terminate counters
                            
                            .. attribute:: terminated_pkts
                            
                            	Number of terminated packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: terminated_bytes
                            
                            	Total bytes terminated
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'pbr-vservice-mgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.Term, self).__init__()

                                self.yang_name = "term"
                                self.yang_parent_name = "sfp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('terminated_pkts', (YLeaf(YType.uint64, 'terminated-pkts'), ['int'])),
                                    ('terminated_bytes', (YLeaf(YType.uint64, 'terminated-bytes'), ['int'])),
                                ])
                                self.terminated_pkts = None
                                self.terminated_bytes = None
                                self._segment_path = lambda: "term"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.Term']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp']['meta_info']


                    class SpiSi(_Entity_):
                        """
                        SPI SI stats
                        
                        .. attribute:: processed_pkts
                        
                        	Number of packets processed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: processed_bytes
                        
                        	Total bytes processed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SpiSi, self).__init__()

                            self.yang_name = "spi-si"
                            self.yang_parent_name = "data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                            ])
                            self.processed_pkts = None
                            self.processed_bytes = None
                            self._segment_path = lambda: "spi-si"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SpiSi']['meta_info']


                    class Term(_Entity_):
                        """
                        Terminate stats
                        
                        .. attribute:: terminated_pkts
                        
                        	Number of terminated packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: terminated_bytes
                        
                        	Total bytes terminated
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Term, self).__init__()

                            self.yang_name = "term"
                            self.yang_parent_name = "data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('terminated_pkts', (YLeaf(YType.uint64, 'terminated-pkts'), ['int'])),
                                ('terminated_bytes', (YLeaf(YType.uint64, 'terminated-bytes'), ['int'])),
                            ])
                            self.terminated_pkts = None
                            self.terminated_bytes = None
                            self._segment_path = lambda: "term"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Term']['meta_info']


                    class Sf(_Entity_):
                        """
                        Service function stats
                        
                        .. attribute:: processed_pkts
                        
                        	Number of packets processed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: processed_bytes
                        
                        	Total bytes processed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sf, self).__init__()

                            self.yang_name = "sf"
                            self.yang_parent_name = "data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                            ])
                            self.processed_pkts = None
                            self.processed_bytes = None
                            self._segment_path = lambda: "sf"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sf, ['processed_pkts', 'processed_bytes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sf']['meta_info']


                    class Sff(_Entity_):
                        """
                        Service function forwarder stats
                        
                        .. attribute:: processed_pkts
                        
                        	Number of packets processed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: processed_bytes
                        
                        	Total bytes processed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sff, self).__init__()

                            self.yang_name = "sff"
                            self.yang_parent_name = "data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                            ])
                            self.processed_pkts = None
                            self.processed_bytes = None
                            self._segment_path = lambda: "sff"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sff, ['processed_pkts', 'processed_bytes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sff']['meta_info']


                    class SffLocal(_Entity_):
                        """
                        Local service function forwarder stats
                        
                        .. attribute:: malformed_err_pkts
                        
                        	Number of packets with invalid NSH header
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: lookup_err_pkts
                        
                        	Number of packets with unknown spi\-si
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: malformed_err_bytes
                        
                        	Total bytes with invalid NSH header
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        .. attribute:: lookup_err_bytes
                        
                        	Total bytes with unknown spi\-si
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SffLocal, self).__init__()

                            self.yang_name = "sff-local"
                            self.yang_parent_name = "data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('malformed_err_pkts', (YLeaf(YType.uint64, 'malformed-err-pkts'), ['int'])),
                                ('lookup_err_pkts', (YLeaf(YType.uint64, 'lookup-err-pkts'), ['int'])),
                                ('malformed_err_bytes', (YLeaf(YType.uint64, 'malformed-err-bytes'), ['int'])),
                                ('lookup_err_bytes', (YLeaf(YType.uint64, 'lookup-err-bytes'), ['int'])),
                            ])
                            self.malformed_err_pkts = None
                            self.lookup_err_pkts = None
                            self.malformed_err_bytes = None
                            self.lookup_err_bytes = None
                            self._segment_path = lambda: "sff-local"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SffLocal, ['malformed_err_pkts', 'lookup_err_pkts', 'malformed_err_bytes', 'lookup_err_bytes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SffLocal']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data']['meta_info']


                class SiArr(_Entity_):
                    """
                    SI array in case of detail stats
                    
                    .. attribute:: data
                    
                    	Stats counter for this index
                    	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data>`
                    
                    	**config**\: False
                    
                    .. attribute:: si
                    
                    	Service index
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'pbr-vservice-mgr-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr, self).__init__()

                        self.yang_name = "si-arr"
                        self.yang_parent_name = "sf-name"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("data", ("data", GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data))])
                        self._leafs = OrderedDict([
                            ('si', (YLeaf(YType.uint8, 'si'), ['int'])),
                        ])
                        self.si = None

                        self.data = GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data()
                        self.data.parent = self
                        self._children_name_map["data"] = "data"
                        self._segment_path = lambda: "si-arr"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr, ['si'], name, value)


                    class Data(_Entity_):
                        """
                        Stats counter for this index
                        
                        .. attribute:: spi_si
                        
                        	SF/SFF stats
                        	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi>`
                        
                        	**config**\: False
                        
                        .. attribute:: term
                        
                        	Terminate stats
                        	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.Term>`
                        
                        	**config**\: False
                        
                        .. attribute:: type
                        
                        	type
                        	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.VsNshStats>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data, self).__init__()

                            self.yang_name = "data"
                            self.yang_parent_name = "si-arr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("spi-si", ("spi_si", GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi)), ("term", ("term", GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.Term))])
                            self._leafs = OrderedDict([
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStats', '')])),
                            ])
                            self.type = None

                            self.spi_si = GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi()
                            self.spi_si.parent = self
                            self._children_name_map["spi_si"] = "spi-si"

                            self.term = GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.Term()
                            self.term.parent = self
                            self._children_name_map["term"] = "term"
                            self._segment_path = lambda: "data"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data, ['type'], name, value)


                        class SpiSi(_Entity_):
                            """
                            SF/SFF stats
                            
                            .. attribute:: processed_pkts
                            
                            	Number of packets processed
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: processed_bytes
                            
                            	Total bytes processed
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'pbr-vservice-mgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi, self).__init__()

                                self.yang_name = "spi-si"
                                self.yang_parent_name = "data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                    ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                ])
                                self.processed_pkts = None
                                self.processed_bytes = None
                                self._segment_path = lambda: "spi-si"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi']['meta_info']


                        class Term(_Entity_):
                            """
                            Terminate stats
                            
                            .. attribute:: terminated_pkts
                            
                            	Number of terminated packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: terminated_bytes
                            
                            	Total bytes terminated
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'pbr-vservice-mgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.Term, self).__init__()

                                self.yang_name = "term"
                                self.yang_parent_name = "data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('terminated_pkts', (YLeaf(YType.uint64, 'terminated-pkts'), ['int'])),
                                    ('terminated_bytes', (YLeaf(YType.uint64, 'terminated-bytes'), ['int'])),
                                ])
                                self.terminated_pkts = None
                                self.terminated_bytes = None
                                self._segment_path = lambda: "term"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.Term']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunction']['meta_info']


    class ServiceFunctionForwarder(_Entity_):
        """
        Service Function Forwarder operational data
        
        .. attribute:: sff_names
        
        	List of Service Function Forwarder Names
        	**type**\:  :py:class:`SffNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames>`
        
        	**config**\: False
        
        .. attribute:: local
        
        	Local Service Function Forwarder operational data
        	**type**\:  :py:class:`Local <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local>`
        
        	**config**\: False
        
        

        """

        _prefix = 'pbr-vservice-mgr-oper'
        _revision = '2017-05-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(GlobalServiceFunctionChaining.ServiceFunctionForwarder, self).__init__()

            self.yang_name = "service-function-forwarder"
            self.yang_parent_name = "global-service-function-chaining"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("sff-names", ("sff_names", GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames)), ("local", ("local", GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local))])
            self._leafs = OrderedDict()

            self.sff_names = GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames()
            self.sff_names.parent = self
            self._children_name_map["sff_names"] = "sff-names"

            self.local = GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local()
            self.local.parent = self
            self._children_name_map["local"] = "local"
            self._segment_path = lambda: "service-function-forwarder"
            self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder, [], name, value)


        class SffNames(_Entity_):
            """
            List of Service Function Forwarder Names
            
            .. attribute:: sff_name
            
            	Name of Service Function Forwarder
            	**type**\: list of  		 :py:class:`SffName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName>`
            
            	**config**\: False
            
            

            """

            _prefix = 'pbr-vservice-mgr-oper'
            _revision = '2017-05-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames, self).__init__()

                self.yang_name = "sff-names"
                self.yang_parent_name = "service-function-forwarder"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("sff-name", ("sff_name", GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName))])
                self._leafs = OrderedDict()

                self.sff_name = YList(self)
                self._segment_path = lambda: "sff-names"
                self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-forwarder/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames, [], name, value)


            class SffName(_Entity_):
                """
                Name of Service Function Forwarder
                
                .. attribute:: name  (key)
                
                	Name
                	**type**\: str
                
                	**length:** 1..32
                
                	**config**\: False
                
                .. attribute:: data
                
                	Statistics data
                	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data>`
                
                	**config**\: False
                
                .. attribute:: si_arr
                
                	SI array in case of detail stats
                	**type**\: list of  		 :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr>`
                
                	**config**\: False
                
                

                """

                _prefix = 'pbr-vservice-mgr-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName, self).__init__()

                    self.yang_name = "sff-name"
                    self.yang_parent_name = "sff-names"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("data", ("data", GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data)), ("si-arr", ("si_arr", GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.data = GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data()
                    self.data.parent = self
                    self._children_name_map["data"] = "data"

                    self.si_arr = YList(self)
                    self._segment_path = lambda: "sff-name" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-forwarder/sff-names/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName, ['name'], name, value)


                class Data(_Entity_):
                    """
                    Statistics data
                    
                    .. attribute:: sfp
                    
                    	SFP stats
                    	**type**\:  :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp>`
                    
                    	**config**\: False
                    
                    .. attribute:: spi_si
                    
                    	SPI SI stats
                    	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi>`
                    
                    	**config**\: False
                    
                    .. attribute:: term
                    
                    	Terminate stats
                    	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Term>`
                    
                    	**config**\: False
                    
                    .. attribute:: sf
                    
                    	Service function stats
                    	**type**\:  :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sf>`
                    
                    	**config**\: False
                    
                    .. attribute:: sff
                    
                    	Service function forwarder stats
                    	**type**\:  :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sff>`
                    
                    	**config**\: False
                    
                    .. attribute:: sff_local
                    
                    	Local service function forwarder stats
                    	**type**\:  :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal>`
                    
                    	**config**\: False
                    
                    .. attribute:: type
                    
                    	type
                    	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.VsNshStats>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'pbr-vservice-mgr-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data, self).__init__()

                        self.yang_name = "data"
                        self.yang_parent_name = "sff-name"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sfp", ("sfp", GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp)), ("spi-si", ("spi_si", GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi)), ("term", ("term", GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Term)), ("sf", ("sf", GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sf)), ("sff", ("sff", GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sff)), ("sff-local", ("sff_local", GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal))])
                        self._leafs = OrderedDict([
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStats', '')])),
                        ])
                        self.type = None

                        self.sfp = GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp()
                        self.sfp.parent = self
                        self._children_name_map["sfp"] = "sfp"

                        self.spi_si = GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi()
                        self.spi_si.parent = self
                        self._children_name_map["spi_si"] = "spi-si"

                        self.term = GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Term()
                        self.term.parent = self
                        self._children_name_map["term"] = "term"

                        self.sf = GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sf()
                        self.sf.parent = self
                        self._children_name_map["sf"] = "sf"

                        self.sff = GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sff()
                        self.sff.parent = self
                        self._children_name_map["sff"] = "sff"

                        self.sff_local = GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal()
                        self.sff_local.parent = self
                        self._children_name_map["sff_local"] = "sff-local"
                        self._segment_path = lambda: "data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data, ['type'], name, value)


                    class Sfp(_Entity_):
                        """
                        SFP stats
                        
                        .. attribute:: spi_si
                        
                        	Service index counters
                        	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi>`
                        
                        	**config**\: False
                        
                        .. attribute:: term
                        
                        	Terminate counters
                        	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp, self).__init__()

                            self.yang_name = "sfp"
                            self.yang_parent_name = "data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("spi-si", ("spi_si", GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi)), ("term", ("term", GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term))])
                            self._leafs = OrderedDict()

                            self.spi_si = GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi()
                            self.spi_si.parent = self
                            self._children_name_map["spi_si"] = "spi-si"

                            self.term = GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term()
                            self.term.parent = self
                            self._children_name_map["term"] = "term"
                            self._segment_path = lambda: "sfp"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp, [], name, value)


                        class SpiSi(_Entity_):
                            """
                            Service index counters
                            
                            .. attribute:: processed_pkts
                            
                            	Number of packets processed
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: processed_bytes
                            
                            	Total bytes processed
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'pbr-vservice-mgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi, self).__init__()

                                self.yang_name = "spi-si"
                                self.yang_parent_name = "sfp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                    ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                ])
                                self.processed_pkts = None
                                self.processed_bytes = None
                                self._segment_path = lambda: "spi-si"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi']['meta_info']


                        class Term(_Entity_):
                            """
                            Terminate counters
                            
                            .. attribute:: terminated_pkts
                            
                            	Number of terminated packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: terminated_bytes
                            
                            	Total bytes terminated
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'pbr-vservice-mgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term, self).__init__()

                                self.yang_name = "term"
                                self.yang_parent_name = "sfp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('terminated_pkts', (YLeaf(YType.uint64, 'terminated-pkts'), ['int'])),
                                    ('terminated_bytes', (YLeaf(YType.uint64, 'terminated-bytes'), ['int'])),
                                ])
                                self.terminated_pkts = None
                                self.terminated_bytes = None
                                self._segment_path = lambda: "term"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp']['meta_info']


                    class SpiSi(_Entity_):
                        """
                        SPI SI stats
                        
                        .. attribute:: processed_pkts
                        
                        	Number of packets processed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: processed_bytes
                        
                        	Total bytes processed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi, self).__init__()

                            self.yang_name = "spi-si"
                            self.yang_parent_name = "data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                            ])
                            self.processed_pkts = None
                            self.processed_bytes = None
                            self._segment_path = lambda: "spi-si"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi']['meta_info']


                    class Term(_Entity_):
                        """
                        Terminate stats
                        
                        .. attribute:: terminated_pkts
                        
                        	Number of terminated packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: terminated_bytes
                        
                        	Total bytes terminated
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Term, self).__init__()

                            self.yang_name = "term"
                            self.yang_parent_name = "data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('terminated_pkts', (YLeaf(YType.uint64, 'terminated-pkts'), ['int'])),
                                ('terminated_bytes', (YLeaf(YType.uint64, 'terminated-bytes'), ['int'])),
                            ])
                            self.terminated_pkts = None
                            self.terminated_bytes = None
                            self._segment_path = lambda: "term"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Term']['meta_info']


                    class Sf(_Entity_):
                        """
                        Service function stats
                        
                        .. attribute:: processed_pkts
                        
                        	Number of packets processed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: processed_bytes
                        
                        	Total bytes processed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sf, self).__init__()

                            self.yang_name = "sf"
                            self.yang_parent_name = "data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                            ])
                            self.processed_pkts = None
                            self.processed_bytes = None
                            self._segment_path = lambda: "sf"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sf, ['processed_pkts', 'processed_bytes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sf']['meta_info']


                    class Sff(_Entity_):
                        """
                        Service function forwarder stats
                        
                        .. attribute:: processed_pkts
                        
                        	Number of packets processed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: processed_bytes
                        
                        	Total bytes processed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sff, self).__init__()

                            self.yang_name = "sff"
                            self.yang_parent_name = "data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                            ])
                            self.processed_pkts = None
                            self.processed_bytes = None
                            self._segment_path = lambda: "sff"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sff, ['processed_pkts', 'processed_bytes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sff']['meta_info']


                    class SffLocal(_Entity_):
                        """
                        Local service function forwarder stats
                        
                        .. attribute:: malformed_err_pkts
                        
                        	Number of packets with invalid NSH header
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: lookup_err_pkts
                        
                        	Number of packets with unknown spi\-si
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: malformed_err_bytes
                        
                        	Total bytes with invalid NSH header
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        .. attribute:: lookup_err_bytes
                        
                        	Total bytes with unknown spi\-si
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal, self).__init__()

                            self.yang_name = "sff-local"
                            self.yang_parent_name = "data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('malformed_err_pkts', (YLeaf(YType.uint64, 'malformed-err-pkts'), ['int'])),
                                ('lookup_err_pkts', (YLeaf(YType.uint64, 'lookup-err-pkts'), ['int'])),
                                ('malformed_err_bytes', (YLeaf(YType.uint64, 'malformed-err-bytes'), ['int'])),
                                ('lookup_err_bytes', (YLeaf(YType.uint64, 'lookup-err-bytes'), ['int'])),
                            ])
                            self.malformed_err_pkts = None
                            self.lookup_err_pkts = None
                            self.malformed_err_bytes = None
                            self.lookup_err_bytes = None
                            self._segment_path = lambda: "sff-local"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal, ['malformed_err_pkts', 'lookup_err_pkts', 'malformed_err_bytes', 'lookup_err_bytes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data']['meta_info']


                class SiArr(_Entity_):
                    """
                    SI array in case of detail stats
                    
                    .. attribute:: data
                    
                    	Stats counter for this index
                    	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data>`
                    
                    	**config**\: False
                    
                    .. attribute:: si
                    
                    	Service index
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'pbr-vservice-mgr-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr, self).__init__()

                        self.yang_name = "si-arr"
                        self.yang_parent_name = "sff-name"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("data", ("data", GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data))])
                        self._leafs = OrderedDict([
                            ('si', (YLeaf(YType.uint8, 'si'), ['int'])),
                        ])
                        self.si = None

                        self.data = GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data()
                        self.data.parent = self
                        self._children_name_map["data"] = "data"
                        self._segment_path = lambda: "si-arr"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr, ['si'], name, value)


                    class Data(_Entity_):
                        """
                        Stats counter for this index
                        
                        .. attribute:: spi_si
                        
                        	SF/SFF stats
                        	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi>`
                        
                        	**config**\: False
                        
                        .. attribute:: term
                        
                        	Terminate stats
                        	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term>`
                        
                        	**config**\: False
                        
                        .. attribute:: type
                        
                        	type
                        	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.VsNshStats>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data, self).__init__()

                            self.yang_name = "data"
                            self.yang_parent_name = "si-arr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("spi-si", ("spi_si", GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi)), ("term", ("term", GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term))])
                            self._leafs = OrderedDict([
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStats', '')])),
                            ])
                            self.type = None

                            self.spi_si = GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi()
                            self.spi_si.parent = self
                            self._children_name_map["spi_si"] = "spi-si"

                            self.term = GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term()
                            self.term.parent = self
                            self._children_name_map["term"] = "term"
                            self._segment_path = lambda: "data"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data, ['type'], name, value)


                        class SpiSi(_Entity_):
                            """
                            SF/SFF stats
                            
                            .. attribute:: processed_pkts
                            
                            	Number of packets processed
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: processed_bytes
                            
                            	Total bytes processed
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'pbr-vservice-mgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi, self).__init__()

                                self.yang_name = "spi-si"
                                self.yang_parent_name = "data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                    ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                ])
                                self.processed_pkts = None
                                self.processed_bytes = None
                                self._segment_path = lambda: "spi-si"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi']['meta_info']


                        class Term(_Entity_):
                            """
                            Terminate stats
                            
                            .. attribute:: terminated_pkts
                            
                            	Number of terminated packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: terminated_bytes
                            
                            	Total bytes terminated
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'pbr-vservice-mgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term, self).__init__()

                                self.yang_name = "term"
                                self.yang_parent_name = "data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('terminated_pkts', (YLeaf(YType.uint64, 'terminated-pkts'), ['int'])),
                                    ('terminated_bytes', (YLeaf(YType.uint64, 'terminated-bytes'), ['int'])),
                                ])
                                self.terminated_pkts = None
                                self.terminated_bytes = None
                                self._segment_path = lambda: "term"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames']['meta_info']


        class Local(_Entity_):
            """
            Local Service Function Forwarder operational
            data
            
            .. attribute:: error
            
            	Error Statistics for local service function forwarder
            	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error>`
            
            	**config**\: False
            
            

            """

            _prefix = 'pbr-vservice-mgr-oper'
            _revision = '2017-05-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local, self).__init__()

                self.yang_name = "local"
                self.yang_parent_name = "service-function-forwarder"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("error", ("error", GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error))])
                self._leafs = OrderedDict()

                self.error = GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error()
                self.error.parent = self
                self._children_name_map["error"] = "error"
                self._segment_path = lambda: "local"
                self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-forwarder/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local, [], name, value)


            class Error(_Entity_):
                """
                Error Statistics for local service function
                forwarder
                
                .. attribute:: data
                
                	Statistics data
                	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data>`
                
                	**config**\: False
                
                .. attribute:: si_arr
                
                	SI array in case of detail stats
                	**type**\: list of  		 :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr>`
                
                	**config**\: False
                
                

                """

                _prefix = 'pbr-vservice-mgr-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error, self).__init__()

                    self.yang_name = "error"
                    self.yang_parent_name = "local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("data", ("data", GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data)), ("si-arr", ("si_arr", GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr))])
                    self._leafs = OrderedDict()

                    self.data = GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data()
                    self.data.parent = self
                    self._children_name_map["data"] = "data"

                    self.si_arr = YList(self)
                    self._segment_path = lambda: "error"
                    self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-forwarder/local/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error, [], name, value)


                class Data(_Entity_):
                    """
                    Statistics data
                    
                    .. attribute:: sfp
                    
                    	SFP stats
                    	**type**\:  :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp>`
                    
                    	**config**\: False
                    
                    .. attribute:: spi_si
                    
                    	SPI SI stats
                    	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SpiSi>`
                    
                    	**config**\: False
                    
                    .. attribute:: term
                    
                    	Terminate stats
                    	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Term>`
                    
                    	**config**\: False
                    
                    .. attribute:: sf
                    
                    	Service function stats
                    	**type**\:  :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sf>`
                    
                    	**config**\: False
                    
                    .. attribute:: sff
                    
                    	Service function forwarder stats
                    	**type**\:  :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sff>`
                    
                    	**config**\: False
                    
                    .. attribute:: sff_local
                    
                    	Local service function forwarder stats
                    	**type**\:  :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SffLocal>`
                    
                    	**config**\: False
                    
                    .. attribute:: type
                    
                    	type
                    	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.VsNshStats>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'pbr-vservice-mgr-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data, self).__init__()

                        self.yang_name = "data"
                        self.yang_parent_name = "error"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sfp", ("sfp", GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp)), ("spi-si", ("spi_si", GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SpiSi)), ("term", ("term", GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Term)), ("sf", ("sf", GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sf)), ("sff", ("sff", GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sff)), ("sff-local", ("sff_local", GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SffLocal))])
                        self._leafs = OrderedDict([
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStats', '')])),
                        ])
                        self.type = None

                        self.sfp = GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp()
                        self.sfp.parent = self
                        self._children_name_map["sfp"] = "sfp"

                        self.spi_si = GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SpiSi()
                        self.spi_si.parent = self
                        self._children_name_map["spi_si"] = "spi-si"

                        self.term = GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Term()
                        self.term.parent = self
                        self._children_name_map["term"] = "term"

                        self.sf = GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sf()
                        self.sf.parent = self
                        self._children_name_map["sf"] = "sf"

                        self.sff = GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sff()
                        self.sff.parent = self
                        self._children_name_map["sff"] = "sff"

                        self.sff_local = GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SffLocal()
                        self.sff_local.parent = self
                        self._children_name_map["sff_local"] = "sff-local"
                        self._segment_path = lambda: "data"
                        self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-forwarder/local/error/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data, ['type'], name, value)


                    class Sfp(_Entity_):
                        """
                        SFP stats
                        
                        .. attribute:: spi_si
                        
                        	Service index counters
                        	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi>`
                        
                        	**config**\: False
                        
                        .. attribute:: term
                        
                        	Terminate counters
                        	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp, self).__init__()

                            self.yang_name = "sfp"
                            self.yang_parent_name = "data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("spi-si", ("spi_si", GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi)), ("term", ("term", GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term))])
                            self._leafs = OrderedDict()

                            self.spi_si = GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi()
                            self.spi_si.parent = self
                            self._children_name_map["spi_si"] = "spi-si"

                            self.term = GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term()
                            self.term.parent = self
                            self._children_name_map["term"] = "term"
                            self._segment_path = lambda: "sfp"
                            self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-forwarder/local/error/data/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp, [], name, value)


                        class SpiSi(_Entity_):
                            """
                            Service index counters
                            
                            .. attribute:: processed_pkts
                            
                            	Number of packets processed
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: processed_bytes
                            
                            	Total bytes processed
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'pbr-vservice-mgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi, self).__init__()

                                self.yang_name = "spi-si"
                                self.yang_parent_name = "sfp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                    ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                ])
                                self.processed_pkts = None
                                self.processed_bytes = None
                                self._segment_path = lambda: "spi-si"
                                self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-forwarder/local/error/data/sfp/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi']['meta_info']


                        class Term(_Entity_):
                            """
                            Terminate counters
                            
                            .. attribute:: terminated_pkts
                            
                            	Number of terminated packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: terminated_bytes
                            
                            	Total bytes terminated
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'pbr-vservice-mgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term, self).__init__()

                                self.yang_name = "term"
                                self.yang_parent_name = "sfp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('terminated_pkts', (YLeaf(YType.uint64, 'terminated-pkts'), ['int'])),
                                    ('terminated_bytes', (YLeaf(YType.uint64, 'terminated-bytes'), ['int'])),
                                ])
                                self.terminated_pkts = None
                                self.terminated_bytes = None
                                self._segment_path = lambda: "term"
                                self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-forwarder/local/error/data/sfp/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp']['meta_info']


                    class SpiSi(_Entity_):
                        """
                        SPI SI stats
                        
                        .. attribute:: processed_pkts
                        
                        	Number of packets processed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: processed_bytes
                        
                        	Total bytes processed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SpiSi, self).__init__()

                            self.yang_name = "spi-si"
                            self.yang_parent_name = "data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                            ])
                            self.processed_pkts = None
                            self.processed_bytes = None
                            self._segment_path = lambda: "spi-si"
                            self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-forwarder/local/error/data/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SpiSi']['meta_info']


                    class Term(_Entity_):
                        """
                        Terminate stats
                        
                        .. attribute:: terminated_pkts
                        
                        	Number of terminated packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: terminated_bytes
                        
                        	Total bytes terminated
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Term, self).__init__()

                            self.yang_name = "term"
                            self.yang_parent_name = "data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('terminated_pkts', (YLeaf(YType.uint64, 'terminated-pkts'), ['int'])),
                                ('terminated_bytes', (YLeaf(YType.uint64, 'terminated-bytes'), ['int'])),
                            ])
                            self.terminated_pkts = None
                            self.terminated_bytes = None
                            self._segment_path = lambda: "term"
                            self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-forwarder/local/error/data/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Term']['meta_info']


                    class Sf(_Entity_):
                        """
                        Service function stats
                        
                        .. attribute:: processed_pkts
                        
                        	Number of packets processed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: processed_bytes
                        
                        	Total bytes processed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sf, self).__init__()

                            self.yang_name = "sf"
                            self.yang_parent_name = "data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                            ])
                            self.processed_pkts = None
                            self.processed_bytes = None
                            self._segment_path = lambda: "sf"
                            self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-forwarder/local/error/data/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sf, ['processed_pkts', 'processed_bytes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sf']['meta_info']


                    class Sff(_Entity_):
                        """
                        Service function forwarder stats
                        
                        .. attribute:: processed_pkts
                        
                        	Number of packets processed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: processed_bytes
                        
                        	Total bytes processed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sff, self).__init__()

                            self.yang_name = "sff"
                            self.yang_parent_name = "data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                            ])
                            self.processed_pkts = None
                            self.processed_bytes = None
                            self._segment_path = lambda: "sff"
                            self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-forwarder/local/error/data/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sff, ['processed_pkts', 'processed_bytes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sff']['meta_info']


                    class SffLocal(_Entity_):
                        """
                        Local service function forwarder stats
                        
                        .. attribute:: malformed_err_pkts
                        
                        	Number of packets with invalid NSH header
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: lookup_err_pkts
                        
                        	Number of packets with unknown spi\-si
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: malformed_err_bytes
                        
                        	Total bytes with invalid NSH header
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        .. attribute:: lookup_err_bytes
                        
                        	Total bytes with unknown spi\-si
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SffLocal, self).__init__()

                            self.yang_name = "sff-local"
                            self.yang_parent_name = "data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('malformed_err_pkts', (YLeaf(YType.uint64, 'malformed-err-pkts'), ['int'])),
                                ('lookup_err_pkts', (YLeaf(YType.uint64, 'lookup-err-pkts'), ['int'])),
                                ('malformed_err_bytes', (YLeaf(YType.uint64, 'malformed-err-bytes'), ['int'])),
                                ('lookup_err_bytes', (YLeaf(YType.uint64, 'lookup-err-bytes'), ['int'])),
                            ])
                            self.malformed_err_pkts = None
                            self.lookup_err_pkts = None
                            self.malformed_err_bytes = None
                            self.lookup_err_bytes = None
                            self._segment_path = lambda: "sff-local"
                            self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-forwarder/local/error/data/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SffLocal, ['malformed_err_pkts', 'lookup_err_pkts', 'malformed_err_bytes', 'lookup_err_bytes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SffLocal']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data']['meta_info']


                class SiArr(_Entity_):
                    """
                    SI array in case of detail stats
                    
                    .. attribute:: data
                    
                    	Stats counter for this index
                    	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data>`
                    
                    	**config**\: False
                    
                    .. attribute:: si
                    
                    	Service index
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'pbr-vservice-mgr-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr, self).__init__()

                        self.yang_name = "si-arr"
                        self.yang_parent_name = "error"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("data", ("data", GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data))])
                        self._leafs = OrderedDict([
                            ('si', (YLeaf(YType.uint8, 'si'), ['int'])),
                        ])
                        self.si = None

                        self.data = GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data()
                        self.data.parent = self
                        self._children_name_map["data"] = "data"
                        self._segment_path = lambda: "si-arr"
                        self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-forwarder/local/error/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr, ['si'], name, value)


                    class Data(_Entity_):
                        """
                        Stats counter for this index
                        
                        .. attribute:: spi_si
                        
                        	SF/SFF stats
                        	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi>`
                        
                        	**config**\: False
                        
                        .. attribute:: term
                        
                        	Terminate stats
                        	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term>`
                        
                        	**config**\: False
                        
                        .. attribute:: type
                        
                        	type
                        	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper.VsNshStats>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'pbr-vservice-mgr-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data, self).__init__()

                            self.yang_name = "data"
                            self.yang_parent_name = "si-arr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("spi-si", ("spi_si", GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi)), ("term", ("term", GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term))])
                            self._leafs = OrderedDict([
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStats', '')])),
                            ])
                            self.type = None

                            self.spi_si = GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi()
                            self.spi_si.parent = self
                            self._children_name_map["spi_si"] = "spi-si"

                            self.term = GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term()
                            self.term.parent = self
                            self._children_name_map["term"] = "term"
                            self._segment_path = lambda: "data"
                            self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-forwarder/local/error/si-arr/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data, ['type'], name, value)


                        class SpiSi(_Entity_):
                            """
                            SF/SFF stats
                            
                            .. attribute:: processed_pkts
                            
                            	Number of packets processed
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: processed_bytes
                            
                            	Total bytes processed
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'pbr-vservice-mgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi, self).__init__()

                                self.yang_name = "spi-si"
                                self.yang_parent_name = "data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('processed_pkts', (YLeaf(YType.uint64, 'processed-pkts'), ['int'])),
                                    ('processed_bytes', (YLeaf(YType.uint64, 'processed-bytes'), ['int'])),
                                ])
                                self.processed_pkts = None
                                self.processed_bytes = None
                                self._segment_path = lambda: "spi-si"
                                self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-forwarder/local/error/si-arr/data/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi']['meta_info']


                        class Term(_Entity_):
                            """
                            Terminate stats
                            
                            .. attribute:: terminated_pkts
                            
                            	Number of terminated packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: terminated_bytes
                            
                            	Total bytes terminated
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'pbr-vservice-mgr-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term, self).__init__()

                                self.yang_name = "term"
                                self.yang_parent_name = "data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('terminated_pkts', (YLeaf(YType.uint64, 'terminated-pkts'), ['int'])),
                                    ('terminated_bytes', (YLeaf(YType.uint64, 'terminated-bytes'), ['int'])),
                                ])
                                self.terminated_pkts = None
                                self.terminated_bytes = None
                                self._segment_path = lambda: "term"
                                self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-mgr-oper:global-service-function-chaining/service-function-forwarder/local/error/si-arr/data/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                        return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                    return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
                return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
            return meta._meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder']['meta_info']

    def clone_ptr(self):
        self._top_entity = GlobalServiceFunctionChaining()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_vservice_mgr_oper as meta
        return meta._meta_table['GlobalServiceFunctionChaining']['meta_info']


