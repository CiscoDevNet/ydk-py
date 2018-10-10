""" Cisco_IOS_XR_prm_server_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR prm\-server package operational data.

This module contains definitions
for the following management objects\:
  hardware\-module\: PRM data
  prm\: prm

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class HardwareModule(Entity):
    """
    PRM data
    
    .. attribute:: nodes
    
    	List of PRM Nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes>`
    
    

    """

    _prefix = 'prm-server-oper'
    _revision = '2016-02-22'

    def __init__(self):
        super(HardwareModule, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module"
        self.yang_parent_name = "Cisco-IOS-XR-prm-server-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", HardwareModule.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = HardwareModule.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-prm-server-oper:hardware-module"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HardwareModule, [], name, value)


    class Nodes(Entity):
        """
        List of PRM Nodes
        
        .. attribute:: node
        
        	Node Information
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node>`
        
        

        """

        _prefix = 'prm-server-oper'
        _revision = '2016-02-22'

        def __init__(self):
            super(HardwareModule.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "hardware-module"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", HardwareModule.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-prm-server-oper:hardware-module/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HardwareModule.Nodes, [], name, value)


        class Node(Entity):
            """
            Node Information
            
            .. attribute:: node_name  (key)
            
            	The node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: np
            
            	Server specific
            	**type**\:  :py:class:`Np <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np>`
            
            

            """

            _prefix = 'prm-server-oper'
            _revision = '2016-02-22'

            def __init__(self):
                super(HardwareModule.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("np", ("np", HardwareModule.Nodes.Node.Np))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.np = HardwareModule.Nodes.Node.Np()
                self.np.parent = self
                self._children_name_map["np"] = "np"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-prm-server-oper:hardware-module/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModule.Nodes.Node, ['node_name'], name, value)


            class Np(Entity):
                """
                Server specific
                
                .. attribute:: cpu
                
                	Resource specific
                	**type**\:  :py:class:`Cpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.Cpu>`
                
                .. attribute:: platform_drop
                
                	Platform drops
                	**type**\:  :py:class:`PlatformDrop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.PlatformDrop>`
                
                

                """

                _prefix = 'prm-server-oper'
                _revision = '2016-02-22'

                def __init__(self):
                    super(HardwareModule.Nodes.Node.Np, self).__init__()

                    self.yang_name = "np"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("cpu", ("cpu", HardwareModule.Nodes.Node.Np.Cpu)), ("platform-drop", ("platform_drop", HardwareModule.Nodes.Node.Np.PlatformDrop))])
                    self._leafs = OrderedDict()

                    self.cpu = HardwareModule.Nodes.Node.Np.Cpu()
                    self.cpu.parent = self
                    self._children_name_map["cpu"] = "cpu"

                    self.platform_drop = HardwareModule.Nodes.Node.Np.PlatformDrop()
                    self.platform_drop.parent = self
                    self._children_name_map["platform_drop"] = "platform-drop"
                    self._segment_path = lambda: "np"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModule.Nodes.Node.Np, [], name, value)


                class Cpu(Entity):
                    """
                    Resource specific
                    
                    .. attribute:: indexes
                    
                    	Data for software resource
                    	**type**\:  :py:class:`Indexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.Cpu.Indexes>`
                    
                    

                    """

                    _prefix = 'prm-server-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(HardwareModule.Nodes.Node.Np.Cpu, self).__init__()

                        self.yang_name = "cpu"
                        self.yang_parent_name = "np"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("indexes", ("indexes", HardwareModule.Nodes.Node.Np.Cpu.Indexes))])
                        self._leafs = OrderedDict()

                        self.indexes = HardwareModule.Nodes.Node.Np.Cpu.Indexes()
                        self.indexes.parent = self
                        self._children_name_map["indexes"] = "indexes"
                        self._segment_path = lambda: "cpu"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HardwareModule.Nodes.Node.Np.Cpu, [], name, value)


                    class Indexes(Entity):
                        """
                        Data for software resource
                        
                        .. attribute:: index
                        
                        	Queue Stats
                        	**type**\: list of  		 :py:class:`Index <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.Cpu.Indexes.Index>`
                        
                        

                        """

                        _prefix = 'prm-server-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(HardwareModule.Nodes.Node.Np.Cpu.Indexes, self).__init__()

                            self.yang_name = "indexes"
                            self.yang_parent_name = "cpu"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("index", ("index", HardwareModule.Nodes.Node.Np.Cpu.Indexes.Index))])
                            self._leafs = OrderedDict()

                            self.index = YList(self)
                            self._segment_path = lambda: "indexes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HardwareModule.Nodes.Node.Np.Cpu.Indexes, [], name, value)


                        class Index(Entity):
                            """
                            Queue Stats
                            
                            .. attribute:: index  (key)
                            
                            	Index value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: cos_q_name
                            
                            	CosQ Name
                            	**type**\: str
                            
                            	**length:** 0..1024
                            
                            .. attribute:: cos_q
                            
                            	CosQ No
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: rx_channel
                            
                            	Rx DMA Channel
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: flow_rate
                            
                            	Flow Rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: burst
                            
                            	Burst
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: accepted
                            
                            	Accepted
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dropped
                            
                            	Dropped
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'prm-server-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                super(HardwareModule.Nodes.Node.Np.Cpu.Indexes.Index, self).__init__()

                                self.yang_name = "index"
                                self.yang_parent_name = "indexes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['index']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                    ('cos_q_name', (YLeaf(YType.str, 'cos-q-name'), ['str'])),
                                    ('cos_q', (YLeaf(YType.uint8, 'cos-q'), ['int'])),
                                    ('rx_channel', (YLeaf(YType.uint32, 'rx-channel'), ['int'])),
                                    ('flow_rate', (YLeaf(YType.uint32, 'flow-rate'), ['int'])),
                                    ('burst', (YLeaf(YType.uint32, 'burst'), ['int'])),
                                    ('accepted', (YLeaf(YType.uint64, 'accepted'), ['int'])),
                                    ('dropped', (YLeaf(YType.uint64, 'dropped'), ['int'])),
                                ])
                                self.index = None
                                self.cos_q_name = None
                                self.cos_q = None
                                self.rx_channel = None
                                self.flow_rate = None
                                self.burst = None
                                self.accepted = None
                                self.dropped = None
                                self._segment_path = lambda: "index" + "[index='" + str(self.index) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(HardwareModule.Nodes.Node.Np.Cpu.Indexes.Index, ['index', 'cos_q_name', 'cos_q', 'rx_channel', 'flow_rate', 'burst', 'accepted', 'dropped'], name, value)


                class PlatformDrop(Entity):
                    """
                    Platform drops
                    
                    .. attribute:: indxes
                    
                    	Captured Packets
                    	**type**\:  :py:class:`Indxes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes>`
                    
                    .. attribute:: idxes
                    
                    	Stats for Drop packets
                    	**type**\:  :py:class:`Idxes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes>`
                    
                    

                    """

                    _prefix = 'prm-server-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(HardwareModule.Nodes.Node.Np.PlatformDrop, self).__init__()

                        self.yang_name = "platform-drop"
                        self.yang_parent_name = "np"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("indxes", ("indxes", HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes)), ("idxes", ("idxes", HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes))])
                        self._leafs = OrderedDict()

                        self.indxes = HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes()
                        self.indxes.parent = self
                        self._children_name_map["indxes"] = "indxes"

                        self.idxes = HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes()
                        self.idxes.parent = self
                        self._children_name_map["idxes"] = "idxes"
                        self._segment_path = lambda: "platform-drop"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HardwareModule.Nodes.Node.Np.PlatformDrop, [], name, value)


                    class Indxes(Entity):
                        """
                        Captured Packets
                        
                        .. attribute:: indx
                        
                        	Captured packets
                        	**type**\: list of  		 :py:class:`Indx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes.Indx>`
                        
                        

                        """

                        _prefix = 'prm-server-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes, self).__init__()

                            self.yang_name = "indxes"
                            self.yang_parent_name = "platform-drop"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("indx", ("indx", HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes.Indx))])
                            self._leafs = OrderedDict()

                            self.indx = YList(self)
                            self._segment_path = lambda: "indxes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes, [], name, value)


                        class Indx(Entity):
                            """
                            Captured packets
                            
                            .. attribute:: index  (key)
                            
                            	Index value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total_captured
                            
                            	Total packets Captured
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: captured_pak
                            
                            	Captured Packet
                            	**type**\: str
                            
                            	**length:** 0..1024
                            
                            .. attribute:: pkt_index
                            
                            	Packet Index
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ifhandle
                            
                            	If Handle
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: buffer_len
                            
                            	Buffer Length
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: reason_hi
                            
                            	Reason Hi
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: reason
                            
                            	Reason
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: years
                            
                            	Year
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: hours
                            
                            	Hours
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: hour
                            
                            .. attribute:: days
                            
                            	Days
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: day
                            
                            .. attribute:: mins
                            
                            	Minutes
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: minute
                            
                            .. attribute:: secs
                            
                            	Seconds
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'prm-server-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                super(HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes.Indx, self).__init__()

                                self.yang_name = "indx"
                                self.yang_parent_name = "indxes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['index']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                    ('total_captured', (YLeaf(YType.uint32, 'total-captured'), ['int'])),
                                    ('captured_pak', (YLeaf(YType.str, 'captured-pak'), ['str'])),
                                    ('pkt_index', (YLeaf(YType.uint8, 'pkt-index'), ['int'])),
                                    ('ifhandle', (YLeaf(YType.uint32, 'ifhandle'), ['int'])),
                                    ('buffer_len', (YLeaf(YType.uint32, 'buffer-len'), ['int'])),
                                    ('reason_hi', (YLeaf(YType.uint32, 'reason-hi'), ['int'])),
                                    ('reason', (YLeaf(YType.uint32, 'reason'), ['int'])),
                                    ('years', (YLeaf(YType.uint64, 'years'), ['int'])),
                                    ('hours', (YLeaf(YType.uint64, 'hours'), ['int'])),
                                    ('days', (YLeaf(YType.uint64, 'days'), ['int'])),
                                    ('mins', (YLeaf(YType.uint64, 'mins'), ['int'])),
                                    ('secs', (YLeaf(YType.uint64, 'secs'), ['int'])),
                                ])
                                self.index = None
                                self.total_captured = None
                                self.captured_pak = None
                                self.pkt_index = None
                                self.ifhandle = None
                                self.buffer_len = None
                                self.reason_hi = None
                                self.reason = None
                                self.years = None
                                self.hours = None
                                self.days = None
                                self.mins = None
                                self.secs = None
                                self._segment_path = lambda: "indx" + "[index='" + str(self.index) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes.Indx, ['index', 'total_captured', 'captured_pak', 'pkt_index', 'ifhandle', 'buffer_len', 'reason_hi', 'reason', 'years', 'hours', 'days', 'mins', 'secs'], name, value)


                    class Idxes(Entity):
                        """
                        Stats for Drop packets
                        
                        .. attribute:: idx
                        
                        	Drop Stats
                        	**type**\: list of  		 :py:class:`Idx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes.Idx>`
                        
                        

                        """

                        _prefix = 'prm-server-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes, self).__init__()

                            self.yang_name = "idxes"
                            self.yang_parent_name = "platform-drop"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("idx", ("idx", HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes.Idx))])
                            self._leafs = OrderedDict()

                            self.idx = YList(self)
                            self._segment_path = lambda: "idxes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes, [], name, value)


                        class Idx(Entity):
                            """
                            Drop Stats
                            
                            .. attribute:: index  (key)
                            
                            	Index value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: drop_reason
                            
                            	Drop Reason
                            	**type**\: str
                            
                            	**length:** 0..1024
                            
                            .. attribute:: counters
                            
                            	Counter
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'prm-server-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                super(HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes.Idx, self).__init__()

                                self.yang_name = "idx"
                                self.yang_parent_name = "idxes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['index']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                    ('drop_reason', (YLeaf(YType.str, 'drop-reason'), ['str'])),
                                    ('counters', (YLeaf(YType.uint32, 'counters'), ['int'])),
                                ])
                                self.index = None
                                self.drop_reason = None
                                self.counters = None
                                self._segment_path = lambda: "idx" + "[index='" + str(self.index) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes.Idx, ['index', 'drop_reason', 'counters'], name, value)

    def clone_ptr(self):
        self._top_entity = HardwareModule()
        return self._top_entity

class Prm(Entity):
    """
    prm
    
    .. attribute:: nodes
    
    	List of PRM Nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.Prm.Nodes>`
    
    

    """

    _prefix = 'prm-server-oper'
    _revision = '2016-02-22'

    def __init__(self):
        super(Prm, self).__init__()
        self._top_entity = None

        self.yang_name = "prm"
        self.yang_parent_name = "Cisco-IOS-XR-prm-server-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Prm.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Prm.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-prm-server-oper:prm"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Prm, [], name, value)


    class Nodes(Entity):
        """
        List of PRM Nodes
        
        .. attribute:: node
        
        	Node Information
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.Prm.Nodes.Node>`
        
        

        """

        _prefix = 'prm-server-oper'
        _revision = '2016-02-22'

        def __init__(self):
            super(Prm.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "prm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Prm.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-prm-server-oper:prm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Prm.Nodes, [], name, value)


        class Node(Entity):
            """
            Node Information
            
            .. attribute:: node_name  (key)
            
            	The node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: server
            
            	Server specific
            	**type**\:  :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.Prm.Nodes.Node.Server>`
            
            

            """

            _prefix = 'prm-server-oper'
            _revision = '2016-02-22'

            def __init__(self):
                super(Prm.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("server", ("server", Prm.Nodes.Node.Server))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.server = Prm.Nodes.Node.Server()
                self.server.parent = self
                self._children_name_map["server"] = "server"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-prm-server-oper:prm/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Prm.Nodes.Node, ['node_name'], name, value)


            class Server(Entity):
                """
                Server specific
                
                .. attribute:: resource
                
                	Resource specific
                	**type**\:  :py:class:`Resource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.Prm.Nodes.Node.Server.Resource>`
                
                

                """

                _prefix = 'prm-server-oper'
                _revision = '2016-02-22'

                def __init__(self):
                    super(Prm.Nodes.Node.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("resource", ("resource", Prm.Nodes.Node.Server.Resource))])
                    self._leafs = OrderedDict()

                    self.resource = Prm.Nodes.Node.Server.Resource()
                    self.resource.parent = self
                    self._children_name_map["resource"] = "resource"
                    self._segment_path = lambda: "server"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Prm.Nodes.Node.Server, [], name, value)


                class Resource(Entity):
                    """
                    Resource specific
                    
                    .. attribute:: indexes
                    
                    	Data for software resource
                    	**type**\:  :py:class:`Indexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.Prm.Nodes.Node.Server.Resource.Indexes>`
                    
                    

                    """

                    _prefix = 'prm-server-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(Prm.Nodes.Node.Server.Resource, self).__init__()

                        self.yang_name = "resource"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("indexes", ("indexes", Prm.Nodes.Node.Server.Resource.Indexes))])
                        self._leafs = OrderedDict()

                        self.indexes = Prm.Nodes.Node.Server.Resource.Indexes()
                        self.indexes.parent = self
                        self._children_name_map["indexes"] = "indexes"
                        self._segment_path = lambda: "resource"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Prm.Nodes.Node.Server.Resource, [], name, value)


                    class Indexes(Entity):
                        """
                        Data for software resource
                        
                        .. attribute:: index
                        
                        	Data for software resource
                        	**type**\: list of  		 :py:class:`Index <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper.Prm.Nodes.Node.Server.Resource.Indexes.Index>`
                        
                        

                        """

                        _prefix = 'prm-server-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(Prm.Nodes.Node.Server.Resource.Indexes, self).__init__()

                            self.yang_name = "indexes"
                            self.yang_parent_name = "resource"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("index", ("index", Prm.Nodes.Node.Server.Resource.Indexes.Index))])
                            self._leafs = OrderedDict()

                            self.index = YList(self)
                            self._segment_path = lambda: "indexes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Prm.Nodes.Node.Server.Resource.Indexes, [], name, value)


                        class Index(Entity):
                            """
                            Data for software resource
                            
                            .. attribute:: index  (key)
                            
                            	Index value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: resource_name
                            
                            	Resource Name
                            	**type**\: str
                            
                            	**length:** 0..1024
                            
                            .. attribute:: resource_type
                            
                            	Resource Type
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total_num
                            
                            	Total Resource Count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: free_num
                            
                            	Free Resource Count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: first_available_index
                            
                            	Next Free Index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_index
                            
                            	Start Index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: availability_status
                            
                            	Availability Status
                            	**type**\: bool
                            
                            .. attribute:: flags
                            
                            	Resource Flags
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: inconsistent
                            
                            	Inconsistice Flags
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'prm-server-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                super(Prm.Nodes.Node.Server.Resource.Indexes.Index, self).__init__()

                                self.yang_name = "index"
                                self.yang_parent_name = "indexes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['index']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                    ('resource_name', (YLeaf(YType.str, 'resource-name'), ['str'])),
                                    ('resource_type', (YLeaf(YType.uint32, 'resource-type'), ['int'])),
                                    ('total_num', (YLeaf(YType.uint32, 'total-num'), ['int'])),
                                    ('free_num', (YLeaf(YType.uint32, 'free-num'), ['int'])),
                                    ('first_available_index', (YLeaf(YType.uint32, 'first-available-index'), ['int'])),
                                    ('start_index', (YLeaf(YType.uint32, 'start-index'), ['int'])),
                                    ('availability_status', (YLeaf(YType.boolean, 'availability-status'), ['bool'])),
                                    ('flags', (YLeaf(YType.uint8, 'flags'), ['int'])),
                                    ('inconsistent', (YLeaf(YType.boolean, 'inconsistent'), ['bool'])),
                                ])
                                self.index = None
                                self.resource_name = None
                                self.resource_type = None
                                self.total_num = None
                                self.free_num = None
                                self.first_available_index = None
                                self.start_index = None
                                self.availability_status = None
                                self.flags = None
                                self.inconsistent = None
                                self._segment_path = lambda: "index" + "[index='" + str(self.index) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Prm.Nodes.Node.Server.Resource.Indexes.Index, ['index', 'resource_name', 'resource_type', 'total_num', 'free_num', 'first_available_index', 'start_index', 'availability_status', 'flags', 'inconsistent'], name, value)

    def clone_ptr(self):
        self._top_entity = Prm()
        return self._top_entity

