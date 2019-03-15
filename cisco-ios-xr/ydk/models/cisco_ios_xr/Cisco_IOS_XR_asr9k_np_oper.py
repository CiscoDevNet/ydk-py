""" Cisco_IOS_XR_asr9k_np_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-np package operational data.

This module contains definitions
for the following management objects\:
  hardware\-module\-np\: Hardware NP Counters

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
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
    
    	**config**\: False
    
    

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
        self._child_classes = OrderedDict([("nodes", ("nodes", HardwareModuleNp.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = HardwareModuleNp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-np-oper:hardware-module-np"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HardwareModuleNp, [], name, value)


    class Nodes(Entity):
        """
        Table of nodes
        
        .. attribute:: node
        
        	Number
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node>`
        
        	**config**\: False
        
        

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
            self._child_classes = OrderedDict([("node", ("node", HardwareModuleNp.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-np-oper:hardware-module-np/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HardwareModuleNp.Nodes, [], name, value)


        class Node(Entity):
            """
            Number
            
            .. attribute:: node_name  (key)
            
            	node number
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: nps
            
            	List of all NP
            	**type**\:  :py:class:`Nps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps>`
            
            	**config**\: False
            
            

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
                self._child_classes = OrderedDict([("nps", ("nps", HardwareModuleNp.Nodes.Node.Nps))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.nps = HardwareModuleNp.Nodes.Node.Nps()
                self.nps.parent = self
                self._children_name_map["nps"] = "nps"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-np-oper:hardware-module-np/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModuleNp.Nodes.Node, ['node_name'], name, value)


            class Nps(Entity):
                """
                List of all NP
                
                .. attribute:: np
                
                	np0 to np7
                	**type**\: list of  		 :py:class:`Np <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np>`
                
                	**config**\: False
                
                

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
                    self._child_classes = OrderedDict([("np", ("np", HardwareModuleNp.Nodes.Node.Nps.Np))])
                    self._leafs = OrderedDict()

                    self.np = YList(self)
                    self._segment_path = lambda: "nps"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps, [], name, value)


                class Np(Entity):
                    """
                    np0 to np7
                    
                    .. attribute:: np_name  (key)
                    
                    	NP name
                    	**type**\: str
                    
                    	**pattern:** (np0)\|(np1)\|(np2)\|(np3)\|(np4)\|(np5)\|(np6)\|(np7)
                    
                    	**config**\: False
                    
                    .. attribute:: chn_load
                    
                    	prm channel load info
                    	**type**\:  :py:class:`ChnLoad <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad>`
                    
                    	**config**\: False
                    
                    .. attribute:: load_utilization
                    
                    	Hardware np load or utilization
                    	**type**\:  :py:class:`LoadUtilization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.LoadUtilization>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcam_summary
                    
                    	prm tcam summary info
                    	**type**\:  :py:class:`TcamSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary>`
                    
                    	**config**\: False
                    
                    .. attribute:: counters
                    
                    	prm counters info
                    	**type**\:  :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.Counters>`
                    
                    	**config**\: False
                    
                    .. attribute:: fast_drop
                    
                    	prm fast drop counters info
                    	**type**\:  :py:class:`FastDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop>`
                    
                    	**config**\: False
                    
                    .. attribute:: efd
                    
                    	EFD COS to Priority Mapping
                    	**type**\:  :py:class:`Efd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.Efd>`
                    
                    	**config**\: False
                    
                    

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
                        self._child_classes = OrderedDict([("chn-load", ("chn_load", HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad)), ("load-utilization", ("load_utilization", HardwareModuleNp.Nodes.Node.Nps.Np.LoadUtilization)), ("tcam-summary", ("tcam_summary", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary)), ("counters", ("counters", HardwareModuleNp.Nodes.Node.Nps.Np.Counters)), ("fast-drop", ("fast_drop", HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop)), ("efd", ("efd", HardwareModuleNp.Nodes.Node.Nps.Np.Efd))])
                        self._leafs = OrderedDict([
                            ('np_name', (YLeaf(YType.str, 'np-name'), ['str'])),
                        ])
                        self.np_name = None

                        self.chn_load = HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad()
                        self.chn_load.parent = self
                        self._children_name_map["chn_load"] = "chn-load"

                        self.load_utilization = HardwareModuleNp.Nodes.Node.Nps.Np.LoadUtilization()
                        self.load_utilization.parent = self
                        self._children_name_map["load_utilization"] = "load-utilization"

                        self.tcam_summary = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary()
                        self.tcam_summary.parent = self
                        self._children_name_map["tcam_summary"] = "tcam-summary"

                        self.counters = HardwareModuleNp.Nodes.Node.Nps.Np.Counters()
                        self.counters.parent = self
                        self._children_name_map["counters"] = "counters"

                        self.fast_drop = HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop()
                        self.fast_drop.parent = self
                        self._children_name_map["fast_drop"] = "fast-drop"

                        self.efd = HardwareModuleNp.Nodes.Node.Nps.Np.Efd()
                        self.efd.parent = self
                        self._children_name_map["efd"] = "efd"
                        self._segment_path = lambda: "np" + "[np-name='" + str(self.np_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np, ['np_name'], name, value)


                    class ChnLoad(Entity):
                        """
                        prm channel load info
                        
                        .. attribute:: np_chn_load
                        
                        	Array of NP Channel load counters
                        	**type**\: list of  		 :py:class:`NpChnLoad <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad>`
                        
                        	**config**\: False
                        
                        

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
                            self._child_classes = OrderedDict([("np-chn-load", ("np_chn_load", HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad))])
                            self._leafs = OrderedDict()

                            self.np_chn_load = YList(self)
                            self._segment_path = lambda: "chn-load"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad, [], name, value)


                        class NpChnLoad(Entity):
                            """
                            Array of NP Channel load counters
                            
                            .. attribute:: flow_ctr_counter
                            
                            	Flow control counters
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: avg_rfd_usage
                            
                            	Average RFD Usage
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: peak_rfd_usage
                            
                            	Peak RFD Usage
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: avg_guar_rfd_usage
                            
                            	Average of garanteed RFD usage
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: peak_guar_rfd_usage
                            
                            	Peak of garanteed RFD usage
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: interface_name
                            
                            	Inerface Name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('flow_ctr_counter', (YLeaf(YType.uint32, 'flow-ctr-counter'), ['int'])),
                                    ('avg_rfd_usage', (YLeaf(YType.uint32, 'avg-rfd-usage'), ['int'])),
                                    ('peak_rfd_usage', (YLeaf(YType.uint32, 'peak-rfd-usage'), ['int'])),
                                    ('avg_guar_rfd_usage', (YLeaf(YType.uint32, 'avg-guar-rfd-usage'), ['int'])),
                                    ('peak_guar_rfd_usage', (YLeaf(YType.uint32, 'peak-guar-rfd-usage'), ['int'])),
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ])
                                self.flow_ctr_counter = None
                                self.avg_rfd_usage = None
                                self.peak_rfd_usage = None
                                self.avg_guar_rfd_usage = None
                                self.peak_guar_rfd_usage = None
                                self.interface_name = None
                                self._segment_path = lambda: "np-chn-load"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad, ['flow_ctr_counter', 'avg_rfd_usage', 'peak_rfd_usage', 'avg_guar_rfd_usage', 'peak_guar_rfd_usage', 'interface_name'], name, value)




                    class LoadUtilization(Entity):
                        """
                        Hardware np load or utilization
                        
                        .. attribute:: utilization
                        
                        	Percent load on the NP engines
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: percentage
                        
                        .. attribute:: packet_per_second_rate
                        
                        	Packet rate load on NP engines
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'asr9k-np-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(HardwareModuleNp.Nodes.Node.Nps.Np.LoadUtilization, self).__init__()

                            self.yang_name = "load-utilization"
                            self.yang_parent_name = "np"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('utilization', (YLeaf(YType.uint32, 'utilization'), ['int'])),
                                ('packet_per_second_rate', (YLeaf(YType.uint32, 'packet-per-second-rate'), ['int'])),
                            ])
                            self.utilization = None
                            self.packet_per_second_rate = None
                            self._segment_path = lambda: "load-utilization"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.LoadUtilization, ['utilization', 'packet_per_second_rate'], name, value)



                    class TcamSummary(Entity):
                        """
                        prm tcam summary info
                        
                        .. attribute:: internal_tcam_info
                        
                        	Internal tcam summary info
                        	**type**\:  :py:class:`InternalTcamInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: tcam_info
                        
                        	External tcam summary info
                        	**type**\:  :py:class:`TcamInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo>`
                        
                        	**config**\: False
                        
                        

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
                            self._child_classes = OrderedDict([("internal-tcam-info", ("internal_tcam_info", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo)), ("tcam-info", ("tcam_info", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo))])
                            self._leafs = OrderedDict()

                            self.internal_tcam_info = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo()
                            self.internal_tcam_info.parent = self
                            self._children_name_map["internal_tcam_info"] = "internal-tcam-info"

                            self.tcam_info = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo()
                            self.tcam_info.parent = self
                            self._children_name_map["tcam_info"] = "tcam-info"
                            self._segment_path = lambda: "tcam-summary"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary, [], name, value)


                        class InternalTcamInfo(Entity):
                            """
                            Internal tcam summary info
                            
                            .. attribute:: tcam_lt_ods2
                            
                            	TCAM LT ODS 2 summary
                            	**type**\:  :py:class:`TcamLtOds2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2>`
                            
                            	**config**\: False
                            
                            .. attribute:: tcam_lt_ods8
                            
                            	TCAM LT\_ODS 8 summary
                            	**type**\:  :py:class:`TcamLtOds8 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8>`
                            
                            	**config**\: False
                            
                            .. attribute:: tcam_lt_l2
                            
                            	Array of TCAM LT L2 partition summaries
                            	**type**\: list of  		 :py:class:`TcamLtL2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2>`
                            
                            	**config**\: False
                            
                            

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
                                self._child_classes = OrderedDict([("tcam-lt-ods2", ("tcam_lt_ods2", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2)), ("tcam-lt-ods8", ("tcam_lt_ods8", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8)), ("tcam-lt-l2", ("tcam_lt_l2", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2))])
                                self._leafs = OrderedDict()

                                self.tcam_lt_ods2 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2()
                                self.tcam_lt_ods2.parent = self
                                self._children_name_map["tcam_lt_ods2"] = "tcam-lt-ods2"

                                self.tcam_lt_ods8 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8()
                                self.tcam_lt_ods8.parent = self
                                self._children_name_map["tcam_lt_ods8"] = "tcam-lt-ods8"

                                self.tcam_lt_l2 = YList(self)
                                self._segment_path = lambda: "internal-tcam-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo, [], name, value)


                            class TcamLtOds2(Entity):
                                """
                                TCAM LT ODS 2 summary
                                
                                .. attribute:: app_id_ifib
                                
                                	app IFIB entry
                                	**type**\:  :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_qos
                                
                                	app qos entry
                                	**type**\:  :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_acl
                                
                                	app acl entry
                                	**type**\:  :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_afmon
                                
                                	app afmon entry
                                	**type**\:  :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_li
                                
                                	app LI entry
                                	**type**\:  :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_pbr
                                
                                	app PBR entry
                                	**type**\:  :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr>`
                                
                                	**config**\: False
                                
                                .. attribute:: application_edpl_entry
                                
                                	app EDPL entry
                                	**type**\:  :py:class:`ApplicationEdplEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry>`
                                
                                	**config**\: False
                                
                                .. attribute:: max_entries
                                
                                	Max entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: free_entries
                                
                                	free entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

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
                                    self._child_classes = OrderedDict([("app-id-ifib", ("app_id_ifib", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib)), ("app-id-qos", ("app_id_qos", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos)), ("app-id-acl", ("app_id_acl", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl)), ("app-id-afmon", ("app_id_afmon", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon)), ("app-id-li", ("app_id_li", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi)), ("app-id-pbr", ("app_id_pbr", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr)), ("application-edpl-entry", ("application_edpl_entry", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry))])
                                    self._leafs = OrderedDict([
                                        ('max_entries', (YLeaf(YType.uint32, 'max-entries'), ['int'])),
                                        ('free_entries', (YLeaf(YType.uint32, 'free-entries'), ['int'])),
                                    ])
                                    self.max_entries = None
                                    self.free_entries = None

                                    self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib()
                                    self.app_id_ifib.parent = self
                                    self._children_name_map["app_id_ifib"] = "app-id-ifib"

                                    self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos()
                                    self.app_id_qos.parent = self
                                    self._children_name_map["app_id_qos"] = "app-id-qos"

                                    self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl()
                                    self.app_id_acl.parent = self
                                    self._children_name_map["app_id_acl"] = "app-id-acl"

                                    self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon()
                                    self.app_id_afmon.parent = self
                                    self._children_name_map["app_id_afmon"] = "app-id-afmon"

                                    self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi()
                                    self.app_id_li.parent = self
                                    self._children_name_map["app_id_li"] = "app-id-li"

                                    self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr()
                                    self.app_id_pbr.parent = self
                                    self._children_name_map["app_id_pbr"] = "app-id-pbr"

                                    self.application_edpl_entry = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry()
                                    self.application_edpl_entry.parent = self
                                    self._children_name_map["application_edpl_entry"] = "application-edpl-entry"
                                    self._segment_path = lambda: "tcam-lt-ods2"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2, ['max_entries', 'free_entries'], name, value)


                                class AppIdIfib(Entity):
                                    """
                                    app IFIB entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('total_used_entries', (YLeaf(YType.uint32, 'total-used-entries'), ['int'])),
                                            ('total_allocated_entries', (YLeaf(YType.uint32, 'total-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-ifib"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)



                                class AppIdQos(Entity):
                                    """
                                    app qos entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('total_used_entries', (YLeaf(YType.uint32, 'total-used-entries'), ['int'])),
                                            ('total_allocated_entries', (YLeaf(YType.uint32, 'total-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-qos"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)



                                class AppIdAcl(Entity):
                                    """
                                    app acl entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('total_used_entries', (YLeaf(YType.uint32, 'total-used-entries'), ['int'])),
                                            ('total_allocated_entries', (YLeaf(YType.uint32, 'total-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-acl"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)



                                class AppIdAfmon(Entity):
                                    """
                                    app afmon entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('total_used_entries', (YLeaf(YType.uint32, 'total-used-entries'), ['int'])),
                                            ('total_allocated_entries', (YLeaf(YType.uint32, 'total-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-afmon"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)



                                class AppIdLi(Entity):
                                    """
                                    app LI entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('total_used_entries', (YLeaf(YType.uint32, 'total-used-entries'), ['int'])),
                                            ('total_allocated_entries', (YLeaf(YType.uint32, 'total-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-li"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)



                                class AppIdPbr(Entity):
                                    """
                                    app PBR entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('total_used_entries', (YLeaf(YType.uint32, 'total-used-entries'), ['int'])),
                                            ('total_allocated_entries', (YLeaf(YType.uint32, 'total-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-pbr"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)



                                class ApplicationEdplEntry(Entity):
                                    """
                                    app EDPL entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('total_used_entries', (YLeaf(YType.uint32, 'total-used-entries'), ['int'])),
                                            ('total_allocated_entries', (YLeaf(YType.uint32, 'total-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "application-edpl-entry"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)




                            class TcamLtOds8(Entity):
                                """
                                TCAM LT\_ODS 8 summary
                                
                                .. attribute:: app_id_ifib
                                
                                	app IFIB entry
                                	**type**\:  :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_qos
                                
                                	app qos entry
                                	**type**\:  :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_acl
                                
                                	app acl entry
                                	**type**\:  :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_afmon
                                
                                	app afmon entry
                                	**type**\:  :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_li
                                
                                	app LI entry
                                	**type**\:  :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_pbr
                                
                                	app PBR entry
                                	**type**\:  :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr>`
                                
                                	**config**\: False
                                
                                .. attribute:: application_edpl_entry
                                
                                	app EDPL entry
                                	**type**\:  :py:class:`ApplicationEdplEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry>`
                                
                                	**config**\: False
                                
                                .. attribute:: max_entries
                                
                                	Max entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: free_entries
                                
                                	free entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

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
                                    self._child_classes = OrderedDict([("app-id-ifib", ("app_id_ifib", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib)), ("app-id-qos", ("app_id_qos", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos)), ("app-id-acl", ("app_id_acl", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl)), ("app-id-afmon", ("app_id_afmon", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon)), ("app-id-li", ("app_id_li", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi)), ("app-id-pbr", ("app_id_pbr", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr)), ("application-edpl-entry", ("application_edpl_entry", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry))])
                                    self._leafs = OrderedDict([
                                        ('max_entries', (YLeaf(YType.uint32, 'max-entries'), ['int'])),
                                        ('free_entries', (YLeaf(YType.uint32, 'free-entries'), ['int'])),
                                    ])
                                    self.max_entries = None
                                    self.free_entries = None

                                    self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib()
                                    self.app_id_ifib.parent = self
                                    self._children_name_map["app_id_ifib"] = "app-id-ifib"

                                    self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos()
                                    self.app_id_qos.parent = self
                                    self._children_name_map["app_id_qos"] = "app-id-qos"

                                    self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl()
                                    self.app_id_acl.parent = self
                                    self._children_name_map["app_id_acl"] = "app-id-acl"

                                    self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon()
                                    self.app_id_afmon.parent = self
                                    self._children_name_map["app_id_afmon"] = "app-id-afmon"

                                    self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi()
                                    self.app_id_li.parent = self
                                    self._children_name_map["app_id_li"] = "app-id-li"

                                    self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr()
                                    self.app_id_pbr.parent = self
                                    self._children_name_map["app_id_pbr"] = "app-id-pbr"

                                    self.application_edpl_entry = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry()
                                    self.application_edpl_entry.parent = self
                                    self._children_name_map["application_edpl_entry"] = "application-edpl-entry"
                                    self._segment_path = lambda: "tcam-lt-ods8"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8, ['max_entries', 'free_entries'], name, value)


                                class AppIdIfib(Entity):
                                    """
                                    app IFIB entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('total_used_entries', (YLeaf(YType.uint32, 'total-used-entries'), ['int'])),
                                            ('total_allocated_entries', (YLeaf(YType.uint32, 'total-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-ifib"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)



                                class AppIdQos(Entity):
                                    """
                                    app qos entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('total_used_entries', (YLeaf(YType.uint32, 'total-used-entries'), ['int'])),
                                            ('total_allocated_entries', (YLeaf(YType.uint32, 'total-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-qos"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)



                                class AppIdAcl(Entity):
                                    """
                                    app acl entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('total_used_entries', (YLeaf(YType.uint32, 'total-used-entries'), ['int'])),
                                            ('total_allocated_entries', (YLeaf(YType.uint32, 'total-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-acl"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)



                                class AppIdAfmon(Entity):
                                    """
                                    app afmon entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('total_used_entries', (YLeaf(YType.uint32, 'total-used-entries'), ['int'])),
                                            ('total_allocated_entries', (YLeaf(YType.uint32, 'total-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-afmon"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)



                                class AppIdLi(Entity):
                                    """
                                    app LI entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('total_used_entries', (YLeaf(YType.uint32, 'total-used-entries'), ['int'])),
                                            ('total_allocated_entries', (YLeaf(YType.uint32, 'total-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-li"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)



                                class AppIdPbr(Entity):
                                    """
                                    app PBR entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('total_used_entries', (YLeaf(YType.uint32, 'total-used-entries'), ['int'])),
                                            ('total_allocated_entries', (YLeaf(YType.uint32, 'total-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "app-id-pbr"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)



                                class ApplicationEdplEntry(Entity):
                                    """
                                    app EDPL entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	number of used vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('total_used_entries', (YLeaf(YType.uint32, 'total-used-entries'), ['int'])),
                                            ('total_allocated_entries', (YLeaf(YType.uint32, 'total-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None
                                        self._segment_path = lambda: "application-edpl-entry"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry, ['num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)




                            class TcamLtL2(Entity):
                                """
                                Array of TCAM LT L2 partition summaries
                                
                                .. attribute:: partition_id
                                
                                	PartitionID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: valid_entries
                                
                                	Valid Entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: free_entries
                                
                                	Free Entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

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
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('partition_id', (YLeaf(YType.uint32, 'partition-id'), ['int'])),
                                        ('valid_entries', (YLeaf(YType.uint32, 'valid-entries'), ['int'])),
                                        ('free_entries', (YLeaf(YType.uint32, 'free-entries'), ['int'])),
                                    ])
                                    self.partition_id = None
                                    self.valid_entries = None
                                    self.free_entries = None
                                    self._segment_path = lambda: "tcam-lt-l2"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2, ['partition_id', 'valid_entries', 'free_entries'], name, value)




                        class TcamInfo(Entity):
                            """
                            External tcam summary info
                            
                            .. attribute:: tcam_lt_ods2
                            
                            	TCAM ODS2 partition summary
                            	**type**\:  :py:class:`TcamLtOds2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2>`
                            
                            	**config**\: False
                            
                            .. attribute:: tcam_lt_ods8
                            
                            	TCAM ODS8 partition summary
                            	**type**\:  :py:class:`TcamLtOds8 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8>`
                            
                            	**config**\: False
                            
                            .. attribute:: tcam_lt_l2
                            
                            	Array of TCAM L2 partition summaries
                            	**type**\: list of  		 :py:class:`TcamLtL2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2>`
                            
                            	**config**\: False
                            
                            

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
                                self._child_classes = OrderedDict([("tcam-lt-ods2", ("tcam_lt_ods2", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2)), ("tcam-lt-ods8", ("tcam_lt_ods8", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8)), ("tcam-lt-l2", ("tcam_lt_l2", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2))])
                                self._leafs = OrderedDict()

                                self.tcam_lt_ods2 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2()
                                self.tcam_lt_ods2.parent = self
                                self._children_name_map["tcam_lt_ods2"] = "tcam-lt-ods2"

                                self.tcam_lt_ods8 = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8()
                                self.tcam_lt_ods8.parent = self
                                self._children_name_map["tcam_lt_ods8"] = "tcam-lt-ods8"

                                self.tcam_lt_l2 = YList(self)
                                self._segment_path = lambda: "tcam-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo, [], name, value)


                            class TcamLtOds2(Entity):
                                """
                                TCAM ODS2 partition summary
                                
                                .. attribute:: acl_common
                                
                                	ACL common region
                                	**type**\:  :py:class:`AclCommon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_ifib
                                
                                	app IFIB entry
                                	**type**\:  :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_qos
                                
                                	app qos entry
                                	**type**\:  :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_acl
                                
                                	app acl entry
                                	**type**\:  :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_afmon
                                
                                	app afmon entry
                                	**type**\:  :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_li
                                
                                	app LI entry
                                	**type**\:  :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_pbr
                                
                                	app PBR entry
                                	**type**\:  :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_edpl
                                
                                	app EDPL entry
                                	**type**\:  :py:class:`AppIdEdpl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl>`
                                
                                	**config**\: False
                                
                                .. attribute:: free_entries
                                
                                	Free entries in the table
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: reserved_entries
                                
                                	The number of active vmr entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

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
                                    self._child_classes = OrderedDict([("acl-common", ("acl_common", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon)), ("app-id-ifib", ("app_id_ifib", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib)), ("app-id-qos", ("app_id_qos", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos)), ("app-id-acl", ("app_id_acl", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl)), ("app-id-afmon", ("app_id_afmon", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon)), ("app-id-li", ("app_id_li", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi)), ("app-id-pbr", ("app_id_pbr", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr)), ("app-id-edpl", ("app_id_edpl", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl))])
                                    self._leafs = OrderedDict([
                                        ('free_entries', (YLeaf(YType.uint32, 'free-entries'), ['int'])),
                                        ('reserved_entries', (YLeaf(YType.uint32, 'reserved-entries'), ['int'])),
                                    ])
                                    self.free_entries = None
                                    self.reserved_entries = None

                                    self.acl_common = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon()
                                    self.acl_common.parent = self
                                    self._children_name_map["acl_common"] = "acl-common"

                                    self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib()
                                    self.app_id_ifib.parent = self
                                    self._children_name_map["app_id_ifib"] = "app-id-ifib"

                                    self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos()
                                    self.app_id_qos.parent = self
                                    self._children_name_map["app_id_qos"] = "app-id-qos"

                                    self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl()
                                    self.app_id_acl.parent = self
                                    self._children_name_map["app_id_acl"] = "app-id-acl"

                                    self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon()
                                    self.app_id_afmon.parent = self
                                    self._children_name_map["app_id_afmon"] = "app-id-afmon"

                                    self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi()
                                    self.app_id_li.parent = self
                                    self._children_name_map["app_id_li"] = "app-id-li"

                                    self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr()
                                    self.app_id_pbr.parent = self
                                    self._children_name_map["app_id_pbr"] = "app-id-pbr"

                                    self.app_id_edpl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl()
                                    self.app_id_edpl.parent = self
                                    self._children_name_map["app_id_edpl"] = "app-id-edpl"
                                    self._segment_path = lambda: "tcam-lt-ods2"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2, ['free_entries', 'reserved_entries'], name, value)


                                class AclCommon(Entity):
                                    """
                                    ACL common region
                                    
                                    .. attribute:: free_entries
                                    
                                    	Free entries in the table
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('free_entries', (YLeaf(YType.uint32, 'free-entries'), ['int'])),
                                            ('allocated_entries', (YLeaf(YType.uint32, 'allocated-entries'), ['int'])),
                                        ])
                                        self.free_entries = None
                                        self.allocated_entries = None
                                        self._segment_path = lambda: "acl-common"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon, ['free_entries', 'allocated_entries'], name, value)



                                class AppIdIfib(Entity):
                                    """
                                    app IFIB entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('num_active_entries', (YLeaf(YType.uint32, 'num-active-entries'), ['int'])),
                                            ('num_allocated_entries', (YLeaf(YType.uint32, 'num-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-ifib"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)



                                class AppIdQos(Entity):
                                    """
                                    app qos entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('num_active_entries', (YLeaf(YType.uint32, 'num-active-entries'), ['int'])),
                                            ('num_allocated_entries', (YLeaf(YType.uint32, 'num-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-qos"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)



                                class AppIdAcl(Entity):
                                    """
                                    app acl entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('num_active_entries', (YLeaf(YType.uint32, 'num-active-entries'), ['int'])),
                                            ('num_allocated_entries', (YLeaf(YType.uint32, 'num-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-acl"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)



                                class AppIdAfmon(Entity):
                                    """
                                    app afmon entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('num_active_entries', (YLeaf(YType.uint32, 'num-active-entries'), ['int'])),
                                            ('num_allocated_entries', (YLeaf(YType.uint32, 'num-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-afmon"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)



                                class AppIdLi(Entity):
                                    """
                                    app LI entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('num_active_entries', (YLeaf(YType.uint32, 'num-active-entries'), ['int'])),
                                            ('num_allocated_entries', (YLeaf(YType.uint32, 'num-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-li"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)



                                class AppIdPbr(Entity):
                                    """
                                    app PBR entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('num_active_entries', (YLeaf(YType.uint32, 'num-active-entries'), ['int'])),
                                            ('num_allocated_entries', (YLeaf(YType.uint32, 'num-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-pbr"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)



                                class AppIdEdpl(Entity):
                                    """
                                    app EDPL entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('num_active_entries', (YLeaf(YType.uint32, 'num-active-entries'), ['int'])),
                                            ('num_allocated_entries', (YLeaf(YType.uint32, 'num-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-edpl"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)




                            class TcamLtOds8(Entity):
                                """
                                TCAM ODS8 partition summary
                                
                                .. attribute:: acl_common
                                
                                	ACL common region
                                	**type**\:  :py:class:`AclCommon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_ifib
                                
                                	app IFIB entry
                                	**type**\:  :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_qos
                                
                                	app qos entry
                                	**type**\:  :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_acl
                                
                                	app acl entry
                                	**type**\:  :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_afmon
                                
                                	app afmon entry
                                	**type**\:  :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_li
                                
                                	app LI entry
                                	**type**\:  :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_pbr
                                
                                	app PBR entry
                                	**type**\:  :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_edpl
                                
                                	app EDPL entry
                                	**type**\:  :py:class:`AppIdEdpl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl>`
                                
                                	**config**\: False
                                
                                .. attribute:: free_entries
                                
                                	Free entries in the table
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: reserved_entries
                                
                                	The number of active vmr entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

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
                                    self._child_classes = OrderedDict([("acl-common", ("acl_common", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon)), ("app-id-ifib", ("app_id_ifib", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib)), ("app-id-qos", ("app_id_qos", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos)), ("app-id-acl", ("app_id_acl", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl)), ("app-id-afmon", ("app_id_afmon", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon)), ("app-id-li", ("app_id_li", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi)), ("app-id-pbr", ("app_id_pbr", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr)), ("app-id-edpl", ("app_id_edpl", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl))])
                                    self._leafs = OrderedDict([
                                        ('free_entries', (YLeaf(YType.uint32, 'free-entries'), ['int'])),
                                        ('reserved_entries', (YLeaf(YType.uint32, 'reserved-entries'), ['int'])),
                                    ])
                                    self.free_entries = None
                                    self.reserved_entries = None

                                    self.acl_common = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon()
                                    self.acl_common.parent = self
                                    self._children_name_map["acl_common"] = "acl-common"

                                    self.app_id_ifib = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib()
                                    self.app_id_ifib.parent = self
                                    self._children_name_map["app_id_ifib"] = "app-id-ifib"

                                    self.app_id_qos = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos()
                                    self.app_id_qos.parent = self
                                    self._children_name_map["app_id_qos"] = "app-id-qos"

                                    self.app_id_acl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl()
                                    self.app_id_acl.parent = self
                                    self._children_name_map["app_id_acl"] = "app-id-acl"

                                    self.app_id_afmon = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon()
                                    self.app_id_afmon.parent = self
                                    self._children_name_map["app_id_afmon"] = "app-id-afmon"

                                    self.app_id_li = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi()
                                    self.app_id_li.parent = self
                                    self._children_name_map["app_id_li"] = "app-id-li"

                                    self.app_id_pbr = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr()
                                    self.app_id_pbr.parent = self
                                    self._children_name_map["app_id_pbr"] = "app-id-pbr"

                                    self.app_id_edpl = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl()
                                    self.app_id_edpl.parent = self
                                    self._children_name_map["app_id_edpl"] = "app-id-edpl"
                                    self._segment_path = lambda: "tcam-lt-ods8"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8, ['free_entries', 'reserved_entries'], name, value)


                                class AclCommon(Entity):
                                    """
                                    ACL common region
                                    
                                    .. attribute:: free_entries
                                    
                                    	Free entries in the table
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('free_entries', (YLeaf(YType.uint32, 'free-entries'), ['int'])),
                                            ('allocated_entries', (YLeaf(YType.uint32, 'allocated-entries'), ['int'])),
                                        ])
                                        self.free_entries = None
                                        self.allocated_entries = None
                                        self._segment_path = lambda: "acl-common"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon, ['free_entries', 'allocated_entries'], name, value)



                                class AppIdIfib(Entity):
                                    """
                                    app IFIB entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('num_active_entries', (YLeaf(YType.uint32, 'num-active-entries'), ['int'])),
                                            ('num_allocated_entries', (YLeaf(YType.uint32, 'num-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-ifib"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)



                                class AppIdQos(Entity):
                                    """
                                    app qos entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('num_active_entries', (YLeaf(YType.uint32, 'num-active-entries'), ['int'])),
                                            ('num_allocated_entries', (YLeaf(YType.uint32, 'num-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-qos"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)



                                class AppIdAcl(Entity):
                                    """
                                    app acl entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('num_active_entries', (YLeaf(YType.uint32, 'num-active-entries'), ['int'])),
                                            ('num_allocated_entries', (YLeaf(YType.uint32, 'num-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-acl"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)



                                class AppIdAfmon(Entity):
                                    """
                                    app afmon entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('num_active_entries', (YLeaf(YType.uint32, 'num-active-entries'), ['int'])),
                                            ('num_allocated_entries', (YLeaf(YType.uint32, 'num-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-afmon"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)



                                class AppIdLi(Entity):
                                    """
                                    app LI entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('num_active_entries', (YLeaf(YType.uint32, 'num-active-entries'), ['int'])),
                                            ('num_allocated_entries', (YLeaf(YType.uint32, 'num-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-li"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)



                                class AppIdPbr(Entity):
                                    """
                                    app PBR entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('num_active_entries', (YLeaf(YType.uint32, 'num-active-entries'), ['int'])),
                                            ('num_allocated_entries', (YLeaf(YType.uint32, 'num-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-pbr"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)



                                class AppIdEdpl(Entity):
                                    """
                                    app EDPL entry
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Vmr IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_active_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_allocated_entries
                                    
                                    	The number of active vmr entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

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
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('num_active_entries', (YLeaf(YType.uint32, 'num-active-entries'), ['int'])),
                                            ('num_allocated_entries', (YLeaf(YType.uint32, 'num-allocated-entries'), ['int'])),
                                        ])
                                        self.num_vmr_ids = None
                                        self.num_active_entries = None
                                        self.num_allocated_entries = None
                                        self._segment_path = lambda: "app-id-edpl"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl, ['num_vmr_ids', 'num_active_entries', 'num_allocated_entries'], name, value)




                            class TcamLtL2(Entity):
                                """
                                Array of TCAM L2 partition summaries
                                
                                .. attribute:: partition_id
                                
                                	PartitionID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: priority
                                
                                	Priority
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: valid_entries
                                
                                	Valid Entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: free_entries
                                
                                	Free Entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

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
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('partition_id', (YLeaf(YType.uint32, 'partition-id'), ['int'])),
                                        ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                        ('valid_entries', (YLeaf(YType.uint32, 'valid-entries'), ['int'])),
                                        ('free_entries', (YLeaf(YType.uint32, 'free-entries'), ['int'])),
                                    ])
                                    self.partition_id = None
                                    self.priority = None
                                    self.valid_entries = None
                                    self.free_entries = None
                                    self._segment_path = lambda: "tcam-lt-l2"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2, ['partition_id', 'priority', 'valid_entries', 'free_entries'], name, value)





                    class Counters(Entity):
                        """
                        prm counters info
                        
                        .. attribute:: np_counter
                        
                        	Array of NP Counters
                        	**type**\: list of  		 :py:class:`NpCounter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter>`
                        
                        	**config**\: False
                        
                        

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
                            self._child_classes = OrderedDict([("np-counter", ("np_counter", HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter))])
                            self._leafs = OrderedDict()

                            self.np_counter = YList(self)
                            self._segment_path = lambda: "counters"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.Counters, [], name, value)


                        class NpCounter(Entity):
                            """
                            Array of NP Counters
                            
                            .. attribute:: counter_index
                            
                            	Counter Index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: counter_value
                            
                            	The accurate value of the counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: rate
                            
                            	Rate in Packets Per Second
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            	**units**\: packet/s
                            
                            .. attribute:: counter_type
                            
                            	Counter TypeDROP\: Drop counterPUNT\: Punt counterFWD\:  Forward or generic counterUNKNOWN\: Counter type unknown
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: counter_name
                            
                            	Counter name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('counter_index', (YLeaf(YType.uint32, 'counter-index'), ['int'])),
                                    ('counter_value', (YLeaf(YType.uint64, 'counter-value'), ['int'])),
                                    ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                                    ('counter_type', (YLeaf(YType.str, 'counter-type'), ['str'])),
                                    ('counter_name', (YLeaf(YType.str, 'counter-name'), ['str'])),
                                ])
                                self.counter_index = None
                                self.counter_value = None
                                self.rate = None
                                self.counter_type = None
                                self.counter_name = None
                                self._segment_path = lambda: "np-counter"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter, ['counter_index', 'counter_value', 'rate', 'counter_type', 'counter_name'], name, value)




                    class FastDrop(Entity):
                        """
                        prm fast drop counters info
                        
                        .. attribute:: np_fast_drop
                        
                        	Array of NP Fast Drop Counters
                        	**type**\: list of  		 :py:class:`NpFastDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop>`
                        
                        	**config**\: False
                        
                        

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
                            self._child_classes = OrderedDict([("np-fast-drop", ("np_fast_drop", HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop))])
                            self._leafs = OrderedDict()

                            self.np_fast_drop = YList(self)
                            self._segment_path = lambda: "fast-drop"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop, [], name, value)


                        class NpFastDrop(Entity):
                            """
                            Array of NP Fast Drop Counters
                            
                            .. attribute:: interface_name
                            
                            	Interface name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: counter_value
                            
                            	The Value of the counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('counter_value', (YLeaf(YType.uint64, 'counter-value'), ['int'])),
                                ])
                                self.interface_name = None
                                self.counter_value = None
                                self._segment_path = lambda: "np-fast-drop"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop, ['interface_name', 'counter_value'], name, value)




                    class Efd(Entity):
                        """
                        EFD COS to Priority Mapping
                        
                        .. attribute:: hp_list_is_supported
                        
                        	high\-priority\-list CLI is supported
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: vlan_cos_mapping
                        
                        	Array of VLAN COS Mapping
                        	**type**\: list of int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: mplscos_mapping
                        
                        	Array of MPLS COS Mapping
                        	**type**\: list of int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: ipcos_mapping
                        
                        	Array of IP COS Mapping
                        	**type**\: list of int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'asr9k-np-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(HardwareModuleNp.Nodes.Node.Nps.Np.Efd, self).__init__()

                            self.yang_name = "efd"
                            self.yang_parent_name = "np"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('hp_list_is_supported', (YLeaf(YType.uint32, 'hp-list-is-supported'), ['int'])),
                                ('vlan_cos_mapping', (YLeafList(YType.uint32, 'vlan-cos-mapping'), ['int'])),
                                ('mplscos_mapping', (YLeafList(YType.uint32, 'mplscos-mapping'), ['int'])),
                                ('ipcos_mapping', (YLeafList(YType.uint32, 'ipcos-mapping'), ['int'])),
                            ])
                            self.hp_list_is_supported = None
                            self.vlan_cos_mapping = []
                            self.mplscos_mapping = []
                            self.ipcos_mapping = []
                            self._segment_path = lambda: "efd"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.Efd, ['hp_list_is_supported', 'vlan_cos_mapping', 'mplscos_mapping', 'ipcos_mapping'], name, value)






    def clone_ptr(self):
        self._top_entity = HardwareModuleNp()
        return self._top_entity



