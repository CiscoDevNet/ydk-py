""" Cisco_IOS_XR_ipv6_nd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-nd package operational data.

This module contains definitions
for the following management objects\:
  ipv6\-node\-discovery\: IPv6 node discovery operational data

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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
        return meta._meta_table['Ipv6NdBndlState']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
        return meta._meta_table['Ipv6NdMediaEncap']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
        return meta._meta_table['Ipv6NdNeighborOrigin']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
        return meta._meta_table['Ipv6NdShState']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
        return meta._meta_table['Ipv6NdShVrFlags']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
        return meta._meta_table['Ipv6NdShVrState']



class Ipv6NodeDiscovery(_Entity_):
    """
    IPv6 node discovery operational data
    
    .. attribute:: nodes
    
    	IPv6 node discovery list of nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'ipv6-nd-oper'
    _revision = '2019-09-26'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Ipv6NodeDiscovery, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6-node-discovery"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-nd-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Ipv6NodeDiscovery.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Ipv6NodeDiscovery.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-nd-oper:ipv6-node-discovery"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv6NodeDiscovery, [], name, value)


    class Nodes(_Entity_):
        """
        IPv6 node discovery list of nodes
        
        .. attribute:: node
        
        	IPv6 node discovery operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ipv6-nd-oper'
        _revision = '2019-09-26'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ipv6NodeDiscovery.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ipv6-node-discovery"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Ipv6NodeDiscovery.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-nd-oper:ipv6-node-discovery/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6NodeDiscovery.Nodes, [], name, value)


        class Node(_Entity_):
            """
            IPv6 node discovery operational data for a
            particular node
            
            .. attribute:: node_name  (key)
            
            	The node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: neighbor_interfaces
            
            	IPv6 node discovery list of neighbor interfaces
            	**type**\:  :py:class:`NeighborInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces>`
            
            	**config**\: False
            
            .. attribute:: neighbor_summary
            
            	Summary of IPv6 Neighbors
            	**type**\:  :py:class:`NeighborSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary>`
            
            	**config**\: False
            
            .. attribute:: bundle_nodes
            
            	IPv6 ND list of bundle nodes for a specific node
            	**type**\:  :py:class:`BundleNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleNodes>`
            
            	**config**\: False
            
            .. attribute:: bundle_interfaces
            
            	IPv6 ND list of bundle interfaces for a specific node
            	**type**\:  :py:class:`BundleInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces>`
            
            	**config**\: False
            
            .. attribute:: interfaces
            
            	IPv6 node discovery list of interfaces for a specific node
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.Interfaces>`
            
            	**config**\: False
            
            .. attribute:: nd_virtual_routers
            
            	IPv6 ND virtual router information for a specific interface
            	**type**\:  :py:class:`NdVirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters>`
            
            	**config**\: False
            
            .. attribute:: slaac_interfaces
            
            	IPv6 ND list of SLAAC MGMT interfaces for a specific node
            	**type**\:  :py:class:`SlaacInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ipv6-nd-oper'
            _revision = '2019-09-26'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ipv6NodeDiscovery.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("neighbor-interfaces", ("neighbor_interfaces", Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces)), ("neighbor-summary", ("neighbor_summary", Ipv6NodeDiscovery.Nodes.Node.NeighborSummary)), ("bundle-nodes", ("bundle_nodes", Ipv6NodeDiscovery.Nodes.Node.BundleNodes)), ("bundle-interfaces", ("bundle_interfaces", Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces)), ("interfaces", ("interfaces", Ipv6NodeDiscovery.Nodes.Node.Interfaces)), ("nd-virtual-routers", ("nd_virtual_routers", Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters)), ("slaac-interfaces", ("slaac_interfaces", Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.neighbor_interfaces = Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces()
                self.neighbor_interfaces.parent = self
                self._children_name_map["neighbor_interfaces"] = "neighbor-interfaces"

                self.neighbor_summary = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary()
                self.neighbor_summary.parent = self
                self._children_name_map["neighbor_summary"] = "neighbor-summary"

                self.bundle_nodes = Ipv6NodeDiscovery.Nodes.Node.BundleNodes()
                self.bundle_nodes.parent = self
                self._children_name_map["bundle_nodes"] = "bundle-nodes"

                self.bundle_interfaces = Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces()
                self.bundle_interfaces.parent = self
                self._children_name_map["bundle_interfaces"] = "bundle-interfaces"

                self.interfaces = Ipv6NodeDiscovery.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"

                self.nd_virtual_routers = Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters()
                self.nd_virtual_routers.parent = self
                self._children_name_map["nd_virtual_routers"] = "nd-virtual-routers"

                self.slaac_interfaces = Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces()
                self.slaac_interfaces.parent = self
                self._children_name_map["slaac_interfaces"] = "slaac-interfaces"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-nd-oper:ipv6-node-discovery/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node, ['node_name'], name, value)


            class NeighborInterfaces(_Entity_):
                """
                IPv6 node discovery list of neighbor
                interfaces
                
                .. attribute:: neighbor_interface
                
                	IPv6 node discovery neighbor interface
                	**type**\: list of  		 :py:class:`NeighborInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2019-09-26'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces, self).__init__()

                    self.yang_name = "neighbor-interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("neighbor-interface", ("neighbor_interface", Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface))])
                    self._leafs = OrderedDict()

                    self.neighbor_interface = YList(self)
                    self._segment_path = lambda: "neighbor-interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces, [], name, value)


                class NeighborInterface(_Entity_):
                    """
                    IPv6 node discovery neighbor interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: host_addresses
                    
                    	IPv6 node discovery list of neighbor host addresses
                    	**type**\:  :py:class:`HostAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2019-09-26'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface, self).__init__()

                        self.yang_name = "neighbor-interface"
                        self.yang_parent_name = "neighbor-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("host-addresses", ("host_addresses", Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None

                        self.host_addresses = Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses()
                        self.host_addresses.parent = self
                        self._children_name_map["host_addresses"] = "host-addresses"
                        self._segment_path = lambda: "neighbor-interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface, ['interface_name'], name, value)


                    class HostAddresses(_Entity_):
                        """
                        IPv6 node discovery list of neighbor host
                        addresses
                        
                        .. attribute:: host_address
                        
                        	IPv6 Neighbor detailed information
                        	**type**\: list of  		 :py:class:`HostAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2019-09-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses, self).__init__()

                            self.yang_name = "host-addresses"
                            self.yang_parent_name = "neighbor-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("host-address", ("host_address", Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress))])
                            self._leafs = OrderedDict()

                            self.host_address = YList(self)
                            self._segment_path = lambda: "host-addresses"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses, [], name, value)


                        class HostAddress(_Entity_):
                            """
                            IPv6 Neighbor detailed information
                            
                            .. attribute:: host_address  (key)
                            
                            	Host Address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            .. attribute:: last_reached_time
                            
                            	Last time of reachability
                            	**type**\:  :py:class:`LastReachedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime>`
                            
                            	**config**\: False
                            
                            .. attribute:: reachability_state
                            
                            	Current state
                            	**type**\:  :py:class:`Ipv6NdShState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdShState>`
                            
                            	**config**\: False
                            
                            .. attribute:: link_layer_address
                            
                            	IPV6 Link\-Layer Address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**config**\: False
                            
                            .. attribute:: encapsulation
                            
                            	Preferred media encap type
                            	**type**\:  :py:class:`Ipv6NdMediaEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdMediaEncap>`
                            
                            	**config**\: False
                            
                            .. attribute:: selected_encapsulation
                            
                            	Selected media encap
                            	**type**\:  :py:class:`Ipv6NdMediaEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdMediaEncap>`
                            
                            	**config**\: False
                            
                            .. attribute:: origin_encapsulation
                            
                            	Neighbor origin
                            	**type**\:  :py:class:`Ipv6NdNeighborOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdNeighborOrigin>`
                            
                            	**config**\: False
                            
                            .. attribute:: interface_name
                            
                            	Name of Interface
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: location
                            
                            	Location where the neighbor entry exists
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            	**config**\: False
                            
                            .. attribute:: is_router
                            
                            	IsRouter
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: serg_flags
                            
                            	ND serg flags for this entry
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: vrfid
                            
                            	VRF name for this entry
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ipv6-nd-oper'
                            _revision = '2019-09-26'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress, self).__init__()

                                self.yang_name = "host-address"
                                self.yang_parent_name = "host-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['host_address']
                                self._child_classes = OrderedDict([("last-reached-time", ("last_reached_time", Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime))])
                                self._leafs = OrderedDict([
                                    ('host_address', (YLeaf(YType.str, 'host-address'), ['str'])),
                                    ('reachability_state', (YLeaf(YType.enumeration, 'reachability-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NdShState', '')])),
                                    ('link_layer_address', (YLeaf(YType.str, 'link-layer-address'), ['str'])),
                                    ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NdMediaEncap', '')])),
                                    ('selected_encapsulation', (YLeaf(YType.enumeration, 'selected-encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NdMediaEncap', '')])),
                                    ('origin_encapsulation', (YLeaf(YType.enumeration, 'origin-encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NdNeighborOrigin', '')])),
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                                    ('is_router', (YLeaf(YType.boolean, 'is-router'), ['bool'])),
                                    ('serg_flags', (YLeaf(YType.uint32, 'serg-flags'), ['int'])),
                                    ('vrfid', (YLeaf(YType.uint32, 'vrfid'), ['int'])),
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
                                self._segment_path = lambda: "host-address" + "[host-address='" + str(self.host_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress, ['host_address', 'reachability_state', 'link_layer_address', 'encapsulation', 'selected_encapsulation', 'origin_encapsulation', 'interface_name', 'location', 'is_router', 'serg_flags', 'vrfid'], name, value)


                            class LastReachedTime(_Entity_):
                                """
                                Last time of reachability
                                
                                .. attribute:: seconds
                                
                                	Number of seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'ipv6-nd-oper'
                                _revision = '2019-09-26'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime, self).__init__()

                                    self.yang_name = "last-reached-time"
                                    self.yang_parent_name = "host-address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                                    ])
                                    self.seconds = None
                                    self._segment_path = lambda: "last-reached-time"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime, ['seconds'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                                return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                            return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces']['meta_info']


            class NeighborSummary(_Entity_):
                """
                Summary of IPv6 Neighbors
                
                .. attribute:: multicast
                
                	Multicast neighbor summary
                	**type**\:  :py:class:`Multicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast>`
                
                	**config**\: False
                
                .. attribute:: static
                
                	Static neighbor summary
                	**type**\:  :py:class:`Static <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static>`
                
                	**config**\: False
                
                .. attribute:: dynamic
                
                	Dynamic neighbor summary
                	**type**\:  :py:class:`Dynamic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic>`
                
                	**config**\: False
                
                .. attribute:: sync
                
                	Sync neighbor summary
                	**type**\:  :py:class:`Sync <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Sync>`
                
                	**config**\: False
                
                .. attribute:: static_sync
                
                	StaticSync neighbor summary
                	**type**\:  :py:class:`StaticSync <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.StaticSync>`
                
                	**config**\: False
                
                .. attribute:: dynamic_sync
                
                	DynamicSync neighbor summary
                	**type**\:  :py:class:`DynamicSync <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.DynamicSync>`
                
                	**config**\: False
                
                .. attribute:: total_neighbor_entries
                
                	Total number of entries
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2019-09-26'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary, self).__init__()

                    self.yang_name = "neighbor-summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("multicast", ("multicast", Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast)), ("static", ("static", Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static)), ("dynamic", ("dynamic", Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic)), ("sync", ("sync", Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Sync)), ("static-sync", ("static_sync", Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.StaticSync)), ("dynamic-sync", ("dynamic_sync", Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.DynamicSync))])
                    self._leafs = OrderedDict([
                        ('total_neighbor_entries', (YLeaf(YType.uint32, 'total-neighbor-entries'), ['int'])),
                    ])
                    self.total_neighbor_entries = None

                    self.multicast = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast()
                    self.multicast.parent = self
                    self._children_name_map["multicast"] = "multicast"

                    self.static = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static()
                    self.static.parent = self
                    self._children_name_map["static"] = "static"

                    self.dynamic = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic()
                    self.dynamic.parent = self
                    self._children_name_map["dynamic"] = "dynamic"

                    self.sync = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Sync()
                    self.sync.parent = self
                    self._children_name_map["sync"] = "sync"

                    self.static_sync = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.StaticSync()
                    self.static_sync.parent = self
                    self._children_name_map["static_sync"] = "static-sync"

                    self.dynamic_sync = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.DynamicSync()
                    self.dynamic_sync.parent = self
                    self._children_name_map["dynamic_sync"] = "dynamic-sync"
                    self._segment_path = lambda: "neighbor-summary"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary, ['total_neighbor_entries'], name, value)


                class Multicast(_Entity_):
                    """
                    Multicast neighbor summary
                    
                    .. attribute:: incomplete_entries
                    
                    	Total ipv6 neighbhors count which are in INCMP state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: reachable_entries
                    
                    	Total ipv6 neighbhors count which are in REACH state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: stale_entries
                    
                    	Total ipv6 neighbhors count which are STALE
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: delayed_entries
                    
                    	Total ipv6 neighbhors count which are in DELAY state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: probe_entries
                    
                    	Total ipv6 neighbhors count which are in PROBE state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: deleted_entries
                    
                    	Total ipv6 neighbhors count which are in DELETE state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: subtotal_neighbor_entries
                    
                    	Total number of entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2019-09-26'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast, self).__init__()

                        self.yang_name = "multicast"
                        self.yang_parent_name = "neighbor-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('incomplete_entries', (YLeaf(YType.uint32, 'incomplete-entries'), ['int'])),
                            ('reachable_entries', (YLeaf(YType.uint32, 'reachable-entries'), ['int'])),
                            ('stale_entries', (YLeaf(YType.uint32, 'stale-entries'), ['int'])),
                            ('delayed_entries', (YLeaf(YType.uint32, 'delayed-entries'), ['int'])),
                            ('probe_entries', (YLeaf(YType.uint32, 'probe-entries'), ['int'])),
                            ('deleted_entries', (YLeaf(YType.uint32, 'deleted-entries'), ['int'])),
                            ('subtotal_neighbor_entries', (YLeaf(YType.uint32, 'subtotal-neighbor-entries'), ['int'])),
                        ])
                        self.incomplete_entries = None
                        self.reachable_entries = None
                        self.stale_entries = None
                        self.delayed_entries = None
                        self.probe_entries = None
                        self.deleted_entries = None
                        self.subtotal_neighbor_entries = None
                        self._segment_path = lambda: "multicast"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast, ['incomplete_entries', 'reachable_entries', 'stale_entries', 'delayed_entries', 'probe_entries', 'deleted_entries', 'subtotal_neighbor_entries'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast']['meta_info']


                class Static(_Entity_):
                    """
                    Static neighbor summary
                    
                    .. attribute:: incomplete_entries
                    
                    	Total ipv6 neighbhors count which are in INCMP state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: reachable_entries
                    
                    	Total ipv6 neighbhors count which are in REACH state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: stale_entries
                    
                    	Total ipv6 neighbhors count which are STALE
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: delayed_entries
                    
                    	Total ipv6 neighbhors count which are in DELAY state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: probe_entries
                    
                    	Total ipv6 neighbhors count which are in PROBE state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: deleted_entries
                    
                    	Total ipv6 neighbhors count which are in DELETE state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: subtotal_neighbor_entries
                    
                    	Total number of entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2019-09-26'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static, self).__init__()

                        self.yang_name = "static"
                        self.yang_parent_name = "neighbor-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('incomplete_entries', (YLeaf(YType.uint32, 'incomplete-entries'), ['int'])),
                            ('reachable_entries', (YLeaf(YType.uint32, 'reachable-entries'), ['int'])),
                            ('stale_entries', (YLeaf(YType.uint32, 'stale-entries'), ['int'])),
                            ('delayed_entries', (YLeaf(YType.uint32, 'delayed-entries'), ['int'])),
                            ('probe_entries', (YLeaf(YType.uint32, 'probe-entries'), ['int'])),
                            ('deleted_entries', (YLeaf(YType.uint32, 'deleted-entries'), ['int'])),
                            ('subtotal_neighbor_entries', (YLeaf(YType.uint32, 'subtotal-neighbor-entries'), ['int'])),
                        ])
                        self.incomplete_entries = None
                        self.reachable_entries = None
                        self.stale_entries = None
                        self.delayed_entries = None
                        self.probe_entries = None
                        self.deleted_entries = None
                        self.subtotal_neighbor_entries = None
                        self._segment_path = lambda: "static"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static, ['incomplete_entries', 'reachable_entries', 'stale_entries', 'delayed_entries', 'probe_entries', 'deleted_entries', 'subtotal_neighbor_entries'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static']['meta_info']


                class Dynamic(_Entity_):
                    """
                    Dynamic neighbor summary
                    
                    .. attribute:: incomplete_entries
                    
                    	Total ipv6 neighbhors count which are in INCMP state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: reachable_entries
                    
                    	Total ipv6 neighbhors count which are in REACH state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: stale_entries
                    
                    	Total ipv6 neighbhors count which are STALE
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: delayed_entries
                    
                    	Total ipv6 neighbhors count which are in DELAY state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: probe_entries
                    
                    	Total ipv6 neighbhors count which are in PROBE state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: deleted_entries
                    
                    	Total ipv6 neighbhors count which are in DELETE state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: subtotal_neighbor_entries
                    
                    	Total number of entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2019-09-26'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic, self).__init__()

                        self.yang_name = "dynamic"
                        self.yang_parent_name = "neighbor-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('incomplete_entries', (YLeaf(YType.uint32, 'incomplete-entries'), ['int'])),
                            ('reachable_entries', (YLeaf(YType.uint32, 'reachable-entries'), ['int'])),
                            ('stale_entries', (YLeaf(YType.uint32, 'stale-entries'), ['int'])),
                            ('delayed_entries', (YLeaf(YType.uint32, 'delayed-entries'), ['int'])),
                            ('probe_entries', (YLeaf(YType.uint32, 'probe-entries'), ['int'])),
                            ('deleted_entries', (YLeaf(YType.uint32, 'deleted-entries'), ['int'])),
                            ('subtotal_neighbor_entries', (YLeaf(YType.uint32, 'subtotal-neighbor-entries'), ['int'])),
                        ])
                        self.incomplete_entries = None
                        self.reachable_entries = None
                        self.stale_entries = None
                        self.delayed_entries = None
                        self.probe_entries = None
                        self.deleted_entries = None
                        self.subtotal_neighbor_entries = None
                        self._segment_path = lambda: "dynamic"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic, ['incomplete_entries', 'reachable_entries', 'stale_entries', 'delayed_entries', 'probe_entries', 'deleted_entries', 'subtotal_neighbor_entries'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic']['meta_info']


                class Sync(_Entity_):
                    """
                    Sync neighbor summary
                    
                    .. attribute:: incomplete_entries
                    
                    	Total ipv6 neighbhors count which are in INCMP state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: reachable_entries
                    
                    	Total ipv6 neighbhors count which are in REACH state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: stale_entries
                    
                    	Total ipv6 neighbhors count which are STALE
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: delayed_entries
                    
                    	Total ipv6 neighbhors count which are in DELAY state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: probe_entries
                    
                    	Total ipv6 neighbhors count which are in PROBE state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: deleted_entries
                    
                    	Total ipv6 neighbhors count which are in DELETE state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: subtotal_neighbor_entries
                    
                    	Total number of entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2019-09-26'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Sync, self).__init__()

                        self.yang_name = "sync"
                        self.yang_parent_name = "neighbor-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('incomplete_entries', (YLeaf(YType.uint32, 'incomplete-entries'), ['int'])),
                            ('reachable_entries', (YLeaf(YType.uint32, 'reachable-entries'), ['int'])),
                            ('stale_entries', (YLeaf(YType.uint32, 'stale-entries'), ['int'])),
                            ('delayed_entries', (YLeaf(YType.uint32, 'delayed-entries'), ['int'])),
                            ('probe_entries', (YLeaf(YType.uint32, 'probe-entries'), ['int'])),
                            ('deleted_entries', (YLeaf(YType.uint32, 'deleted-entries'), ['int'])),
                            ('subtotal_neighbor_entries', (YLeaf(YType.uint32, 'subtotal-neighbor-entries'), ['int'])),
                        ])
                        self.incomplete_entries = None
                        self.reachable_entries = None
                        self.stale_entries = None
                        self.delayed_entries = None
                        self.probe_entries = None
                        self.deleted_entries = None
                        self.subtotal_neighbor_entries = None
                        self._segment_path = lambda: "sync"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Sync, ['incomplete_entries', 'reachable_entries', 'stale_entries', 'delayed_entries', 'probe_entries', 'deleted_entries', 'subtotal_neighbor_entries'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Sync']['meta_info']


                class StaticSync(_Entity_):
                    """
                    StaticSync neighbor summary
                    
                    .. attribute:: incomplete_entries
                    
                    	Total ipv6 neighbhors count which are in INCMP state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: reachable_entries
                    
                    	Total ipv6 neighbhors count which are in REACH state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: stale_entries
                    
                    	Total ipv6 neighbhors count which are STALE
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: delayed_entries
                    
                    	Total ipv6 neighbhors count which are in DELAY state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: probe_entries
                    
                    	Total ipv6 neighbhors count which are in PROBE state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: deleted_entries
                    
                    	Total ipv6 neighbhors count which are in DELETE state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: subtotal_neighbor_entries
                    
                    	Total number of entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2019-09-26'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.StaticSync, self).__init__()

                        self.yang_name = "static-sync"
                        self.yang_parent_name = "neighbor-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('incomplete_entries', (YLeaf(YType.uint32, 'incomplete-entries'), ['int'])),
                            ('reachable_entries', (YLeaf(YType.uint32, 'reachable-entries'), ['int'])),
                            ('stale_entries', (YLeaf(YType.uint32, 'stale-entries'), ['int'])),
                            ('delayed_entries', (YLeaf(YType.uint32, 'delayed-entries'), ['int'])),
                            ('probe_entries', (YLeaf(YType.uint32, 'probe-entries'), ['int'])),
                            ('deleted_entries', (YLeaf(YType.uint32, 'deleted-entries'), ['int'])),
                            ('subtotal_neighbor_entries', (YLeaf(YType.uint32, 'subtotal-neighbor-entries'), ['int'])),
                        ])
                        self.incomplete_entries = None
                        self.reachable_entries = None
                        self.stale_entries = None
                        self.delayed_entries = None
                        self.probe_entries = None
                        self.deleted_entries = None
                        self.subtotal_neighbor_entries = None
                        self._segment_path = lambda: "static-sync"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.StaticSync, ['incomplete_entries', 'reachable_entries', 'stale_entries', 'delayed_entries', 'probe_entries', 'deleted_entries', 'subtotal_neighbor_entries'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.StaticSync']['meta_info']


                class DynamicSync(_Entity_):
                    """
                    DynamicSync neighbor summary
                    
                    .. attribute:: incomplete_entries
                    
                    	Total ipv6 neighbhors count which are in INCMP state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: reachable_entries
                    
                    	Total ipv6 neighbhors count which are in REACH state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: stale_entries
                    
                    	Total ipv6 neighbhors count which are STALE
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: delayed_entries
                    
                    	Total ipv6 neighbhors count which are in DELAY state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: probe_entries
                    
                    	Total ipv6 neighbhors count which are in PROBE state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: deleted_entries
                    
                    	Total ipv6 neighbhors count which are in DELETE state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: subtotal_neighbor_entries
                    
                    	Total number of entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2019-09-26'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.DynamicSync, self).__init__()

                        self.yang_name = "dynamic-sync"
                        self.yang_parent_name = "neighbor-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('incomplete_entries', (YLeaf(YType.uint32, 'incomplete-entries'), ['int'])),
                            ('reachable_entries', (YLeaf(YType.uint32, 'reachable-entries'), ['int'])),
                            ('stale_entries', (YLeaf(YType.uint32, 'stale-entries'), ['int'])),
                            ('delayed_entries', (YLeaf(YType.uint32, 'delayed-entries'), ['int'])),
                            ('probe_entries', (YLeaf(YType.uint32, 'probe-entries'), ['int'])),
                            ('deleted_entries', (YLeaf(YType.uint32, 'deleted-entries'), ['int'])),
                            ('subtotal_neighbor_entries', (YLeaf(YType.uint32, 'subtotal-neighbor-entries'), ['int'])),
                        ])
                        self.incomplete_entries = None
                        self.reachable_entries = None
                        self.stale_entries = None
                        self.delayed_entries = None
                        self.probe_entries = None
                        self.deleted_entries = None
                        self.subtotal_neighbor_entries = None
                        self._segment_path = lambda: "dynamic-sync"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.DynamicSync, ['incomplete_entries', 'reachable_entries', 'stale_entries', 'delayed_entries', 'probe_entries', 'deleted_entries', 'subtotal_neighbor_entries'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.DynamicSync']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborSummary']['meta_info']


            class BundleNodes(_Entity_):
                """
                IPv6 ND list of bundle nodes for a specific
                node
                
                .. attribute:: bundle_node
                
                	IPv6 ND operational data for a specific bundle node
                	**type**\: list of  		 :py:class:`BundleNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2019-09-26'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ipv6NodeDiscovery.Nodes.Node.BundleNodes, self).__init__()

                    self.yang_name = "bundle-nodes"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("bundle-node", ("bundle_node", Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode))])
                    self._leafs = OrderedDict()

                    self.bundle_node = YList(self)
                    self._segment_path = lambda: "bundle-nodes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.BundleNodes, [], name, value)


                class BundleNode(_Entity_):
                    """
                    IPv6 ND operational data for a specific
                    bundle node
                    
                    .. attribute:: node_name  (key)
                    
                    	The bundle node name
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    	**config**\: False
                    
                    .. attribute:: age
                    
                    	Uptime of node (secs)
                    	**type**\:  :py:class:`Age <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age>`
                    
                    	**config**\: False
                    
                    .. attribute:: group_id
                    
                    	Group ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: process_name
                    
                    	Name of the process
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: sent_sequence_number
                    
                    	Sent sequence number for error detection
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: received_sequence_number
                    
                    	Received sequence num for error detection
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	State
                    	**type**\:  :py:class:`Ipv6NdBndlState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdBndlState>`
                    
                    	**config**\: False
                    
                    .. attribute:: state_changes
                    
                    	change of state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sent_packets
                    
                    	Total packet sends
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: received_packets
                    
                    	Total packet receives
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2019-09-26'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode, self).__init__()

                        self.yang_name = "bundle-node"
                        self.yang_parent_name = "bundle-nodes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['node_name']
                        self._child_classes = OrderedDict([("age", ("age", Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age))])
                        self._leafs = OrderedDict([
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                            ('group_id', (YLeaf(YType.uint32, 'group-id'), ['int'])),
                            ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                            ('sent_sequence_number', (YLeaf(YType.uint32, 'sent-sequence-number'), ['int'])),
                            ('received_sequence_number', (YLeaf(YType.uint32, 'received-sequence-number'), ['int'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NdBndlState', '')])),
                            ('state_changes', (YLeaf(YType.uint32, 'state-changes'), ['int'])),
                            ('sent_packets', (YLeaf(YType.uint32, 'sent-packets'), ['int'])),
                            ('received_packets', (YLeaf(YType.uint32, 'received-packets'), ['int'])),
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
                        self._segment_path = lambda: "bundle-node" + "[node-name='" + str(self.node_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode, ['node_name', 'group_id', 'process_name', 'sent_sequence_number', 'received_sequence_number', 'state', 'state_changes', 'sent_packets', 'received_packets'], name, value)


                    class Age(_Entity_):
                        """
                        Uptime of node (secs)
                        
                        .. attribute:: seconds
                        
                        	Number of seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2019-09-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age, self).__init__()

                            self.yang_name = "age"
                            self.yang_parent_name = "bundle-node"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                            ])
                            self.seconds = None
                            self._segment_path = lambda: "age"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age, ['seconds'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                            return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleNodes']['meta_info']


            class BundleInterfaces(_Entity_):
                """
                IPv6 ND list of bundle interfaces for a
                specific node
                
                .. attribute:: bundle_interface
                
                	IPv6 ND operational data for a specific bundler interface
                	**type**\: list of  		 :py:class:`BundleInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2019-09-26'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces, self).__init__()

                    self.yang_name = "bundle-interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("bundle-interface", ("bundle_interface", Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface))])
                    self._leafs = OrderedDict()

                    self.bundle_interface = YList(self)
                    self._segment_path = lambda: "bundle-interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces, [], name, value)


                class BundleInterface(_Entity_):
                    """
                    IPv6 ND operational data for a specific
                    bundler interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: nd_parameters
                    
                    	ND interface parameters
                    	**type**\:  :py:class:`NdParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters>`
                    
                    	**config**\: False
                    
                    .. attribute:: local_address
                    
                    	IPV6 Link local address
                    	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress>`
                    
                    	**config**\: False
                    
                    .. attribute:: parent_interface_name
                    
                    	Name of the Parent interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: iftype
                    
                    	Interface type
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: mtu
                    
                    	MTU
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: etype
                    
                    	etype field
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: vlan_tag
                    
                    	vlan tag/id/ucv
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: mac_addr_size
                    
                    	size of mac address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: mac_addr
                    
                    	media access control address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    	**config**\: False
                    
                    .. attribute:: is_interface_enabled
                    
                    	If true, interface is enabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_ipv6_enabled
                    
                    	If true, IPv6 is enabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_mpls_enabled
                    
                    	If true, MPLS is enabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: member_link
                    
                    	List of member links
                    	**type**\: list of int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: global_address
                    
                    	List of ND global addresses
                    	**type**\: list of  		 :py:class:`GlobalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress>`
                    
                    	**config**\: False
                    
                    .. attribute:: member_node
                    
                    	List of member nodes
                    	**type**\: list of  		 :py:class:`MemberNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2019-09-26'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface, self).__init__()

                        self.yang_name = "bundle-interface"
                        self.yang_parent_name = "bundle-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("nd-parameters", ("nd_parameters", Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters)), ("local-address", ("local_address", Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress)), ("global-address", ("global_address", Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress)), ("member-node", ("member_node", Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('parent_interface_name', (YLeaf(YType.str, 'parent-interface-name'), ['str'])),
                            ('iftype', (YLeaf(YType.uint32, 'iftype'), ['int'])),
                            ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                            ('etype', (YLeaf(YType.uint32, 'etype'), ['int'])),
                            ('vlan_tag', (YLeaf(YType.uint16, 'vlan-tag'), ['int'])),
                            ('mac_addr_size', (YLeaf(YType.uint32, 'mac-addr-size'), ['int'])),
                            ('mac_addr', (YLeaf(YType.str, 'mac-addr'), ['str'])),
                            ('is_interface_enabled', (YLeaf(YType.boolean, 'is-interface-enabled'), ['bool'])),
                            ('is_ipv6_enabled', (YLeaf(YType.boolean, 'is-ipv6-enabled'), ['bool'])),
                            ('is_mpls_enabled', (YLeaf(YType.boolean, 'is-mpls-enabled'), ['bool'])),
                            ('member_link', (YLeafList(YType.uint32, 'member-link'), ['int'])),
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

                        self.local_address = Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress()
                        self.local_address.parent = self
                        self._children_name_map["local_address"] = "local-address"

                        self.global_address = YList(self)
                        self.member_node = YList(self)
                        self._segment_path = lambda: "bundle-interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface, ['interface_name', 'parent_interface_name', 'iftype', 'mtu', 'etype', 'vlan_tag', 'mac_addr_size', 'mac_addr', 'is_interface_enabled', 'is_ipv6_enabled', 'is_mpls_enabled', 'member_link'], name, value)


                    class NdParameters(_Entity_):
                        """
                        ND interface parameters
                        
                        .. attribute:: is_dad_enabled
                        
                        	If true, DAD (D.. A.. D..) is enabled otherwise it is disabled
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: dad_attempts
                        
                        	DAD attempt count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: is_icm_pv6_redirect
                        
                        	ICMP redirect flag
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_dhcp_managed
                        
                        	Flag used for utilising DHCP
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_route_address_managed
                        
                        	Flag used to manage routable address
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_suppressed
                        
                        	Suppress flag
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: send_unicast_ra
                        
                        	unicast RA send flag
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: nd_retransmit_interval
                        
                        	ND retransmit interval in msec
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: nd_min_transmit_interval
                        
                        	ND router advertisement minimum transmit interval in sec
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: nd_max_transmit_interval
                        
                        	ND router advertisement maximum transmit interval in sec
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: nd_advertisement_lifetime
                        
                        	ND router advertisement life time in sec
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: nd_reachable_time
                        
                        	Time to reach ND in msec
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: nd_cache_limit
                        
                        	Completed adjacency limit per interface
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: complete_protocol_count
                        
                        	Completed PROTO entry Count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: complete_glean_count
                        
                        	Completed GLEAN entry count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: incomplete_protocol_count
                        
                        	Incomplete PROTO entry count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: incomplete_glean_count
                        
                        	Incomplete GLEAN entry count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dropped_protocol_req_count
                        
                        	Dropped PROTO entry request count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dropped_glean_req_count
                        
                        	Dropped GLEAN entry lequest count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2019-09-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters, self).__init__()

                            self.yang_name = "nd-parameters"
                            self.yang_parent_name = "bundle-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_dad_enabled', (YLeaf(YType.boolean, 'is-dad-enabled'), ['bool'])),
                                ('dad_attempts', (YLeaf(YType.uint32, 'dad-attempts'), ['int'])),
                                ('is_icm_pv6_redirect', (YLeaf(YType.boolean, 'is-icm-pv6-redirect'), ['bool'])),
                                ('is_dhcp_managed', (YLeaf(YType.boolean, 'is-dhcp-managed'), ['bool'])),
                                ('is_route_address_managed', (YLeaf(YType.boolean, 'is-route-address-managed'), ['bool'])),
                                ('is_suppressed', (YLeaf(YType.boolean, 'is-suppressed'), ['bool'])),
                                ('send_unicast_ra', (YLeaf(YType.boolean, 'send-unicast-ra'), ['bool'])),
                                ('nd_retransmit_interval', (YLeaf(YType.uint32, 'nd-retransmit-interval'), ['int'])),
                                ('nd_min_transmit_interval', (YLeaf(YType.uint32, 'nd-min-transmit-interval'), ['int'])),
                                ('nd_max_transmit_interval', (YLeaf(YType.uint32, 'nd-max-transmit-interval'), ['int'])),
                                ('nd_advertisement_lifetime', (YLeaf(YType.uint32, 'nd-advertisement-lifetime'), ['int'])),
                                ('nd_reachable_time', (YLeaf(YType.uint32, 'nd-reachable-time'), ['int'])),
                                ('nd_cache_limit', (YLeaf(YType.uint32, 'nd-cache-limit'), ['int'])),
                                ('complete_protocol_count', (YLeaf(YType.uint32, 'complete-protocol-count'), ['int'])),
                                ('complete_glean_count', (YLeaf(YType.uint32, 'complete-glean-count'), ['int'])),
                                ('incomplete_protocol_count', (YLeaf(YType.uint32, 'incomplete-protocol-count'), ['int'])),
                                ('incomplete_glean_count', (YLeaf(YType.uint32, 'incomplete-glean-count'), ['int'])),
                                ('dropped_protocol_req_count', (YLeaf(YType.uint32, 'dropped-protocol-req-count'), ['int'])),
                                ('dropped_glean_req_count', (YLeaf(YType.uint32, 'dropped-glean-req-count'), ['int'])),
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
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters, ['is_dad_enabled', 'dad_attempts', 'is_icm_pv6_redirect', 'is_dhcp_managed', 'is_route_address_managed', 'is_suppressed', 'send_unicast_ra', 'nd_retransmit_interval', 'nd_min_transmit_interval', 'nd_max_transmit_interval', 'nd_advertisement_lifetime', 'nd_reachable_time', 'nd_cache_limit', 'complete_protocol_count', 'complete_glean_count', 'incomplete_protocol_count', 'incomplete_glean_count', 'dropped_protocol_req_count', 'dropped_glean_req_count'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                            return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters']['meta_info']


                    class LocalAddress(_Entity_):
                        """
                        IPV6 Link local address
                        
                        .. attribute:: ipv6_address
                        
                        	Address of type IPV6
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: valid_lifetime
                        
                        	Valid lifetime of a Prefix
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: pref_lifetime
                        
                        	Preffered lifetime of a Prefix
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: prefix_length
                        
                        	IPV6 Prefix length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: flags
                        
                        	Address flags
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2019-09-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress, self).__init__()

                            self.yang_name = "local-address"
                            self.yang_parent_name = "bundle-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                ('valid_lifetime', (YLeaf(YType.uint32, 'valid-lifetime'), ['int'])),
                                ('pref_lifetime', (YLeaf(YType.uint32, 'pref-lifetime'), ['int'])),
                                ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                ('flags', (YLeaf(YType.uint32, 'flags'), ['int'])),
                            ])
                            self.ipv6_address = None
                            self.valid_lifetime = None
                            self.pref_lifetime = None
                            self.prefix_length = None
                            self.flags = None
                            self._segment_path = lambda: "local-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress, ['ipv6_address', 'valid_lifetime', 'pref_lifetime', 'prefix_length', 'flags'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                            return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress']['meta_info']


                    class GlobalAddress(_Entity_):
                        """
                        List of ND global addresses
                        
                        .. attribute:: ipv6_address
                        
                        	Address of type IPV6
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: valid_lifetime
                        
                        	Valid lifetime of a Prefix
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: pref_lifetime
                        
                        	Preffered lifetime of a Prefix
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: prefix_length
                        
                        	IPV6 Prefix length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: flags
                        
                        	Address flags
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2019-09-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress, self).__init__()

                            self.yang_name = "global-address"
                            self.yang_parent_name = "bundle-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                ('valid_lifetime', (YLeaf(YType.uint32, 'valid-lifetime'), ['int'])),
                                ('pref_lifetime', (YLeaf(YType.uint32, 'pref-lifetime'), ['int'])),
                                ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                ('flags', (YLeaf(YType.uint32, 'flags'), ['int'])),
                            ])
                            self.ipv6_address = None
                            self.valid_lifetime = None
                            self.pref_lifetime = None
                            self.prefix_length = None
                            self.flags = None
                            self._segment_path = lambda: "global-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress, ['ipv6_address', 'valid_lifetime', 'pref_lifetime', 'prefix_length', 'flags'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                            return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress']['meta_info']


                    class MemberNode(_Entity_):
                        """
                        List of member nodes
                        
                        .. attribute:: node_name
                        
                        	Node Name
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        	**config**\: False
                        
                        .. attribute:: total_links
                        
                        	Number of links on the node
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2019-09-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode, self).__init__()

                            self.yang_name = "member-node"
                            self.yang_parent_name = "bundle-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                                ('total_links', (YLeaf(YType.uint32, 'total-links'), ['int'])),
                            ])
                            self.node_name = None
                            self.total_links = None
                            self._segment_path = lambda: "member-node"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode, ['node_name', 'total_links'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                            return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces']['meta_info']


            class Interfaces(_Entity_):
                """
                IPv6 node discovery list of interfaces for a
                specific node
                
                .. attribute:: interface
                
                	IPv6  node discovery operational data for a specific node and interface
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2019-09-26'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ipv6NodeDiscovery.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.Interfaces, [], name, value)


                class Interface(_Entity_):
                    """
                    IPv6  node discovery operational data for a
                    specific node and interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: is_dad_enabled
                    
                    	If true, DAD (D.. A.. D..) is enabled otherwise it is disabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: dad_attempts
                    
                    	DAD attempt count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: is_icm_pv6_redirect
                    
                    	ICMP redirect flag
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_dhcp_managed
                    
                    	Flag used for utilising DHCP
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_route_address_managed
                    
                    	Flag used to manage routable address
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_suppressed
                    
                    	Suppress flag
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: send_unicast_ra
                    
                    	unicast RA send flag
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: nd_retransmit_interval
                    
                    	ND retransmit interval in msec
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: nd_min_transmit_interval
                    
                    	ND router advertisement minimum transmit interval in sec
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: nd_max_transmit_interval
                    
                    	ND router advertisement maximum transmit interval in sec
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: nd_advertisement_lifetime
                    
                    	ND router advertisement life time in sec
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: nd_reachable_time
                    
                    	Time to reach ND in msec
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: nd_cache_limit
                    
                    	Completed adjacency limit per interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: complete_protocol_count
                    
                    	Completed PROTO entry Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: complete_glean_count
                    
                    	Completed GLEAN entry count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: incomplete_protocol_count
                    
                    	Incomplete PROTO entry count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: incomplete_glean_count
                    
                    	Incomplete GLEAN entry count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dropped_protocol_req_count
                    
                    	Dropped PROTO entry request count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dropped_glean_req_count
                    
                    	Dropped GLEAN entry lequest count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2019-09-26'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('is_dad_enabled', (YLeaf(YType.boolean, 'is-dad-enabled'), ['bool'])),
                            ('dad_attempts', (YLeaf(YType.uint32, 'dad-attempts'), ['int'])),
                            ('is_icm_pv6_redirect', (YLeaf(YType.boolean, 'is-icm-pv6-redirect'), ['bool'])),
                            ('is_dhcp_managed', (YLeaf(YType.boolean, 'is-dhcp-managed'), ['bool'])),
                            ('is_route_address_managed', (YLeaf(YType.boolean, 'is-route-address-managed'), ['bool'])),
                            ('is_suppressed', (YLeaf(YType.boolean, 'is-suppressed'), ['bool'])),
                            ('send_unicast_ra', (YLeaf(YType.boolean, 'send-unicast-ra'), ['bool'])),
                            ('nd_retransmit_interval', (YLeaf(YType.uint32, 'nd-retransmit-interval'), ['int'])),
                            ('nd_min_transmit_interval', (YLeaf(YType.uint32, 'nd-min-transmit-interval'), ['int'])),
                            ('nd_max_transmit_interval', (YLeaf(YType.uint32, 'nd-max-transmit-interval'), ['int'])),
                            ('nd_advertisement_lifetime', (YLeaf(YType.uint32, 'nd-advertisement-lifetime'), ['int'])),
                            ('nd_reachable_time', (YLeaf(YType.uint32, 'nd-reachable-time'), ['int'])),
                            ('nd_cache_limit', (YLeaf(YType.uint32, 'nd-cache-limit'), ['int'])),
                            ('complete_protocol_count', (YLeaf(YType.uint32, 'complete-protocol-count'), ['int'])),
                            ('complete_glean_count', (YLeaf(YType.uint32, 'complete-glean-count'), ['int'])),
                            ('incomplete_protocol_count', (YLeaf(YType.uint32, 'incomplete-protocol-count'), ['int'])),
                            ('incomplete_glean_count', (YLeaf(YType.uint32, 'incomplete-glean-count'), ['int'])),
                            ('dropped_protocol_req_count', (YLeaf(YType.uint32, 'dropped-protocol-req-count'), ['int'])),
                            ('dropped_glean_req_count', (YLeaf(YType.uint32, 'dropped-glean-req-count'), ['int'])),
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
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface, ['interface_name', 'is_dad_enabled', 'dad_attempts', 'is_icm_pv6_redirect', 'is_dhcp_managed', 'is_route_address_managed', 'is_suppressed', 'send_unicast_ra', 'nd_retransmit_interval', 'nd_min_transmit_interval', 'nd_max_transmit_interval', 'nd_advertisement_lifetime', 'nd_reachable_time', 'nd_cache_limit', 'complete_protocol_count', 'complete_glean_count', 'incomplete_protocol_count', 'incomplete_glean_count', 'dropped_protocol_req_count', 'dropped_glean_req_count'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.Interfaces']['meta_info']


            class NdVirtualRouters(_Entity_):
                """
                IPv6 ND virtual router information for a
                specific interface
                
                .. attribute:: nd_virtual_router
                
                	IPv6 ND virtual  router operational data for a specific interface
                	**type**\: list of  		 :py:class:`NdVirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2019-09-26'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters, self).__init__()

                    self.yang_name = "nd-virtual-routers"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("nd-virtual-router", ("nd_virtual_router", Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter))])
                    self._leafs = OrderedDict()

                    self.nd_virtual_router = YList(self)
                    self._segment_path = lambda: "nd-virtual-routers"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters, [], name, value)


                class NdVirtualRouter(_Entity_):
                    """
                    IPv6 ND virtual  router operational data for
                    a specific interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: local_address
                    
                    	IPV6 Link local address
                    	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress>`
                    
                    	**config**\: False
                    
                    .. attribute:: link_layer_address
                    
                    	IPV6 Link\-Layer Address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    	**config**\: False
                    
                    .. attribute:: context
                    
                    	Virtual Router ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	VR state
                    	**type**\:  :py:class:`Ipv6NdShVrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdShVrState>`
                    
                    	**config**\: False
                    
                    .. attribute:: flags
                    
                    	VR Flags
                    	**type**\:  :py:class:`Ipv6NdShVrFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdShVrFlags>`
                    
                    	**config**\: False
                    
                    .. attribute:: vr_gl_addr_ct
                    
                    	Virtual Global Address Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: vr_global_address
                    
                    	List of ND global addresses
                    	**type**\: list of  		 :py:class:`VrGlobalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2019-09-26'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter, self).__init__()

                        self.yang_name = "nd-virtual-router"
                        self.yang_parent_name = "nd-virtual-routers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("local-address", ("local_address", Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress)), ("vr-global-address", ("vr_global_address", Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('link_layer_address', (YLeaf(YType.str, 'link-layer-address'), ['str'])),
                            ('context', (YLeaf(YType.uint32, 'context'), ['int'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NdShVrState', '')])),
                            ('flags', (YLeaf(YType.enumeration, 'flags'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NdShVrFlags', '')])),
                            ('vr_gl_addr_ct', (YLeaf(YType.uint32, 'vr-gl-addr-ct'), ['int'])),
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

                        self.vr_global_address = YList(self)
                        self._segment_path = lambda: "nd-virtual-router" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter, ['interface_name', 'link_layer_address', 'context', 'state', 'flags', 'vr_gl_addr_ct'], name, value)


                    class LocalAddress(_Entity_):
                        """
                        IPV6 Link local address
                        
                        .. attribute:: ipv6_address
                        
                        	Address of type IPV6
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: valid_lifetime
                        
                        	Valid lifetime of a Prefix
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: pref_lifetime
                        
                        	Preffered lifetime of a Prefix
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: prefix_length
                        
                        	IPV6 Prefix length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: flags
                        
                        	Address flags
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2019-09-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress, self).__init__()

                            self.yang_name = "local-address"
                            self.yang_parent_name = "nd-virtual-router"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                ('valid_lifetime', (YLeaf(YType.uint32, 'valid-lifetime'), ['int'])),
                                ('pref_lifetime', (YLeaf(YType.uint32, 'pref-lifetime'), ['int'])),
                                ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                ('flags', (YLeaf(YType.uint32, 'flags'), ['int'])),
                            ])
                            self.ipv6_address = None
                            self.valid_lifetime = None
                            self.pref_lifetime = None
                            self.prefix_length = None
                            self.flags = None
                            self._segment_path = lambda: "local-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress, ['ipv6_address', 'valid_lifetime', 'pref_lifetime', 'prefix_length', 'flags'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                            return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress']['meta_info']


                    class VrGlobalAddress(_Entity_):
                        """
                        List of ND global addresses
                        
                        .. attribute:: ipv6_address
                        
                        	Address of type IPV6
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: valid_lifetime
                        
                        	Valid lifetime of a Prefix
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: pref_lifetime
                        
                        	Preffered lifetime of a Prefix
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: prefix_length
                        
                        	IPV6 Prefix length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: flags
                        
                        	Address flags
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2019-09-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress, self).__init__()

                            self.yang_name = "vr-global-address"
                            self.yang_parent_name = "nd-virtual-router"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                ('valid_lifetime', (YLeaf(YType.uint32, 'valid-lifetime'), ['int'])),
                                ('pref_lifetime', (YLeaf(YType.uint32, 'pref-lifetime'), ['int'])),
                                ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                ('flags', (YLeaf(YType.uint32, 'flags'), ['int'])),
                            ])
                            self.ipv6_address = None
                            self.valid_lifetime = None
                            self.pref_lifetime = None
                            self.prefix_length = None
                            self.flags = None
                            self._segment_path = lambda: "vr-global-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress, ['ipv6_address', 'valid_lifetime', 'pref_lifetime', 'prefix_length', 'flags'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                            return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters']['meta_info']


            class SlaacInterfaces(_Entity_):
                """
                IPv6 ND list of SLAAC MGMT interfaces for a
                specific node
                
                .. attribute:: slaac_interface
                
                	IPv6 ND operational data for a specific slaac interface
                	**type**\: list of  		 :py:class:`SlaacInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2019-09-26'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces, self).__init__()

                    self.yang_name = "slaac-interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("slaac-interface", ("slaac_interface", Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface))])
                    self._leafs = OrderedDict()

                    self.slaac_interface = YList(self)
                    self._segment_path = lambda: "slaac-interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces, [], name, value)


                class SlaacInterface(_Entity_):
                    """
                    IPv6 ND operational data for a specific slaac
                    interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: router_advert_detail
                    
                    	IPv6 ND operational data for a specific slaac interface
                    	**type**\:  :py:class:`RouterAdvertDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2019-09-26'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface, self).__init__()

                        self.yang_name = "slaac-interface"
                        self.yang_parent_name = "slaac-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("router-advert-detail", ("router_advert_detail", Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None

                        self.router_advert_detail = Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail()
                        self.router_advert_detail.parent = self
                        self._children_name_map["router_advert_detail"] = "router-advert-detail"
                        self._segment_path = lambda: "slaac-interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface, ['interface_name'], name, value)


                    class RouterAdvertDetail(_Entity_):
                        """
                        IPv6 ND operational data for a specific
                        slaac interface
                        
                        .. attribute:: idb
                        
                        	interface database
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: ra
                        
                        	slaac db
                        	**type**\: list of  		 :py:class:`Ra <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2019-09-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail, self).__init__()

                            self.yang_name = "router-advert-detail"
                            self.yang_parent_name = "slaac-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("ra", ("ra", Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra))])
                            self._leafs = OrderedDict([
                                ('idb', (YLeaf(YType.str, 'idb'), ['str'])),
                            ])
                            self.idb = None

                            self.ra = YList(self)
                            self._segment_path = lambda: "router-advert-detail"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail, ['idb'], name, value)


                        class Ra(_Entity_):
                            """
                            slaac db
                            
                            .. attribute:: elapsed_ra_time
                            
                            	elapsedRATime
                            	**type**\:  :py:class:`ElapsedRaTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ElapsedRaTime>`
                            
                            	**config**\: False
                            
                            .. attribute:: reachable_time
                            
                            	common reachabletime
                            	**type**\:  :py:class:`ReachableTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ReachableTime>`
                            
                            	**config**\: False
                            
                            .. attribute:: retrans_time
                            
                            	RA retransmit time
                            	**type**\:  :py:class:`RetransTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.RetransTime>`
                            
                            	**config**\: False
                            
                            .. attribute:: address
                            
                            	address of type IPV6
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            .. attribute:: hops
                            
                            	number of intermediate devices between source and destination
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: flags
                            
                            	RA flags
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: life_time
                            
                            	active time
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: mtu
                            
                            	maximum transmission unit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: err_msg
                            
                            	message having the error info
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: vrf_id
                            
                            	virtual routing and forwarding id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: u6_tbl_id
                            
                            	tbl id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: rib_protoid
                            
                            	proto id
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: default_router
                            
                            	router
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: reachability
                            
                            	reach
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: prefix_q
                            
                            	Prefix Queue
                            	**type**\: list of  		 :py:class:`PrefixQ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.PrefixQ>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ipv6-nd-oper'
                            _revision = '2019-09-26'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra, self).__init__()

                                self.yang_name = "ra"
                                self.yang_parent_name = "router-advert-detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("elapsed-ra-time", ("elapsed_ra_time", Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ElapsedRaTime)), ("reachable-time", ("reachable_time", Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ReachableTime)), ("retrans-time", ("retrans_time", Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.RetransTime)), ("prefix-q", ("prefix_q", Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.PrefixQ))])
                                self._leafs = OrderedDict([
                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                    ('hops', (YLeaf(YType.uint32, 'hops'), ['int'])),
                                    ('flags', (YLeaf(YType.uint32, 'flags'), ['int'])),
                                    ('life_time', (YLeaf(YType.uint32, 'life-time'), ['int'])),
                                    ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                                    ('err_msg', (YLeaf(YType.boolean, 'err-msg'), ['bool'])),
                                    ('vrf_id', (YLeaf(YType.uint32, 'vrf-id'), ['int'])),
                                    ('u6_tbl_id', (YLeaf(YType.uint32, 'u6-tbl-id'), ['int'])),
                                    ('rib_protoid', (YLeaf(YType.uint16, 'rib-protoid'), ['int'])),
                                    ('default_router', (YLeaf(YType.boolean, 'default-router'), ['bool'])),
                                    ('reachability', (YLeaf(YType.uint32, 'reachability'), ['int'])),
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

                                self.reachable_time = Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ReachableTime()
                                self.reachable_time.parent = self
                                self._children_name_map["reachable_time"] = "reachable-time"

                                self.retrans_time = Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.RetransTime()
                                self.retrans_time.parent = self
                                self._children_name_map["retrans_time"] = "retrans-time"

                                self.prefix_q = YList(self)
                                self._segment_path = lambda: "ra"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra, ['address', 'hops', 'flags', 'life_time', 'mtu', 'err_msg', 'vrf_id', 'u6_tbl_id', 'rib_protoid', 'default_router', 'reachability'], name, value)


                            class ElapsedRaTime(_Entity_):
                                """
                                elapsedRATime
                                
                                .. attribute:: seconds
                                
                                	Number of seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'ipv6-nd-oper'
                                _revision = '2019-09-26'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ElapsedRaTime, self).__init__()

                                    self.yang_name = "elapsed-ra-time"
                                    self.yang_parent_name = "ra"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                                    ])
                                    self.seconds = None
                                    self._segment_path = lambda: "elapsed-ra-time"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ElapsedRaTime, ['seconds'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ElapsedRaTime']['meta_info']


                            class ReachableTime(_Entity_):
                                """
                                common reachabletime
                                
                                .. attribute:: seconds
                                
                                	Number of seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'ipv6-nd-oper'
                                _revision = '2019-09-26'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ReachableTime, self).__init__()

                                    self.yang_name = "reachable-time"
                                    self.yang_parent_name = "ra"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                                    ])
                                    self.seconds = None
                                    self._segment_path = lambda: "reachable-time"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ReachableTime, ['seconds'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.ReachableTime']['meta_info']


                            class RetransTime(_Entity_):
                                """
                                RA retransmit time
                                
                                .. attribute:: seconds
                                
                                	Number of seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'ipv6-nd-oper'
                                _revision = '2019-09-26'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.RetransTime, self).__init__()

                                    self.yang_name = "retrans-time"
                                    self.yang_parent_name = "ra"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                                    ])
                                    self.seconds = None
                                    self._segment_path = lambda: "retrans-time"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.RetransTime, ['seconds'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.RetransTime']['meta_info']


                            class PrefixQ(_Entity_):
                                """
                                Prefix Queue
                                
                                .. attribute:: prefix_address
                                
                                	IPV6 Prefix address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                .. attribute:: eui64
                                
                                	IPv6 Auto generated address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                .. attribute:: valid_life_time
                                
                                	IPV6 Prefix Valid Life Time
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: preferred_life_time
                                
                                	IPV6 Prefix Preferred Life Time
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: prefix_len
                                
                                	IPV6 Prefix Length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: flags
                                
                                	IPv6 Address Specific Flags
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: pfx_flags
                                
                                	Prefix Address Specific Flags
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv6-nd-oper'
                                _revision = '2019-09-26'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.PrefixQ, self).__init__()

                                    self.yang_name = "prefix-q"
                                    self.yang_parent_name = "ra"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('prefix_address', (YLeaf(YType.str, 'prefix-address'), ['str'])),
                                        ('eui64', (YLeaf(YType.str, 'eui64'), ['str'])),
                                        ('valid_life_time', (YLeaf(YType.uint32, 'valid-life-time'), ['int'])),
                                        ('preferred_life_time', (YLeaf(YType.uint32, 'preferred-life-time'), ['int'])),
                                        ('prefix_len', (YLeaf(YType.uint32, 'prefix-len'), ['int'])),
                                        ('flags', (YLeaf(YType.uint32, 'flags'), ['int'])),
                                        ('pfx_flags', (YLeaf(YType.uint32, 'pfx-flags'), ['int'])),
                                    ])
                                    self.prefix_address = None
                                    self.eui64 = None
                                    self.valid_life_time = None
                                    self.preferred_life_time = None
                                    self.prefix_len = None
                                    self.flags = None
                                    self.pfx_flags = None
                                    self._segment_path = lambda: "prefix-q"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.PrefixQ, ['prefix_address', 'eui64', 'valid_life_time', 'preferred_life_time', 'prefix_len', 'flags', 'pfx_flags'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra.PrefixQ']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                                return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail.Ra']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                            return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface.RouterAdvertDetail']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                        return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces.SlaacInterface']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                    return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node.SlaacInterfaces']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
                return meta._meta_table['Ipv6NodeDiscovery.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
            return meta._meta_table['Ipv6NodeDiscovery.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = Ipv6NodeDiscovery()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_oper as meta
        return meta._meta_table['Ipv6NodeDiscovery']['meta_info']


