""" Cisco_IOS_XR_ppp_ea_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ppp\-ea package operational data.

This module contains definitions
for the following management objects\:
  pppea\: PPPEA operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class PppEaAdjState(Enum):
    """
    PppEaAdjState

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
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.Pppea.Nodes>`
    
    

    """

    _prefix = 'ppp-ea-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Pppea, self).__init__()
        self._top_entity = None

        self.yang_name = "pppea"
        self.yang_parent_name = "Cisco-IOS-XR-ppp-ea-oper"

        self.nodes = Pppea.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Per node PPPEA operational data
        
        .. attribute:: node
        
        	The PPPEA operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.Pppea.Nodes.Node>`
        
        

        """

        _prefix = 'ppp-ea-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Pppea.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "pppea"

            self.node = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Pppea.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Pppea.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            The PPPEA operational data for a particular
            node
            
            .. attribute:: node_name  <key>
            
            	The identifier for the node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: ea_interface_names
            
            	Show interface related information from the PPP EA
            	**type**\:   :py:class:`EaInterfaceNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.Pppea.Nodes.Node.EaInterfaceNames>`
            
            

            """

            _prefix = 'ppp-ea-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Pppea.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.ea_interface_names = Pppea.Nodes.Node.EaInterfaceNames()
                self.ea_interface_names.parent = self
                self._children_name_map["ea_interface_names"] = "ea-interface-names"
                self._children_yang_names.add("ea-interface-names")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Pppea.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Pppea.Nodes.Node, self).__setattr__(name, value)


            class EaInterfaceNames(Entity):
                """
                Show interface related information from the
                PPP EA
                
                .. attribute:: ea_interface_name
                
                	Interface name
                	**type**\: list of    :py:class:`EaInterfaceName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.Pppea.Nodes.Node.EaInterfaceNames.EaInterfaceName>`
                
                

                """

                _prefix = 'ppp-ea-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Pppea.Nodes.Node.EaInterfaceNames, self).__init__()

                    self.yang_name = "ea-interface-names"
                    self.yang_parent_name = "node"

                    self.ea_interface_name = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Pppea.Nodes.Node.EaInterfaceNames, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Pppea.Nodes.Node.EaInterfaceNames, self).__setattr__(name, value)


                class EaInterfaceName(Entity):
                    """
                    Interface name
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface running PPPEA
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: echo_request_interval
                    
                    	Echo\-Request interval
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: echo_request_retry_count
                    
                    	Echo\-Request retry count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: forwarding_enabled
                    
                    	Forwarding State
                    	**type**\:  bool
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface_adjacency_state
                    
                    	Interface adjacency state
                    	**type**\:   :py:class:`PppEaAdjState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjState>`
                    
                    .. attribute:: ipv4_adjacency_state
                    
                    	Ipv4 adjacency state
                    	**type**\:   :py:class:`PppEaAdjState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjState>`
                    
                    .. attribute:: ipv6_adjacency_state
                    
                    	IPv6 adjacency state
                    	**type**\:   :py:class:`PppEaAdjState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjState>`
                    
                    .. attribute:: ipv6vrf_table_id
                    
                    	IPv6CP VRF Table ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_ipcp_running
                    
                    	TRUE if IPCP is running in the dataplane for the interface
                    	**type**\:  bool
                    
                    .. attribute:: is_ipv6cp_running
                    
                    	TRUE if IPV6CP is running in the dataplane for the interface
                    	**type**\:  bool
                    
                    .. attribute:: is_lcp_running
                    
                    	TRUE if LCP is running in the dataplane for the interface
                    	**type**\:  bool
                    
                    .. attribute:: is_mplscp_running
                    
                    	TRUE if MPLSCP is running in the dataplane for the interface
                    	**type**\:  bool
                    
                    .. attribute:: is_multilink_bundle
                    
                    	TRUE if this is a Multilink bundle interface
                    	**type**\:  bool
                    
                    .. attribute:: is_vpdn_tunneled
                    
                    	Is VPDN tunneled
                    	**type**\:  bool
                    
                    .. attribute:: l2_adjacency_state
                    
                    	L2 adjacency state
                    	**type**\:   :py:class:`PppEaAdjState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjState>`
                    
                    .. attribute:: l2_provisioned
                    
                    	L2 Provisioned State
                    	**type**\:  bool
                    
                    .. attribute:: l2_tunnel_enabled
                    
                    	L2 Tunnel State
                    	**type**\:  bool
                    
                    .. attribute:: l2ip_interworking_adjacency_state
                    
                    	L2 IP Interworking adjacency state
                    	**type**\:   :py:class:`PppEaAdjState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjState>`
                    
                    .. attribute:: l2ip_interworking_enabled
                    
                    	L2 IP Interworking State
                    	**type**\:  bool
                    
                    .. attribute:: lac_adjacency_state
                    
                    	LAC adjacency state
                    	**type**\:   :py:class:`PppEaAdjState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjState>`
                    
                    .. attribute:: local_magic
                    
                    	Local magic number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_mcmp_classes
                    
                    	Local number of MCMP Suspension classes
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: local_mrru
                    
                    	Local MRRU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: local_mtu
                    
                    	Local interface MTU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: mpls_adjacency_state
                    
                    	MPLS adjacency state
                    	**type**\:   :py:class:`PppEaAdjState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ea_oper.PppEaAdjState>`
                    
                    .. attribute:: multilink_interface
                    
                    	Multilink interface that this interface is a member of, if any
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: parent_interface_handle
                    
                    	Parent Interface Handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: peer_magic
                    
                    	Peer magic number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_mcmp_classes
                    
                    	Peer number of MCMP Suspension classes
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: peer_mrru
                    
                    	Peer MRRU
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: synchronized
                    
                    	MA synchronization
                    	**type**\:  bool
                    
                    .. attribute:: vrf_table_id
                    
                    	IPCP VRF Table ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: xconnect_id
                    
                    	XConnect ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ppp-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppea.Nodes.Node.EaInterfaceNames.EaInterfaceName, self).__init__()

                        self.yang_name = "ea-interface-name"
                        self.yang_parent_name = "ea-interface-names"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.echo_request_interval = YLeaf(YType.uint32, "echo-request-interval")

                        self.echo_request_retry_count = YLeaf(YType.uint32, "echo-request-retry-count")

                        self.forwarding_enabled = YLeaf(YType.boolean, "forwarding-enabled")

                        self.interface = YLeaf(YType.str, "interface")

                        self.interface_adjacency_state = YLeaf(YType.enumeration, "interface-adjacency-state")

                        self.ipv4_adjacency_state = YLeaf(YType.enumeration, "ipv4-adjacency-state")

                        self.ipv6_adjacency_state = YLeaf(YType.enumeration, "ipv6-adjacency-state")

                        self.ipv6vrf_table_id = YLeaf(YType.uint32, "ipv6vrf-table-id")

                        self.is_ipcp_running = YLeaf(YType.boolean, "is-ipcp-running")

                        self.is_ipv6cp_running = YLeaf(YType.boolean, "is-ipv6cp-running")

                        self.is_lcp_running = YLeaf(YType.boolean, "is-lcp-running")

                        self.is_mplscp_running = YLeaf(YType.boolean, "is-mplscp-running")

                        self.is_multilink_bundle = YLeaf(YType.boolean, "is-multilink-bundle")

                        self.is_vpdn_tunneled = YLeaf(YType.boolean, "is-vpdn-tunneled")

                        self.l2_adjacency_state = YLeaf(YType.enumeration, "l2-adjacency-state")

                        self.l2_provisioned = YLeaf(YType.boolean, "l2-provisioned")

                        self.l2_tunnel_enabled = YLeaf(YType.boolean, "l2-tunnel-enabled")

                        self.l2ip_interworking_adjacency_state = YLeaf(YType.enumeration, "l2ip-interworking-adjacency-state")

                        self.l2ip_interworking_enabled = YLeaf(YType.boolean, "l2ip-interworking-enabled")

                        self.lac_adjacency_state = YLeaf(YType.enumeration, "lac-adjacency-state")

                        self.local_magic = YLeaf(YType.uint32, "local-magic")

                        self.local_mcmp_classes = YLeaf(YType.uint8, "local-mcmp-classes")

                        self.local_mrru = YLeaf(YType.uint16, "local-mrru")

                        self.local_mtu = YLeaf(YType.uint16, "local-mtu")

                        self.mpls_adjacency_state = YLeaf(YType.enumeration, "mpls-adjacency-state")

                        self.multilink_interface = YLeaf(YType.str, "multilink-interface")

                        self.parent_interface_handle = YLeaf(YType.str, "parent-interface-handle")

                        self.peer_magic = YLeaf(YType.uint32, "peer-magic")

                        self.peer_mcmp_classes = YLeaf(YType.uint8, "peer-mcmp-classes")

                        self.peer_mrru = YLeaf(YType.uint16, "peer-mrru")

                        self.synchronized = YLeaf(YType.boolean, "synchronized")

                        self.vrf_table_id = YLeaf(YType.uint32, "vrf-table-id")

                        self.xconnect_id = YLeaf(YType.uint32, "xconnect-id")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name",
                                        "echo_request_interval",
                                        "echo_request_retry_count",
                                        "forwarding_enabled",
                                        "interface",
                                        "interface_adjacency_state",
                                        "ipv4_adjacency_state",
                                        "ipv6_adjacency_state",
                                        "ipv6vrf_table_id",
                                        "is_ipcp_running",
                                        "is_ipv6cp_running",
                                        "is_lcp_running",
                                        "is_mplscp_running",
                                        "is_multilink_bundle",
                                        "is_vpdn_tunneled",
                                        "l2_adjacency_state",
                                        "l2_provisioned",
                                        "l2_tunnel_enabled",
                                        "l2ip_interworking_adjacency_state",
                                        "l2ip_interworking_enabled",
                                        "lac_adjacency_state",
                                        "local_magic",
                                        "local_mcmp_classes",
                                        "local_mrru",
                                        "local_mtu",
                                        "mpls_adjacency_state",
                                        "multilink_interface",
                                        "parent_interface_handle",
                                        "peer_magic",
                                        "peer_mcmp_classes",
                                        "peer_mrru",
                                        "synchronized",
                                        "vrf_table_id",
                                        "xconnect_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pppea.Nodes.Node.EaInterfaceNames.EaInterfaceName, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pppea.Nodes.Node.EaInterfaceNames.EaInterfaceName, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.echo_request_interval.is_set or
                            self.echo_request_retry_count.is_set or
                            self.forwarding_enabled.is_set or
                            self.interface.is_set or
                            self.interface_adjacency_state.is_set or
                            self.ipv4_adjacency_state.is_set or
                            self.ipv6_adjacency_state.is_set or
                            self.ipv6vrf_table_id.is_set or
                            self.is_ipcp_running.is_set or
                            self.is_ipv6cp_running.is_set or
                            self.is_lcp_running.is_set or
                            self.is_mplscp_running.is_set or
                            self.is_multilink_bundle.is_set or
                            self.is_vpdn_tunneled.is_set or
                            self.l2_adjacency_state.is_set or
                            self.l2_provisioned.is_set or
                            self.l2_tunnel_enabled.is_set or
                            self.l2ip_interworking_adjacency_state.is_set or
                            self.l2ip_interworking_enabled.is_set or
                            self.lac_adjacency_state.is_set or
                            self.local_magic.is_set or
                            self.local_mcmp_classes.is_set or
                            self.local_mrru.is_set or
                            self.local_mtu.is_set or
                            self.mpls_adjacency_state.is_set or
                            self.multilink_interface.is_set or
                            self.parent_interface_handle.is_set or
                            self.peer_magic.is_set or
                            self.peer_mcmp_classes.is_set or
                            self.peer_mrru.is_set or
                            self.synchronized.is_set or
                            self.vrf_table_id.is_set or
                            self.xconnect_id.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.echo_request_interval.yfilter != YFilter.not_set or
                            self.echo_request_retry_count.yfilter != YFilter.not_set or
                            self.forwarding_enabled.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.interface_adjacency_state.yfilter != YFilter.not_set or
                            self.ipv4_adjacency_state.yfilter != YFilter.not_set or
                            self.ipv6_adjacency_state.yfilter != YFilter.not_set or
                            self.ipv6vrf_table_id.yfilter != YFilter.not_set or
                            self.is_ipcp_running.yfilter != YFilter.not_set or
                            self.is_ipv6cp_running.yfilter != YFilter.not_set or
                            self.is_lcp_running.yfilter != YFilter.not_set or
                            self.is_mplscp_running.yfilter != YFilter.not_set or
                            self.is_multilink_bundle.yfilter != YFilter.not_set or
                            self.is_vpdn_tunneled.yfilter != YFilter.not_set or
                            self.l2_adjacency_state.yfilter != YFilter.not_set or
                            self.l2_provisioned.yfilter != YFilter.not_set or
                            self.l2_tunnel_enabled.yfilter != YFilter.not_set or
                            self.l2ip_interworking_adjacency_state.yfilter != YFilter.not_set or
                            self.l2ip_interworking_enabled.yfilter != YFilter.not_set or
                            self.lac_adjacency_state.yfilter != YFilter.not_set or
                            self.local_magic.yfilter != YFilter.not_set or
                            self.local_mcmp_classes.yfilter != YFilter.not_set or
                            self.local_mrru.yfilter != YFilter.not_set or
                            self.local_mtu.yfilter != YFilter.not_set or
                            self.mpls_adjacency_state.yfilter != YFilter.not_set or
                            self.multilink_interface.yfilter != YFilter.not_set or
                            self.parent_interface_handle.yfilter != YFilter.not_set or
                            self.peer_magic.yfilter != YFilter.not_set or
                            self.peer_mcmp_classes.yfilter != YFilter.not_set or
                            self.peer_mrru.yfilter != YFilter.not_set or
                            self.synchronized.yfilter != YFilter.not_set or
                            self.vrf_table_id.yfilter != YFilter.not_set or
                            self.xconnect_id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ea-interface-name" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.echo_request_interval.is_set or self.echo_request_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.echo_request_interval.get_name_leafdata())
                        if (self.echo_request_retry_count.is_set or self.echo_request_retry_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.echo_request_retry_count.get_name_leafdata())
                        if (self.forwarding_enabled.is_set or self.forwarding_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.forwarding_enabled.get_name_leafdata())
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.interface_adjacency_state.is_set or self.interface_adjacency_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_adjacency_state.get_name_leafdata())
                        if (self.ipv4_adjacency_state.is_set or self.ipv4_adjacency_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_adjacency_state.get_name_leafdata())
                        if (self.ipv6_adjacency_state.is_set or self.ipv6_adjacency_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_adjacency_state.get_name_leafdata())
                        if (self.ipv6vrf_table_id.is_set or self.ipv6vrf_table_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6vrf_table_id.get_name_leafdata())
                        if (self.is_ipcp_running.is_set or self.is_ipcp_running.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_ipcp_running.get_name_leafdata())
                        if (self.is_ipv6cp_running.is_set or self.is_ipv6cp_running.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_ipv6cp_running.get_name_leafdata())
                        if (self.is_lcp_running.is_set or self.is_lcp_running.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_lcp_running.get_name_leafdata())
                        if (self.is_mplscp_running.is_set or self.is_mplscp_running.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_mplscp_running.get_name_leafdata())
                        if (self.is_multilink_bundle.is_set or self.is_multilink_bundle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_multilink_bundle.get_name_leafdata())
                        if (self.is_vpdn_tunneled.is_set or self.is_vpdn_tunneled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_vpdn_tunneled.get_name_leafdata())
                        if (self.l2_adjacency_state.is_set or self.l2_adjacency_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.l2_adjacency_state.get_name_leafdata())
                        if (self.l2_provisioned.is_set or self.l2_provisioned.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.l2_provisioned.get_name_leafdata())
                        if (self.l2_tunnel_enabled.is_set or self.l2_tunnel_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.l2_tunnel_enabled.get_name_leafdata())
                        if (self.l2ip_interworking_adjacency_state.is_set or self.l2ip_interworking_adjacency_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.l2ip_interworking_adjacency_state.get_name_leafdata())
                        if (self.l2ip_interworking_enabled.is_set or self.l2ip_interworking_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.l2ip_interworking_enabled.get_name_leafdata())
                        if (self.lac_adjacency_state.is_set or self.lac_adjacency_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lac_adjacency_state.get_name_leafdata())
                        if (self.local_magic.is_set or self.local_magic.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_magic.get_name_leafdata())
                        if (self.local_mcmp_classes.is_set or self.local_mcmp_classes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_mcmp_classes.get_name_leafdata())
                        if (self.local_mrru.is_set or self.local_mrru.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_mrru.get_name_leafdata())
                        if (self.local_mtu.is_set or self.local_mtu.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_mtu.get_name_leafdata())
                        if (self.mpls_adjacency_state.is_set or self.mpls_adjacency_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mpls_adjacency_state.get_name_leafdata())
                        if (self.multilink_interface.is_set or self.multilink_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multilink_interface.get_name_leafdata())
                        if (self.parent_interface_handle.is_set or self.parent_interface_handle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.parent_interface_handle.get_name_leafdata())
                        if (self.peer_magic.is_set or self.peer_magic.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_magic.get_name_leafdata())
                        if (self.peer_mcmp_classes.is_set or self.peer_mcmp_classes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_mcmp_classes.get_name_leafdata())
                        if (self.peer_mrru.is_set or self.peer_mrru.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_mrru.get_name_leafdata())
                        if (self.synchronized.is_set or self.synchronized.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.synchronized.get_name_leafdata())
                        if (self.vrf_table_id.is_set or self.vrf_table_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_table_id.get_name_leafdata())
                        if (self.xconnect_id.is_set or self.xconnect_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.xconnect_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name" or name == "echo-request-interval" or name == "echo-request-retry-count" or name == "forwarding-enabled" or name == "interface" or name == "interface-adjacency-state" or name == "ipv4-adjacency-state" or name == "ipv6-adjacency-state" or name == "ipv6vrf-table-id" or name == "is-ipcp-running" or name == "is-ipv6cp-running" or name == "is-lcp-running" or name == "is-mplscp-running" or name == "is-multilink-bundle" or name == "is-vpdn-tunneled" or name == "l2-adjacency-state" or name == "l2-provisioned" or name == "l2-tunnel-enabled" or name == "l2ip-interworking-adjacency-state" or name == "l2ip-interworking-enabled" or name == "lac-adjacency-state" or name == "local-magic" or name == "local-mcmp-classes" or name == "local-mrru" or name == "local-mtu" or name == "mpls-adjacency-state" or name == "multilink-interface" or name == "parent-interface-handle" or name == "peer-magic" or name == "peer-mcmp-classes" or name == "peer-mrru" or name == "synchronized" or name == "vrf-table-id" or name == "xconnect-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "echo-request-interval"):
                            self.echo_request_interval = value
                            self.echo_request_interval.value_namespace = name_space
                            self.echo_request_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "echo-request-retry-count"):
                            self.echo_request_retry_count = value
                            self.echo_request_retry_count.value_namespace = name_space
                            self.echo_request_retry_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "forwarding-enabled"):
                            self.forwarding_enabled = value
                            self.forwarding_enabled.value_namespace = name_space
                            self.forwarding_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-adjacency-state"):
                            self.interface_adjacency_state = value
                            self.interface_adjacency_state.value_namespace = name_space
                            self.interface_adjacency_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4-adjacency-state"):
                            self.ipv4_adjacency_state = value
                            self.ipv4_adjacency_state.value_namespace = name_space
                            self.ipv4_adjacency_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-adjacency-state"):
                            self.ipv6_adjacency_state = value
                            self.ipv6_adjacency_state.value_namespace = name_space
                            self.ipv6_adjacency_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6vrf-table-id"):
                            self.ipv6vrf_table_id = value
                            self.ipv6vrf_table_id.value_namespace = name_space
                            self.ipv6vrf_table_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-ipcp-running"):
                            self.is_ipcp_running = value
                            self.is_ipcp_running.value_namespace = name_space
                            self.is_ipcp_running.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-ipv6cp-running"):
                            self.is_ipv6cp_running = value
                            self.is_ipv6cp_running.value_namespace = name_space
                            self.is_ipv6cp_running.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-lcp-running"):
                            self.is_lcp_running = value
                            self.is_lcp_running.value_namespace = name_space
                            self.is_lcp_running.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-mplscp-running"):
                            self.is_mplscp_running = value
                            self.is_mplscp_running.value_namespace = name_space
                            self.is_mplscp_running.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-multilink-bundle"):
                            self.is_multilink_bundle = value
                            self.is_multilink_bundle.value_namespace = name_space
                            self.is_multilink_bundle.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-vpdn-tunneled"):
                            self.is_vpdn_tunneled = value
                            self.is_vpdn_tunneled.value_namespace = name_space
                            self.is_vpdn_tunneled.value_namespace_prefix = name_space_prefix
                        if(value_path == "l2-adjacency-state"):
                            self.l2_adjacency_state = value
                            self.l2_adjacency_state.value_namespace = name_space
                            self.l2_adjacency_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "l2-provisioned"):
                            self.l2_provisioned = value
                            self.l2_provisioned.value_namespace = name_space
                            self.l2_provisioned.value_namespace_prefix = name_space_prefix
                        if(value_path == "l2-tunnel-enabled"):
                            self.l2_tunnel_enabled = value
                            self.l2_tunnel_enabled.value_namespace = name_space
                            self.l2_tunnel_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "l2ip-interworking-adjacency-state"):
                            self.l2ip_interworking_adjacency_state = value
                            self.l2ip_interworking_adjacency_state.value_namespace = name_space
                            self.l2ip_interworking_adjacency_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "l2ip-interworking-enabled"):
                            self.l2ip_interworking_enabled = value
                            self.l2ip_interworking_enabled.value_namespace = name_space
                            self.l2ip_interworking_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "lac-adjacency-state"):
                            self.lac_adjacency_state = value
                            self.lac_adjacency_state.value_namespace = name_space
                            self.lac_adjacency_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-magic"):
                            self.local_magic = value
                            self.local_magic.value_namespace = name_space
                            self.local_magic.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-mcmp-classes"):
                            self.local_mcmp_classes = value
                            self.local_mcmp_classes.value_namespace = name_space
                            self.local_mcmp_classes.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-mrru"):
                            self.local_mrru = value
                            self.local_mrru.value_namespace = name_space
                            self.local_mrru.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-mtu"):
                            self.local_mtu = value
                            self.local_mtu.value_namespace = name_space
                            self.local_mtu.value_namespace_prefix = name_space_prefix
                        if(value_path == "mpls-adjacency-state"):
                            self.mpls_adjacency_state = value
                            self.mpls_adjacency_state.value_namespace = name_space
                            self.mpls_adjacency_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "multilink-interface"):
                            self.multilink_interface = value
                            self.multilink_interface.value_namespace = name_space
                            self.multilink_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "parent-interface-handle"):
                            self.parent_interface_handle = value
                            self.parent_interface_handle.value_namespace = name_space
                            self.parent_interface_handle.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-magic"):
                            self.peer_magic = value
                            self.peer_magic.value_namespace = name_space
                            self.peer_magic.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-mcmp-classes"):
                            self.peer_mcmp_classes = value
                            self.peer_mcmp_classes.value_namespace = name_space
                            self.peer_mcmp_classes.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-mrru"):
                            self.peer_mrru = value
                            self.peer_mrru.value_namespace = name_space
                            self.peer_mrru.value_namespace_prefix = name_space_prefix
                        if(value_path == "synchronized"):
                            self.synchronized = value
                            self.synchronized.value_namespace = name_space
                            self.synchronized.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-table-id"):
                            self.vrf_table_id = value
                            self.vrf_table_id.value_namespace = name_space
                            self.vrf_table_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "xconnect-id"):
                            self.xconnect_id = value
                            self.xconnect_id.value_namespace = name_space
                            self.xconnect_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ea_interface_name:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ea_interface_name:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ea-interface-names" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ea-interface-name"):
                        for c in self.ea_interface_name:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Pppea.Nodes.Node.EaInterfaceNames.EaInterfaceName()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ea_interface_name.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ea-interface-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.ea_interface_names is not None and self.ea_interface_names.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.ea_interface_names is not None and self.ea_interface_names.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ppp-ea-oper:pppea/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ea-interface-names"):
                    if (self.ea_interface_names is None):
                        self.ea_interface_names = Pppea.Nodes.Node.EaInterfaceNames()
                        self.ea_interface_names.parent = self
                        self._children_name_map["ea_interface_names"] = "ea-interface-names"
                    return self.ea_interface_names

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ea-interface-names" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ppp-ea-oper:pppea/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Pppea.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ppp-ea-oper:pppea" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = Pppea.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Pppea()
        return self._top_entity

