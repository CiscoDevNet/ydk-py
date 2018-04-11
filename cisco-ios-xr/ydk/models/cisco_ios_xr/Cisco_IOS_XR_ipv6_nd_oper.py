""" Cisco_IOS_XR_ipv6_nd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-nd package operational data.

This module contains definitions
for the following management objects\:
  ipv6\-node\-discovery\: IPv6 node discovery operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ipv6NdBndlState(Enum):
    """
    Ipv6NdBndlState (Enum Class)

    IPv6 ND Bundle State

    .. data:: run = 0

    	Running state

    .. data:: error = 1

    	Error state

    .. data:: wait = 2

    	Wait state

    """

    run = Enum.YLeaf(0, "run")

    error = Enum.YLeaf(1, "error")

    wait = Enum.YLeaf(2, "wait")


class Ipv6NdMediaEncap(Enum):
    """
    Ipv6NdMediaEncap (Enum Class)

    IPv6 ND Media Encapsulation Type

    .. data:: none = 0

    	No encapsulation

    .. data:: arpa = 1

    	ARPA encapsulation

    .. data:: snap = 2

    	SNAP encapsulation

    .. data:: ieee802_1q = 3

    	802_1Q encapsulation

    .. data:: srp = 4

    	SRP encapsulation

    .. data:: srpa = 5

    	SRPA encapsulation

    .. data:: srpb = 6

    	SRPB encapsulation

    .. data:: ppp = 7

    	PPP encapsulation

    .. data:: hdlc = 8

    	HDLC encapsulation

    .. data:: chdlc = 9

    	CHDLC encapsulation

    .. data:: dot1q = 10

    	DOT1Q encapsulation

    .. data:: fr = 11

    	FR encapsulation

    .. data:: gre = 12

    	GRE encapsulation

    """

    none = Enum.YLeaf(0, "none")

    arpa = Enum.YLeaf(1, "arpa")

    snap = Enum.YLeaf(2, "snap")

    ieee802_1q = Enum.YLeaf(3, "ieee802-1q")

    srp = Enum.YLeaf(4, "srp")

    srpa = Enum.YLeaf(5, "srpa")

    srpb = Enum.YLeaf(6, "srpb")

    ppp = Enum.YLeaf(7, "ppp")

    hdlc = Enum.YLeaf(8, "hdlc")

    chdlc = Enum.YLeaf(9, "chdlc")

    dot1q = Enum.YLeaf(10, "dot1q")

    fr = Enum.YLeaf(11, "fr")

    gre = Enum.YLeaf(12, "gre")


class Ipv6NdNeighborOrigin(Enum):
    """
    Ipv6NdNeighborOrigin (Enum Class)

    IPv6 ND Neighbor Origin Type

    .. data:: other = 0

    	Other Address

    .. data:: static = 1

    	Static Address

    .. data:: dynamic = 2

    	Dynamic Address

    """

    other = Enum.YLeaf(0, "other")

    static = Enum.YLeaf(1, "static")

    dynamic = Enum.YLeaf(2, "dynamic")


class Ipv6NdShState(Enum):
    """
    Ipv6NdShState (Enum Class)

    IPv6 ND Neighbor Reachability State

    .. data:: incomplete = 0

    	Incomplete

    .. data:: reachable = 1

    	Reachable

    .. data:: stale = 2

    	Stale

    .. data:: glean = 3

    	Glean

    .. data:: delay = 4

    	Delay

    .. data:: probe = 5

    	Probe

    .. data:: delete = 6

    	Delete

    """

    incomplete = Enum.YLeaf(0, "incomplete")

    reachable = Enum.YLeaf(1, "reachable")

    stale = Enum.YLeaf(2, "stale")

    glean = Enum.YLeaf(3, "glean")

    delay = Enum.YLeaf(4, "delay")

    probe = Enum.YLeaf(5, "probe")

    delete = Enum.YLeaf(6, "delete")


class Ipv6NdShVrFlags(Enum):
    """
    Ipv6NdShVrFlags (Enum Class)

    IPv6 ND VR Entry Flags Type 

    .. data:: no_flags = 0

    	None

    .. data:: final_ra = 1

    	Final RA

    """

    no_flags = Enum.YLeaf(0, "no-flags")

    final_ra = Enum.YLeaf(1, "final-ra")


class Ipv6NdShVrState(Enum):
    """
    Ipv6NdShVrState (Enum Class)

    IPv6 ND VR Entry State Type 

    .. data:: deleted = 0

    	Delete

    .. data:: standby = 1

    	Standby

    .. data:: active = 2

    	Active

    """

    deleted = Enum.YLeaf(0, "deleted")

    standby = Enum.YLeaf(1, "standby")

    active = Enum.YLeaf(2, "active")



class Ipv6NodeDiscovery(Entity):
    """
    IPv6 node discovery operational data
    
    .. attribute:: nodes
    
    	IPv6 node discovery list of nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes>`
    
    

    """

    _prefix = 'ipv6-nd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ipv6NodeDiscovery, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6-node-discovery"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-nd-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", Ipv6NodeDiscovery.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = Ipv6NodeDiscovery.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-nd-oper:ipv6-node-discovery"


    class Nodes(Entity):
        """
        IPv6 node discovery list of nodes
        
        .. attribute:: node
        
        	IPv6 node discovery operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node>`
        
        

        """

        _prefix = 'ipv6-nd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv6NodeDiscovery.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ipv6-node-discovery"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", Ipv6NodeDiscovery.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-nd-oper:ipv6-node-discovery/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6NodeDiscovery.Nodes, [], name, value)


        class Node(Entity):
            """
            IPv6 node discovery operational data for a
            particular node
            
            .. attribute:: node_name  (key)
            
            	The node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: neighbor_interfaces
            
            	IPv6 node discovery list of neighbor interfaces
            	**type**\:  :py:class:`NeighborInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces>`
            
            .. attribute:: neighbor_summary
            
            	IPv6 Neighbor summary
            	**type**\:  :py:class:`NeighborSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary>`
            
            .. attribute:: bundle_nodes
            
            	IPv6 ND list of bundle nodes for a specific node
            	**type**\:  :py:class:`BundleNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleNodes>`
            
            .. attribute:: bundle_interfaces
            
            	IPv6 ND list of bundle interfaces for a specific node
            	**type**\:  :py:class:`BundleInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces>`
            
            .. attribute:: interfaces
            
            	IPv6 node discovery list of interfaces for a specific node
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.Interfaces>`
            
            .. attribute:: nd_virtual_routers
            
            	IPv6 ND virtual router information for a specific interface
            	**type**\:  :py:class:`NdVirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters>`
            
            .. attribute:: slaac_interfaces
            
            	IPv6 ND list of SLAAC MGMT interfaces for a specific node
            	**type**\:  :py:class:`SlaacInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces>`
            
            

            """

            _prefix = 'ipv6-nd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv6NodeDiscovery.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_container_classes = OrderedDict([("neighbor-interfaces", ("neighbor_interfaces", Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces)), ("neighbor-summary", ("neighbor_summary", Ipv6NodeDiscovery.Nodes.Node.NeighborSummary)), ("bundle-nodes", ("bundle_nodes", Ipv6NodeDiscovery.Nodes.Node.BundleNodes)), ("bundle-interfaces", ("bundle_interfaces", Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces)), ("interfaces", ("interfaces", Ipv6NodeDiscovery.Nodes.Node.Interfaces)), ("nd-virtual-routers", ("nd_virtual_routers", Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters)), ("slaac-interfaces", ("slaac_interfaces", Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                ])
                self.node_name = None

                self.neighbor_interfaces = Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces()
                self.neighbor_interfaces.parent = self
                self._children_name_map["neighbor_interfaces"] = "neighbor-interfaces"
                self._children_yang_names.add("neighbor-interfaces")

                self.neighbor_summary = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary()
                self.neighbor_summary.parent = self
                self._children_name_map["neighbor_summary"] = "neighbor-summary"
                self._children_yang_names.add("neighbor-summary")

                self.bundle_nodes = Ipv6NodeDiscovery.Nodes.Node.BundleNodes()
                self.bundle_nodes.parent = self
                self._children_name_map["bundle_nodes"] = "bundle-nodes"
                self._children_yang_names.add("bundle-nodes")

                self.bundle_interfaces = Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces()
                self.bundle_interfaces.parent = self
                self._children_name_map["bundle_interfaces"] = "bundle-interfaces"
                self._children_yang_names.add("bundle-interfaces")

                self.interfaces = Ipv6NodeDiscovery.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.nd_virtual_routers = Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters()
                self.nd_virtual_routers.parent = self
                self._children_name_map["nd_virtual_routers"] = "nd-virtual-routers"
                self._children_yang_names.add("nd-virtual-routers")

                self.slaac_interfaces = Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces()
                self.slaac_interfaces.parent = self
                self._children_name_map["slaac_interfaces"] = "slaac-interfaces"
                self._children_yang_names.add("slaac-interfaces")
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-nd-oper:ipv6-node-discovery/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node, ['node_name'], name, value)


            class NeighborInterfaces(Entity):
                """
                IPv6 node discovery list of neighbor
                interfaces
                
                .. attribute:: neighbor_interface
                
                	IPv6 node discovery neighbor interface
                	**type**\: list of  		 :py:class:`NeighborInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface>`
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces, self).__init__()

                    self.yang_name = "neighbor-interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("neighbor-interface", ("neighbor_interface", Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface))])
                    self._leafs = OrderedDict()

                    self.neighbor_interface = YList(self)
                    self._segment_path = lambda: "neighbor-interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces, [], name, value)


                class NeighborInterface(Entity):
                    """
                    IPv6 node discovery neighbor interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: host_addresses
                    
                    	IPv6 node discovery list of neighbor host addresses
                    	**type**\:  :py:class:`HostAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses>`
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface, self).__init__()

                        self.yang_name = "neighbor-interface"
                        self.yang_parent_name = "neighbor-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_container_classes = OrderedDict([("host-addresses", ("host_addresses", Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', YLeaf(YType.str, 'interface-name')),
                        ])
                        self.interface_name = None

                        self.host_addresses = Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses()
                        self.host_addresses.parent = self
                        self._children_name_map["host_addresses"] = "host-addresses"
                        self._children_yang_names.add("host-addresses")
                        self._segment_path = lambda: "neighbor-interface" + "[interface-name='" + str(self.interface_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface, ['interface_name'], name, value)


                    class HostAddresses(Entity):
                        """
                        IPv6 node discovery list of neighbor host
                        addresses
                        
                        .. attribute:: host_address
                        
                        	IPv6 Neighbor detailed information
                        	**type**\: list of  		 :py:class:`HostAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress>`
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses, self).__init__()

                            self.yang_name = "host-addresses"
                            self.yang_parent_name = "neighbor-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("host-address", ("host_address", Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress))])
                            self._leafs = OrderedDict()

                            self.host_address = YList(self)
                            self._segment_path = lambda: "host-addresses"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses, [], name, value)


                        class HostAddress(Entity):
                            """
                            IPv6 Neighbor detailed information
                            
                            .. attribute:: host_address  (key)
                            
                            	Host Address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: last_reached_time
                            
                            	Last time of reachability
                            	**type**\:  :py:class:`LastReachedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime>`
                            
                            .. attribute:: reachability_state
                            
                            	Current state
                            	**type**\:  :py:class:`Ipv6NdShState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdShState>`
                            
                            .. attribute:: link_layer_address
                            
                            	Link\-Layer Address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: encapsulation
                            
                            	Preferred media encap type
                            	**type**\:  :py:class:`Ipv6NdMediaEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdMediaEncap>`
                            
                            .. attribute:: selected_encapsulation
                            
                            	Selected media encap
                            	**type**\:  :py:class:`Ipv6NdMediaEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdMediaEncap>`
                            
                            .. attribute:: origin_encapsulation
                            
                            	Neighbor origin
                            	**type**\:  :py:class:`Ipv6NdNeighborOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdNeighborOrigin>`
                            
                            .. attribute:: interface_name
                            
                            	Interface name
                            	**type**\: str
                            
                            .. attribute:: location
                            
                            	Location where the neighbor entry exists
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: is_router
                            
                            	IsRouter
                            	**type**\: bool
                            
                            .. attribute:: serg_flags
                            
                            	ND serg flags for this entry
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrfid
                            
                            	VRF name for this entry
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-nd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress, self).__init__()

                                self.yang_name = "host-address"
                                self.yang_parent_name = "host-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['host_address']
                                self._child_container_classes = OrderedDict([("last-reached-time", ("last_reached_time", Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('host_address', YLeaf(YType.str, 'host-address')),
                                    ('reachability_state', YLeaf(YType.enumeration, 'reachability-state')),
                                    ('link_layer_address', YLeaf(YType.str, 'link-layer-address')),
                                    ('encapsulation', YLeaf(YType.enumeration, 'encapsulation')),
                                    ('selected_encapsulation', YLeaf(YType.enumeration, 'selected-encapsulation')),
                                    ('origin_encapsulation', YLeaf(YType.enumeration, 'origin-encapsulation')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('location', YLeaf(YType.str, 'location')),
                                    ('is_router', YLeaf(YType.boolean, 'is-router')),
                                    ('serg_flags', YLeaf(YType.uint32, 'serg-flags')),
                                    ('vrfid', YLeaf(YType.uint32, 'vrfid')),
                                ])
                                self.host_address = None
                                self.reachability_state = None
                                self.link_layer_address = None
                                self.encapsulation = None
                                self.selected_encapsulation = None
                                self.origin_encapsulation = None
                                self.interface_name = None
                                self.location = None
                                self.is_router = None
                                self.serg_flags = None
                                self.vrfid = None

                                self.last_reached_time = Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime()
                                self.last_reached_time.parent = self
                                self._children_name_map["last_reached_time"] = "last-reached-time"
                                self._children_yang_names.add("last-reached-time")
                                self._segment_path = lambda: "host-address" + "[host-address='" + str(self.host_address) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress, ['host_address', 'reachability_state', 'link_layer_address', 'encapsulation', 'selected_encapsulation', 'origin_encapsulation', 'interface_name', 'location', 'is_router', 'serg_flags', 'vrfid'], name, value)


                            class LastReachedTime(Entity):
                                """
                                Last time of reachability
                                
                                .. attribute:: seconds
                                
                                	Number of seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'ipv6-nd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime, self).__init__()

                                    self.yang_name = "last-reached-time"
                                    self.yang_parent_name = "host-address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('seconds', YLeaf(YType.uint32, 'seconds')),
                                    ])
                                    self.seconds = None
                                    self._segment_path = lambda: "last-reached-time"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime, ['seconds'], name, value)


            class NeighborSummary(Entity):
                """
                IPv6 Neighbor summary
                
                .. attribute:: multicast
                
                	Multicast neighbor summary
                	**type**\:  :py:class:`Multicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast>`
                
                .. attribute:: static
                
                	Static neighbor summary
                	**type**\:  :py:class:`Static <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static>`
                
                .. attribute:: dynamic
                
                	Dynamic neighbor summary
                	**type**\:  :py:class:`Dynamic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic>`
                
                .. attribute:: total_neighbor_entries
                
                	Total number of entries
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary, self).__init__()

                    self.yang_name = "neighbor-summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("multicast", ("multicast", Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast)), ("static", ("static", Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static)), ("dynamic", ("dynamic", Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('total_neighbor_entries', YLeaf(YType.uint32, 'total-neighbor-entries')),
                    ])
                    self.total_neighbor_entries = None

                    self.multicast = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast()
                    self.multicast.parent = self
                    self._children_name_map["multicast"] = "multicast"
                    self._children_yang_names.add("multicast")

                    self.static = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static()
                    self.static.parent = self
                    self._children_name_map["static"] = "static"
                    self._children_yang_names.add("static")

                    self.dynamic = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic()
                    self.dynamic.parent = self
                    self._children_name_map["dynamic"] = "dynamic"
                    self._children_yang_names.add("dynamic")
                    self._segment_path = lambda: "neighbor-summary"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary, ['total_neighbor_entries'], name, value)


                class Multicast(Entity):
                    """
                    Multicast neighbor summary
                    
                    .. attribute:: incomplete_entries
                    
                    	Total incomplete entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reachable_entries
                    
                    	Total reachable entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: stale_entries
                    
                    	Total stale entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delayed_entries
                    
                    	Total delayed entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: probe_entries
                    
                    	Total probe entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: deleted_entries
                    
                    	Total deleted entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subtotal_neighbor_entries
                    
                    	Total number of entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast, self).__init__()

                        self.yang_name = "multicast"
                        self.yang_parent_name = "neighbor-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('incomplete_entries', YLeaf(YType.uint32, 'incomplete-entries')),
                            ('reachable_entries', YLeaf(YType.uint32, 'reachable-entries')),
                            ('stale_entries', YLeaf(YType.uint32, 'stale-entries')),
                            ('delayed_entries', YLeaf(YType.uint32, 'delayed-entries')),
                            ('probe_entries', YLeaf(YType.uint32, 'probe-entries')),
                            ('deleted_entries', YLeaf(YType.uint32, 'deleted-entries')),
                            ('subtotal_neighbor_entries', YLeaf(YType.uint32, 'subtotal-neighbor-entries')),
                        ])
                        self.incomplete_entries = None
                        self.reachable_entries = None
                        self.stale_entries = None
                        self.delayed_entries = None
                        self.probe_entries = None
                        self.deleted_entries = None
                        self.subtotal_neighbor_entries = None
                        self._segment_path = lambda: "multicast"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast, ['incomplete_entries', 'reachable_entries', 'stale_entries', 'delayed_entries', 'probe_entries', 'deleted_entries', 'subtotal_neighbor_entries'], name, value)


                class Static(Entity):
                    """
                    Static neighbor summary
                    
                    .. attribute:: incomplete_entries
                    
                    	Total incomplete entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reachable_entries
                    
                    	Total reachable entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: stale_entries
                    
                    	Total stale entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delayed_entries
                    
                    	Total delayed entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: probe_entries
                    
                    	Total probe entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: deleted_entries
                    
                    	Total deleted entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subtotal_neighbor_entries
                    
                    	Total number of entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static, self).__init__()

                        self.yang_name = "static"
                        self.yang_parent_name = "neighbor-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('incomplete_entries', YLeaf(YType.uint32, 'incomplete-entries')),
                            ('reachable_entries', YLeaf(YType.uint32, 'reachable-entries')),
                            ('stale_entries', YLeaf(YType.uint32, 'stale-entries')),
                            ('delayed_entries', YLeaf(YType.uint32, 'delayed-entries')),
                            ('probe_entries', YLeaf(YType.uint32, 'probe-entries')),
                            ('deleted_entries', YLeaf(YType.uint32, 'deleted-entries')),
                            ('subtotal_neighbor_entries', YLeaf(YType.uint32, 'subtotal-neighbor-entries')),
                        ])
                        self.incomplete_entries = None
                        self.reachable_entries = None
                        self.stale_entries = None
                        self.delayed_entries = None
                        self.probe_entries = None
                        self.deleted_entries = None
                        self.subtotal_neighbor_entries = None
                        self._segment_path = lambda: "static"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static, ['incomplete_entries', 'reachable_entries', 'stale_entries', 'delayed_entries', 'probe_entries', 'deleted_entries', 'subtotal_neighbor_entries'], name, value)


                class Dynamic(Entity):
                    """
                    Dynamic neighbor summary
                    
                    .. attribute:: incomplete_entries
                    
                    	Total incomplete entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reachable_entries
                    
                    	Total reachable entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: stale_entries
                    
                    	Total stale entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delayed_entries
                    
                    	Total delayed entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: probe_entries
                    
                    	Total probe entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: deleted_entries
                    
                    	Total deleted entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subtotal_neighbor_entries
                    
                    	Total number of entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic, self).__init__()

                        self.yang_name = "dynamic"
                        self.yang_parent_name = "neighbor-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('incomplete_entries', YLeaf(YType.uint32, 'incomplete-entries')),
                            ('reachable_entries', YLeaf(YType.uint32, 'reachable-entries')),
                            ('stale_entries', YLeaf(YType.uint32, 'stale-entries')),
                            ('delayed_entries', YLeaf(YType.uint32, 'delayed-entries')),
                            ('probe_entries', YLeaf(YType.uint32, 'probe-entries')),
                            ('deleted_entries', YLeaf(YType.uint32, 'deleted-entries')),
                            ('subtotal_neighbor_entries', YLeaf(YType.uint32, 'subtotal-neighbor-entries')),
                        ])
                        self.incomplete_entries = None
                        self.reachable_entries = None
                        self.stale_entries = None
                        self.delayed_entries = None
                        self.probe_entries = None
                        self.deleted_entries = None
                        self.subtotal_neighbor_entries = None
                        self._segment_path = lambda: "dynamic"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic, ['incomplete_entries', 'reachable_entries', 'stale_entries', 'delayed_entries', 'probe_entries', 'deleted_entries', 'subtotal_neighbor_entries'], name, value)


            class BundleNodes(Entity):
                """
                IPv6 ND list of bundle nodes for a specific
                node
                
                .. attribute:: bundle_node
                
                	IPv6 ND operational data for a specific bundle node
                	**type**\: list of  		 :py:class:`BundleNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode>`
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6NodeDiscovery.Nodes.Node.BundleNodes, self).__init__()

                    self.yang_name = "bundle-nodes"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("bundle-node", ("bundle_node", Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode))])
                    self._leafs = OrderedDict()

                    self.bundle_node = YList(self)
                    self._segment_path = lambda: "bundle-nodes"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.BundleNodes, [], name, value)


                class BundleNode(Entity):
                    """
                    IPv6 ND operational data for a specific
                    bundle node
                    
                    .. attribute:: node_name  (key)
                    
                    	The bundle node name
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: age
                    
                    	Uptime of node (secs)
                    	**type**\:  :py:class:`Age <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age>`
                    
                    .. attribute:: group_id
                    
                    	Group ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: process_name
                    
                    	Process Name
                    	**type**\: str
                    
                    .. attribute:: sent_sequence_number
                    
                    	Sent sequence num
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_sequence_number
                    
                    	Received sequence num
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: state
                    
                    	State
                    	**type**\:  :py:class:`Ipv6NdBndlState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdBndlState>`
                    
                    .. attribute:: state_changes
                    
                    	State changes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent_packets
                    
                    	Total packet sends
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_packets
                    
                    	Total packet receives
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode, self).__init__()

                        self.yang_name = "bundle-node"
                        self.yang_parent_name = "bundle-nodes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['node_name']
                        self._child_container_classes = OrderedDict([("age", ("age", Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('node_name', YLeaf(YType.str, 'node-name')),
                            ('group_id', YLeaf(YType.uint32, 'group-id')),
                            ('process_name', YLeaf(YType.str, 'process-name')),
                            ('sent_sequence_number', YLeaf(YType.uint32, 'sent-sequence-number')),
                            ('received_sequence_number', YLeaf(YType.uint32, 'received-sequence-number')),
                            ('state', YLeaf(YType.enumeration, 'state')),
                            ('state_changes', YLeaf(YType.uint32, 'state-changes')),
                            ('sent_packets', YLeaf(YType.uint32, 'sent-packets')),
                            ('received_packets', YLeaf(YType.uint32, 'received-packets')),
                        ])
                        self.node_name = None
                        self.group_id = None
                        self.process_name = None
                        self.sent_sequence_number = None
                        self.received_sequence_number = None
                        self.state = None
                        self.state_changes = None
                        self.sent_packets = None
                        self.received_packets = None

                        self.age = Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age()
                        self.age.parent = self
                        self._children_name_map["age"] = "age"
                        self._children_yang_names.add("age")
                        self._segment_path = lambda: "bundle-node" + "[node-name='" + str(self.node_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode, ['node_name', 'group_id', 'process_name', 'sent_sequence_number', 'received_sequence_number', 'state', 'state_changes', 'sent_packets', 'received_packets'], name, value)


                    class Age(Entity):
                        """
                        Uptime of node (secs)
                        
                        .. attribute:: seconds
                        
                        	Number of seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age, self).__init__()

                            self.yang_name = "age"
                            self.yang_parent_name = "bundle-node"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('seconds', YLeaf(YType.uint32, 'seconds')),
                            ])
                            self.seconds = None
                            self._segment_path = lambda: "age"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age, ['seconds'], name, value)


            class BundleInterfaces(Entity):
                """
                IPv6 ND list of bundle interfaces for a
                specific node
                
                .. attribute:: bundle_interface
                
                	IPv6 ND operational data for a specific bundler interface
                	**type**\: list of  		 :py:class:`BundleInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface>`
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces, self).__init__()

                    self.yang_name = "bundle-interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("bundle-interface", ("bundle_interface", Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface))])
                    self._leafs = OrderedDict()

                    self.bundle_interface = YList(self)
                    self._segment_path = lambda: "bundle-interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces, [], name, value)


                class BundleInterface(Entity):
                    """
                    IPv6 ND operational data for a specific
                    bundler interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: nd_parameters
                    
                    	ND interface parameters
                    	**type**\:  :py:class:`NdParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters>`
                    
                    .. attribute:: local_address
                    
                    	Link local address
                    	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress>`
                    
                    .. attribute:: parent_interface_name
                    
                    	Parent interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: iftype
                    
                    	Interface type
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mtu
                    
                    	MTU
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: etype
                    
                    	etype
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vlan_tag
                    
                    	vlan tag/id/ucv
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: mac_addr_size
                    
                    	mac address size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mac_addr
                    
                    	mac address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: is_interface_enabled
                    
                    	If true, interface is enabled
                    	**type**\: bool
                    
                    .. attribute:: is_ipv6_enabled
                    
                    	If true, IPv6 is enabled
                    	**type**\: bool
                    
                    .. attribute:: is_mpls_enabled
                    
                    	If true, MPLS is enabled
                    	**type**\: bool
                    
                    .. attribute:: member_link
                    
                    	List of member links
                    	**type**\: list of int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: global_address
                    
                    	List of ND global addresses
                    	**type**\: list of  		 :py:class:`GlobalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress>`
                    
                    .. attribute:: member_node
                    
                    	List of member nodes
                    	**type**\: list of  		 :py:class:`MemberNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode>`
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface, self).__init__()

                        self.yang_name = "bundle-interface"
                        self.yang_parent_name = "bundle-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_container_classes = OrderedDict([("nd-parameters", ("nd_parameters", Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters)), ("local-address", ("local_address", Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress))])
                        self._child_list_classes = OrderedDict([("global-address", ("global_address", Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress)), ("member-node", ("member_node", Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode))])
                        self._leafs = OrderedDict([
                            ('interface_name', YLeaf(YType.str, 'interface-name')),
                            ('parent_interface_name', YLeaf(YType.str, 'parent-interface-name')),
                            ('iftype', YLeaf(YType.uint32, 'iftype')),
                            ('mtu', YLeaf(YType.uint32, 'mtu')),
                            ('etype', YLeaf(YType.uint32, 'etype')),
                            ('vlan_tag', YLeaf(YType.uint16, 'vlan-tag')),
                            ('mac_addr_size', YLeaf(YType.uint32, 'mac-addr-size')),
                            ('mac_addr', YLeaf(YType.str, 'mac-addr')),
                            ('is_interface_enabled', YLeaf(YType.boolean, 'is-interface-enabled')),
                            ('is_ipv6_enabled', YLeaf(YType.boolean, 'is-ipv6-enabled')),
                            ('is_mpls_enabled', YLeaf(YType.boolean, 'is-mpls-enabled')),
                            ('member_link', YLeafList(YType.uint32, 'member-link')),
                        ])
                        self.interface_name = None
                        self.parent_interface_name = None
                        self.iftype = None
                        self.mtu = None
                        self.etype = None
                        self.vlan_tag = None
                        self.mac_addr_size = None
                        self.mac_addr = None
                        self.is_interface_enabled = None
                        self.is_ipv6_enabled = None
                        self.is_mpls_enabled = None
                        self.member_link = []

                        self.nd_parameters = Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters()
                        self.nd_parameters.parent = self
                        self._children_name_map["nd_parameters"] = "nd-parameters"
                        self._children_yang_names.add("nd-parameters")

                        self.local_address = Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress()
                        self.local_address.parent = self
                        self._children_name_map["local_address"] = "local-address"
                        self._children_yang_names.add("local-address")

                        self.global_address = YList(self)
                        self.member_node = YList(self)
                        self._segment_path = lambda: "bundle-interface" + "[interface-name='" + str(self.interface_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface, ['interface_name', 'parent_interface_name', 'iftype', 'mtu', 'etype', 'vlan_tag', 'mac_addr_size', 'mac_addr', 'is_interface_enabled', 'is_ipv6_enabled', 'is_mpls_enabled', 'member_link'], name, value)


                    class NdParameters(Entity):
                        """
                        ND interface parameters
                        
                        .. attribute:: is_dad_enabled
                        
                        	If true, DAD (D.. A.. D..) is enabled otherwise it is disabled
                        	**type**\: bool
                        
                        .. attribute:: dad_attempts
                        
                        	DAD attempt count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_icm_pv6_redirect
                        
                        	ICMP redirect flag
                        	**type**\: bool
                        
                        .. attribute:: is_dhcp_managed
                        
                        	Flag used for utilising DHCP
                        	**type**\: bool
                        
                        .. attribute:: is_route_address_managed
                        
                        	Flag used to manage routable address
                        	**type**\: bool
                        
                        .. attribute:: is_suppressed
                        
                        	Suppress flag
                        	**type**\: bool
                        
                        .. attribute:: send_unicast_ra
                        
                        	unicast RA send flag
                        	**type**\: bool
                        
                        .. attribute:: nd_retransmit_interval
                        
                        	ND retransmit interval in msec
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nd_min_transmit_interval
                        
                        	ND router advertisement minimum transmit interval in sec
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nd_max_transmit_interval
                        
                        	ND router advertisement maximum transmit interval in sec
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nd_advertisement_lifetime
                        
                        	ND router advertisement life time in sec
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nd_reachable_time
                        
                        	Time to reach ND in msec
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nd_cache_limit
                        
                        	Completed adjacency limit per interface
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: complete_protocol_count
                        
                        	Completed PROTO entry Count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: complete_glean_count
                        
                        	Completed GLEAN entry count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incomplete_protocol_count
                        
                        	Incomplete PROTO entry count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incomplete_glean_count
                        
                        	Incomplete GLEAN entry count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_protocol_req_count
                        
                        	Dropped PROTO entry request count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_glean_req_count
                        
                        	Dropped GLEAN entry lequest count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters, self).__init__()

                            self.yang_name = "nd-parameters"
                            self.yang_parent_name = "bundle-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_dad_enabled', YLeaf(YType.boolean, 'is-dad-enabled')),
                                ('dad_attempts', YLeaf(YType.uint32, 'dad-attempts')),
                                ('is_icm_pv6_redirect', YLeaf(YType.boolean, 'is-icm-pv6-redirect')),
                                ('is_dhcp_managed', YLeaf(YType.boolean, 'is-dhcp-managed')),
                                ('is_route_address_managed', YLeaf(YType.boolean, 'is-route-address-managed')),
                                ('is_suppressed', YLeaf(YType.boolean, 'is-suppressed')),
                                ('send_unicast_ra', YLeaf(YType.boolean, 'send-unicast-ra')),
                                ('nd_retransmit_interval', YLeaf(YType.uint32, 'nd-retransmit-interval')),
                                ('nd_min_transmit_interval', YLeaf(YType.uint32, 'nd-min-transmit-interval')),
                                ('nd_max_transmit_interval', YLeaf(YType.uint32, 'nd-max-transmit-interval')),
                                ('nd_advertisement_lifetime', YLeaf(YType.uint32, 'nd-advertisement-lifetime')),
                                ('nd_reachable_time', YLeaf(YType.uint32, 'nd-reachable-time')),
                                ('nd_cache_limit', YLeaf(YType.uint32, 'nd-cache-limit')),
                                ('complete_protocol_count', YLeaf(YType.uint32, 'complete-protocol-count')),
                                ('complete_glean_count', YLeaf(YType.uint32, 'complete-glean-count')),
                                ('incomplete_protocol_count', YLeaf(YType.uint32, 'incomplete-protocol-count')),
                                ('incomplete_glean_count', YLeaf(YType.uint32, 'incomplete-glean-count')),
                                ('dropped_protocol_req_count', YLeaf(YType.uint32, 'dropped-protocol-req-count')),
                                ('dropped_glean_req_count', YLeaf(YType.uint32, 'dropped-glean-req-count')),
                            ])
                            self.is_dad_enabled = None
                            self.dad_attempts = None
                            self.is_icm_pv6_redirect = None
                            self.is_dhcp_managed = None
                            self.is_route_address_managed = None
                            self.is_suppressed = None
                            self.send_unicast_ra = None
                            self.nd_retransmit_interval = None
                            self.nd_min_transmit_interval = None
                            self.nd_max_transmit_interval = None
                            self.nd_advertisement_lifetime = None
                            self.nd_reachable_time = None
                            self.nd_cache_limit = None
                            self.complete_protocol_count = None
                            self.complete_glean_count = None
                            self.incomplete_protocol_count = None
                            self.incomplete_glean_count = None
                            self.dropped_protocol_req_count = None
                            self.dropped_glean_req_count = None
                            self._segment_path = lambda: "nd-parameters"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters, ['is_dad_enabled', 'dad_attempts', 'is_icm_pv6_redirect', 'is_dhcp_managed', 'is_route_address_managed', 'is_suppressed', 'send_unicast_ra', 'nd_retransmit_interval', 'nd_min_transmit_interval', 'nd_max_transmit_interval', 'nd_advertisement_lifetime', 'nd_reachable_time', 'nd_cache_limit', 'complete_protocol_count', 'complete_glean_count', 'incomplete_protocol_count', 'incomplete_glean_count', 'dropped_protocol_req_count', 'dropped_glean_req_count'], name, value)


                    class LocalAddress(Entity):
                        """
                        Link local address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress, self).__init__()

                            self.yang_name = "local-address"
                            self.yang_parent_name = "bundle-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv6_address', YLeaf(YType.str, 'ipv6-address')),
                            ])
                            self.ipv6_address = None
                            self._segment_path = lambda: "local-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress, ['ipv6_address'], name, value)


                    class GlobalAddress(Entity):
                        """
                        List of ND global addresses
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress, self).__init__()

                            self.yang_name = "global-address"
                            self.yang_parent_name = "bundle-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv6_address', YLeaf(YType.str, 'ipv6-address')),
                            ])
                            self.ipv6_address = None
                            self._segment_path = lambda: "global-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress, ['ipv6_address'], name, value)


                    class MemberNode(Entity):
                        """
                        List of member nodes
                        
                        .. attribute:: node_name
                        
                        	Node Name
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: total_links
                        
                        	Number of links on the node
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode, self).__init__()

                            self.yang_name = "member-node"
                            self.yang_parent_name = "bundle-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node_name', YLeaf(YType.str, 'node-name')),
                                ('total_links', YLeaf(YType.uint32, 'total-links')),
                            ])
                            self.node_name = None
                            self.total_links = None
                            self._segment_path = lambda: "member-node"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode, ['node_name', 'total_links'], name, value)


            class Interfaces(Entity):
                """
                IPv6 node discovery list of interfaces for a
                specific node
                
                .. attribute:: interface
                
                	IPv6  node discovery operational data for a specific node and interface
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6NodeDiscovery.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("interface", ("interface", Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    IPv6  node discovery operational data for a
                    specific node and interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: is_dad_enabled
                    
                    	If true, DAD (D.. A.. D..) is enabled otherwise it is disabled
                    	**type**\: bool
                    
                    .. attribute:: dad_attempts
                    
                    	DAD attempt count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_icm_pv6_redirect
                    
                    	ICMP redirect flag
                    	**type**\: bool
                    
                    .. attribute:: is_dhcp_managed
                    
                    	Flag used for utilising DHCP
                    	**type**\: bool
                    
                    .. attribute:: is_route_address_managed
                    
                    	Flag used to manage routable address
                    	**type**\: bool
                    
                    .. attribute:: is_suppressed
                    
                    	Suppress flag
                    	**type**\: bool
                    
                    .. attribute:: send_unicast_ra
                    
                    	unicast RA send flag
                    	**type**\: bool
                    
                    .. attribute:: nd_retransmit_interval
                    
                    	ND retransmit interval in msec
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nd_min_transmit_interval
                    
                    	ND router advertisement minimum transmit interval in sec
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nd_max_transmit_interval
                    
                    	ND router advertisement maximum transmit interval in sec
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nd_advertisement_lifetime
                    
                    	ND router advertisement life time in sec
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nd_reachable_time
                    
                    	Time to reach ND in msec
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nd_cache_limit
                    
                    	Completed adjacency limit per interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: complete_protocol_count
                    
                    	Completed PROTO entry Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: complete_glean_count
                    
                    	Completed GLEAN entry count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: incomplete_protocol_count
                    
                    	Incomplete PROTO entry count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: incomplete_glean_count
                    
                    	Incomplete GLEAN entry count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dropped_protocol_req_count
                    
                    	Dropped PROTO entry request count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dropped_glean_req_count
                    
                    	Dropped GLEAN entry lequest count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', YLeaf(YType.str, 'interface-name')),
                            ('is_dad_enabled', YLeaf(YType.boolean, 'is-dad-enabled')),
                            ('dad_attempts', YLeaf(YType.uint32, 'dad-attempts')),
                            ('is_icm_pv6_redirect', YLeaf(YType.boolean, 'is-icm-pv6-redirect')),
                            ('is_dhcp_managed', YLeaf(YType.boolean, 'is-dhcp-managed')),
                            ('is_route_address_managed', YLeaf(YType.boolean, 'is-route-address-managed')),
                            ('is_suppressed', YLeaf(YType.boolean, 'is-suppressed')),
                            ('send_unicast_ra', YLeaf(YType.boolean, 'send-unicast-ra')),
                            ('nd_retransmit_interval', YLeaf(YType.uint32, 'nd-retransmit-interval')),
                            ('nd_min_transmit_interval', YLeaf(YType.uint32, 'nd-min-transmit-interval')),
                            ('nd_max_transmit_interval', YLeaf(YType.uint32, 'nd-max-transmit-interval')),
                            ('nd_advertisement_lifetime', YLeaf(YType.uint32, 'nd-advertisement-lifetime')),
                            ('nd_reachable_time', YLeaf(YType.uint32, 'nd-reachable-time')),
                            ('nd_cache_limit', YLeaf(YType.uint32, 'nd-cache-limit')),
                            ('complete_protocol_count', YLeaf(YType.uint32, 'complete-protocol-count')),
                            ('complete_glean_count', YLeaf(YType.uint32, 'complete-glean-count')),
                            ('incomplete_protocol_count', YLeaf(YType.uint32, 'incomplete-protocol-count')),
                            ('incomplete_glean_count', YLeaf(YType.uint32, 'incomplete-glean-count')),
                            ('dropped_protocol_req_count', YLeaf(YType.uint32, 'dropped-protocol-req-count')),
                            ('dropped_glean_req_count', YLeaf(YType.uint32, 'dropped-glean-req-count')),
                        ])
                        self.interface_name = None
                        self.is_dad_enabled = None
                        self.dad_attempts = None
                        self.is_icm_pv6_redirect = None
                        self.is_dhcp_managed = None
                        self.is_route_address_managed = None
                        self.is_suppressed = None
                        self.send_unicast_ra = None
                        self.nd_retransmit_interval = None
                        self.nd_min_transmit_interval = None
                        self.nd_max_transmit_interval = None
                        self.nd_advertisement_lifetime = None
                        self.nd_reachable_time = None
                        self.nd_cache_limit = None
                        self.complete_protocol_count = None
                        self.complete_glean_count = None
                        self.incomplete_protocol_count = None
                        self.incomplete_glean_count = None
                        self.dropped_protocol_req_count = None
                        self.dropped_glean_req_count = None
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface, ['interface_name', 'is_dad_enabled', 'dad_attempts', 'is_icm_pv6_redirect', 'is_dhcp_managed', 'is_route_address_managed', 'is_suppressed', 'send_unicast_ra', 'nd_retransmit_interval', 'nd_min_transmit_interval', 'nd_max_transmit_interval', 'nd_advertisement_lifetime', 'nd_reachable_time', 'nd_cache_limit', 'complete_protocol_count', 'complete_glean_count', 'incomplete_protocol_count', 'incomplete_glean_count', 'dropped_protocol_req_count', 'dropped_glean_req_count'], name, value)


            class NdVirtualRouters(Entity):
                """
                IPv6 ND virtual router information for a
                specific interface
                
                .. attribute:: nd_virtual_router
                
                	IPv6 ND virtual  router operational data for a specific interface
                	**type**\: list of  		 :py:class:`NdVirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter>`
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters, self).__init__()

                    self.yang_name = "nd-virtual-routers"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("nd-virtual-router", ("nd_virtual_router", Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter))])
                    self._leafs = OrderedDict()

                    self.nd_virtual_router = YList(self)
                    self._segment_path = lambda: "nd-virtual-routers"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters, [], name, value)


                class NdVirtualRouter(Entity):
                    """
                    IPv6 ND virtual  router operational data for
                    a specific interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: local_address
                    
                    	Link local address
                    	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress>`
                    
                    .. attribute:: link_layer_address
                    
                    	Link\-Layer Address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: context
                    
                    	Virtual Router ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: state
                    
                    	VR state
                    	**type**\:  :py:class:`Ipv6NdShVrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdShVrState>`
                    
                    .. attribute:: flags
                    
                    	VR Flags
                    	**type**\:  :py:class:`Ipv6NdShVrFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdShVrFlags>`
                    
                    .. attribute:: vr_gl_addr_ct
                    
                    	Virtual Global Address Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vr_global_address
                    
                    	List of ND global addresses
                    	**type**\: list of  		 :py:class:`VrGlobalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress>`
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter, self).__init__()

                        self.yang_name = "nd-virtual-router"
                        self.yang_parent_name = "nd-virtual-routers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_container_classes = OrderedDict([("local-address", ("local_address", Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress))])
                        self._child_list_classes = OrderedDict([("vr-global-address", ("vr_global_address", Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress))])
                        self._leafs = OrderedDict([
                            ('interface_name', YLeaf(YType.str, 'interface-name')),
                            ('link_layer_address', YLeaf(YType.str, 'link-layer-address')),
                            ('context', YLeaf(YType.uint32, 'context')),
                            ('state', YLeaf(YType.enumeration, 'state')),
                            ('flags', YLeaf(YType.enumeration, 'flags')),
                            ('vr_gl_addr_ct', YLeaf(YType.uint32, 'vr-gl-addr-ct')),
                        ])
                        self.interface_name = None
                        self.link_layer_address = None
                        self.context = None
                        self.state = None
                        self.flags = None
                        self.vr_gl_addr_ct = None

                        self.local_address = Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress()
                        self.local_address.parent = self
                        self._children_name_map["local_address"] = "local-address"
                        self._children_yang_names.add("local-address")

                        self.vr_global_address = YList(self)
                        self._segment_path = lambda: "nd-virtual-router" + "[interface-name='" + str(self.interface_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter, ['interface_name', 'link_layer_address', 'context', 'state', 'flags', 'vr_gl_addr_ct'], name, value)


                    class LocalAddress(Entity):
                        """
                        Link local address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress, self).__init__()

                            self.yang_name = "local-address"
                            self.yang_parent_name = "nd-virtual-router"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv6_address', YLeaf(YType.str, 'ipv6-address')),
                            ])
                            self.ipv6_address = None
                            self._segment_path = lambda: "local-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress, ['ipv6_address'], name, value)


                    class VrGlobalAddress(Entity):
                        """
                        List of ND global addresses
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress, self).__init__()

                            self.yang_name = "vr-global-address"
                            self.yang_parent_name = "nd-virtual-router"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv6_address', YLeaf(YType.str, 'ipv6-address')),
                            ])
                            self.ipv6_address = None
                            self._segment_path = lambda: "vr-global-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress, ['ipv6_address'], name, value)


            class SlaacInterfaces(Entity):
                """
                IPv6 ND list of SLAAC MGMT interfaces for a
                specific node
                
                .. attribute:: slaac_interface
                
                	IPv6 ND operational data for a specific slaac interface
                	**type**\: list of  		 :py:class:`SlaacInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface>`
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces, self).__init__()

                    self.yang_name = "slaac-interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("slaac-interface", ("slaac_interface", Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface))])
                    self._leafs = OrderedDict()

                    self.slaac_interface = YList(self)
                    self._segment_path = lambda: "slaac-interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces, [], name, value)


                class SlaacInterface(Entity):
                    """
                    IPv6 ND operational data for a specific slaac
                    interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: router_advert_detail
                    
                    	IPv6 ND operational data for a specific slaac interface
                    	**type**\:  :py:class:`RouterAdvertDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail>`
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface, self).__init__()

                        self.yang_name = "slaac-interface"
                        self.yang_parent_name = "slaac-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_container_classes = OrderedDict([("router-advert-detail", ("router_advert_detail", Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', YLeaf(YType.str, 'interface-name')),
                        ])
                        self.interface_name = None

                        self.router_advert_detail = Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail()
                        self.router_advert_detail.parent = self
                        self._children_name_map["router_advert_detail"] = "router-advert-detail"
                        self._children_yang_names.add("router-advert-detail")
                        self._segment_path = lambda: "slaac-interface" + "[interface-name='" + str(self.interface_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface, ['interface_name'], name, value)


                    class RouterAdvertDetail(Entity):
                        """
                        IPv6 ND operational data for a specific
                        slaac interface
                        
                        .. attribute:: idb
                        
                        	idb
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: ra
                        
                        	slaac db
                        	**type**\: list of  		 :py:class:`Ra <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra>`
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail, self).__init__()

                            self.yang_name = "router-advert-detail"
                            self.yang_parent_name = "slaac-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("ra", ("ra", Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra))])
                            self._leafs = OrderedDict([
                                ('idb', YLeaf(YType.str, 'idb')),
                            ])
                            self.idb = None

                            self.ra = YList(self)
                            self._segment_path = lambda: "router-advert-detail"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail, ['idb'], name, value)


                        class Ra(Entity):
                            """
                            slaac db
                            
                            .. attribute:: elapsed_ra_time
                            
                            	elapsedRATime
                            	**type**\:  :py:class:`ElapsedRaTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ElapsedRaTime>`
                            
                            .. attribute:: reachable_time
                            
                            	reachabletime
                            	**type**\:  :py:class:`ReachableTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ReachableTime>`
                            
                            .. attribute:: retrans_time
                            
                            	retranstime
                            	**type**\:  :py:class:`RetransTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.RetransTime>`
                            
                            .. attribute:: address
                            
                            	address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: hops
                            
                            	hops
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: flags
                            
                            	flags
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: life_time
                            
                            	lifetime
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mtu
                            
                            	mtu
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: err_msg
                            
                            	errmsg
                            	**type**\: bool
                            
                            .. attribute:: vrf_id
                            
                            	vrf id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: u6_tbl_id
                            
                            	tbl id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rib_protoid
                            
                            	proto id
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: default_router
                            
                            	router
                            	**type**\: bool
                            
                            .. attribute:: reachability
                            
                            	reach
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: prefix_q
                            
                            	Prefix Queue
                            	**type**\: list of  		 :py:class:`PrefixQ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.PrefixQ>`
                            
                            

                            """

                            _prefix = 'ipv6-nd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra, self).__init__()

                                self.yang_name = "ra"
                                self.yang_parent_name = "router-advert-detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("elapsed-ra-time", ("elapsed_ra_time", Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ElapsedRaTime)), ("reachable-time", ("reachable_time", Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ReachableTime)), ("retrans-time", ("retrans_time", Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.RetransTime))])
                                self._child_list_classes = OrderedDict([("prefix-q", ("prefix_q", Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.PrefixQ))])
                                self._leafs = OrderedDict([
                                    ('address', YLeaf(YType.str, 'address')),
                                    ('hops', YLeaf(YType.uint32, 'hops')),
                                    ('flags', YLeaf(YType.uint32, 'flags')),
                                    ('life_time', YLeaf(YType.uint32, 'life-time')),
                                    ('mtu', YLeaf(YType.uint32, 'mtu')),
                                    ('err_msg', YLeaf(YType.boolean, 'err-msg')),
                                    ('vrf_id', YLeaf(YType.uint32, 'vrf-id')),
                                    ('u6_tbl_id', YLeaf(YType.uint32, 'u6-tbl-id')),
                                    ('rib_protoid', YLeaf(YType.uint16, 'rib-protoid')),
                                    ('default_router', YLeaf(YType.boolean, 'default-router')),
                                    ('reachability', YLeaf(YType.uint32, 'reachability')),
                                ])
                                self.address = None
                                self.hops = None
                                self.flags = None
                                self.life_time = None
                                self.mtu = None
                                self.err_msg = None
                                self.vrf_id = None
                                self.u6_tbl_id = None
                                self.rib_protoid = None
                                self.default_router = None
                                self.reachability = None

                                self.elapsed_ra_time = Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ElapsedRaTime()
                                self.elapsed_ra_time.parent = self
                                self._children_name_map["elapsed_ra_time"] = "elapsed-ra-time"
                                self._children_yang_names.add("elapsed-ra-time")

                                self.reachable_time = Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ReachableTime()
                                self.reachable_time.parent = self
                                self._children_name_map["reachable_time"] = "reachable-time"
                                self._children_yang_names.add("reachable-time")

                                self.retrans_time = Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.RetransTime()
                                self.retrans_time.parent = self
                                self._children_name_map["retrans_time"] = "retrans-time"
                                self._children_yang_names.add("retrans-time")

                                self.prefix_q = YList(self)
                                self._segment_path = lambda: "ra"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra, ['address', 'hops', 'flags', 'life_time', 'mtu', 'err_msg', 'vrf_id', 'u6_tbl_id', 'rib_protoid', 'default_router', 'reachability'], name, value)


                            class ElapsedRaTime(Entity):
                                """
                                elapsedRATime
                                
                                .. attribute:: seconds
                                
                                	Number of seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'ipv6-nd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ElapsedRaTime, self).__init__()

                                    self.yang_name = "elapsed-ra-time"
                                    self.yang_parent_name = "ra"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('seconds', YLeaf(YType.uint32, 'seconds')),
                                    ])
                                    self.seconds = None
                                    self._segment_path = lambda: "elapsed-ra-time"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ElapsedRaTime, ['seconds'], name, value)


                            class ReachableTime(Entity):
                                """
                                reachabletime
                                
                                .. attribute:: seconds
                                
                                	Number of seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'ipv6-nd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ReachableTime, self).__init__()

                                    self.yang_name = "reachable-time"
                                    self.yang_parent_name = "ra"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('seconds', YLeaf(YType.uint32, 'seconds')),
                                    ])
                                    self.seconds = None
                                    self._segment_path = lambda: "reachable-time"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ReachableTime, ['seconds'], name, value)


                            class RetransTime(Entity):
                                """
                                retranstime
                                
                                .. attribute:: seconds
                                
                                	Number of seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'ipv6-nd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.RetransTime, self).__init__()

                                    self.yang_name = "retrans-time"
                                    self.yang_parent_name = "ra"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('seconds', YLeaf(YType.uint32, 'seconds')),
                                    ])
                                    self.seconds = None
                                    self._segment_path = lambda: "retrans-time"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.RetransTime, ['seconds'], name, value)


                            class PrefixQ(Entity):
                                """
                                Prefix Queue
                                
                                .. attribute:: prefix_address
                                
                                	Prefix address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: eui64
                                
                                	IPv6 Auto generated address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: valid_life_time
                                
                                	Valid Life Time
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: preferred_life_time
                                
                                	Preferred Life Time
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: prefix_len
                                
                                	Prefix Length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: flags
                                
                                	IPv6 Address Specific Flags
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: pfx_flags
                                
                                	Prefix Address Specific Flags
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ipv6-nd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.PrefixQ, self).__init__()

                                    self.yang_name = "prefix-q"
                                    self.yang_parent_name = "ra"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('prefix_address', YLeaf(YType.str, 'prefix-address')),
                                        ('eui64', YLeaf(YType.str, 'eui64')),
                                        ('valid_life_time', YLeaf(YType.uint32, 'valid-life-time')),
                                        ('preferred_life_time', YLeaf(YType.uint32, 'preferred-life-time')),
                                        ('prefix_len', YLeaf(YType.uint32, 'prefix-len')),
                                        ('flags', YLeaf(YType.uint32, 'flags')),
                                        ('pfx_flags', YLeaf(YType.uint32, 'pfx-flags')),
                                    ])
                                    self.prefix_address = None
                                    self.eui64 = None
                                    self.valid_life_time = None
                                    self.preferred_life_time = None
                                    self.prefix_len = None
                                    self.flags = None
                                    self.pfx_flags = None
                                    self._segment_path = lambda: "prefix-q"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.PrefixQ, ['prefix_address', 'eui64', 'valid_life_time', 'preferred_life_time', 'prefix_len', 'flags', 'pfx_flags'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv6NodeDiscovery()
        return self._top_entity

