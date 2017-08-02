""" Cisco_IOS_XR_ipv6_nd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-nd package operational data.

This module contains definitions
for the following management objects\:
  ipv6\-node\-discovery\: IPv6 node discovery operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ipv6NdBndlState(Enum):
    """
    Ipv6NdBndlState

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
    Ipv6NdMediaEncap

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
    Ipv6NdNeighborOrigin

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
    Ipv6NdShState

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
    Ipv6NdShVrFlags

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
    Ipv6NdShVrState

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
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes>`
    
    

    """

    _prefix = 'ipv6-nd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ipv6NodeDiscovery, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6-node-discovery"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-nd-oper"

        self.nodes = Ipv6NodeDiscovery.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        IPv6 node discovery list of nodes
        
        .. attribute:: node
        
        	IPv6 node discovery operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node>`
        
        

        """

        _prefix = 'ipv6-nd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv6NodeDiscovery.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ipv6-node-discovery"

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
                        super(Ipv6NodeDiscovery.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv6NodeDiscovery.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            IPv6 node discovery operational data for a
            particular node
            
            .. attribute:: node_name  <key>
            
            	The node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: bundle_interfaces
            
            	IPv6 ND list of bundle interfaces for a specific node
            	**type**\:   :py:class:`BundleInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces>`
            
            .. attribute:: bundle_nodes
            
            	IPv6 ND list of bundle nodes for a specific node
            	**type**\:   :py:class:`BundleNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleNodes>`
            
            .. attribute:: interfaces
            
            	IPv6 node discovery list of interfaces for a specific node
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.Interfaces>`
            
            .. attribute:: nd_virtual_routers
            
            	IPv6 ND virtual router information for a specific interface
            	**type**\:   :py:class:`NdVirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters>`
            
            .. attribute:: neighbor_interfaces
            
            	IPv6 node discovery list of neighbor interfaces
            	**type**\:   :py:class:`NeighborInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces>`
            
            .. attribute:: neighbor_summary
            
            	IPv6 Neighbor summary
            	**type**\:   :py:class:`NeighborSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary>`
            
            

            """

            _prefix = 'ipv6-nd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv6NodeDiscovery.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.bundle_interfaces = Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces()
                self.bundle_interfaces.parent = self
                self._children_name_map["bundle_interfaces"] = "bundle-interfaces"
                self._children_yang_names.add("bundle-interfaces")

                self.bundle_nodes = Ipv6NodeDiscovery.Nodes.Node.BundleNodes()
                self.bundle_nodes.parent = self
                self._children_name_map["bundle_nodes"] = "bundle-nodes"
                self._children_yang_names.add("bundle-nodes")

                self.interfaces = Ipv6NodeDiscovery.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.nd_virtual_routers = Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters()
                self.nd_virtual_routers.parent = self
                self._children_name_map["nd_virtual_routers"] = "nd-virtual-routers"
                self._children_yang_names.add("nd-virtual-routers")

                self.neighbor_interfaces = Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces()
                self.neighbor_interfaces.parent = self
                self._children_name_map["neighbor_interfaces"] = "neighbor-interfaces"
                self._children_yang_names.add("neighbor-interfaces")

                self.neighbor_summary = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary()
                self.neighbor_summary.parent = self
                self._children_name_map["neighbor_summary"] = "neighbor-summary"
                self._children_yang_names.add("neighbor-summary")

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
                            super(Ipv6NodeDiscovery.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv6NodeDiscovery.Nodes.Node, self).__setattr__(name, value)


            class NeighborInterfaces(Entity):
                """
                IPv6 node discovery list of neighbor
                interfaces
                
                .. attribute:: neighbor_interface
                
                	IPv6 node discovery neighbor interface
                	**type**\: list of    :py:class:`NeighborInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface>`
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces, self).__init__()

                    self.yang_name = "neighbor-interfaces"
                    self.yang_parent_name = "node"

                    self.neighbor_interface = YList(self)

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
                                super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces, self).__setattr__(name, value)


                class NeighborInterface(Entity):
                    """
                    IPv6 node discovery neighbor interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: host_addresses
                    
                    	IPv6 node discovery list of neighbor host addresses
                    	**type**\:   :py:class:`HostAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses>`
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface, self).__init__()

                        self.yang_name = "neighbor-interface"
                        self.yang_parent_name = "neighbor-interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.host_addresses = Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses()
                        self.host_addresses.parent = self
                        self._children_name_map["host_addresses"] = "host-addresses"
                        self._children_yang_names.add("host-addresses")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface, self).__setattr__(name, value)


                    class HostAddresses(Entity):
                        """
                        IPv6 node discovery list of neighbor host
                        addresses
                        
                        .. attribute:: host_address
                        
                        	IPv6 Neighbor detailed information
                        	**type**\: list of    :py:class:`HostAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress>`
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses, self).__init__()

                            self.yang_name = "host-addresses"
                            self.yang_parent_name = "neighbor-interface"

                            self.host_address = YList(self)

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
                                        super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses, self).__setattr__(name, value)


                        class HostAddress(Entity):
                            """
                            IPv6 Neighbor detailed information
                            
                            .. attribute:: host_address  <key>
                            
                            	Host Address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: encapsulation
                            
                            	Preferred media encap type
                            	**type**\:   :py:class:`Ipv6NdMediaEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdMediaEncap>`
                            
                            .. attribute:: interface_name
                            
                            	Interface name
                            	**type**\:  str
                            
                            .. attribute:: is_router
                            
                            	IsRouter
                            	**type**\:  bool
                            
                            .. attribute:: last_reached_time
                            
                            	Last time of reachability
                            	**type**\:   :py:class:`LastReachedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime>`
                            
                            .. attribute:: link_layer_address
                            
                            	Link\-Layer Address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: location
                            
                            	Location where the neighbor entry exists
                            	**type**\:  str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: origin_encapsulation
                            
                            	Neighbor origin
                            	**type**\:   :py:class:`Ipv6NdNeighborOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdNeighborOrigin>`
                            
                            .. attribute:: reachability_state
                            
                            	Current state
                            	**type**\:   :py:class:`Ipv6NdShState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdShState>`
                            
                            .. attribute:: selected_encapsulation
                            
                            	Selected media encap
                            	**type**\:   :py:class:`Ipv6NdMediaEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdMediaEncap>`
                            
                            .. attribute:: serg_flags
                            
                            	ND serg flags for this entry
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-nd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress, self).__init__()

                                self.yang_name = "host-address"
                                self.yang_parent_name = "host-addresses"

                                self.host_address = YLeaf(YType.str, "host-address")

                                self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.is_router = YLeaf(YType.boolean, "is-router")

                                self.link_layer_address = YLeaf(YType.str, "link-layer-address")

                                self.location = YLeaf(YType.str, "location")

                                self.origin_encapsulation = YLeaf(YType.enumeration, "origin-encapsulation")

                                self.reachability_state = YLeaf(YType.enumeration, "reachability-state")

                                self.selected_encapsulation = YLeaf(YType.enumeration, "selected-encapsulation")

                                self.serg_flags = YLeaf(YType.uint32, "serg-flags")

                                self.last_reached_time = Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime()
                                self.last_reached_time.parent = self
                                self._children_name_map["last_reached_time"] = "last-reached-time"
                                self._children_yang_names.add("last-reached-time")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("host_address",
                                                "encapsulation",
                                                "interface_name",
                                                "is_router",
                                                "link_layer_address",
                                                "location",
                                                "origin_encapsulation",
                                                "reachability_state",
                                                "selected_encapsulation",
                                                "serg_flags") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress, self).__setattr__(name, value)


                            class LastReachedTime(Entity):
                                """
                                Last time of reachability
                                
                                .. attribute:: seconds
                                
                                	Number of seconds
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'ipv6-nd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime, self).__init__()

                                    self.yang_name = "last-reached-time"
                                    self.yang_parent_name = "host-address"

                                    self.seconds = YLeaf(YType.uint32, "seconds")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("seconds") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime, self).__setattr__(name, value)

                                def has_data(self):
                                    return self.seconds.is_set

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.seconds.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "last-reached-time" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.seconds.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "seconds"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "seconds"):
                                        self.seconds = value
                                        self.seconds.value_namespace = name_space
                                        self.seconds.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.host_address.is_set or
                                    self.encapsulation.is_set or
                                    self.interface_name.is_set or
                                    self.is_router.is_set or
                                    self.link_layer_address.is_set or
                                    self.location.is_set or
                                    self.origin_encapsulation.is_set or
                                    self.reachability_state.is_set or
                                    self.selected_encapsulation.is_set or
                                    self.serg_flags.is_set or
                                    (self.last_reached_time is not None and self.last_reached_time.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.host_address.yfilter != YFilter.not_set or
                                    self.encapsulation.yfilter != YFilter.not_set or
                                    self.interface_name.yfilter != YFilter.not_set or
                                    self.is_router.yfilter != YFilter.not_set or
                                    self.link_layer_address.yfilter != YFilter.not_set or
                                    self.location.yfilter != YFilter.not_set or
                                    self.origin_encapsulation.yfilter != YFilter.not_set or
                                    self.reachability_state.yfilter != YFilter.not_set or
                                    self.selected_encapsulation.yfilter != YFilter.not_set or
                                    self.serg_flags.yfilter != YFilter.not_set or
                                    (self.last_reached_time is not None and self.last_reached_time.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "host-address" + "[host-address='" + self.host_address.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.host_address.is_set or self.host_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.host_address.get_name_leafdata())
                                if (self.encapsulation.is_set or self.encapsulation.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.encapsulation.get_name_leafdata())
                                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                                if (self.is_router.is_set or self.is_router.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_router.get_name_leafdata())
                                if (self.link_layer_address.is_set or self.link_layer_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.link_layer_address.get_name_leafdata())
                                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.location.get_name_leafdata())
                                if (self.origin_encapsulation.is_set or self.origin_encapsulation.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.origin_encapsulation.get_name_leafdata())
                                if (self.reachability_state.is_set or self.reachability_state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.reachability_state.get_name_leafdata())
                                if (self.selected_encapsulation.is_set or self.selected_encapsulation.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.selected_encapsulation.get_name_leafdata())
                                if (self.serg_flags.is_set or self.serg_flags.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.serg_flags.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "last-reached-time"):
                                    if (self.last_reached_time is None):
                                        self.last_reached_time = Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime()
                                        self.last_reached_time.parent = self
                                        self._children_name_map["last_reached_time"] = "last-reached-time"
                                    return self.last_reached_time

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "last-reached-time" or name == "host-address" or name == "encapsulation" or name == "interface-name" or name == "is-router" or name == "link-layer-address" or name == "location" or name == "origin-encapsulation" or name == "reachability-state" or name == "selected-encapsulation" or name == "serg-flags"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "host-address"):
                                    self.host_address = value
                                    self.host_address.value_namespace = name_space
                                    self.host_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "encapsulation"):
                                    self.encapsulation = value
                                    self.encapsulation.value_namespace = name_space
                                    self.encapsulation.value_namespace_prefix = name_space_prefix
                                if(value_path == "interface-name"):
                                    self.interface_name = value
                                    self.interface_name.value_namespace = name_space
                                    self.interface_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-router"):
                                    self.is_router = value
                                    self.is_router.value_namespace = name_space
                                    self.is_router.value_namespace_prefix = name_space_prefix
                                if(value_path == "link-layer-address"):
                                    self.link_layer_address = value
                                    self.link_layer_address.value_namespace = name_space
                                    self.link_layer_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "location"):
                                    self.location = value
                                    self.location.value_namespace = name_space
                                    self.location.value_namespace_prefix = name_space_prefix
                                if(value_path == "origin-encapsulation"):
                                    self.origin_encapsulation = value
                                    self.origin_encapsulation.value_namespace = name_space
                                    self.origin_encapsulation.value_namespace_prefix = name_space_prefix
                                if(value_path == "reachability-state"):
                                    self.reachability_state = value
                                    self.reachability_state.value_namespace = name_space
                                    self.reachability_state.value_namespace_prefix = name_space_prefix
                                if(value_path == "selected-encapsulation"):
                                    self.selected_encapsulation = value
                                    self.selected_encapsulation.value_namespace = name_space
                                    self.selected_encapsulation.value_namespace_prefix = name_space_prefix
                                if(value_path == "serg-flags"):
                                    self.serg_flags = value
                                    self.serg_flags.value_namespace = name_space
                                    self.serg_flags.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.host_address:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.host_address:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "host-addresses" + path_buffer

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

                            if (child_yang_name == "host-address"):
                                for c in self.host_address:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.host_address.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "host-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            (self.host_addresses is not None and self.host_addresses.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            (self.host_addresses is not None and self.host_addresses.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "neighbor-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

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

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "host-addresses"):
                            if (self.host_addresses is None):
                                self.host_addresses = Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses()
                                self.host_addresses.parent = self
                                self._children_name_map["host_addresses"] = "host-addresses"
                            return self.host_addresses

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "host-addresses" or name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.neighbor_interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.neighbor_interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "neighbor-interfaces" + path_buffer

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

                    if (child_yang_name == "neighbor-interface"):
                        for c in self.neighbor_interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.neighbor_interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "neighbor-interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class NeighborSummary(Entity):
                """
                IPv6 Neighbor summary
                
                .. attribute:: dynamic
                
                	Dynamic neighbor summary
                	**type**\:   :py:class:`Dynamic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic>`
                
                .. attribute:: multicast
                
                	Multicast neighbor summary
                	**type**\:   :py:class:`Multicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast>`
                
                .. attribute:: static
                
                	Static neighbor summary
                	**type**\:   :py:class:`Static <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static>`
                
                .. attribute:: total_neighbor_entries
                
                	Total number of entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary, self).__init__()

                    self.yang_name = "neighbor-summary"
                    self.yang_parent_name = "node"

                    self.total_neighbor_entries = YLeaf(YType.uint32, "total-neighbor-entries")

                    self.dynamic = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic()
                    self.dynamic.parent = self
                    self._children_name_map["dynamic"] = "dynamic"
                    self._children_yang_names.add("dynamic")

                    self.multicast = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast()
                    self.multicast.parent = self
                    self._children_name_map["multicast"] = "multicast"
                    self._children_yang_names.add("multicast")

                    self.static = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static()
                    self.static.parent = self
                    self._children_name_map["static"] = "static"
                    self._children_yang_names.add("static")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("total_neighbor_entries") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary, self).__setattr__(name, value)


                class Multicast(Entity):
                    """
                    Multicast neighbor summary
                    
                    .. attribute:: delayed_entries
                    
                    	Total delayed entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: deleted_entries
                    
                    	Total deleted entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: incomplete_entries
                    
                    	Total incomplete entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: probe_entries
                    
                    	Total probe entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reachable_entries
                    
                    	Total reachable entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: stale_entries
                    
                    	Total stale entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subtotal_neighbor_entries
                    
                    	Total number of entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast, self).__init__()

                        self.yang_name = "multicast"
                        self.yang_parent_name = "neighbor-summary"

                        self.delayed_entries = YLeaf(YType.uint32, "delayed-entries")

                        self.deleted_entries = YLeaf(YType.uint32, "deleted-entries")

                        self.incomplete_entries = YLeaf(YType.uint32, "incomplete-entries")

                        self.probe_entries = YLeaf(YType.uint32, "probe-entries")

                        self.reachable_entries = YLeaf(YType.uint32, "reachable-entries")

                        self.stale_entries = YLeaf(YType.uint32, "stale-entries")

                        self.subtotal_neighbor_entries = YLeaf(YType.uint32, "subtotal-neighbor-entries")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("delayed_entries",
                                        "deleted_entries",
                                        "incomplete_entries",
                                        "probe_entries",
                                        "reachable_entries",
                                        "stale_entries",
                                        "subtotal_neighbor_entries") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.delayed_entries.is_set or
                            self.deleted_entries.is_set or
                            self.incomplete_entries.is_set or
                            self.probe_entries.is_set or
                            self.reachable_entries.is_set or
                            self.stale_entries.is_set or
                            self.subtotal_neighbor_entries.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.delayed_entries.yfilter != YFilter.not_set or
                            self.deleted_entries.yfilter != YFilter.not_set or
                            self.incomplete_entries.yfilter != YFilter.not_set or
                            self.probe_entries.yfilter != YFilter.not_set or
                            self.reachable_entries.yfilter != YFilter.not_set or
                            self.stale_entries.yfilter != YFilter.not_set or
                            self.subtotal_neighbor_entries.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "multicast" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.delayed_entries.is_set or self.delayed_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.delayed_entries.get_name_leafdata())
                        if (self.deleted_entries.is_set or self.deleted_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.deleted_entries.get_name_leafdata())
                        if (self.incomplete_entries.is_set or self.incomplete_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.incomplete_entries.get_name_leafdata())
                        if (self.probe_entries.is_set or self.probe_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.probe_entries.get_name_leafdata())
                        if (self.reachable_entries.is_set or self.reachable_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reachable_entries.get_name_leafdata())
                        if (self.stale_entries.is_set or self.stale_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.stale_entries.get_name_leafdata())
                        if (self.subtotal_neighbor_entries.is_set or self.subtotal_neighbor_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subtotal_neighbor_entries.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "delayed-entries" or name == "deleted-entries" or name == "incomplete-entries" or name == "probe-entries" or name == "reachable-entries" or name == "stale-entries" or name == "subtotal-neighbor-entries"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "delayed-entries"):
                            self.delayed_entries = value
                            self.delayed_entries.value_namespace = name_space
                            self.delayed_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "deleted-entries"):
                            self.deleted_entries = value
                            self.deleted_entries.value_namespace = name_space
                            self.deleted_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "incomplete-entries"):
                            self.incomplete_entries = value
                            self.incomplete_entries.value_namespace = name_space
                            self.incomplete_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "probe-entries"):
                            self.probe_entries = value
                            self.probe_entries.value_namespace = name_space
                            self.probe_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "reachable-entries"):
                            self.reachable_entries = value
                            self.reachable_entries.value_namespace = name_space
                            self.reachable_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "stale-entries"):
                            self.stale_entries = value
                            self.stale_entries.value_namespace = name_space
                            self.stale_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "subtotal-neighbor-entries"):
                            self.subtotal_neighbor_entries = value
                            self.subtotal_neighbor_entries.value_namespace = name_space
                            self.subtotal_neighbor_entries.value_namespace_prefix = name_space_prefix


                class Static(Entity):
                    """
                    Static neighbor summary
                    
                    .. attribute:: delayed_entries
                    
                    	Total delayed entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: deleted_entries
                    
                    	Total deleted entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: incomplete_entries
                    
                    	Total incomplete entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: probe_entries
                    
                    	Total probe entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reachable_entries
                    
                    	Total reachable entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: stale_entries
                    
                    	Total stale entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subtotal_neighbor_entries
                    
                    	Total number of entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static, self).__init__()

                        self.yang_name = "static"
                        self.yang_parent_name = "neighbor-summary"

                        self.delayed_entries = YLeaf(YType.uint32, "delayed-entries")

                        self.deleted_entries = YLeaf(YType.uint32, "deleted-entries")

                        self.incomplete_entries = YLeaf(YType.uint32, "incomplete-entries")

                        self.probe_entries = YLeaf(YType.uint32, "probe-entries")

                        self.reachable_entries = YLeaf(YType.uint32, "reachable-entries")

                        self.stale_entries = YLeaf(YType.uint32, "stale-entries")

                        self.subtotal_neighbor_entries = YLeaf(YType.uint32, "subtotal-neighbor-entries")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("delayed_entries",
                                        "deleted_entries",
                                        "incomplete_entries",
                                        "probe_entries",
                                        "reachable_entries",
                                        "stale_entries",
                                        "subtotal_neighbor_entries") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.delayed_entries.is_set or
                            self.deleted_entries.is_set or
                            self.incomplete_entries.is_set or
                            self.probe_entries.is_set or
                            self.reachable_entries.is_set or
                            self.stale_entries.is_set or
                            self.subtotal_neighbor_entries.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.delayed_entries.yfilter != YFilter.not_set or
                            self.deleted_entries.yfilter != YFilter.not_set or
                            self.incomplete_entries.yfilter != YFilter.not_set or
                            self.probe_entries.yfilter != YFilter.not_set or
                            self.reachable_entries.yfilter != YFilter.not_set or
                            self.stale_entries.yfilter != YFilter.not_set or
                            self.subtotal_neighbor_entries.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "static" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.delayed_entries.is_set or self.delayed_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.delayed_entries.get_name_leafdata())
                        if (self.deleted_entries.is_set or self.deleted_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.deleted_entries.get_name_leafdata())
                        if (self.incomplete_entries.is_set or self.incomplete_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.incomplete_entries.get_name_leafdata())
                        if (self.probe_entries.is_set or self.probe_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.probe_entries.get_name_leafdata())
                        if (self.reachable_entries.is_set or self.reachable_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reachable_entries.get_name_leafdata())
                        if (self.stale_entries.is_set or self.stale_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.stale_entries.get_name_leafdata())
                        if (self.subtotal_neighbor_entries.is_set or self.subtotal_neighbor_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subtotal_neighbor_entries.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "delayed-entries" or name == "deleted-entries" or name == "incomplete-entries" or name == "probe-entries" or name == "reachable-entries" or name == "stale-entries" or name == "subtotal-neighbor-entries"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "delayed-entries"):
                            self.delayed_entries = value
                            self.delayed_entries.value_namespace = name_space
                            self.delayed_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "deleted-entries"):
                            self.deleted_entries = value
                            self.deleted_entries.value_namespace = name_space
                            self.deleted_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "incomplete-entries"):
                            self.incomplete_entries = value
                            self.incomplete_entries.value_namespace = name_space
                            self.incomplete_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "probe-entries"):
                            self.probe_entries = value
                            self.probe_entries.value_namespace = name_space
                            self.probe_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "reachable-entries"):
                            self.reachable_entries = value
                            self.reachable_entries.value_namespace = name_space
                            self.reachable_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "stale-entries"):
                            self.stale_entries = value
                            self.stale_entries.value_namespace = name_space
                            self.stale_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "subtotal-neighbor-entries"):
                            self.subtotal_neighbor_entries = value
                            self.subtotal_neighbor_entries.value_namespace = name_space
                            self.subtotal_neighbor_entries.value_namespace_prefix = name_space_prefix


                class Dynamic(Entity):
                    """
                    Dynamic neighbor summary
                    
                    .. attribute:: delayed_entries
                    
                    	Total delayed entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: deleted_entries
                    
                    	Total deleted entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: incomplete_entries
                    
                    	Total incomplete entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: probe_entries
                    
                    	Total probe entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reachable_entries
                    
                    	Total reachable entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: stale_entries
                    
                    	Total stale entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subtotal_neighbor_entries
                    
                    	Total number of entries
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic, self).__init__()

                        self.yang_name = "dynamic"
                        self.yang_parent_name = "neighbor-summary"

                        self.delayed_entries = YLeaf(YType.uint32, "delayed-entries")

                        self.deleted_entries = YLeaf(YType.uint32, "deleted-entries")

                        self.incomplete_entries = YLeaf(YType.uint32, "incomplete-entries")

                        self.probe_entries = YLeaf(YType.uint32, "probe-entries")

                        self.reachable_entries = YLeaf(YType.uint32, "reachable-entries")

                        self.stale_entries = YLeaf(YType.uint32, "stale-entries")

                        self.subtotal_neighbor_entries = YLeaf(YType.uint32, "subtotal-neighbor-entries")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("delayed_entries",
                                        "deleted_entries",
                                        "incomplete_entries",
                                        "probe_entries",
                                        "reachable_entries",
                                        "stale_entries",
                                        "subtotal_neighbor_entries") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.delayed_entries.is_set or
                            self.deleted_entries.is_set or
                            self.incomplete_entries.is_set or
                            self.probe_entries.is_set or
                            self.reachable_entries.is_set or
                            self.stale_entries.is_set or
                            self.subtotal_neighbor_entries.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.delayed_entries.yfilter != YFilter.not_set or
                            self.deleted_entries.yfilter != YFilter.not_set or
                            self.incomplete_entries.yfilter != YFilter.not_set or
                            self.probe_entries.yfilter != YFilter.not_set or
                            self.reachable_entries.yfilter != YFilter.not_set or
                            self.stale_entries.yfilter != YFilter.not_set or
                            self.subtotal_neighbor_entries.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "dynamic" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.delayed_entries.is_set or self.delayed_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.delayed_entries.get_name_leafdata())
                        if (self.deleted_entries.is_set or self.deleted_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.deleted_entries.get_name_leafdata())
                        if (self.incomplete_entries.is_set or self.incomplete_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.incomplete_entries.get_name_leafdata())
                        if (self.probe_entries.is_set or self.probe_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.probe_entries.get_name_leafdata())
                        if (self.reachable_entries.is_set or self.reachable_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reachable_entries.get_name_leafdata())
                        if (self.stale_entries.is_set or self.stale_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.stale_entries.get_name_leafdata())
                        if (self.subtotal_neighbor_entries.is_set or self.subtotal_neighbor_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subtotal_neighbor_entries.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "delayed-entries" or name == "deleted-entries" or name == "incomplete-entries" or name == "probe-entries" or name == "reachable-entries" or name == "stale-entries" or name == "subtotal-neighbor-entries"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "delayed-entries"):
                            self.delayed_entries = value
                            self.delayed_entries.value_namespace = name_space
                            self.delayed_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "deleted-entries"):
                            self.deleted_entries = value
                            self.deleted_entries.value_namespace = name_space
                            self.deleted_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "incomplete-entries"):
                            self.incomplete_entries = value
                            self.incomplete_entries.value_namespace = name_space
                            self.incomplete_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "probe-entries"):
                            self.probe_entries = value
                            self.probe_entries.value_namespace = name_space
                            self.probe_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "reachable-entries"):
                            self.reachable_entries = value
                            self.reachable_entries.value_namespace = name_space
                            self.reachable_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "stale-entries"):
                            self.stale_entries = value
                            self.stale_entries.value_namespace = name_space
                            self.stale_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "subtotal-neighbor-entries"):
                            self.subtotal_neighbor_entries = value
                            self.subtotal_neighbor_entries.value_namespace = name_space
                            self.subtotal_neighbor_entries.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.total_neighbor_entries.is_set or
                        (self.dynamic is not None and self.dynamic.has_data()) or
                        (self.multicast is not None and self.multicast.has_data()) or
                        (self.static is not None and self.static.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.total_neighbor_entries.yfilter != YFilter.not_set or
                        (self.dynamic is not None and self.dynamic.has_operation()) or
                        (self.multicast is not None and self.multicast.has_operation()) or
                        (self.static is not None and self.static.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "neighbor-summary" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.total_neighbor_entries.is_set or self.total_neighbor_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_neighbor_entries.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "dynamic"):
                        if (self.dynamic is None):
                            self.dynamic = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic()
                            self.dynamic.parent = self
                            self._children_name_map["dynamic"] = "dynamic"
                        return self.dynamic

                    if (child_yang_name == "multicast"):
                        if (self.multicast is None):
                            self.multicast = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast()
                            self.multicast.parent = self
                            self._children_name_map["multicast"] = "multicast"
                        return self.multicast

                    if (child_yang_name == "static"):
                        if (self.static is None):
                            self.static = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static()
                            self.static.parent = self
                            self._children_name_map["static"] = "static"
                        return self.static

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "dynamic" or name == "multicast" or name == "static" or name == "total-neighbor-entries"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "total-neighbor-entries"):
                        self.total_neighbor_entries = value
                        self.total_neighbor_entries.value_namespace = name_space
                        self.total_neighbor_entries.value_namespace_prefix = name_space_prefix


            class BundleNodes(Entity):
                """
                IPv6 ND list of bundle nodes for a specific
                node
                
                .. attribute:: bundle_node
                
                	IPv6 ND operational data for a specific bundle node
                	**type**\: list of    :py:class:`BundleNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode>`
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6NodeDiscovery.Nodes.Node.BundleNodes, self).__init__()

                    self.yang_name = "bundle-nodes"
                    self.yang_parent_name = "node"

                    self.bundle_node = YList(self)

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
                                super(Ipv6NodeDiscovery.Nodes.Node.BundleNodes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv6NodeDiscovery.Nodes.Node.BundleNodes, self).__setattr__(name, value)


                class BundleNode(Entity):
                    """
                    IPv6 ND operational data for a specific
                    bundle node
                    
                    .. attribute:: node_name  <key>
                    
                    	The bundle node name
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: age
                    
                    	Uptime of node (secs)
                    	**type**\:   :py:class:`Age <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age>`
                    
                    .. attribute:: group_id
                    
                    	Group ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: process_name
                    
                    	Process Name
                    	**type**\:  str
                    
                    .. attribute:: received_packets
                    
                    	Total packet receives
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_sequence_number
                    
                    	Received sequence num
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent_packets
                    
                    	Total packet sends
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent_sequence_number
                    
                    	Sent sequence num
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: state
                    
                    	State
                    	**type**\:   :py:class:`Ipv6NdBndlState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdBndlState>`
                    
                    .. attribute:: state_changes
                    
                    	State changes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode, self).__init__()

                        self.yang_name = "bundle-node"
                        self.yang_parent_name = "bundle-nodes"

                        self.node_name = YLeaf(YType.str, "node-name")

                        self.group_id = YLeaf(YType.uint32, "group-id")

                        self.process_name = YLeaf(YType.str, "process-name")

                        self.received_packets = YLeaf(YType.uint32, "received-packets")

                        self.received_sequence_number = YLeaf(YType.uint32, "received-sequence-number")

                        self.sent_packets = YLeaf(YType.uint32, "sent-packets")

                        self.sent_sequence_number = YLeaf(YType.uint32, "sent-sequence-number")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.state_changes = YLeaf(YType.uint32, "state-changes")

                        self.age = Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age()
                        self.age.parent = self
                        self._children_name_map["age"] = "age"
                        self._children_yang_names.add("age")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("node_name",
                                        "group_id",
                                        "process_name",
                                        "received_packets",
                                        "received_sequence_number",
                                        "sent_packets",
                                        "sent_sequence_number",
                                        "state",
                                        "state_changes") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode, self).__setattr__(name, value)


                    class Age(Entity):
                        """
                        Uptime of node (secs)
                        
                        .. attribute:: seconds
                        
                        	Number of seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age, self).__init__()

                            self.yang_name = "age"
                            self.yang_parent_name = "bundle-node"

                            self.seconds = YLeaf(YType.uint32, "seconds")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("seconds") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age, self).__setattr__(name, value)

                        def has_data(self):
                            return self.seconds.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.seconds.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "age" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.seconds.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "seconds"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "seconds"):
                                self.seconds = value
                                self.seconds.value_namespace = name_space
                                self.seconds.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.node_name.is_set or
                            self.group_id.is_set or
                            self.process_name.is_set or
                            self.received_packets.is_set or
                            self.received_sequence_number.is_set or
                            self.sent_packets.is_set or
                            self.sent_sequence_number.is_set or
                            self.state.is_set or
                            self.state_changes.is_set or
                            (self.age is not None and self.age.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.node_name.yfilter != YFilter.not_set or
                            self.group_id.yfilter != YFilter.not_set or
                            self.process_name.yfilter != YFilter.not_set or
                            self.received_packets.yfilter != YFilter.not_set or
                            self.received_sequence_number.yfilter != YFilter.not_set or
                            self.sent_packets.yfilter != YFilter.not_set or
                            self.sent_sequence_number.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.state_changes.yfilter != YFilter.not_set or
                            (self.age is not None and self.age.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bundle-node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.node_name.get_name_leafdata())
                        if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_id.get_name_leafdata())
                        if (self.process_name.is_set or self.process_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.process_name.get_name_leafdata())
                        if (self.received_packets.is_set or self.received_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.received_packets.get_name_leafdata())
                        if (self.received_sequence_number.is_set or self.received_sequence_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.received_sequence_number.get_name_leafdata())
                        if (self.sent_packets.is_set or self.sent_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sent_packets.get_name_leafdata())
                        if (self.sent_sequence_number.is_set or self.sent_sequence_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sent_sequence_number.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.state_changes.is_set or self.state_changes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state_changes.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "age"):
                            if (self.age is None):
                                self.age = Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age()
                                self.age.parent = self
                                self._children_name_map["age"] = "age"
                            return self.age

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "age" or name == "node-name" or name == "group-id" or name == "process-name" or name == "received-packets" or name == "received-sequence-number" or name == "sent-packets" or name == "sent-sequence-number" or name == "state" or name == "state-changes"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "node-name"):
                            self.node_name = value
                            self.node_name.value_namespace = name_space
                            self.node_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "group-id"):
                            self.group_id = value
                            self.group_id.value_namespace = name_space
                            self.group_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "process-name"):
                            self.process_name = value
                            self.process_name.value_namespace = name_space
                            self.process_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "received-packets"):
                            self.received_packets = value
                            self.received_packets.value_namespace = name_space
                            self.received_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "received-sequence-number"):
                            self.received_sequence_number = value
                            self.received_sequence_number.value_namespace = name_space
                            self.received_sequence_number.value_namespace_prefix = name_space_prefix
                        if(value_path == "sent-packets"):
                            self.sent_packets = value
                            self.sent_packets.value_namespace = name_space
                            self.sent_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "sent-sequence-number"):
                            self.sent_sequence_number = value
                            self.sent_sequence_number.value_namespace = name_space
                            self.sent_sequence_number.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "state-changes"):
                            self.state_changes = value
                            self.state_changes.value_namespace = name_space
                            self.state_changes.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.bundle_node:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.bundle_node:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bundle-nodes" + path_buffer

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

                    if (child_yang_name == "bundle-node"):
                        for c in self.bundle_node:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.bundle_node.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bundle-node"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class BundleInterfaces(Entity):
                """
                IPv6 ND list of bundle interfaces for a
                specific node
                
                .. attribute:: bundle_interface
                
                	IPv6 ND operational data for a specific bundler interface
                	**type**\: list of    :py:class:`BundleInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface>`
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces, self).__init__()

                    self.yang_name = "bundle-interfaces"
                    self.yang_parent_name = "node"

                    self.bundle_interface = YList(self)

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
                                super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces, self).__setattr__(name, value)


                class BundleInterface(Entity):
                    """
                    IPv6 ND operational data for a specific
                    bundler interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: etype
                    
                    	etype
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: global_address
                    
                    	List of ND global addresses
                    	**type**\: list of    :py:class:`GlobalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress>`
                    
                    .. attribute:: iftype
                    
                    	Interface type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_interface_enabled
                    
                    	If true, interface is enabled
                    	**type**\:  bool
                    
                    .. attribute:: is_ipv6_enabled
                    
                    	If true, IPv6 is enabled
                    	**type**\:  bool
                    
                    .. attribute:: is_mpls_enabled
                    
                    	If true, MPLS is enabled
                    	**type**\:  bool
                    
                    .. attribute:: local_address
                    
                    	Link local address
                    	**type**\:   :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress>`
                    
                    .. attribute:: mac_addr
                    
                    	mac address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: mac_addr_size
                    
                    	mac address size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: member_link
                    
                    	List of member links
                    	**type**\:  list of int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: member_node
                    
                    	List of member nodes
                    	**type**\: list of    :py:class:`MemberNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode>`
                    
                    .. attribute:: mtu
                    
                    	MTU
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nd_parameters
                    
                    	ND interface parameters
                    	**type**\:   :py:class:`NdParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters>`
                    
                    .. attribute:: parent_interface_name
                    
                    	Parent interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: vlan_tag
                    
                    	vlan tag/id/ucv
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface, self).__init__()

                        self.yang_name = "bundle-interface"
                        self.yang_parent_name = "bundle-interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.etype = YLeaf(YType.uint32, "etype")

                        self.iftype = YLeaf(YType.uint32, "iftype")

                        self.is_interface_enabled = YLeaf(YType.boolean, "is-interface-enabled")

                        self.is_ipv6_enabled = YLeaf(YType.boolean, "is-ipv6-enabled")

                        self.is_mpls_enabled = YLeaf(YType.boolean, "is-mpls-enabled")

                        self.mac_addr = YLeaf(YType.str, "mac-addr")

                        self.mac_addr_size = YLeaf(YType.uint32, "mac-addr-size")

                        self.member_link = YLeafList(YType.uint32, "member-link")

                        self.mtu = YLeaf(YType.uint32, "mtu")

                        self.parent_interface_name = YLeaf(YType.str, "parent-interface-name")

                        self.vlan_tag = YLeaf(YType.uint16, "vlan-tag")

                        self.local_address = Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress()
                        self.local_address.parent = self
                        self._children_name_map["local_address"] = "local-address"
                        self._children_yang_names.add("local-address")

                        self.nd_parameters = Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters()
                        self.nd_parameters.parent = self
                        self._children_name_map["nd_parameters"] = "nd-parameters"
                        self._children_yang_names.add("nd-parameters")

                        self.global_address = YList(self)
                        self.member_node = YList(self)

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
                                        "etype",
                                        "iftype",
                                        "is_interface_enabled",
                                        "is_ipv6_enabled",
                                        "is_mpls_enabled",
                                        "mac_addr",
                                        "mac_addr_size",
                                        "member_link",
                                        "mtu",
                                        "parent_interface_name",
                                        "vlan_tag") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface, self).__setattr__(name, value)


                    class NdParameters(Entity):
                        """
                        ND interface parameters
                        
                        .. attribute:: complete_glean_count
                        
                        	Completed GLEAN entry count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: complete_protocol_count
                        
                        	Completed PROTO entry Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dad_attempts
                        
                        	DAD attempt count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_glean_req_count
                        
                        	Dropped GLEAN entry lequest count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_protocol_req_count
                        
                        	Dropped PROTO entry request count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incomplete_glean_count
                        
                        	Incomplete GLEAN entry count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incomplete_protocol_count
                        
                        	Incomplete PROTO entry count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_dad_enabled
                        
                        	If true, DAD (D.. A.. D..) is enabled otherwise it is disabled
                        	**type**\:  bool
                        
                        .. attribute:: is_dhcp_managed
                        
                        	Flag used for utilising DHCP
                        	**type**\:  bool
                        
                        .. attribute:: is_icm_pv6_redirect
                        
                        	ICMP redirect flag
                        	**type**\:  bool
                        
                        .. attribute:: is_route_address_managed
                        
                        	Flag used to manage routable address
                        	**type**\:  bool
                        
                        .. attribute:: is_suppressed
                        
                        	Suppress flag
                        	**type**\:  bool
                        
                        .. attribute:: nd_advertisement_lifetime
                        
                        	ND router advertisement life time in sec
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nd_cache_limit
                        
                        	Completed adjacency limit per interface
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nd_max_transmit_interval
                        
                        	ND router advertisement maximum transmit interval in sec
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nd_min_transmit_interval
                        
                        	ND router advertisement minimum transmit interval in sec
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nd_reachable_time
                        
                        	Time to reach ND in msec
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nd_retransmit_interval
                        
                        	ND retransmit interval in msec
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: send_unicast_ra
                        
                        	unicast RA send flag
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters, self).__init__()

                            self.yang_name = "nd-parameters"
                            self.yang_parent_name = "bundle-interface"

                            self.complete_glean_count = YLeaf(YType.uint32, "complete-glean-count")

                            self.complete_protocol_count = YLeaf(YType.uint32, "complete-protocol-count")

                            self.dad_attempts = YLeaf(YType.uint32, "dad-attempts")

                            self.dropped_glean_req_count = YLeaf(YType.uint32, "dropped-glean-req-count")

                            self.dropped_protocol_req_count = YLeaf(YType.uint32, "dropped-protocol-req-count")

                            self.incomplete_glean_count = YLeaf(YType.uint32, "incomplete-glean-count")

                            self.incomplete_protocol_count = YLeaf(YType.uint32, "incomplete-protocol-count")

                            self.is_dad_enabled = YLeaf(YType.boolean, "is-dad-enabled")

                            self.is_dhcp_managed = YLeaf(YType.boolean, "is-dhcp-managed")

                            self.is_icm_pv6_redirect = YLeaf(YType.boolean, "is-icm-pv6-redirect")

                            self.is_route_address_managed = YLeaf(YType.boolean, "is-route-address-managed")

                            self.is_suppressed = YLeaf(YType.boolean, "is-suppressed")

                            self.nd_advertisement_lifetime = YLeaf(YType.uint32, "nd-advertisement-lifetime")

                            self.nd_cache_limit = YLeaf(YType.uint32, "nd-cache-limit")

                            self.nd_max_transmit_interval = YLeaf(YType.uint32, "nd-max-transmit-interval")

                            self.nd_min_transmit_interval = YLeaf(YType.uint32, "nd-min-transmit-interval")

                            self.nd_reachable_time = YLeaf(YType.uint32, "nd-reachable-time")

                            self.nd_retransmit_interval = YLeaf(YType.uint32, "nd-retransmit-interval")

                            self.send_unicast_ra = YLeaf(YType.boolean, "send-unicast-ra")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("complete_glean_count",
                                            "complete_protocol_count",
                                            "dad_attempts",
                                            "dropped_glean_req_count",
                                            "dropped_protocol_req_count",
                                            "incomplete_glean_count",
                                            "incomplete_protocol_count",
                                            "is_dad_enabled",
                                            "is_dhcp_managed",
                                            "is_icm_pv6_redirect",
                                            "is_route_address_managed",
                                            "is_suppressed",
                                            "nd_advertisement_lifetime",
                                            "nd_cache_limit",
                                            "nd_max_transmit_interval",
                                            "nd_min_transmit_interval",
                                            "nd_reachable_time",
                                            "nd_retransmit_interval",
                                            "send_unicast_ra") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.complete_glean_count.is_set or
                                self.complete_protocol_count.is_set or
                                self.dad_attempts.is_set or
                                self.dropped_glean_req_count.is_set or
                                self.dropped_protocol_req_count.is_set or
                                self.incomplete_glean_count.is_set or
                                self.incomplete_protocol_count.is_set or
                                self.is_dad_enabled.is_set or
                                self.is_dhcp_managed.is_set or
                                self.is_icm_pv6_redirect.is_set or
                                self.is_route_address_managed.is_set or
                                self.is_suppressed.is_set or
                                self.nd_advertisement_lifetime.is_set or
                                self.nd_cache_limit.is_set or
                                self.nd_max_transmit_interval.is_set or
                                self.nd_min_transmit_interval.is_set or
                                self.nd_reachable_time.is_set or
                                self.nd_retransmit_interval.is_set or
                                self.send_unicast_ra.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.complete_glean_count.yfilter != YFilter.not_set or
                                self.complete_protocol_count.yfilter != YFilter.not_set or
                                self.dad_attempts.yfilter != YFilter.not_set or
                                self.dropped_glean_req_count.yfilter != YFilter.not_set or
                                self.dropped_protocol_req_count.yfilter != YFilter.not_set or
                                self.incomplete_glean_count.yfilter != YFilter.not_set or
                                self.incomplete_protocol_count.yfilter != YFilter.not_set or
                                self.is_dad_enabled.yfilter != YFilter.not_set or
                                self.is_dhcp_managed.yfilter != YFilter.not_set or
                                self.is_icm_pv6_redirect.yfilter != YFilter.not_set or
                                self.is_route_address_managed.yfilter != YFilter.not_set or
                                self.is_suppressed.yfilter != YFilter.not_set or
                                self.nd_advertisement_lifetime.yfilter != YFilter.not_set or
                                self.nd_cache_limit.yfilter != YFilter.not_set or
                                self.nd_max_transmit_interval.yfilter != YFilter.not_set or
                                self.nd_min_transmit_interval.yfilter != YFilter.not_set or
                                self.nd_reachable_time.yfilter != YFilter.not_set or
                                self.nd_retransmit_interval.yfilter != YFilter.not_set or
                                self.send_unicast_ra.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "nd-parameters" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.complete_glean_count.is_set or self.complete_glean_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.complete_glean_count.get_name_leafdata())
                            if (self.complete_protocol_count.is_set or self.complete_protocol_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.complete_protocol_count.get_name_leafdata())
                            if (self.dad_attempts.is_set or self.dad_attempts.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dad_attempts.get_name_leafdata())
                            if (self.dropped_glean_req_count.is_set or self.dropped_glean_req_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped_glean_req_count.get_name_leafdata())
                            if (self.dropped_protocol_req_count.is_set or self.dropped_protocol_req_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped_protocol_req_count.get_name_leafdata())
                            if (self.incomplete_glean_count.is_set or self.incomplete_glean_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.incomplete_glean_count.get_name_leafdata())
                            if (self.incomplete_protocol_count.is_set or self.incomplete_protocol_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.incomplete_protocol_count.get_name_leafdata())
                            if (self.is_dad_enabled.is_set or self.is_dad_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_dad_enabled.get_name_leafdata())
                            if (self.is_dhcp_managed.is_set or self.is_dhcp_managed.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_dhcp_managed.get_name_leafdata())
                            if (self.is_icm_pv6_redirect.is_set or self.is_icm_pv6_redirect.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_icm_pv6_redirect.get_name_leafdata())
                            if (self.is_route_address_managed.is_set or self.is_route_address_managed.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_route_address_managed.get_name_leafdata())
                            if (self.is_suppressed.is_set or self.is_suppressed.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_suppressed.get_name_leafdata())
                            if (self.nd_advertisement_lifetime.is_set or self.nd_advertisement_lifetime.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.nd_advertisement_lifetime.get_name_leafdata())
                            if (self.nd_cache_limit.is_set or self.nd_cache_limit.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.nd_cache_limit.get_name_leafdata())
                            if (self.nd_max_transmit_interval.is_set or self.nd_max_transmit_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.nd_max_transmit_interval.get_name_leafdata())
                            if (self.nd_min_transmit_interval.is_set or self.nd_min_transmit_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.nd_min_transmit_interval.get_name_leafdata())
                            if (self.nd_reachable_time.is_set or self.nd_reachable_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.nd_reachable_time.get_name_leafdata())
                            if (self.nd_retransmit_interval.is_set or self.nd_retransmit_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.nd_retransmit_interval.get_name_leafdata())
                            if (self.send_unicast_ra.is_set or self.send_unicast_ra.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.send_unicast_ra.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "complete-glean-count" or name == "complete-protocol-count" or name == "dad-attempts" or name == "dropped-glean-req-count" or name == "dropped-protocol-req-count" or name == "incomplete-glean-count" or name == "incomplete-protocol-count" or name == "is-dad-enabled" or name == "is-dhcp-managed" or name == "is-icm-pv6-redirect" or name == "is-route-address-managed" or name == "is-suppressed" or name == "nd-advertisement-lifetime" or name == "nd-cache-limit" or name == "nd-max-transmit-interval" or name == "nd-min-transmit-interval" or name == "nd-reachable-time" or name == "nd-retransmit-interval" or name == "send-unicast-ra"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "complete-glean-count"):
                                self.complete_glean_count = value
                                self.complete_glean_count.value_namespace = name_space
                                self.complete_glean_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "complete-protocol-count"):
                                self.complete_protocol_count = value
                                self.complete_protocol_count.value_namespace = name_space
                                self.complete_protocol_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "dad-attempts"):
                                self.dad_attempts = value
                                self.dad_attempts.value_namespace = name_space
                                self.dad_attempts.value_namespace_prefix = name_space_prefix
                            if(value_path == "dropped-glean-req-count"):
                                self.dropped_glean_req_count = value
                                self.dropped_glean_req_count.value_namespace = name_space
                                self.dropped_glean_req_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "dropped-protocol-req-count"):
                                self.dropped_protocol_req_count = value
                                self.dropped_protocol_req_count.value_namespace = name_space
                                self.dropped_protocol_req_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "incomplete-glean-count"):
                                self.incomplete_glean_count = value
                                self.incomplete_glean_count.value_namespace = name_space
                                self.incomplete_glean_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "incomplete-protocol-count"):
                                self.incomplete_protocol_count = value
                                self.incomplete_protocol_count.value_namespace = name_space
                                self.incomplete_protocol_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-dad-enabled"):
                                self.is_dad_enabled = value
                                self.is_dad_enabled.value_namespace = name_space
                                self.is_dad_enabled.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-dhcp-managed"):
                                self.is_dhcp_managed = value
                                self.is_dhcp_managed.value_namespace = name_space
                                self.is_dhcp_managed.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-icm-pv6-redirect"):
                                self.is_icm_pv6_redirect = value
                                self.is_icm_pv6_redirect.value_namespace = name_space
                                self.is_icm_pv6_redirect.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-route-address-managed"):
                                self.is_route_address_managed = value
                                self.is_route_address_managed.value_namespace = name_space
                                self.is_route_address_managed.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-suppressed"):
                                self.is_suppressed = value
                                self.is_suppressed.value_namespace = name_space
                                self.is_suppressed.value_namespace_prefix = name_space_prefix
                            if(value_path == "nd-advertisement-lifetime"):
                                self.nd_advertisement_lifetime = value
                                self.nd_advertisement_lifetime.value_namespace = name_space
                                self.nd_advertisement_lifetime.value_namespace_prefix = name_space_prefix
                            if(value_path == "nd-cache-limit"):
                                self.nd_cache_limit = value
                                self.nd_cache_limit.value_namespace = name_space
                                self.nd_cache_limit.value_namespace_prefix = name_space_prefix
                            if(value_path == "nd-max-transmit-interval"):
                                self.nd_max_transmit_interval = value
                                self.nd_max_transmit_interval.value_namespace = name_space
                                self.nd_max_transmit_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "nd-min-transmit-interval"):
                                self.nd_min_transmit_interval = value
                                self.nd_min_transmit_interval.value_namespace = name_space
                                self.nd_min_transmit_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "nd-reachable-time"):
                                self.nd_reachable_time = value
                                self.nd_reachable_time.value_namespace = name_space
                                self.nd_reachable_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "nd-retransmit-interval"):
                                self.nd_retransmit_interval = value
                                self.nd_retransmit_interval.value_namespace = name_space
                                self.nd_retransmit_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "send-unicast-ra"):
                                self.send_unicast_ra = value
                                self.send_unicast_ra.value_namespace = name_space
                                self.send_unicast_ra.value_namespace_prefix = name_space_prefix


                    class LocalAddress(Entity):
                        """
                        Link local address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress, self).__init__()

                            self.yang_name = "local-address"
                            self.yang_parent_name = "bundle-interface"

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ipv6_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return self.ipv6_address.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ipv6_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "local-address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipv6-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ipv6-address"):
                                self.ipv6_address = value
                                self.ipv6_address.value_namespace = name_space
                                self.ipv6_address.value_namespace_prefix = name_space_prefix


                    class GlobalAddress(Entity):
                        """
                        List of ND global addresses
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress, self).__init__()

                            self.yang_name = "global-address"
                            self.yang_parent_name = "bundle-interface"

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ipv6_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return self.ipv6_address.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ipv6_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "global-address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipv6-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ipv6-address"):
                                self.ipv6_address = value
                                self.ipv6_address.value_namespace = name_space
                                self.ipv6_address.value_namespace_prefix = name_space_prefix


                    class MemberNode(Entity):
                        """
                        List of member nodes
                        
                        .. attribute:: node_name
                        
                        	Node Name
                        	**type**\:  str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: total_links
                        
                        	Number of links on the node
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode, self).__init__()

                            self.yang_name = "member-node"
                            self.yang_parent_name = "bundle-interface"

                            self.node_name = YLeaf(YType.str, "node-name")

                            self.total_links = YLeaf(YType.uint32, "total-links")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("node_name",
                                            "total_links") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.node_name.is_set or
                                self.total_links.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.node_name.yfilter != YFilter.not_set or
                                self.total_links.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "member-node" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.node_name.get_name_leafdata())
                            if (self.total_links.is_set or self.total_links.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_links.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "node-name" or name == "total-links"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "node-name"):
                                self.node_name = value
                                self.node_name.value_namespace = name_space
                                self.node_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-links"):
                                self.total_links = value
                                self.total_links.value_namespace = name_space
                                self.total_links.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.global_address:
                            if (c.has_data()):
                                return True
                        for c in self.member_node:
                            if (c.has_data()):
                                return True
                        for leaf in self.member_link.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return (
                            self.interface_name.is_set or
                            self.etype.is_set or
                            self.iftype.is_set or
                            self.is_interface_enabled.is_set or
                            self.is_ipv6_enabled.is_set or
                            self.is_mpls_enabled.is_set or
                            self.mac_addr.is_set or
                            self.mac_addr_size.is_set or
                            self.mtu.is_set or
                            self.parent_interface_name.is_set or
                            self.vlan_tag.is_set or
                            (self.local_address is not None and self.local_address.has_data()) or
                            (self.nd_parameters is not None and self.nd_parameters.has_data()))

                    def has_operation(self):
                        for c in self.global_address:
                            if (c.has_operation()):
                                return True
                        for c in self.member_node:
                            if (c.has_operation()):
                                return True
                        for leaf in self.member_link.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.etype.yfilter != YFilter.not_set or
                            self.iftype.yfilter != YFilter.not_set or
                            self.is_interface_enabled.yfilter != YFilter.not_set or
                            self.is_ipv6_enabled.yfilter != YFilter.not_set or
                            self.is_mpls_enabled.yfilter != YFilter.not_set or
                            self.mac_addr.yfilter != YFilter.not_set or
                            self.mac_addr_size.yfilter != YFilter.not_set or
                            self.member_link.yfilter != YFilter.not_set or
                            self.mtu.yfilter != YFilter.not_set or
                            self.parent_interface_name.yfilter != YFilter.not_set or
                            self.vlan_tag.yfilter != YFilter.not_set or
                            (self.local_address is not None and self.local_address.has_operation()) or
                            (self.nd_parameters is not None and self.nd_parameters.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bundle-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

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
                        if (self.etype.is_set or self.etype.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.etype.get_name_leafdata())
                        if (self.iftype.is_set or self.iftype.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.iftype.get_name_leafdata())
                        if (self.is_interface_enabled.is_set or self.is_interface_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_interface_enabled.get_name_leafdata())
                        if (self.is_ipv6_enabled.is_set or self.is_ipv6_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_ipv6_enabled.get_name_leafdata())
                        if (self.is_mpls_enabled.is_set or self.is_mpls_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_mpls_enabled.get_name_leafdata())
                        if (self.mac_addr.is_set or self.mac_addr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mac_addr.get_name_leafdata())
                        if (self.mac_addr_size.is_set or self.mac_addr_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mac_addr_size.get_name_leafdata())
                        if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mtu.get_name_leafdata())
                        if (self.parent_interface_name.is_set or self.parent_interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.parent_interface_name.get_name_leafdata())
                        if (self.vlan_tag.is_set or self.vlan_tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vlan_tag.get_name_leafdata())

                        leaf_name_data.extend(self.member_link.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "global-address"):
                            for c in self.global_address:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.global_address.append(c)
                            return c

                        if (child_yang_name == "local-address"):
                            if (self.local_address is None):
                                self.local_address = Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress()
                                self.local_address.parent = self
                                self._children_name_map["local_address"] = "local-address"
                            return self.local_address

                        if (child_yang_name == "member-node"):
                            for c in self.member_node:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.member_node.append(c)
                            return c

                        if (child_yang_name == "nd-parameters"):
                            if (self.nd_parameters is None):
                                self.nd_parameters = Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters()
                                self.nd_parameters.parent = self
                                self._children_name_map["nd_parameters"] = "nd-parameters"
                            return self.nd_parameters

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "global-address" or name == "local-address" or name == "member-node" or name == "nd-parameters" or name == "interface-name" or name == "etype" or name == "iftype" or name == "is-interface-enabled" or name == "is-ipv6-enabled" or name == "is-mpls-enabled" or name == "mac-addr" or name == "mac-addr-size" or name == "member-link" or name == "mtu" or name == "parent-interface-name" or name == "vlan-tag"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "etype"):
                            self.etype = value
                            self.etype.value_namespace = name_space
                            self.etype.value_namespace_prefix = name_space_prefix
                        if(value_path == "iftype"):
                            self.iftype = value
                            self.iftype.value_namespace = name_space
                            self.iftype.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-interface-enabled"):
                            self.is_interface_enabled = value
                            self.is_interface_enabled.value_namespace = name_space
                            self.is_interface_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-ipv6-enabled"):
                            self.is_ipv6_enabled = value
                            self.is_ipv6_enabled.value_namespace = name_space
                            self.is_ipv6_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-mpls-enabled"):
                            self.is_mpls_enabled = value
                            self.is_mpls_enabled.value_namespace = name_space
                            self.is_mpls_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "mac-addr"):
                            self.mac_addr = value
                            self.mac_addr.value_namespace = name_space
                            self.mac_addr.value_namespace_prefix = name_space_prefix
                        if(value_path == "mac-addr-size"):
                            self.mac_addr_size = value
                            self.mac_addr_size.value_namespace = name_space
                            self.mac_addr_size.value_namespace_prefix = name_space_prefix
                        if(value_path == "member-link"):
                            self.member_link.append(value)
                        if(value_path == "mtu"):
                            self.mtu = value
                            self.mtu.value_namespace = name_space
                            self.mtu.value_namespace_prefix = name_space_prefix
                        if(value_path == "parent-interface-name"):
                            self.parent_interface_name = value
                            self.parent_interface_name.value_namespace = name_space
                            self.parent_interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "vlan-tag"):
                            self.vlan_tag = value
                            self.vlan_tag.value_namespace = name_space
                            self.vlan_tag.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.bundle_interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.bundle_interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bundle-interfaces" + path_buffer

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

                    if (child_yang_name == "bundle-interface"):
                        for c in self.bundle_interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.bundle_interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bundle-interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Interfaces(Entity):
                """
                IPv6 node discovery list of interfaces for a
                specific node
                
                .. attribute:: interface
                
                	IPv6  node discovery operational data for a specific node and interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6NodeDiscovery.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"

                    self.interface = YList(self)

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
                                super(Ipv6NodeDiscovery.Nodes.Node.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv6NodeDiscovery.Nodes.Node.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    IPv6  node discovery operational data for a
                    specific node and interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: complete_glean_count
                    
                    	Completed GLEAN entry count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: complete_protocol_count
                    
                    	Completed PROTO entry Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dad_attempts
                    
                    	DAD attempt count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dropped_glean_req_count
                    
                    	Dropped GLEAN entry lequest count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dropped_protocol_req_count
                    
                    	Dropped PROTO entry request count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: incomplete_glean_count
                    
                    	Incomplete GLEAN entry count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: incomplete_protocol_count
                    
                    	Incomplete PROTO entry count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_dad_enabled
                    
                    	If true, DAD (D.. A.. D..) is enabled otherwise it is disabled
                    	**type**\:  bool
                    
                    .. attribute:: is_dhcp_managed
                    
                    	Flag used for utilising DHCP
                    	**type**\:  bool
                    
                    .. attribute:: is_icm_pv6_redirect
                    
                    	ICMP redirect flag
                    	**type**\:  bool
                    
                    .. attribute:: is_route_address_managed
                    
                    	Flag used to manage routable address
                    	**type**\:  bool
                    
                    .. attribute:: is_suppressed
                    
                    	Suppress flag
                    	**type**\:  bool
                    
                    .. attribute:: nd_advertisement_lifetime
                    
                    	ND router advertisement life time in sec
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nd_cache_limit
                    
                    	Completed adjacency limit per interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nd_max_transmit_interval
                    
                    	ND router advertisement maximum transmit interval in sec
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nd_min_transmit_interval
                    
                    	ND router advertisement minimum transmit interval in sec
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nd_reachable_time
                    
                    	Time to reach ND in msec
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nd_retransmit_interval
                    
                    	ND retransmit interval in msec
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_unicast_ra
                    
                    	unicast RA send flag
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.complete_glean_count = YLeaf(YType.uint32, "complete-glean-count")

                        self.complete_protocol_count = YLeaf(YType.uint32, "complete-protocol-count")

                        self.dad_attempts = YLeaf(YType.uint32, "dad-attempts")

                        self.dropped_glean_req_count = YLeaf(YType.uint32, "dropped-glean-req-count")

                        self.dropped_protocol_req_count = YLeaf(YType.uint32, "dropped-protocol-req-count")

                        self.incomplete_glean_count = YLeaf(YType.uint32, "incomplete-glean-count")

                        self.incomplete_protocol_count = YLeaf(YType.uint32, "incomplete-protocol-count")

                        self.is_dad_enabled = YLeaf(YType.boolean, "is-dad-enabled")

                        self.is_dhcp_managed = YLeaf(YType.boolean, "is-dhcp-managed")

                        self.is_icm_pv6_redirect = YLeaf(YType.boolean, "is-icm-pv6-redirect")

                        self.is_route_address_managed = YLeaf(YType.boolean, "is-route-address-managed")

                        self.is_suppressed = YLeaf(YType.boolean, "is-suppressed")

                        self.nd_advertisement_lifetime = YLeaf(YType.uint32, "nd-advertisement-lifetime")

                        self.nd_cache_limit = YLeaf(YType.uint32, "nd-cache-limit")

                        self.nd_max_transmit_interval = YLeaf(YType.uint32, "nd-max-transmit-interval")

                        self.nd_min_transmit_interval = YLeaf(YType.uint32, "nd-min-transmit-interval")

                        self.nd_reachable_time = YLeaf(YType.uint32, "nd-reachable-time")

                        self.nd_retransmit_interval = YLeaf(YType.uint32, "nd-retransmit-interval")

                        self.send_unicast_ra = YLeaf(YType.boolean, "send-unicast-ra")

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
                                        "complete_glean_count",
                                        "complete_protocol_count",
                                        "dad_attempts",
                                        "dropped_glean_req_count",
                                        "dropped_protocol_req_count",
                                        "incomplete_glean_count",
                                        "incomplete_protocol_count",
                                        "is_dad_enabled",
                                        "is_dhcp_managed",
                                        "is_icm_pv6_redirect",
                                        "is_route_address_managed",
                                        "is_suppressed",
                                        "nd_advertisement_lifetime",
                                        "nd_cache_limit",
                                        "nd_max_transmit_interval",
                                        "nd_min_transmit_interval",
                                        "nd_reachable_time",
                                        "nd_retransmit_interval",
                                        "send_unicast_ra") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.complete_glean_count.is_set or
                            self.complete_protocol_count.is_set or
                            self.dad_attempts.is_set or
                            self.dropped_glean_req_count.is_set or
                            self.dropped_protocol_req_count.is_set or
                            self.incomplete_glean_count.is_set or
                            self.incomplete_protocol_count.is_set or
                            self.is_dad_enabled.is_set or
                            self.is_dhcp_managed.is_set or
                            self.is_icm_pv6_redirect.is_set or
                            self.is_route_address_managed.is_set or
                            self.is_suppressed.is_set or
                            self.nd_advertisement_lifetime.is_set or
                            self.nd_cache_limit.is_set or
                            self.nd_max_transmit_interval.is_set or
                            self.nd_min_transmit_interval.is_set or
                            self.nd_reachable_time.is_set or
                            self.nd_retransmit_interval.is_set or
                            self.send_unicast_ra.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.complete_glean_count.yfilter != YFilter.not_set or
                            self.complete_protocol_count.yfilter != YFilter.not_set or
                            self.dad_attempts.yfilter != YFilter.not_set or
                            self.dropped_glean_req_count.yfilter != YFilter.not_set or
                            self.dropped_protocol_req_count.yfilter != YFilter.not_set or
                            self.incomplete_glean_count.yfilter != YFilter.not_set or
                            self.incomplete_protocol_count.yfilter != YFilter.not_set or
                            self.is_dad_enabled.yfilter != YFilter.not_set or
                            self.is_dhcp_managed.yfilter != YFilter.not_set or
                            self.is_icm_pv6_redirect.yfilter != YFilter.not_set or
                            self.is_route_address_managed.yfilter != YFilter.not_set or
                            self.is_suppressed.yfilter != YFilter.not_set or
                            self.nd_advertisement_lifetime.yfilter != YFilter.not_set or
                            self.nd_cache_limit.yfilter != YFilter.not_set or
                            self.nd_max_transmit_interval.yfilter != YFilter.not_set or
                            self.nd_min_transmit_interval.yfilter != YFilter.not_set or
                            self.nd_reachable_time.yfilter != YFilter.not_set or
                            self.nd_retransmit_interval.yfilter != YFilter.not_set or
                            self.send_unicast_ra.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

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
                        if (self.complete_glean_count.is_set or self.complete_glean_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.complete_glean_count.get_name_leafdata())
                        if (self.complete_protocol_count.is_set or self.complete_protocol_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.complete_protocol_count.get_name_leafdata())
                        if (self.dad_attempts.is_set or self.dad_attempts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dad_attempts.get_name_leafdata())
                        if (self.dropped_glean_req_count.is_set or self.dropped_glean_req_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dropped_glean_req_count.get_name_leafdata())
                        if (self.dropped_protocol_req_count.is_set or self.dropped_protocol_req_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dropped_protocol_req_count.get_name_leafdata())
                        if (self.incomplete_glean_count.is_set or self.incomplete_glean_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.incomplete_glean_count.get_name_leafdata())
                        if (self.incomplete_protocol_count.is_set or self.incomplete_protocol_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.incomplete_protocol_count.get_name_leafdata())
                        if (self.is_dad_enabled.is_set or self.is_dad_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_dad_enabled.get_name_leafdata())
                        if (self.is_dhcp_managed.is_set or self.is_dhcp_managed.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_dhcp_managed.get_name_leafdata())
                        if (self.is_icm_pv6_redirect.is_set or self.is_icm_pv6_redirect.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_icm_pv6_redirect.get_name_leafdata())
                        if (self.is_route_address_managed.is_set or self.is_route_address_managed.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_route_address_managed.get_name_leafdata())
                        if (self.is_suppressed.is_set or self.is_suppressed.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_suppressed.get_name_leafdata())
                        if (self.nd_advertisement_lifetime.is_set or self.nd_advertisement_lifetime.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nd_advertisement_lifetime.get_name_leafdata())
                        if (self.nd_cache_limit.is_set or self.nd_cache_limit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nd_cache_limit.get_name_leafdata())
                        if (self.nd_max_transmit_interval.is_set or self.nd_max_transmit_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nd_max_transmit_interval.get_name_leafdata())
                        if (self.nd_min_transmit_interval.is_set or self.nd_min_transmit_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nd_min_transmit_interval.get_name_leafdata())
                        if (self.nd_reachable_time.is_set or self.nd_reachable_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nd_reachable_time.get_name_leafdata())
                        if (self.nd_retransmit_interval.is_set or self.nd_retransmit_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nd_retransmit_interval.get_name_leafdata())
                        if (self.send_unicast_ra.is_set or self.send_unicast_ra.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.send_unicast_ra.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name" or name == "complete-glean-count" or name == "complete-protocol-count" or name == "dad-attempts" or name == "dropped-glean-req-count" or name == "dropped-protocol-req-count" or name == "incomplete-glean-count" or name == "incomplete-protocol-count" or name == "is-dad-enabled" or name == "is-dhcp-managed" or name == "is-icm-pv6-redirect" or name == "is-route-address-managed" or name == "is-suppressed" or name == "nd-advertisement-lifetime" or name == "nd-cache-limit" or name == "nd-max-transmit-interval" or name == "nd-min-transmit-interval" or name == "nd-reachable-time" or name == "nd-retransmit-interval" or name == "send-unicast-ra"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "complete-glean-count"):
                            self.complete_glean_count = value
                            self.complete_glean_count.value_namespace = name_space
                            self.complete_glean_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "complete-protocol-count"):
                            self.complete_protocol_count = value
                            self.complete_protocol_count.value_namespace = name_space
                            self.complete_protocol_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "dad-attempts"):
                            self.dad_attempts = value
                            self.dad_attempts.value_namespace = name_space
                            self.dad_attempts.value_namespace_prefix = name_space_prefix
                        if(value_path == "dropped-glean-req-count"):
                            self.dropped_glean_req_count = value
                            self.dropped_glean_req_count.value_namespace = name_space
                            self.dropped_glean_req_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "dropped-protocol-req-count"):
                            self.dropped_protocol_req_count = value
                            self.dropped_protocol_req_count.value_namespace = name_space
                            self.dropped_protocol_req_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "incomplete-glean-count"):
                            self.incomplete_glean_count = value
                            self.incomplete_glean_count.value_namespace = name_space
                            self.incomplete_glean_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "incomplete-protocol-count"):
                            self.incomplete_protocol_count = value
                            self.incomplete_protocol_count.value_namespace = name_space
                            self.incomplete_protocol_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-dad-enabled"):
                            self.is_dad_enabled = value
                            self.is_dad_enabled.value_namespace = name_space
                            self.is_dad_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-dhcp-managed"):
                            self.is_dhcp_managed = value
                            self.is_dhcp_managed.value_namespace = name_space
                            self.is_dhcp_managed.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-icm-pv6-redirect"):
                            self.is_icm_pv6_redirect = value
                            self.is_icm_pv6_redirect.value_namespace = name_space
                            self.is_icm_pv6_redirect.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-route-address-managed"):
                            self.is_route_address_managed = value
                            self.is_route_address_managed.value_namespace = name_space
                            self.is_route_address_managed.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-suppressed"):
                            self.is_suppressed = value
                            self.is_suppressed.value_namespace = name_space
                            self.is_suppressed.value_namespace_prefix = name_space_prefix
                        if(value_path == "nd-advertisement-lifetime"):
                            self.nd_advertisement_lifetime = value
                            self.nd_advertisement_lifetime.value_namespace = name_space
                            self.nd_advertisement_lifetime.value_namespace_prefix = name_space_prefix
                        if(value_path == "nd-cache-limit"):
                            self.nd_cache_limit = value
                            self.nd_cache_limit.value_namespace = name_space
                            self.nd_cache_limit.value_namespace_prefix = name_space_prefix
                        if(value_path == "nd-max-transmit-interval"):
                            self.nd_max_transmit_interval = value
                            self.nd_max_transmit_interval.value_namespace = name_space
                            self.nd_max_transmit_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "nd-min-transmit-interval"):
                            self.nd_min_transmit_interval = value
                            self.nd_min_transmit_interval.value_namespace = name_space
                            self.nd_min_transmit_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "nd-reachable-time"):
                            self.nd_reachable_time = value
                            self.nd_reachable_time.value_namespace = name_space
                            self.nd_reachable_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "nd-retransmit-interval"):
                            self.nd_retransmit_interval = value
                            self.nd_retransmit_interval.value_namespace = name_space
                            self.nd_retransmit_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "send-unicast-ra"):
                            self.send_unicast_ra = value
                            self.send_unicast_ra.value_namespace = name_space
                            self.send_unicast_ra.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interfaces" + path_buffer

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

                    if (child_yang_name == "interface"):
                        for c in self.interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class NdVirtualRouters(Entity):
                """
                IPv6 ND virtual router information for a
                specific interface
                
                .. attribute:: nd_virtual_router
                
                	IPv6 ND virtual  router operational data for a specific interface
                	**type**\: list of    :py:class:`NdVirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter>`
                
                

                """

                _prefix = 'ipv6-nd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters, self).__init__()

                    self.yang_name = "nd-virtual-routers"
                    self.yang_parent_name = "node"

                    self.nd_virtual_router = YList(self)

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
                                super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters, self).__setattr__(name, value)


                class NdVirtualRouter(Entity):
                    """
                    IPv6 ND virtual  router operational data for
                    a specific interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: context
                    
                    	Virtual Router ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flags
                    
                    	VR Flags
                    	**type**\:   :py:class:`Ipv6NdShVrFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdShVrFlags>`
                    
                    .. attribute:: link_layer_address
                    
                    	Link\-Layer Address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: local_address
                    
                    	Link local address
                    	**type**\:   :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress>`
                    
                    .. attribute:: state
                    
                    	VR state
                    	**type**\:   :py:class:`Ipv6NdShVrState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NdShVrState>`
                    
                    .. attribute:: vr_gl_addr_ct
                    
                    	Virtual Global Address Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vr_global_address
                    
                    	List of ND global addresses
                    	**type**\: list of    :py:class:`VrGlobalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper.Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress>`
                    
                    

                    """

                    _prefix = 'ipv6-nd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter, self).__init__()

                        self.yang_name = "nd-virtual-router"
                        self.yang_parent_name = "nd-virtual-routers"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.context = YLeaf(YType.uint32, "context")

                        self.flags = YLeaf(YType.enumeration, "flags")

                        self.link_layer_address = YLeaf(YType.str, "link-layer-address")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.vr_gl_addr_ct = YLeaf(YType.uint32, "vr-gl-addr-ct")

                        self.local_address = Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress()
                        self.local_address.parent = self
                        self._children_name_map["local_address"] = "local-address"
                        self._children_yang_names.add("local-address")

                        self.vr_global_address = YList(self)

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
                                        "context",
                                        "flags",
                                        "link_layer_address",
                                        "state",
                                        "vr_gl_addr_ct") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter, self).__setattr__(name, value)


                    class LocalAddress(Entity):
                        """
                        Link local address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress, self).__init__()

                            self.yang_name = "local-address"
                            self.yang_parent_name = "nd-virtual-router"

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ipv6_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return self.ipv6_address.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ipv6_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "local-address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipv6-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ipv6-address"):
                                self.ipv6_address = value
                                self.ipv6_address.value_namespace = name_space
                                self.ipv6_address.value_namespace_prefix = name_space_prefix


                    class VrGlobalAddress(Entity):
                        """
                        List of ND global addresses
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv6-nd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress, self).__init__()

                            self.yang_name = "vr-global-address"
                            self.yang_parent_name = "nd-virtual-router"

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ipv6_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return self.ipv6_address.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ipv6_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "vr-global-address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipv6-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ipv6-address"):
                                self.ipv6_address = value
                                self.ipv6_address.value_namespace = name_space
                                self.ipv6_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.vr_global_address:
                            if (c.has_data()):
                                return True
                        return (
                            self.interface_name.is_set or
                            self.context.is_set or
                            self.flags.is_set or
                            self.link_layer_address.is_set or
                            self.state.is_set or
                            self.vr_gl_addr_ct.is_set or
                            (self.local_address is not None and self.local_address.has_data()))

                    def has_operation(self):
                        for c in self.vr_global_address:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.context.yfilter != YFilter.not_set or
                            self.flags.yfilter != YFilter.not_set or
                            self.link_layer_address.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.vr_gl_addr_ct.yfilter != YFilter.not_set or
                            (self.local_address is not None and self.local_address.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "nd-virtual-router" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

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
                        if (self.context.is_set or self.context.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.context.get_name_leafdata())
                        if (self.flags.is_set or self.flags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flags.get_name_leafdata())
                        if (self.link_layer_address.is_set or self.link_layer_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.link_layer_address.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.vr_gl_addr_ct.is_set or self.vr_gl_addr_ct.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vr_gl_addr_ct.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "local-address"):
                            if (self.local_address is None):
                                self.local_address = Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress()
                                self.local_address.parent = self
                                self._children_name_map["local_address"] = "local-address"
                            return self.local_address

                        if (child_yang_name == "vr-global-address"):
                            for c in self.vr_global_address:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.vr_global_address.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "local-address" or name == "vr-global-address" or name == "interface-name" or name == "context" or name == "flags" or name == "link-layer-address" or name == "state" or name == "vr-gl-addr-ct"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "context"):
                            self.context = value
                            self.context.value_namespace = name_space
                            self.context.value_namespace_prefix = name_space_prefix
                        if(value_path == "flags"):
                            self.flags = value
                            self.flags.value_namespace = name_space
                            self.flags.value_namespace_prefix = name_space_prefix
                        if(value_path == "link-layer-address"):
                            self.link_layer_address = value
                            self.link_layer_address.value_namespace = name_space
                            self.link_layer_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "vr-gl-addr-ct"):
                            self.vr_gl_addr_ct = value
                            self.vr_gl_addr_ct.value_namespace = name_space
                            self.vr_gl_addr_ct.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.nd_virtual_router:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.nd_virtual_router:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "nd-virtual-routers" + path_buffer

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

                    if (child_yang_name == "nd-virtual-router"):
                        for c in self.nd_virtual_router:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.nd_virtual_router.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "nd-virtual-router"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.bundle_interfaces is not None and self.bundle_interfaces.has_data()) or
                    (self.bundle_nodes is not None and self.bundle_nodes.has_data()) or
                    (self.interfaces is not None and self.interfaces.has_data()) or
                    (self.nd_virtual_routers is not None and self.nd_virtual_routers.has_data()) or
                    (self.neighbor_interfaces is not None and self.neighbor_interfaces.has_data()) or
                    (self.neighbor_summary is not None and self.neighbor_summary.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.bundle_interfaces is not None and self.bundle_interfaces.has_operation()) or
                    (self.bundle_nodes is not None and self.bundle_nodes.has_operation()) or
                    (self.interfaces is not None and self.interfaces.has_operation()) or
                    (self.nd_virtual_routers is not None and self.nd_virtual_routers.has_operation()) or
                    (self.neighbor_interfaces is not None and self.neighbor_interfaces.has_operation()) or
                    (self.neighbor_summary is not None and self.neighbor_summary.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv6-nd-oper:ipv6-node-discovery/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "bundle-interfaces"):
                    if (self.bundle_interfaces is None):
                        self.bundle_interfaces = Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces()
                        self.bundle_interfaces.parent = self
                        self._children_name_map["bundle_interfaces"] = "bundle-interfaces"
                    return self.bundle_interfaces

                if (child_yang_name == "bundle-nodes"):
                    if (self.bundle_nodes is None):
                        self.bundle_nodes = Ipv6NodeDiscovery.Nodes.Node.BundleNodes()
                        self.bundle_nodes.parent = self
                        self._children_name_map["bundle_nodes"] = "bundle-nodes"
                    return self.bundle_nodes

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = Ipv6NodeDiscovery.Nodes.Node.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                if (child_yang_name == "nd-virtual-routers"):
                    if (self.nd_virtual_routers is None):
                        self.nd_virtual_routers = Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters()
                        self.nd_virtual_routers.parent = self
                        self._children_name_map["nd_virtual_routers"] = "nd-virtual-routers"
                    return self.nd_virtual_routers

                if (child_yang_name == "neighbor-interfaces"):
                    if (self.neighbor_interfaces is None):
                        self.neighbor_interfaces = Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces()
                        self.neighbor_interfaces.parent = self
                        self._children_name_map["neighbor_interfaces"] = "neighbor-interfaces"
                    return self.neighbor_interfaces

                if (child_yang_name == "neighbor-summary"):
                    if (self.neighbor_summary is None):
                        self.neighbor_summary = Ipv6NodeDiscovery.Nodes.Node.NeighborSummary()
                        self.neighbor_summary.parent = self
                        self._children_name_map["neighbor_summary"] = "neighbor-summary"
                    return self.neighbor_summary

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bundle-interfaces" or name == "bundle-nodes" or name == "interfaces" or name == "nd-virtual-routers" or name == "neighbor-interfaces" or name == "neighbor-summary" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-ipv6-nd-oper:ipv6-node-discovery/%s" % self.get_segment_path()
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
                c = Ipv6NodeDiscovery.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-ipv6-nd-oper:ipv6-node-discovery" + path_buffer

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
                self.nodes = Ipv6NodeDiscovery.Nodes()
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
        self._top_entity = Ipv6NodeDiscovery()
        return self._top_entity

