""" Cisco_IOS_XR_ppp_ea_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ppp\-ea package operational data.

This module contains definitions
for the following management objects\:
  pppea\: PPPEA operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class PppEaAdjState(Enum):
    """
    PppEaAdjState (Enum Class)

    Ppp ea adj state

    .. data:: ppp_ea_adj_state_not_installed = 0

    	Ajacency not installed in AIB

    .. data:: ppp_ea_adj_state_installed = 1

    	Adjacency installed in AIB

    """

    ppp_ea_adj_state_not_installed = Enum.YLeaf(0, "ppp-ea-adj-state-not-installed")

    ppp_ea_adj_state_installed = Enum.YLeaf(1, "ppp-ea-adj-state-installed")



class Pppea(Entity):
    """
    PPPEA operational data
    
    .. attribute:: nodes
    
    	Per node PPPEA operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.Pppea.Nodes>`
    
    

    """

    _prefix = 'ppp-ea-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Pppea, self).__init__()
        self._top_entity = None

        self.yang_name = "pppea"
        self.yang_parent_name = "Cisco-IOS-XR-ppp-ea-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Pppea.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Pppea.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-ppp-ea-oper:pppea"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Pppea, [], name, value)


    class Nodes(Entity):
        """
        Per node PPPEA operational data
        
        .. attribute:: node
        
        	The PPPEA operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.Pppea.Nodes.Node>`
        
        

        """

        _prefix = 'ppp-ea-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Pppea.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "pppea"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Pppea.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ppp-ea-oper:pppea/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pppea.Nodes, [], name, value)


        class Node(Entity):
            """
            The PPPEA operational data for a particular
            node
            
            .. attribute:: node_name  (key)
            
            	The identifier for the node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: ea_interface_names
            
            	Show interface related information from the PPP EA
            	**type**\:  :py:class:`EaInterfaceNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.Pppea.Nodes.Node.EaInterfaceNames>`
            
            

            """

            _prefix = 'ppp-ea-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Pppea.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("ea-interface-names", ("ea_interface_names", Pppea.Nodes.Node.EaInterfaceNames))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.ea_interface_names = Pppea.Nodes.Node.EaInterfaceNames()
                self.ea_interface_names.parent = self
                self._children_name_map["ea_interface_names"] = "ea-interface-names"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ppp-ea-oper:pppea/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pppea.Nodes.Node, ['node_name'], name, value)


            class EaInterfaceNames(Entity):
                """
                Show interface related information from the
                PPP EA
                
                .. attribute:: ea_interface_name
                
                	Interface name
                	**type**\: list of  		 :py:class:`EaInterfaceName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.Pppea.Nodes.Node.EaInterfaceNames.EaInterfaceName>`
                
                

                """

                _prefix = 'ppp-ea-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Pppea.Nodes.Node.EaInterfaceNames, self).__init__()

                    self.yang_name = "ea-interface-names"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ea-interface-name", ("ea_interface_name", Pppea.Nodes.Node.EaInterfaceNames.EaInterfaceName))])
                    self._leafs = OrderedDict()

                    self.ea_interface_name = YList(self)
                    self._segment_path = lambda: "ea-interface-names"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pppea.Nodes.Node.EaInterfaceNames, [], name, value)


                class EaInterfaceName(Entity):
                    """
                    Interface name
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface running PPPEA
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: is_lcp_running
                    
                    	TRUE if LCP is running in the dataplane for the interface
                    	**type**\: bool
                    
                    .. attribute:: is_ipcp_running
                    
                    	TRUE if IPCP is running in the dataplane for the interface
                    	**type**\: bool
                    
                    .. attribute:: is_ipv6cp_running
                    
                    	TRUE if IPV6CP is running in the dataplane for the interface
                    	**type**\: bool
                    
                    .. attribute:: is_mplscp_running
                    
                    	TRUE if MPLSCP is running in the dataplane for the interface
                    	**type**\: bool
                    
                    .. attribute:: local_mtu
                    
                    	Local interface MTU
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: local_mrru
                    
                    	Local MRRU
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: peer_mrru
                    
                    	Peer MRRU
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: local_magic
                    
                    	Local magic number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_magic
                    
                    	Peer magic number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_mcmp_classes
                    
                    	Local number of MCMP Suspension classes
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: peer_mcmp_classes
                    
                    	Peer number of MCMP Suspension classes
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: echo_request_interval
                    
                    	Echo\-Request interval
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: echo_request_retry_count
                    
                    	Echo\-Request retry count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_multilink_bundle
                    
                    	TRUE if this is a Multilink bundle interface
                    	**type**\: bool
                    
                    .. attribute:: synchronized
                    
                    	MA synchronization
                    	**type**\: bool
                    
                    .. attribute:: forwarding_enabled
                    
                    	Forwarding State
                    	**type**\: bool
                    
                    .. attribute:: multilink_interface
                    
                    	Multilink interface that this interface is a member of, if any
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: l2_tunnel_enabled
                    
                    	L2 Tunnel State
                    	**type**\: bool
                    
                    .. attribute:: l2_provisioned
                    
                    	L2 Provisioned State
                    	**type**\: bool
                    
                    .. attribute:: l2ip_interworking_enabled
                    
                    	L2 IP Interworking State
                    	**type**\: bool
                    
                    .. attribute:: is_vpdn_tunneled
                    
                    	Is VPDN tunneled
                    	**type**\: bool
                    
                    .. attribute:: xconnect_id
                    
                    	XConnect ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: parent_interface_handle
                    
                    	Parent Interface Handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: vrf_table_id
                    
                    	IPCP VRF Table ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv6vrf_table_id
                    
                    	IPv6CP VRF Table ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: l2_adjacency_state
                    
                    	L2 adjacency state
                    	**type**\:  :py:class:`PppEaAdjState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjState>`
                    
                    .. attribute:: l2ip_interworking_adjacency_state
                    
                    	L2 IP Interworking adjacency state
                    	**type**\:  :py:class:`PppEaAdjState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjState>`
                    
                    .. attribute:: lac_adjacency_state
                    
                    	LAC adjacency state
                    	**type**\:  :py:class:`PppEaAdjState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjState>`
                    
                    .. attribute:: interface_adjacency_state
                    
                    	Interface adjacency state
                    	**type**\:  :py:class:`PppEaAdjState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjState>`
                    
                    .. attribute:: ipv4_adjacency_state
                    
                    	Ipv4 adjacency state
                    	**type**\:  :py:class:`PppEaAdjState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjState>`
                    
                    .. attribute:: ipv6_adjacency_state
                    
                    	IPv6 adjacency state
                    	**type**\:  :py:class:`PppEaAdjState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjState>`
                    
                    .. attribute:: mpls_adjacency_state
                    
                    	MPLS adjacency state
                    	**type**\:  :py:class:`PppEaAdjState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjState>`
                    
                    

                    """

                    _prefix = 'ppp-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppea.Nodes.Node.EaInterfaceNames.EaInterfaceName, self).__init__()

                        self.yang_name = "ea-interface-name"
                        self.yang_parent_name = "ea-interface-names"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('is_lcp_running', (YLeaf(YType.boolean, 'is-lcp-running'), ['bool'])),
                            ('is_ipcp_running', (YLeaf(YType.boolean, 'is-ipcp-running'), ['bool'])),
                            ('is_ipv6cp_running', (YLeaf(YType.boolean, 'is-ipv6cp-running'), ['bool'])),
                            ('is_mplscp_running', (YLeaf(YType.boolean, 'is-mplscp-running'), ['bool'])),
                            ('local_mtu', (YLeaf(YType.uint16, 'local-mtu'), ['int'])),
                            ('local_mrru', (YLeaf(YType.uint16, 'local-mrru'), ['int'])),
                            ('peer_mrru', (YLeaf(YType.uint16, 'peer-mrru'), ['int'])),
                            ('local_magic', (YLeaf(YType.uint32, 'local-magic'), ['int'])),
                            ('peer_magic', (YLeaf(YType.uint32, 'peer-magic'), ['int'])),
                            ('local_mcmp_classes', (YLeaf(YType.uint8, 'local-mcmp-classes'), ['int'])),
                            ('peer_mcmp_classes', (YLeaf(YType.uint8, 'peer-mcmp-classes'), ['int'])),
                            ('echo_request_interval', (YLeaf(YType.uint32, 'echo-request-interval'), ['int'])),
                            ('echo_request_retry_count', (YLeaf(YType.uint32, 'echo-request-retry-count'), ['int'])),
                            ('is_multilink_bundle', (YLeaf(YType.boolean, 'is-multilink-bundle'), ['bool'])),
                            ('synchronized', (YLeaf(YType.boolean, 'synchronized'), ['bool'])),
                            ('forwarding_enabled', (YLeaf(YType.boolean, 'forwarding-enabled'), ['bool'])),
                            ('multilink_interface', (YLeaf(YType.str, 'multilink-interface'), ['str'])),
                            ('l2_tunnel_enabled', (YLeaf(YType.boolean, 'l2-tunnel-enabled'), ['bool'])),
                            ('l2_provisioned', (YLeaf(YType.boolean, 'l2-provisioned'), ['bool'])),
                            ('l2ip_interworking_enabled', (YLeaf(YType.boolean, 'l2ip-interworking-enabled'), ['bool'])),
                            ('is_vpdn_tunneled', (YLeaf(YType.boolean, 'is-vpdn-tunneled'), ['bool'])),
                            ('xconnect_id', (YLeaf(YType.uint32, 'xconnect-id'), ['int'])),
                            ('parent_interface_handle', (YLeaf(YType.str, 'parent-interface-handle'), ['str'])),
                            ('vrf_table_id', (YLeaf(YType.uint32, 'vrf-table-id'), ['int'])),
                            ('ipv6vrf_table_id', (YLeaf(YType.uint32, 'ipv6vrf-table-id'), ['int'])),
                            ('l2_adjacency_state', (YLeaf(YType.enumeration, 'l2-adjacency-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'PppEaAdjState', '')])),
                            ('l2ip_interworking_adjacency_state', (YLeaf(YType.enumeration, 'l2ip-interworking-adjacency-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'PppEaAdjState', '')])),
                            ('lac_adjacency_state', (YLeaf(YType.enumeration, 'lac-adjacency-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'PppEaAdjState', '')])),
                            ('interface_adjacency_state', (YLeaf(YType.enumeration, 'interface-adjacency-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'PppEaAdjState', '')])),
                            ('ipv4_adjacency_state', (YLeaf(YType.enumeration, 'ipv4-adjacency-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'PppEaAdjState', '')])),
                            ('ipv6_adjacency_state', (YLeaf(YType.enumeration, 'ipv6-adjacency-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'PppEaAdjState', '')])),
                            ('mpls_adjacency_state', (YLeaf(YType.enumeration, 'mpls-adjacency-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper', 'PppEaAdjState', '')])),
                        ])
                        self.interface_name = None
                        self.interface = None
                        self.is_lcp_running = None
                        self.is_ipcp_running = None
                        self.is_ipv6cp_running = None
                        self.is_mplscp_running = None
                        self.local_mtu = None
                        self.local_mrru = None
                        self.peer_mrru = None
                        self.local_magic = None
                        self.peer_magic = None
                        self.local_mcmp_classes = None
                        self.peer_mcmp_classes = None
                        self.echo_request_interval = None
                        self.echo_request_retry_count = None
                        self.is_multilink_bundle = None
                        self.synchronized = None
                        self.forwarding_enabled = None
                        self.multilink_interface = None
                        self.l2_tunnel_enabled = None
                        self.l2_provisioned = None
                        self.l2ip_interworking_enabled = None
                        self.is_vpdn_tunneled = None
                        self.xconnect_id = None
                        self.parent_interface_handle = None
                        self.vrf_table_id = None
                        self.ipv6vrf_table_id = None
                        self.l2_adjacency_state = None
                        self.l2ip_interworking_adjacency_state = None
                        self.lac_adjacency_state = None
                        self.interface_adjacency_state = None
                        self.ipv4_adjacency_state = None
                        self.ipv6_adjacency_state = None
                        self.mpls_adjacency_state = None
                        self._segment_path = lambda: "ea-interface-name" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppea.Nodes.Node.EaInterfaceNames.EaInterfaceName, ['interface_name', u'interface', u'is_lcp_running', u'is_ipcp_running', u'is_ipv6cp_running', u'is_mplscp_running', u'local_mtu', u'local_mrru', u'peer_mrru', u'local_magic', u'peer_magic', u'local_mcmp_classes', u'peer_mcmp_classes', u'echo_request_interval', u'echo_request_retry_count', u'is_multilink_bundle', u'synchronized', u'forwarding_enabled', u'multilink_interface', u'l2_tunnel_enabled', u'l2_provisioned', u'l2ip_interworking_enabled', u'is_vpdn_tunneled', u'xconnect_id', u'parent_interface_handle', u'vrf_table_id', u'ipv6vrf_table_id', u'l2_adjacency_state', u'l2ip_interworking_adjacency_state', u'lac_adjacency_state', u'interface_adjacency_state', u'ipv4_adjacency_state', u'ipv6_adjacency_state', u'mpls_adjacency_state'], name, value)

    def clone_ptr(self):
        self._top_entity = Pppea()
        return self._top_entity

