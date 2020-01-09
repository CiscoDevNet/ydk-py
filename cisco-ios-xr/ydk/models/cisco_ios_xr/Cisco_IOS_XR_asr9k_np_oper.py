""" Cisco_IOS_XR_asr9k_np_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-np package operational data.

This module contains definitions
for the following management objects\:
  hardware\-module\-np\: Hardware NP Counters

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




class HardwareModuleNp(_Entity_):
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
        if sys.version_info > (3,):
            super().__init__()
        else:
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


    class Nodes(_Entity_):
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
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class Node(_Entity_):
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
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class Nps(_Entity_):
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
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class Np(_Entity_):
                    """
                    np0 to np7
                    
                    .. attribute:: np_name  (key)
                    
                    	NP name
                    	**type**\: str
                    
                    	**pattern:** (np0)\|(np1)\|(np2)\|(np3)\|(np4)\|(np5)\|(np6)\|(np7)
                    
                    	**config**\: False
                    
                    .. attribute:: np_uidb
                    
                    	Hardware np uidb
                    	**type**\:  :py:class:`NpUidb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.NpUidb>`
                    
                    	**config**\: False
                    
                    .. attribute:: tcam_region_summary
                    
                    	tcam region summary info
                    	**type**\:  :py:class:`TcamRegionSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary>`
                    
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
                    
                    .. attribute:: l2rm_hw_resource
                    
                    	L2rm Hardware Resources
                    	**type**\:  :py:class:`L2rmHwResource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource>`
                    
                    	**config**\: False
                    
                    .. attribute:: profile
                    
                    	Hardware Profile
                    	**type**\:  :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.Profile>`
                    
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
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(HardwareModuleNp.Nodes.Node.Nps.Np, self).__init__()

                        self.yang_name = "np"
                        self.yang_parent_name = "nps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['np_name']
                        self._child_classes = OrderedDict([("np-uidb", ("np_uidb", HardwareModuleNp.Nodes.Node.Nps.Np.NpUidb)), ("tcam-region-summary", ("tcam_region_summary", HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary)), ("chn-load", ("chn_load", HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad)), ("load-utilization", ("load_utilization", HardwareModuleNp.Nodes.Node.Nps.Np.LoadUtilization)), ("tcam-summary", ("tcam_summary", HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary)), ("l2rm-hw-resource", ("l2rm_hw_resource", HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource)), ("profile", ("profile", HardwareModuleNp.Nodes.Node.Nps.Np.Profile)), ("counters", ("counters", HardwareModuleNp.Nodes.Node.Nps.Np.Counters)), ("fast-drop", ("fast_drop", HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop)), ("efd", ("efd", HardwareModuleNp.Nodes.Node.Nps.Np.Efd))])
                        self._leafs = OrderedDict([
                            ('np_name', (YLeaf(YType.str, 'np-name'), ['str'])),
                        ])
                        self.np_name = None

                        self.np_uidb = HardwareModuleNp.Nodes.Node.Nps.Np.NpUidb()
                        self.np_uidb.parent = self
                        self._children_name_map["np_uidb"] = "np-uidb"

                        self.tcam_region_summary = HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary()
                        self.tcam_region_summary.parent = self
                        self._children_name_map["tcam_region_summary"] = "tcam-region-summary"

                        self.chn_load = HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad()
                        self.chn_load.parent = self
                        self._children_name_map["chn_load"] = "chn-load"

                        self.load_utilization = HardwareModuleNp.Nodes.Node.Nps.Np.LoadUtilization()
                        self.load_utilization.parent = self
                        self._children_name_map["load_utilization"] = "load-utilization"

                        self.tcam_summary = HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary()
                        self.tcam_summary.parent = self
                        self._children_name_map["tcam_summary"] = "tcam-summary"

                        self.l2rm_hw_resource = HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource()
                        self.l2rm_hw_resource.parent = self
                        self._children_name_map["l2rm_hw_resource"] = "l2rm-hw-resource"

                        self.profile = HardwareModuleNp.Nodes.Node.Nps.Np.Profile()
                        self.profile.parent = self
                        self._children_name_map["profile"] = "profile"

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


                    class NpUidb(_Entity_):
                        """
                        Hardware np uidb
                        
                        .. attribute:: uidb_index
                        
                        	Array of NP UIDB Index
                        	**type**\: list of  		 :py:class:`UidbIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.NpUidb.UidbIndex>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'asr9k-np-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(HardwareModuleNp.Nodes.Node.Nps.Np.NpUidb, self).__init__()

                            self.yang_name = "np-uidb"
                            self.yang_parent_name = "np"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("uidb-index", ("uidb_index", HardwareModuleNp.Nodes.Node.Nps.Np.NpUidb.UidbIndex))])
                            self._leafs = OrderedDict()

                            self.uidb_index = YList(self)
                            self._segment_path = lambda: "np-uidb"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.NpUidb, [], name, value)


                        class UidbIndex(_Entity_):
                            """
                            Array of NP UIDB Index
                            
                            .. attribute:: interface_name
                            
                            	Interface name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: interface_handle
                            
                            	Interface handle
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: index
                            
                            	UIDB Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: interface_type
                            
                            	Interface type
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'asr9k-np-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.NpUidb.UidbIndex, self).__init__()

                                self.yang_name = "uidb-index"
                                self.yang_parent_name = "np-uidb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                                    ('index', (YLeaf(YType.uint16, 'index'), ['int'])),
                                    ('interface_type', (YLeaf(YType.str, 'interface-type'), ['str'])),
                                ])
                                self.interface_name = None
                                self.interface_handle = None
                                self.index = None
                                self.interface_type = None
                                self._segment_path = lambda: "uidb-index"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.NpUidb.UidbIndex, ['interface_name', 'interface_handle', 'index', 'interface_type'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.NpUidb.UidbIndex']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                            return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.NpUidb']['meta_info']


                    class TcamRegionSummary(_Entity_):
                        """
                        tcam region summary info
                        
                        .. attribute:: internal_tcam_info
                        
                        	Internal tcam summary info
                        	**type**\:  :py:class:`InternalTcamInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'asr9k-np-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary, self).__init__()

                            self.yang_name = "tcam-region-summary"
                            self.yang_parent_name = "np"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("internal-tcam-info", ("internal_tcam_info", HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo))])
                            self._leafs = OrderedDict()

                            self.internal_tcam_info = HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo()
                            self.internal_tcam_info.parent = self
                            self._children_name_map["internal_tcam_info"] = "internal-tcam-info"
                            self._segment_path = lambda: "tcam-region-summary"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary, [], name, value)


                        class InternalTcamInfo(_Entity_):
                            """
                            Internal tcam summary info
                            
                            .. attribute:: tcam_region
                            
                            	TCAM Regions
                            	**type**\: list of  		 :py:class:`TcamRegion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo.TcamRegion>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'asr9k-np-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo, self).__init__()

                                self.yang_name = "internal-tcam-info"
                                self.yang_parent_name = "tcam-region-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("tcam-region", ("tcam_region", HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo.TcamRegion))])
                                self._leafs = OrderedDict()

                                self.tcam_region = YList(self)
                                self._segment_path = lambda: "internal-tcam-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo, [], name, value)


                            class TcamRegion(_Entity_):
                                """
                                TCAM Regions
                                
                                .. attribute:: region_name
                                
                                	Region Name
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: max_entries
                                
                                	Max entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: free_entries
                                
                                	Free entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: feature
                                
                                	Feature
                                	**type**\: list of  		 :py:class:`Feature <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo.TcamRegion.Feature>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo.TcamRegion, self).__init__()

                                    self.yang_name = "tcam-region"
                                    self.yang_parent_name = "internal-tcam-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("feature", ("feature", HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo.TcamRegion.Feature))])
                                    self._leafs = OrderedDict([
                                        ('region_name', (YLeaf(YType.str, 'region-name'), ['str'])),
                                        ('max_entries', (YLeaf(YType.uint32, 'max-entries'), ['int'])),
                                        ('free_entries', (YLeaf(YType.uint32, 'free-entries'), ['int'])),
                                    ])
                                    self.region_name = None
                                    self.max_entries = None
                                    self.free_entries = None

                                    self.feature = YList(self)
                                    self._segment_path = lambda: "tcam-region"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo.TcamRegion, ['region_name', 'max_entries', 'free_entries'], name, value)


                                class Feature(_Entity_):
                                    """
                                    Feature
                                    
                                    .. attribute:: feature_id
                                    
                                    	Feature ID
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_vmr_ids
                                    
                                    	Number of VRM IDs
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_used_entries
                                    
                                    	Number of used VMR entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: total_allocated_entries
                                    
                                    	Total Allocated entries
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: vmr_entry
                                    
                                    	VMR entries
                                    	**type**\: list of  		 :py:class:`VmrEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo.TcamRegion.Feature.VmrEntry>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'asr9k-np-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo.TcamRegion.Feature, self).__init__()

                                        self.yang_name = "feature"
                                        self.yang_parent_name = "tcam-region"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("vmr-entry", ("vmr_entry", HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo.TcamRegion.Feature.VmrEntry))])
                                        self._leafs = OrderedDict([
                                            ('feature_id', (YLeaf(YType.str, 'feature-id'), ['str'])),
                                            ('num_vmr_ids', (YLeaf(YType.uint32, 'num-vmr-ids'), ['int'])),
                                            ('total_used_entries', (YLeaf(YType.uint32, 'total-used-entries'), ['int'])),
                                            ('total_allocated_entries', (YLeaf(YType.uint32, 'total-allocated-entries'), ['int'])),
                                        ])
                                        self.feature_id = None
                                        self.num_vmr_ids = None
                                        self.total_used_entries = None
                                        self.total_allocated_entries = None

                                        self.vmr_entry = YList(self)
                                        self._segment_path = lambda: "feature"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo.TcamRegion.Feature, ['feature_id', 'num_vmr_ids', 'total_used_entries', 'total_allocated_entries'], name, value)


                                    class VmrEntry(_Entity_):
                                        """
                                        VMR entries
                                        
                                        .. attribute:: vmr_id
                                        
                                        	Vmr ID
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: used_entries
                                        
                                        	The number of used vmr entries
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
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo.TcamRegion.Feature.VmrEntry, self).__init__()

                                            self.yang_name = "vmr-entry"
                                            self.yang_parent_name = "feature"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('vmr_id', (YLeaf(YType.uint32, 'vmr-id'), ['int'])),
                                                ('used_entries', (YLeaf(YType.uint32, 'used-entries'), ['int'])),
                                                ('allocated_entries', (YLeaf(YType.uint32, 'allocated-entries'), ['int'])),
                                            ])
                                            self.vmr_id = None
                                            self.used_entries = None
                                            self.allocated_entries = None
                                            self._segment_path = lambda: "vmr-entry"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo.TcamRegion.Feature.VmrEntry, ['vmr_id', 'used_entries', 'allocated_entries'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                            return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo.TcamRegion.Feature.VmrEntry']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo.TcamRegion.Feature']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                    return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo.TcamRegion']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary.InternalTcamInfo']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                            return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamRegionSummary']['meta_info']


                    class ChnLoad(_Entity_):
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
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class NpChnLoad(_Entity_):
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
                            
                            	Average of guaranteed RFD usage
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: peak_guar_rfd_usage
                            
                            	Peak of guaranteed RFD usage
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
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                            return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad']['meta_info']


                    class LoadUtilization(_Entity_):
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
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                            return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.LoadUtilization']['meta_info']


                    class TcamSummary(_Entity_):
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
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class InternalTcamInfo(_Entity_):
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
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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


                            class TcamLtOds2(_Entity_):
                                """
                                TCAM LT ODS 2 summary
                                
                                .. attribute:: app_id_ifib
                                
                                	App IFIB entry
                                	**type**\:  :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_qos
                                
                                	App qos entry
                                	**type**\:  :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_acl
                                
                                	App acl entry
                                	**type**\:  :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_afmon
                                
                                	App afmon entry
                                	**type**\:  :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_li
                                
                                	App LI entry
                                	**type**\:  :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_pbr
                                
                                	App PBR entry
                                	**type**\:  :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr>`
                                
                                	**config**\: False
                                
                                .. attribute:: application_edpl_entry
                                
                                	App EDPL entry
                                	**type**\:  :py:class:`ApplicationEdplEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry>`
                                
                                	**config**\: False
                                
                                .. attribute:: max_entries
                                
                                	Max entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: free_entries
                                
                                	Free entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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


                                class AppIdIfib(_Entity_):
                                    """
                                    App IFIB entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib']['meta_info']


                                class AppIdQos(_Entity_):
                                    """
                                    App qos entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos']['meta_info']


                                class AppIdAcl(_Entity_):
                                    """
                                    App acl entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl']['meta_info']


                                class AppIdAfmon(_Entity_):
                                    """
                                    App afmon entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon']['meta_info']


                                class AppIdLi(_Entity_):
                                    """
                                    App LI entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi']['meta_info']


                                class AppIdPbr(_Entity_):
                                    """
                                    App PBR entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr']['meta_info']


                                class ApplicationEdplEntry(_Entity_):
                                    """
                                    App EDPL entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                    return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2']['meta_info']


                            class TcamLtOds8(_Entity_):
                                """
                                TCAM LT\_ODS 8 summary
                                
                                .. attribute:: app_id_ifib
                                
                                	App IFIB entry
                                	**type**\:  :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_qos
                                
                                	App qos entry
                                	**type**\:  :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_acl
                                
                                	App acl entry
                                	**type**\:  :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_afmon
                                
                                	App afmon entry
                                	**type**\:  :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_li
                                
                                	App LI entry
                                	**type**\:  :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_pbr
                                
                                	App PBR entry
                                	**type**\:  :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr>`
                                
                                	**config**\: False
                                
                                .. attribute:: application_edpl_entry
                                
                                	App EDPL entry
                                	**type**\:  :py:class:`ApplicationEdplEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry>`
                                
                                	**config**\: False
                                
                                .. attribute:: max_entries
                                
                                	Max entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: free_entries
                                
                                	Free entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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


                                class AppIdIfib(_Entity_):
                                    """
                                    App IFIB entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib']['meta_info']


                                class AppIdQos(_Entity_):
                                    """
                                    App qos entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos']['meta_info']


                                class AppIdAcl(_Entity_):
                                    """
                                    App acl entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl']['meta_info']


                                class AppIdAfmon(_Entity_):
                                    """
                                    App afmon entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon']['meta_info']


                                class AppIdLi(_Entity_):
                                    """
                                    App LI entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi']['meta_info']


                                class AppIdPbr(_Entity_):
                                    """
                                    App PBR entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr']['meta_info']


                                class ApplicationEdplEntry(_Entity_):
                                    """
                                    App EDPL entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                    return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8']['meta_info']


                            class TcamLtL2(_Entity_):
                                """
                                Array of TCAM LT L2 partition summaries
                                
                                .. attribute:: partition_id
                                
                                	PartitionID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: valid_entries
                                
                                	Valid entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: free_entries
                                
                                	Free entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                    return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo']['meta_info']


                        class TcamInfo(_Entity_):
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
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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


                            class TcamLtOds2(_Entity_):
                                """
                                TCAM ODS2 partition summary
                                
                                .. attribute:: acl_common
                                
                                	ACL common region
                                	**type**\:  :py:class:`AclCommon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_ifib
                                
                                	App IFIB entry
                                	**type**\:  :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_qos
                                
                                	App qos entry
                                	**type**\:  :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_acl
                                
                                	App acl entry
                                	**type**\:  :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_afmon
                                
                                	App afmon entry
                                	**type**\:  :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_li
                                
                                	App LI entry
                                	**type**\:  :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_pbr
                                
                                	App PBR entry
                                	**type**\:  :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_edpl
                                
                                	App EDPL entry
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
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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


                                class AclCommon(_Entity_):
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon']['meta_info']


                                class AppIdIfib(_Entity_):
                                    """
                                    App IFIB entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib']['meta_info']


                                class AppIdQos(_Entity_):
                                    """
                                    App qos entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos']['meta_info']


                                class AppIdAcl(_Entity_):
                                    """
                                    App acl entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl']['meta_info']


                                class AppIdAfmon(_Entity_):
                                    """
                                    App afmon entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon']['meta_info']


                                class AppIdLi(_Entity_):
                                    """
                                    App LI entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi']['meta_info']


                                class AppIdPbr(_Entity_):
                                    """
                                    App PBR entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr']['meta_info']


                                class AppIdEdpl(_Entity_):
                                    """
                                    App EDPL entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                    return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2']['meta_info']


                            class TcamLtOds8(_Entity_):
                                """
                                TCAM ODS8 partition summary
                                
                                .. attribute:: acl_common
                                
                                	ACL common region
                                	**type**\:  :py:class:`AclCommon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_ifib
                                
                                	App IFIB entry
                                	**type**\:  :py:class:`AppIdIfib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_qos
                                
                                	App qos entry
                                	**type**\:  :py:class:`AppIdQos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_acl
                                
                                	App acl entry
                                	**type**\:  :py:class:`AppIdAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_afmon
                                
                                	App afmon entry
                                	**type**\:  :py:class:`AppIdAfmon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_li
                                
                                	App LI entry
                                	**type**\:  :py:class:`AppIdLi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_pbr
                                
                                	App PBR entry
                                	**type**\:  :py:class:`AppIdPbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr>`
                                
                                	**config**\: False
                                
                                .. attribute:: app_id_edpl
                                
                                	App EDPL entry
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
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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


                                class AclCommon(_Entity_):
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon']['meta_info']


                                class AppIdIfib(_Entity_):
                                    """
                                    App IFIB entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib']['meta_info']


                                class AppIdQos(_Entity_):
                                    """
                                    App qos entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos']['meta_info']


                                class AppIdAcl(_Entity_):
                                    """
                                    App acl entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl']['meta_info']


                                class AppIdAfmon(_Entity_):
                                    """
                                    App afmon entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon']['meta_info']


                                class AppIdLi(_Entity_):
                                    """
                                    App LI entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi']['meta_info']


                                class AppIdPbr(_Entity_):
                                    """
                                    App PBR entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr']['meta_info']


                                class AppIdEdpl(_Entity_):
                                    """
                                    App EDPL entry
                                    
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
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
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

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                    return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8']['meta_info']


                            class TcamLtL2(_Entity_):
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
                                
                                	Valid entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: free_entries
                                
                                	Free entries
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                    return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                            return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary']['meta_info']


                    class L2rmHwResource(_Entity_):
                        """
                        L2rm Hardware Resources
                        
                        .. attribute:: hw_resource
                        
                        	resources per hw blk
                        	**type**\:  :py:class:`HwResource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource.HwResource>`
                        
                        	**config**\: False
                        
                        .. attribute:: ppt_alloc
                        
                        	ppt allocated
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: ppt_write
                        
                        	ppt write
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: ppt_free
                        
                        	ppt free
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'asr9k-np-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource, self).__init__()

                            self.yang_name = "l2rm-hw-resource"
                            self.yang_parent_name = "np"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("hw-resource", ("hw_resource", HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource.HwResource))])
                            self._leafs = OrderedDict([
                                ('ppt_alloc', (YLeaf(YType.uint64, 'ppt-alloc'), ['int'])),
                                ('ppt_write', (YLeaf(YType.uint64, 'ppt-write'), ['int'])),
                                ('ppt_free', (YLeaf(YType.uint64, 'ppt-free'), ['int'])),
                            ])
                            self.ppt_alloc = None
                            self.ppt_write = None
                            self.ppt_free = None

                            self.hw_resource = HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource.HwResource()
                            self.hw_resource.parent = self
                            self._children_name_map["hw_resource"] = "hw-resource"
                            self._segment_path = lambda: "l2rm-hw-resource"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource, ['ppt_alloc', 'ppt_write', 'ppt_free'], name, value)


                        class HwResource(_Entity_):
                            """
                            resources per hw blk
                            
                            .. attribute:: hash_block
                            
                            	Hash Block hw blk
                            	**type**\: list of  		 :py:class:`HashBlock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource.HwResource.HashBlock>`
                            
                            	**config**\: False
                            
                            .. attribute:: tcam_partition
                            
                            	TCAM partition per hw blk
                            	**type**\: list of  		 :py:class:`TcamPartition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper.HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource.HwResource.TcamPartition>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'asr9k-np-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource.HwResource, self).__init__()

                                self.yang_name = "hw-resource"
                                self.yang_parent_name = "l2rm-hw-resource"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("hash-block", ("hash_block", HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource.HwResource.HashBlock)), ("tcam-partition", ("tcam_partition", HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource.HwResource.TcamPartition))])
                                self._leafs = OrderedDict()

                                self.hash_block = YList(self)
                                self.tcam_partition = YList(self)
                                self._segment_path = lambda: "hw-resource"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource.HwResource, [], name, value)


                            class HashBlock(_Entity_):
                                """
                                Hash Block hw blk
                                
                                .. attribute:: hash_blk
                                
                                	hash block
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: total
                                
                                	total
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: free
                                
                                	free
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource.HwResource.HashBlock, self).__init__()

                                    self.yang_name = "hash-block"
                                    self.yang_parent_name = "hw-resource"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('hash_blk', (YLeaf(YType.uint32, 'hash-blk'), ['int'])),
                                        ('total', (YLeaf(YType.uint32, 'total'), ['int'])),
                                        ('free', (YLeaf(YType.uint32, 'free'), ['int'])),
                                    ])
                                    self.hash_blk = None
                                    self.total = None
                                    self.free = None
                                    self._segment_path = lambda: "hash-block"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource.HwResource.HashBlock, ['hash_blk', 'total', 'free'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                    return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource.HwResource.HashBlock']['meta_info']


                            class TcamPartition(_Entity_):
                                """
                                TCAM partition per hw blk
                                
                                .. attribute:: tcam_par
                                
                                	tcam par
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: total
                                
                                	total
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: free
                                
                                	free
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-np-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource.HwResource.TcamPartition, self).__init__()

                                    self.yang_name = "tcam-partition"
                                    self.yang_parent_name = "hw-resource"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('tcam_par', (YLeaf(YType.uint32, 'tcam-par'), ['int'])),
                                        ('total', (YLeaf(YType.uint32, 'total'), ['int'])),
                                        ('free', (YLeaf(YType.uint32, 'free'), ['int'])),
                                    ])
                                    self.tcam_par = None
                                    self.total = None
                                    self.free = None
                                    self._segment_path = lambda: "tcam-partition"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource.HwResource.TcamPartition, ['tcam_par', 'total', 'free'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                    return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource.HwResource.TcamPartition']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource.HwResource']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                            return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.L2rmHwResource']['meta_info']


                    class Profile(_Entity_):
                        """
                        Hardware Profile
                        
                        .. attribute:: scale
                        
                        	Scale
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'asr9k-np-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(HardwareModuleNp.Nodes.Node.Nps.Np.Profile, self).__init__()

                            self.yang_name = "profile"
                            self.yang_parent_name = "np"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('scale', (YLeaf(YType.str, 'scale'), ['str'])),
                            ])
                            self.scale = None
                            self._segment_path = lambda: "profile"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HardwareModuleNp.Nodes.Node.Nps.Np.Profile, ['scale'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                            return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.Profile']['meta_info']


                    class Counters(_Entity_):
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
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class NpCounter(_Entity_):
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
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                            return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.Counters']['meta_info']


                    class FastDrop(_Entity_):
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
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class NpFastDrop(_Entity_):
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
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                                return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                            return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop']['meta_info']


                    class Efd(_Entity_):
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
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                            return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.Efd']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                        return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps.Np']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                    return meta._meta_table['HardwareModuleNp.Nodes.Node.Nps']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
                return meta._meta_table['HardwareModuleNp.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
            return meta._meta_table['HardwareModuleNp.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = HardwareModuleNp()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_np_oper as meta
        return meta._meta_table['HardwareModuleNp']['meta_info']


