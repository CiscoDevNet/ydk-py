""" common_mpls_static 

YANG module describing configuration and
operational data relating to MPLS Static.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Hoptype(Enum):
    """
    Hoptype (Enum Class)

    The Nexthop type

    .. data:: PRIMARY = 0

    	Primary next hop

    .. data:: BACKUP = 1

    	Backup next hop

    """

    PRIMARY = Enum.YLeaf(0, "PRIMARY")

    BACKUP = Enum.YLeaf(1, "BACKUP")



class LspType(Identity):
    """
    The type of Label Switched Path
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:common-mpls-static", pref="common-mpls-static", tag="common-mpls-static:lsp-type"):
        super(LspType, self).__init__(ns, pref, tag)



class NexthopResolutionType(Identity):
    """
    The Routing Protocol from which the nexthop is resolved
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:common-mpls-static", pref="common-mpls-static", tag="common-mpls-static:nexthop-resolution-type"):
        super(NexthopResolutionType, self).__init__(ns, pref, tag)



class MplsStatic(Entity):
    """
    MPLS Static module
    
    .. attribute:: mpls_static_cfg
    
    	MPLS Static configuration commands
    	**type**\:  :py:class:`MplsStaticCfg <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg>`
    
    .. attribute:: mpls_static_state
    
    	MPLS static operational data
    	**type**\:  :py:class:`MplsStaticState <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState>`
    
    	**config**\: False
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        super(MplsStatic, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-static"
        self.yang_parent_name = "common-mpls-static"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("mpls-static-cfg", ("mpls_static_cfg", MplsStatic.MplsStaticCfg)), ("mpls-static-state", ("mpls_static_state", MplsStatic.MplsStaticState))])
        self._leafs = OrderedDict()

        self.mpls_static_cfg = MplsStatic.MplsStaticCfg()
        self.mpls_static_cfg.parent = self
        self._children_name_map["mpls_static_cfg"] = "mpls-static-cfg"

        self.mpls_static_state = MplsStatic.MplsStaticState()
        self.mpls_static_state.parent = self
        self._children_name_map["mpls_static_state"] = "mpls-static-state"
        self._segment_path = lambda: "common-mpls-static:mpls-static"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(MplsStatic, [], name, value)


    class MplsStaticCfg(Entity):
        """
        MPLS Static configuration commands
        
        .. attribute:: ipv4_ingress_lsps
        
        	The LSPs indexed by ipv4 prefix
        	**type**\:  :py:class:`Ipv4IngressLsps <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps>`
        
        .. attribute:: in_label_lsps
        
        	The LSPs indexed by in\-label
        	**type**\:  :py:class:`InLabelLsps <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps>`
        
        .. attribute:: ipv6_ingress_lsps
        
        	The LSPs indexed by ipv6 prefix
        	**type**\:  :py:class:`Ipv6IngressLsps <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps>`
        
        .. attribute:: interfaces
        
        	The list of interfaces configured with mpls
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Interfaces>`
        
        .. attribute:: named_lsps
        
        	The LSPs indexed by name
        	**type**\:  :py:class:`NamedLsps <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps>`
        
        

        """

        _prefix = 'ms'
        _revision = '2015-07-22'

        def __init__(self):
            super(MplsStatic.MplsStaticCfg, self).__init__()

            self.yang_name = "mpls-static-cfg"
            self.yang_parent_name = "mpls-static"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ipv4-ingress-lsps", ("ipv4_ingress_lsps", MplsStatic.MplsStaticCfg.Ipv4IngressLsps)), ("in-label-lsps", ("in_label_lsps", MplsStatic.MplsStaticCfg.InLabelLsps)), ("ipv6-ingress-lsps", ("ipv6_ingress_lsps", MplsStatic.MplsStaticCfg.Ipv6IngressLsps)), ("interfaces", ("interfaces", MplsStatic.MplsStaticCfg.Interfaces)), ("named-lsps", ("named_lsps", MplsStatic.MplsStaticCfg.NamedLsps))])
            self._leafs = OrderedDict()

            self.ipv4_ingress_lsps = MplsStatic.MplsStaticCfg.Ipv4IngressLsps()
            self.ipv4_ingress_lsps.parent = self
            self._children_name_map["ipv4_ingress_lsps"] = "ipv4-ingress-lsps"

            self.in_label_lsps = MplsStatic.MplsStaticCfg.InLabelLsps()
            self.in_label_lsps.parent = self
            self._children_name_map["in_label_lsps"] = "in-label-lsps"

            self.ipv6_ingress_lsps = MplsStatic.MplsStaticCfg.Ipv6IngressLsps()
            self.ipv6_ingress_lsps.parent = self
            self._children_name_map["ipv6_ingress_lsps"] = "ipv6-ingress-lsps"

            self.interfaces = MplsStatic.MplsStaticCfg.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"

            self.named_lsps = MplsStatic.MplsStaticCfg.NamedLsps()
            self.named_lsps.parent = self
            self._children_name_map["named_lsps"] = "named-lsps"
            self._segment_path = lambda: "mpls-static-cfg"
            self._absolute_path = lambda: "common-mpls-static:mpls-static/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MplsStatic.MplsStaticCfg, [], name, value)


        class Ipv4IngressLsps(Entity):
            """
            The LSPs indexed by ipv4 prefix
            
            .. attribute:: ipv4_ingress_lsp
            
            	MPLS Static IPv4 Label Switched Path Configuration at Ingress
            	**type**\: list of  		 :py:class:`Ipv4IngressLsp <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp>`
            
            

            """

            _prefix = 'ms'
            _revision = '2015-07-22'

            def __init__(self):
                super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps, self).__init__()

                self.yang_name = "ipv4-ingress-lsps"
                self.yang_parent_name = "mpls-static-cfg"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ipv4-ingress-lsp", ("ipv4_ingress_lsp", MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp))])
                self._leafs = OrderedDict()

                self.ipv4_ingress_lsp = YList(self)
                self._segment_path = lambda: "ipv4-ingress-lsps"
                self._absolute_path = lambda: "common-mpls-static:mpls-static/mpls-static-cfg/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv4IngressLsps, [], name, value)


            class Ipv4IngressLsp(Entity):
                """
                MPLS Static IPv4 Label Switched
                Path Configuration at Ingress
                
                .. attribute:: vrf_name  (key)
                
                	Name of the VRF
                	**type**\: str
                
                .. attribute:: prefix  (key)
                
                	IPv4 prefix of packets that will ingress on this LSP
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                .. attribute:: in_label
                
                	Value of the local label. Optional for ingress
                	**type**\: union of the below types:
                
                		**type**\: int
                
                			**range:** 16..1048575
                
                		**type**\:  :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                
                .. attribute:: path
                
                	Fowarding path
                	**type**\:  :py:class:`Path <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path>`
                
                .. attribute:: name
                
                	Name of the LSP
                	**type**\: str
                
                

                """

                _prefix = 'ms'
                _revision = '2015-07-22'

                def __init__(self):
                    super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp, self).__init__()

                    self.yang_name = "ipv4-ingress-lsp"
                    self.yang_parent_name = "ipv4-ingress-lsps"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name','prefix']
                    self._child_classes = OrderedDict([("path", ("path", MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path))])
                    self._leafs = OrderedDict([
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                        ('in_label', (YLeaf(YType.str, 'in-label'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.vrf_name = None
                    self.prefix = None
                    self.in_label = None
                    self.name = None

                    self.path = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path()
                    self.path.parent = self
                    self._children_name_map["path"] = "path"
                    self._segment_path = lambda: "ipv4-ingress-lsp" + "[vrf-name='" + str(self.vrf_name) + "']" + "[prefix='" + str(self.prefix) + "']"
                    self._absolute_path = lambda: "common-mpls-static:mpls-static/mpls-static-cfg/ipv4-ingress-lsps/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp, ['vrf_name', 'prefix', 'in_label', 'name'], name, value)


                class Path(Entity):
                    """
                    Fowarding path
                    
                    .. attribute:: next_hop
                    
                    	next\-hops list
                    	**type**\: list of  		 :py:class:`NextHop <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop>`
                    
                    .. attribute:: operations
                    
                    	The incoming label processing
                    	**type**\:  :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations>`
                    
                    .. attribute:: auto_protect
                    
                    	Enables automatic protection if true
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path, self).__init__()

                        self.yang_name = "path"
                        self.yang_parent_name = "ipv4-ingress-lsp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("next-hop", ("next_hop", MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop)), ("operations", ("operations", MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations))])
                        self._leafs = OrderedDict([
                            ('auto_protect', (YLeaf(YType.boolean, 'auto-protect'), ['bool'])),
                        ])
                        self.auto_protect = None

                        self.operations = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations()
                        self.operations.parent = self
                        self._children_name_map["operations"] = "operations"

                        self.next_hop = YList(self)
                        self._segment_path = lambda: "path"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path, ['auto_protect'], name, value)


                    class NextHop(Entity):
                        """
                        next\-hops list
                        
                        .. attribute:: index  (key)
                        
                        	Index of the nexthop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        .. attribute:: protected_by
                        
                        	Index of the nexthop that protects this nexthop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: next_hop_type
                        
                        	Next\-hop
                        	**type**\:  :py:class:`NextHopType <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.NextHopType>`
                        
                        .. attribute:: operations
                        
                        	The incoming label processing
                        	**type**\:  :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations>`
                        
                        .. attribute:: type
                        
                        	The forwarding path's hoptype
                        	**type**\:  :py:class:`Hoptype <ydk.models.cisco_ios_xe.common_mpls_static.Hoptype>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['index']
                            self._child_classes = OrderedDict([("next-hop-type", ("next_hop_type", MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.NextHopType)), ("operations", ("operations", MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations))])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                ('protected_by', (YLeaf(YType.uint32, 'protected-by'), ['int'])),
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xe.common_mpls_static', 'Hoptype', '')])),
                            ])
                            self.index = None
                            self.protected_by = None
                            self.type = None

                            self.next_hop_type = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.NextHopType()
                            self.next_hop_type.parent = self
                            self._children_name_map["next_hop_type"] = "next-hop-type"

                            self.operations = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations()
                            self.operations.parent = self
                            self._children_name_map["operations"] = "operations"
                            self._segment_path = lambda: "next-hop" + "[index='" + str(self.index) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop, ['index', 'protected_by', 'type'], name, value)


                        class NextHopType(Entity):
                            """
                            Next\-hop
                            
                            .. attribute:: out_interface_name
                            
                            	Name of the outgoing interface
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 Address of the nexthop
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: mac_address
                            
                            	MAC address of the nexthop
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address of the nexthop
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: if_index
                            
                            	The interface index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.NextHopType, self).__init__()

                                self.yang_name = "next-hop-type"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('out_interface_name', (YLeaf(YType.str, 'out-interface-name'), ['str'])),
                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                    ('if_index', (YLeaf(YType.uint32, 'if-index'), ['int'])),
                                ])
                                self.out_interface_name = None
                                self.ipv6_address = None
                                self.mac_address = None
                                self.ipv4_address = None
                                self.if_index = None
                                self._segment_path = lambda: "next-hop-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.NextHopType, ['out_interface_name', 'ipv6_address', 'mac_address', 'ipv4_address', 'if_index'], name, value)



                        class Operations(Entity):
                            """
                            The incoming label processing
                            
                            .. attribute:: pop_and_forward
                            
                            	Pop the incoming label and forward
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: swap
                            
                            	Push outgoing label stack
                            	**type**\:  :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap>`
                            
                            .. attribute:: preserve
                            
                            	preserve incoming label stack
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: push
                            
                            	Push outgoing label stack
                            	**type**\:  :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations, self).__init__()

                                self.yang_name = "operations"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("swap", ("swap", MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap)), ("push", ("push", MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push))])
                                self._leafs = OrderedDict([
                                    ('pop_and_forward', (YLeaf(YType.empty, 'pop-and-forward'), ['Empty'])),
                                    ('preserve', (YLeaf(YType.empty, 'preserve'), ['Empty'])),
                                ])
                                self.pop_and_forward = None
                                self.preserve = None

                                self.swap = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap()
                                self.swap.parent = self
                                self._children_name_map["swap"] = "swap"

                                self.push = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push()
                                self.push.parent = self
                                self._children_name_map["push"] = "push"
                                self._segment_path = lambda: "operations"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations, ['pop_and_forward', 'preserve'], name, value)


                            class Swap(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap, self).__init__()

                                    self.yang_name = "swap"
                                    self.yang_parent_name = "operations"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap.Stack))])
                                    self._leafs = OrderedDict()

                                    self.stack = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._segment_path = lambda: "swap"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap, [], name, value)


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: list of int
                                    
                                    			**range:** 16..1048575
                                    
                                    		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "swap"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                        ])
                                        self.label_stack = []
                                        self._segment_path = lambda: "stack"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap.Stack, ['label_stack'], name, value)




                            class Push(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push, self).__init__()

                                    self.yang_name = "push"
                                    self.yang_parent_name = "operations"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push.Stack))])
                                    self._leafs = OrderedDict()

                                    self.stack = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._segment_path = lambda: "push"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push, [], name, value)


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: list of int
                                    
                                    			**range:** 16..1048575
                                    
                                    		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "push"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                        ])
                                        self.label_stack = []
                                        self._segment_path = lambda: "stack"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push.Stack, ['label_stack'], name, value)






                    class Operations(Entity):
                        """
                        The incoming label processing
                        
                        .. attribute:: preserve
                        
                        	preserve incoming label stack
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: swap
                        
                        	Push outgoing label stack
                        	**type**\:  :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap>`
                        
                        .. attribute:: push
                        
                        	Push outgoing label stack
                        	**type**\:  :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push>`
                        
                        .. attribute:: pop_and_forward
                        
                        	Pop the incoming label and forward
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations, self).__init__()

                            self.yang_name = "operations"
                            self.yang_parent_name = "path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("swap", ("swap", MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap)), ("push", ("push", MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push))])
                            self._leafs = OrderedDict([
                                ('preserve', (YLeaf(YType.empty, 'preserve'), ['Empty'])),
                                ('pop_and_forward', (YLeaf(YType.empty, 'pop-and-forward'), ['Empty'])),
                            ])
                            self.preserve = None
                            self.pop_and_forward = None

                            self.swap = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap()
                            self.swap.parent = self
                            self._children_name_map["swap"] = "swap"

                            self.push = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push()
                            self.push.parent = self
                            self._children_name_map["push"] = "push"
                            self._segment_path = lambda: "operations"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations, ['preserve', 'pop_and_forward'], name, value)


                        class Swap(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap, self).__init__()

                                self.yang_name = "swap"
                                self.yang_parent_name = "operations"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap.Stack))])
                                self._leafs = OrderedDict()

                                self.stack = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._segment_path = lambda: "swap"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap, [], name, value)


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: union of the below types:
                                
                                		**type**\: list of int
                                
                                			**range:** 16..1048575
                                
                                		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "swap"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                    ])
                                    self.label_stack = []
                                    self._segment_path = lambda: "stack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap.Stack, ['label_stack'], name, value)




                        class Push(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push, self).__init__()

                                self.yang_name = "push"
                                self.yang_parent_name = "operations"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push.Stack))])
                                self._leafs = OrderedDict()

                                self.stack = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._segment_path = lambda: "push"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push, [], name, value)


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: union of the below types:
                                
                                		**type**\: list of int
                                
                                			**range:** 16..1048575
                                
                                		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "push"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                    ])
                                    self.label_stack = []
                                    self._segment_path = lambda: "stack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push.Stack, ['label_stack'], name, value)








        class InLabelLsps(Entity):
            """
            The LSPs indexed by in\-label
            
            .. attribute:: in_label_lsp
            
            	Non\-ingress MPLS Static LSPs, keyed on the incoming label
            	**type**\: list of  		 :py:class:`InLabelLsp <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp>`
            
            

            """

            _prefix = 'ms'
            _revision = '2015-07-22'

            def __init__(self):
                super(MplsStatic.MplsStaticCfg.InLabelLsps, self).__init__()

                self.yang_name = "in-label-lsps"
                self.yang_parent_name = "mpls-static-cfg"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("in-label-lsp", ("in_label_lsp", MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp))])
                self._leafs = OrderedDict()

                self.in_label_lsp = YList(self)
                self._segment_path = lambda: "in-label-lsps"
                self._absolute_path = lambda: "common-mpls-static:mpls-static/mpls-static-cfg/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsStatic.MplsStaticCfg.InLabelLsps, [], name, value)


            class InLabelLsp(Entity):
                """
                Non\-ingress MPLS Static LSPs,
                keyed on the incoming label
                
                .. attribute:: vrf_name  (key)
                
                	Name of the VRF
                	**type**\: str
                
                .. attribute:: in_label  (key)
                
                	Value of the local label
                	**type**\: union of the below types:
                
                		**type**\: int
                
                			**range:** 16..1048575
                
                		**type**\:  :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                
                .. attribute:: path
                
                	Fowarding path
                	**type**\:  :py:class:`Path <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path>`
                
                

                """

                _prefix = 'ms'
                _revision = '2015-07-22'

                def __init__(self):
                    super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp, self).__init__()

                    self.yang_name = "in-label-lsp"
                    self.yang_parent_name = "in-label-lsps"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name','in_label']
                    self._child_classes = OrderedDict([("path", ("path", MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path))])
                    self._leafs = OrderedDict([
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('in_label', (YLeaf(YType.str, 'in-label'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                    ])
                    self.vrf_name = None
                    self.in_label = None

                    self.path = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path()
                    self.path.parent = self
                    self._children_name_map["path"] = "path"
                    self._segment_path = lambda: "in-label-lsp" + "[vrf-name='" + str(self.vrf_name) + "']" + "[in-label='" + str(self.in_label) + "']"
                    self._absolute_path = lambda: "common-mpls-static:mpls-static/mpls-static-cfg/in-label-lsps/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp, ['vrf_name', 'in_label'], name, value)


                class Path(Entity):
                    """
                    Fowarding path
                    
                    .. attribute:: operations
                    
                    	The incoming label processing
                    	**type**\:  :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations>`
                    
                    .. attribute:: auto_protect
                    
                    	Enables automatic protection if true
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: next_hop
                    
                    	next\-hops list
                    	**type**\: list of  		 :py:class:`NextHop <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop>`
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path, self).__init__()

                        self.yang_name = "path"
                        self.yang_parent_name = "in-label-lsp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("operations", ("operations", MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations)), ("next-hop", ("next_hop", MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop))])
                        self._leafs = OrderedDict([
                            ('auto_protect', (YLeaf(YType.boolean, 'auto-protect'), ['bool'])),
                        ])
                        self.auto_protect = None

                        self.operations = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations()
                        self.operations.parent = self
                        self._children_name_map["operations"] = "operations"

                        self.next_hop = YList(self)
                        self._segment_path = lambda: "path"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path, ['auto_protect'], name, value)


                    class Operations(Entity):
                        """
                        The incoming label processing
                        
                        .. attribute:: preserve
                        
                        	preserve incoming label stack
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: swap
                        
                        	Push outgoing label stack
                        	**type**\:  :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap>`
                        
                        .. attribute:: push
                        
                        	Push outgoing label stack
                        	**type**\:  :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push>`
                        
                        .. attribute:: pop_and_forward
                        
                        	Pop the incoming label and forward
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations, self).__init__()

                            self.yang_name = "operations"
                            self.yang_parent_name = "path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("swap", ("swap", MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap)), ("push", ("push", MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push))])
                            self._leafs = OrderedDict([
                                ('preserve', (YLeaf(YType.empty, 'preserve'), ['Empty'])),
                                ('pop_and_forward', (YLeaf(YType.empty, 'pop-and-forward'), ['Empty'])),
                            ])
                            self.preserve = None
                            self.pop_and_forward = None

                            self.swap = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap()
                            self.swap.parent = self
                            self._children_name_map["swap"] = "swap"

                            self.push = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push()
                            self.push.parent = self
                            self._children_name_map["push"] = "push"
                            self._segment_path = lambda: "operations"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations, ['preserve', 'pop_and_forward'], name, value)


                        class Swap(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap, self).__init__()

                                self.yang_name = "swap"
                                self.yang_parent_name = "operations"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap.Stack))])
                                self._leafs = OrderedDict()

                                self.stack = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._segment_path = lambda: "swap"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap, [], name, value)


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: union of the below types:
                                
                                		**type**\: list of int
                                
                                			**range:** 16..1048575
                                
                                		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "swap"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                    ])
                                    self.label_stack = []
                                    self._segment_path = lambda: "stack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap.Stack, ['label_stack'], name, value)




                        class Push(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push, self).__init__()

                                self.yang_name = "push"
                                self.yang_parent_name = "operations"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push.Stack))])
                                self._leafs = OrderedDict()

                                self.stack = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._segment_path = lambda: "push"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push, [], name, value)


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: union of the below types:
                                
                                		**type**\: list of int
                                
                                			**range:** 16..1048575
                                
                                		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "push"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                    ])
                                    self.label_stack = []
                                    self._segment_path = lambda: "stack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push.Stack, ['label_stack'], name, value)





                    class NextHop(Entity):
                        """
                        next\-hops list
                        
                        .. attribute:: index  (key)
                        
                        	Index of the nexthop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        .. attribute:: type
                        
                        	The forwarding path's hoptype
                        	**type**\:  :py:class:`Hoptype <ydk.models.cisco_ios_xe.common_mpls_static.Hoptype>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: protected_by
                        
                        	Index of the nexthop that protects this nexthop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: next_hop_type
                        
                        	Next\-hop
                        	**type**\:  :py:class:`NextHopType <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.NextHopType>`
                        
                        .. attribute:: operations
                        
                        	The incoming label processing
                        	**type**\:  :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations>`
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['index']
                            self._child_classes = OrderedDict([("next-hop-type", ("next_hop_type", MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.NextHopType)), ("operations", ("operations", MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations))])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xe.common_mpls_static', 'Hoptype', '')])),
                                ('protected_by', (YLeaf(YType.uint32, 'protected-by'), ['int'])),
                            ])
                            self.index = None
                            self.type = None
                            self.protected_by = None

                            self.next_hop_type = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.NextHopType()
                            self.next_hop_type.parent = self
                            self._children_name_map["next_hop_type"] = "next-hop-type"

                            self.operations = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations()
                            self.operations.parent = self
                            self._children_name_map["operations"] = "operations"
                            self._segment_path = lambda: "next-hop" + "[index='" + str(self.index) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop, ['index', 'type', 'protected_by'], name, value)


                        class NextHopType(Entity):
                            """
                            Next\-hop
                            
                            .. attribute:: if_index
                            
                            	The interface index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address of the nexthop
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 Address of the nexthop
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: mac_address
                            
                            	MAC address of the nexthop
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**mandatory**\: True
                            
                            .. attribute:: out_interface_name
                            
                            	Name of the outgoing interface
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.NextHopType, self).__init__()

                                self.yang_name = "next-hop-type"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('if_index', (YLeaf(YType.uint32, 'if-index'), ['int'])),
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                    ('out_interface_name', (YLeaf(YType.str, 'out-interface-name'), ['str'])),
                                ])
                                self.if_index = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.mac_address = None
                                self.out_interface_name = None
                                self._segment_path = lambda: "next-hop-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.NextHopType, ['if_index', 'ipv4_address', 'ipv6_address', 'mac_address', 'out_interface_name'], name, value)



                        class Operations(Entity):
                            """
                            The incoming label processing
                            
                            .. attribute:: preserve
                            
                            	preserve incoming label stack
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: swap
                            
                            	Push outgoing label stack
                            	**type**\:  :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap>`
                            
                            .. attribute:: push
                            
                            	Push outgoing label stack
                            	**type**\:  :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push>`
                            
                            .. attribute:: pop_and_forward
                            
                            	Pop the incoming label and forward
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations, self).__init__()

                                self.yang_name = "operations"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("swap", ("swap", MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap)), ("push", ("push", MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push))])
                                self._leafs = OrderedDict([
                                    ('preserve', (YLeaf(YType.empty, 'preserve'), ['Empty'])),
                                    ('pop_and_forward', (YLeaf(YType.empty, 'pop-and-forward'), ['Empty'])),
                                ])
                                self.preserve = None
                                self.pop_and_forward = None

                                self.swap = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap()
                                self.swap.parent = self
                                self._children_name_map["swap"] = "swap"

                                self.push = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push()
                                self.push.parent = self
                                self._children_name_map["push"] = "push"
                                self._segment_path = lambda: "operations"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations, ['preserve', 'pop_and_forward'], name, value)


                            class Swap(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap, self).__init__()

                                    self.yang_name = "swap"
                                    self.yang_parent_name = "operations"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap.Stack))])
                                    self._leafs = OrderedDict()

                                    self.stack = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._segment_path = lambda: "swap"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap, [], name, value)


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: list of int
                                    
                                    			**range:** 16..1048575
                                    
                                    		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "swap"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                        ])
                                        self.label_stack = []
                                        self._segment_path = lambda: "stack"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap.Stack, ['label_stack'], name, value)




                            class Push(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push, self).__init__()

                                    self.yang_name = "push"
                                    self.yang_parent_name = "operations"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push.Stack))])
                                    self._leafs = OrderedDict()

                                    self.stack = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._segment_path = lambda: "push"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push, [], name, value)


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: list of int
                                    
                                    			**range:** 16..1048575
                                    
                                    		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "push"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                        ])
                                        self.label_stack = []
                                        self._segment_path = lambda: "stack"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push.Stack, ['label_stack'], name, value)









        class Ipv6IngressLsps(Entity):
            """
            The LSPs indexed by ipv6 prefix
            
            .. attribute:: ipv6_ingress_lsp
            
            	MPLS Static IPv6 Label Switched Path Configuration at Ingress
            	**type**\: list of  		 :py:class:`Ipv6IngressLsp <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp>`
            
            

            """

            _prefix = 'ms'
            _revision = '2015-07-22'

            def __init__(self):
                super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps, self).__init__()

                self.yang_name = "ipv6-ingress-lsps"
                self.yang_parent_name = "mpls-static-cfg"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ipv6-ingress-lsp", ("ipv6_ingress_lsp", MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp))])
                self._leafs = OrderedDict()

                self.ipv6_ingress_lsp = YList(self)
                self._segment_path = lambda: "ipv6-ingress-lsps"
                self._absolute_path = lambda: "common-mpls-static:mpls-static/mpls-static-cfg/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv6IngressLsps, [], name, value)


            class Ipv6IngressLsp(Entity):
                """
                MPLS Static IPv6 Label Switched Path
                Configuration at Ingress
                
                .. attribute:: vrf_name  (key)
                
                	Name of the VRF
                	**type**\: str
                
                .. attribute:: prefix  (key)
                
                	IPv6 prefix of packets that will ingress on this LSP
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                .. attribute:: name
                
                	Name of the LSP
                	**type**\: str
                
                .. attribute:: in_label
                
                	Value of the local label. Optional for ingress
                	**type**\: union of the below types:
                
                		**type**\: int
                
                			**range:** 16..1048575
                
                		**type**\:  :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                
                .. attribute:: path
                
                	Fowarding path
                	**type**\:  :py:class:`Path <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path>`
                
                

                """

                _prefix = 'ms'
                _revision = '2015-07-22'

                def __init__(self):
                    super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp, self).__init__()

                    self.yang_name = "ipv6-ingress-lsp"
                    self.yang_parent_name = "ipv6-ingress-lsps"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name','prefix']
                    self._child_classes = OrderedDict([("path", ("path", MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path))])
                    self._leafs = OrderedDict([
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('in_label', (YLeaf(YType.str, 'in-label'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                    ])
                    self.vrf_name = None
                    self.prefix = None
                    self.name = None
                    self.in_label = None

                    self.path = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path()
                    self.path.parent = self
                    self._children_name_map["path"] = "path"
                    self._segment_path = lambda: "ipv6-ingress-lsp" + "[vrf-name='" + str(self.vrf_name) + "']" + "[prefix='" + str(self.prefix) + "']"
                    self._absolute_path = lambda: "common-mpls-static:mpls-static/mpls-static-cfg/ipv6-ingress-lsps/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp, ['vrf_name', 'prefix', 'name', 'in_label'], name, value)


                class Path(Entity):
                    """
                    Fowarding path
                    
                    .. attribute:: operations
                    
                    	The incoming label processing
                    	**type**\:  :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations>`
                    
                    .. attribute:: auto_protect
                    
                    	Enables automatic protection if true
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: next_hop
                    
                    	next\-hops list
                    	**type**\: list of  		 :py:class:`NextHop <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop>`
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path, self).__init__()

                        self.yang_name = "path"
                        self.yang_parent_name = "ipv6-ingress-lsp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("operations", ("operations", MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations)), ("next-hop", ("next_hop", MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop))])
                        self._leafs = OrderedDict([
                            ('auto_protect', (YLeaf(YType.boolean, 'auto-protect'), ['bool'])),
                        ])
                        self.auto_protect = None

                        self.operations = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations()
                        self.operations.parent = self
                        self._children_name_map["operations"] = "operations"

                        self.next_hop = YList(self)
                        self._segment_path = lambda: "path"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path, ['auto_protect'], name, value)


                    class Operations(Entity):
                        """
                        The incoming label processing
                        
                        .. attribute:: preserve
                        
                        	preserve incoming label stack
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: swap
                        
                        	Push outgoing label stack
                        	**type**\:  :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap>`
                        
                        .. attribute:: push
                        
                        	Push outgoing label stack
                        	**type**\:  :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push>`
                        
                        .. attribute:: pop_and_forward
                        
                        	Pop the incoming label and forward
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations, self).__init__()

                            self.yang_name = "operations"
                            self.yang_parent_name = "path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("swap", ("swap", MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap)), ("push", ("push", MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push))])
                            self._leafs = OrderedDict([
                                ('preserve', (YLeaf(YType.empty, 'preserve'), ['Empty'])),
                                ('pop_and_forward', (YLeaf(YType.empty, 'pop-and-forward'), ['Empty'])),
                            ])
                            self.preserve = None
                            self.pop_and_forward = None

                            self.swap = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap()
                            self.swap.parent = self
                            self._children_name_map["swap"] = "swap"

                            self.push = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push()
                            self.push.parent = self
                            self._children_name_map["push"] = "push"
                            self._segment_path = lambda: "operations"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations, ['preserve', 'pop_and_forward'], name, value)


                        class Swap(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap, self).__init__()

                                self.yang_name = "swap"
                                self.yang_parent_name = "operations"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap.Stack))])
                                self._leafs = OrderedDict()

                                self.stack = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._segment_path = lambda: "swap"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap, [], name, value)


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: union of the below types:
                                
                                		**type**\: list of int
                                
                                			**range:** 16..1048575
                                
                                		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "swap"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                    ])
                                    self.label_stack = []
                                    self._segment_path = lambda: "stack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap.Stack, ['label_stack'], name, value)




                        class Push(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push, self).__init__()

                                self.yang_name = "push"
                                self.yang_parent_name = "operations"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push.Stack))])
                                self._leafs = OrderedDict()

                                self.stack = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._segment_path = lambda: "push"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push, [], name, value)


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: union of the below types:
                                
                                		**type**\: list of int
                                
                                			**range:** 16..1048575
                                
                                		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "push"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                    ])
                                    self.label_stack = []
                                    self._segment_path = lambda: "stack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push.Stack, ['label_stack'], name, value)





                    class NextHop(Entity):
                        """
                        next\-hops list
                        
                        .. attribute:: index  (key)
                        
                        	Index of the nexthop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        .. attribute:: type
                        
                        	The forwarding path's hoptype
                        	**type**\:  :py:class:`Hoptype <ydk.models.cisco_ios_xe.common_mpls_static.Hoptype>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: protected_by
                        
                        	Index of the nexthop that protects this nexthop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: next_hop_type
                        
                        	Next\-hop
                        	**type**\:  :py:class:`NextHopType <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.NextHopType>`
                        
                        .. attribute:: operations
                        
                        	The incoming label processing
                        	**type**\:  :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations>`
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['index']
                            self._child_classes = OrderedDict([("next-hop-type", ("next_hop_type", MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.NextHopType)), ("operations", ("operations", MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations))])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xe.common_mpls_static', 'Hoptype', '')])),
                                ('protected_by', (YLeaf(YType.uint32, 'protected-by'), ['int'])),
                            ])
                            self.index = None
                            self.type = None
                            self.protected_by = None

                            self.next_hop_type = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.NextHopType()
                            self.next_hop_type.parent = self
                            self._children_name_map["next_hop_type"] = "next-hop-type"

                            self.operations = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations()
                            self.operations.parent = self
                            self._children_name_map["operations"] = "operations"
                            self._segment_path = lambda: "next-hop" + "[index='" + str(self.index) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop, ['index', 'type', 'protected_by'], name, value)


                        class NextHopType(Entity):
                            """
                            Next\-hop
                            
                            .. attribute:: if_index
                            
                            	The interface index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address of the nexthop
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 Address of the nexthop
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: mac_address
                            
                            	MAC address of the nexthop
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**mandatory**\: True
                            
                            .. attribute:: out_interface_name
                            
                            	Name of the outgoing interface
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.NextHopType, self).__init__()

                                self.yang_name = "next-hop-type"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('if_index', (YLeaf(YType.uint32, 'if-index'), ['int'])),
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                    ('out_interface_name', (YLeaf(YType.str, 'out-interface-name'), ['str'])),
                                ])
                                self.if_index = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.mac_address = None
                                self.out_interface_name = None
                                self._segment_path = lambda: "next-hop-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.NextHopType, ['if_index', 'ipv4_address', 'ipv6_address', 'mac_address', 'out_interface_name'], name, value)



                        class Operations(Entity):
                            """
                            The incoming label processing
                            
                            .. attribute:: preserve
                            
                            	preserve incoming label stack
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: swap
                            
                            	Push outgoing label stack
                            	**type**\:  :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap>`
                            
                            .. attribute:: push
                            
                            	Push outgoing label stack
                            	**type**\:  :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push>`
                            
                            .. attribute:: pop_and_forward
                            
                            	Pop the incoming label and forward
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations, self).__init__()

                                self.yang_name = "operations"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("swap", ("swap", MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap)), ("push", ("push", MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push))])
                                self._leafs = OrderedDict([
                                    ('preserve', (YLeaf(YType.empty, 'preserve'), ['Empty'])),
                                    ('pop_and_forward', (YLeaf(YType.empty, 'pop-and-forward'), ['Empty'])),
                                ])
                                self.preserve = None
                                self.pop_and_forward = None

                                self.swap = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap()
                                self.swap.parent = self
                                self._children_name_map["swap"] = "swap"

                                self.push = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push()
                                self.push.parent = self
                                self._children_name_map["push"] = "push"
                                self._segment_path = lambda: "operations"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations, ['preserve', 'pop_and_forward'], name, value)


                            class Swap(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap, self).__init__()

                                    self.yang_name = "swap"
                                    self.yang_parent_name = "operations"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap.Stack))])
                                    self._leafs = OrderedDict()

                                    self.stack = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._segment_path = lambda: "swap"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap, [], name, value)


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: list of int
                                    
                                    			**range:** 16..1048575
                                    
                                    		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "swap"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                        ])
                                        self.label_stack = []
                                        self._segment_path = lambda: "stack"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap.Stack, ['label_stack'], name, value)




                            class Push(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push, self).__init__()

                                    self.yang_name = "push"
                                    self.yang_parent_name = "operations"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push.Stack))])
                                    self._leafs = OrderedDict()

                                    self.stack = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._segment_path = lambda: "push"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push, [], name, value)


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: list of int
                                    
                                    			**range:** 16..1048575
                                    
                                    		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "push"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                        ])
                                        self.label_stack = []
                                        self._segment_path = lambda: "stack"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push.Stack, ['label_stack'], name, value)









        class Interfaces(Entity):
            """
            The list of interfaces configured with mpls
            
            .. attribute:: interface
            
            	List of interfaces that can be enabled under mpls static
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Interfaces.Interface>`
            
            

            """

            _prefix = 'ms'
            _revision = '2015-07-22'

            def __init__(self):
                super(MplsStatic.MplsStaticCfg.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "mpls-static-cfg"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface", ("interface", MplsStatic.MplsStaticCfg.Interfaces.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "common-mpls-static:mpls-static/mpls-static-cfg/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsStatic.MplsStaticCfg.Interfaces, [], name, value)


            class Interface(Entity):
                """
                List of interfaces that can be enabled under
                mpls static
                
                .. attribute:: name  (key)
                
                	Interface name
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                
                	**mandatory**\: True
                
                .. attribute:: enabled
                
                	Interface Enabled boolean
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ms'
                _revision = '2015-07-22'

                def __init__(self):
                    super(MplsStatic.MplsStaticCfg.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('enabled', (YLeaf(YType.uint32, 'enabled'), ['int'])),
                    ])
                    self.name = None
                    self.enabled = None
                    self._segment_path = lambda: "interface" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "common-mpls-static:mpls-static/mpls-static-cfg/interfaces/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.MplsStaticCfg.Interfaces.Interface, ['name', 'enabled'], name, value)




        class NamedLsps(Entity):
            """
            The LSPs indexed by name
            
            .. attribute:: named_lsp
            
            	MPLS Static Label Switched Path Configuration. The LSPs in this list are referenced by a string name. The LSPs may be ingress/egress/crossconnect, may have v4/v6 prefixes and may be associated with any VRF. The other specialized lists above are for implemetations that are keyed on prefixes or in\-labels instead of the LSP name
            	**type**\: list of  		 :py:class:`NamedLsp <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp>`
            
            

            """

            _prefix = 'ms'
            _revision = '2015-07-22'

            def __init__(self):
                super(MplsStatic.MplsStaticCfg.NamedLsps, self).__init__()

                self.yang_name = "named-lsps"
                self.yang_parent_name = "mpls-static-cfg"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("named-lsp", ("named_lsp", MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp))])
                self._leafs = OrderedDict()

                self.named_lsp = YList(self)
                self._segment_path = lambda: "named-lsps"
                self._absolute_path = lambda: "common-mpls-static:mpls-static/mpls-static-cfg/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsStatic.MplsStaticCfg.NamedLsps, [], name, value)


            class NamedLsp(Entity):
                """
                MPLS Static Label Switched Path Configuration.
                The LSPs in this list are referenced by a string name.
                The LSPs may be ingress/egress/crossconnect,
                may have v4/v6 prefixes and may be associated with any
                VRF. The other specialized lists above are for
                implemetations that are keyed on prefixes or in\-labels
                instead of the LSP name.
                
                .. attribute:: vrf_name  (key)
                
                	Name of the VRF
                	**type**\: str
                
                .. attribute:: name  (key)
                
                	Name of the LSP
                	**type**\: str
                
                	**mandatory**\: True
                
                .. attribute:: lsp_type
                
                	lsp type
                	**type**\:  :py:class:`LspType <ydk.models.cisco_ios_xe.common_mpls_static.LspType>`
                
                	**mandatory**\: True
                
                .. attribute:: in_label
                
                	Value of the local label
                	**type**\: union of the below types:
                
                		**type**\: int
                
                			**range:** 16..1048575
                
                		**type**\:  :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                
                .. attribute:: ipv4_prefix
                
                	ipv4 prefix
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                .. attribute:: ipv6_prefix
                
                	ipv6 prefix
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                .. attribute:: path
                
                	Fowarding path
                	**type**\:  :py:class:`Path <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path>`
                
                

                """

                _prefix = 'ms'
                _revision = '2015-07-22'

                def __init__(self):
                    super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp, self).__init__()

                    self.yang_name = "named-lsp"
                    self.yang_parent_name = "named-lsps"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name','name']
                    self._child_classes = OrderedDict([("path", ("path", MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path))])
                    self._leafs = OrderedDict([
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('lsp_type', (YLeaf(YType.identityref, 'lsp-type'), [('ydk.models.cisco_ios_xe.common_mpls_static', 'LspType')])),
                        ('in_label', (YLeaf(YType.str, 'in-label'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                        ('ipv4_prefix', (YLeaf(YType.str, 'ipv4-prefix'), ['str'])),
                        ('ipv6_prefix', (YLeaf(YType.str, 'ipv6-prefix'), ['str'])),
                    ])
                    self.vrf_name = None
                    self.name = None
                    self.lsp_type = None
                    self.in_label = None
                    self.ipv4_prefix = None
                    self.ipv6_prefix = None

                    self.path = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path()
                    self.path.parent = self
                    self._children_name_map["path"] = "path"
                    self._segment_path = lambda: "named-lsp" + "[vrf-name='" + str(self.vrf_name) + "']" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "common-mpls-static:mpls-static/mpls-static-cfg/named-lsps/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp, ['vrf_name', 'name', 'lsp_type', 'in_label', 'ipv4_prefix', 'ipv6_prefix'], name, value)


                class Path(Entity):
                    """
                    Fowarding path
                    
                    .. attribute:: operations
                    
                    	The incoming label processing
                    	**type**\:  :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations>`
                    
                    .. attribute:: auto_protect
                    
                    	Enables automatic protection if true
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: next_hop
                    
                    	next\-hops list
                    	**type**\: list of  		 :py:class:`NextHop <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop>`
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path, self).__init__()

                        self.yang_name = "path"
                        self.yang_parent_name = "named-lsp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("operations", ("operations", MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations)), ("next-hop", ("next_hop", MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop))])
                        self._leafs = OrderedDict([
                            ('auto_protect', (YLeaf(YType.boolean, 'auto-protect'), ['bool'])),
                        ])
                        self.auto_protect = None

                        self.operations = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations()
                        self.operations.parent = self
                        self._children_name_map["operations"] = "operations"

                        self.next_hop = YList(self)
                        self._segment_path = lambda: "path"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path, ['auto_protect'], name, value)


                    class Operations(Entity):
                        """
                        The incoming label processing
                        
                        .. attribute:: preserve
                        
                        	preserve incoming label stack
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: swap
                        
                        	Push outgoing label stack
                        	**type**\:  :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap>`
                        
                        .. attribute:: push
                        
                        	Push outgoing label stack
                        	**type**\:  :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push>`
                        
                        .. attribute:: pop_and_forward
                        
                        	Pop the incoming label and forward
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations, self).__init__()

                            self.yang_name = "operations"
                            self.yang_parent_name = "path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("swap", ("swap", MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap)), ("push", ("push", MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push))])
                            self._leafs = OrderedDict([
                                ('preserve', (YLeaf(YType.empty, 'preserve'), ['Empty'])),
                                ('pop_and_forward', (YLeaf(YType.empty, 'pop-and-forward'), ['Empty'])),
                            ])
                            self.preserve = None
                            self.pop_and_forward = None

                            self.swap = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap()
                            self.swap.parent = self
                            self._children_name_map["swap"] = "swap"

                            self.push = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push()
                            self.push.parent = self
                            self._children_name_map["push"] = "push"
                            self._segment_path = lambda: "operations"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations, ['preserve', 'pop_and_forward'], name, value)


                        class Swap(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap, self).__init__()

                                self.yang_name = "swap"
                                self.yang_parent_name = "operations"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap.Stack))])
                                self._leafs = OrderedDict()

                                self.stack = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._segment_path = lambda: "swap"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap, [], name, value)


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: union of the below types:
                                
                                		**type**\: list of int
                                
                                			**range:** 16..1048575
                                
                                		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "swap"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                    ])
                                    self.label_stack = []
                                    self._segment_path = lambda: "stack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap.Stack, ['label_stack'], name, value)




                        class Push(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push, self).__init__()

                                self.yang_name = "push"
                                self.yang_parent_name = "operations"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push.Stack))])
                                self._leafs = OrderedDict()

                                self.stack = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._segment_path = lambda: "push"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push, [], name, value)


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: union of the below types:
                                
                                		**type**\: list of int
                                
                                			**range:** 16..1048575
                                
                                		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "push"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                    ])
                                    self.label_stack = []
                                    self._segment_path = lambda: "stack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push.Stack, ['label_stack'], name, value)





                    class NextHop(Entity):
                        """
                        next\-hops list
                        
                        .. attribute:: index  (key)
                        
                        	Index of the nexthop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        .. attribute:: type
                        
                        	The forwarding path's hoptype
                        	**type**\:  :py:class:`Hoptype <ydk.models.cisco_ios_xe.common_mpls_static.Hoptype>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: protected_by
                        
                        	Index of the nexthop that protects this nexthop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: next_hop_type
                        
                        	Next\-hop
                        	**type**\:  :py:class:`NextHopType <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.NextHopType>`
                        
                        .. attribute:: operations
                        
                        	The incoming label processing
                        	**type**\:  :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations>`
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['index']
                            self._child_classes = OrderedDict([("next-hop-type", ("next_hop_type", MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.NextHopType)), ("operations", ("operations", MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations))])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xe.common_mpls_static', 'Hoptype', '')])),
                                ('protected_by', (YLeaf(YType.uint32, 'protected-by'), ['int'])),
                            ])
                            self.index = None
                            self.type = None
                            self.protected_by = None

                            self.next_hop_type = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.NextHopType()
                            self.next_hop_type.parent = self
                            self._children_name_map["next_hop_type"] = "next-hop-type"

                            self.operations = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations()
                            self.operations.parent = self
                            self._children_name_map["operations"] = "operations"
                            self._segment_path = lambda: "next-hop" + "[index='" + str(self.index) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop, ['index', 'type', 'protected_by'], name, value)


                        class NextHopType(Entity):
                            """
                            Next\-hop
                            
                            .. attribute:: if_index
                            
                            	The interface index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address of the nexthop
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 Address of the nexthop
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: mac_address
                            
                            	MAC address of the nexthop
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**mandatory**\: True
                            
                            .. attribute:: out_interface_name
                            
                            	Name of the outgoing interface
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.NextHopType, self).__init__()

                                self.yang_name = "next-hop-type"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('if_index', (YLeaf(YType.uint32, 'if-index'), ['int'])),
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                    ('out_interface_name', (YLeaf(YType.str, 'out-interface-name'), ['str'])),
                                ])
                                self.if_index = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.mac_address = None
                                self.out_interface_name = None
                                self._segment_path = lambda: "next-hop-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.NextHopType, ['if_index', 'ipv4_address', 'ipv6_address', 'mac_address', 'out_interface_name'], name, value)



                        class Operations(Entity):
                            """
                            The incoming label processing
                            
                            .. attribute:: preserve
                            
                            	preserve incoming label stack
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: swap
                            
                            	Push outgoing label stack
                            	**type**\:  :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap>`
                            
                            .. attribute:: push
                            
                            	Push outgoing label stack
                            	**type**\:  :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push>`
                            
                            .. attribute:: pop_and_forward
                            
                            	Pop the incoming label and forward
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations, self).__init__()

                                self.yang_name = "operations"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("swap", ("swap", MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap)), ("push", ("push", MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push))])
                                self._leafs = OrderedDict([
                                    ('preserve', (YLeaf(YType.empty, 'preserve'), ['Empty'])),
                                    ('pop_and_forward', (YLeaf(YType.empty, 'pop-and-forward'), ['Empty'])),
                                ])
                                self.preserve = None
                                self.pop_and_forward = None

                                self.swap = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap()
                                self.swap.parent = self
                                self._children_name_map["swap"] = "swap"

                                self.push = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push()
                                self.push.parent = self
                                self._children_name_map["push"] = "push"
                                self._segment_path = lambda: "operations"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations, ['preserve', 'pop_and_forward'], name, value)


                            class Swap(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap, self).__init__()

                                    self.yang_name = "swap"
                                    self.yang_parent_name = "operations"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap.Stack))])
                                    self._leafs = OrderedDict()

                                    self.stack = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._segment_path = lambda: "swap"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap, [], name, value)


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: list of int
                                    
                                    			**range:** 16..1048575
                                    
                                    		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "swap"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                        ])
                                        self.label_stack = []
                                        self._segment_path = lambda: "stack"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap.Stack, ['label_stack'], name, value)




                            class Push(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push, self).__init__()

                                    self.yang_name = "push"
                                    self.yang_parent_name = "operations"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push.Stack))])
                                    self._leafs = OrderedDict()

                                    self.stack = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._segment_path = lambda: "push"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push, [], name, value)


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: list of int
                                    
                                    			**range:** 16..1048575
                                    
                                    		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "push"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                        ])
                                        self.label_stack = []
                                        self._segment_path = lambda: "stack"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push.Stack, ['label_stack'], name, value)










    class MplsStaticState(Entity):
        """
        MPLS static operational data
        
        .. attribute:: label_switched_paths
        
        	MPLS Static Label Switched Paths
        	**type**\:  :py:class:`LabelSwitchedPaths <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ms'
        _revision = '2015-07-22'

        def __init__(self):
            super(MplsStatic.MplsStaticState, self).__init__()

            self.yang_name = "mpls-static-state"
            self.yang_parent_name = "mpls-static"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("label-switched-paths", ("label_switched_paths", MplsStatic.MplsStaticState.LabelSwitchedPaths))])
            self._leafs = OrderedDict()

            self.label_switched_paths = MplsStatic.MplsStaticState.LabelSwitchedPaths()
            self.label_switched_paths.parent = self
            self._children_name_map["label_switched_paths"] = "label-switched-paths"
            self._segment_path = lambda: "mpls-static-state"
            self._absolute_path = lambda: "common-mpls-static:mpls-static/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MplsStatic.MplsStaticState, [], name, value)


        class LabelSwitchedPaths(Entity):
            """
            MPLS Static Label Switched Paths
            
            .. attribute:: label_switched_path
            
            	MPLS LSPs list
            	**type**\: list of  		 :py:class:`LabelSwitchedPath <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ms'
            _revision = '2015-07-22'

            def __init__(self):
                super(MplsStatic.MplsStaticState.LabelSwitchedPaths, self).__init__()

                self.yang_name = "label-switched-paths"
                self.yang_parent_name = "mpls-static-state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("label-switched-path", ("label_switched_path", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath))])
                self._leafs = OrderedDict()

                self.label_switched_path = YList(self)
                self._segment_path = lambda: "label-switched-paths"
                self._absolute_path = lambda: "common-mpls-static:mpls-static/mpls-static-state/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths, [], name, value)


            class LabelSwitchedPath(Entity):
                """
                MPLS LSPs list
                
                .. attribute:: vrf_name  (key)
                
                	Name of the VRF
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: prefix  (key)
                
                	IP v4/v6 prefix
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                	**config**\: False
                
                .. attribute:: name
                
                	Name of the LSP
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: in_label_value
                
                	Value of the local label
                	**type**\: union of the below types:
                
                		**type**\: int
                
                			**range:** 16..1048575
                
                		**type**\:  :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                
                	**config**\: False
                
                .. attribute:: ingress_stats
                
                	ingress stats
                	**type**\:  :py:class:`IngressStats <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats>`
                
                	**config**\: False
                
                .. attribute:: egress_stats
                
                	egress stats
                	**type**\:  :py:class:`EgressStats <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats>`
                
                	**config**\: False
                
                .. attribute:: path
                
                	Fowarding path
                	**type**\:  :py:class:`Path <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ms'
                _revision = '2015-07-22'

                def __init__(self):
                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath, self).__init__()

                    self.yang_name = "label-switched-path"
                    self.yang_parent_name = "label-switched-paths"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name','prefix']
                    self._child_classes = OrderedDict([("ingress-stats", ("ingress_stats", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats)), ("egress-stats", ("egress_stats", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats)), ("path", ("path", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path))])
                    self._leafs = OrderedDict([
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str','str'])),
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('in_label_value', (YLeaf(YType.str, 'in-label-value'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                    ])
                    self.vrf_name = None
                    self.prefix = None
                    self.name = None
                    self.in_label_value = None

                    self.ingress_stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats()
                    self.ingress_stats.parent = self
                    self._children_name_map["ingress_stats"] = "ingress-stats"

                    self.egress_stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats()
                    self.egress_stats.parent = self
                    self._children_name_map["egress_stats"] = "egress-stats"

                    self.path = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path()
                    self.path.parent = self
                    self._children_name_map["path"] = "path"
                    self._segment_path = lambda: "label-switched-path" + "[vrf-name='" + str(self.vrf_name) + "']" + "[prefix='" + str(self.prefix) + "']"
                    self._absolute_path = lambda: "common-mpls-static:mpls-static/mpls-static-state/label-switched-paths/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath, ['vrf_name', 'prefix', 'name', 'in_label_value'], name, value)


                class IngressStats(Entity):
                    """
                    ingress stats
                    
                    .. attribute:: stats
                    
                    	Statistics
                    	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats.Stats>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats, self).__init__()

                        self.yang_name = "ingress-stats"
                        self.yang_parent_name = "label-switched-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("stats", ("stats", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats.Stats))])
                        self._leafs = OrderedDict()

                        self.stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats.Stats()
                        self.stats.parent = self
                        self._children_name_map["stats"] = "stats"
                        self._segment_path = lambda: "ingress-stats"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats, [], name, value)


                    class Stats(Entity):
                        """
                        Statistics
                        
                        .. attribute:: packets
                        
                        	stats for packet count
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: bytes
                        
                        	stats for byte count
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: dropped_packets
                        
                        	stats for dropped\-packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: dropped_bytes
                        
                        	stats for dropped\-bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats.Stats, self).__init__()

                            self.yang_name = "stats"
                            self.yang_parent_name = "ingress-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                ('dropped_bytes', (YLeaf(YType.uint64, 'dropped-bytes'), ['int'])),
                            ])
                            self.packets = None
                            self.bytes = None
                            self.dropped_packets = None
                            self.dropped_bytes = None
                            self._segment_path = lambda: "stats"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats.Stats, ['packets', 'bytes', 'dropped_packets', 'dropped_bytes'], name, value)




                class EgressStats(Entity):
                    """
                    egress stats
                    
                    .. attribute:: stats
                    
                    	Statistics
                    	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats.Stats>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats, self).__init__()

                        self.yang_name = "egress-stats"
                        self.yang_parent_name = "label-switched-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("stats", ("stats", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats.Stats))])
                        self._leafs = OrderedDict()

                        self.stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats.Stats()
                        self.stats.parent = self
                        self._children_name_map["stats"] = "stats"
                        self._segment_path = lambda: "egress-stats"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats, [], name, value)


                    class Stats(Entity):
                        """
                        Statistics
                        
                        .. attribute:: packets
                        
                        	stats for packet count
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: bytes
                        
                        	stats for byte count
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: dropped_packets
                        
                        	stats for dropped\-packets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: dropped_bytes
                        
                        	stats for dropped\-bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats.Stats, self).__init__()

                            self.yang_name = "stats"
                            self.yang_parent_name = "egress-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                ('dropped_bytes', (YLeaf(YType.uint64, 'dropped-bytes'), ['int'])),
                            ])
                            self.packets = None
                            self.bytes = None
                            self.dropped_packets = None
                            self.dropped_bytes = None
                            self._segment_path = lambda: "stats"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats.Stats, ['packets', 'bytes', 'dropped_packets', 'dropped_bytes'], name, value)




                class Path(Entity):
                    """
                    Fowarding path
                    
                    .. attribute:: operations
                    
                    	The incoming label processing
                    	**type**\:  :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations>`
                    
                    	**config**\: False
                    
                    .. attribute:: auto_protect
                    
                    	Enables automatic protection if true
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    	**default value**\: false
                    
                    .. attribute:: next_hop
                    
                    	next\-hops list
                    	**type**\: list of  		 :py:class:`NextHop <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path, self).__init__()

                        self.yang_name = "path"
                        self.yang_parent_name = "label-switched-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("operations", ("operations", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations)), ("next-hop", ("next_hop", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop))])
                        self._leafs = OrderedDict([
                            ('auto_protect', (YLeaf(YType.boolean, 'auto-protect'), ['bool'])),
                        ])
                        self.auto_protect = None

                        self.operations = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations()
                        self.operations.parent = self
                        self._children_name_map["operations"] = "operations"

                        self.next_hop = YList(self)
                        self._segment_path = lambda: "path"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path, ['auto_protect'], name, value)


                    class Operations(Entity):
                        """
                        The incoming label processing
                        
                        .. attribute:: preserve
                        
                        	preserve incoming label stack
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        	**config**\: False
                        
                        .. attribute:: swap
                        
                        	Push outgoing label stack
                        	**type**\:  :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap>`
                        
                        	**config**\: False
                        
                        .. attribute:: push
                        
                        	Push outgoing label stack
                        	**type**\:  :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push>`
                        
                        	**config**\: False
                        
                        .. attribute:: pop_and_forward
                        
                        	Pop the incoming label and forward
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations, self).__init__()

                            self.yang_name = "operations"
                            self.yang_parent_name = "path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("swap", ("swap", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap)), ("push", ("push", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push))])
                            self._leafs = OrderedDict([
                                ('preserve', (YLeaf(YType.empty, 'preserve'), ['Empty'])),
                                ('pop_and_forward', (YLeaf(YType.empty, 'pop-and-forward'), ['Empty'])),
                            ])
                            self.preserve = None
                            self.pop_and_forward = None

                            self.swap = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap()
                            self.swap.parent = self
                            self._children_name_map["swap"] = "swap"

                            self.push = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push()
                            self.push.parent = self
                            self._children_name_map["push"] = "push"
                            self._segment_path = lambda: "operations"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations, ['preserve', 'pop_and_forward'], name, value)


                        class Swap(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap.Stack>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap, self).__init__()

                                self.yang_name = "swap"
                                self.yang_parent_name = "operations"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap.Stack))])
                                self._leafs = OrderedDict()

                                self.stack = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._segment_path = lambda: "swap"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap, [], name, value)


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: union of the below types:
                                
                                		**type**\: list of int
                                
                                			**range:** 16..1048575
                                
                                		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "swap"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                    ])
                                    self.label_stack = []
                                    self._segment_path = lambda: "stack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap.Stack, ['label_stack'], name, value)




                        class Push(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push.Stack>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push, self).__init__()

                                self.yang_name = "push"
                                self.yang_parent_name = "operations"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push.Stack))])
                                self._leafs = OrderedDict()

                                self.stack = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._segment_path = lambda: "push"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push, [], name, value)


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: union of the below types:
                                
                                		**type**\: list of int
                                
                                			**range:** 16..1048575
                                
                                		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "push"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                    ])
                                    self.label_stack = []
                                    self._segment_path = lambda: "stack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push.Stack, ['label_stack'], name, value)





                    class NextHop(Entity):
                        """
                        next\-hops list
                        
                        .. attribute:: index  (key)
                        
                        	Index of the nexthop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        	**config**\: False
                        
                        .. attribute:: type
                        
                        	The forwarding path's hoptype
                        	**type**\:  :py:class:`Hoptype <ydk.models.cisco_ios_xe.common_mpls_static.Hoptype>`
                        
                        	**mandatory**\: True
                        
                        	**config**\: False
                        
                        .. attribute:: protected_by
                        
                        	Index of the nexthop that protects this nexthop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: next_hop_type
                        
                        	Next\-hop
                        	**type**\:  :py:class:`NextHopType <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NextHopType>`
                        
                        	**config**\: False
                        
                        .. attribute:: operations
                        
                        	The incoming label processing
                        	**type**\:  :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations>`
                        
                        	**config**\: False
                        
                        .. attribute:: origin
                        
                        	The origin of this nexthop
                        	**type**\:  :py:class:`NexthopResolutionType <ydk.models.cisco_ios_xe.common_mpls_static.NexthopResolutionType>`
                        
                        	**config**\: False
                        
                        .. attribute:: nexthop_stats
                        
                        	lsp stats
                        	**type**\:  :py:class:`NexthopStats <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['index']
                            self._child_classes = OrderedDict([("next-hop-type", ("next_hop_type", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NextHopType)), ("operations", ("operations", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations)), ("nexthop-stats", ("nexthop_stats", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats))])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xe.common_mpls_static', 'Hoptype', '')])),
                                ('protected_by', (YLeaf(YType.uint32, 'protected-by'), ['int'])),
                                ('origin', (YLeaf(YType.identityref, 'origin'), [('ydk.models.cisco_ios_xe.common_mpls_static', 'NexthopResolutionType')])),
                            ])
                            self.index = None
                            self.type = None
                            self.protected_by = None
                            self.origin = None

                            self.next_hop_type = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NextHopType()
                            self.next_hop_type.parent = self
                            self._children_name_map["next_hop_type"] = "next-hop-type"

                            self.operations = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations()
                            self.operations.parent = self
                            self._children_name_map["operations"] = "operations"

                            self.nexthop_stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats()
                            self.nexthop_stats.parent = self
                            self._children_name_map["nexthop_stats"] = "nexthop-stats"
                            self._segment_path = lambda: "next-hop" + "[index='" + str(self.index) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop, ['index', 'type', 'protected_by', 'origin'], name, value)


                        class NextHopType(Entity):
                            """
                            Next\-hop
                            
                            .. attribute:: if_index
                            
                            	The interface index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            	**config**\: False
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address of the nexthop
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            	**config**\: False
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 Address of the nexthop
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            	**config**\: False
                            
                            .. attribute:: mac_address
                            
                            	MAC address of the nexthop
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**mandatory**\: True
                            
                            	**config**\: False
                            
                            .. attribute:: out_interface_name
                            
                            	Name of the outgoing interface
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NextHopType, self).__init__()

                                self.yang_name = "next-hop-type"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('if_index', (YLeaf(YType.uint32, 'if-index'), ['int'])),
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                    ('out_interface_name', (YLeaf(YType.str, 'out-interface-name'), ['str'])),
                                ])
                                self.if_index = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.mac_address = None
                                self.out_interface_name = None
                                self._segment_path = lambda: "next-hop-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NextHopType, ['if_index', 'ipv4_address', 'ipv6_address', 'mac_address', 'out_interface_name'], name, value)



                        class Operations(Entity):
                            """
                            The incoming label processing
                            
                            .. attribute:: preserve
                            
                            	preserve incoming label stack
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            	**config**\: False
                            
                            .. attribute:: swap
                            
                            	Push outgoing label stack
                            	**type**\:  :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap>`
                            
                            	**config**\: False
                            
                            .. attribute:: push
                            
                            	Push outgoing label stack
                            	**type**\:  :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push>`
                            
                            	**config**\: False
                            
                            .. attribute:: pop_and_forward
                            
                            	Pop the incoming label and forward
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations, self).__init__()

                                self.yang_name = "operations"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("swap", ("swap", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap)), ("push", ("push", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push))])
                                self._leafs = OrderedDict([
                                    ('preserve', (YLeaf(YType.empty, 'preserve'), ['Empty'])),
                                    ('pop_and_forward', (YLeaf(YType.empty, 'pop-and-forward'), ['Empty'])),
                                ])
                                self.preserve = None
                                self.pop_and_forward = None

                                self.swap = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap()
                                self.swap.parent = self
                                self._children_name_map["swap"] = "swap"

                                self.push = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push()
                                self.push.parent = self
                                self._children_name_map["push"] = "push"
                                self._segment_path = lambda: "operations"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations, ['preserve', 'pop_and_forward'], name, value)


                            class Swap(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap.Stack>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap, self).__init__()

                                    self.yang_name = "swap"
                                    self.yang_parent_name = "operations"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap.Stack))])
                                    self._leafs = OrderedDict()

                                    self.stack = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._segment_path = lambda: "swap"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap, [], name, value)


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: list of int
                                    
                                    			**range:** 16..1048575
                                    
                                    		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "swap"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                        ])
                                        self.label_stack = []
                                        self._segment_path = lambda: "stack"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap.Stack, ['label_stack'], name, value)




                            class Push(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:  :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push.Stack>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push, self).__init__()

                                    self.yang_name = "push"
                                    self.yang_parent_name = "operations"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("stack", ("stack", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push.Stack))])
                                    self._leafs = OrderedDict()

                                    self.stack = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._segment_path = lambda: "push"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push, [], name, value)


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: list of int
                                    
                                    			**range:** 16..1048575
                                    
                                    		**type**\: list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "push"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('label_stack', (YLeafList(YType.str, 'label-stack'), ['int',('ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabel', '')])),
                                        ])
                                        self.label_stack = []
                                        self._segment_path = lambda: "stack"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push.Stack, ['label_stack'], name, value)





                        class NexthopStats(Entity):
                            """
                            lsp stats
                            
                            .. attribute:: stats
                            
                            	Statistics
                            	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats.Stats>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats, self).__init__()

                                self.yang_name = "nexthop-stats"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("stats", ("stats", MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats.Stats))])
                                self._leafs = OrderedDict()

                                self.stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats.Stats()
                                self.stats.parent = self
                                self._children_name_map["stats"] = "stats"
                                self._segment_path = lambda: "nexthop-stats"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats, [], name, value)


                            class Stats(Entity):
                                """
                                Statistics
                                
                                .. attribute:: packets
                                
                                	stats for packet count
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: bytes
                                
                                	stats for byte count
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: dropped_packets
                                
                                	stats for dropped\-packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: dropped_bytes
                                
                                	stats for dropped\-bytes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats.Stats, self).__init__()

                                    self.yang_name = "stats"
                                    self.yang_parent_name = "nexthop-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                        ('dropped_bytes', (YLeaf(YType.uint64, 'dropped-bytes'), ['int'])),
                                    ])
                                    self.packets = None
                                    self.bytes = None
                                    self.dropped_packets = None
                                    self.dropped_bytes = None
                                    self._segment_path = lambda: "stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats.Stats, ['packets', 'bytes', 'dropped_packets', 'dropped_bytes'], name, value)








    def clone_ptr(self):
        self._top_entity = MplsStatic()
        return self._top_entity



class LspIPv4(LspType):
    """
    The LSP is for an IPv4 prefix
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:common-mpls-static", pref="common-mpls-static", tag="common-mpls-static:lsp-IPv4"):
        super(LspIPv4, self).__init__(ns, pref, tag)



class LspIPv6(LspType):
    """
    The LSP is for an IPv6 prefix
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:common-mpls-static", pref="common-mpls-static", tag="common-mpls-static:lsp-IPv6"):
        super(LspIPv6, self).__init__(ns, pref, tag)



class LspVrf(LspType):
    """
    The LSP is per VRF
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:common-mpls-static", pref="common-mpls-static", tag="common-mpls-static:lsp-vrf"):
        super(LspVrf, self).__init__(ns, pref, tag)



class Lsp(LspType):
    """
    The LSP is cross\-connect
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:common-mpls-static", pref="common-mpls-static", tag="common-mpls-static:lsp"):
        super(Lsp, self).__init__(ns, pref, tag)



class StaticNexthop(NexthopResolutionType):
    """
    The nexthop resolved from statically configured route
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:common-mpls-static", pref="common-mpls-static", tag="common-mpls-static:static-nexthop"):
        super(StaticNexthop, self).__init__(ns, pref, tag)



class BgpRouteNexthop(NexthopResolutionType):
    """
    The nexthop resolved from a BGP route
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:common-mpls-static", pref="common-mpls-static", tag="common-mpls-static:bgp-route-nexthop"):
        super(BgpRouteNexthop, self).__init__(ns, pref, tag)



class OspfRouteNexthop(NexthopResolutionType):
    """
    The nexthop resolved from an OSPF route
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:common-mpls-static", pref="common-mpls-static", tag="common-mpls-static:ospf-route-nexthop"):
        super(OspfRouteNexthop, self).__init__(ns, pref, tag)



class IsisRouteNexthop(NexthopResolutionType):
    """
    The nexthop resolved from an ISIS route
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:common-mpls-static", pref="common-mpls-static", tag="common-mpls-static:isis-route-nexthop"):
        super(IsisRouteNexthop, self).__init__(ns, pref, tag)



