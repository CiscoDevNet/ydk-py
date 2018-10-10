""" Cisco_IOS_XR_ipv4_io_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-io package operational data.

This module contains definitions
for the following management objects\:
  ipv4\-network\: IPv4 network operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ipv4MaOperConfig(Enum):
    """
    Ipv4MaOperConfig (Enum Class)

    ipv4 client type

    .. data:: ipv4_ma_oper_client_none = 0

    	ipv4 ma oper client none

    .. data:: ipv4_ma_oper_non_oc_client = 1

    	ipv4 ma oper non oc client

    .. data:: ipv4_ma_oper_oc_client = 2

    	ipv4 ma oper oc client

    """

    ipv4_ma_oper_client_none = Enum.YLeaf(0, "ipv4-ma-oper-client-none")

    ipv4_ma_oper_non_oc_client = Enum.YLeaf(1, "ipv4-ma-oper-non-oc-client")

    ipv4_ma_oper_oc_client = Enum.YLeaf(2, "ipv4-ma-oper-oc-client")


class Ipv4MaOperLineState(Enum):
    """
    Ipv4MaOperLineState (Enum Class)

    Interface line states

    .. data:: unknown = 0

    	Interface state is unknown

    .. data:: shutdown = 1

    	Interface has been shutdown

    .. data:: down = 2

    	Interface state is down

    .. data:: up = 3

    	Interface state is up

    """

    unknown = Enum.YLeaf(0, "unknown")

    shutdown = Enum.YLeaf(1, "shutdown")

    down = Enum.YLeaf(2, "down")

    up = Enum.YLeaf(3, "up")


class RpfMode(Enum):
    """
    RpfMode (Enum Class)

    Interface line states

    .. data:: strict = 0

    	Strict RPF

    .. data:: loose = 1

    	Loose RPF

    """

    strict = Enum.YLeaf(0, "strict")

    loose = Enum.YLeaf(1, "loose")



class Ipv4Network(Entity):
    """
    IPv4 network operational data
    
    .. attribute:: nodes
    
    	Node\-specific IPv4 network operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes>`
    
    .. attribute:: interfaces
    
    	IPv4 network operational interface data
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces>`
    
    

    """

    _prefix = 'ipv4-io-oper'
    _revision = '2015-10-20'

    def __init__(self):
        super(Ipv4Network, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv4-network"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-io-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Ipv4Network.Nodes)), ("Cisco-IOS-XR-ipv4-ma-oper:interfaces", ("interfaces", Ipv4Network.Interfaces))])
        self._leafs = OrderedDict()

        self.nodes = Ipv4Network.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"

        self.interfaces = Ipv4Network.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "Cisco-IOS-XR-ipv4-ma-oper:interfaces"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-io-oper:ipv4-network"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv4Network, [], name, value)


    class Nodes(Entity):
        """
        Node\-specific IPv4 network operational data
        
        .. attribute:: node
        
        	IPv4 network operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node>`
        
        

        """

        _prefix = 'ipv4-io-oper'
        _revision = '2015-10-20'

        def __init__(self):
            super(Ipv4Network.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ipv4-network"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Ipv4Network.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-io-oper:ipv4-network/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Network.Nodes, [], name, value)


        class Node(Entity):
            """
            IPv4 network operational data for a particular
            node
            
            .. attribute:: node_name  (key)
            
            	The node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interface_data
            
            	IPv4 network operational interface data
            	**type**\:  :py:class:`InterfaceData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData>`
            
            .. attribute:: statistics
            
            	Statistical IPv4 network operational data for a node
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ipv4-io-oper'
            _revision = '2015-10-20'

            def __init__(self):
                super(Ipv4Network.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("interface-data", ("interface_data", Ipv4Network.Nodes.Node.InterfaceData)), ("statistics", ("statistics", Ipv4Network.Nodes.Node.Statistics))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.interface_data = Ipv4Network.Nodes.Node.InterfaceData()
                self.interface_data.parent = self
                self._children_name_map["interface_data"] = "interface-data"

                self.statistics = Ipv4Network.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-io-oper:ipv4-network/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Network.Nodes.Node, ['node_name'], name, value)


            class InterfaceData(Entity):
                """
                IPv4 network operational interface data
                
                .. attribute:: vrfs
                
                	VRF specific IPv4 network operational interface data
                	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs>`
                
                .. attribute:: summary
                
                	Summary of IPv4 network operational interface data on a node
                	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Summary>`
                
                

                """

                _prefix = 'ipv4-io-oper'
                _revision = '2015-10-20'

                def __init__(self):
                    super(Ipv4Network.Nodes.Node.InterfaceData, self).__init__()

                    self.yang_name = "interface-data"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("vrfs", ("vrfs", Ipv4Network.Nodes.Node.InterfaceData.Vrfs)), ("summary", ("summary", Ipv4Network.Nodes.Node.InterfaceData.Summary))])
                    self._leafs = OrderedDict()

                    self.vrfs = Ipv4Network.Nodes.Node.InterfaceData.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"

                    self.summary = Ipv4Network.Nodes.Node.InterfaceData.Summary()
                    self.summary.parent = self
                    self._children_name_map["summary"] = "summary"
                    self._segment_path = lambda: "interface-data"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData, [], name, value)


                class Vrfs(Entity):
                    """
                    VRF specific IPv4 network operational
                    interface data
                    
                    .. attribute:: vrf
                    
                    	VRF name of an interface belong to
                    	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv4-io-oper'
                    _revision = '2015-10-20'

                    def __init__(self):
                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs, self).__init__()

                        self.yang_name = "vrfs"
                        self.yang_parent_name = "interface-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("vrf", ("vrf", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf))])
                        self._leafs = OrderedDict()

                        self.vrf = YList(self)
                        self._segment_path = lambda: "vrfs"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs, [], name, value)


                    class Vrf(Entity):
                        """
                        VRF name of an interface belong to
                        
                        .. attribute:: vrf_name  (key)
                        
                        	The VRF name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: briefs
                        
                        	Brief interface IPv4 network operational data for a node
                        	**type**\:  :py:class:`Briefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs>`
                        
                        .. attribute:: details
                        
                        	Detail interface IPv4 network operational data for a node
                        	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details>`
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "vrfs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['vrf_name']
                            self._child_classes = OrderedDict([("briefs", ("briefs", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs)), ("details", ("details", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details))])
                            self._leafs = OrderedDict([
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ])
                            self.vrf_name = None

                            self.briefs = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs()
                            self.briefs.parent = self
                            self._children_name_map["briefs"] = "briefs"

                            self.details = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details()
                            self.details.parent = self
                            self._children_name_map["details"] = "details"
                            self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf, ['vrf_name'], name, value)


                        class Briefs(Entity):
                            """
                            Brief interface IPv4 network operational
                            data for a node
                            
                            .. attribute:: brief
                            
                            	Brief interface IPv4 network operational data for an interface
                            	**type**\: list of  		 :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief>`
                            
                            

                            """

                            _prefix = 'ipv4-io-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs, self).__init__()

                                self.yang_name = "briefs"
                                self.yang_parent_name = "vrf"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("brief", ("brief", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief))])
                                self._leafs = OrderedDict()

                                self.brief = YList(self)
                                self._segment_path = lambda: "briefs"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs, [], name, value)


                            class Brief(Entity):
                                """
                                Brief interface IPv4 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  (key)
                                
                                	The name of the interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                .. attribute:: primary_address
                                
                                	Primary address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: vrf_id
                                
                                	VRF ID of the interface
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: vrf_name
                                
                                	VRF name of the interface
                                	**type**\: str
                                
                                .. attribute:: line_state
                                
                                	Line state of the interface
                                	**type**\:  :py:class:`Ipv4MaOperLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4MaOperLineState>`
                                
                                

                                """

                                _prefix = 'ipv4-io-oper'
                                _revision = '2015-10-20'

                                def __init__(self):
                                    super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief, self).__init__()

                                    self.yang_name = "brief"
                                    self.yang_parent_name = "briefs"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('primary_address', (YLeaf(YType.str, 'primary-address'), ['str'])),
                                        ('vrf_id', (YLeaf(YType.uint32, 'vrf-id'), ['int'])),
                                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                        ('line_state', (YLeaf(YType.enumeration, 'line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4MaOperLineState', '')])),
                                    ])
                                    self.interface_name = None
                                    self.primary_address = None
                                    self.vrf_id = None
                                    self.vrf_name = None
                                    self.line_state = None
                                    self._segment_path = lambda: "brief" + "[interface-name='" + str(self.interface_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief, ['interface_name', u'primary_address', u'vrf_id', u'vrf_name', u'line_state'], name, value)


                        class Details(Entity):
                            """
                            Detail interface IPv4 network operational
                            data for a node
                            
                            .. attribute:: detail
                            
                            	Detail interface IPv4 network operational data for an interface
                            	**type**\: list of  		 :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail>`
                            
                            

                            """

                            _prefix = 'ipv4-io-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details, self).__init__()

                                self.yang_name = "details"
                                self.yang_parent_name = "vrf"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("detail", ("detail", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail))])
                                self._leafs = OrderedDict()

                                self.detail = YList(self)
                                self._segment_path = lambda: "details"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details, [], name, value)


                            class Detail(Entity):
                                """
                                Detail interface IPv4 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  (key)
                                
                                	The name of the interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                .. attribute:: acl
                                
                                	ACLs configured on the interface
                                	**type**\:  :py:class:`Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl>`
                                
                                .. attribute:: multi_acl
                                
                                	Multi ACLs configured on the interface
                                	**type**\:  :py:class:`MultiAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl>`
                                
                                .. attribute:: helper_address
                                
                                	Helper Addresses configured on the interface
                                	**type**\:  :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress>`
                                
                                .. attribute:: rpf
                                
                                	RPF config on the interface
                                	**type**\:  :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf>`
                                
                                .. attribute:: bgp_pa
                                
                                	BGP PA config on the interface
                                	**type**\:  :py:class:`BgpPa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa>`
                                
                                .. attribute:: pub_utime
                                
                                	Address Publish Time
                                	**type**\:  :py:class:`PubUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.PubUtime>`
                                
                                .. attribute:: idb_utime
                                
                                	IDB Create Time
                                	**type**\:  :py:class:`IdbUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime>`
                                
                                .. attribute:: caps_utime
                                
                                	CAPS Add Time
                                	**type**\:  :py:class:`CapsUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime>`
                                
                                .. attribute:: fwd_en_utime
                                
                                	FWD ENABLE Time
                                	**type**\:  :py:class:`FwdEnUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime>`
                                
                                .. attribute:: fwd_dis_utime
                                
                                	FWD DISABLE Time
                                	**type**\:  :py:class:`FwdDisUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime>`
                                
                                .. attribute:: primary_address
                                
                                	Primary address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: vrf_id
                                
                                	VRF ID of the interface
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: line_state
                                
                                	Line state of the interface
                                	**type**\:  :py:class:`Ipv4MaOperLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4MaOperLineState>`
                                
                                .. attribute:: prefix_length
                                
                                	Prefix length of primary address
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: route_tag
                                
                                	Route tag associated with the primary address (0 = no tag)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: mtu
                                
                                	IP MTU of the interface
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: unreachable
                                
                                	Are ICMP unreachables sent on the interface?
                                	**type**\: bool
                                
                                .. attribute:: redirect
                                
                                	Are ICMP redirects sent on the interface?
                                	**type**\: bool
                                
                                .. attribute:: direct_broadcast
                                
                                	Are direct broadcasts sent on the interface?
                                	**type**\: bool
                                
                                .. attribute:: mask_reply
                                
                                	Are mask replies sent on the interface?
                                	**type**\: bool
                                
                                .. attribute:: rg_id_exists
                                
                                	Does ICCP RG ID exist on the interface?
                                	**type**\: bool
                                
                                .. attribute:: mlacp_active
                                
                                	Is mLACP state Active (valid if RG ID exists)
                                	**type**\: bool
                                
                                .. attribute:: unnumbered_interface_name
                                
                                	Name of referenced interface (valid if unnumbered)
                                	**type**\: str
                                
                                .. attribute:: next_unnumbered_interface_name
                                
                                	Name of interface which is also unnum to         same interface where this intf is unnumbered
                                	**type**\: str
                                
                                .. attribute:: proxy_arp_disabled
                                
                                	Is Proxy ARP disabled on the interface?
                                	**type**\: bool
                                
                                .. attribute:: flow_tag_src
                                
                                	Is BGP Flow Tag Source is enable
                                	**type**\: bool
                                
                                .. attribute:: flow_tag_dst
                                
                                	Is BGP Flow Tag Destination is enable
                                	**type**\: bool
                                
                                .. attribute:: config_flags
                                
                                	IDB configuration flags
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: oper_flags
                                
                                	IDB operational flags
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: arm_flags
                                
                                	IP ARM operation flags
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: state_recvd_frm_im
                                
                                	state as recieved                                from IM
                                	**type**\:  :py:class:`Ipv4MaOperLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4MaOperLineState>`
                                
                                .. attribute:: cflct_address
                                
                                	Conflicated ipv4 address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: client_type
                                
                                	Client type for IDB
                                	**type**\:  :py:class:`Ipv4MaOperConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4MaOperConfig>`
                                
                                .. attribute:: is_or_event
                                
                                	Is OR event for IDB
                                	**type**\: bool
                                
                                .. attribute:: or_im_state
                                
                                	OR IM state type
                                	**type**\:  :py:class:`Ipv4MaOperLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4MaOperLineState>`
                                
                                .. attribute:: idb_pointer
                                
                                	idb pointer value
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: multicast_group
                                
                                	Multicast groups joined on the interface
                                	**type**\: list of  		 :py:class:`MulticastGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup>`
                                
                                .. attribute:: secondary_address
                                
                                	Secondary addresses on the interface
                                	**type**\: list of  		 :py:class:`SecondaryAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.SecondaryAddress>`
                                
                                

                                """

                                _prefix = 'ipv4-io-oper'
                                _revision = '2015-10-20'

                                def __init__(self):
                                    super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "details"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface_name']
                                    self._child_classes = OrderedDict([("acl", ("acl", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl)), ("multi-acl", ("multi_acl", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl)), ("helper-address", ("helper_address", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress)), ("rpf", ("rpf", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf)), ("bgp-pa", ("bgp_pa", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa)), ("pub-utime", ("pub_utime", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.PubUtime)), ("idb-utime", ("idb_utime", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime)), ("caps-utime", ("caps_utime", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime)), ("fwd-en-utime", ("fwd_en_utime", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime)), ("fwd-dis-utime", ("fwd_dis_utime", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime)), ("multicast-group", ("multicast_group", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup)), ("secondary-address", ("secondary_address", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.SecondaryAddress))])
                                    self._leafs = OrderedDict([
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('primary_address', (YLeaf(YType.str, 'primary-address'), ['str'])),
                                        ('vrf_id', (YLeaf(YType.uint32, 'vrf-id'), ['int'])),
                                        ('line_state', (YLeaf(YType.enumeration, 'line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4MaOperLineState', '')])),
                                        ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                        ('route_tag', (YLeaf(YType.uint32, 'route-tag'), ['int'])),
                                        ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                                        ('unreachable', (YLeaf(YType.boolean, 'unreachable'), ['bool'])),
                                        ('redirect', (YLeaf(YType.boolean, 'redirect'), ['bool'])),
                                        ('direct_broadcast', (YLeaf(YType.boolean, 'direct-broadcast'), ['bool'])),
                                        ('mask_reply', (YLeaf(YType.boolean, 'mask-reply'), ['bool'])),
                                        ('rg_id_exists', (YLeaf(YType.boolean, 'rg-id-exists'), ['bool'])),
                                        ('mlacp_active', (YLeaf(YType.boolean, 'mlacp-active'), ['bool'])),
                                        ('unnumbered_interface_name', (YLeaf(YType.str, 'unnumbered-interface-name'), ['str'])),
                                        ('next_unnumbered_interface_name', (YLeaf(YType.str, 'next-unnumbered-interface-name'), ['str'])),
                                        ('proxy_arp_disabled', (YLeaf(YType.boolean, 'proxy-arp-disabled'), ['bool'])),
                                        ('flow_tag_src', (YLeaf(YType.boolean, 'flow-tag-src'), ['bool'])),
                                        ('flow_tag_dst', (YLeaf(YType.boolean, 'flow-tag-dst'), ['bool'])),
                                        ('config_flags', (YLeaf(YType.uint16, 'config-flags'), ['int'])),
                                        ('oper_flags', (YLeaf(YType.uint64, 'oper-flags'), ['int'])),
                                        ('arm_flags', (YLeaf(YType.uint16, 'arm-flags'), ['int'])),
                                        ('state_recvd_frm_im', (YLeaf(YType.enumeration, 'state-recvd-frm-im'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4MaOperLineState', '')])),
                                        ('cflct_address', (YLeaf(YType.str, 'cflct-address'), ['str'])),
                                        ('client_type', (YLeaf(YType.enumeration, 'client-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4MaOperConfig', '')])),
                                        ('is_or_event', (YLeaf(YType.boolean, 'is-or-event'), ['bool'])),
                                        ('or_im_state', (YLeaf(YType.enumeration, 'or-im-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4MaOperLineState', '')])),
                                        ('idb_pointer', (YLeaf(YType.uint64, 'idb-pointer'), ['int'])),
                                    ])
                                    self.interface_name = None
                                    self.primary_address = None
                                    self.vrf_id = None
                                    self.line_state = None
                                    self.prefix_length = None
                                    self.route_tag = None
                                    self.mtu = None
                                    self.unreachable = None
                                    self.redirect = None
                                    self.direct_broadcast = None
                                    self.mask_reply = None
                                    self.rg_id_exists = None
                                    self.mlacp_active = None
                                    self.unnumbered_interface_name = None
                                    self.next_unnumbered_interface_name = None
                                    self.proxy_arp_disabled = None
                                    self.flow_tag_src = None
                                    self.flow_tag_dst = None
                                    self.config_flags = None
                                    self.oper_flags = None
                                    self.arm_flags = None
                                    self.state_recvd_frm_im = None
                                    self.cflct_address = None
                                    self.client_type = None
                                    self.is_or_event = None
                                    self.or_im_state = None
                                    self.idb_pointer = None

                                    self.acl = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl()
                                    self.acl.parent = self
                                    self._children_name_map["acl"] = "acl"

                                    self.multi_acl = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl()
                                    self.multi_acl.parent = self
                                    self._children_name_map["multi_acl"] = "multi-acl"

                                    self.helper_address = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress()
                                    self.helper_address.parent = self
                                    self._children_name_map["helper_address"] = "helper-address"

                                    self.rpf = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf()
                                    self.rpf.parent = self
                                    self._children_name_map["rpf"] = "rpf"

                                    self.bgp_pa = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa()
                                    self.bgp_pa.parent = self
                                    self._children_name_map["bgp_pa"] = "bgp-pa"

                                    self.pub_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.PubUtime()
                                    self.pub_utime.parent = self
                                    self._children_name_map["pub_utime"] = "pub-utime"

                                    self.idb_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime()
                                    self.idb_utime.parent = self
                                    self._children_name_map["idb_utime"] = "idb-utime"

                                    self.caps_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime()
                                    self.caps_utime.parent = self
                                    self._children_name_map["caps_utime"] = "caps-utime"

                                    self.fwd_en_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime()
                                    self.fwd_en_utime.parent = self
                                    self._children_name_map["fwd_en_utime"] = "fwd-en-utime"

                                    self.fwd_dis_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime()
                                    self.fwd_dis_utime.parent = self
                                    self._children_name_map["fwd_dis_utime"] = "fwd-dis-utime"

                                    self.multicast_group = YList(self)
                                    self.secondary_address = YList(self)
                                    self._segment_path = lambda: "detail" + "[interface-name='" + str(self.interface_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail, ['interface_name', u'primary_address', u'vrf_id', u'line_state', u'prefix_length', u'route_tag', u'mtu', u'unreachable', u'redirect', u'direct_broadcast', u'mask_reply', u'rg_id_exists', u'mlacp_active', u'unnumbered_interface_name', u'next_unnumbered_interface_name', u'proxy_arp_disabled', u'flow_tag_src', u'flow_tag_dst', u'config_flags', u'oper_flags', u'arm_flags', u'state_recvd_frm_im', u'cflct_address', u'client_type', u'is_or_event', u'or_im_state', u'idb_pointer'], name, value)


                                class Acl(Entity):
                                    """
                                    ACLs configured on the interface
                                    
                                    .. attribute:: inbound
                                    
                                    	ACL applied to incoming packets
                                    	**type**\: str
                                    
                                    .. attribute:: outbound
                                    
                                    	ACL applied to outgoing packets
                                    	**type**\: str
                                    
                                    .. attribute:: common_in_bound
                                    
                                    	Common ACL applied to incoming packets
                                    	**type**\: str
                                    
                                    .. attribute:: common_out_bound
                                    
                                    	Common ACL applied to outgoing packets
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl, self).__init__()

                                        self.yang_name = "acl"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('inbound', (YLeaf(YType.str, 'inbound'), ['str'])),
                                            ('outbound', (YLeaf(YType.str, 'outbound'), ['str'])),
                                            ('common_in_bound', (YLeaf(YType.str, 'common-in-bound'), ['str'])),
                                            ('common_out_bound', (YLeaf(YType.str, 'common-out-bound'), ['str'])),
                                        ])
                                        self.inbound = None
                                        self.outbound = None
                                        self.common_in_bound = None
                                        self.common_out_bound = None
                                        self._segment_path = lambda: "acl"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl, [u'inbound', u'outbound', u'common_in_bound', u'common_out_bound'], name, value)


                                class MultiAcl(Entity):
                                    """
                                    Multi ACLs configured on the interface
                                    
                                    .. attribute:: inbound
                                    
                                    	Inbound ACLs
                                    	**type**\: list of  		 :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Inbound>`
                                    
                                    .. attribute:: outbound
                                    
                                    	Outbound ACLs
                                    	**type**\: list of  		 :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Outbound>`
                                    
                                    .. attribute:: common
                                    
                                    	Common ACLs
                                    	**type**\: list of  		 :py:class:`Common <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Common>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl, self).__init__()

                                        self.yang_name = "multi-acl"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("inbound", ("inbound", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Inbound)), ("outbound", ("outbound", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Outbound)), ("common", ("common", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Common))])
                                        self._leafs = OrderedDict()

                                        self.inbound = YList(self)
                                        self.outbound = YList(self)
                                        self.common = YList(self)
                                        self._segment_path = lambda: "multi-acl"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl, [], name, value)


                                    class Inbound(Entity):
                                        """
                                        Inbound ACLs
                                        
                                        .. attribute:: entry
                                        
                                        	
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-io-oper'
                                        _revision = '2015-10-20'

                                        def __init__(self):
                                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Inbound, self).__init__()

                                            self.yang_name = "inbound"
                                            self.yang_parent_name = "multi-acl"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('entry', (YLeaf(YType.str, 'entry'), ['str'])),
                                            ])
                                            self.entry = None
                                            self._segment_path = lambda: "inbound"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Inbound, [u'entry'], name, value)


                                    class Outbound(Entity):
                                        """
                                        Outbound ACLs
                                        
                                        .. attribute:: entry
                                        
                                        	
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-io-oper'
                                        _revision = '2015-10-20'

                                        def __init__(self):
                                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Outbound, self).__init__()

                                            self.yang_name = "outbound"
                                            self.yang_parent_name = "multi-acl"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('entry', (YLeaf(YType.str, 'entry'), ['str'])),
                                            ])
                                            self.entry = None
                                            self._segment_path = lambda: "outbound"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Outbound, [u'entry'], name, value)


                                    class Common(Entity):
                                        """
                                        Common ACLs
                                        
                                        .. attribute:: entry
                                        
                                        	
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-io-oper'
                                        _revision = '2015-10-20'

                                        def __init__(self):
                                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Common, self).__init__()

                                            self.yang_name = "common"
                                            self.yang_parent_name = "multi-acl"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('entry', (YLeaf(YType.str, 'entry'), ['str'])),
                                            ])
                                            self.entry = None
                                            self._segment_path = lambda: "common"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl.Common, [u'entry'], name, value)


                                class HelperAddress(Entity):
                                    """
                                    Helper Addresses configured on the interface
                                    
                                    .. attribute:: address_array
                                    
                                    	Helper address
                                    	**type**\: list of  		 :py:class:`AddressArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress.AddressArray>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress, self).__init__()

                                        self.yang_name = "helper-address"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("address-array", ("address_array", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress.AddressArray))])
                                        self._leafs = OrderedDict()

                                        self.address_array = YList(self)
                                        self._segment_path = lambda: "helper-address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress, [], name, value)


                                    class AddressArray(Entity):
                                        """
                                        Helper address
                                        
                                        .. attribute:: entry
                                        
                                        	
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        

                                        """

                                        _prefix = 'ipv4-io-oper'
                                        _revision = '2015-10-20'

                                        def __init__(self):
                                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress.AddressArray, self).__init__()

                                            self.yang_name = "address-array"
                                            self.yang_parent_name = "helper-address"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('entry', (YLeaf(YType.str, 'entry'), ['str'])),
                                            ])
                                            self.entry = None
                                            self._segment_path = lambda: "address-array"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress.AddressArray, [u'entry'], name, value)


                                class Rpf(Entity):
                                    """
                                    RPF config on the interface
                                    
                                    .. attribute:: enable
                                    
                                    	Enable RPF config
                                    	**type**\: bool
                                    
                                    .. attribute:: allow_default_route
                                    
                                    	Allow Default Route
                                    	**type**\: bool
                                    
                                    .. attribute:: allow_self_ping
                                    
                                    	Allow Self Ping
                                    	**type**\: bool
                                    
                                    .. attribute:: mode
                                    
                                    	RPF Mode (loose/strict)
                                    	**type**\:  :py:class:`RpfMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.RpfMode>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf, self).__init__()

                                        self.yang_name = "rpf"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                            ('allow_default_route', (YLeaf(YType.boolean, 'allow-default-route'), ['bool'])),
                                            ('allow_self_ping', (YLeaf(YType.boolean, 'allow-self-ping'), ['bool'])),
                                            ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'RpfMode', '')])),
                                        ])
                                        self.enable = None
                                        self.allow_default_route = None
                                        self.allow_self_ping = None
                                        self.mode = None
                                        self._segment_path = lambda: "rpf"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf, [u'enable', u'allow_default_route', u'allow_self_ping', u'mode'], name, value)


                                class BgpPa(Entity):
                                    """
                                    BGP PA config on the interface
                                    
                                    .. attribute:: input
                                    
                                    	BGP PA input config
                                    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input>`
                                    
                                    .. attribute:: output
                                    
                                    	BGP PA output config
                                    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa, self).__init__()

                                        self.yang_name = "bgp-pa"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("input", ("input", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input)), ("output", ("output", Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output))])
                                        self._leafs = OrderedDict()

                                        self.input = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input()
                                        self.input.parent = self
                                        self._children_name_map["input"] = "input"

                                        self.output = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output()
                                        self.output.parent = self
                                        self._children_name_map["output"] = "output"
                                        self._segment_path = lambda: "bgp-pa"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa, [], name, value)


                                    class Input(Entity):
                                        """
                                        BGP PA input config
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP PA for ingress/egress
                                        	**type**\: bool
                                        
                                        .. attribute:: source
                                        
                                        	Enable source accouting
                                        	**type**\: bool
                                        
                                        .. attribute:: destination
                                        
                                        	Enable destination accouting
                                        	**type**\: bool
                                        
                                        

                                        """

                                        _prefix = 'ipv4-io-oper'
                                        _revision = '2015-10-20'

                                        def __init__(self):
                                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input, self).__init__()

                                            self.yang_name = "input"
                                            self.yang_parent_name = "bgp-pa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                                ('source', (YLeaf(YType.boolean, 'source'), ['bool'])),
                                                ('destination', (YLeaf(YType.boolean, 'destination'), ['bool'])),
                                            ])
                                            self.enable = None
                                            self.source = None
                                            self.destination = None
                                            self._segment_path = lambda: "input"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input, [u'enable', u'source', u'destination'], name, value)


                                    class Output(Entity):
                                        """
                                        BGP PA output config
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP PA for ingress/egress
                                        	**type**\: bool
                                        
                                        .. attribute:: source
                                        
                                        	Enable source accouting
                                        	**type**\: bool
                                        
                                        .. attribute:: destination
                                        
                                        	Enable destination accouting
                                        	**type**\: bool
                                        
                                        

                                        """

                                        _prefix = 'ipv4-io-oper'
                                        _revision = '2015-10-20'

                                        def __init__(self):
                                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output, self).__init__()

                                            self.yang_name = "output"
                                            self.yang_parent_name = "bgp-pa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                                ('source', (YLeaf(YType.boolean, 'source'), ['bool'])),
                                                ('destination', (YLeaf(YType.boolean, 'destination'), ['bool'])),
                                            ])
                                            self.enable = None
                                            self.source = None
                                            self.destination = None
                                            self._segment_path = lambda: "output"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output, [u'enable', u'source', u'destination'], name, value)


                                class PubUtime(Entity):
                                    """
                                    Address Publish Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.PubUtime, self).__init__()

                                        self.yang_name = "pub-utime"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict()
                                        self._segment_path = lambda: "pub-utime"
                                        self._is_frozen = True


                                class IdbUtime(Entity):
                                    """
                                    IDB Create Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime, self).__init__()

                                        self.yang_name = "idb-utime"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict()
                                        self._segment_path = lambda: "idb-utime"
                                        self._is_frozen = True


                                class CapsUtime(Entity):
                                    """
                                    CAPS Add Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime, self).__init__()

                                        self.yang_name = "caps-utime"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict()
                                        self._segment_path = lambda: "caps-utime"
                                        self._is_frozen = True


                                class FwdEnUtime(Entity):
                                    """
                                    FWD ENABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime, self).__init__()

                                        self.yang_name = "fwd-en-utime"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict()
                                        self._segment_path = lambda: "fwd-en-utime"
                                        self._is_frozen = True


                                class FwdDisUtime(Entity):
                                    """
                                    FWD DISABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime, self).__init__()

                                        self.yang_name = "fwd-dis-utime"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict()
                                        self._segment_path = lambda: "fwd-dis-utime"
                                        self._is_frozen = True


                                class MulticastGroup(Entity):
                                    """
                                    Multicast groups joined on the interface
                                    
                                    .. attribute:: group_address
                                    
                                    	Address of multicast group
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup, self).__init__()

                                        self.yang_name = "multicast-group"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('group_address', (YLeaf(YType.str, 'group-address'), ['str'])),
                                        ])
                                        self.group_address = None
                                        self._segment_path = lambda: "multicast-group"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup, [u'group_address'], name, value)


                                class SecondaryAddress(Entity):
                                    """
                                    Secondary addresses on the interface
                                    
                                    .. attribute:: address
                                    
                                    	Address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix length of address
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route Tag associated with this address (0 = no tag)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.SecondaryAddress, self).__init__()

                                        self.yang_name = "secondary-address"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                            ('route_tag', (YLeaf(YType.uint32, 'route-tag'), ['int'])),
                                        ])
                                        self.address = None
                                        self.prefix_length = None
                                        self.route_tag = None
                                        self._segment_path = lambda: "secondary-address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.SecondaryAddress, [u'address', u'prefix_length', u'route_tag'], name, value)


                class Summary(Entity):
                    """
                    Summary of IPv4 network operational interface
                    data on a node
                    
                    .. attribute:: if_up_up
                    
                    	Number of interfaces (up,up)
                    	**type**\:  :py:class:`IfUpUp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp>`
                    
                    .. attribute:: if_up_down
                    
                    	Number of interfaces (up,down)
                    	**type**\:  :py:class:`IfUpDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown>`
                    
                    .. attribute:: if_down_down
                    
                    	Number of interfaces (down,down)
                    	**type**\:  :py:class:`IfDownDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown>`
                    
                    .. attribute:: if_shutdown_down
                    
                    	Number of interfaces (shutdown,down)
                    	**type**\:  :py:class:`IfShutdownDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown>`
                    
                    .. attribute:: if_up_down_basecaps_up
                    
                    	Number of interfaces (up,down) with basecaps up
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-io-oper'
                    _revision = '2015-10-20'

                    def __init__(self):
                        super(Ipv4Network.Nodes.Node.InterfaceData.Summary, self).__init__()

                        self.yang_name = "summary"
                        self.yang_parent_name = "interface-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("if-up-up", ("if_up_up", Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp)), ("if-up-down", ("if_up_down", Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown)), ("if-down-down", ("if_down_down", Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown)), ("if-shutdown-down", ("if_shutdown_down", Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown))])
                        self._leafs = OrderedDict([
                            ('if_up_down_basecaps_up', (YLeaf(YType.uint32, 'if-up-down-basecaps-up'), ['int'])),
                        ])
                        self.if_up_down_basecaps_up = None

                        self.if_up_up = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp()
                        self.if_up_up.parent = self
                        self._children_name_map["if_up_up"] = "if-up-up"

                        self.if_up_down = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown()
                        self.if_up_down.parent = self
                        self._children_name_map["if_up_down"] = "if-up-down"

                        self.if_down_down = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown()
                        self.if_down_down.parent = self
                        self._children_name_map["if_down_down"] = "if-down-down"

                        self.if_shutdown_down = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown()
                        self.if_shutdown_down.parent = self
                        self._children_name_map["if_shutdown_down"] = "if-shutdown-down"
                        self._segment_path = lambda: "summary"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Summary, [u'if_up_down_basecaps_up'], name, value)


                    class IfUpUp(Entity):
                        """
                        Number of interfaces (up,up)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp, self).__init__()

                            self.yang_name = "if-up-up"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ip_assigned', (YLeaf(YType.uint32, 'ip-assigned'), ['int'])),
                                ('ip_unnumbered', (YLeaf(YType.uint32, 'ip-unnumbered'), ['int'])),
                                ('ip_unassigned', (YLeaf(YType.uint32, 'ip-unassigned'), ['int'])),
                            ])
                            self.ip_assigned = None
                            self.ip_unnumbered = None
                            self.ip_unassigned = None
                            self._segment_path = lambda: "if-up-up"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp, [u'ip_assigned', u'ip_unnumbered', u'ip_unassigned'], name, value)


                    class IfUpDown(Entity):
                        """
                        Number of interfaces (up,down)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown, self).__init__()

                            self.yang_name = "if-up-down"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ip_assigned', (YLeaf(YType.uint32, 'ip-assigned'), ['int'])),
                                ('ip_unnumbered', (YLeaf(YType.uint32, 'ip-unnumbered'), ['int'])),
                                ('ip_unassigned', (YLeaf(YType.uint32, 'ip-unassigned'), ['int'])),
                            ])
                            self.ip_assigned = None
                            self.ip_unnumbered = None
                            self.ip_unassigned = None
                            self._segment_path = lambda: "if-up-down"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown, [u'ip_assigned', u'ip_unnumbered', u'ip_unassigned'], name, value)


                    class IfDownDown(Entity):
                        """
                        Number of interfaces (down,down)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown, self).__init__()

                            self.yang_name = "if-down-down"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ip_assigned', (YLeaf(YType.uint32, 'ip-assigned'), ['int'])),
                                ('ip_unnumbered', (YLeaf(YType.uint32, 'ip-unnumbered'), ['int'])),
                                ('ip_unassigned', (YLeaf(YType.uint32, 'ip-unassigned'), ['int'])),
                            ])
                            self.ip_assigned = None
                            self.ip_unnumbered = None
                            self.ip_unassigned = None
                            self._segment_path = lambda: "if-down-down"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown, [u'ip_assigned', u'ip_unnumbered', u'ip_unassigned'], name, value)


                    class IfShutdownDown(Entity):
                        """
                        Number of interfaces (shutdown,down)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces with explicit addresses
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown, self).__init__()

                            self.yang_name = "if-shutdown-down"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ip_assigned', (YLeaf(YType.uint32, 'ip-assigned'), ['int'])),
                                ('ip_unnumbered', (YLeaf(YType.uint32, 'ip-unnumbered'), ['int'])),
                                ('ip_unassigned', (YLeaf(YType.uint32, 'ip-unassigned'), ['int'])),
                            ])
                            self.ip_assigned = None
                            self.ip_unnumbered = None
                            self.ip_unassigned = None
                            self._segment_path = lambda: "if-shutdown-down"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown, [u'ip_assigned', u'ip_unnumbered', u'ip_unassigned'], name, value)


            class Statistics(Entity):
                """
                Statistical IPv4 network operational data for
                a node
                
                .. attribute:: traffic
                
                	Traffic statistics for a node
                	**type**\:  :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.Statistics.Traffic>`
                
                

                """

                _prefix = 'ipv4-io-oper'
                _revision = '2015-10-20'

                def __init__(self):
                    super(Ipv4Network.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("traffic", ("traffic", Ipv4Network.Nodes.Node.Statistics.Traffic))])
                    self._leafs = OrderedDict()

                    self.traffic = Ipv4Network.Nodes.Node.Statistics.Traffic()
                    self.traffic.parent = self
                    self._children_name_map["traffic"] = "traffic"
                    self._segment_path = lambda: "statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Network.Nodes.Node.Statistics, [], name, value)


                class Traffic(Entity):
                    """
                    Traffic statistics for a node
                    
                    .. attribute:: ipv4_stats
                    
                    	IPv4 Network Stats
                    	**type**\:  :py:class:`Ipv4Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats>`
                    
                    .. attribute:: icmp_stats
                    
                    	ICMP Stats
                    	**type**\:  :py:class:`IcmpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats>`
                    
                    

                    """

                    _prefix = 'ipv4-io-oper'
                    _revision = '2015-10-20'

                    def __init__(self):
                        super(Ipv4Network.Nodes.Node.Statistics.Traffic, self).__init__()

                        self.yang_name = "traffic"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ipv4-stats", ("ipv4_stats", Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats)), ("icmp-stats", ("icmp_stats", Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats))])
                        self._leafs = OrderedDict()

                        self.ipv4_stats = Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats()
                        self.ipv4_stats.parent = self
                        self._children_name_map["ipv4_stats"] = "ipv4-stats"

                        self.icmp_stats = Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats()
                        self.icmp_stats.parent = self
                        self._children_name_map["icmp_stats"] = "icmp-stats"
                        self._segment_path = lambda: "traffic"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Network.Nodes.Node.Statistics.Traffic, [], name, value)


                    class Ipv4Stats(Entity):
                        """
                        IPv4 Network Stats
                        
                        .. attribute:: input_packets
                        
                        	Input Packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_packets
                        
                        	Received Packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: format_errors
                        
                        	Format Errors
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hop_count
                        
                        	Bad Hop Count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_source_address
                        
                        	Bad Source Address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_header
                        
                        	Bad Header
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_protocol
                        
                        	No Protocol
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_gateway
                        
                        	No Gateway
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassemble_input
                        
                        	RaInput
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassembled
                        
                        	Reassembled
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassemble_timeout
                        
                        	Reassembly Timeout
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassemble_max_drop
                        
                        	Reassembly Max Drop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassemble_failed
                        
                        	Reassembly Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: options_present
                        
                        	IP Options Present
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_option
                        
                        	Bad Option
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_option
                        
                        	Unknown Option
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_security_option
                        
                        	Bad Security Option
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: basic_security_option
                        
                        	Basic Security Option
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: extended_security_option
                        
                        	Extended Security Option
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: cipso_option
                        
                        	Cipso Option
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: strict_source_route_option
                        
                        	Strict Source Route Option
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: loose_source_route_option
                        
                        	Loose Source Route Option
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: record_route_option
                        
                        	Record Route Option
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sid_option
                        
                        	SID Option
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: timestamp_option
                        
                        	Timestamp Option
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: router_alert_option
                        
                        	Router Alert Option
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: noop_option
                        
                        	Noop Option
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_option
                        
                        	End Option
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: packets_output
                        
                        	Packets Output
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: packets_forwarded
                        
                        	Packets Forwarded
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: packets_fragmented
                        
                        	Packets Fragmented
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fragment_count
                        
                        	Fragment Count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: encapsulation_failed
                        
                        	Encapsulation Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_router
                        
                        	No Router
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: packet_too_big
                        
                        	Packet Too Big
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: multicast_in
                        
                        	Multicast In
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: multicast_out
                        
                        	Multicast Out
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: broadcast_in
                        
                        	Broadcast In
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: broadcast_out
                        
                        	Broadcast Out
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v4_encap
                        
                        	Lisp IPv4 encapped packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v4_decap
                        
                        	Lisp IPv4 decapped packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v6_encap
                        
                        	Lisp IPv6 encapped packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v6_decap
                        
                        	Lisp IPv6 decapped packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_encap_error
                        
                        	Lisp encap errors
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_decap_error
                        
                        	Lisp decap errors
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            super(Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats, self).__init__()

                            self.yang_name = "ipv4-stats"
                            self.yang_parent_name = "traffic"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('input_packets', (YLeaf(YType.uint32, 'input-packets'), ['int'])),
                                ('received_packets', (YLeaf(YType.uint32, 'received-packets'), ['int'])),
                                ('format_errors', (YLeaf(YType.uint32, 'format-errors'), ['int'])),
                                ('bad_hop_count', (YLeaf(YType.uint32, 'bad-hop-count'), ['int'])),
                                ('bad_source_address', (YLeaf(YType.uint32, 'bad-source-address'), ['int'])),
                                ('bad_header', (YLeaf(YType.uint32, 'bad-header'), ['int'])),
                                ('no_protocol', (YLeaf(YType.uint32, 'no-protocol'), ['int'])),
                                ('no_gateway', (YLeaf(YType.uint32, 'no-gateway'), ['int'])),
                                ('reassemble_input', (YLeaf(YType.uint32, 'reassemble-input'), ['int'])),
                                ('reassembled', (YLeaf(YType.uint32, 'reassembled'), ['int'])),
                                ('reassemble_timeout', (YLeaf(YType.uint32, 'reassemble-timeout'), ['int'])),
                                ('reassemble_max_drop', (YLeaf(YType.uint32, 'reassemble-max-drop'), ['int'])),
                                ('reassemble_failed', (YLeaf(YType.uint32, 'reassemble-failed'), ['int'])),
                                ('options_present', (YLeaf(YType.uint32, 'options-present'), ['int'])),
                                ('bad_option', (YLeaf(YType.uint32, 'bad-option'), ['int'])),
                                ('unknown_option', (YLeaf(YType.uint32, 'unknown-option'), ['int'])),
                                ('bad_security_option', (YLeaf(YType.uint32, 'bad-security-option'), ['int'])),
                                ('basic_security_option', (YLeaf(YType.uint32, 'basic-security-option'), ['int'])),
                                ('extended_security_option', (YLeaf(YType.uint32, 'extended-security-option'), ['int'])),
                                ('cipso_option', (YLeaf(YType.uint32, 'cipso-option'), ['int'])),
                                ('strict_source_route_option', (YLeaf(YType.uint32, 'strict-source-route-option'), ['int'])),
                                ('loose_source_route_option', (YLeaf(YType.uint32, 'loose-source-route-option'), ['int'])),
                                ('record_route_option', (YLeaf(YType.uint32, 'record-route-option'), ['int'])),
                                ('sid_option', (YLeaf(YType.uint32, 'sid-option'), ['int'])),
                                ('timestamp_option', (YLeaf(YType.uint32, 'timestamp-option'), ['int'])),
                                ('router_alert_option', (YLeaf(YType.uint32, 'router-alert-option'), ['int'])),
                                ('noop_option', (YLeaf(YType.uint32, 'noop-option'), ['int'])),
                                ('end_option', (YLeaf(YType.uint32, 'end-option'), ['int'])),
                                ('packets_output', (YLeaf(YType.uint32, 'packets-output'), ['int'])),
                                ('packets_forwarded', (YLeaf(YType.uint32, 'packets-forwarded'), ['int'])),
                                ('packets_fragmented', (YLeaf(YType.uint32, 'packets-fragmented'), ['int'])),
                                ('fragment_count', (YLeaf(YType.uint32, 'fragment-count'), ['int'])),
                                ('encapsulation_failed', (YLeaf(YType.uint32, 'encapsulation-failed'), ['int'])),
                                ('no_router', (YLeaf(YType.uint32, 'no-router'), ['int'])),
                                ('packet_too_big', (YLeaf(YType.uint32, 'packet-too-big'), ['int'])),
                                ('multicast_in', (YLeaf(YType.uint32, 'multicast-in'), ['int'])),
                                ('multicast_out', (YLeaf(YType.uint32, 'multicast-out'), ['int'])),
                                ('broadcast_in', (YLeaf(YType.uint32, 'broadcast-in'), ['int'])),
                                ('broadcast_out', (YLeaf(YType.uint32, 'broadcast-out'), ['int'])),
                                ('lisp_v4_encap', (YLeaf(YType.uint32, 'lisp-v4-encap'), ['int'])),
                                ('lisp_v4_decap', (YLeaf(YType.uint32, 'lisp-v4-decap'), ['int'])),
                                ('lisp_v6_encap', (YLeaf(YType.uint32, 'lisp-v6-encap'), ['int'])),
                                ('lisp_v6_decap', (YLeaf(YType.uint32, 'lisp-v6-decap'), ['int'])),
                                ('lisp_encap_error', (YLeaf(YType.uint32, 'lisp-encap-error'), ['int'])),
                                ('lisp_decap_error', (YLeaf(YType.uint32, 'lisp-decap-error'), ['int'])),
                            ])
                            self.input_packets = None
                            self.received_packets = None
                            self.format_errors = None
                            self.bad_hop_count = None
                            self.bad_source_address = None
                            self.bad_header = None
                            self.no_protocol = None
                            self.no_gateway = None
                            self.reassemble_input = None
                            self.reassembled = None
                            self.reassemble_timeout = None
                            self.reassemble_max_drop = None
                            self.reassemble_failed = None
                            self.options_present = None
                            self.bad_option = None
                            self.unknown_option = None
                            self.bad_security_option = None
                            self.basic_security_option = None
                            self.extended_security_option = None
                            self.cipso_option = None
                            self.strict_source_route_option = None
                            self.loose_source_route_option = None
                            self.record_route_option = None
                            self.sid_option = None
                            self.timestamp_option = None
                            self.router_alert_option = None
                            self.noop_option = None
                            self.end_option = None
                            self.packets_output = None
                            self.packets_forwarded = None
                            self.packets_fragmented = None
                            self.fragment_count = None
                            self.encapsulation_failed = None
                            self.no_router = None
                            self.packet_too_big = None
                            self.multicast_in = None
                            self.multicast_out = None
                            self.broadcast_in = None
                            self.broadcast_out = None
                            self.lisp_v4_encap = None
                            self.lisp_v4_decap = None
                            self.lisp_v6_encap = None
                            self.lisp_v6_decap = None
                            self.lisp_encap_error = None
                            self.lisp_decap_error = None
                            self._segment_path = lambda: "ipv4-stats"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats, [u'input_packets', u'received_packets', u'format_errors', u'bad_hop_count', u'bad_source_address', u'bad_header', u'no_protocol', u'no_gateway', u'reassemble_input', u'reassembled', u'reassemble_timeout', u'reassemble_max_drop', u'reassemble_failed', u'options_present', u'bad_option', u'unknown_option', u'bad_security_option', u'basic_security_option', u'extended_security_option', u'cipso_option', u'strict_source_route_option', u'loose_source_route_option', u'record_route_option', u'sid_option', u'timestamp_option', u'router_alert_option', u'noop_option', u'end_option', u'packets_output', u'packets_forwarded', u'packets_fragmented', u'fragment_count', u'encapsulation_failed', u'no_router', u'packet_too_big', u'multicast_in', u'multicast_out', u'broadcast_in', u'broadcast_out', u'lisp_v4_encap', u'lisp_v4_decap', u'lisp_v6_encap', u'lisp_v6_decap', u'lisp_encap_error', u'lisp_decap_error'], name, value)


                    class IcmpStats(Entity):
                        """
                        ICMP Stats
                        
                        .. attribute:: received
                        
                        	ICMP Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: checksum_error
                        
                        	ICMP Checksum Errors
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown
                        
                        	ICMP Unknown
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: output
                        
                        	ICMP Transmitted
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: admin_unreachable_sent
                        
                        	ICMP Admin Unreachable Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: network_unreachable_sent
                        
                        	ICMP Network Unreachable Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: host_unreachable_sent
                        
                        	ICMP Host Unreachable Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: protocol_unreachable_sent
                        
                        	ICMP Protocol Unreachable Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: port_unreachable_sent
                        
                        	ICMP Port Unreachable Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fragment_unreachable_sent
                        
                        	ICMP Fragment Unreachable Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: admin_unreachable_received
                        
                        	ICMP Admin Unreachable Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: network_unreachable_received
                        
                        	ICMP Network Unreachable Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: host_unreachable_received
                        
                        	ICMP Host Unreachable Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: protocol_unreachable_received
                        
                        	ICMP Protocol Unreachable Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: port_unreachable_received
                        
                        	ICMP Port Unreachable Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fragment_unreachable_received
                        
                        	ICMP Fragment Unreachable Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hopcount_sent
                        
                        	ICMP Hopcount Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassembly_sent
                        
                        	ICMP Reassembly Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hopcount_received
                        
                        	ICMP Hopcount Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassebly_received
                        
                        	ICMP Reassembly Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: param_error_received
                        
                        	ICMP Parameter Error Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: param_error_send
                        
                        	ICMP Parameter Error Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: echo_request_sent
                        
                        	ICMP Echo Request Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: echo_request_received
                        
                        	ICMP Echo Request Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: echo_reply_sent
                        
                        	ICMP Echo Reply Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: echo_reply_received
                        
                        	ICMP Echo Reply Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mask_request_sent
                        
                        	ICMP Mask Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mask_request_received
                        
                        	ICMP Mask Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mask_reply_sent
                        
                        	ICMP Mask Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mask_reply_received
                        
                        	ICMP Mask Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: source_quench_received
                        
                        	ICMP Source Quench
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: redirect_received
                        
                        	ICMP Redirect Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: redirect_send
                        
                        	ICMP Redirect Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: timestamp_received
                        
                        	ICMP Timestamp Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: timestamp_reply_received
                        
                        	ICMP Timestamp Reply Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: router_advert_received
                        
                        	ICMP Router Advertisement Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: router_solicit_received
                        
                        	ICMP Router Solicited Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            super(Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats, self).__init__()

                            self.yang_name = "icmp-stats"
                            self.yang_parent_name = "traffic"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('received', (YLeaf(YType.uint32, 'received'), ['int'])),
                                ('checksum_error', (YLeaf(YType.uint32, 'checksum-error'), ['int'])),
                                ('unknown', (YLeaf(YType.uint32, 'unknown'), ['int'])),
                                ('output', (YLeaf(YType.uint32, 'output'), ['int'])),
                                ('admin_unreachable_sent', (YLeaf(YType.uint32, 'admin-unreachable-sent'), ['int'])),
                                ('network_unreachable_sent', (YLeaf(YType.uint32, 'network-unreachable-sent'), ['int'])),
                                ('host_unreachable_sent', (YLeaf(YType.uint32, 'host-unreachable-sent'), ['int'])),
                                ('protocol_unreachable_sent', (YLeaf(YType.uint32, 'protocol-unreachable-sent'), ['int'])),
                                ('port_unreachable_sent', (YLeaf(YType.uint32, 'port-unreachable-sent'), ['int'])),
                                ('fragment_unreachable_sent', (YLeaf(YType.uint32, 'fragment-unreachable-sent'), ['int'])),
                                ('admin_unreachable_received', (YLeaf(YType.uint32, 'admin-unreachable-received'), ['int'])),
                                ('network_unreachable_received', (YLeaf(YType.uint32, 'network-unreachable-received'), ['int'])),
                                ('host_unreachable_received', (YLeaf(YType.uint32, 'host-unreachable-received'), ['int'])),
                                ('protocol_unreachable_received', (YLeaf(YType.uint32, 'protocol-unreachable-received'), ['int'])),
                                ('port_unreachable_received', (YLeaf(YType.uint32, 'port-unreachable-received'), ['int'])),
                                ('fragment_unreachable_received', (YLeaf(YType.uint32, 'fragment-unreachable-received'), ['int'])),
                                ('hopcount_sent', (YLeaf(YType.uint32, 'hopcount-sent'), ['int'])),
                                ('reassembly_sent', (YLeaf(YType.uint32, 'reassembly-sent'), ['int'])),
                                ('hopcount_received', (YLeaf(YType.uint32, 'hopcount-received'), ['int'])),
                                ('reassebly_received', (YLeaf(YType.uint32, 'reassebly-received'), ['int'])),
                                ('param_error_received', (YLeaf(YType.uint32, 'param-error-received'), ['int'])),
                                ('param_error_send', (YLeaf(YType.uint32, 'param-error-send'), ['int'])),
                                ('echo_request_sent', (YLeaf(YType.uint32, 'echo-request-sent'), ['int'])),
                                ('echo_request_received', (YLeaf(YType.uint32, 'echo-request-received'), ['int'])),
                                ('echo_reply_sent', (YLeaf(YType.uint32, 'echo-reply-sent'), ['int'])),
                                ('echo_reply_received', (YLeaf(YType.uint32, 'echo-reply-received'), ['int'])),
                                ('mask_request_sent', (YLeaf(YType.uint32, 'mask-request-sent'), ['int'])),
                                ('mask_request_received', (YLeaf(YType.uint32, 'mask-request-received'), ['int'])),
                                ('mask_reply_sent', (YLeaf(YType.uint32, 'mask-reply-sent'), ['int'])),
                                ('mask_reply_received', (YLeaf(YType.uint32, 'mask-reply-received'), ['int'])),
                                ('source_quench_received', (YLeaf(YType.uint32, 'source-quench-received'), ['int'])),
                                ('redirect_received', (YLeaf(YType.uint32, 'redirect-received'), ['int'])),
                                ('redirect_send', (YLeaf(YType.uint32, 'redirect-send'), ['int'])),
                                ('timestamp_received', (YLeaf(YType.uint32, 'timestamp-received'), ['int'])),
                                ('timestamp_reply_received', (YLeaf(YType.uint32, 'timestamp-reply-received'), ['int'])),
                                ('router_advert_received', (YLeaf(YType.uint32, 'router-advert-received'), ['int'])),
                                ('router_solicit_received', (YLeaf(YType.uint32, 'router-solicit-received'), ['int'])),
                            ])
                            self.received = None
                            self.checksum_error = None
                            self.unknown = None
                            self.output = None
                            self.admin_unreachable_sent = None
                            self.network_unreachable_sent = None
                            self.host_unreachable_sent = None
                            self.protocol_unreachable_sent = None
                            self.port_unreachable_sent = None
                            self.fragment_unreachable_sent = None
                            self.admin_unreachable_received = None
                            self.network_unreachable_received = None
                            self.host_unreachable_received = None
                            self.protocol_unreachable_received = None
                            self.port_unreachable_received = None
                            self.fragment_unreachable_received = None
                            self.hopcount_sent = None
                            self.reassembly_sent = None
                            self.hopcount_received = None
                            self.reassebly_received = None
                            self.param_error_received = None
                            self.param_error_send = None
                            self.echo_request_sent = None
                            self.echo_request_received = None
                            self.echo_reply_sent = None
                            self.echo_reply_received = None
                            self.mask_request_sent = None
                            self.mask_request_received = None
                            self.mask_reply_sent = None
                            self.mask_reply_received = None
                            self.source_quench_received = None
                            self.redirect_received = None
                            self.redirect_send = None
                            self.timestamp_received = None
                            self.timestamp_reply_received = None
                            self.router_advert_received = None
                            self.router_solicit_received = None
                            self._segment_path = lambda: "icmp-stats"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats, [u'received', u'checksum_error', u'unknown', u'output', u'admin_unreachable_sent', u'network_unreachable_sent', u'host_unreachable_sent', u'protocol_unreachable_sent', u'port_unreachable_sent', u'fragment_unreachable_sent', u'admin_unreachable_received', u'network_unreachable_received', u'host_unreachable_received', u'protocol_unreachable_received', u'port_unreachable_received', u'fragment_unreachable_received', u'hopcount_sent', u'reassembly_sent', u'hopcount_received', u'reassebly_received', u'param_error_received', u'param_error_send', u'echo_request_sent', u'echo_request_received', u'echo_reply_sent', u'echo_reply_received', u'mask_request_sent', u'mask_request_received', u'mask_reply_sent', u'mask_reply_received', u'source_quench_received', u'redirect_received', u'redirect_send', u'timestamp_received', u'timestamp_reply_received', u'router_advert_received', u'router_solicit_received'], name, value)


    class Interfaces(Entity):
        """
        IPv4 network operational interface data
        
        .. attribute:: interface
        
        	Interface names with VRF
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv4-ma-oper'
        _revision = '2017-08-23'

        def __init__(self):
            super(Ipv4Network.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "ipv4-network"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", Ipv4Network.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ma-oper:interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-io-oper:ipv4-network/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Network.Interfaces, [], name, value)


        class Interface(Entity):
            """
            Interface names with VRF
            
            .. attribute:: interface_name  (key)
            
            	The name of the interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: vrfs
            
            	List of VRF on the interface
            	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs>`
            
            

            """

            _prefix = 'ipv4-ma-oper'
            _revision = '2017-08-23'

            def __init__(self):
                super(Ipv4Network.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("vrfs", ("vrfs", Ipv4Network.Interfaces.Interface.Vrfs))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                ])
                self.interface_name = None

                self.vrfs = Ipv4Network.Interfaces.Interface.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-io-oper:ipv4-network/Cisco-IOS-XR-ipv4-ma-oper:interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Network.Interfaces.Interface, ['interface_name'], name, value)


            class Vrfs(Entity):
                """
                List of VRF on the interface
                
                .. attribute:: vrf
                
                	VRF information on the interface
                	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf>`
                
                

                """

                _prefix = 'ipv4-ma-oper'
                _revision = '2017-08-23'

                def __init__(self):
                    super(Ipv4Network.Interfaces.Interface.Vrfs, self).__init__()

                    self.yang_name = "vrfs"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("vrf", ("vrf", Ipv4Network.Interfaces.Interface.Vrfs.Vrf))])
                    self._leafs = OrderedDict()

                    self.vrf = YList(self)
                    self._segment_path = lambda: "vrfs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs, [], name, value)


                class Vrf(Entity):
                    """
                    VRF information on the interface
                    
                    .. attribute:: vrf_name  (key)
                    
                    	The VRF name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: detail
                    
                    	Detail IPv4 network operational data for an interface
                    	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail>`
                    
                    .. attribute:: brief
                    
                    	Brief IPv4 network operational data for an interface
                    	**type**\:  :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief>`
                    
                    

                    """

                    _prefix = 'ipv4-ma-oper'
                    _revision = '2017-08-23'

                    def __init__(self):
                        super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "vrfs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['vrf_name']
                        self._child_classes = OrderedDict([("detail", ("detail", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail)), ("brief", ("brief", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief))])
                        self._leafs = OrderedDict([
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ])
                        self.vrf_name = None

                        self.detail = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail()
                        self.detail.parent = self
                        self._children_name_map["detail"] = "detail"

                        self.brief = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief()
                        self.brief.parent = self
                        self._children_name_map["brief"] = "brief"
                        self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf, ['vrf_name'], name, value)


                    class Detail(Entity):
                        """
                        Detail IPv4 network operational data for an
                        interface
                        
                        .. attribute:: acl
                        
                        	ACLs configured on the interface
                        	**type**\:  :py:class:`Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl>`
                        
                        .. attribute:: multi_acl
                        
                        	Multi ACLs configured on the interface
                        	**type**\:  :py:class:`MultiAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl>`
                        
                        .. attribute:: helper_address
                        
                        	Helper Addresses configured on the interface
                        	**type**\:  :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress>`
                        
                        .. attribute:: rpf
                        
                        	RPF config on the interface
                        	**type**\:  :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf>`
                        
                        .. attribute:: bgp_pa
                        
                        	BGP PA config on the interface
                        	**type**\:  :py:class:`BgpPa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa>`
                        
                        .. attribute:: pub_utime
                        
                        	Address Publish Time
                        	**type**\:  :py:class:`PubUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.PubUtime>`
                        
                        .. attribute:: idb_utime
                        
                        	IDB Create Time
                        	**type**\:  :py:class:`IdbUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.IdbUtime>`
                        
                        .. attribute:: caps_utime
                        
                        	CAPS Add Time
                        	**type**\:  :py:class:`CapsUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.CapsUtime>`
                        
                        .. attribute:: fwd_en_utime
                        
                        	FWD ENABLE Time
                        	**type**\:  :py:class:`FwdEnUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdEnUtime>`
                        
                        .. attribute:: fwd_dis_utime
                        
                        	FWD DISABLE Time
                        	**type**\:  :py:class:`FwdDisUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdDisUtime>`
                        
                        .. attribute:: primary_address
                        
                        	Primary address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_id
                        
                        	VRF ID of the interface
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: line_state
                        
                        	Line state of the interface
                        	**type**\:  :py:class:`Ipv4MaOperLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper.Ipv4MaOperLineState>`
                        
                        .. attribute:: prefix_length
                        
                        	Prefix length of primary address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: route_tag
                        
                        	Route tag associated with the primary address (0 = no tag)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mtu
                        
                        	IP MTU of the interface
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unreachable
                        
                        	Are ICMP unreachables sent on the interface?
                        	**type**\: bool
                        
                        .. attribute:: redirect
                        
                        	Are ICMP redirects sent on the interface?
                        	**type**\: bool
                        
                        .. attribute:: direct_broadcast
                        
                        	Are direct broadcasts sent on the interface?
                        	**type**\: bool
                        
                        .. attribute:: mask_reply
                        
                        	Are mask replies sent on the interface?
                        	**type**\: bool
                        
                        .. attribute:: rg_id_exists
                        
                        	Does ICCP RG ID exist on the interface?
                        	**type**\: bool
                        
                        .. attribute:: mlacp_active
                        
                        	Is mLACP state Active (valid if RG ID exists)
                        	**type**\: bool
                        
                        .. attribute:: unnumbered_interface_name
                        
                        	Name of referenced interface (valid if unnumbered)
                        	**type**\: str
                        
                        .. attribute:: next_unnumbered_interface_name
                        
                        	Name of interface which is also unnum to         same interface where this intf is unnumbered
                        	**type**\: str
                        
                        .. attribute:: proxy_arp_disabled
                        
                        	Is Proxy ARP disabled on the interface?
                        	**type**\: bool
                        
                        .. attribute:: flow_tag_src
                        
                        	Is BGP Flow Tag Source is enable
                        	**type**\: bool
                        
                        .. attribute:: flow_tag_dst
                        
                        	Is BGP Flow Tag Destination is enable
                        	**type**\: bool
                        
                        .. attribute:: config_flags
                        
                        	IDB configuration flags
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: oper_flags
                        
                        	IDB operational flags
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: arm_flags
                        
                        	IP ARM operation flags
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: state_recvd_frm_im
                        
                        	state as recieved                                from IM
                        	**type**\:  :py:class:`Ipv4MaOperLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper.Ipv4MaOperLineState>`
                        
                        .. attribute:: cflct_address
                        
                        	Conflicated ipv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: client_type
                        
                        	Client type for IDB
                        	**type**\:  :py:class:`Ipv4MaOperConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper.Ipv4MaOperConfig>`
                        
                        .. attribute:: is_or_event
                        
                        	Is OR event for IDB
                        	**type**\: bool
                        
                        .. attribute:: or_im_state
                        
                        	OR IM state type
                        	**type**\:  :py:class:`Ipv4MaOperLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper.Ipv4MaOperLineState>`
                        
                        .. attribute:: idb_pointer
                        
                        	idb pointer value
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: multicast_group
                        
                        	Multicast groups joined on the interface
                        	**type**\: list of  		 :py:class:`MulticastGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MulticastGroup>`
                        
                        .. attribute:: secondary_address
                        
                        	Secondary addresses on the interface
                        	**type**\: list of  		 :py:class:`SecondaryAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.SecondaryAddress>`
                        
                        

                        """

                        _prefix = 'ipv4-ma-oper'
                        _revision = '2017-08-23'

                        def __init__(self):
                            super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail, self).__init__()

                            self.yang_name = "detail"
                            self.yang_parent_name = "vrf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("acl", ("acl", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl)), ("multi-acl", ("multi_acl", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl)), ("helper-address", ("helper_address", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress)), ("rpf", ("rpf", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf)), ("bgp-pa", ("bgp_pa", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa)), ("pub-utime", ("pub_utime", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.PubUtime)), ("idb-utime", ("idb_utime", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.IdbUtime)), ("caps-utime", ("caps_utime", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.CapsUtime)), ("fwd-en-utime", ("fwd_en_utime", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdEnUtime)), ("fwd-dis-utime", ("fwd_dis_utime", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdDisUtime)), ("multicast-group", ("multicast_group", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MulticastGroup)), ("secondary-address", ("secondary_address", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.SecondaryAddress))])
                            self._leafs = OrderedDict([
                                ('primary_address', (YLeaf(YType.str, 'primary-address'), ['str'])),
                                ('vrf_id', (YLeaf(YType.uint32, 'vrf-id'), ['int'])),
                                ('line_state', (YLeaf(YType.enumeration, 'line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper', 'Ipv4MaOperLineState', '')])),
                                ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                ('route_tag', (YLeaf(YType.uint32, 'route-tag'), ['int'])),
                                ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                                ('unreachable', (YLeaf(YType.boolean, 'unreachable'), ['bool'])),
                                ('redirect', (YLeaf(YType.boolean, 'redirect'), ['bool'])),
                                ('direct_broadcast', (YLeaf(YType.boolean, 'direct-broadcast'), ['bool'])),
                                ('mask_reply', (YLeaf(YType.boolean, 'mask-reply'), ['bool'])),
                                ('rg_id_exists', (YLeaf(YType.boolean, 'rg-id-exists'), ['bool'])),
                                ('mlacp_active', (YLeaf(YType.boolean, 'mlacp-active'), ['bool'])),
                                ('unnumbered_interface_name', (YLeaf(YType.str, 'unnumbered-interface-name'), ['str'])),
                                ('next_unnumbered_interface_name', (YLeaf(YType.str, 'next-unnumbered-interface-name'), ['str'])),
                                ('proxy_arp_disabled', (YLeaf(YType.boolean, 'proxy-arp-disabled'), ['bool'])),
                                ('flow_tag_src', (YLeaf(YType.boolean, 'flow-tag-src'), ['bool'])),
                                ('flow_tag_dst', (YLeaf(YType.boolean, 'flow-tag-dst'), ['bool'])),
                                ('config_flags', (YLeaf(YType.uint16, 'config-flags'), ['int'])),
                                ('oper_flags', (YLeaf(YType.uint64, 'oper-flags'), ['int'])),
                                ('arm_flags', (YLeaf(YType.uint16, 'arm-flags'), ['int'])),
                                ('state_recvd_frm_im', (YLeaf(YType.enumeration, 'state-recvd-frm-im'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper', 'Ipv4MaOperLineState', '')])),
                                ('cflct_address', (YLeaf(YType.str, 'cflct-address'), ['str'])),
                                ('client_type', (YLeaf(YType.enumeration, 'client-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper', 'Ipv4MaOperConfig', '')])),
                                ('is_or_event', (YLeaf(YType.boolean, 'is-or-event'), ['bool'])),
                                ('or_im_state', (YLeaf(YType.enumeration, 'or-im-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper', 'Ipv4MaOperLineState', '')])),
                                ('idb_pointer', (YLeaf(YType.uint64, 'idb-pointer'), ['int'])),
                            ])
                            self.primary_address = None
                            self.vrf_id = None
                            self.line_state = None
                            self.prefix_length = None
                            self.route_tag = None
                            self.mtu = None
                            self.unreachable = None
                            self.redirect = None
                            self.direct_broadcast = None
                            self.mask_reply = None
                            self.rg_id_exists = None
                            self.mlacp_active = None
                            self.unnumbered_interface_name = None
                            self.next_unnumbered_interface_name = None
                            self.proxy_arp_disabled = None
                            self.flow_tag_src = None
                            self.flow_tag_dst = None
                            self.config_flags = None
                            self.oper_flags = None
                            self.arm_flags = None
                            self.state_recvd_frm_im = None
                            self.cflct_address = None
                            self.client_type = None
                            self.is_or_event = None
                            self.or_im_state = None
                            self.idb_pointer = None

                            self.acl = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl()
                            self.acl.parent = self
                            self._children_name_map["acl"] = "acl"

                            self.multi_acl = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl()
                            self.multi_acl.parent = self
                            self._children_name_map["multi_acl"] = "multi-acl"

                            self.helper_address = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress()
                            self.helper_address.parent = self
                            self._children_name_map["helper_address"] = "helper-address"

                            self.rpf = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf()
                            self.rpf.parent = self
                            self._children_name_map["rpf"] = "rpf"

                            self.bgp_pa = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa()
                            self.bgp_pa.parent = self
                            self._children_name_map["bgp_pa"] = "bgp-pa"

                            self.pub_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.PubUtime()
                            self.pub_utime.parent = self
                            self._children_name_map["pub_utime"] = "pub-utime"

                            self.idb_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.IdbUtime()
                            self.idb_utime.parent = self
                            self._children_name_map["idb_utime"] = "idb-utime"

                            self.caps_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.CapsUtime()
                            self.caps_utime.parent = self
                            self._children_name_map["caps_utime"] = "caps-utime"

                            self.fwd_en_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdEnUtime()
                            self.fwd_en_utime.parent = self
                            self._children_name_map["fwd_en_utime"] = "fwd-en-utime"

                            self.fwd_dis_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdDisUtime()
                            self.fwd_dis_utime.parent = self
                            self._children_name_map["fwd_dis_utime"] = "fwd-dis-utime"

                            self.multicast_group = YList(self)
                            self.secondary_address = YList(self)
                            self._segment_path = lambda: "detail"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail, ['primary_address', 'vrf_id', 'line_state', 'prefix_length', 'route_tag', 'mtu', 'unreachable', 'redirect', 'direct_broadcast', 'mask_reply', 'rg_id_exists', 'mlacp_active', 'unnumbered_interface_name', 'next_unnumbered_interface_name', 'proxy_arp_disabled', 'flow_tag_src', 'flow_tag_dst', 'config_flags', 'oper_flags', 'arm_flags', 'state_recvd_frm_im', 'cflct_address', 'client_type', 'is_or_event', 'or_im_state', 'idb_pointer'], name, value)


                        class Acl(Entity):
                            """
                            ACLs configured on the interface
                            
                            .. attribute:: inbound
                            
                            	ACL applied to incoming packets
                            	**type**\: str
                            
                            .. attribute:: outbound
                            
                            	ACL applied to outgoing packets
                            	**type**\: str
                            
                            .. attribute:: common_in_bound
                            
                            	Common ACL applied to incoming packets
                            	**type**\: str
                            
                            .. attribute:: common_out_bound
                            
                            	Common ACL applied to outgoing packets
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2017-08-23'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl, self).__init__()

                                self.yang_name = "acl"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('inbound', (YLeaf(YType.str, 'inbound'), ['str'])),
                                    ('outbound', (YLeaf(YType.str, 'outbound'), ['str'])),
                                    ('common_in_bound', (YLeaf(YType.str, 'common-in-bound'), ['str'])),
                                    ('common_out_bound', (YLeaf(YType.str, 'common-out-bound'), ['str'])),
                                ])
                                self.inbound = None
                                self.outbound = None
                                self.common_in_bound = None
                                self.common_out_bound = None
                                self._segment_path = lambda: "acl"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl, ['inbound', 'outbound', 'common_in_bound', 'common_out_bound'], name, value)


                        class MultiAcl(Entity):
                            """
                            Multi ACLs configured on the interface
                            
                            .. attribute:: inbound
                            
                            	Inbound ACLs
                            	**type**\: list of  		 :py:class:`Inbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl.Inbound>`
                            
                            .. attribute:: outbound
                            
                            	Outbound ACLs
                            	**type**\: list of  		 :py:class:`Outbound <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl.Outbound>`
                            
                            .. attribute:: common
                            
                            	Common ACLs
                            	**type**\: list of  		 :py:class:`Common <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl.Common>`
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2017-08-23'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl, self).__init__()

                                self.yang_name = "multi-acl"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("inbound", ("inbound", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl.Inbound)), ("outbound", ("outbound", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl.Outbound)), ("common", ("common", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl.Common))])
                                self._leafs = OrderedDict()

                                self.inbound = YList(self)
                                self.outbound = YList(self)
                                self.common = YList(self)
                                self._segment_path = lambda: "multi-acl"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl, [], name, value)


                            class Inbound(Entity):
                                """
                                Inbound ACLs
                                
                                .. attribute:: entry
                                
                                	
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ipv4-ma-oper'
                                _revision = '2017-08-23'

                                def __init__(self):
                                    super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl.Inbound, self).__init__()

                                    self.yang_name = "inbound"
                                    self.yang_parent_name = "multi-acl"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('entry', (YLeaf(YType.str, 'entry'), ['str'])),
                                    ])
                                    self.entry = None
                                    self._segment_path = lambda: "inbound"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl.Inbound, ['entry'], name, value)


                            class Outbound(Entity):
                                """
                                Outbound ACLs
                                
                                .. attribute:: entry
                                
                                	
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ipv4-ma-oper'
                                _revision = '2017-08-23'

                                def __init__(self):
                                    super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl.Outbound, self).__init__()

                                    self.yang_name = "outbound"
                                    self.yang_parent_name = "multi-acl"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('entry', (YLeaf(YType.str, 'entry'), ['str'])),
                                    ])
                                    self.entry = None
                                    self._segment_path = lambda: "outbound"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl.Outbound, ['entry'], name, value)


                            class Common(Entity):
                                """
                                Common ACLs
                                
                                .. attribute:: entry
                                
                                	
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ipv4-ma-oper'
                                _revision = '2017-08-23'

                                def __init__(self):
                                    super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl.Common, self).__init__()

                                    self.yang_name = "common"
                                    self.yang_parent_name = "multi-acl"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('entry', (YLeaf(YType.str, 'entry'), ['str'])),
                                    ])
                                    self.entry = None
                                    self._segment_path = lambda: "common"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl.Common, ['entry'], name, value)


                        class HelperAddress(Entity):
                            """
                            Helper Addresses configured on the interface
                            
                            .. attribute:: address_array
                            
                            	Helper address
                            	**type**\: list of  		 :py:class:`AddressArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress.AddressArray>`
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2017-08-23'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress, self).__init__()

                                self.yang_name = "helper-address"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("address-array", ("address_array", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress.AddressArray))])
                                self._leafs = OrderedDict()

                                self.address_array = YList(self)
                                self._segment_path = lambda: "helper-address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress, [], name, value)


                            class AddressArray(Entity):
                                """
                                Helper address
                                
                                .. attribute:: entry
                                
                                	
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-ma-oper'
                                _revision = '2017-08-23'

                                def __init__(self):
                                    super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress.AddressArray, self).__init__()

                                    self.yang_name = "address-array"
                                    self.yang_parent_name = "helper-address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('entry', (YLeaf(YType.str, 'entry'), ['str'])),
                                    ])
                                    self.entry = None
                                    self._segment_path = lambda: "address-array"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress.AddressArray, ['entry'], name, value)


                        class Rpf(Entity):
                            """
                            RPF config on the interface
                            
                            .. attribute:: enable
                            
                            	Enable RPF config
                            	**type**\: bool
                            
                            .. attribute:: allow_default_route
                            
                            	Allow Default Route
                            	**type**\: bool
                            
                            .. attribute:: allow_self_ping
                            
                            	Allow Self Ping
                            	**type**\: bool
                            
                            .. attribute:: mode
                            
                            	RPF Mode (loose/strict)
                            	**type**\:  :py:class:`RpfMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper.RpfMode>`
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2017-08-23'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf, self).__init__()

                                self.yang_name = "rpf"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                    ('allow_default_route', (YLeaf(YType.boolean, 'allow-default-route'), ['bool'])),
                                    ('allow_self_ping', (YLeaf(YType.boolean, 'allow-self-ping'), ['bool'])),
                                    ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper', 'RpfMode', '')])),
                                ])
                                self.enable = None
                                self.allow_default_route = None
                                self.allow_self_ping = None
                                self.mode = None
                                self._segment_path = lambda: "rpf"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf, ['enable', 'allow_default_route', 'allow_self_ping', 'mode'], name, value)


                        class BgpPa(Entity):
                            """
                            BGP PA config on the interface
                            
                            .. attribute:: input
                            
                            	BGP PA input config
                            	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input>`
                            
                            .. attribute:: output
                            
                            	BGP PA output config
                            	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output>`
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2017-08-23'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa, self).__init__()

                                self.yang_name = "bgp-pa"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("input", ("input", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input)), ("output", ("output", Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output))])
                                self._leafs = OrderedDict()

                                self.input = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input()
                                self.input.parent = self
                                self._children_name_map["input"] = "input"

                                self.output = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output()
                                self.output.parent = self
                                self._children_name_map["output"] = "output"
                                self._segment_path = lambda: "bgp-pa"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa, [], name, value)


                            class Input(Entity):
                                """
                                BGP PA input config
                                
                                .. attribute:: enable
                                
                                	Enable BGP PA for ingress/egress
                                	**type**\: bool
                                
                                .. attribute:: source
                                
                                	Enable source accouting
                                	**type**\: bool
                                
                                .. attribute:: destination
                                
                                	Enable destination accouting
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'ipv4-ma-oper'
                                _revision = '2017-08-23'

                                def __init__(self):
                                    super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input, self).__init__()

                                    self.yang_name = "input"
                                    self.yang_parent_name = "bgp-pa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                        ('source', (YLeaf(YType.boolean, 'source'), ['bool'])),
                                        ('destination', (YLeaf(YType.boolean, 'destination'), ['bool'])),
                                    ])
                                    self.enable = None
                                    self.source = None
                                    self.destination = None
                                    self._segment_path = lambda: "input"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input, ['enable', 'source', 'destination'], name, value)


                            class Output(Entity):
                                """
                                BGP PA output config
                                
                                .. attribute:: enable
                                
                                	Enable BGP PA for ingress/egress
                                	**type**\: bool
                                
                                .. attribute:: source
                                
                                	Enable source accouting
                                	**type**\: bool
                                
                                .. attribute:: destination
                                
                                	Enable destination accouting
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'ipv4-ma-oper'
                                _revision = '2017-08-23'

                                def __init__(self):
                                    super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output, self).__init__()

                                    self.yang_name = "output"
                                    self.yang_parent_name = "bgp-pa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                        ('source', (YLeaf(YType.boolean, 'source'), ['bool'])),
                                        ('destination', (YLeaf(YType.boolean, 'destination'), ['bool'])),
                                    ])
                                    self.enable = None
                                    self.source = None
                                    self.destination = None
                                    self._segment_path = lambda: "output"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output, ['enable', 'source', 'destination'], name, value)


                        class PubUtime(Entity):
                            """
                            Address Publish Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2017-08-23'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.PubUtime, self).__init__()

                                self.yang_name = "pub-utime"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict()
                                self._segment_path = lambda: "pub-utime"
                                self._is_frozen = True


                        class IdbUtime(Entity):
                            """
                            IDB Create Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2017-08-23'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.IdbUtime, self).__init__()

                                self.yang_name = "idb-utime"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict()
                                self._segment_path = lambda: "idb-utime"
                                self._is_frozen = True


                        class CapsUtime(Entity):
                            """
                            CAPS Add Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2017-08-23'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.CapsUtime, self).__init__()

                                self.yang_name = "caps-utime"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict()
                                self._segment_path = lambda: "caps-utime"
                                self._is_frozen = True


                        class FwdEnUtime(Entity):
                            """
                            FWD ENABLE Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2017-08-23'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdEnUtime, self).__init__()

                                self.yang_name = "fwd-en-utime"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict()
                                self._segment_path = lambda: "fwd-en-utime"
                                self._is_frozen = True


                        class FwdDisUtime(Entity):
                            """
                            FWD DISABLE Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2017-08-23'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdDisUtime, self).__init__()

                                self.yang_name = "fwd-dis-utime"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict()
                                self._segment_path = lambda: "fwd-dis-utime"
                                self._is_frozen = True


                        class MulticastGroup(Entity):
                            """
                            Multicast groups joined on the interface
                            
                            .. attribute:: group_address
                            
                            	Address of multicast group
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2017-08-23'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MulticastGroup, self).__init__()

                                self.yang_name = "multicast-group"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_address', (YLeaf(YType.str, 'group-address'), ['str'])),
                                ])
                                self.group_address = None
                                self._segment_path = lambda: "multicast-group"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MulticastGroup, ['group_address'], name, value)


                        class SecondaryAddress(Entity):
                            """
                            Secondary addresses on the interface
                            
                            .. attribute:: address
                            
                            	Address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length
                            
                            	Prefix length of address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: route_tag
                            
                            	Route Tag associated with this address (0 = no tag)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2017-08-23'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.SecondaryAddress, self).__init__()

                                self.yang_name = "secondary-address"
                                self.yang_parent_name = "detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                    ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                    ('route_tag', (YLeaf(YType.uint32, 'route-tag'), ['int'])),
                                ])
                                self.address = None
                                self.prefix_length = None
                                self.route_tag = None
                                self._segment_path = lambda: "secondary-address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.SecondaryAddress, ['address', 'prefix_length', 'route_tag'], name, value)


                    class Brief(Entity):
                        """
                        Brief IPv4 network operational data for an
                        interface
                        
                        .. attribute:: primary_address
                        
                        	Primary address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_id
                        
                        	VRF ID of the interface
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vrf_name
                        
                        	VRF name of the interface
                        	**type**\: str
                        
                        .. attribute:: line_state
                        
                        	Line state of the interface
                        	**type**\:  :py:class:`Ipv4MaOperLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper.Ipv4MaOperLineState>`
                        
                        

                        """

                        _prefix = 'ipv4-ma-oper'
                        _revision = '2017-08-23'

                        def __init__(self):
                            super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief, self).__init__()

                            self.yang_name = "brief"
                            self.yang_parent_name = "vrf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('primary_address', (YLeaf(YType.str, 'primary-address'), ['str'])),
                                ('vrf_id', (YLeaf(YType.uint32, 'vrf-id'), ['int'])),
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                ('line_state', (YLeaf(YType.enumeration, 'line-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper', 'Ipv4MaOperLineState', '')])),
                            ])
                            self.primary_address = None
                            self.vrf_id = None
                            self.vrf_name = None
                            self.line_state = None
                            self._segment_path = lambda: "brief"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief, ['primary_address', 'vrf_id', 'vrf_name', 'line_state'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv4Network()
        return self._top_entity

