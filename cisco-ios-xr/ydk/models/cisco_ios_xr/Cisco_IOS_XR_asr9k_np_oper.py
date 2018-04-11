""" Cisco_IOS_XR_asr9k_np_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-np package operational data.

This module contains definitions
for the following management objects\:
  hardware\-module\-np\: Hardware NP Counters

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class HardwareModuleNp(Entity):
    """
    Hardware NP Counters
    
    .. attribute:: nodes
    
    	Table of nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes>`
    
    

    """

    _prefix = 'asr9k-np-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(HardwareModuleNp, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module-np"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-np-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", HardwareModuleNp.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = HardwareModuleNp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-np-oper:hardware-module-np"


    class Nodes(Entity):
        """
        Table of nodes
        
        .. attribute:: node
        
        	Number
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-np-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(HardwareModuleNp.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "hardware-module-np"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", HardwareModuleNp.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-np-oper:hardware-module-np/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(HardwareModuleNp.Nodes, [], name, value)


        class Node(Entity):
            """
            Number
            
            .. attribute:: node_name  (key)
            
            	node number
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: nps
            
            	List of all NP
            	**type**\:  :py:class:`Nps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps>`
            
            

            """

            _prefix = 'asr9k-np-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModuleNp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_container_classes = OrderedDict([("nps", ("nps", HardwareModuleNp.Nodes.Node.Nps))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                ])
                self.node_name = None

                self.nps = HardwareModuleNp.Nodes.Node.Nps()
                self.nps.parent = self
                self._children_name_map["nps"] = "nps"
                self._children_yang_names.add("nps")
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-np-oper:hardware-module-np/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModuleNp.Nodes.Node, ['node_name'], name, value)


            class Nps(Entity):
                """
                List of all NP
                
                .. attribute:: np
                
                	np0 to np7
                	**type**\: list of  		 :py:class:`Np <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np>`
                
                

                """

                _prefix = 'asr9k-np-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModuleNp.Nodes.Node.Nps, self).__init__()

                    self.yang_name = "nps"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("np", ("np", HardwareModuleNp.Nodes.Node.Nps.Np))])
                    self._leafs = OrderedDict()

                    self.np = YList(self)
                    self._segment_path = lambda: "nps"

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps, [], name, value)


                class Np(Entity):
                    """
                    np0 to np7
                    
                    .. attribute:: np_name  (key)
                    
                    	NP name
                    	**type**\: str
                    
                    	**pattern:** (np0)\|(np1)\|(np2)\|(np3)\|(np4)\|(np5)\|(np6)\|(np7)
                    
                    .. attribute:: chn_load
                    
                    	prm channel load info
                    	**type**\:  :py:class:`ChnLoad <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad>`
                    
                    .. attribute:: tcam_summary
                    
                    	prm tcam summary info
                    	**type**\:  :py:class:`TcamSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary>`
                    
                    .. attribute:: counters
                    
                    	prm counters info
                    	**type**\:  :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.Counters>`
                    
                    .. attribute:: fast_drop
                    
                    	prm fast drop counters info
                    	**type**\:  :py:class:`FastDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop>`
                    
                    

                    """

                    _prefix = 'asr9k-np-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(HardwareModuleNp.Nodes.Node.Nps.Np, self).__init__()

                        self.yang_name = "np"
                        self.yang_parent_name = "nps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['np_name']
                        self._child_container_classes = OrderedDict([("chn-load", ("chn_load", HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad)), ("tcam-summary", ("tcam_summary", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary)), ("counters", ("counters", HardwareModuleNp.Nodes.Node.Nps.Np.Counters)), ("fast-drop", ("fast_drop", HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('np_name', YLeaf(YType.str, 'np-name')),
                        ])
                        self.np_name = None

                        self.chn_load = HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad()
                        self.chn_load.parent = self
                        self._children_name_map["chn_load"] = "chn-load"
                        self._children_yang_names.add("chn-load")

                        self.tcam_summary = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary()
                        self.tcam_summary.parent = self
                        self._children_name_map["tcam_summary"] = "tcam-summary"
                        self._children_yang_names.add("tcam-summary")

                        self.counters = HardwareModuleNp.Nodes.Node.Nps.Np.Counters()
                        self.counters.parent = self
                        self._children_name_map["counters"] = "counters"
                        self._children_yang_names.add("counters")

                        self.fast_drop = HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop()
                        self.fast_drop.parent = self
                        self._children_name_map["fast_drop"] = "fast-drop"
                        self._children_yang_names.add("fast-drop")
                        self._segment_path = lambda: "np" + "[np-name='" + str(self.np_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np, ['np_name'], name, value)


                    class ChnLoad(Entity):
                        """
                        prm channel load info
                        
                        .. attribute:: np_chn_load
                        
                        	Array of NP Channel load counters
                        	**type**\: list of  		 :py:class:`NpChnLoad <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad>`
                        
                        

                        """

                        _prefix = 'asr9k-np-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad, self).__init__()

                            self.yang_name = "chn-load"
                            self.yang_parent_name = "np"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("np-chn-load", ("np_chn_load", HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad))])
                            self._leafs = OrderedDict()

                            self.np_chn_load = YList(self)
                            self._segment_path = lambda: "chn-load"

                        def __setattr__(self, name, value):
                            self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad, [], name, value)


                        class NpChnLoad(Entity):
                            """
                            Array of NP Channel load counters
                            
                            .. attribute:: flow_ctr_counter
                            
                            	Flow control counters
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: avg_rfd_usage
                            
                            	Average RFD Usage
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: peak_rfd_usage
                            
                            	Peak RFD Usage
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: avg_guar_rfd_usage
                            
                            	Average of garanteed RFD usage
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: peak_guar_rfd_usage
                            
                            	Peak of garanteed RFD usage
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interface_name
                            
                            	Inerface Name
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'asr9k-np-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad, self).__init__()

                                self.yang_name = "np-chn-load"
                                self.yang_parent_name = "chn-load"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('flow_ctr_counter', YLeaf(YType.uint32, 'flow-ctr-counter')),
                                    ('avg_rfd_usage', YLeaf(YType.uint32, 'avg-rfd-usage')),
                                    ('peak_rfd_usage', YLeaf(YType.uint32, 'peak-rfd-usage')),
                                    ('avg_guar_rfd_usage', YLeaf(YType.uint32, 'avg-guar-rfd-usage')),
                                    ('peak_guar_rfd_usage', YLeaf(YType.uint32, 'peak-guar-rfd-usage')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                ])
                                self.flow_ctr_counter = None
                                self.avg_rfd_usage = None
                                self.peak_rfd_usage = None
                                self.avg_guar_rfd_usage = None
                                self.peak_guar_rfd_usage = None
                                self.interface_name = None
                                self._segment_path = lambda: "np-chn-load"

                            def __setattr__(self, name, value):
                                self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad, ['flow_ctr_counter', 'avg_rfd_usage', 'peak_rfd_usage', 'avg_guar_rfd_usage', 'peak_guar_rfd_usage', 'interface_name'], name, value)


                    class TcamSummary(Entity):
                        """
                        prm tcam summary info
                        
                        .. attribute:: internal_tcam_info
                        
                        	Internal tcam summary info
                        	**type**\:  :py:class:`InternalTcamInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo>`
                        
                        .. attribute:: tcam_info
                        
                        	External tcam summary info
                        	**type**\:  :py:class:`TcamInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo>`
                        
                        

                        """

                        _prefix = 'asr9k-np-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary, self).__init__()

                            self.yang_name = "tcam-summary"
                            self.yang_parent_name = "np"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("internal-tcam-info", ("internal_tcam_info", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo)), ("tcam-info", ("tcam_info", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.internal_tcam_info = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo()
                            self.internal_tcam_info.parent = self
                            self._children_name_map["internal_tcam_info"] = "internal-tcam-info"
                            self._children_yang_names.add("internal-tcam-info")

                            self.tcam_info = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo()
                            self.tcam_info.parent = self
                            self._children_name_map["tcam_info"] = "tcam-info"
                            self._children_yang_names.add("tcam-info")
                            self._segment_path = lambda: "tcam-summary"


                        class InternalTcamInfo(Entity):
                            """
                            Internal tcam summary info
                            
                            .. attribute:: tcam_lt_ods2
                            
                            	TCAM LT ODS 2 summary
                            	**type**\:  :py:class:`TcamLtOds2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2>`
                            
                            .. attribute:: tcam_lt_ods8
                            
                            	TCAM LT\_ODS 8 summary
                            	**type**\:  :py:class:`TcamLtOds8 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8>`
                            
                            .. attribute:: tcam_lt_l2
                            
                            	Array of TCAM LT L2 partition summaries
                            	**type**\: list of  		 :py:class:`TcamLtL2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2>`
                            
                            

                            """

                            _prefix = 'asr9k-np-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo, self).__init__()

                                self.yang_name = "internal-tcam-info"
                                self.yang_parent_name = "tcam-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("tcam-lt-ods2", ("tcam_lt_ods2", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2)), ("tcam-lt-ods8", ("tcam_lt_ods8", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8))])
                                self._child_list_classes = OrderedDict([("tcam-lt-l2", ("tcam_lt_l2", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2))])
                                self._leafs = OrderedDict()

                                self.tcam_lt_ods2 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2()
                                self.tcam_lt_ods2.parent = self
                                self._children_name_map["tcam_lt_ods2"] = "tcam-lt-ods2"
                                self._children_yang_names.add("tcam-lt-ods2")

                                self.tcam_lt_ods8 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8()
                                self.tcam_lt_ods8.parent = self
                                self._children_name_map["tcam_lt_ods8"] = "tcam-lt-ods8"
                                self._children_yang_names.add("tcam-lt-ods8")

                                self.tcam_lt_l2 = YList(self)
                                self._segment_path = lambda: "internal-tcam-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo, [], name, value)


                            class TcamLtOds2(Entity):
                                """
                                TCAM LT ODS 2 summary
                                
                                .. attribute:: app_id_ifib
                                
                                	app IFIB entry
                                	**type**\:  :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib>`
                                
                                .. attribute:: app_id_qos
                                
                                	app qos entry
                                	**type**\:  :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos>`
                                
                                .. attribute:: app_id_acl
                                
                                	app acl entry
                                	**type**\:  :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl>`
                                
                                .. attribute:: app_id_afmon
                                
                                	app afmon entry
                                	**type**\:  :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon>`
                                
                                .. attribute:: app_id_li
                                
                                	app LI entry
                                	**type**\:  :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi>`
                                
                                .. attribute:: app_id_pbr
                                
                                	app PBR entry
                                	**type**\:  :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr>`
                                
                                .. attribute:: application_edpl_entry
                                
                                	app EDPL entry
                                	**type**\:  :py:class:`ApplicationEdplEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry>`
                                
                                .. attribute:: max_entries
                                
                                	Max entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: free_entries
                                
                                	free entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2, self).__init__()

                                    self.yang_name = "tcam-lt-ods2"
                                    self.yang_parent_name = "internal-tcam-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("app-id-ifib", ("app_id_ifib", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib)), ("app-id-qos", ("app_id_qos", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos)), ("app-id-acl", ("app_id_acl", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl)), ("app-id-afmon", ("app_id_afmon", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon)), ("app-id-li", ("app_id_li", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi)), ("app-id-pbr", ("app_id_pbr", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr)), ("application-edpl-entry", ("application_edpl_entry", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_entries', YLeaf(YType.uint32, 'max-entries')),
                                        ('free_entries', YLeaf(YType.uint32, 'free-entries')),
                                    ])
                                    self.max_entries = None
                                    self.free_entries = None

                                    self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib()
                                    self.app_id_ifib.parent = self
                                    self._children_name_map["app_id_ifib"] = "app-id-ifib"
                                    self._children_yang_names.add("app-id-ifib")

                                    self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos()
                                    self.app_id_qos.parent = self
                                    self._children_name_map["app_id_qos"] = "app-id-qos"
                                    self._children_yang_names.add("app-id-qos")

                                    self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl()
                                    self.app_id_acl.parent = self
                                    self._children_name_map["app_id_acl"] = "app-id-acl"
                                    self._children_yang_names.add("app-id-acl")

                                    self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon()
                                    self.app_id_afmon.parent = self
                                    self._children_name_map["app_id_afmon"] = "app-id-afmon"
                                    self._children_yang_names.add("app-id-afmon")

                                    self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi()
                                    self.app_id_li.parent = self
                                    self._children_name_map["app_id_li"] = "app-id-li"
                                    self._children_yang_names.add("app-id-li")

                                    self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr()
                                    self.app_id_pbr.parent = self
                                    self._children_name_map["app_id_pbr"] = "app-id-pbr"
                                    self._children_yang_names.add("app-id-pbr")

                                    self.application_edpl_entry = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry()
                                    self.application_edpl_entry.parent = self
                                    self._children_name_map["application_edpl_entry"] = "application-edpl-entry"
                                    self._children_yang_names.add("application-edpl-entry")
                                    self._segment_path = lambda: "tcam-lt-ods2"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2, ['max_entries', 'free_entries'], name, value)


                                class AppIdIfib(Entity):
                                    """
                                    app IFIB entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib, self).__init__()

                                        self.yang_name = "app-id-ifib"
                                        self.yang_parent_name = "tcam-lt-ods2"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('total_used_entries', YLeaf(YType.uint32, 'total-used-entries')),
                                            ('total_allocated_entries', YLeaf(YType.uint32, 'total-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-ifib"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)


                                class AppIdQos(Entity):
                                    """
                                    app qos entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos, self).__init__()

                                        self.yang_name = "app-id-qos"
                                        self.yang_parent_name = "tcam-lt-ods2"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('total_used_entries', YLeaf(YType.uint32, 'total-used-entries')),
                                            ('total_allocated_entries', YLeaf(YType.uint32, 'total-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-qos"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)


                                class AppIdAcl(Entity):
                                    """
                                    app acl entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl, self).__init__()

                                        self.yang_name = "app-id-acl"
                                        self.yang_parent_name = "tcam-lt-ods2"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('total_used_entries', YLeaf(YType.uint32, 'total-used-entries')),
                                            ('total_allocated_entries', YLeaf(YType.uint32, 'total-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-acl"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)


                                class AppIdAfmon(Entity):
                                    """
                                    app afmon entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon, self).__init__()

                                        self.yang_name = "app-id-afmon"
                                        self.yang_parent_name = "tcam-lt-ods2"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('total_used_entries', YLeaf(YType.uint32, 'total-used-entries')),
                                            ('total_allocated_entries', YLeaf(YType.uint32, 'total-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-afmon"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)


                                class AppIdLi(Entity):
                                    """
                                    app LI entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi, self).__init__()

                                        self.yang_name = "app-id-li"
                                        self.yang_parent_name = "tcam-lt-ods2"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('total_used_entries', YLeaf(YType.uint32, 'total-used-entries')),
                                            ('total_allocated_entries', YLeaf(YType.uint32, 'total-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-li"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)


                                class AppIdPbr(Entity):
                                    """
                                    app PBR entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr, self).__init__()

                                        self.yang_name = "app-id-pbr"
                                        self.yang_parent_name = "tcam-lt-ods2"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('total_used_entries', YLeaf(YType.uint32, 'total-used-entries')),
                                            ('total_allocated_entries', YLeaf(YType.uint32, 'total-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-pbr"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)


                                class ApplicationEdplEntry(Entity):
                                    """
                                    app EDPL entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry, self).__init__()

                                        self.yang_name = "application-edpl-entry"
                                        self.yang_parent_name = "tcam-lt-ods2"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('total_used_entries', YLeaf(YType.uint32, 'total-used-entries')),
                                            ('total_allocated_entries', YLeaf(YType.uint32, 'total-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "application-edpl-entry"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)


                            class TcamLtOds8(Entity):
                                """
                                TCAM LT\_ODS 8 summary
                                
                                .. attribute:: app_id_ifib
                                
                                	app IFIB entry
                                	**type**\:  :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib>`
                                
                                .. attribute:: app_id_qos
                                
                                	app qos entry
                                	**type**\:  :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos>`
                                
                                .. attribute:: app_id_acl
                                
                                	app acl entry
                                	**type**\:  :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl>`
                                
                                .. attribute:: app_id_afmon
                                
                                	app afmon entry
                                	**type**\:  :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon>`
                                
                                .. attribute:: app_id_li
                                
                                	app LI entry
                                	**type**\:  :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi>`
                                
                                .. attribute:: app_id_pbr
                                
                                	app PBR entry
                                	**type**\:  :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr>`
                                
                                .. attribute:: application_edpl_entry
                                
                                	app EDPL entry
                                	**type**\:  :py:class:`ApplicationEdplEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry>`
                                
                                .. attribute:: max_entries
                                
                                	Max entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: free_entries
                                
                                	free entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8, self).__init__()

                                    self.yang_name = "tcam-lt-ods8"
                                    self.yang_parent_name = "internal-tcam-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("app-id-ifib", ("app_id_ifib", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib)), ("app-id-qos", ("app_id_qos", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos)), ("app-id-acl", ("app_id_acl", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl)), ("app-id-afmon", ("app_id_afmon", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon)), ("app-id-li", ("app_id_li", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi)), ("app-id-pbr", ("app_id_pbr", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr)), ("application-edpl-entry", ("application_edpl_entry", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_entries', YLeaf(YType.uint32, 'max-entries')),
                                        ('free_entries', YLeaf(YType.uint32, 'free-entries')),
                                    ])
                                    self.max_entries = None
                                    self.free_entries = None

                                    self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib()
                                    self.app_id_ifib.parent = self
                                    self._children_name_map["app_id_ifib"] = "app-id-ifib"
                                    self._children_yang_names.add("app-id-ifib")

                                    self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos()
                                    self.app_id_qos.parent = self
                                    self._children_name_map["app_id_qos"] = "app-id-qos"
                                    self._children_yang_names.add("app-id-qos")

                                    self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl()
                                    self.app_id_acl.parent = self
                                    self._children_name_map["app_id_acl"] = "app-id-acl"
                                    self._children_yang_names.add("app-id-acl")

                                    self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon()
                                    self.app_id_afmon.parent = self
                                    self._children_name_map["app_id_afmon"] = "app-id-afmon"
                                    self._children_yang_names.add("app-id-afmon")

                                    self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi()
                                    self.app_id_li.parent = self
                                    self._children_name_map["app_id_li"] = "app-id-li"
                                    self._children_yang_names.add("app-id-li")

                                    self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr()
                                    self.app_id_pbr.parent = self
                                    self._children_name_map["app_id_pbr"] = "app-id-pbr"
                                    self._children_yang_names.add("app-id-pbr")

                                    self.application_edpl_entry = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry()
                                    self.application_edpl_entry.parent = self
                                    self._children_name_map["application_edpl_entry"] = "application-edpl-entry"
                                    self._children_yang_names.add("application-edpl-entry")
                                    self._segment_path = lambda: "tcam-lt-ods8"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8, ['max_entries', 'free_entries'], name, value)


                                class AppIdIfib(Entity):
                                    """
                                    app IFIB entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib, self).__init__()

                                        self.yang_name = "app-id-ifib"
                                        self.yang_parent_name = "tcam-lt-ods8"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('total_used_entries', YLeaf(YType.uint32, 'total-used-entries')),
                                            ('total_allocated_entries', YLeaf(YType.uint32, 'total-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-ifib"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)


                                class AppIdQos(Entity):
                                    """
                                    app qos entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos, self).__init__()

                                        self.yang_name = "app-id-qos"
                                        self.yang_parent_name = "tcam-lt-ods8"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('total_used_entries', YLeaf(YType.uint32, 'total-used-entries')),
                                            ('total_allocated_entries', YLeaf(YType.uint32, 'total-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-qos"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)


                                class AppIdAcl(Entity):
                                    """
                                    app acl entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl, self).__init__()

                                        self.yang_name = "app-id-acl"
                                        self.yang_parent_name = "tcam-lt-ods8"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('total_used_entries', YLeaf(YType.uint32, 'total-used-entries')),
                                            ('total_allocated_entries', YLeaf(YType.uint32, 'total-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-acl"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)


                                class AppIdAfmon(Entity):
                                    """
                                    app afmon entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon, self).__init__()

                                        self.yang_name = "app-id-afmon"
                                        self.yang_parent_name = "tcam-lt-ods8"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('total_used_entries', YLeaf(YType.uint32, 'total-used-entries')),
                                            ('total_allocated_entries', YLeaf(YType.uint32, 'total-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-afmon"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)


                                class AppIdLi(Entity):
                                    """
                                    app LI entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi, self).__init__()

                                        self.yang_name = "app-id-li"
                                        self.yang_parent_name = "tcam-lt-ods8"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('total_used_entries', YLeaf(YType.uint32, 'total-used-entries')),
                                            ('total_allocated_entries', YLeaf(YType.uint32, 'total-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-li"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)


                                class AppIdPbr(Entity):
                                    """
                                    app PBR entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr, self).__init__()

                                        self.yang_name = "app-id-pbr"
                                        self.yang_parent_name = "tcam-lt-ods8"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('total_used_entries', YLeaf(YType.uint32, 'total-used-entries')),
                                            ('total_allocated_entries', YLeaf(YType.uint32, 'total-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-pbr"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)


                                class ApplicationEdplEntry(Entity):
                                    """
                                    app EDPL entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry, self).__init__()

                                        self.yang_name = "application-edpl-entry"
                                        self.yang_parent_name = "tcam-lt-ods8"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('total_used_entries', YLeaf(YType.uint32, 'total-used-entries')),
                                            ('total_allocated_entries', YLeaf(YType.uint32, 'total-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "application-edpl-entry"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)


                            class TcamLtL2(Entity):
                                """
                                Array of TCAM LT L2 partition summaries
                                
                                .. attribute:: partition_id
                                
                                	PartitionID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: valid_entries
                                
                                	Valid Entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: free_entries
                                
                                	Free Entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2, self).__init__()

                                    self.yang_name = "tcam-lt-l2"
                                    self.yang_parent_name = "internal-tcam-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('partition_id', YLeaf(YType.uint32, 'partition-id')),
                                        ('valid_entries', YLeaf(YType.uint32, 'valid-entries')),
                                        ('free_entries', YLeaf(YType.uint32, 'free-entries')),
                                    ])
                                    self.partition_id = None
                                    self.valid_entries = None
                                    self.free_entries = None
                                    self._segment_path = lambda: "tcam-lt-l2"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2, ['partition_id', 'valid_entries', 'free_entries'], name, value)


                        class TcamInfo(Entity):
                            """
                            External tcam summary info
                            
                            .. attribute:: tcam_lt_ods2
                            
                            	TCAM ODS2 partition summary
                            	**type**\:  :py:class:`TcamLtOds2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2>`
                            
                            .. attribute:: tcam_lt_ods8
                            
                            	TCAM ODS8 partition summary
                            	**type**\:  :py:class:`TcamLtOds8 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8>`
                            
                            .. attribute:: tcam_lt_l2
                            
                            	Array of TCAM L2 partition summaries
                            	**type**\: list of  		 :py:class:`TcamLtL2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2>`
                            
                            

                            """

                            _prefix = 'asr9k-np-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo, self).__init__()

                                self.yang_name = "tcam-info"
                                self.yang_parent_name = "tcam-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("tcam-lt-ods2", ("tcam_lt_ods2", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2)), ("tcam-lt-ods8", ("tcam_lt_ods8", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8))])
                                self._child_list_classes = OrderedDict([("tcam-lt-l2", ("tcam_lt_l2", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2))])
                                self._leafs = OrderedDict()

                                self.tcam_lt_ods2 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2()
                                self.tcam_lt_ods2.parent = self
                                self._children_name_map["tcam_lt_ods2"] = "tcam-lt-ods2"
                                self._children_yang_names.add("tcam-lt-ods2")

                                self.tcam_lt_ods8 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8()
                                self.tcam_lt_ods8.parent = self
                                self._children_name_map["tcam_lt_ods8"] = "tcam-lt-ods8"
                                self._children_yang_names.add("tcam-lt-ods8")

                                self.tcam_lt_l2 = YList(self)
                                self._segment_path = lambda: "tcam-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo, [], name, value)


                            class TcamLtOds2(Entity):
                                """
                                TCAM ODS2 partition summary
                                
                                .. attribute:: acl_common
                                
                                	ACL common region
                                	**type**\:  :py:class:`AclCommon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon>`
                                
                                .. attribute:: app_id_ifib
                                
                                	app IFIB entry
                                	**type**\:  :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib>`
                                
                                .. attribute:: app_id_qos
                                
                                	app qos entry
                                	**type**\:  :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos>`
                                
                                .. attribute:: app_id_acl
                                
                                	app acl entry
                                	**type**\:  :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl>`
                                
                                .. attribute:: app_id_afmon
                                
                                	app afmon entry
                                	**type**\:  :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon>`
                                
                                .. attribute:: app_id_li
                                
                                	app LI entry
                                	**type**\:  :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi>`
                                
                                .. attribute:: app_id_pbr
                                
                                	app PBR entry
                                	**type**\:  :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr>`
                                
                                .. attribute:: app_id_edpl
                                
                                	app EDPL entry
                                	**type**\:  :py:class:`AppIdEdpl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl>`
                                
                                .. attribute:: free_entries
                                
                                	Free entries in the table
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: reserved_entries
                                
                                	The number of active vmr entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2, self).__init__()

                                    self.yang_name = "tcam-lt-ods2"
                                    self.yang_parent_name = "tcam-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("acl-common", ("acl_common", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon)), ("app-id-ifib", ("app_id_ifib", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib)), ("app-id-qos", ("app_id_qos", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos)), ("app-id-acl", ("app_id_acl", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl)), ("app-id-afmon", ("app_id_afmon", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon)), ("app-id-li", ("app_id_li", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi)), ("app-id-pbr", ("app_id_pbr", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr)), ("app-id-edpl", ("app_id_edpl", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('free_entries', YLeaf(YType.uint32, 'free-entries')),
                                        ('reserved_entries', YLeaf(YType.uint32, 'reserved-entries')),
                                    ])
                                    self.free_entries = None
                                    self.reserved_entries = None

                                    self.acl_common = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon()
                                    self.acl_common.parent = self
                                    self._children_name_map["acl_common"] = "acl-common"
                                    self._children_yang_names.add("acl-common")

                                    self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib()
                                    self.app_id_ifib.parent = self
                                    self._children_name_map["app_id_ifib"] = "app-id-ifib"
                                    self._children_yang_names.add("app-id-ifib")

                                    self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos()
                                    self.app_id_qos.parent = self
                                    self._children_name_map["app_id_qos"] = "app-id-qos"
                                    self._children_yang_names.add("app-id-qos")

                                    self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl()
                                    self.app_id_acl.parent = self
                                    self._children_name_map["app_id_acl"] = "app-id-acl"
                                    self._children_yang_names.add("app-id-acl")

                                    self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon()
                                    self.app_id_afmon.parent = self
                                    self._children_name_map["app_id_afmon"] = "app-id-afmon"
                                    self._children_yang_names.add("app-id-afmon")

                                    self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi()
                                    self.app_id_li.parent = self
                                    self._children_name_map["app_id_li"] = "app-id-li"
                                    self._children_yang_names.add("app-id-li")

                                    self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr()
                                    self.app_id_pbr.parent = self
                                    self._children_name_map["app_id_pbr"] = "app-id-pbr"
                                    self._children_yang_names.add("app-id-pbr")

                                    self.app_id_edpl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl()
                                    self.app_id_edpl.parent = self
                                    self._children_name_map["app_id_edpl"] = "app-id-edpl"
                                    self._children_yang_names.add("app-id-edpl")
                                    self._segment_path = lambda: "tcam-lt-ods2"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2, ['free_entries', 'reserved_entries'], name, value)


                                class AclCommon(Entity):
                                    """
                                    ACL common region
                                    
                                    .. attribute:: free_entries
                                    
                                    	Free entries in the table
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon, self).__init__()

                                        self.yang_name = "acl-common"
                                        self.yang_parent_name = "tcam-lt-ods2"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('free_entries', YLeaf(YType.uint32, 'free-entries')),
                                            ('allocated_entries', YLeaf(YType.uint32, 'allocated-entries')),
                                        ])
                                        self.free_entries = None
                                        self.allocated_entries = None
                                        self._segment_path = lambda: "acl-common"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon, ['free_entries', 'allocated_entries'], name, value)


                                class AppIdIfib(Entity):
                                    """
                                    app IFIB entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib, self).__init__()

                                        self.yang_name = "app-id-ifib"
                                        self.yang_parent_name = "tcam-lt-ods2"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('num_active_entries', YLeaf(YType.uint32, 'num-active-entries')),
                                            ('num_allocated_entries', YLeaf(YType.uint32, 'num-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-ifib"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)


                                class AppIdQos(Entity):
                                    """
                                    app qos entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos, self).__init__()

                                        self.yang_name = "app-id-qos"
                                        self.yang_parent_name = "tcam-lt-ods2"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('num_active_entries', YLeaf(YType.uint32, 'num-active-entries')),
                                            ('num_allocated_entries', YLeaf(YType.uint32, 'num-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-qos"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)


                                class AppIdAcl(Entity):
                                    """
                                    app acl entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl, self).__init__()

                                        self.yang_name = "app-id-acl"
                                        self.yang_parent_name = "tcam-lt-ods2"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('num_active_entries', YLeaf(YType.uint32, 'num-active-entries')),
                                            ('num_allocated_entries', YLeaf(YType.uint32, 'num-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-acl"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)


                                class AppIdAfmon(Entity):
                                    """
                                    app afmon entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon, self).__init__()

                                        self.yang_name = "app-id-afmon"
                                        self.yang_parent_name = "tcam-lt-ods2"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('num_active_entries', YLeaf(YType.uint32, 'num-active-entries')),
                                            ('num_allocated_entries', YLeaf(YType.uint32, 'num-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-afmon"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)


                                class AppIdLi(Entity):
                                    """
                                    app LI entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi, self).__init__()

                                        self.yang_name = "app-id-li"
                                        self.yang_parent_name = "tcam-lt-ods2"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('num_active_entries', YLeaf(YType.uint32, 'num-active-entries')),
                                            ('num_allocated_entries', YLeaf(YType.uint32, 'num-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-li"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)


                                class AppIdPbr(Entity):
                                    """
                                    app PBR entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr, self).__init__()

                                        self.yang_name = "app-id-pbr"
                                        self.yang_parent_name = "tcam-lt-ods2"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('num_active_entries', YLeaf(YType.uint32, 'num-active-entries')),
                                            ('num_allocated_entries', YLeaf(YType.uint32, 'num-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-pbr"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)


                                class AppIdEdpl(Entity):
                                    """
                                    app EDPL entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl, self).__init__()

                                        self.yang_name = "app-id-edpl"
                                        self.yang_parent_name = "tcam-lt-ods2"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('num_active_entries', YLeaf(YType.uint32, 'num-active-entries')),
                                            ('num_allocated_entries', YLeaf(YType.uint32, 'num-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-edpl"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)


                            class TcamLtOds8(Entity):
                                """
                                TCAM ODS8 partition summary
                                
                                .. attribute:: acl_common
                                
                                	ACL common region
                                	**type**\:  :py:class:`AclCommon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon>`
                                
                                .. attribute:: app_id_ifib
                                
                                	app IFIB entry
                                	**type**\:  :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib>`
                                
                                .. attribute:: app_id_qos
                                
                                	app qos entry
                                	**type**\:  :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos>`
                                
                                .. attribute:: app_id_acl
                                
                                	app acl entry
                                	**type**\:  :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl>`
                                
                                .. attribute:: app_id_afmon
                                
                                	app afmon entry
                                	**type**\:  :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon>`
                                
                                .. attribute:: app_id_li
                                
                                	app LI entry
                                	**type**\:  :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi>`
                                
                                .. attribute:: app_id_pbr
                                
                                	app PBR entry
                                	**type**\:  :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr>`
                                
                                .. attribute:: app_id_edpl
                                
                                	app EDPL entry
                                	**type**\:  :py:class:`AppIdEdpl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl>`
                                
                                .. attribute:: free_entries
                                
                                	Free entries in the table
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: reserved_entries
                                
                                	The number of active vmr entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8, self).__init__()

                                    self.yang_name = "tcam-lt-ods8"
                                    self.yang_parent_name = "tcam-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("acl-common", ("acl_common", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon)), ("app-id-ifib", ("app_id_ifib", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib)), ("app-id-qos", ("app_id_qos", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos)), ("app-id-acl", ("app_id_acl", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl)), ("app-id-afmon", ("app_id_afmon", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon)), ("app-id-li", ("app_id_li", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi)), ("app-id-pbr", ("app_id_pbr", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr)), ("app-id-edpl", ("app_id_edpl", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('free_entries', YLeaf(YType.uint32, 'free-entries')),
                                        ('reserved_entries', YLeaf(YType.uint32, 'reserved-entries')),
                                    ])
                                    self.free_entries = None
                                    self.reserved_entries = None

                                    self.acl_common = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon()
                                    self.acl_common.parent = self
                                    self._children_name_map["acl_common"] = "acl-common"
                                    self._children_yang_names.add("acl-common")

                                    self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib()
                                    self.app_id_ifib.parent = self
                                    self._children_name_map["app_id_ifib"] = "app-id-ifib"
                                    self._children_yang_names.add("app-id-ifib")

                                    self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos()
                                    self.app_id_qos.parent = self
                                    self._children_name_map["app_id_qos"] = "app-id-qos"
                                    self._children_yang_names.add("app-id-qos")

                                    self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl()
                                    self.app_id_acl.parent = self
                                    self._children_name_map["app_id_acl"] = "app-id-acl"
                                    self._children_yang_names.add("app-id-acl")

                                    self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon()
                                    self.app_id_afmon.parent = self
                                    self._children_name_map["app_id_afmon"] = "app-id-afmon"
                                    self._children_yang_names.add("app-id-afmon")

                                    self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi()
                                    self.app_id_li.parent = self
                                    self._children_name_map["app_id_li"] = "app-id-li"
                                    self._children_yang_names.add("app-id-li")

                                    self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr()
                                    self.app_id_pbr.parent = self
                                    self._children_name_map["app_id_pbr"] = "app-id-pbr"
                                    self._children_yang_names.add("app-id-pbr")

                                    self.app_id_edpl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl()
                                    self.app_id_edpl.parent = self
                                    self._children_name_map["app_id_edpl"] = "app-id-edpl"
                                    self._children_yang_names.add("app-id-edpl")
                                    self._segment_path = lambda: "tcam-lt-ods8"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8, ['free_entries', 'reserved_entries'], name, value)


                                class AclCommon(Entity):
                                    """
                                    ACL common region
                                    
                                    .. attribute:: free_entries
                                    
                                    	Free entries in the table
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon, self).__init__()

                                        self.yang_name = "acl-common"
                                        self.yang_parent_name = "tcam-lt-ods8"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('free_entries', YLeaf(YType.uint32, 'free-entries')),
                                            ('allocated_entries', YLeaf(YType.uint32, 'allocated-entries')),
                                        ])
                                        self.free_entries = None
                                        self.allocated_entries = None
                                        self._segment_path = lambda: "acl-common"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon, ['free_entries', 'allocated_entries'], name, value)


                                class AppIdIfib(Entity):
                                    """
                                    app IFIB entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib, self).__init__()

                                        self.yang_name = "app-id-ifib"
                                        self.yang_parent_name = "tcam-lt-ods8"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('num_active_entries', YLeaf(YType.uint32, 'num-active-entries')),
                                            ('num_allocated_entries', YLeaf(YType.uint32, 'num-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-ifib"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)


                                class AppIdQos(Entity):
                                    """
                                    app qos entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos, self).__init__()

                                        self.yang_name = "app-id-qos"
                                        self.yang_parent_name = "tcam-lt-ods8"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('num_active_entries', YLeaf(YType.uint32, 'num-active-entries')),
                                            ('num_allocated_entries', YLeaf(YType.uint32, 'num-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-qos"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)


                                class AppIdAcl(Entity):
                                    """
                                    app acl entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl, self).__init__()

                                        self.yang_name = "app-id-acl"
                                        self.yang_parent_name = "tcam-lt-ods8"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('num_active_entries', YLeaf(YType.uint32, 'num-active-entries')),
                                            ('num_allocated_entries', YLeaf(YType.uint32, 'num-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-acl"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)


                                class AppIdAfmon(Entity):
                                    """
                                    app afmon entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon, self).__init__()

                                        self.yang_name = "app-id-afmon"
                                        self.yang_parent_name = "tcam-lt-ods8"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('num_active_entries', YLeaf(YType.uint32, 'num-active-entries')),
                                            ('num_allocated_entries', YLeaf(YType.uint32, 'num-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-afmon"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)


                                class AppIdLi(Entity):
                                    """
                                    app LI entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi, self).__init__()

                                        self.yang_name = "app-id-li"
                                        self.yang_parent_name = "tcam-lt-ods8"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('num_active_entries', YLeaf(YType.uint32, 'num-active-entries')),
                                            ('num_allocated_entries', YLeaf(YType.uint32, 'num-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-li"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)


                                class AppIdPbr(Entity):
                                    """
                                    app PBR entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr, self).__init__()

                                        self.yang_name = "app-id-pbr"
                                        self.yang_parent_name = "tcam-lt-ods8"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('num_active_entries', YLeaf(YType.uint32, 'num-active-entries')),
                                            ('num_allocated_entries', YLeaf(YType.uint32, 'num-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-pbr"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)


                                class AppIdEdpl(Entity):
                                    """
                                    app EDPL entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl, self).__init__()

                                        self.yang_name = "app-id-edpl"
                                        self.yang_parent_name = "tcam-lt-ods8"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', YLeaf(YType.uint32, 'num-vmr-ids')),
                                            ('num_active_entries', YLeaf(YType.uint32, 'num-active-entries')),
                                            ('num_allocated_entries', YLeaf(YType.uint32, 'num-allocated-entries')),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-edpl"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)


                            class TcamLtL2(Entity):
                                """
                                Array of TCAM L2 partition summaries
                                
                                .. attribute:: partition_id
                                
                                	PartitionID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: priority
                                
                                	Priority
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: valid_entries
                                
                                	Valid Entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: free_entries
                                
                                	Free Entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2, self).__init__()

                                    self.yang_name = "tcam-lt-l2"
                                    self.yang_parent_name = "tcam-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('partition_id', YLeaf(YType.uint32, 'partition-id')),
                                        ('priority', YLeaf(YType.uint32, 'priority')),
                                        ('valid_entries', YLeaf(YType.uint32, 'valid-entries')),
                                        ('free_entries', YLeaf(YType.uint32, 'free-entries')),
                                    ])
                                    self.partition_id = None
                                    self.priority = None
                                    self.valid_entries = None
                                    self.free_entries = None
                                    self._segment_path = lambda: "tcam-lt-l2"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2, ['partition_id', 'priority', 'valid_entries', 'free_entries'], name, value)


                    class Counters(Entity):
                        """
                        prm counters info
                        
                        .. attribute:: np_counter
                        
                        	Array of NP Counters
                        	**type**\: list of  		 :py:class:`NpCounter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter>`
                        
                        

                        """

                        _prefix = 'asr9k-np-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(HardwareModuleNp.Nodes.Node.Nps.Np.Counters, self).__init__()

                            self.yang_name = "counters"
                            self.yang_parent_name = "np"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("np-counter", ("np_counter", HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter))])
                            self._leafs = OrderedDict()

                            self.np_counter = YList(self)
                            self._segment_path = lambda: "counters"

                        def __setattr__(self, name, value):
                            self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.Counters, [], name, value)


                        class NpCounter(Entity):
                            """
                            Array of NP Counters
                            
                            .. attribute:: counter_index
                            
                            	Counter Index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: counter_value
                            
                            	The accurate value of the counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rate
                            
                            	Rate in Packets Per Second
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: packet/s
                            
                            .. attribute:: counter_type
                            
                            	Counter TypeDROP\: Drop counterPUNT\: Punt counterFWD\:  Forward or generic counterUNKNOWN\: Counter type unknown
                            	**type**\: str
                            
                            .. attribute:: counter_name
                            
                            	Counter name
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'asr9k-np-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter, self).__init__()

                                self.yang_name = "np-counter"
                                self.yang_parent_name = "counters"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('counter_index', YLeaf(YType.uint32, 'counter-index')),
                                    ('counter_value', YLeaf(YType.uint64, 'counter-value')),
                                    ('rate', YLeaf(YType.uint32, 'rate')),
                                    ('counter_type', YLeaf(YType.str, 'counter-type')),
                                    ('counter_name', YLeaf(YType.str, 'counter-name')),
                                ])
                                self.counter_index = None
                                self.counter_value = None
                                self.rate = None
                                self.counter_type = None
                                self.counter_name = None
                                self._segment_path = lambda: "np-counter"

                            def __setattr__(self, name, value):
                                self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter, ['counter_index', 'counter_value', 'rate', 'counter_type', 'counter_name'], name, value)


                    class FastDrop(Entity):
                        """
                        prm fast drop counters info
                        
                        .. attribute:: np_fast_drop
                        
                        	Array of NP Fast Drop Counters
                        	**type**\: list of  		 :py:class:`NpFastDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop>`
                        
                        

                        """

                        _prefix = 'asr9k-np-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop, self).__init__()

                            self.yang_name = "fast-drop"
                            self.yang_parent_name = "np"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("np-fast-drop", ("np_fast_drop", HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop))])
                            self._leafs = OrderedDict()

                            self.np_fast_drop = YList(self)
                            self._segment_path = lambda: "fast-drop"

                        def __setattr__(self, name, value):
                            self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop, [], name, value)


                        class NpFastDrop(Entity):
                            """
                            Array of NP Fast Drop Counters
                            
                            .. attribute:: interface_name
                            
                            	Interface name
                            	**type**\: str
                            
                            .. attribute:: counter_value
                            
                            	The Value of the counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'asr9k-np-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop, self).__init__()

                                self.yang_name = "np-fast-drop"
                                self.yang_parent_name = "fast-drop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('counter_value', YLeaf(YType.uint64, 'counter-value')),
                                ])
                                self.interface_name = None
                                self.counter_value = None
                                self._segment_path = lambda: "np-fast-drop"

                            def __setattr__(self, name, value):
                                self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop, ['interface_name', 'counter_value'], name, value)

    def clone_ptr(self):
        self._top_entity = HardwareModuleNp()
        return self._top_entity

