""" ietf_routing 

This YANG module defines essential components for the management
of a routing subsystem.

Copyright (c) 2014 IETF Trust and the persons identified as
authors of the code. All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject to
the license terms contained in, the Simplified BSD License set
forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

The key words 'MUST', 'MUST NOT', 'REQUIRED', 'SHALL', 'SHALL
NOT', 'SHOULD', 'SHOULD NOT', 'RECOMMENDED', 'MAY', and
'OPTIONAL' in the module text are to be interpreted as described
in RFC 2119 (http\://tools.ietf.org/html/rfc2119).

This version of this YANG module is part of RFC XXXX
(http\://tools.ietf.org/html/rfcXXXX); see the RFC itself for
full legal notices.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AddressFamily(Identity):
    """
    Base identity from which identities describing address
    families are derived.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        super(AddressFamily, self).__init__("urn:ietf:params:xml:ns:yang:ietf-routing", "ietf-routing", "ietf-routing:address-family")


class FibRoute(Entity):
    """
    Return the active FIB route that a routing\-instance uses for
    sending packets to a destination address.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_routing.FibRoute.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_routing.FibRoute.Output>`
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        super(FibRoute, self).__init__()
        self._top_entity = None

        self.yang_name = "fib-route"
        self.yang_parent_name = "ietf-routing"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

        self.input = FibRoute.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = FibRoute.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "ietf-routing:fib-route"


    class Input(Entity):
        """
        
        
        .. attribute:: destination_address
        
        	Network layer destination address.  Address family specific modules MUST augment this container with a leaf named 'address'
        	**type**\:   :py:class:`DestinationAddress <ydk.models.ietf.ietf_routing.FibRoute.Input.DestinationAddress>`
        
        .. attribute:: routing_instance_name
        
        	Name of the routing instance whose forwarding information base is being queried.  If the routing instance with name equal to the value of this parameter doesn't exist, then this operation SHALL fail with error\-tag 'data\-missing' and error\-app\-tag 'routing\-instance\-not\-found'
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'rt'
        _revision = '2015-05-25'

        def __init__(self):
            super(FibRoute.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "fib-route"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"destination-address" : ("destination_address", FibRoute.Input.DestinationAddress)}
            self._child_list_classes = {}

            self.routing_instance_name = YLeaf(YType.str, "routing-instance-name")

            self.destination_address = FibRoute.Input.DestinationAddress()
            self.destination_address.parent = self
            self._children_name_map["destination_address"] = "destination-address"
            self._children_yang_names.add("destination-address")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "ietf-routing:fib-route/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(FibRoute.Input, ['routing_instance_name'], name, value)


        class DestinationAddress(Entity):
            """
            Network layer destination address.
            
            Address family specific modules MUST augment this
            container with a leaf named 'address'.
            
            .. attribute:: address_family
            
            	Address family
            	**type**\:   :py:class:`AddressFamily <ydk.models.ietf.ietf_routing.AddressFamily>`
            
            	**mandatory**\: True
            
            .. attribute:: ietf_ipv4_unicast_routing_address
            
            	IPv4 destination address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ietf_ipv6_unicast_routing_address
            
            	IPv6 destination address
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                super(FibRoute.Input.DestinationAddress, self).__init__()

                self.yang_name = "destination-address"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.address_family = YLeaf(YType.identityref, "address-family")

                self.ietf_ipv4_unicast_routing_address = YLeaf(YType.str, "ietf-ipv4-unicast-routing:ietf-ipv4-unicast-routing_address")

                self.ietf_ipv6_unicast_routing_address = YLeaf(YType.str, "ietf-ipv6-unicast-routing:ietf-ipv6-unicast-routing_address")
                self._segment_path = lambda: "destination-address"
                self._absolute_path = lambda: "ietf-routing:fib-route/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(FibRoute.Input.DestinationAddress, ['address_family', 'ietf_ipv4_unicast_routing_address', 'ietf_ipv6_unicast_routing_address'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: route
        
        	The active FIB route for the specified destination.  If the routing instance has no active FIB route for the destination address, no output is returned \- the server SHALL send an <rpc\-reply> containing a single element <ok>.  Address family specific modules MUST augment this list with appropriate route contents
        	**type**\:   :py:class:`Route <ydk.models.ietf.ietf_routing.FibRoute.Output.Route>`
        
        

        """

        _prefix = 'rt'
        _revision = '2015-05-25'

        def __init__(self):
            super(FibRoute.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "fib-route"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"route" : ("route", FibRoute.Output.Route)}
            self._child_list_classes = {}

            self.route = FibRoute.Output.Route()
            self.route.parent = self
            self._children_name_map["route"] = "route"
            self._children_yang_names.add("route")
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "ietf-routing:fib-route/%s" % self._segment_path()


        class Route(Entity):
            """
            The active FIB route for the specified destination.
            
            If the routing instance has no active FIB route for the
            destination address, no output is returned \- the server
            SHALL send an <rpc\-reply> containing a single element
            <ok>.
            
            Address family specific modules MUST augment this list
            with appropriate route contents.
            
            .. attribute:: active
            
            	Presence of this leaf indicates that the route is preferred among all routes in the same RIB that have the same destination prefix
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: address_family
            
            	Address family
            	**type**\:   :py:class:`AddressFamily <ydk.models.ietf.ietf_routing.AddressFamily>`
            
            	**mandatory**\: True
            
            .. attribute:: ietf_ipv4_unicast_routing_destination_prefix
            
            	IPv4 destination prefix
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
            
            .. attribute:: ietf_ipv6_unicast_routing_destination_prefix
            
            	IPv6 destination prefix
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
            
            .. attribute:: last_updated
            
            	Time stamp of the last modification of the route. If the route was never modified, it is the time when the route was inserted into the RIB
            	**type**\:  str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: next_hop
            
            	Route's next\-hop attribute
            	**type**\:   :py:class:`NextHop <ydk.models.ietf.ietf_routing.FibRoute.Output.Route.NextHop>`
            
            .. attribute:: source_protocol
            
            	Type of the routing protocol from which the route originated
            	**type**\:   :py:class:`RoutingProtocol <ydk.models.ietf.ietf_routing.RoutingProtocol>`
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                super(FibRoute.Output.Route, self).__init__()

                self.yang_name = "route"
                self.yang_parent_name = "output"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"next-hop" : ("next_hop", FibRoute.Output.Route.NextHop)}
                self._child_list_classes = {}

                self.active = YLeaf(YType.empty, "active")

                self.address_family = YLeaf(YType.identityref, "address-family")

                self.ietf_ipv4_unicast_routing_destination_prefix = YLeaf(YType.str, "ietf-ipv4-unicast-routing:ietf-ipv4-unicast-routing_destination-prefix")

                self.ietf_ipv6_unicast_routing_destination_prefix = YLeaf(YType.str, "ietf-ipv6-unicast-routing:ietf-ipv6-unicast-routing_destination-prefix")

                self.last_updated = YLeaf(YType.str, "last-updated")

                self.source_protocol = YLeaf(YType.identityref, "source-protocol")

                self.next_hop = FibRoute.Output.Route.NextHop()
                self.next_hop.parent = self
                self._children_name_map["next_hop"] = "next-hop"
                self._children_yang_names.add("next-hop")
                self._segment_path = lambda: "route"
                self._absolute_path = lambda: "ietf-routing:fib-route/output/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(FibRoute.Output.Route, ['active', 'address_family', 'ietf_ipv4_unicast_routing_destination_prefix', 'ietf_ipv6_unicast_routing_destination_prefix', 'last_updated', 'source_protocol'], name, value)


            class NextHop(Entity):
                """
                Route's next\-hop attribute.
                
                .. attribute:: ietf_ipv4_unicast_routing_next_hop_address
                
                	IPv4 address of the next\-hop
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ietf_ipv6_unicast_routing_next_hop_address
                
                	IPv6 address of the next\-hop
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ietf_routing_next_hop_address
                
                	IP address
                	**type**\:  str
                
                .. attribute:: outgoing_interface
                
                	Name of the outgoing interface
                	**type**\:  str
                
                .. attribute:: special_next_hop
                
                	Special next\-hop options
                	**type**\:   :py:class:`SpecialNextHop <ydk.models.ietf.ietf_routing.FibRoute.Output.Route.NextHop.SpecialNextHop>`
                
                

                """

                _prefix = 'rt'
                _revision = '2015-05-25'

                def __init__(self):
                    super(FibRoute.Output.Route.NextHop, self).__init__()

                    self.yang_name = "next-hop"
                    self.yang_parent_name = "route"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ietf_ipv4_unicast_routing_next_hop_address = YLeaf(YType.str, "ietf-ipv4-unicast-routing:ietf-ipv4-unicast-routing_next-hop-address")

                    self.ietf_ipv6_unicast_routing_next_hop_address = YLeaf(YType.str, "ietf-ipv6-unicast-routing:ietf-ipv6-unicast-routing_next-hop-address")

                    self.ietf_routing_next_hop_address = YLeaf(YType.str, "ietf-routing_next-hop-address")

                    self.outgoing_interface = YLeaf(YType.str, "outgoing-interface")

                    self.special_next_hop = YLeaf(YType.enumeration, "special-next-hop")
                    self._segment_path = lambda: "next-hop"
                    self._absolute_path = lambda: "ietf-routing:fib-route/output/route/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(FibRoute.Output.Route.NextHop, ['ietf_ipv4_unicast_routing_next_hop_address', 'ietf_ipv6_unicast_routing_next_hop_address', 'ietf_routing_next_hop_address', 'outgoing_interface', 'special_next_hop'], name, value)

                class SpecialNextHop(Enum):
                    """
                    SpecialNextHop

                    Special next\-hop options.

                    .. data:: blackhole = 0

                    	Silently discard the packet.

                    .. data:: unreachable = 1

                    	Discard the packet and notify the sender with an error

                    	message indicating that the destination host is

                    	unreachable.

                    .. data:: prohibit = 2

                    	Discard the packet and notify the sender with an error

                    	message indicating that the communication is

                    	administratively prohibited.

                    .. data:: receive = 3

                    	The packet will be received by the local system.

                    """

                    blackhole = Enum.YLeaf(0, "blackhole")

                    unreachable = Enum.YLeaf(1, "unreachable")

                    prohibit = Enum.YLeaf(2, "prohibit")

                    receive = Enum.YLeaf(3, "receive")


    def clone_ptr(self):
        self._top_entity = FibRoute()
        return self._top_entity

class Routing(Entity):
    """
    Configuration parameters for the routing subsystem.
    
    .. attribute:: routing_instance
    
    	Configuration of a routing instance
    	**type**\: list of    :py:class:`RoutingInstance <ydk.models.ietf.ietf_routing.Routing.RoutingInstance>`
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        super(Routing, self).__init__()
        self._top_entity = None

        self.yang_name = "routing"
        self.yang_parent_name = "ietf-routing"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"routing-instance" : ("routing_instance", Routing.RoutingInstance)}

        self.routing_instance = YList(self)
        self._segment_path = lambda: "ietf-routing:routing"

    def __setattr__(self, name, value):
        self._perform_setattr(Routing, [], name, value)


    class RoutingInstance(Entity):
        """
        Configuration of a routing instance.
        
        .. attribute:: name  <key>
        
        	The name of the routing instance.  For system\-controlled entries, the value of this leaf must be the same as the name of the corresponding entry in state data.  For user\-controlled entries, an arbitrary name can be used
        	**type**\:  str
        
        .. attribute:: description
        
        	Textual description of the routing instance
        	**type**\:  str
        
        .. attribute:: enabled
        
        	Enable/disable the routing instance.  If this parameter is false, the parent routing instance is disabled and does not appear in state data, despite any other configuration that might be present
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: interfaces
        
        	Assignment of the routing instance's interfaces
        	**type**\:   :py:class:`Interfaces <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.Interfaces>`
        
        .. attribute:: ribs
        
        	Configuration of RIBs
        	**type**\:   :py:class:`Ribs <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.Ribs>`
        
        .. attribute:: router_id
        
        	A 32\-bit number in the form of a dotted quad that is used by some routing protocols identifying a router
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
        
        .. attribute:: routing_protocols
        
        	Configuration of routing protocol instances
        	**type**\:   :py:class:`RoutingProtocols <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols>`
        
        .. attribute:: type
        
        	The type of the routing instance
        	**type**\:   :py:class:`RoutingInstance <ydk.models.ietf.ietf_routing.RoutingInstance>`
        
        	**default value**\: rt:default-routing-instance
        
        

        """

        _prefix = 'rt'
        _revision = '2015-05-25'

        def __init__(self):
            super(Routing.RoutingInstance, self).__init__()

            self.yang_name = "routing-instance"
            self.yang_parent_name = "routing"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"interfaces" : ("interfaces", Routing.RoutingInstance.Interfaces), "ribs" : ("ribs", Routing.RoutingInstance.Ribs), "routing-protocols" : ("routing_protocols", Routing.RoutingInstance.RoutingProtocols)}
            self._child_list_classes = {}

            self.name = YLeaf(YType.str, "name")

            self.description = YLeaf(YType.str, "description")

            self.enabled = YLeaf(YType.boolean, "enabled")

            self.router_id = YLeaf(YType.str, "router-id")

            self.type = YLeaf(YType.identityref, "type")

            self.interfaces = Routing.RoutingInstance.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.ribs = Routing.RoutingInstance.Ribs()
            self.ribs.parent = self
            self._children_name_map["ribs"] = "ribs"
            self._children_yang_names.add("ribs")

            self.routing_protocols = Routing.RoutingInstance.RoutingProtocols()
            self.routing_protocols.parent = self
            self._children_name_map["routing_protocols"] = "routing-protocols"
            self._children_yang_names.add("routing-protocols")
            self._segment_path = lambda: "routing-instance" + "[name='" + self.name.get() + "']"
            self._absolute_path = lambda: "ietf-routing:routing/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Routing.RoutingInstance, ['name', 'description', 'enabled', 'router_id', 'type'], name, value)


        class Interfaces(Entity):
            """
            Assignment of the routing instance's interfaces.
            
            .. attribute:: interface
            
            	The name of a configured network layer interface to be assigned to the routing\-instance
            	**type**\:  list of str
            
            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                super(Routing.RoutingInstance.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "routing-instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.interface = YLeafList(YType.str, "interface")
                self._segment_path = lambda: "interfaces"

            def __setattr__(self, name, value):
                self._perform_setattr(Routing.RoutingInstance.Interfaces, ['interface'], name, value)


        class Ribs(Entity):
            """
            Configuration of RIBs.
            
            .. attribute:: rib
            
            	Each entry contains configuration for a RIB identified by the 'name' key.  Entries having the same key as a system\-controlled entry of the list /routing\-state/routing\-instance/ribs/rib are used for configuring parameters of that entry. Other entries define additional user\-controlled RIBs
            	**type**\: list of    :py:class:`Rib <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.Ribs.Rib>`
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                super(Routing.RoutingInstance.Ribs, self).__init__()

                self.yang_name = "ribs"
                self.yang_parent_name = "routing-instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"rib" : ("rib", Routing.RoutingInstance.Ribs.Rib)}

                self.rib = YList(self)
                self._segment_path = lambda: "ribs"

            def __setattr__(self, name, value):
                self._perform_setattr(Routing.RoutingInstance.Ribs, [], name, value)


            class Rib(Entity):
                """
                Each entry contains configuration for a RIB identified
                by the 'name' key.
                
                Entries having the same key as a system\-controlled entry
                of the list /routing\-state/routing\-instance/ribs/rib are
                used for configuring parameters of that entry. Other
                entries define additional user\-controlled RIBs.
                
                .. attribute:: name  <key>
                
                	The name of the RIB.  For system\-controlled entries, the value of this leaf must be the same as the name of the corresponding entry in state data.  For user\-controlled entries, an arbitrary name can be used
                	**type**\:  str
                
                .. attribute:: address_family
                
                	Address family
                	**type**\:   :py:class:`AddressFamily <ydk.models.ietf.ietf_routing.AddressFamily>`
                
                .. attribute:: description
                
                	Textual description of the RIB
                	**type**\:  str
                
                

                """

                _prefix = 'rt'
                _revision = '2015-05-25'

                def __init__(self):
                    super(Routing.RoutingInstance.Ribs.Rib, self).__init__()

                    self.yang_name = "rib"
                    self.yang_parent_name = "ribs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.address_family = YLeaf(YType.identityref, "address-family")

                    self.description = YLeaf(YType.str, "description")
                    self._segment_path = lambda: "rib" + "[name='" + self.name.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Routing.RoutingInstance.Ribs.Rib, ['name', 'address_family', 'description'], name, value)


        class RoutingProtocols(Entity):
            """
            Configuration of routing protocol instances.
            
            .. attribute:: routing_protocol
            
            	Each entry contains configuration of a routing protocol instance
            	**type**\: list of    :py:class:`RoutingProtocol <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol>`
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                super(Routing.RoutingInstance.RoutingProtocols, self).__init__()

                self.yang_name = "routing-protocols"
                self.yang_parent_name = "routing-instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"routing-protocol" : ("routing_protocol", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol)}

                self.routing_protocol = YList(self)
                self._segment_path = lambda: "routing-protocols"

            def __setattr__(self, name, value):
                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols, [], name, value)


            class RoutingProtocol(Entity):
                """
                Each entry contains configuration of a routing protocol
                instance.
                
                .. attribute:: type  <key>
                
                	Type of the routing protocol \- an identity derived from the 'routing\-protocol' base identity
                	**type**\:   :py:class:`RoutingProtocol <ydk.models.ietf.ietf_routing.RoutingProtocol>`
                
                .. attribute:: name  <key>
                
                	An arbitrary name of the routing protocol instance
                	**type**\:  str
                
                .. attribute:: description
                
                	Textual description of the routing protocol instance
                	**type**\:  str
                
                .. attribute:: ospf
                
                	OSPF
                	**type**\:   :py:class:`Ospf <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf>`
                
                .. attribute:: static_routes
                
                	Configuration of the 'static' pseudo\-protocol.  Address\-family\-specific modules augment this node with their lists of routes
                	**type**\:   :py:class:`StaticRoutes <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes>`
                
                

                """

                _prefix = 'rt'
                _revision = '2015-05-25'

                def __init__(self):
                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol, self).__init__()

                    self.yang_name = "routing-protocol"
                    self.yang_parent_name = "routing-protocols"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"ospf" : ("ospf", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf), "static-routes" : ("static_routes", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes)}
                    self._child_list_classes = {}

                    self.type = YLeaf(YType.identityref, "type")

                    self.name = YLeaf(YType.str, "name")

                    self.description = YLeaf(YType.str, "description")

                    self.ospf = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf()
                    self.ospf.parent = self
                    self._children_name_map["ospf"] = "ospf"
                    self._children_yang_names.add("ospf")

                    self.static_routes = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes()
                    self.static_routes.parent = self
                    self._children_name_map["static_routes"] = "static-routes"
                    self._children_yang_names.add("static-routes")
                    self._segment_path = lambda: "routing-protocol" + "[type='" + self.type.get() + "']" + "[name='" + self.name.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol, ['type', 'name', 'description'], name, value)


                class Ospf(Entity):
                    """
                    OSPF.
                    
                    .. attribute:: all_instances_inherit
                    
                    	Inheritance support to all instances
                    	**type**\:   :py:class:`AllInstancesInherit <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit>`
                    
                    .. attribute:: instance
                    
                    	An OSPF routing protocol instance
                    	**type**\: list of    :py:class:`Instance <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance>`
                    
                    .. attribute:: operation_mode
                    
                    	OSPF operation mode
                    	**type**\:   :py:class:`OperationMode <ydk.models.ietf.ietf_ospf.OperationMode>`
                    
                    	**default value**\: ospf:ships-in-the-night
                    
                    

                    """

                    _prefix = 'ospf'
                    _revision = '2015-03-09'

                    def __init__(self):
                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf, self).__init__()

                        self.yang_name = "ospf"
                        self.yang_parent_name = "routing-protocol"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"all-instances-inherit" : ("all_instances_inherit", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit)}
                        self._child_list_classes = {"instance" : ("instance", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance)}

                        self.operation_mode = YLeaf(YType.identityref, "operation-mode")

                        self.all_instances_inherit = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit()
                        self.all_instances_inherit.parent = self
                        self._children_name_map["all_instances_inherit"] = "all-instances-inherit"
                        self._children_yang_names.add("all-instances-inherit")

                        self.instance = YList(self)
                        self._segment_path = lambda: "ietf-ospf:ospf"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf, ['operation_mode'], name, value)


                    class AllInstancesInherit(Entity):
                        """
                        Inheritance support to all instances.
                        
                        .. attribute:: area
                        
                        	Area config to be inherited by all areas in all instances
                        	**type**\:   :py:class:`Area <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Area>`
                        
                        .. attribute:: interface
                        
                        	Interface config to be inherited by all interfaces in all instances
                        	**type**\:   :py:class:`Interface <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Interface>`
                        
                        

                        """

                        _prefix = 'ospf'
                        _revision = '2015-03-09'

                        def __init__(self):
                            super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit, self).__init__()

                            self.yang_name = "all-instances-inherit"
                            self.yang_parent_name = "ospf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"area" : ("area", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Area), "interface" : ("interface", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Interface)}
                            self._child_list_classes = {}

                            self.area = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Area()
                            self.area.parent = self
                            self._children_name_map["area"] = "area"
                            self._children_yang_names.add("area")

                            self.interface = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Interface()
                            self.interface.parent = self
                            self._children_name_map["interface"] = "interface"
                            self._children_yang_names.add("interface")
                            self._segment_path = lambda: "all-instances-inherit"


                        class Area(Entity):
                            """
                            Area config to be inherited by all areas in
                            all instances.
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Area, self).__init__()

                                self.yang_name = "area"
                                self.yang_parent_name = "all-instances-inherit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self._segment_path = lambda: "area"


                        class Interface(Entity):
                            """
                            Interface config to be inherited by all interfaces
                            in all instances.
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "all-instances-inherit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self._segment_path = lambda: "interface"


                    class Instance(Entity):
                        """
                        An OSPF routing protocol instance.
                        
                        .. attribute:: af  <key>
                        
                        	Address\-family of the instance
                        	**type**\:   :py:class:`AddressFamily <ydk.models.ietf.ietf_routing.AddressFamily>`
                        
                        .. attribute:: admin_distance
                        
                        	Admin distance config state
                        	**type**\:   :py:class:`AdminDistance <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AdminDistance>`
                        
                        .. attribute:: all_areas_inherit
                        
                        	Inheritance for all areas
                        	**type**\:   :py:class:`AllAreasInherit <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit>`
                        
                        .. attribute:: area
                        
                        	List of ospf areas
                        	**type**\: list of    :py:class:`Area <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area>`
                        
                        .. attribute:: auto_cost
                        
                        	Auto cost config state
                        	**type**\:   :py:class:`AutoCost <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AutoCost>`
                        
                        .. attribute:: database_control
                        
                        	Database maintenance control
                        	**type**\:   :py:class:`DatabaseControl <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.DatabaseControl>`
                        
                        .. attribute:: enable
                        
                        	Enable/Disable the protocol
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        .. attribute:: fast_reroute
                        
                        	This container may be augmented with global parameters for IPFRR
                        	**type**\:   :py:class:`FastReroute <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute>`
                        
                        .. attribute:: graceful_restart
                        
                        	Graceful restart config state
                        	**type**\:   :py:class:`GracefulRestart <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.GracefulRestart>`
                        
                        .. attribute:: mpls
                        
                        	OSPF MPLS config state
                        	**type**\:   :py:class:`Mpls <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls>`
                        
                        .. attribute:: nsr
                        
                        	NSR config state
                        	**type**\:   :py:class:`Nsr <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Nsr>`
                        
                        .. attribute:: reload_control
                        
                        	Protocol reload control
                        	**type**\:   :py:class:`ReloadControl <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.ReloadControl>`
                        
                        .. attribute:: router_id
                        
                        	Defined in RFC 2328. A 32\-bit number that uniquely identifies the router
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                        
                        .. attribute:: spf_control
                        
                        	SPF calculation control
                        	**type**\:   :py:class:`SpfControl <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.SpfControl>`
                        
                        .. attribute:: topology
                        
                        	OSPF topology
                        	**type**\: list of    :py:class:`Topology <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology>`
                        
                        

                        """

                        _prefix = 'ospf'
                        _revision = '2015-03-09'

                        def __init__(self):
                            super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance, self).__init__()

                            self.yang_name = "instance"
                            self.yang_parent_name = "ospf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"admin-distance" : ("admin_distance", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AdminDistance), "all-areas-inherit" : ("all_areas_inherit", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit), "auto-cost" : ("auto_cost", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AutoCost), "database-control" : ("database_control", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.DatabaseControl), "fast-reroute" : ("fast_reroute", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute), "graceful-restart" : ("graceful_restart", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.GracefulRestart), "mpls" : ("mpls", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls), "nsr" : ("nsr", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Nsr), "reload-control" : ("reload_control", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.ReloadControl), "spf-control" : ("spf_control", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.SpfControl)}
                            self._child_list_classes = {"area" : ("area", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area), "topology" : ("topology", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology)}

                            self.af = YLeaf(YType.identityref, "af")

                            self.enable = YLeaf(YType.boolean, "enable")

                            self.router_id = YLeaf(YType.str, "router-id")

                            self.admin_distance = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AdminDistance()
                            self.admin_distance.parent = self
                            self._children_name_map["admin_distance"] = "admin-distance"
                            self._children_yang_names.add("admin-distance")

                            self.all_areas_inherit = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit()
                            self.all_areas_inherit.parent = self
                            self._children_name_map["all_areas_inherit"] = "all-areas-inherit"
                            self._children_yang_names.add("all-areas-inherit")

                            self.auto_cost = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AutoCost()
                            self.auto_cost.parent = self
                            self._children_name_map["auto_cost"] = "auto-cost"
                            self._children_yang_names.add("auto-cost")

                            self.database_control = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.DatabaseControl()
                            self.database_control.parent = self
                            self._children_name_map["database_control"] = "database-control"
                            self._children_yang_names.add("database-control")

                            self.fast_reroute = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute()
                            self.fast_reroute.parent = self
                            self._children_name_map["fast_reroute"] = "fast-reroute"
                            self._children_yang_names.add("fast-reroute")

                            self.graceful_restart = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.GracefulRestart()
                            self.graceful_restart.parent = self
                            self._children_name_map["graceful_restart"] = "graceful-restart"
                            self._children_yang_names.add("graceful-restart")

                            self.mpls = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls()
                            self.mpls.parent = self
                            self._children_name_map["mpls"] = "mpls"
                            self._children_yang_names.add("mpls")

                            self.nsr = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Nsr()
                            self.nsr.parent = self
                            self._children_name_map["nsr"] = "nsr"
                            self._children_yang_names.add("nsr")

                            self.reload_control = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.ReloadControl()
                            self.reload_control.parent = self
                            self._children_name_map["reload_control"] = "reload-control"
                            self._children_yang_names.add("reload-control")

                            self.spf_control = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.SpfControl()
                            self.spf_control.parent = self
                            self._children_name_map["spf_control"] = "spf-control"
                            self._children_yang_names.add("spf-control")

                            self.area = YList(self)
                            self.topology = YList(self)
                            self._segment_path = lambda: "instance" + "[af='" + self.af.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance, ['af', 'enable', 'router_id'], name, value)


                        class AdminDistance(Entity):
                            """
                            Admin distance config state.
                            
                            .. attribute:: external
                            
                            	Admin distance for both external route
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: inter_area
                            
                            	Admin distance for inter\-area route
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: internal
                            
                            	Admin distance for both intra\-area and inter\-area route
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: intra_area
                            
                            	Admin distance for intra\-area route
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AdminDistance, self).__init__()

                                self.yang_name = "admin-distance"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.external = YLeaf(YType.uint8, "external")

                                self.inter_area = YLeaf(YType.uint8, "inter-area")

                                self.internal = YLeaf(YType.uint8, "internal")

                                self.intra_area = YLeaf(YType.uint8, "intra-area")
                                self._segment_path = lambda: "admin-distance"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AdminDistance, ['external', 'inter_area', 'internal', 'intra_area'], name, value)


                        class AllAreasInherit(Entity):
                            """
                            Inheritance for all areas.
                            
                            .. attribute:: area
                            
                            	Area config to be inherited by all areas
                            	**type**\:   :py:class:`Area <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Area>`
                            
                            .. attribute:: interface
                            
                            	Interface config to be inherited by all interfaces in all areas
                            	**type**\:   :py:class:`Interface <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Interface>`
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit, self).__init__()

                                self.yang_name = "all-areas-inherit"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"area" : ("area", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Area), "interface" : ("interface", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Interface)}
                                self._child_list_classes = {}

                                self.area = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Area()
                                self.area.parent = self
                                self._children_name_map["area"] = "area"
                                self._children_yang_names.add("area")

                                self.interface = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Interface()
                                self.interface.parent = self
                                self._children_name_map["interface"] = "interface"
                                self._children_yang_names.add("interface")
                                self._segment_path = lambda: "all-areas-inherit"


                            class Area(Entity):
                                """
                                Area config to be inherited by all areas.
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Area, self).__init__()

                                    self.yang_name = "area"
                                    self.yang_parent_name = "all-areas-inherit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}
                                    self._segment_path = lambda: "area"


                            class Interface(Entity):
                                """
                                Interface config to be inherited by all interfaces
                                in all areas.
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Interface, self).__init__()

                                    self.yang_name = "interface"
                                    self.yang_parent_name = "all-areas-inherit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}
                                    self._segment_path = lambda: "interface"


                        class Area(Entity):
                            """
                            List of ospf areas
                            
                            .. attribute:: area_id  <key>
                            
                            	Area ID
                            	**type**\: one of the below types:
                            
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                            
                            
                            ----
                            .. attribute:: all_interfaces_inherit
                            
                            	Inheritance for all interfaces
                            	**type**\:   :py:class:`AllInterfacesInherit <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit>`
                            
                            .. attribute:: area_type
                            
                            	Area type
                            	**type**\:   :py:class:`AreaType <ydk.models.ietf.ietf_ospf.AreaType>`
                            
                            	**default value**\: normal
                            
                            .. attribute:: default_cost
                            
                            	Set the summary default\-cost for a stub or NSSA area
                            	**type**\:  int
                            
                            	**range:** 1..16777215
                            
                            .. attribute:: interface
                            
                            	List of OSPF interfaces
                            	**type**\: list of    :py:class:`Interface <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface>`
                            
                            .. attribute:: range
                            
                            	Summarize routes matching address/mask (border routers only)
                            	**type**\: list of    :py:class:`Range <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Range>`
                            
                            .. attribute:: sham_link
                            
                            	OSPF sham link
                            	**type**\: list of    :py:class:`ShamLink <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink>`
                            
                            .. attribute:: summary
                            
                            	Enable/Disable summary generation to the stub or NSSA area
                            	**type**\:  bool
                            
                            .. attribute:: virtual_link
                            
                            	OSPF virtual link
                            	**type**\: list of    :py:class:`VirtualLink <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink>`
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area, self).__init__()

                                self.yang_name = "area"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"all-interfaces-inherit" : ("all_interfaces_inherit", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit)}
                                self._child_list_classes = {"interface" : ("interface", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface), "range" : ("range", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Range), "sham-link" : ("sham_link", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink), "virtual-link" : ("virtual_link", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink)}

                                self.area_id = YLeaf(YType.str, "area-id")

                                self.area_type = YLeaf(YType.identityref, "area-type")

                                self.default_cost = YLeaf(YType.uint32, "default-cost")

                                self.summary = YLeaf(YType.boolean, "summary")

                                self.all_interfaces_inherit = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit()
                                self.all_interfaces_inherit.parent = self
                                self._children_name_map["all_interfaces_inherit"] = "all-interfaces-inherit"
                                self._children_yang_names.add("all-interfaces-inherit")

                                self.interface = YList(self)
                                self.range = YList(self)
                                self.sham_link = YList(self)
                                self.virtual_link = YList(self)
                                self._segment_path = lambda: "area" + "[area-id='" + self.area_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area, ['area_id', 'area_type', 'default_cost', 'summary'], name, value)


                            class AllInterfacesInherit(Entity):
                                """
                                Inheritance for all interfaces
                                
                                .. attribute:: interface
                                
                                	Interface config to be inherited by all interfaces
                                	**type**\:   :py:class:`Interface <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit.Interface>`
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit, self).__init__()

                                    self.yang_name = "all-interfaces-inherit"
                                    self.yang_parent_name = "area"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"interface" : ("interface", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit.Interface)}
                                    self._child_list_classes = {}

                                    self.interface = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit.Interface()
                                    self.interface.parent = self
                                    self._children_name_map["interface"] = "interface"
                                    self._children_yang_names.add("interface")
                                    self._segment_path = lambda: "all-interfaces-inherit"


                                class Interface(Entity):
                                    """
                                    Interface config to be inherited by all
                                    interfaces.
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit.Interface, self).__init__()

                                        self.yang_name = "interface"
                                        self.yang_parent_name = "all-interfaces-inherit"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}
                                        self._segment_path = lambda: "interface"


                            class Interface(Entity):
                                """
                                List of OSPF interfaces.
                                
                                .. attribute:: interface  <key>
                                
                                	Interface
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                                
                                .. attribute:: authentication
                                
                                	Authentication configuration
                                	**type**\:   :py:class:`Authentication <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication>`
                                
                                .. attribute:: bfd
                                
                                	Enable/disable bfd
                                	**type**\:  bool
                                
                                .. attribute:: cost
                                
                                	Interface cost
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                .. attribute:: dead_interval
                                
                                	Interval after which a neighbor is declared dead
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: demand_circuit
                                
                                	Enable/Disable demand circuit
                                	**type**\:  bool
                                
                                .. attribute:: enable
                                
                                	Enable/disable protocol on the interface
                                	**type**\:  bool
                                
                                	**default value**\: true
                                
                                .. attribute:: fast_reroute
                                
                                	Fast\-reroute configuration
                                	**type**\:   :py:class:`FastReroute <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute>`
                                
                                .. attribute:: hello_interval
                                
                                	Time between hello packets
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: lls
                                
                                	Enable/Disable link\-local signaling (LLS) support
                                	**type**\:  bool
                                
                                .. attribute:: mtu_ignore
                                
                                	Enable/Disable ignoring of MTU in DBD packets
                                	**type**\:  bool
                                
                                .. attribute:: multi_area
                                
                                	Configure ospf multi\-area
                                	**type**\:   :py:class:`MultiArea <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.MultiArea>`
                                
                                .. attribute:: network_type
                                
                                	Network type
                                	**type**\:   :py:class:`NetworkType <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.NetworkType>`
                                
                                .. attribute:: node_flag
                                
                                	Set prefix as a node representative prefix
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: passive
                                
                                	Enable/Disable passive
                                	**type**\:  bool
                                
                                .. attribute:: prefix_suppression
                                
                                	Suppress advertisement of the prefixes
                                	**type**\:  bool
                                
                                .. attribute:: retransmit_interval
                                
                                	Time between retransmitting unacknowledged Link State Advertisements (LSAs)
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: static_neighbors
                                
                                	Static configured neighbors
                                	**type**\:   :py:class:`StaticNeighbors <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors>`
                                
                                .. attribute:: topology
                                
                                	OSPF interface topology
                                	**type**\: list of    :py:class:`Topology <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Topology>`
                                
                                .. attribute:: transmit_delay
                                
                                	Estimated time needed to send link\-state update
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: ttl_security
                                
                                	TTL security check
                                	**type**\:   :py:class:`TtlSecurity <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.TtlSecurity>`
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface, self).__init__()

                                    self.yang_name = "interface"
                                    self.yang_parent_name = "area"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"authentication" : ("authentication", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication), "fast-reroute" : ("fast_reroute", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute), "multi-area" : ("multi_area", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.MultiArea), "static-neighbors" : ("static_neighbors", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors), "ttl-security" : ("ttl_security", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.TtlSecurity)}
                                    self._child_list_classes = {"topology" : ("topology", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Topology)}

                                    self.interface = YLeaf(YType.str, "interface")

                                    self.bfd = YLeaf(YType.boolean, "bfd")

                                    self.cost = YLeaf(YType.uint16, "cost")

                                    self.dead_interval = YLeaf(YType.uint16, "dead-interval")

                                    self.demand_circuit = YLeaf(YType.boolean, "demand-circuit")

                                    self.enable = YLeaf(YType.boolean, "enable")

                                    self.hello_interval = YLeaf(YType.uint16, "hello-interval")

                                    self.lls = YLeaf(YType.boolean, "lls")

                                    self.mtu_ignore = YLeaf(YType.boolean, "mtu-ignore")

                                    self.network_type = YLeaf(YType.enumeration, "network-type")

                                    self.node_flag = YLeaf(YType.boolean, "node-flag")

                                    self.passive = YLeaf(YType.boolean, "passive")

                                    self.prefix_suppression = YLeaf(YType.boolean, "prefix-suppression")

                                    self.retransmit_interval = YLeaf(YType.uint16, "retransmit-interval")

                                    self.transmit_delay = YLeaf(YType.uint16, "transmit-delay")

                                    self.authentication = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication()
                                    self.authentication.parent = self
                                    self._children_name_map["authentication"] = "authentication"
                                    self._children_yang_names.add("authentication")

                                    self.fast_reroute = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute()
                                    self.fast_reroute.parent = self
                                    self._children_name_map["fast_reroute"] = "fast-reroute"
                                    self._children_yang_names.add("fast-reroute")

                                    self.multi_area = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.MultiArea()
                                    self.multi_area.parent = self
                                    self._children_name_map["multi_area"] = "multi-area"
                                    self._children_yang_names.add("multi-area")

                                    self.static_neighbors = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors()
                                    self.static_neighbors.parent = self
                                    self._children_name_map["static_neighbors"] = "static-neighbors"
                                    self._children_yang_names.add("static-neighbors")

                                    self.ttl_security = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.TtlSecurity()
                                    self.ttl_security.parent = self
                                    self._children_name_map["ttl_security"] = "ttl-security"
                                    self._children_yang_names.add("ttl-security")

                                    self.topology = YList(self)
                                    self._segment_path = lambda: "interface" + "[interface='" + self.interface.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface, ['interface', 'bfd', 'cost', 'dead_interval', 'demand_circuit', 'enable', 'hello_interval', 'lls', 'mtu_ignore', 'network_type', 'node_flag', 'passive', 'prefix_suppression', 'retransmit_interval', 'transmit_delay'], name, value)

                                class NetworkType(Enum):
                                    """
                                    NetworkType

                                    Network type.

                                    .. data:: broadcast = 0

                                    	Specify OSPF broadcast multi-access network.

                                    .. data:: non_broadcast = 1

                                    	Specify OSPF Non-Broadcast Multi-Access

                                    	(NBMA) network.

                                    .. data:: point_to_multipoint = 2

                                    	Specify OSPF point-to-multipoint network.

                                    .. data:: point_to_point = 3

                                    	Specify OSPF point-to-point network.

                                    """

                                    broadcast = Enum.YLeaf(0, "broadcast")

                                    non_broadcast = Enum.YLeaf(1, "non-broadcast")

                                    point_to_multipoint = Enum.YLeaf(2, "point-to-multipoint")

                                    point_to_point = Enum.YLeaf(3, "point-to-point")



                                class Authentication(Entity):
                                    """
                                    Authentication configuration.
                                    
                                    .. attribute:: crypto_algorithm
                                    
                                    	Cryptographic algorithm associated with key
                                    	**type**\:   :py:class:`CryptoAlgorithm <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication.CryptoAlgorithm>`
                                    
                                    .. attribute:: key
                                    
                                    	Key string in ASCII format
                                    	**type**\:  str
                                    
                                    .. attribute:: key_chain
                                    
                                    	key\-chain name
                                    	**type**\:  str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_key_chain.KeyChains>`
                                    
                                    .. attribute:: sa
                                    
                                    	SA name
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication, self).__init__()

                                        self.yang_name = "authentication"
                                        self.yang_parent_name = "interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"crypto-algorithm" : ("crypto_algorithm", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication.CryptoAlgorithm)}
                                        self._child_list_classes = {}

                                        self.key = YLeaf(YType.str, "key")

                                        self.key_chain = YLeaf(YType.str, "key-chain")

                                        self.sa = YLeaf(YType.str, "sa")

                                        self.crypto_algorithm = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication.CryptoAlgorithm()
                                        self.crypto_algorithm.parent = self
                                        self._children_name_map["crypto_algorithm"] = "crypto-algorithm"
                                        self._children_yang_names.add("crypto-algorithm")
                                        self._segment_path = lambda: "authentication"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication, ['key', 'key_chain', 'sa'], name, value)


                                    class CryptoAlgorithm(Entity):
                                        """
                                        Cryptographic algorithm associated with key.
                                        
                                        .. attribute:: hmac_sha1_12
                                        
                                        	The HMAC\-SHA1\-12 algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha1_20
                                        
                                        	The HMAC\-SHA1\-20 algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_1
                                        
                                        	HMAC\-SHA\-1 authentication algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_256
                                        
                                        	HMAC\-SHA\-256 authentication algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_384
                                        
                                        	HMAC\-SHA\-384 authentication algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_512
                                        
                                        	HMAC\-SHA\-512 authentication algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: md5
                                        
                                        	The MD5 algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: sha_1
                                        
                                        	The SHA\-1 algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication.CryptoAlgorithm, self).__init__()

                                            self.yang_name = "crypto-algorithm"
                                            self.yang_parent_name = "authentication"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.hmac_sha1_12 = YLeaf(YType.empty, "hmac-sha1-12")

                                            self.hmac_sha1_20 = YLeaf(YType.empty, "hmac-sha1-20")

                                            self.hmac_sha_1 = YLeaf(YType.empty, "hmac-sha-1")

                                            self.hmac_sha_256 = YLeaf(YType.empty, "hmac-sha-256")

                                            self.hmac_sha_384 = YLeaf(YType.empty, "hmac-sha-384")

                                            self.hmac_sha_512 = YLeaf(YType.empty, "hmac-sha-512")

                                            self.md5 = YLeaf(YType.empty, "md5")

                                            self.sha_1 = YLeaf(YType.empty, "sha-1")
                                            self._segment_path = lambda: "crypto-algorithm"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication.CryptoAlgorithm, ['hmac_sha1_12', 'hmac_sha1_20', 'hmac_sha_1', 'hmac_sha_256', 'hmac_sha_384', 'hmac_sha_512', 'md5', 'sha_1'], name, value)


                                class FastReroute(Entity):
                                    """
                                    Fast\-reroute configuration.
                                    
                                    .. attribute:: lfa
                                    
                                    	LFA configuration
                                    	**type**\:   :py:class:`Lfa <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute, self).__init__()

                                        self.yang_name = "fast-reroute"
                                        self.yang_parent_name = "interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"lfa" : ("lfa", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa)}
                                        self._child_list_classes = {}

                                        self.lfa = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa()
                                        self.lfa.parent = self
                                        self._children_name_map["lfa"] = "lfa"
                                        self._children_yang_names.add("lfa")
                                        self._segment_path = lambda: "fast-reroute"


                                    class Lfa(Entity):
                                        """
                                        LFA configuration.
                                        
                                        .. attribute:: candidate_disabled
                                        
                                        	Prevent the interface to be used as backup
                                        	**type**\:  bool
                                        
                                        .. attribute:: enabled
                                        
                                        	Activates LFA. This model assumes activation of per\-prefix LFA
                                        	**type**\:  bool
                                        
                                        .. attribute:: remote_lfa
                                        
                                        	Remote LFA configuration
                                        	**type**\:   :py:class:`RemoteLfa <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa.RemoteLfa>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa, self).__init__()

                                            self.yang_name = "lfa"
                                            self.yang_parent_name = "fast-reroute"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"remote-lfa" : ("remote_lfa", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa.RemoteLfa)}
                                            self._child_list_classes = {}

                                            self.candidate_disabled = YLeaf(YType.boolean, "candidate-disabled")

                                            self.enabled = YLeaf(YType.boolean, "enabled")

                                            self.remote_lfa = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa.RemoteLfa()
                                            self.remote_lfa.parent = self
                                            self._children_name_map["remote_lfa"] = "remote-lfa"
                                            self._children_yang_names.add("remote-lfa")
                                            self._segment_path = lambda: "lfa"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa, ['candidate_disabled', 'enabled'], name, value)


                                        class RemoteLfa(Entity):
                                            """
                                            Remote LFA configuration.
                                            
                                            .. attribute:: enabled
                                            
                                            	Activates remote LFA
                                            	**type**\:  bool
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa.RemoteLfa, self).__init__()

                                                self.yang_name = "remote-lfa"
                                                self.yang_parent_name = "lfa"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.enabled = YLeaf(YType.boolean, "enabled")
                                                self._segment_path = lambda: "remote-lfa"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa.RemoteLfa, ['enabled'], name, value)


                                class MultiArea(Entity):
                                    """
                                    Configure ospf multi\-area.
                                    
                                    .. attribute:: cost
                                    
                                    	Interface cost for multi\-area
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: multi_area_id
                                    
                                    	Multi\-area ID
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.MultiArea, self).__init__()

                                        self.yang_name = "multi-area"
                                        self.yang_parent_name = "interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.cost = YLeaf(YType.uint16, "cost")

                                        self.multi_area_id = YLeaf(YType.str, "multi-area-id")
                                        self._segment_path = lambda: "multi-area"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.MultiArea, ['cost', 'multi_area_id'], name, value)


                                class StaticNeighbors(Entity):
                                    """
                                    Static configured neighbors.
                                    
                                    .. attribute:: neighbor
                                    
                                    	Specify a neighbor router
                                    	**type**\: list of    :py:class:`Neighbor <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors.Neighbor>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors, self).__init__()

                                        self.yang_name = "static-neighbors"
                                        self.yang_parent_name = "interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"neighbor" : ("neighbor", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors.Neighbor)}

                                        self.neighbor = YList(self)
                                        self._segment_path = lambda: "static-neighbors"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors, [], name, value)


                                    class Neighbor(Entity):
                                        """
                                        Specify a neighbor router.
                                        
                                        .. attribute:: address  <key>
                                        
                                        	Neighbor IP address
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        	**type**\:  str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        .. attribute:: cost
                                        
                                        	Neighbor cost
                                        	**type**\:  int
                                        
                                        	**range:** 1..65535
                                        
                                        .. attribute:: poll_interval
                                        
                                        	Neighbor poll interval
                                        	**type**\:  int
                                        
                                        	**range:** 1..65535
                                        
                                        	**units**\: seconds
                                        
                                        .. attribute:: priority
                                        
                                        	Neighbor priority for DR election
                                        	**type**\:  int
                                        
                                        	**range:** 1..255
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors.Neighbor, self).__init__()

                                            self.yang_name = "neighbor"
                                            self.yang_parent_name = "static-neighbors"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.address = YLeaf(YType.str, "address")

                                            self.cost = YLeaf(YType.uint16, "cost")

                                            self.poll_interval = YLeaf(YType.uint16, "poll-interval")

                                            self.priority = YLeaf(YType.uint8, "priority")
                                            self._segment_path = lambda: "neighbor" + "[address='" + self.address.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors.Neighbor, ['address', 'cost', 'poll_interval', 'priority'], name, value)


                                class Topology(Entity):
                                    """
                                    OSPF interface topology.
                                    
                                    .. attribute:: name  <key>
                                    
                                    	One of the topology enabled on this interface
                                    	**type**\:  str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.Ribs.Rib>`
                                    
                                    .. attribute:: cost
                                    
                                    	Interface cost for this topology
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Topology, self).__init__()

                                        self.yang_name = "topology"
                                        self.yang_parent_name = "interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.name = YLeaf(YType.str, "name")

                                        self.cost = YLeaf(YType.uint32, "cost")
                                        self._segment_path = lambda: "topology" + "[name='" + self.name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Topology, ['name', 'cost'], name, value)


                                class TtlSecurity(Entity):
                                    """
                                    TTL security check.
                                    
                                    .. attribute:: enable
                                    
                                    	Enable/Disable TTL security check
                                    	**type**\:  bool
                                    
                                    .. attribute:: hops
                                    
                                    	Maximum number of hops that a OSPF packet may have traveled
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.TtlSecurity, self).__init__()

                                        self.yang_name = "ttl-security"
                                        self.yang_parent_name = "interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.enable = YLeaf(YType.boolean, "enable")

                                        self.hops = YLeaf(YType.uint8, "hops")
                                        self._segment_path = lambda: "ttl-security"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.TtlSecurity, ['enable', 'hops'], name, value)


                            class Range(Entity):
                                """
                                Summarize routes matching address/mask (border
                                routers only)
                                
                                .. attribute:: prefix  <key>
                                
                                	IPv4 or IPv6 prefix
                                	**type**\:  str
                                
                                .. attribute:: advertise
                                
                                	Advertise or hide
                                	**type**\:  bool
                                
                                .. attribute:: cost
                                
                                	Cost of summary route
                                	**type**\:  int
                                
                                	**range:** 0..16777214
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Range, self).__init__()

                                    self.yang_name = "range"
                                    self.yang_parent_name = "area"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.prefix = YLeaf(YType.str, "prefix")

                                    self.advertise = YLeaf(YType.boolean, "advertise")

                                    self.cost = YLeaf(YType.uint32, "cost")
                                    self._segment_path = lambda: "range" + "[prefix='" + self.prefix.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Range, ['prefix', 'advertise', 'cost'], name, value)


                            class ShamLink(Entity):
                                """
                                OSPF sham link
                                
                                .. attribute:: local_id  <key>
                                
                                	Address of the local end\-point
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: remote_id  <key>
                                
                                	Address of the remote end\-point
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: authentication
                                
                                	Authentication configuration
                                	**type**\:   :py:class:`Authentication <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication>`
                                
                                .. attribute:: bfd
                                
                                	Enable/disable bfd
                                	**type**\:  bool
                                
                                .. attribute:: cost
                                
                                	Interface cost
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                .. attribute:: dead_interval
                                
                                	Interval after which a neighbor is declared dead
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: enable
                                
                                	Enable/disable protocol on the interface
                                	**type**\:  bool
                                
                                	**default value**\: true
                                
                                .. attribute:: hello_interval
                                
                                	Time between hello packets
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: lls
                                
                                	Enable/Disable link\-local signaling (LLS) support
                                	**type**\:  bool
                                
                                .. attribute:: mtu_ignore
                                
                                	Enable/Disable ignoring of MTU in DBD packets
                                	**type**\:  bool
                                
                                .. attribute:: prefix_suppression
                                
                                	Suppress advertisement of the prefixes
                                	**type**\:  bool
                                
                                .. attribute:: retransmit_interval
                                
                                	Time between retransmitting unacknowledged Link State Advertisements (LSAs)
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: transmit_delay
                                
                                	Estimated time needed to send link\-state update
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: ttl_security
                                
                                	TTL security check
                                	**type**\:   :py:class:`TtlSecurity <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.TtlSecurity>`
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink, self).__init__()

                                    self.yang_name = "sham-link"
                                    self.yang_parent_name = "area"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"authentication" : ("authentication", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication), "ttl-security" : ("ttl_security", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.TtlSecurity)}
                                    self._child_list_classes = {}

                                    self.local_id = YLeaf(YType.str, "local-id")

                                    self.remote_id = YLeaf(YType.str, "remote-id")

                                    self.bfd = YLeaf(YType.boolean, "bfd")

                                    self.cost = YLeaf(YType.uint16, "cost")

                                    self.dead_interval = YLeaf(YType.uint16, "dead-interval")

                                    self.enable = YLeaf(YType.boolean, "enable")

                                    self.hello_interval = YLeaf(YType.uint16, "hello-interval")

                                    self.lls = YLeaf(YType.boolean, "lls")

                                    self.mtu_ignore = YLeaf(YType.boolean, "mtu-ignore")

                                    self.prefix_suppression = YLeaf(YType.boolean, "prefix-suppression")

                                    self.retransmit_interval = YLeaf(YType.uint16, "retransmit-interval")

                                    self.transmit_delay = YLeaf(YType.uint16, "transmit-delay")

                                    self.authentication = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication()
                                    self.authentication.parent = self
                                    self._children_name_map["authentication"] = "authentication"
                                    self._children_yang_names.add("authentication")

                                    self.ttl_security = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.TtlSecurity()
                                    self.ttl_security.parent = self
                                    self._children_name_map["ttl_security"] = "ttl-security"
                                    self._children_yang_names.add("ttl-security")
                                    self._segment_path = lambda: "sham-link" + "[local-id='" + self.local_id.get() + "']" + "[remote-id='" + self.remote_id.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink, ['local_id', 'remote_id', 'bfd', 'cost', 'dead_interval', 'enable', 'hello_interval', 'lls', 'mtu_ignore', 'prefix_suppression', 'retransmit_interval', 'transmit_delay'], name, value)


                                class Authentication(Entity):
                                    """
                                    Authentication configuration.
                                    
                                    .. attribute:: crypto_algorithm
                                    
                                    	Cryptographic algorithm associated with key
                                    	**type**\:   :py:class:`CryptoAlgorithm <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication.CryptoAlgorithm>`
                                    
                                    .. attribute:: key
                                    
                                    	Key string in ASCII format
                                    	**type**\:  str
                                    
                                    .. attribute:: key_chain
                                    
                                    	key\-chain name
                                    	**type**\:  str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_key_chain.KeyChains>`
                                    
                                    .. attribute:: sa
                                    
                                    	SA name
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication, self).__init__()

                                        self.yang_name = "authentication"
                                        self.yang_parent_name = "sham-link"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"crypto-algorithm" : ("crypto_algorithm", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication.CryptoAlgorithm)}
                                        self._child_list_classes = {}

                                        self.key = YLeaf(YType.str, "key")

                                        self.key_chain = YLeaf(YType.str, "key-chain")

                                        self.sa = YLeaf(YType.str, "sa")

                                        self.crypto_algorithm = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication.CryptoAlgorithm()
                                        self.crypto_algorithm.parent = self
                                        self._children_name_map["crypto_algorithm"] = "crypto-algorithm"
                                        self._children_yang_names.add("crypto-algorithm")
                                        self._segment_path = lambda: "authentication"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication, ['key', 'key_chain', 'sa'], name, value)


                                    class CryptoAlgorithm(Entity):
                                        """
                                        Cryptographic algorithm associated with key.
                                        
                                        .. attribute:: hmac_sha1_12
                                        
                                        	The HMAC\-SHA1\-12 algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha1_20
                                        
                                        	The HMAC\-SHA1\-20 algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_1
                                        
                                        	HMAC\-SHA\-1 authentication algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_256
                                        
                                        	HMAC\-SHA\-256 authentication algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_384
                                        
                                        	HMAC\-SHA\-384 authentication algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_512
                                        
                                        	HMAC\-SHA\-512 authentication algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: md5
                                        
                                        	The MD5 algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: sha_1
                                        
                                        	The SHA\-1 algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication.CryptoAlgorithm, self).__init__()

                                            self.yang_name = "crypto-algorithm"
                                            self.yang_parent_name = "authentication"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.hmac_sha1_12 = YLeaf(YType.empty, "hmac-sha1-12")

                                            self.hmac_sha1_20 = YLeaf(YType.empty, "hmac-sha1-20")

                                            self.hmac_sha_1 = YLeaf(YType.empty, "hmac-sha-1")

                                            self.hmac_sha_256 = YLeaf(YType.empty, "hmac-sha-256")

                                            self.hmac_sha_384 = YLeaf(YType.empty, "hmac-sha-384")

                                            self.hmac_sha_512 = YLeaf(YType.empty, "hmac-sha-512")

                                            self.md5 = YLeaf(YType.empty, "md5")

                                            self.sha_1 = YLeaf(YType.empty, "sha-1")
                                            self._segment_path = lambda: "crypto-algorithm"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication.CryptoAlgorithm, ['hmac_sha1_12', 'hmac_sha1_20', 'hmac_sha_1', 'hmac_sha_256', 'hmac_sha_384', 'hmac_sha_512', 'md5', 'sha_1'], name, value)


                                class TtlSecurity(Entity):
                                    """
                                    TTL security check.
                                    
                                    .. attribute:: enable
                                    
                                    	Enable/Disable TTL security check
                                    	**type**\:  bool
                                    
                                    .. attribute:: hops
                                    
                                    	Maximum number of hops that a OSPF packet may have traveled
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.TtlSecurity, self).__init__()

                                        self.yang_name = "ttl-security"
                                        self.yang_parent_name = "sham-link"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.enable = YLeaf(YType.boolean, "enable")

                                        self.hops = YLeaf(YType.uint8, "hops")
                                        self._segment_path = lambda: "ttl-security"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.TtlSecurity, ['enable', 'hops'], name, value)


                            class VirtualLink(Entity):
                                """
                                OSPF virtual link
                                
                                .. attribute:: router_id  <key>
                                
                                	Virtual link router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                
                                .. attribute:: authentication
                                
                                	Authentication configuration
                                	**type**\:   :py:class:`Authentication <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication>`
                                
                                .. attribute:: bfd
                                
                                	Enable/disable bfd
                                	**type**\:  bool
                                
                                .. attribute:: cost
                                
                                	Interface cost
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                .. attribute:: dead_interval
                                
                                	Interval after which a neighbor is declared dead
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: enable
                                
                                	Enable/disable protocol on the interface
                                	**type**\:  bool
                                
                                	**default value**\: true
                                
                                .. attribute:: hello_interval
                                
                                	Time between hello packets
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: lls
                                
                                	Enable/Disable link\-local signaling (LLS) support
                                	**type**\:  bool
                                
                                .. attribute:: mtu_ignore
                                
                                	Enable/Disable ignoring of MTU in DBD packets
                                	**type**\:  bool
                                
                                .. attribute:: prefix_suppression
                                
                                	Suppress advertisement of the prefixes
                                	**type**\:  bool
                                
                                .. attribute:: retransmit_interval
                                
                                	Time between retransmitting unacknowledged Link State Advertisements (LSAs)
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: transmit_delay
                                
                                	Estimated time needed to send link\-state update
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: ttl_security
                                
                                	TTL security check
                                	**type**\:   :py:class:`TtlSecurity <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.TtlSecurity>`
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink, self).__init__()

                                    self.yang_name = "virtual-link"
                                    self.yang_parent_name = "area"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"authentication" : ("authentication", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication), "ttl-security" : ("ttl_security", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.TtlSecurity)}
                                    self._child_list_classes = {}

                                    self.router_id = YLeaf(YType.str, "router-id")

                                    self.bfd = YLeaf(YType.boolean, "bfd")

                                    self.cost = YLeaf(YType.uint16, "cost")

                                    self.dead_interval = YLeaf(YType.uint16, "dead-interval")

                                    self.enable = YLeaf(YType.boolean, "enable")

                                    self.hello_interval = YLeaf(YType.uint16, "hello-interval")

                                    self.lls = YLeaf(YType.boolean, "lls")

                                    self.mtu_ignore = YLeaf(YType.boolean, "mtu-ignore")

                                    self.prefix_suppression = YLeaf(YType.boolean, "prefix-suppression")

                                    self.retransmit_interval = YLeaf(YType.uint16, "retransmit-interval")

                                    self.transmit_delay = YLeaf(YType.uint16, "transmit-delay")

                                    self.authentication = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication()
                                    self.authentication.parent = self
                                    self._children_name_map["authentication"] = "authentication"
                                    self._children_yang_names.add("authentication")

                                    self.ttl_security = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.TtlSecurity()
                                    self.ttl_security.parent = self
                                    self._children_name_map["ttl_security"] = "ttl-security"
                                    self._children_yang_names.add("ttl-security")
                                    self._segment_path = lambda: "virtual-link" + "[router-id='" + self.router_id.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink, ['router_id', 'bfd', 'cost', 'dead_interval', 'enable', 'hello_interval', 'lls', 'mtu_ignore', 'prefix_suppression', 'retransmit_interval', 'transmit_delay'], name, value)


                                class Authentication(Entity):
                                    """
                                    Authentication configuration.
                                    
                                    .. attribute:: crypto_algorithm
                                    
                                    	Cryptographic algorithm associated with key
                                    	**type**\:   :py:class:`CryptoAlgorithm <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication.CryptoAlgorithm>`
                                    
                                    .. attribute:: key
                                    
                                    	Key string in ASCII format
                                    	**type**\:  str
                                    
                                    .. attribute:: key_chain
                                    
                                    	key\-chain name
                                    	**type**\:  str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_key_chain.KeyChains>`
                                    
                                    .. attribute:: sa
                                    
                                    	SA name
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication, self).__init__()

                                        self.yang_name = "authentication"
                                        self.yang_parent_name = "virtual-link"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"crypto-algorithm" : ("crypto_algorithm", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication.CryptoAlgorithm)}
                                        self._child_list_classes = {}

                                        self.key = YLeaf(YType.str, "key")

                                        self.key_chain = YLeaf(YType.str, "key-chain")

                                        self.sa = YLeaf(YType.str, "sa")

                                        self.crypto_algorithm = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication.CryptoAlgorithm()
                                        self.crypto_algorithm.parent = self
                                        self._children_name_map["crypto_algorithm"] = "crypto-algorithm"
                                        self._children_yang_names.add("crypto-algorithm")
                                        self._segment_path = lambda: "authentication"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication, ['key', 'key_chain', 'sa'], name, value)


                                    class CryptoAlgorithm(Entity):
                                        """
                                        Cryptographic algorithm associated with key.
                                        
                                        .. attribute:: hmac_sha1_12
                                        
                                        	The HMAC\-SHA1\-12 algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha1_20
                                        
                                        	The HMAC\-SHA1\-20 algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_1
                                        
                                        	HMAC\-SHA\-1 authentication algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_256
                                        
                                        	HMAC\-SHA\-256 authentication algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_384
                                        
                                        	HMAC\-SHA\-384 authentication algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_512
                                        
                                        	HMAC\-SHA\-512 authentication algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: md5
                                        
                                        	The MD5 algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: sha_1
                                        
                                        	The SHA\-1 algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication.CryptoAlgorithm, self).__init__()

                                            self.yang_name = "crypto-algorithm"
                                            self.yang_parent_name = "authentication"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.hmac_sha1_12 = YLeaf(YType.empty, "hmac-sha1-12")

                                            self.hmac_sha1_20 = YLeaf(YType.empty, "hmac-sha1-20")

                                            self.hmac_sha_1 = YLeaf(YType.empty, "hmac-sha-1")

                                            self.hmac_sha_256 = YLeaf(YType.empty, "hmac-sha-256")

                                            self.hmac_sha_384 = YLeaf(YType.empty, "hmac-sha-384")

                                            self.hmac_sha_512 = YLeaf(YType.empty, "hmac-sha-512")

                                            self.md5 = YLeaf(YType.empty, "md5")

                                            self.sha_1 = YLeaf(YType.empty, "sha-1")
                                            self._segment_path = lambda: "crypto-algorithm"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication.CryptoAlgorithm, ['hmac_sha1_12', 'hmac_sha1_20', 'hmac_sha_1', 'hmac_sha_256', 'hmac_sha_384', 'hmac_sha_512', 'md5', 'sha_1'], name, value)


                                class TtlSecurity(Entity):
                                    """
                                    TTL security check.
                                    
                                    .. attribute:: enable
                                    
                                    	Enable/Disable TTL security check
                                    	**type**\:  bool
                                    
                                    .. attribute:: hops
                                    
                                    	Maximum number of hops that a OSPF packet may have traveled
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.TtlSecurity, self).__init__()

                                        self.yang_name = "ttl-security"
                                        self.yang_parent_name = "virtual-link"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.enable = YLeaf(YType.boolean, "enable")

                                        self.hops = YLeaf(YType.uint8, "hops")
                                        self._segment_path = lambda: "ttl-security"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.TtlSecurity, ['enable', 'hops'], name, value)


                        class AutoCost(Entity):
                            """
                            Auto cost config state.
                            
                            .. attribute:: enable
                            
                            	Enable/Disable auto cost
                            	**type**\:  bool
                            
                            .. attribute:: reference_bandwidth
                            
                            	Configure reference bandwidth in term of Mbits
                            	**type**\:  int
                            
                            	**range:** 1..4294967
                            
                            	**units**\: Mbits
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AutoCost, self).__init__()

                                self.yang_name = "auto-cost"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.enable = YLeaf(YType.boolean, "enable")

                                self.reference_bandwidth = YLeaf(YType.uint32, "reference-bandwidth")
                                self._segment_path = lambda: "auto-cost"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AutoCost, ['enable', 'reference_bandwidth'], name, value)


                        class DatabaseControl(Entity):
                            """
                            Database maintenance control.
                            
                            .. attribute:: max_lsa
                            
                            	Maximum number of LSAs OSPF will receive
                            	**type**\:  int
                            
                            	**range:** 1..4294967294
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.DatabaseControl, self).__init__()

                                self.yang_name = "database-control"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.max_lsa = YLeaf(YType.uint32, "max-lsa")
                                self._segment_path = lambda: "database-control"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.DatabaseControl, ['max_lsa'], name, value)


                        class FastReroute(Entity):
                            """
                            This container may be augmented with global
                            parameters for IPFRR.
                            
                            .. attribute:: lfa
                            
                            	This container may be augmented with global parameters for LFA. Creating the container has no effect on LFA activation
                            	**type**\:   :py:class:`Lfa <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute.Lfa>`
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute, self).__init__()

                                self.yang_name = "fast-reroute"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"lfa" : ("lfa", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute.Lfa)}
                                self._child_list_classes = {}

                                self.lfa = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute.Lfa()
                                self.lfa.parent = self
                                self._children_name_map["lfa"] = "lfa"
                                self._children_yang_names.add("lfa")
                                self._segment_path = lambda: "fast-reroute"


                            class Lfa(Entity):
                                """
                                This container may be augmented with
                                global parameters for LFA.
                                Creating the container has no effect on
                                LFA activation.
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute.Lfa, self).__init__()

                                    self.yang_name = "lfa"
                                    self.yang_parent_name = "fast-reroute"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}
                                    self._segment_path = lambda: "lfa"


                        class GracefulRestart(Entity):
                            """
                            Graceful restart config state.
                            
                            .. attribute:: enable
                            
                            	Enable/Disable graceful restart as defined in RFC 3623
                            	**type**\:  bool
                            
                            .. attribute:: helper_enable
                            
                            	Enable RestartHelperSupport in RFC 3623 Section B.2
                            	**type**\:  bool
                            
                            .. attribute:: helper_strict_lsa_checking
                            
                            	RestartHelperStrictLSAChecking option in RFC 3623 Section B.2
                            	**type**\:  bool
                            
                            .. attribute:: restart_interval
                            
                            	RestartInterval option in RFC 3623 Section B.1
                            	**type**\:  int
                            
                            	**range:** 1..1800
                            
                            	**units**\: seconds
                            
                            	**default value**\: 120
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.GracefulRestart, self).__init__()

                                self.yang_name = "graceful-restart"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.enable = YLeaf(YType.boolean, "enable")

                                self.helper_enable = YLeaf(YType.boolean, "helper-enable")

                                self.helper_strict_lsa_checking = YLeaf(YType.boolean, "helper-strict-lsa-checking")

                                self.restart_interval = YLeaf(YType.uint16, "restart-interval")
                                self._segment_path = lambda: "graceful-restart"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.GracefulRestart, ['enable', 'helper_enable', 'helper_strict_lsa_checking', 'restart_interval'], name, value)


                        class Mpls(Entity):
                            """
                            OSPF MPLS config state.
                            
                            .. attribute:: ldp
                            
                            	OSPF MPLS LDP config state
                            	**type**\:   :py:class:`Ldp <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.Ldp>`
                            
                            .. attribute:: te_rid
                            
                            	Traffic Engineering stable IP address for system
                            	**type**\:   :py:class:`TeRid <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.TeRid>`
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls, self).__init__()

                                self.yang_name = "mpls"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ldp" : ("ldp", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.Ldp), "te-rid" : ("te_rid", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.TeRid)}
                                self._child_list_classes = {}

                                self.ldp = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.Ldp()
                                self.ldp.parent = self
                                self._children_name_map["ldp"] = "ldp"
                                self._children_yang_names.add("ldp")

                                self.te_rid = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.TeRid()
                                self.te_rid.parent = self
                                self._children_name_map["te_rid"] = "te-rid"
                                self._children_yang_names.add("te-rid")
                                self._segment_path = lambda: "mpls"


                            class Ldp(Entity):
                                """
                                OSPF MPLS LDP config state.
                                
                                .. attribute:: autoconfig
                                
                                	Enable LDP IGP interface auto\-configuration
                                	**type**\:  bool
                                
                                .. attribute:: igp_sync
                                
                                	Enable LDP IGP synchronization
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.Ldp, self).__init__()

                                    self.yang_name = "ldp"
                                    self.yang_parent_name = "mpls"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.autoconfig = YLeaf(YType.boolean, "autoconfig")

                                    self.igp_sync = YLeaf(YType.boolean, "igp-sync")
                                    self._segment_path = lambda: "ldp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.Ldp, ['autoconfig', 'igp_sync'], name, value)


                            class TeRid(Entity):
                                """
                                Traffic Engineering stable IP address for system.
                                
                                .. attribute:: interface
                                
                                	Take the interface's IPv4 address as TE router ID
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                                
                                .. attribute:: router_id
                                
                                	Explicitly configure the TE router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.TeRid, self).__init__()

                                    self.yang_name = "te-rid"
                                    self.yang_parent_name = "mpls"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.interface = YLeaf(YType.str, "interface")

                                    self.router_id = YLeaf(YType.str, "router-id")
                                    self._segment_path = lambda: "te-rid"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.TeRid, ['interface', 'router_id'], name, value)


                        class Nsr(Entity):
                            """
                            NSR config state.
                            
                            .. attribute:: enable
                            
                            	Enable/Disable NSR
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Nsr, self).__init__()

                                self.yang_name = "nsr"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.enable = YLeaf(YType.boolean, "enable")
                                self._segment_path = lambda: "nsr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Nsr, ['enable'], name, value)


                        class ReloadControl(Entity):
                            """
                            Protocol reload control.
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.ReloadControl, self).__init__()

                                self.yang_name = "reload-control"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self._segment_path = lambda: "reload-control"


                        class SpfControl(Entity):
                            """
                            SPF calculation control.
                            
                            .. attribute:: paths
                            
                            	Maximum number of ECMP paths
                            	**type**\:  int
                            
                            	**range:** 1..32
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.SpfControl, self).__init__()

                                self.yang_name = "spf-control"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.paths = YLeaf(YType.uint16, "paths")
                                self._segment_path = lambda: "spf-control"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.SpfControl, ['paths'], name, value)


                        class Topology(Entity):
                            """
                            OSPF topology.
                            
                            .. attribute:: name  <key>
                            
                            	RIB
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.Ribs.Rib>`
                            
                            .. attribute:: area
                            
                            	List of ospf areas
                            	**type**\: list of    :py:class:`Area <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area>`
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology, self).__init__()

                                self.yang_name = "topology"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"area" : ("area", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area)}

                                self.name = YLeaf(YType.str, "name")

                                self.area = YList(self)
                                self._segment_path = lambda: "topology" + "[name='" + self.name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology, ['name'], name, value)


                            class Area(Entity):
                                """
                                List of ospf areas
                                
                                .. attribute:: area_id  <key>
                                
                                	Area ID
                                	**type**\: one of the below types:
                                
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                
                                
                                ----
                                .. attribute:: area_type
                                
                                	Area type
                                	**type**\:   :py:class:`AreaType <ydk.models.ietf.ietf_ospf.AreaType>`
                                
                                	**default value**\: normal
                                
                                .. attribute:: default_cost
                                
                                	Set the summary default\-cost for a stub or NSSA area
                                	**type**\:  int
                                
                                	**range:** 1..16777215
                                
                                .. attribute:: range
                                
                                	Summarize routes matching address/mask (border routers only)
                                	**type**\: list of    :py:class:`Range <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area.Range>`
                                
                                .. attribute:: summary
                                
                                	Enable/Disable summary generation to the stub or NSSA area
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area, self).__init__()

                                    self.yang_name = "area"
                                    self.yang_parent_name = "topology"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"range" : ("range", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area.Range)}

                                    self.area_id = YLeaf(YType.str, "area-id")

                                    self.area_type = YLeaf(YType.identityref, "area-type")

                                    self.default_cost = YLeaf(YType.uint32, "default-cost")

                                    self.summary = YLeaf(YType.boolean, "summary")

                                    self.range = YList(self)
                                    self._segment_path = lambda: "area" + "[area-id='" + self.area_id.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area, ['area_id', 'area_type', 'default_cost', 'summary'], name, value)


                                class Range(Entity):
                                    """
                                    Summarize routes matching address/mask (border
                                    routers only)
                                    
                                    .. attribute:: prefix  <key>
                                    
                                    	IPv4 or IPv6 prefix
                                    	**type**\:  str
                                    
                                    .. attribute:: advertise
                                    
                                    	Advertise or hide
                                    	**type**\:  bool
                                    
                                    .. attribute:: cost
                                    
                                    	Cost of summary route
                                    	**type**\:  int
                                    
                                    	**range:** 0..16777214
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area.Range, self).__init__()

                                        self.yang_name = "range"
                                        self.yang_parent_name = "area"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.prefix = YLeaf(YType.str, "prefix")

                                        self.advertise = YLeaf(YType.boolean, "advertise")

                                        self.cost = YLeaf(YType.uint32, "cost")
                                        self._segment_path = lambda: "range" + "[prefix='" + self.prefix.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area.Range, ['prefix', 'advertise', 'cost'], name, value)


                class StaticRoutes(Entity):
                    """
                    Configuration of the 'static' pseudo\-protocol.
                    
                    Address\-family\-specific modules augment this node with
                    their lists of routes.
                    
                    .. attribute:: ipv4
                    
                    	Configuration of a 'static' pseudo\-protocol instance consists of a list of routes
                    	**type**\:   :py:class:`Ipv4 <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4>`
                    
                    .. attribute:: ipv6
                    
                    	Configuration of a 'static' pseudo\-protocol instance consists of a list of routes
                    	**type**\:   :py:class:`Ipv6 <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6>`
                    
                    

                    """

                    _prefix = 'rt'
                    _revision = '2015-05-25'

                    def __init__(self):
                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes, self).__init__()

                        self.yang_name = "static-routes"
                        self.yang_parent_name = "routing-protocol"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"ipv4" : ("ipv4", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4), "ipv6" : ("ipv6", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6)}
                        self._child_list_classes = {}

                        self.ipv4 = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4()
                        self.ipv4.parent = self
                        self._children_name_map["ipv4"] = "ipv4"
                        self._children_yang_names.add("ipv4")

                        self.ipv6 = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6()
                        self.ipv6.parent = self
                        self._children_name_map["ipv6"] = "ipv6"
                        self._children_yang_names.add("ipv6")
                        self._segment_path = lambda: "static-routes"


                    class Ipv4(Entity):
                        """
                        Configuration of a 'static' pseudo\-protocol instance
                        consists of a list of routes.
                        
                        .. attribute:: route
                        
                        	A user\-ordered list of static routes
                        	**type**\: list of    :py:class:`Route <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route>`
                        
                        

                        """

                        _prefix = 'v4ur'
                        _revision = '2015-05-25'

                        def __init__(self):
                            super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4, self).__init__()

                            self.yang_name = "ipv4"
                            self.yang_parent_name = "static-routes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"route" : ("route", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route)}

                            self.route = YList(self)
                            self._segment_path = lambda: "ietf-ipv4-unicast-routing:ipv4"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4, [], name, value)


                        class Route(Entity):
                            """
                            A user\-ordered list of static routes.
                            
                            .. attribute:: destination_prefix  <key>
                            
                            	IPv4 destination prefix
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                            
                            	**mandatory**\: True
                            
                            .. attribute:: description
                            
                            	Textual description of the route
                            	**type**\:  str
                            
                            .. attribute:: next_hop
                            
                            	Configuration of next\-hop
                            	**type**\:   :py:class:`NextHop <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop>`
                            
                            

                            """

                            _prefix = 'v4ur'
                            _revision = '2015-05-25'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route, self).__init__()

                                self.yang_name = "route"
                                self.yang_parent_name = "ipv4"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"next-hop" : ("next_hop", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop)}
                                self._child_list_classes = {}

                                self.destination_prefix = YLeaf(YType.str, "destination-prefix")

                                self.description = YLeaf(YType.str, "description")

                                self.next_hop = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop()
                                self.next_hop.parent = self
                                self._children_name_map["next_hop"] = "next-hop"
                                self._children_yang_names.add("next-hop")
                                self._segment_path = lambda: "route" + "[destination-prefix='" + self.destination_prefix.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route, ['destination_prefix', 'description'], name, value)


                            class NextHop(Entity):
                                """
                                Configuration of next\-hop.
                                
                                .. attribute:: next_hop_address
                                
                                	IPv4 address of the next\-hop
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: outgoing_interface
                                
                                	Name of the outgoing interface
                                	**type**\:  str
                                
                                .. attribute:: special_next_hop
                                
                                	Special next\-hop options
                                	**type**\:   :py:class:`SpecialNextHop <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop.SpecialNextHop>`
                                
                                

                                """

                                _prefix = 'v4ur'
                                _revision = '2015-05-25'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop, self).__init__()

                                    self.yang_name = "next-hop"
                                    self.yang_parent_name = "route"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                                    self.outgoing_interface = YLeaf(YType.str, "outgoing-interface")

                                    self.special_next_hop = YLeaf(YType.enumeration, "special-next-hop")
                                    self._segment_path = lambda: "next-hop"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop, ['next_hop_address', 'outgoing_interface', 'special_next_hop'], name, value)

                                class SpecialNextHop(Enum):
                                    """
                                    SpecialNextHop

                                    Special next\-hop options.

                                    .. data:: blackhole = 0

                                    	Silently discard the packet.

                                    .. data:: unreachable = 1

                                    	Discard the packet and notify the sender with an error

                                    	message indicating that the destination host is

                                    	unreachable.

                                    .. data:: prohibit = 2

                                    	Discard the packet and notify the sender with an error

                                    	message indicating that the communication is

                                    	administratively prohibited.

                                    .. data:: receive = 3

                                    	The packet will be received by the local system.

                                    """

                                    blackhole = Enum.YLeaf(0, "blackhole")

                                    unreachable = Enum.YLeaf(1, "unreachable")

                                    prohibit = Enum.YLeaf(2, "prohibit")

                                    receive = Enum.YLeaf(3, "receive")



                    class Ipv6(Entity):
                        """
                        Configuration of a 'static' pseudo\-protocol instance
                        consists of a list of routes.
                        
                        .. attribute:: route
                        
                        	A user\-ordered list of static routes
                        	**type**\: list of    :py:class:`Route <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route>`
                        
                        

                        """

                        _prefix = 'v6ur'
                        _revision = '2015-05-25'

                        def __init__(self):
                            super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6, self).__init__()

                            self.yang_name = "ipv6"
                            self.yang_parent_name = "static-routes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"route" : ("route", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route)}

                            self.route = YList(self)
                            self._segment_path = lambda: "ietf-ipv6-unicast-routing:ipv6"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6, [], name, value)


                        class Route(Entity):
                            """
                            A user\-ordered list of static routes.
                            
                            .. attribute:: destination_prefix  <key>
                            
                            	IPv6 destination prefix
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                            
                            	**mandatory**\: True
                            
                            .. attribute:: description
                            
                            	Textual description of the route
                            	**type**\:  str
                            
                            .. attribute:: next_hop
                            
                            	Configuration of next\-hop
                            	**type**\:   :py:class:`NextHop <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop>`
                            
                            

                            """

                            _prefix = 'v6ur'
                            _revision = '2015-05-25'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route, self).__init__()

                                self.yang_name = "route"
                                self.yang_parent_name = "ipv6"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"next-hop" : ("next_hop", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop)}
                                self._child_list_classes = {}

                                self.destination_prefix = YLeaf(YType.str, "destination-prefix")

                                self.description = YLeaf(YType.str, "description")

                                self.next_hop = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop()
                                self.next_hop.parent = self
                                self._children_name_map["next_hop"] = "next-hop"
                                self._children_yang_names.add("next-hop")
                                self._segment_path = lambda: "route" + "[destination-prefix='" + self.destination_prefix.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route, ['destination_prefix', 'description'], name, value)


                            class NextHop(Entity):
                                """
                                Configuration of next\-hop.
                                
                                .. attribute:: next_hop_address
                                
                                	IPv6 address of the next\-hop
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: outgoing_interface
                                
                                	Name of the outgoing interface
                                	**type**\:  str
                                
                                .. attribute:: special_next_hop
                                
                                	Special next\-hop options
                                	**type**\:   :py:class:`SpecialNextHop <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop.SpecialNextHop>`
                                
                                

                                """

                                _prefix = 'v6ur'
                                _revision = '2015-05-25'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop, self).__init__()

                                    self.yang_name = "next-hop"
                                    self.yang_parent_name = "route"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                                    self.outgoing_interface = YLeaf(YType.str, "outgoing-interface")

                                    self.special_next_hop = YLeaf(YType.enumeration, "special-next-hop")
                                    self._segment_path = lambda: "next-hop"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop, ['next_hop_address', 'outgoing_interface', 'special_next_hop'], name, value)

                                class SpecialNextHop(Enum):
                                    """
                                    SpecialNextHop

                                    Special next\-hop options.

                                    .. data:: blackhole = 0

                                    	Silently discard the packet.

                                    .. data:: unreachable = 1

                                    	Discard the packet and notify the sender with an error

                                    	message indicating that the destination host is

                                    	unreachable.

                                    .. data:: prohibit = 2

                                    	Discard the packet and notify the sender with an error

                                    	message indicating that the communication is

                                    	administratively prohibited.

                                    .. data:: receive = 3

                                    	The packet will be received by the local system.

                                    """

                                    blackhole = Enum.YLeaf(0, "blackhole")

                                    unreachable = Enum.YLeaf(1, "unreachable")

                                    prohibit = Enum.YLeaf(2, "prohibit")

                                    receive = Enum.YLeaf(3, "receive")


    def clone_ptr(self):
        self._top_entity = Routing()
        return self._top_entity

class RoutingInstance(Identity):
    """
    Base identity from which identities describing routing
    instance types are derived.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        super(RoutingInstance, self).__init__("urn:ietf:params:xml:ns:yang:ietf-routing", "ietf-routing", "ietf-routing:routing-instance")


class RoutingProtocol(Identity):
    """
    Base identity from which routing protocol identities are
    derived.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        super(RoutingProtocol, self).__init__("urn:ietf:params:xml:ns:yang:ietf-routing", "ietf-routing", "ietf-routing:routing-protocol")


class RoutingState(Entity):
    """
    State data of the routing subsystem.
    
    .. attribute:: routing_instance
    
    	Each list entry is a container for state data of a routing instance.  An implementation MUST support routing instance(s) of the type 'rt\:default\-routing\-instance', and MAY support other types. An implementation MAY restrict the number of routing instances of each supported type.  An implementation SHOULD create at least one system\-controlled instance, and MAY allow the clients to create user\-controlled routing instances in configuration
    	**type**\: list of    :py:class:`RoutingInstance <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance>`
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        super(RoutingState, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-state"
        self.yang_parent_name = "ietf-routing"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"routing-instance" : ("routing_instance", RoutingState.RoutingInstance)}

        self.routing_instance = YList(self)
        self._segment_path = lambda: "ietf-routing:routing-state"

    def __setattr__(self, name, value):
        self._perform_setattr(RoutingState, [], name, value)


    class RoutingInstance(Entity):
        """
        Each list entry is a container for state data of a routing
        instance.
        
        An implementation MUST support routing instance(s) of the
        type 'rt\:default\-routing\-instance', and MAY support other
        types. An implementation MAY restrict the number of routing
        instances of each supported type.
        
        An implementation SHOULD create at least one
        system\-controlled instance, and MAY allow the clients to
        create user\-controlled routing instances in
        configuration.
        
        .. attribute:: name  <key>
        
        	The name of the routing instance.  For system\-controlled instances the name is persistent, i.e., it SHOULD NOT change across reboots
        	**type**\:  str
        
        .. attribute:: interfaces
        
        	Network layer interfaces belonging to the routing instance
        	**type**\:   :py:class:`Interfaces <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Interfaces>`
        
        .. attribute:: ribs
        
        	Container for RIBs
        	**type**\:   :py:class:`Ribs <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Ribs>`
        
        .. attribute:: router_id
        
        	A 32\-bit number in the form of a dotted quad that is used by some routing protocols identifying a router
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
        
        .. attribute:: routing_protocols
        
        	Container for the list of routing protocol instances
        	**type**\:   :py:class:`RoutingProtocols <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols>`
        
        .. attribute:: type
        
        	The routing instance type
        	**type**\:   :py:class:`RoutingInstance <ydk.models.ietf.ietf_routing.RoutingInstance>`
        
        

        """

        _prefix = 'rt'
        _revision = '2015-05-25'

        def __init__(self):
            super(RoutingState.RoutingInstance, self).__init__()

            self.yang_name = "routing-instance"
            self.yang_parent_name = "routing-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"interfaces" : ("interfaces", RoutingState.RoutingInstance.Interfaces), "ribs" : ("ribs", RoutingState.RoutingInstance.Ribs), "routing-protocols" : ("routing_protocols", RoutingState.RoutingInstance.RoutingProtocols)}
            self._child_list_classes = {}

            self.name = YLeaf(YType.str, "name")

            self.router_id = YLeaf(YType.str, "router-id")

            self.type = YLeaf(YType.identityref, "type")

            self.interfaces = RoutingState.RoutingInstance.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.ribs = RoutingState.RoutingInstance.Ribs()
            self.ribs.parent = self
            self._children_name_map["ribs"] = "ribs"
            self._children_yang_names.add("ribs")

            self.routing_protocols = RoutingState.RoutingInstance.RoutingProtocols()
            self.routing_protocols.parent = self
            self._children_name_map["routing_protocols"] = "routing-protocols"
            self._children_yang_names.add("routing-protocols")
            self._segment_path = lambda: "routing-instance" + "[name='" + self.name.get() + "']"
            self._absolute_path = lambda: "ietf-routing:routing-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RoutingState.RoutingInstance, ['name', 'router_id', 'type'], name, value)


        class Interfaces(Entity):
            """
            Network layer interfaces belonging to the routing
            instance.
            
            .. attribute:: interface
            
            	Each entry is a reference to the name of a configured network layer interface
            	**type**\:  list of str
            
            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface>`
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                super(RoutingState.RoutingInstance.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "routing-instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.interface = YLeafList(YType.str, "interface")
                self._segment_path = lambda: "interfaces"

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingState.RoutingInstance.Interfaces, ['interface'], name, value)


        class Ribs(Entity):
            """
            Container for RIBs.
            
            .. attribute:: rib
            
            	Each entry represents a RIB identified by the 'name' key. All routes in a RIB MUST belong to the same address family.  For each routing instance, an implementation SHOULD provide one system\-controlled default RIB for each supported address family
            	**type**\: list of    :py:class:`Rib <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Ribs.Rib>`
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                super(RoutingState.RoutingInstance.Ribs, self).__init__()

                self.yang_name = "ribs"
                self.yang_parent_name = "routing-instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"rib" : ("rib", RoutingState.RoutingInstance.Ribs.Rib)}

                self.rib = YList(self)
                self._segment_path = lambda: "ribs"

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingState.RoutingInstance.Ribs, [], name, value)


            class Rib(Entity):
                """
                Each entry represents a RIB identified by the 'name'
                key. All routes in a RIB MUST belong to the same address
                family.
                
                For each routing instance, an implementation SHOULD
                provide one system\-controlled default RIB for each
                supported address family.
                
                .. attribute:: name  <key>
                
                	The name of the RIB
                	**type**\:  str
                
                .. attribute:: address_family
                
                	Address family
                	**type**\:   :py:class:`AddressFamily <ydk.models.ietf.ietf_routing.AddressFamily>`
                
                	**mandatory**\: True
                
                .. attribute:: default_rib
                
                	This flag has the value of 'true' if and only if the RIB is the default RIB for the given address family.  A default RIB always receives direct routes. By default it also receives routes from all routing protocols
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: routes
                
                	Current content of the RIB
                	**type**\:   :py:class:`Routes <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Ribs.Rib.Routes>`
                
                

                """

                _prefix = 'rt'
                _revision = '2015-05-25'

                def __init__(self):
                    super(RoutingState.RoutingInstance.Ribs.Rib, self).__init__()

                    self.yang_name = "rib"
                    self.yang_parent_name = "ribs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"routes" : ("routes", RoutingState.RoutingInstance.Ribs.Rib.Routes)}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.address_family = YLeaf(YType.identityref, "address-family")

                    self.default_rib = YLeaf(YType.boolean, "default-rib")

                    self.routes = RoutingState.RoutingInstance.Ribs.Rib.Routes()
                    self.routes.parent = self
                    self._children_name_map["routes"] = "routes"
                    self._children_yang_names.add("routes")
                    self._segment_path = lambda: "rib" + "[name='" + self.name.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingState.RoutingInstance.Ribs.Rib, ['name', 'address_family', 'default_rib'], name, value)


                class Routes(Entity):
                    """
                    Current content of the RIB.
                    
                    .. attribute:: route
                    
                    	A RIB route entry. This data node MUST be augmented with information specific for routes of each address family
                    	**type**\: list of    :py:class:`Route <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Ribs.Rib.Routes.Route>`
                    
                    

                    """

                    _prefix = 'rt'
                    _revision = '2015-05-25'

                    def __init__(self):
                        super(RoutingState.RoutingInstance.Ribs.Rib.Routes, self).__init__()

                        self.yang_name = "routes"
                        self.yang_parent_name = "rib"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"route" : ("route", RoutingState.RoutingInstance.Ribs.Rib.Routes.Route)}

                        self.route = YList(self)
                        self._segment_path = lambda: "routes"

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingState.RoutingInstance.Ribs.Rib.Routes, [], name, value)


                    class Route(Entity):
                        """
                        A RIB route entry. This data node MUST be augmented
                        with information specific for routes of each address
                        family.
                        
                        .. attribute:: destination_prefix  <key>
                        
                        	Destination IP address with prefix
                        	**type**\:  str
                        
                        .. attribute:: active
                        
                        	Presence of this leaf indicates that the route is preferred among all routes in the same RIB that have the same destination prefix
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: last_updated
                        
                        	Time stamp of the last modification of the route. If the route was never modified, it is the time when the route was inserted into the RIB
                        	**type**\:  str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        .. attribute:: metric
                        
                        	Route metric
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: next_hop
                        
                        	Route's next\-hop attribute
                        	**type**\:   :py:class:`NextHop <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop>`
                        
                        .. attribute:: route_preference
                        
                        	This route attribute, also known as administrative distance, allows for selecting the preferred route among routes with the same destination prefix. A smaller value means a more preferred route
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: route_type
                        
                        	OSPF route type
                        	**type**\:   :py:class:`RouteType <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.RouteType>`
                        
                        .. attribute:: source_protocol
                        
                        	Type of the routing protocol from which the route originated
                        	**type**\:   :py:class:`RoutingProtocol <ydk.models.ietf.ietf_routing.RoutingProtocol>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: tag
                        
                        	OSPF route tag
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: update_source
                        
                        	Update source for the route
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'rt'
                        _revision = '2015-05-25'

                        def __init__(self):
                            super(RoutingState.RoutingInstance.Ribs.Rib.Routes.Route, self).__init__()

                            self.yang_name = "route"
                            self.yang_parent_name = "routes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"next-hop" : ("next_hop", RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop)}
                            self._child_list_classes = {}

                            self.destination_prefix = YLeaf(YType.str, "destination-prefix")

                            self.active = YLeaf(YType.empty, "active")

                            self.last_updated = YLeaf(YType.str, "last-updated")

                            self.metric = YLeaf(YType.uint32, "metric")

                            self.route_preference = YLeaf(YType.uint32, "route-preference")

                            self.route_type = YLeaf(YType.enumeration, "ietf-ospf:route-type")

                            self.source_protocol = YLeaf(YType.identityref, "source-protocol")

                            self.tag = YLeaf(YType.uint32, "ietf-ospf:tag")

                            self.update_source = YLeaf(YType.str, "update-source")

                            self.next_hop = RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop()
                            self.next_hop.parent = self
                            self._children_name_map["next_hop"] = "next-hop"
                            self._children_yang_names.add("next-hop")
                            self._segment_path = lambda: "route" + "[destination-prefix='" + self.destination_prefix.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingState.RoutingInstance.Ribs.Rib.Routes.Route, ['destination_prefix', 'active', 'last_updated', 'metric', 'route_preference', 'route_type', 'source_protocol', 'tag', 'update_source'], name, value)

                        class RouteType(Enum):
                            """
                            RouteType

                            OSPF route type

                            .. data:: intra_area = 0

                            	OSPF intra-area route

                            .. data:: inter_area = 1

                            	OSPF inter-area route

                            .. data:: external_1 = 2

                            	OSPF external route type 1

                            .. data:: external_2 = 3

                            	OSPF External route type 2

                            .. data:: nssa_1 = 4

                            	OSPF NSSA external route type 1

                            .. data:: nssa_2 = 5

                            	OSPF NSSA external route type 2

                            """

                            intra_area = Enum.YLeaf(0, "intra-area")

                            inter_area = Enum.YLeaf(1, "inter-area")

                            external_1 = Enum.YLeaf(2, "external-1")

                            external_2 = Enum.YLeaf(3, "external-2")

                            nssa_1 = Enum.YLeaf(4, "nssa-1")

                            nssa_2 = Enum.YLeaf(5, "nssa-2")



                        class NextHop(Entity):
                            """
                            Route's next\-hop attribute.
                            
                            .. attribute:: next_hop_address
                            
                            	IP address
                            	**type**\:  str
                            
                            .. attribute:: outgoing_interface
                            
                            	Name of the outgoing interface
                            	**type**\:  str
                            
                            .. attribute:: special_next_hop
                            
                            	Special next\-hop options
                            	**type**\:   :py:class:`SpecialNextHop <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop.SpecialNextHop>`
                            
                            

                            """

                            _prefix = 'rt'
                            _revision = '2015-05-25'

                            def __init__(self):
                                super(RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop, self).__init__()

                                self.yang_name = "next-hop"
                                self.yang_parent_name = "route"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                                self.outgoing_interface = YLeaf(YType.str, "outgoing-interface")

                                self.special_next_hop = YLeaf(YType.enumeration, "special-next-hop")
                                self._segment_path = lambda: "next-hop"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop, ['next_hop_address', 'outgoing_interface', 'special_next_hop'], name, value)

                            class SpecialNextHop(Enum):
                                """
                                SpecialNextHop

                                Special next\-hop options.

                                .. data:: blackhole = 0

                                	Silently discard the packet.

                                .. data:: unreachable = 1

                                	Discard the packet and notify the sender with an error

                                	message indicating that the destination host is

                                	unreachable.

                                .. data:: prohibit = 2

                                	Discard the packet and notify the sender with an error

                                	message indicating that the communication is

                                	administratively prohibited.

                                .. data:: receive = 3

                                	The packet will be received by the local system.

                                """

                                blackhole = Enum.YLeaf(0, "blackhole")

                                unreachable = Enum.YLeaf(1, "unreachable")

                                prohibit = Enum.YLeaf(2, "prohibit")

                                receive = Enum.YLeaf(3, "receive")



        class RoutingProtocols(Entity):
            """
            Container for the list of routing protocol instances.
            
            .. attribute:: routing_protocol
            
            	State data of a routing protocol instance.  An implementation MUST provide exactly one system\-controlled instance of the type 'direct'. Other instances MAY be created by configuration
            	**type**\: list of    :py:class:`RoutingProtocol <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol>`
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                super(RoutingState.RoutingInstance.RoutingProtocols, self).__init__()

                self.yang_name = "routing-protocols"
                self.yang_parent_name = "routing-instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"routing-protocol" : ("routing_protocol", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol)}

                self.routing_protocol = YList(self)
                self._segment_path = lambda: "routing-protocols"

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols, [], name, value)


            class RoutingProtocol(Entity):
                """
                State data of a routing protocol instance.
                
                An implementation MUST provide exactly one
                system\-controlled instance of the type 'direct'. Other
                instances MAY be created by configuration.
                
                .. attribute:: type  <key>
                
                	Type of the routing protocol
                	**type**\:   :py:class:`RoutingProtocol <ydk.models.ietf.ietf_routing.RoutingProtocol>`
                
                .. attribute:: name  <key>
                
                	The name of the routing protocol instance.  For system\-controlled instances this name is persistent, i.e., it SHOULD NOT change across reboots
                	**type**\:  str
                
                .. attribute:: ospf
                
                	OSPF
                	**type**\:   :py:class:`Ospf <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf>`
                
                

                """

                _prefix = 'rt'
                _revision = '2015-05-25'

                def __init__(self):
                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol, self).__init__()

                    self.yang_name = "routing-protocol"
                    self.yang_parent_name = "routing-protocols"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"ospf" : ("ospf", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf)}
                    self._child_list_classes = {}

                    self.type = YLeaf(YType.identityref, "type")

                    self.name = YLeaf(YType.str, "name")

                    self.ospf = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf()
                    self.ospf.parent = self
                    self._children_name_map["ospf"] = "ospf"
                    self._children_yang_names.add("ospf")
                    self._segment_path = lambda: "routing-protocol" + "[type='" + self.type.get() + "']" + "[name='" + self.name.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol, ['type', 'name'], name, value)


                class Ospf(Entity):
                    """
                    OSPF
                    
                    .. attribute:: instance
                    
                    	An OSPF routing protocol instance
                    	**type**\: list of    :py:class:`Instance <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance>`
                    
                    .. attribute:: operation_mode
                    
                    	OSPF operation mode
                    	**type**\:   :py:class:`OperationMode <ydk.models.ietf.ietf_ospf.OperationMode>`
                    
                    

                    """

                    _prefix = 'ospf'
                    _revision = '2015-03-09'

                    def __init__(self):
                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf, self).__init__()

                        self.yang_name = "ospf"
                        self.yang_parent_name = "routing-protocol"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"instance" : ("instance", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance)}

                        self.operation_mode = YLeaf(YType.identityref, "operation-mode")

                        self.instance = YList(self)
                        self._segment_path = lambda: "ietf-ospf:ospf"

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf, ['operation_mode'], name, value)


                    class Instance(Entity):
                        """
                        An OSPF routing protocol instance.
                        
                        .. attribute:: af  <key>
                        
                        	Address\-family of the instance
                        	**type**\:   :py:class:`AddressFamily <ydk.models.ietf.ietf_routing.AddressFamily>`
                        
                        .. attribute:: area
                        
                        	List of OSPF areas
                        	**type**\: list of    :py:class:`Area <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area>`
                        
                        .. attribute:: as_scope_lsas
                        
                        	List OSPF AS scope LSA databases
                        	**type**\: list of    :py:class:`AsScopeLsas <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas>`
                        
                        .. attribute:: router_id
                        
                        	Defined in RFC 2328. A 32\-bit number that uniquely identifies the router
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                        
                        .. attribute:: topology
                        
                        	OSPF topology
                        	**type**\: list of    :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology>`
                        
                        

                        """

                        _prefix = 'ospf'
                        _revision = '2015-03-09'

                        def __init__(self):
                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance, self).__init__()

                            self.yang_name = "instance"
                            self.yang_parent_name = "ospf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"area" : ("area", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area), "as-scope-lsas" : ("as_scope_lsas", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas), "topology" : ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology)}

                            self.af = YLeaf(YType.identityref, "af")

                            self.router_id = YLeaf(YType.str, "router-id")

                            self.area = YList(self)
                            self.as_scope_lsas = YList(self)
                            self.topology = YList(self)
                            self._segment_path = lambda: "instance" + "[af='" + self.af.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance, ['af', 'router_id'], name, value)


                        class Area(Entity):
                            """
                            List of OSPF areas
                            
                            .. attribute:: area_id  <key>
                            
                            	Area ID
                            	**type**\: one of the below types:
                            
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                            
                            
                            ----
                            .. attribute:: area_scope_lsas
                            
                            	List OSPF area scope LSA databases
                            	**type**\: list of    :py:class:`AreaScopeLsas <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas>`
                            
                            .. attribute:: interfaces
                            
                            	List of OSPF interfaces
                            	**type**\: list of    :py:class:`Interfaces <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces>`
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area, self).__init__()

                                self.yang_name = "area"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"area-scope-lsas" : ("area_scope_lsas", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas), "interfaces" : ("interfaces", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces)}

                                self.area_id = YLeaf(YType.str, "area-id")

                                self.area_scope_lsas = YList(self)
                                self.interfaces = YList(self)
                                self._segment_path = lambda: "area" + "[area-id='" + self.area_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area, ['area_id'], name, value)


                            class AreaScopeLsas(Entity):
                                """
                                List OSPF area scope LSA databases
                                
                                .. attribute:: lsa_type  <key>
                                
                                	OSPF area scope LSA type
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: area_scope_lsa
                                
                                	List of OSPF area scope LSAs
                                	**type**\: list of    :py:class:`AreaScopeLsa <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa>`
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas, self).__init__()

                                    self.yang_name = "area-scope-lsas"
                                    self.yang_parent_name = "area"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"area-scope-lsa" : ("area_scope_lsa", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa)}

                                    self.lsa_type = YLeaf(YType.uint8, "lsa-type")

                                    self.area_scope_lsa = YList(self)
                                    self._segment_path = lambda: "area-scope-lsas" + "[lsa-type='" + self.lsa_type.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas, ['lsa_type'], name, value)


                                class AreaScopeLsa(Entity):
                                    """
                                    List of OSPF area scope LSAs
                                    
                                    .. attribute:: lsa_id  <key>
                                    
                                    	LSA ID
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    
                                    ----
                                    .. attribute:: adv_router  <key>
                                    
                                    	Advertising router
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: decoded_completed
                                    
                                    	The OSPF LSA body is fully decoded
                                    	**type**\:  bool
                                    
                                    .. attribute:: ospfv2
                                    
                                    	OSPFv2 LSA
                                    	**type**\:   :py:class:`Ospfv2 <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2>`
                                    
                                    .. attribute:: ospfv3
                                    
                                    	OSPFv3 LSA
                                    	**type**\:   :py:class:`Ospfv3 <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3>`
                                    
                                    .. attribute:: raw_data
                                    
                                    	The complete LSA in network byte order as received/sent over the wire
                                    	**type**\:  str
                                    
                                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa, self).__init__()

                                        self.yang_name = "area-scope-lsa"
                                        self.yang_parent_name = "area-scope-lsas"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"ospfv2" : ("ospfv2", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2), "ospfv3" : ("ospfv3", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3)}
                                        self._child_list_classes = {}

                                        self.lsa_id = YLeaf(YType.str, "lsa-id")

                                        self.adv_router = YLeaf(YType.str, "adv-router")

                                        self.decoded_completed = YLeaf(YType.boolean, "decoded-completed")

                                        self.raw_data = YLeaf(YType.str, "raw-data")

                                        self.ospfv2 = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2()
                                        self.ospfv2.parent = self
                                        self._children_name_map["ospfv2"] = "ospfv2"
                                        self._children_yang_names.add("ospfv2")

                                        self.ospfv3 = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3()
                                        self.ospfv3.parent = self
                                        self._children_name_map["ospfv3"] = "ospfv3"
                                        self._children_yang_names.add("ospfv3")
                                        self._segment_path = lambda: "area-scope-lsa" + "[lsa-id='" + self.lsa_id.get() + "']" + "[adv-router='" + self.adv_router.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa, ['lsa_id', 'adv_router', 'decoded_completed', 'raw_data'], name, value)


                                    class Ospfv2(Entity):
                                        """
                                        OSPFv2 LSA
                                        
                                        .. attribute:: body
                                        
                                        	Decoded OSPFv2 LSA body data
                                        	**type**\:   :py:class:`Body <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body>`
                                        
                                        .. attribute:: header
                                        
                                        	Decoded OSPFv2 LSA header data
                                        	**type**\:   :py:class:`Header <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2, self).__init__()

                                            self.yang_name = "ospfv2"
                                            self.yang_parent_name = "area-scope-lsa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"body" : ("body", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body), "header" : ("header", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header)}
                                            self._child_list_classes = {}

                                            self.body = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body()
                                            self.body.parent = self
                                            self._children_name_map["body"] = "body"
                                            self._children_yang_names.add("body")

                                            self.header = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header()
                                            self.header.parent = self
                                            self._children_name_map["header"] = "header"
                                            self._children_yang_names.add("header")
                                            self._segment_path = lambda: "ospfv2"


                                        class Body(Entity):
                                            """
                                            Decoded OSPFv2 LSA body data.
                                            
                                            .. attribute:: external
                                            
                                            	External LSA
                                            	**type**\:   :py:class:`External <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External>`
                                            
                                            .. attribute:: network
                                            
                                            	Network LSA
                                            	**type**\:   :py:class:`Network <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Network>`
                                            
                                            .. attribute:: opaque
                                            
                                            	Opaque LSA
                                            	**type**\:   :py:class:`Opaque <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque>`
                                            
                                            .. attribute:: router
                                            
                                            	Router LSA
                                            	**type**\:   :py:class:`Router <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router>`
                                            
                                            .. attribute:: summary
                                            
                                            	Summary LSA
                                            	**type**\:   :py:class:`Summary <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary>`
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body, self).__init__()

                                                self.yang_name = "body"
                                                self.yang_parent_name = "ospfv2"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {"external" : ("external", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External), "network" : ("network", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Network), "opaque" : ("opaque", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque), "router" : ("router", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router), "summary" : ("summary", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary)}
                                                self._child_list_classes = {}

                                                self.external = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External()
                                                self.external.parent = self
                                                self._children_name_map["external"] = "external"
                                                self._children_yang_names.add("external")

                                                self.network = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Network()
                                                self.network.parent = self
                                                self._children_name_map["network"] = "network"
                                                self._children_yang_names.add("network")

                                                self.opaque = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque()
                                                self.opaque.parent = self
                                                self._children_name_map["opaque"] = "opaque"
                                                self._children_yang_names.add("opaque")

                                                self.router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router()
                                                self.router.parent = self
                                                self._children_name_map["router"] = "router"
                                                self._children_yang_names.add("router")

                                                self.summary = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary()
                                                self.summary.parent = self
                                                self._children_name_map["summary"] = "summary"
                                                self._children_yang_names.add("summary")
                                                self._segment_path = lambda: "body"


                                            class External(Entity):
                                                """
                                                External LSA.
                                                
                                                .. attribute:: network_mask
                                                
                                                	The IP address mask for the network
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: topology
                                                
                                                	Topology specific information
                                                	**type**\: list of    :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External.Topology>`
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External, self).__init__()

                                                    self.yang_name = "external"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {"topology" : ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External.Topology)}

                                                    self.network_mask = YLeaf(YType.str, "network-mask")

                                                    self.topology = YList(self)
                                                    self._segment_path = lambda: "external"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External, ['network_mask'], name, value)


                                                class Topology(Entity):
                                                    """
                                                    Topology specific information.
                                                    
                                                    .. attribute:: mt_id  <key>
                                                    
                                                    	The MT\-ID for topology enabled on the link
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: external_route_tag
                                                    
                                                    	Route tag
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: flags
                                                    
                                                    	Flags
                                                    	**type**\:   :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External.Topology.Flags>`
                                                    
                                                    .. attribute:: forwarding_address
                                                    
                                                    	Forwarding address
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric for the topology
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..16777215
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External.Topology, self).__init__()

                                                        self.yang_name = "topology"
                                                        self.yang_parent_name = "external"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.mt_id = YLeaf(YType.uint8, "mt-id")

                                                        self.external_route_tag = YLeaf(YType.uint32, "external-route-tag")

                                                        self.flags = YLeaf(YType.bits, "flags")

                                                        self.forwarding_address = YLeaf(YType.str, "forwarding-address")

                                                        self.metric = YLeaf(YType.uint32, "metric")
                                                        self._segment_path = lambda: "topology" + "[mt-id='" + self.mt_id.get() + "']"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External.Topology, ['mt_id', 'external_route_tag', 'flags', 'forwarding_address', 'metric'], name, value)


                                            class Network(Entity):
                                                """
                                                Network LSA.
                                                
                                                .. attribute:: attached_router
                                                
                                                	List of the routers attached to the network
                                                	**type**\:  list of str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                
                                                .. attribute:: network_mask
                                                
                                                	The IP address mask for the network
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Network, self).__init__()

                                                    self.yang_name = "network"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.attached_router = YLeafList(YType.str, "attached-router")

                                                    self.network_mask = YLeaf(YType.str, "network-mask")
                                                    self._segment_path = lambda: "network"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Network, ['attached_router', 'network_mask'], name, value)


                                            class Opaque(Entity):
                                                """
                                                Opaque LSA.
                                                
                                                .. attribute:: link_tlv
                                                
                                                	Link TLV
                                                	**type**\:   :py:class:`LinkTlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv>`
                                                
                                                .. attribute:: router_address_tlv
                                                
                                                	Router address TLV
                                                	**type**\:   :py:class:`RouterAddressTlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv>`
                                                
                                                .. attribute:: unknown_tlv
                                                
                                                	Unknown TLV
                                                	**type**\: list of    :py:class:`UnknownTlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.UnknownTlv>`
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque, self).__init__()

                                                    self.yang_name = "opaque"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {"link-tlv" : ("link_tlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv), "router-address-tlv" : ("router_address_tlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv)}
                                                    self._child_list_classes = {"unknown-tlv" : ("unknown_tlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.UnknownTlv)}

                                                    self.link_tlv = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv()
                                                    self.link_tlv.parent = self
                                                    self._children_name_map["link_tlv"] = "link-tlv"
                                                    self._children_yang_names.add("link-tlv")

                                                    self.router_address_tlv = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv()
                                                    self.router_address_tlv.parent = self
                                                    self._children_name_map["router_address_tlv"] = "router-address-tlv"
                                                    self._children_yang_names.add("router-address-tlv")

                                                    self.unknown_tlv = YList(self)
                                                    self._segment_path = lambda: "opaque"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque, [], name, value)


                                                class LinkTlv(Entity):
                                                    """
                                                    Link TLV.
                                                    
                                                    .. attribute:: admin_group
                                                    
                                                    	Administrative group/Resource class/Color
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: link_id
                                                    
                                                    	Link ID
                                                    	**type**\: one of the below types:
                                                    
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    
                                                    ----
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    
                                                    ----
                                                    .. attribute:: link_type
                                                    
                                                    	Link type
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    .. attribute:: local_if_ipv4_addr
                                                    
                                                    	List of local interface IPv4 addresses
                                                    	**type**\:  list of str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: local_remote_ipv4_addr
                                                    
                                                    	List of remote interface IPv4 addresses
                                                    	**type**\:  list of str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: max_bandwidth
                                                    
                                                    	Maximum bandwidth
                                                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                                                    
                                                    	**range:** \-92233720368547758.08..92233720368547758.07
                                                    
                                                    .. attribute:: max_reservable_bandwidth
                                                    
                                                    	Maximum reservable bandwidth
                                                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                                                    
                                                    	**range:** \-92233720368547758.08..92233720368547758.07
                                                    
                                                    .. attribute:: te_metric
                                                    
                                                    	TE metric
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: unknown_subtlv
                                                    
                                                    	Unknown sub\-TLV
                                                    	**type**\: list of    :py:class:`UnknownSubtlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv>`
                                                    
                                                    .. attribute:: unreserved_bandwidth
                                                    
                                                    	Unreserved bandwidth
                                                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                                                    
                                                    	**range:** \-92233720368547758.08..92233720368547758.07
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv, self).__init__()

                                                        self.yang_name = "link-tlv"
                                                        self.yang_parent_name = "opaque"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {"unknown-subtlv" : ("unknown_subtlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv)}

                                                        self.admin_group = YLeaf(YType.uint32, "admin-group")

                                                        self.link_id = YLeaf(YType.str, "link-id")

                                                        self.link_type = YLeaf(YType.uint8, "link-type")

                                                        self.local_if_ipv4_addr = YLeafList(YType.str, "local-if-ipv4-addr")

                                                        self.local_remote_ipv4_addr = YLeafList(YType.str, "local-remote-ipv4-addr")

                                                        self.max_bandwidth = YLeaf(YType.str, "max-bandwidth")

                                                        self.max_reservable_bandwidth = YLeaf(YType.str, "max-reservable-bandwidth")

                                                        self.te_metric = YLeaf(YType.uint32, "te-metric")

                                                        self.unreserved_bandwidth = YLeaf(YType.str, "unreserved-bandwidth")

                                                        self.unknown_subtlv = YList(self)
                                                        self._segment_path = lambda: "link-tlv"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv, ['admin_group', 'link_id', 'link_type', 'local_if_ipv4_addr', 'local_remote_ipv4_addr', 'max_bandwidth', 'max_reservable_bandwidth', 'te_metric', 'unreserved_bandwidth'], name, value)


                                                    class UnknownSubtlv(Entity):
                                                        """
                                                        Unknown sub\-TLV.
                                                        
                                                        .. attribute:: type  <key>
                                                        
                                                        	TLV type
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..65535
                                                        
                                                        .. attribute:: length
                                                        
                                                        	TLV length
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..65535
                                                        
                                                        .. attribute:: value
                                                        
                                                        	TLV value
                                                        	**type**\:  str
                                                        
                                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                                        
                                                        

                                                        """

                                                        _prefix = 'ospf'
                                                        _revision = '2015-03-09'

                                                        def __init__(self):
                                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv, self).__init__()

                                                            self.yang_name = "unknown-subtlv"
                                                            self.yang_parent_name = "link-tlv"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {}
                                                            self._child_list_classes = {}

                                                            self.type = YLeaf(YType.uint16, "type")

                                                            self.length = YLeaf(YType.uint16, "length")

                                                            self.value = YLeaf(YType.str, "value")
                                                            self._segment_path = lambda: "unknown-subtlv" + "[type='" + self.type.get() + "']"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv, ['type', 'length', 'value'], name, value)


                                                class RouterAddressTlv(Entity):
                                                    """
                                                    Router address TLV.
                                                    
                                                    .. attribute:: router_address
                                                    
                                                    	Router address
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv, self).__init__()

                                                        self.yang_name = "router-address-tlv"
                                                        self.yang_parent_name = "opaque"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.router_address = YLeaf(YType.str, "router-address")
                                                        self._segment_path = lambda: "router-address-tlv"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv, ['router_address'], name, value)


                                                class UnknownTlv(Entity):
                                                    """
                                                    Unknown TLV.
                                                    
                                                    .. attribute:: type  <key>
                                                    
                                                    	TLV type
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    .. attribute:: length
                                                    
                                                    	TLV length
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    .. attribute:: value
                                                    
                                                    	TLV value
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.UnknownTlv, self).__init__()

                                                        self.yang_name = "unknown-tlv"
                                                        self.yang_parent_name = "opaque"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.type = YLeaf(YType.uint16, "type")

                                                        self.length = YLeaf(YType.uint16, "length")

                                                        self.value = YLeaf(YType.str, "value")
                                                        self._segment_path = lambda: "unknown-tlv" + "[type='" + self.type.get() + "']"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.UnknownTlv, ['type', 'length', 'value'], name, value)


                                            class Router(Entity):
                                                """
                                                Router LSA.
                                                
                                                .. attribute:: flags
                                                
                                                	Flags
                                                	**type**\:   :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Flags>`
                                                
                                                .. attribute:: link
                                                
                                                	Router LSA link
                                                	**type**\: list of    :py:class:`Link <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link>`
                                                
                                                .. attribute:: num_of_links
                                                
                                                	Number of links
                                                	**type**\:  int
                                                
                                                	**range:** 0..65535
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router, self).__init__()

                                                    self.yang_name = "router"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {"link" : ("link", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link)}

                                                    self.flags = YLeaf(YType.bits, "flags")

                                                    self.num_of_links = YLeaf(YType.uint16, "num-of-links")

                                                    self.link = YList(self)
                                                    self._segment_path = lambda: "router"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router, ['flags', 'num_of_links'], name, value)


                                                class Link(Entity):
                                                    """
                                                    Router LSA link.
                                                    
                                                    .. attribute:: link_id  <key>
                                                    
                                                    	Link ID
                                                    	**type**\: one of the below types:
                                                    
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    
                                                    ----
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                    
                                                    
                                                    ----
                                                    .. attribute:: link_data  <key>
                                                    
                                                    	Link data
                                                    	**type**\: one of the below types:
                                                    
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    
                                                    ----
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    
                                                    ----
                                                    .. attribute:: topology
                                                    
                                                    	Topology specific information
                                                    	**type**\: list of    :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link.Topology>`
                                                    
                                                    .. attribute:: type
                                                    
                                                    	Link type
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link, self).__init__()

                                                        self.yang_name = "link"
                                                        self.yang_parent_name = "router"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {"topology" : ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link.Topology)}

                                                        self.link_id = YLeaf(YType.str, "link-id")

                                                        self.link_data = YLeaf(YType.str, "link-data")

                                                        self.type = YLeaf(YType.uint8, "type")

                                                        self.topology = YList(self)
                                                        self._segment_path = lambda: "link" + "[link-id='" + self.link_id.get() + "']" + "[link-data='" + self.link_data.get() + "']"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link, ['link_id', 'link_data', 'type'], name, value)


                                                    class Topology(Entity):
                                                        """
                                                        Topology specific information.
                                                        
                                                        .. attribute:: mt_id  <key>
                                                        
                                                        	The MT\-ID for topology enabled on the link
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: metric
                                                        
                                                        	Metric for the topology
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..65535
                                                        
                                                        

                                                        """

                                                        _prefix = 'ospf'
                                                        _revision = '2015-03-09'

                                                        def __init__(self):
                                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link.Topology, self).__init__()

                                                            self.yang_name = "topology"
                                                            self.yang_parent_name = "link"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {}
                                                            self._child_list_classes = {}

                                                            self.mt_id = YLeaf(YType.uint8, "mt-id")

                                                            self.metric = YLeaf(YType.uint16, "metric")
                                                            self._segment_path = lambda: "topology" + "[mt-id='" + self.mt_id.get() + "']"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link.Topology, ['mt_id', 'metric'], name, value)


                                            class Summary(Entity):
                                                """
                                                Summary LSA.
                                                
                                                .. attribute:: network_mask
                                                
                                                	The IP address mask for the network
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: topology
                                                
                                                	Topology specific information
                                                	**type**\: list of    :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary.Topology>`
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary, self).__init__()

                                                    self.yang_name = "summary"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {"topology" : ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary.Topology)}

                                                    self.network_mask = YLeaf(YType.str, "network-mask")

                                                    self.topology = YList(self)
                                                    self._segment_path = lambda: "summary"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary, ['network_mask'], name, value)


                                                class Topology(Entity):
                                                    """
                                                    Topology specific information.
                                                    
                                                    .. attribute:: mt_id  <key>
                                                    
                                                    	The MT\-ID for topology enabled on the link
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric for the topology
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..16777215
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary.Topology, self).__init__()

                                                        self.yang_name = "topology"
                                                        self.yang_parent_name = "summary"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.mt_id = YLeaf(YType.uint8, "mt-id")

                                                        self.metric = YLeaf(YType.uint32, "metric")
                                                        self._segment_path = lambda: "topology" + "[mt-id='" + self.mt_id.get() + "']"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary.Topology, ['mt_id', 'metric'], name, value)


                                        class Header(Entity):
                                            """
                                            Decoded OSPFv2 LSA header data.
                                            
                                            .. attribute:: adv_router
                                            
                                            	LSA advertising router
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: age
                                            
                                            	LSA age
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: checksum
                                            
                                            	LSA checksum
                                            	**type**\:  str
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: length
                                            
                                            	LSA length
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: lsa_id
                                            
                                            	LSA ID
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: opaque_id
                                            
                                            	Opaque id
                                            	**type**\:  int
                                            
                                            	**range:** 0..16777215
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: opaque_type
                                            
                                            	Opaque type
                                            	**type**\:  int
                                            
                                            	**range:** 0..255
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: options
                                            
                                            	LSA option
                                            	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header.Options>`
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: seq_num
                                            
                                            	LSA sequence number
                                            	**type**\:  str
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: type
                                            
                                            	LSA type
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header, self).__init__()

                                                self.yang_name = "header"
                                                self.yang_parent_name = "ospfv2"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.adv_router = YLeaf(YType.str, "adv-router")

                                                self.age = YLeaf(YType.uint16, "age")

                                                self.checksum = YLeaf(YType.str, "checksum")

                                                self.length = YLeaf(YType.uint16, "length")

                                                self.lsa_id = YLeaf(YType.str, "lsa-id")

                                                self.opaque_id = YLeaf(YType.uint32, "opaque-id")

                                                self.opaque_type = YLeaf(YType.uint8, "opaque-type")

                                                self.options = YLeaf(YType.bits, "options")

                                                self.seq_num = YLeaf(YType.str, "seq-num")

                                                self.type = YLeaf(YType.uint16, "type")
                                                self._segment_path = lambda: "header"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header, ['adv_router', 'age', 'checksum', 'length', 'lsa_id', 'opaque_id', 'opaque_type', 'options', 'seq_num', 'type'], name, value)


                                    class Ospfv3(Entity):
                                        """
                                        OSPFv3 LSA
                                        
                                        .. attribute:: body
                                        
                                        	Decoded OSPF LSA body data
                                        	**type**\:   :py:class:`Body <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body>`
                                        
                                        .. attribute:: header
                                        
                                        	Decoded OSPFv3 LSA header data
                                        	**type**\:   :py:class:`Header <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3, self).__init__()

                                            self.yang_name = "ospfv3"
                                            self.yang_parent_name = "area-scope-lsa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"body" : ("body", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body), "header" : ("header", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header)}
                                            self._child_list_classes = {}

                                            self.body = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body()
                                            self.body.parent = self
                                            self._children_name_map["body"] = "body"
                                            self._children_yang_names.add("body")

                                            self.header = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header()
                                            self.header.parent = self
                                            self._children_name_map["header"] = "header"
                                            self._children_yang_names.add("header")
                                            self._segment_path = lambda: "ospfv3"


                                        class Body(Entity):
                                            """
                                            Decoded OSPF LSA body data.
                                            
                                            .. attribute:: as_external
                                            
                                            	AS\-External LSA
                                            	**type**\:   :py:class:`AsExternal <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal>`
                                            
                                            .. attribute:: inter_area_prefix
                                            
                                            	Inter\-Area\-Prefix LSA
                                            	**type**\:   :py:class:`InterAreaPrefix <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaPrefix>`
                                            
                                            .. attribute:: inter_area_router
                                            
                                            	Inter\-Area\-Router LSA
                                            	**type**\:   :py:class:`InterAreaRouter <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter>`
                                            
                                            .. attribute:: intra_area_prefix
                                            
                                            	Intra\-Area\-Prefix LSA
                                            	**type**\:   :py:class:`IntraAreaPrefix <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix>`
                                            
                                            .. attribute:: link
                                            
                                            	Link LSA
                                            	**type**\:   :py:class:`Link <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link>`
                                            
                                            .. attribute:: network
                                            
                                            	Network LSA
                                            	**type**\:   :py:class:`Network <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network>`
                                            
                                            .. attribute:: nssa
                                            
                                            	NSSA LSA
                                            	**type**\:   :py:class:`Nssa <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa>`
                                            
                                            .. attribute:: router
                                            
                                            	Router LSA
                                            	**type**\:   :py:class:`Router <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router>`
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body, self).__init__()

                                                self.yang_name = "body"
                                                self.yang_parent_name = "ospfv3"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {"as-external" : ("as_external", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal), "inter-area-prefix" : ("inter_area_prefix", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaPrefix), "inter-area-router" : ("inter_area_router", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter), "intra-area-prefix" : ("intra_area_prefix", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix), "link" : ("link", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link), "network" : ("network", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network), "nssa" : ("nssa", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa), "router" : ("router", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router)}
                                                self._child_list_classes = {}

                                                self.as_external = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal()
                                                self.as_external.parent = self
                                                self._children_name_map["as_external"] = "as-external"
                                                self._children_yang_names.add("as-external")

                                                self.inter_area_prefix = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaPrefix()
                                                self.inter_area_prefix.parent = self
                                                self._children_name_map["inter_area_prefix"] = "inter-area-prefix"
                                                self._children_yang_names.add("inter-area-prefix")

                                                self.inter_area_router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter()
                                                self.inter_area_router.parent = self
                                                self._children_name_map["inter_area_router"] = "inter-area-router"
                                                self._children_yang_names.add("inter-area-router")

                                                self.intra_area_prefix = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix()
                                                self.intra_area_prefix.parent = self
                                                self._children_name_map["intra_area_prefix"] = "intra-area-prefix"
                                                self._children_yang_names.add("intra-area-prefix")

                                                self.link = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link()
                                                self.link.parent = self
                                                self._children_name_map["link"] = "link"
                                                self._children_yang_names.add("link")

                                                self.network = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network()
                                                self.network.parent = self
                                                self._children_name_map["network"] = "network"
                                                self._children_yang_names.add("network")

                                                self.nssa = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa()
                                                self.nssa.parent = self
                                                self._children_name_map["nssa"] = "nssa"
                                                self._children_yang_names.add("nssa")

                                                self.router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router()
                                                self.router.parent = self
                                                self._children_name_map["router"] = "router"
                                                self._children_yang_names.add("router")
                                                self._segment_path = lambda: "body"


                                            class AsExternal(Entity):
                                                """
                                                AS\-External LSA.
                                                
                                                .. attribute:: external_route_tag
                                                
                                                	Route tag
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: flags
                                                
                                                	Flags
                                                	**type**\:   :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal.Flags>`
                                                
                                                .. attribute:: forwarding_address
                                                
                                                	Forwarding address
                                                	**type**\:  str
                                                
                                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: metric
                                                
                                                	Metric
                                                	**type**\:  int
                                                
                                                	**range:** 0..16777215
                                                
                                                .. attribute:: prefix
                                                
                                                	Prefix
                                                	**type**\:  str
                                                
                                                .. attribute:: prefix_options
                                                
                                                	Prefix options
                                                	**type**\:  str
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: referenced_link_state_id
                                                
                                                	Referenced Link State ID
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: referenced_ls_type
                                                
                                                	Referenced Link State type
                                                	**type**\:  int
                                                
                                                	**range:** 0..65535
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal, self).__init__()

                                                    self.yang_name = "as-external"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.external_route_tag = YLeaf(YType.uint32, "external-route-tag")

                                                    self.flags = YLeaf(YType.bits, "flags")

                                                    self.forwarding_address = YLeaf(YType.str, "forwarding-address")

                                                    self.metric = YLeaf(YType.uint32, "metric")

                                                    self.prefix = YLeaf(YType.str, "prefix")

                                                    self.prefix_options = YLeaf(YType.str, "prefix-options")

                                                    self.referenced_link_state_id = YLeaf(YType.uint32, "referenced-link-state-id")

                                                    self.referenced_ls_type = YLeaf(YType.uint16, "referenced-ls-type")
                                                    self._segment_path = lambda: "as-external"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal, ['external_route_tag', 'flags', 'forwarding_address', 'metric', 'prefix', 'prefix_options', 'referenced_link_state_id', 'referenced_ls_type'], name, value)


                                            class InterAreaPrefix(Entity):
                                                """
                                                Inter\-Area\-Prefix LSA.
                                                
                                                .. attribute:: metric
                                                
                                                	Metric
                                                	**type**\:  int
                                                
                                                	**range:** 0..16777215
                                                
                                                .. attribute:: prefix
                                                
                                                	Prefix
                                                	**type**\:  str
                                                
                                                .. attribute:: prefix_options
                                                
                                                	Prefix options
                                                	**type**\:  str
                                                
                                                	**mandatory**\: True
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaPrefix, self).__init__()

                                                    self.yang_name = "inter-area-prefix"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.metric = YLeaf(YType.uint32, "metric")

                                                    self.prefix = YLeaf(YType.str, "prefix")

                                                    self.prefix_options = YLeaf(YType.str, "prefix-options")
                                                    self._segment_path = lambda: "inter-area-prefix"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaPrefix, ['metric', 'prefix', 'prefix_options'], name, value)


                                            class InterAreaRouter(Entity):
                                                """
                                                Inter\-Area\-Router LSA.
                                                
                                                .. attribute:: destination_router_id
                                                
                                                	The Router ID of the router being described by the LSA
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                
                                                .. attribute:: metric
                                                
                                                	Metric
                                                	**type**\:  int
                                                
                                                	**range:** 0..16777215
                                                
                                                .. attribute:: options
                                                
                                                	OSPFv3 LSA options
                                                	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter.Options>`
                                                
                                                	**mandatory**\: True
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter, self).__init__()

                                                    self.yang_name = "inter-area-router"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.destination_router_id = YLeaf(YType.str, "destination-router-id")

                                                    self.metric = YLeaf(YType.uint32, "metric")

                                                    self.options = YLeaf(YType.bits, "options")
                                                    self._segment_path = lambda: "inter-area-router"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter, ['destination_router_id', 'metric', 'options'], name, value)


                                            class IntraAreaPrefix(Entity):
                                                """
                                                Intra\-Area\-Prefix LSA.
                                                
                                                .. attribute:: num_of_prefixes
                                                
                                                	Number of prefixes
                                                	**type**\:  int
                                                
                                                	**range:** 0..65535
                                                
                                                .. attribute:: prefix_list
                                                
                                                	List of prefixes associated with the link
                                                	**type**\: list of    :py:class:`PrefixList <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList>`
                                                
                                                .. attribute:: referenced_adv_router
                                                
                                                	Referenced Advertising Router
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: referenced_link_state_id
                                                
                                                	Referenced Link State ID
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: referenced_ls_type
                                                
                                                	Referenced Link State type
                                                	**type**\:  int
                                                
                                                	**range:** 0..65535
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix, self).__init__()

                                                    self.yang_name = "intra-area-prefix"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {"prefix-list" : ("prefix_list", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList)}

                                                    self.num_of_prefixes = YLeaf(YType.uint16, "num-of-prefixes")

                                                    self.referenced_adv_router = YLeaf(YType.str, "referenced-adv-router")

                                                    self.referenced_link_state_id = YLeaf(YType.uint32, "referenced-link-state-id")

                                                    self.referenced_ls_type = YLeaf(YType.uint16, "referenced-ls-type")

                                                    self.prefix_list = YList(self)
                                                    self._segment_path = lambda: "intra-area-prefix"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix, ['num_of_prefixes', 'referenced_adv_router', 'referenced_link_state_id', 'referenced_ls_type'], name, value)


                                                class PrefixList(Entity):
                                                    """
                                                    List of prefixes associated with the link.
                                                    
                                                    .. attribute:: prefix  <key>
                                                    
                                                    	Prefix
                                                    	**type**\:  str
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..16777215
                                                    
                                                    .. attribute:: prefix_options
                                                    
                                                    	Prefix options
                                                    	**type**\:  str
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList, self).__init__()

                                                        self.yang_name = "prefix-list"
                                                        self.yang_parent_name = "intra-area-prefix"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.prefix = YLeaf(YType.str, "prefix")

                                                        self.metric = YLeaf(YType.uint32, "metric")

                                                        self.prefix_options = YLeaf(YType.str, "prefix-options")
                                                        self._segment_path = lambda: "prefix-list" + "[prefix='" + self.prefix.get() + "']"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList, ['prefix', 'metric', 'prefix_options'], name, value)


                                            class Link(Entity):
                                                """
                                                Link LSA.
                                                
                                                .. attribute:: link_local_interface_address
                                                
                                                	The originating router's link\-local interface address on the link
                                                	**type**\: one of the below types:
                                                
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                
                                                ----
                                                	**type**\:  str
                                                
                                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                
                                                ----
                                                .. attribute:: num_of_prefixes
                                                
                                                	Number of prefixes
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: options
                                                
                                                	OSPFv3 LSA options
                                                	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link.Options>`
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: prefix_list
                                                
                                                	List of prefixes associated with the link
                                                	**type**\: list of    :py:class:`PrefixList <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link.PrefixList>`
                                                
                                                .. attribute:: rtr_priority
                                                
                                                	Router Priority of the interface
                                                	**type**\:  int
                                                
                                                	**range:** 0..255
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link, self).__init__()

                                                    self.yang_name = "link"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {"prefix-list" : ("prefix_list", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link.PrefixList)}

                                                    self.link_local_interface_address = YLeaf(YType.str, "link-local-interface-address")

                                                    self.num_of_prefixes = YLeaf(YType.uint32, "num-of-prefixes")

                                                    self.options = YLeaf(YType.bits, "options")

                                                    self.rtr_priority = YLeaf(YType.uint8, "rtr-priority")

                                                    self.prefix_list = YList(self)
                                                    self._segment_path = lambda: "link"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link, ['link_local_interface_address', 'num_of_prefixes', 'options', 'rtr_priority'], name, value)


                                                class PrefixList(Entity):
                                                    """
                                                    List of prefixes associated with the link.
                                                    
                                                    .. attribute:: prefix  <key>
                                                    
                                                    	Prefix
                                                    	**type**\:  str
                                                    
                                                    .. attribute:: prefix_options
                                                    
                                                    	Prefix options
                                                    	**type**\:  str
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link.PrefixList, self).__init__()

                                                        self.yang_name = "prefix-list"
                                                        self.yang_parent_name = "link"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.prefix = YLeaf(YType.str, "prefix")

                                                        self.prefix_options = YLeaf(YType.str, "prefix-options")
                                                        self._segment_path = lambda: "prefix-list" + "[prefix='" + self.prefix.get() + "']"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link.PrefixList, ['prefix', 'prefix_options'], name, value)


                                            class Network(Entity):
                                                """
                                                Network LSA.
                                                
                                                .. attribute:: attached_router
                                                
                                                	List of the routers attached to the network
                                                	**type**\:  list of str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                
                                                .. attribute:: options
                                                
                                                	OSPFv3 LSA options
                                                	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network.Options>`
                                                
                                                	**mandatory**\: True
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network, self).__init__()

                                                    self.yang_name = "network"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.attached_router = YLeafList(YType.str, "attached-router")

                                                    self.options = YLeaf(YType.bits, "options")
                                                    self._segment_path = lambda: "network"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network, ['attached_router', 'options'], name, value)


                                            class Nssa(Entity):
                                                """
                                                NSSA LSA.
                                                
                                                .. attribute:: external_route_tag
                                                
                                                	Route tag
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: flags
                                                
                                                	Flags
                                                	**type**\:   :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa.Flags>`
                                                
                                                .. attribute:: forwarding_address
                                                
                                                	Forwarding address
                                                	**type**\:  str
                                                
                                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: metric
                                                
                                                	Metric
                                                	**type**\:  int
                                                
                                                	**range:** 0..16777215
                                                
                                                .. attribute:: prefix
                                                
                                                	Prefix
                                                	**type**\:  str
                                                
                                                .. attribute:: prefix_options
                                                
                                                	Prefix options
                                                	**type**\:  str
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: referenced_link_state_id
                                                
                                                	Referenced Link State ID
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: referenced_ls_type
                                                
                                                	Referenced Link State type
                                                	**type**\:  int
                                                
                                                	**range:** 0..65535
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa, self).__init__()

                                                    self.yang_name = "nssa"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.external_route_tag = YLeaf(YType.uint32, "external-route-tag")

                                                    self.flags = YLeaf(YType.bits, "flags")

                                                    self.forwarding_address = YLeaf(YType.str, "forwarding-address")

                                                    self.metric = YLeaf(YType.uint32, "metric")

                                                    self.prefix = YLeaf(YType.str, "prefix")

                                                    self.prefix_options = YLeaf(YType.str, "prefix-options")

                                                    self.referenced_link_state_id = YLeaf(YType.uint32, "referenced-link-state-id")

                                                    self.referenced_ls_type = YLeaf(YType.uint16, "referenced-ls-type")
                                                    self._segment_path = lambda: "nssa"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa, ['external_route_tag', 'flags', 'forwarding_address', 'metric', 'prefix', 'prefix_options', 'referenced_link_state_id', 'referenced_ls_type'], name, value)


                                            class Router(Entity):
                                                """
                                                Router LSA.
                                                
                                                .. attribute:: flags
                                                
                                                	LSA option
                                                	**type**\:   :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Flags>`
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: link
                                                
                                                	Router LSA link
                                                	**type**\: list of    :py:class:`Link <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Link>`
                                                
                                                .. attribute:: options
                                                
                                                	OSPFv3 LSA options
                                                	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Options>`
                                                
                                                	**mandatory**\: True
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router, self).__init__()

                                                    self.yang_name = "router"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {"link" : ("link", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Link)}

                                                    self.flags = YLeaf(YType.bits, "flags")

                                                    self.options = YLeaf(YType.bits, "options")

                                                    self.link = YList(self)
                                                    self._segment_path = lambda: "router"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router, ['flags', 'options'], name, value)


                                                class Link(Entity):
                                                    """
                                                    Router LSA link.
                                                    
                                                    .. attribute:: interface_id  <key>
                                                    
                                                    	Interface ID
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: neighbor_interface_id  <key>
                                                    
                                                    	Neighbor Interface ID
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: neighbor_router_id  <key>
                                                    
                                                    	Neighbor Router ID
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    .. attribute:: type
                                                    
                                                    	Link type
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Link, self).__init__()

                                                        self.yang_name = "link"
                                                        self.yang_parent_name = "router"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.interface_id = YLeaf(YType.uint32, "interface-id")

                                                        self.neighbor_interface_id = YLeaf(YType.uint32, "neighbor-interface-id")

                                                        self.neighbor_router_id = YLeaf(YType.str, "neighbor-router-id")

                                                        self.metric = YLeaf(YType.uint16, "metric")

                                                        self.type = YLeaf(YType.uint8, "type")
                                                        self._segment_path = lambda: "link" + "[interface-id='" + self.interface_id.get() + "']" + "[neighbor-interface-id='" + self.neighbor_interface_id.get() + "']" + "[neighbor-router-id='" + self.neighbor_router_id.get() + "']"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Link, ['interface_id', 'neighbor_interface_id', 'neighbor_router_id', 'metric', 'type'], name, value)


                                        class Header(Entity):
                                            """
                                            Decoded OSPFv3 LSA header data.
                                            
                                            .. attribute:: adv_router
                                            
                                            	LSA advertising router
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: age
                                            
                                            	LSA age
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: checksum
                                            
                                            	LSA checksum
                                            	**type**\:  str
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: length
                                            
                                            	LSA length
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: lsa_id
                                            
                                            	LSA ID
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: options
                                            
                                            	OSPFv3 LSA options
                                            	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header.Options>`
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: seq_num
                                            
                                            	LSA sequence number
                                            	**type**\:  str
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: type
                                            
                                            	LSA type
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header, self).__init__()

                                                self.yang_name = "header"
                                                self.yang_parent_name = "ospfv3"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.adv_router = YLeaf(YType.str, "adv-router")

                                                self.age = YLeaf(YType.uint16, "age")

                                                self.checksum = YLeaf(YType.str, "checksum")

                                                self.length = YLeaf(YType.uint16, "length")

                                                self.lsa_id = YLeaf(YType.uint32, "lsa-id")

                                                self.options = YLeaf(YType.bits, "options")

                                                self.seq_num = YLeaf(YType.str, "seq-num")

                                                self.type = YLeaf(YType.uint16, "type")
                                                self._segment_path = lambda: "header"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header, ['adv_router', 'age', 'checksum', 'length', 'lsa_id', 'options', 'seq_num', 'type'], name, value)


                            class Interfaces(Entity):
                                """
                                List of OSPF interfaces.
                                
                                .. attribute:: interface  <key>
                                
                                	Interface
                                	**type**\:  str
                                
                                .. attribute:: authentication
                                
                                	Authentication configuration
                                	**type**\:   :py:class:`Authentication <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication>`
                                
                                .. attribute:: bdr
                                
                                	BDR
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: bfd
                                
                                	Enable/disable bfd
                                	**type**\:  bool
                                
                                .. attribute:: cost
                                
                                	Interface cost
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                .. attribute:: dead_interval
                                
                                	Interval after which a neighbor is declared dead
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: demand_circuit
                                
                                	Enable/Disable demand circuit
                                	**type**\:  bool
                                
                                .. attribute:: dr
                                
                                	DR
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: enable
                                
                                	Enable/disable protocol on the interface
                                	**type**\:  bool
                                
                                	**default value**\: true
                                
                                .. attribute:: fast_reroute
                                
                                	Fast\-reroute configuration
                                	**type**\:   :py:class:`FastReroute <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute>`
                                
                                .. attribute:: hello_interval
                                
                                	Time between hello packets
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: hello_timer
                                
                                	Hello timer
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: milliseconds
                                
                                .. attribute:: link_scope_lsas
                                
                                	List OSPF link scope LSA databases
                                	**type**\: list of    :py:class:`LinkScopeLsas <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas>`
                                
                                .. attribute:: lls
                                
                                	Enable/Disable link\-local signaling (LLS) support
                                	**type**\:  bool
                                
                                .. attribute:: mtu_ignore
                                
                                	Enable/Disable ignoring of MTU in DBD packets
                                	**type**\:  bool
                                
                                .. attribute:: multi_area
                                
                                	Configure ospf multi\-area
                                	**type**\:   :py:class:`MultiArea <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.MultiArea>`
                                
                                .. attribute:: neighbor
                                
                                	List of OSPF neighbors
                                	**type**\: list of    :py:class:`Neighbor <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Neighbor>`
                                
                                .. attribute:: network_type
                                
                                	Network type
                                	**type**\:   :py:class:`NetworkType <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.NetworkType>`
                                
                                .. attribute:: node_flag
                                
                                	Set prefix as a node representative prefix
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: passive
                                
                                	Enable/Disable passive
                                	**type**\:  bool
                                
                                .. attribute:: prefix_suppression
                                
                                	Suppress advertisement of the prefixes
                                	**type**\:  bool
                                
                                .. attribute:: retransmit_interval
                                
                                	Time between retransmitting unacknowledged Link State Advertisements (LSAs)
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: state
                                
                                	Interface state
                                	**type**\:  str
                                
                                .. attribute:: static_neighbors
                                
                                	Static configured neighbors
                                	**type**\:   :py:class:`StaticNeighbors <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors>`
                                
                                .. attribute:: topology
                                
                                	OSPF interface topology
                                	**type**\: list of    :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Topology>`
                                
                                .. attribute:: transmit_delay
                                
                                	Estimated time needed to send link\-state update
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: ttl_security
                                
                                	TTL security check
                                	**type**\:   :py:class:`TtlSecurity <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.TtlSecurity>`
                                
                                .. attribute:: wait_timer
                                
                                	Wait timer
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: milliseconds
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces, self).__init__()

                                    self.yang_name = "interfaces"
                                    self.yang_parent_name = "area"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"authentication" : ("authentication", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication), "fast-reroute" : ("fast_reroute", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute), "multi-area" : ("multi_area", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.MultiArea), "static-neighbors" : ("static_neighbors", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors), "ttl-security" : ("ttl_security", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.TtlSecurity)}
                                    self._child_list_classes = {"link-scope-lsas" : ("link_scope_lsas", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas), "neighbor" : ("neighbor", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Neighbor), "topology" : ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Topology)}

                                    self.interface = YLeaf(YType.str, "interface")

                                    self.bdr = YLeaf(YType.str, "bdr")

                                    self.bfd = YLeaf(YType.boolean, "bfd")

                                    self.cost = YLeaf(YType.uint16, "cost")

                                    self.dead_interval = YLeaf(YType.uint16, "dead-interval")

                                    self.demand_circuit = YLeaf(YType.boolean, "demand-circuit")

                                    self.dr = YLeaf(YType.str, "dr")

                                    self.enable = YLeaf(YType.boolean, "enable")

                                    self.hello_interval = YLeaf(YType.uint16, "hello-interval")

                                    self.hello_timer = YLeaf(YType.uint32, "hello-timer")

                                    self.lls = YLeaf(YType.boolean, "lls")

                                    self.mtu_ignore = YLeaf(YType.boolean, "mtu-ignore")

                                    self.network_type = YLeaf(YType.enumeration, "network-type")

                                    self.node_flag = YLeaf(YType.boolean, "node-flag")

                                    self.passive = YLeaf(YType.boolean, "passive")

                                    self.prefix_suppression = YLeaf(YType.boolean, "prefix-suppression")

                                    self.retransmit_interval = YLeaf(YType.uint16, "retransmit-interval")

                                    self.state = YLeaf(YType.str, "state")

                                    self.transmit_delay = YLeaf(YType.uint16, "transmit-delay")

                                    self.wait_timer = YLeaf(YType.uint32, "wait-timer")

                                    self.authentication = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication()
                                    self.authentication.parent = self
                                    self._children_name_map["authentication"] = "authentication"
                                    self._children_yang_names.add("authentication")

                                    self.fast_reroute = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute()
                                    self.fast_reroute.parent = self
                                    self._children_name_map["fast_reroute"] = "fast-reroute"
                                    self._children_yang_names.add("fast-reroute")

                                    self.multi_area = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.MultiArea()
                                    self.multi_area.parent = self
                                    self._children_name_map["multi_area"] = "multi-area"
                                    self._children_yang_names.add("multi-area")

                                    self.static_neighbors = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors()
                                    self.static_neighbors.parent = self
                                    self._children_name_map["static_neighbors"] = "static-neighbors"
                                    self._children_yang_names.add("static-neighbors")

                                    self.ttl_security = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.TtlSecurity()
                                    self.ttl_security.parent = self
                                    self._children_name_map["ttl_security"] = "ttl-security"
                                    self._children_yang_names.add("ttl-security")

                                    self.link_scope_lsas = YList(self)
                                    self.neighbor = YList(self)
                                    self.topology = YList(self)
                                    self._segment_path = lambda: "interfaces" + "[interface='" + self.interface.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces, ['interface', 'bdr', 'bfd', 'cost', 'dead_interval', 'demand_circuit', 'dr', 'enable', 'hello_interval', 'hello_timer', 'lls', 'mtu_ignore', 'network_type', 'node_flag', 'passive', 'prefix_suppression', 'retransmit_interval', 'state', 'transmit_delay', 'wait_timer'], name, value)

                                class NetworkType(Enum):
                                    """
                                    NetworkType

                                    Network type.

                                    .. data:: broadcast = 0

                                    	Specify OSPF broadcast multi-access network.

                                    .. data:: non_broadcast = 1

                                    	Specify OSPF Non-Broadcast Multi-Access

                                    	(NBMA) network.

                                    .. data:: point_to_multipoint = 2

                                    	Specify OSPF point-to-multipoint network.

                                    .. data:: point_to_point = 3

                                    	Specify OSPF point-to-point network.

                                    """

                                    broadcast = Enum.YLeaf(0, "broadcast")

                                    non_broadcast = Enum.YLeaf(1, "non-broadcast")

                                    point_to_multipoint = Enum.YLeaf(2, "point-to-multipoint")

                                    point_to_point = Enum.YLeaf(3, "point-to-point")



                                class Authentication(Entity):
                                    """
                                    Authentication configuration.
                                    
                                    .. attribute:: crypto_algorithm
                                    
                                    	Cryptographic algorithm associated with key
                                    	**type**\:   :py:class:`CryptoAlgorithm <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication.CryptoAlgorithm>`
                                    
                                    .. attribute:: key
                                    
                                    	Key string in ASCII format
                                    	**type**\:  str
                                    
                                    .. attribute:: key_chain
                                    
                                    	key\-chain name
                                    	**type**\:  str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_key_chain.KeyChains>`
                                    
                                    .. attribute:: sa
                                    
                                    	SA name
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication, self).__init__()

                                        self.yang_name = "authentication"
                                        self.yang_parent_name = "interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"crypto-algorithm" : ("crypto_algorithm", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication.CryptoAlgorithm)}
                                        self._child_list_classes = {}

                                        self.key = YLeaf(YType.str, "key")

                                        self.key_chain = YLeaf(YType.str, "key-chain")

                                        self.sa = YLeaf(YType.str, "sa")

                                        self.crypto_algorithm = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication.CryptoAlgorithm()
                                        self.crypto_algorithm.parent = self
                                        self._children_name_map["crypto_algorithm"] = "crypto-algorithm"
                                        self._children_yang_names.add("crypto-algorithm")
                                        self._segment_path = lambda: "authentication"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication, ['key', 'key_chain', 'sa'], name, value)


                                    class CryptoAlgorithm(Entity):
                                        """
                                        Cryptographic algorithm associated with key.
                                        
                                        .. attribute:: hmac_sha1_12
                                        
                                        	The HMAC\-SHA1\-12 algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha1_20
                                        
                                        	The HMAC\-SHA1\-20 algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_1
                                        
                                        	HMAC\-SHA\-1 authentication algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_256
                                        
                                        	HMAC\-SHA\-256 authentication algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_384
                                        
                                        	HMAC\-SHA\-384 authentication algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_512
                                        
                                        	HMAC\-SHA\-512 authentication algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: md5
                                        
                                        	The MD5 algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: sha_1
                                        
                                        	The SHA\-1 algorithm
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication.CryptoAlgorithm, self).__init__()

                                            self.yang_name = "crypto-algorithm"
                                            self.yang_parent_name = "authentication"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.hmac_sha1_12 = YLeaf(YType.empty, "hmac-sha1-12")

                                            self.hmac_sha1_20 = YLeaf(YType.empty, "hmac-sha1-20")

                                            self.hmac_sha_1 = YLeaf(YType.empty, "hmac-sha-1")

                                            self.hmac_sha_256 = YLeaf(YType.empty, "hmac-sha-256")

                                            self.hmac_sha_384 = YLeaf(YType.empty, "hmac-sha-384")

                                            self.hmac_sha_512 = YLeaf(YType.empty, "hmac-sha-512")

                                            self.md5 = YLeaf(YType.empty, "md5")

                                            self.sha_1 = YLeaf(YType.empty, "sha-1")
                                            self._segment_path = lambda: "crypto-algorithm"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication.CryptoAlgorithm, ['hmac_sha1_12', 'hmac_sha1_20', 'hmac_sha_1', 'hmac_sha_256', 'hmac_sha_384', 'hmac_sha_512', 'md5', 'sha_1'], name, value)


                                class FastReroute(Entity):
                                    """
                                    Fast\-reroute configuration.
                                    
                                    .. attribute:: lfa
                                    
                                    	LFA configuration
                                    	**type**\:   :py:class:`Lfa <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute, self).__init__()

                                        self.yang_name = "fast-reroute"
                                        self.yang_parent_name = "interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"lfa" : ("lfa", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa)}
                                        self._child_list_classes = {}

                                        self.lfa = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa()
                                        self.lfa.parent = self
                                        self._children_name_map["lfa"] = "lfa"
                                        self._children_yang_names.add("lfa")
                                        self._segment_path = lambda: "fast-reroute"


                                    class Lfa(Entity):
                                        """
                                        LFA configuration.
                                        
                                        .. attribute:: candidate_disabled
                                        
                                        	Prevent the interface to be used as backup
                                        	**type**\:  bool
                                        
                                        .. attribute:: enabled
                                        
                                        	Activates LFA. This model assumes activation of per\-prefix LFA
                                        	**type**\:  bool
                                        
                                        .. attribute:: remote_lfa
                                        
                                        	Remote LFA configuration
                                        	**type**\:   :py:class:`RemoteLfa <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa.RemoteLfa>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa, self).__init__()

                                            self.yang_name = "lfa"
                                            self.yang_parent_name = "fast-reroute"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"remote-lfa" : ("remote_lfa", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa.RemoteLfa)}
                                            self._child_list_classes = {}

                                            self.candidate_disabled = YLeaf(YType.boolean, "candidate-disabled")

                                            self.enabled = YLeaf(YType.boolean, "enabled")

                                            self.remote_lfa = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa.RemoteLfa()
                                            self.remote_lfa.parent = self
                                            self._children_name_map["remote_lfa"] = "remote-lfa"
                                            self._children_yang_names.add("remote-lfa")
                                            self._segment_path = lambda: "lfa"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa, ['candidate_disabled', 'enabled'], name, value)


                                        class RemoteLfa(Entity):
                                            """
                                            Remote LFA configuration.
                                            
                                            .. attribute:: enabled
                                            
                                            	Activates remote LFA
                                            	**type**\:  bool
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa.RemoteLfa, self).__init__()

                                                self.yang_name = "remote-lfa"
                                                self.yang_parent_name = "lfa"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.enabled = YLeaf(YType.boolean, "enabled")
                                                self._segment_path = lambda: "remote-lfa"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa.RemoteLfa, ['enabled'], name, value)


                                class LinkScopeLsas(Entity):
                                    """
                                    List OSPF link scope LSA databases
                                    
                                    .. attribute:: lsa_type  <key>
                                    
                                    	OSPF link scope LSA type
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: link_scope_lsa
                                    
                                    	List of OSPF link scope LSAs
                                    	**type**\: list of    :py:class:`LinkScopeLsa <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas, self).__init__()

                                        self.yang_name = "link-scope-lsas"
                                        self.yang_parent_name = "interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"link-scope-lsa" : ("link_scope_lsa", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa)}

                                        self.lsa_type = YLeaf(YType.uint8, "lsa-type")

                                        self.link_scope_lsa = YList(self)
                                        self._segment_path = lambda: "link-scope-lsas" + "[lsa-type='" + self.lsa_type.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas, ['lsa_type'], name, value)


                                    class LinkScopeLsa(Entity):
                                        """
                                        List of OSPF link scope LSAs
                                        
                                        .. attribute:: lsa_id  <key>
                                        
                                        	LSA ID
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        
                                        ----
                                        .. attribute:: adv_router  <key>
                                        
                                        	Advertising router
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: decoded_completed
                                        
                                        	The OSPF LSA body is fully decoded
                                        	**type**\:  bool
                                        
                                        .. attribute:: ospfv2
                                        
                                        	OSPFv2 LSA
                                        	**type**\:   :py:class:`Ospfv2 <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2>`
                                        
                                        .. attribute:: ospfv3
                                        
                                        	OSPFv3 LSA
                                        	**type**\:   :py:class:`Ospfv3 <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3>`
                                        
                                        .. attribute:: raw_data
                                        
                                        	The complete LSA in network byte order as received/sent over the wire
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa, self).__init__()

                                            self.yang_name = "link-scope-lsa"
                                            self.yang_parent_name = "link-scope-lsas"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"ospfv2" : ("ospfv2", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2), "ospfv3" : ("ospfv3", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3)}
                                            self._child_list_classes = {}

                                            self.lsa_id = YLeaf(YType.str, "lsa-id")

                                            self.adv_router = YLeaf(YType.str, "adv-router")

                                            self.decoded_completed = YLeaf(YType.boolean, "decoded-completed")

                                            self.raw_data = YLeaf(YType.str, "raw-data")

                                            self.ospfv2 = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2()
                                            self.ospfv2.parent = self
                                            self._children_name_map["ospfv2"] = "ospfv2"
                                            self._children_yang_names.add("ospfv2")

                                            self.ospfv3 = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3()
                                            self.ospfv3.parent = self
                                            self._children_name_map["ospfv3"] = "ospfv3"
                                            self._children_yang_names.add("ospfv3")
                                            self._segment_path = lambda: "link-scope-lsa" + "[lsa-id='" + self.lsa_id.get() + "']" + "[adv-router='" + self.adv_router.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa, ['lsa_id', 'adv_router', 'decoded_completed', 'raw_data'], name, value)


                                        class Ospfv2(Entity):
                                            """
                                            OSPFv2 LSA
                                            
                                            .. attribute:: body
                                            
                                            	Decoded OSPFv2 LSA body data
                                            	**type**\:   :py:class:`Body <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body>`
                                            
                                            .. attribute:: header
                                            
                                            	Decoded OSPFv2 LSA header data
                                            	**type**\:   :py:class:`Header <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header>`
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2, self).__init__()

                                                self.yang_name = "ospfv2"
                                                self.yang_parent_name = "link-scope-lsa"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {"body" : ("body", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body), "header" : ("header", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header)}
                                                self._child_list_classes = {}

                                                self.body = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body()
                                                self.body.parent = self
                                                self._children_name_map["body"] = "body"
                                                self._children_yang_names.add("body")

                                                self.header = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header()
                                                self.header.parent = self
                                                self._children_name_map["header"] = "header"
                                                self._children_yang_names.add("header")
                                                self._segment_path = lambda: "ospfv2"


                                            class Body(Entity):
                                                """
                                                Decoded OSPFv2 LSA body data.
                                                
                                                .. attribute:: external
                                                
                                                	External LSA
                                                	**type**\:   :py:class:`External <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External>`
                                                
                                                .. attribute:: network
                                                
                                                	Network LSA
                                                	**type**\:   :py:class:`Network <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Network>`
                                                
                                                .. attribute:: opaque
                                                
                                                	Opaque LSA
                                                	**type**\:   :py:class:`Opaque <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque>`
                                                
                                                .. attribute:: router
                                                
                                                	Router LSA
                                                	**type**\:   :py:class:`Router <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router>`
                                                
                                                .. attribute:: summary
                                                
                                                	Summary LSA
                                                	**type**\:   :py:class:`Summary <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary>`
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body, self).__init__()

                                                    self.yang_name = "body"
                                                    self.yang_parent_name = "ospfv2"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {"external" : ("external", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External), "network" : ("network", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Network), "opaque" : ("opaque", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque), "router" : ("router", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router), "summary" : ("summary", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary)}
                                                    self._child_list_classes = {}

                                                    self.external = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External()
                                                    self.external.parent = self
                                                    self._children_name_map["external"] = "external"
                                                    self._children_yang_names.add("external")

                                                    self.network = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Network()
                                                    self.network.parent = self
                                                    self._children_name_map["network"] = "network"
                                                    self._children_yang_names.add("network")

                                                    self.opaque = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque()
                                                    self.opaque.parent = self
                                                    self._children_name_map["opaque"] = "opaque"
                                                    self._children_yang_names.add("opaque")

                                                    self.router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router()
                                                    self.router.parent = self
                                                    self._children_name_map["router"] = "router"
                                                    self._children_yang_names.add("router")

                                                    self.summary = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary()
                                                    self.summary.parent = self
                                                    self._children_name_map["summary"] = "summary"
                                                    self._children_yang_names.add("summary")
                                                    self._segment_path = lambda: "body"


                                                class External(Entity):
                                                    """
                                                    External LSA.
                                                    
                                                    .. attribute:: network_mask
                                                    
                                                    	The IP address mask for the network
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: topology
                                                    
                                                    	Topology specific information
                                                    	**type**\: list of    :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External.Topology>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External, self).__init__()

                                                        self.yang_name = "external"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {"topology" : ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External.Topology)}

                                                        self.network_mask = YLeaf(YType.str, "network-mask")

                                                        self.topology = YList(self)
                                                        self._segment_path = lambda: "external"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External, ['network_mask'], name, value)


                                                    class Topology(Entity):
                                                        """
                                                        Topology specific information.
                                                        
                                                        .. attribute:: mt_id  <key>
                                                        
                                                        	The MT\-ID for topology enabled on the link
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: external_route_tag
                                                        
                                                        	Route tag
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: flags
                                                        
                                                        	Flags
                                                        	**type**\:   :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External.Topology.Flags>`
                                                        
                                                        .. attribute:: forwarding_address
                                                        
                                                        	Forwarding address
                                                        	**type**\:  str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        .. attribute:: metric
                                                        
                                                        	Metric for the topology
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..16777215
                                                        
                                                        

                                                        """

                                                        _prefix = 'ospf'
                                                        _revision = '2015-03-09'

                                                        def __init__(self):
                                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External.Topology, self).__init__()

                                                            self.yang_name = "topology"
                                                            self.yang_parent_name = "external"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {}
                                                            self._child_list_classes = {}

                                                            self.mt_id = YLeaf(YType.uint8, "mt-id")

                                                            self.external_route_tag = YLeaf(YType.uint32, "external-route-tag")

                                                            self.flags = YLeaf(YType.bits, "flags")

                                                            self.forwarding_address = YLeaf(YType.str, "forwarding-address")

                                                            self.metric = YLeaf(YType.uint32, "metric")
                                                            self._segment_path = lambda: "topology" + "[mt-id='" + self.mt_id.get() + "']"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External.Topology, ['mt_id', 'external_route_tag', 'flags', 'forwarding_address', 'metric'], name, value)


                                                class Network(Entity):
                                                    """
                                                    Network LSA.
                                                    
                                                    .. attribute:: attached_router
                                                    
                                                    	List of the routers attached to the network
                                                    	**type**\:  list of str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                    
                                                    .. attribute:: network_mask
                                                    
                                                    	The IP address mask for the network
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Network, self).__init__()

                                                        self.yang_name = "network"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.attached_router = YLeafList(YType.str, "attached-router")

                                                        self.network_mask = YLeaf(YType.str, "network-mask")
                                                        self._segment_path = lambda: "network"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Network, ['attached_router', 'network_mask'], name, value)


                                                class Opaque(Entity):
                                                    """
                                                    Opaque LSA.
                                                    
                                                    .. attribute:: link_tlv
                                                    
                                                    	Link TLV
                                                    	**type**\:   :py:class:`LinkTlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv>`
                                                    
                                                    .. attribute:: router_address_tlv
                                                    
                                                    	Router address TLV
                                                    	**type**\:   :py:class:`RouterAddressTlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv>`
                                                    
                                                    .. attribute:: unknown_tlv
                                                    
                                                    	Unknown TLV
                                                    	**type**\: list of    :py:class:`UnknownTlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.UnknownTlv>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque, self).__init__()

                                                        self.yang_name = "opaque"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {"link-tlv" : ("link_tlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv), "router-address-tlv" : ("router_address_tlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv)}
                                                        self._child_list_classes = {"unknown-tlv" : ("unknown_tlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.UnknownTlv)}

                                                        self.link_tlv = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv()
                                                        self.link_tlv.parent = self
                                                        self._children_name_map["link_tlv"] = "link-tlv"
                                                        self._children_yang_names.add("link-tlv")

                                                        self.router_address_tlv = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv()
                                                        self.router_address_tlv.parent = self
                                                        self._children_name_map["router_address_tlv"] = "router-address-tlv"
                                                        self._children_yang_names.add("router-address-tlv")

                                                        self.unknown_tlv = YList(self)
                                                        self._segment_path = lambda: "opaque"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque, [], name, value)


                                                    class LinkTlv(Entity):
                                                        """
                                                        Link TLV.
                                                        
                                                        .. attribute:: admin_group
                                                        
                                                        	Administrative group/Resource class/Color
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: link_id
                                                        
                                                        	Link ID
                                                        	**type**\: one of the below types:
                                                        
                                                        	**type**\:  str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        	**mandatory**\: True
                                                        
                                                        
                                                        ----
                                                        	**type**\:  str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                        
                                                        	**mandatory**\: True
                                                        
                                                        
                                                        ----
                                                        .. attribute:: link_type
                                                        
                                                        	Link type
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..255
                                                        
                                                        	**mandatory**\: True
                                                        
                                                        .. attribute:: local_if_ipv4_addr
                                                        
                                                        	List of local interface IPv4 addresses
                                                        	**type**\:  list of str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        .. attribute:: local_remote_ipv4_addr
                                                        
                                                        	List of remote interface IPv4 addresses
                                                        	**type**\:  list of str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        .. attribute:: max_bandwidth
                                                        
                                                        	Maximum bandwidth
                                                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                                                        
                                                        	**range:** \-92233720368547758.08..92233720368547758.07
                                                        
                                                        .. attribute:: max_reservable_bandwidth
                                                        
                                                        	Maximum reservable bandwidth
                                                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                                                        
                                                        	**range:** \-92233720368547758.08..92233720368547758.07
                                                        
                                                        .. attribute:: te_metric
                                                        
                                                        	TE metric
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: unknown_subtlv
                                                        
                                                        	Unknown sub\-TLV
                                                        	**type**\: list of    :py:class:`UnknownSubtlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv>`
                                                        
                                                        .. attribute:: unreserved_bandwidth
                                                        
                                                        	Unreserved bandwidth
                                                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                                                        
                                                        	**range:** \-92233720368547758.08..92233720368547758.07
                                                        
                                                        

                                                        """

                                                        _prefix = 'ospf'
                                                        _revision = '2015-03-09'

                                                        def __init__(self):
                                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv, self).__init__()

                                                            self.yang_name = "link-tlv"
                                                            self.yang_parent_name = "opaque"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {}
                                                            self._child_list_classes = {"unknown-subtlv" : ("unknown_subtlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv)}

                                                            self.admin_group = YLeaf(YType.uint32, "admin-group")

                                                            self.link_id = YLeaf(YType.str, "link-id")

                                                            self.link_type = YLeaf(YType.uint8, "link-type")

                                                            self.local_if_ipv4_addr = YLeafList(YType.str, "local-if-ipv4-addr")

                                                            self.local_remote_ipv4_addr = YLeafList(YType.str, "local-remote-ipv4-addr")

                                                            self.max_bandwidth = YLeaf(YType.str, "max-bandwidth")

                                                            self.max_reservable_bandwidth = YLeaf(YType.str, "max-reservable-bandwidth")

                                                            self.te_metric = YLeaf(YType.uint32, "te-metric")

                                                            self.unreserved_bandwidth = YLeaf(YType.str, "unreserved-bandwidth")

                                                            self.unknown_subtlv = YList(self)
                                                            self._segment_path = lambda: "link-tlv"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv, ['admin_group', 'link_id', 'link_type', 'local_if_ipv4_addr', 'local_remote_ipv4_addr', 'max_bandwidth', 'max_reservable_bandwidth', 'te_metric', 'unreserved_bandwidth'], name, value)


                                                        class UnknownSubtlv(Entity):
                                                            """
                                                            Unknown sub\-TLV.
                                                            
                                                            .. attribute:: type  <key>
                                                            
                                                            	TLV type
                                                            	**type**\:  int
                                                            
                                                            	**range:** 0..65535
                                                            
                                                            .. attribute:: length
                                                            
                                                            	TLV length
                                                            	**type**\:  int
                                                            
                                                            	**range:** 0..65535
                                                            
                                                            .. attribute:: value
                                                            
                                                            	TLV value
                                                            	**type**\:  str
                                                            
                                                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                                            
                                                            

                                                            """

                                                            _prefix = 'ospf'
                                                            _revision = '2015-03-09'

                                                            def __init__(self):
                                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv, self).__init__()

                                                                self.yang_name = "unknown-subtlv"
                                                                self.yang_parent_name = "link-tlv"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self._child_container_classes = {}
                                                                self._child_list_classes = {}

                                                                self.type = YLeaf(YType.uint16, "type")

                                                                self.length = YLeaf(YType.uint16, "length")

                                                                self.value = YLeaf(YType.str, "value")
                                                                self._segment_path = lambda: "unknown-subtlv" + "[type='" + self.type.get() + "']"

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv, ['type', 'length', 'value'], name, value)


                                                    class RouterAddressTlv(Entity):
                                                        """
                                                        Router address TLV.
                                                        
                                                        .. attribute:: router_address
                                                        
                                                        	Router address
                                                        	**type**\:  str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        

                                                        """

                                                        _prefix = 'ospf'
                                                        _revision = '2015-03-09'

                                                        def __init__(self):
                                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv, self).__init__()

                                                            self.yang_name = "router-address-tlv"
                                                            self.yang_parent_name = "opaque"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {}
                                                            self._child_list_classes = {}

                                                            self.router_address = YLeaf(YType.str, "router-address")
                                                            self._segment_path = lambda: "router-address-tlv"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv, ['router_address'], name, value)


                                                    class UnknownTlv(Entity):
                                                        """
                                                        Unknown TLV.
                                                        
                                                        .. attribute:: type  <key>
                                                        
                                                        	TLV type
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..65535
                                                        
                                                        .. attribute:: length
                                                        
                                                        	TLV length
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..65535
                                                        
                                                        .. attribute:: value
                                                        
                                                        	TLV value
                                                        	**type**\:  str
                                                        
                                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                                        
                                                        

                                                        """

                                                        _prefix = 'ospf'
                                                        _revision = '2015-03-09'

                                                        def __init__(self):
                                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.UnknownTlv, self).__init__()

                                                            self.yang_name = "unknown-tlv"
                                                            self.yang_parent_name = "opaque"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {}
                                                            self._child_list_classes = {}

                                                            self.type = YLeaf(YType.uint16, "type")

                                                            self.length = YLeaf(YType.uint16, "length")

                                                            self.value = YLeaf(YType.str, "value")
                                                            self._segment_path = lambda: "unknown-tlv" + "[type='" + self.type.get() + "']"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.UnknownTlv, ['type', 'length', 'value'], name, value)


                                                class Router(Entity):
                                                    """
                                                    Router LSA.
                                                    
                                                    .. attribute:: flags
                                                    
                                                    	Flags
                                                    	**type**\:   :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Flags>`
                                                    
                                                    .. attribute:: link
                                                    
                                                    	Router LSA link
                                                    	**type**\: list of    :py:class:`Link <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link>`
                                                    
                                                    .. attribute:: num_of_links
                                                    
                                                    	Number of links
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router, self).__init__()

                                                        self.yang_name = "router"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {"link" : ("link", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link)}

                                                        self.flags = YLeaf(YType.bits, "flags")

                                                        self.num_of_links = YLeaf(YType.uint16, "num-of-links")

                                                        self.link = YList(self)
                                                        self._segment_path = lambda: "router"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router, ['flags', 'num_of_links'], name, value)


                                                    class Link(Entity):
                                                        """
                                                        Router LSA link.
                                                        
                                                        .. attribute:: link_id  <key>
                                                        
                                                        	Link ID
                                                        	**type**\: one of the below types:
                                                        
                                                        	**type**\:  str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        
                                                        ----
                                                        	**type**\:  str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                        
                                                        
                                                        ----
                                                        .. attribute:: link_data  <key>
                                                        
                                                        	Link data
                                                        	**type**\: one of the below types:
                                                        
                                                        	**type**\:  str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        
                                                        ----
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        
                                                        ----
                                                        .. attribute:: topology
                                                        
                                                        	Topology specific information
                                                        	**type**\: list of    :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link.Topology>`
                                                        
                                                        .. attribute:: type
                                                        
                                                        	Link type
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..255
                                                        
                                                        

                                                        """

                                                        _prefix = 'ospf'
                                                        _revision = '2015-03-09'

                                                        def __init__(self):
                                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link, self).__init__()

                                                            self.yang_name = "link"
                                                            self.yang_parent_name = "router"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {}
                                                            self._child_list_classes = {"topology" : ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link.Topology)}

                                                            self.link_id = YLeaf(YType.str, "link-id")

                                                            self.link_data = YLeaf(YType.str, "link-data")

                                                            self.type = YLeaf(YType.uint8, "type")

                                                            self.topology = YList(self)
                                                            self._segment_path = lambda: "link" + "[link-id='" + self.link_id.get() + "']" + "[link-data='" + self.link_data.get() + "']"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link, ['link_id', 'link_data', 'type'], name, value)


                                                        class Topology(Entity):
                                                            """
                                                            Topology specific information.
                                                            
                                                            .. attribute:: mt_id  <key>
                                                            
                                                            	The MT\-ID for topology enabled on the link
                                                            	**type**\:  int
                                                            
                                                            	**range:** 0..255
                                                            
                                                            .. attribute:: metric
                                                            
                                                            	Metric for the topology
                                                            	**type**\:  int
                                                            
                                                            	**range:** 0..65535
                                                            
                                                            

                                                            """

                                                            _prefix = 'ospf'
                                                            _revision = '2015-03-09'

                                                            def __init__(self):
                                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link.Topology, self).__init__()

                                                                self.yang_name = "topology"
                                                                self.yang_parent_name = "link"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self._child_container_classes = {}
                                                                self._child_list_classes = {}

                                                                self.mt_id = YLeaf(YType.uint8, "mt-id")

                                                                self.metric = YLeaf(YType.uint16, "metric")
                                                                self._segment_path = lambda: "topology" + "[mt-id='" + self.mt_id.get() + "']"

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link.Topology, ['mt_id', 'metric'], name, value)


                                                class Summary(Entity):
                                                    """
                                                    Summary LSA.
                                                    
                                                    .. attribute:: network_mask
                                                    
                                                    	The IP address mask for the network
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: topology
                                                    
                                                    	Topology specific information
                                                    	**type**\: list of    :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary.Topology>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary, self).__init__()

                                                        self.yang_name = "summary"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {"topology" : ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary.Topology)}

                                                        self.network_mask = YLeaf(YType.str, "network-mask")

                                                        self.topology = YList(self)
                                                        self._segment_path = lambda: "summary"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary, ['network_mask'], name, value)


                                                    class Topology(Entity):
                                                        """
                                                        Topology specific information.
                                                        
                                                        .. attribute:: mt_id  <key>
                                                        
                                                        	The MT\-ID for topology enabled on the link
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: metric
                                                        
                                                        	Metric for the topology
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..16777215
                                                        
                                                        

                                                        """

                                                        _prefix = 'ospf'
                                                        _revision = '2015-03-09'

                                                        def __init__(self):
                                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary.Topology, self).__init__()

                                                            self.yang_name = "topology"
                                                            self.yang_parent_name = "summary"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {}
                                                            self._child_list_classes = {}

                                                            self.mt_id = YLeaf(YType.uint8, "mt-id")

                                                            self.metric = YLeaf(YType.uint32, "metric")
                                                            self._segment_path = lambda: "topology" + "[mt-id='" + self.mt_id.get() + "']"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary.Topology, ['mt_id', 'metric'], name, value)


                                            class Header(Entity):
                                                """
                                                Decoded OSPFv2 LSA header data.
                                                
                                                .. attribute:: adv_router
                                                
                                                	LSA advertising router
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: age
                                                
                                                	LSA age
                                                	**type**\:  int
                                                
                                                	**range:** 0..65535
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: checksum
                                                
                                                	LSA checksum
                                                	**type**\:  str
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: length
                                                
                                                	LSA length
                                                	**type**\:  int
                                                
                                                	**range:** 0..65535
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: lsa_id
                                                
                                                	LSA ID
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: opaque_id
                                                
                                                	Opaque id
                                                	**type**\:  int
                                                
                                                	**range:** 0..16777215
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: opaque_type
                                                
                                                	Opaque type
                                                	**type**\:  int
                                                
                                                	**range:** 0..255
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: options
                                                
                                                	LSA option
                                                	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header.Options>`
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: seq_num
                                                
                                                	LSA sequence number
                                                	**type**\:  str
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: type
                                                
                                                	LSA type
                                                	**type**\:  int
                                                
                                                	**range:** 0..65535
                                                
                                                	**mandatory**\: True
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header, self).__init__()

                                                    self.yang_name = "header"
                                                    self.yang_parent_name = "ospfv2"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.adv_router = YLeaf(YType.str, "adv-router")

                                                    self.age = YLeaf(YType.uint16, "age")

                                                    self.checksum = YLeaf(YType.str, "checksum")

                                                    self.length = YLeaf(YType.uint16, "length")

                                                    self.lsa_id = YLeaf(YType.str, "lsa-id")

                                                    self.opaque_id = YLeaf(YType.uint32, "opaque-id")

                                                    self.opaque_type = YLeaf(YType.uint8, "opaque-type")

                                                    self.options = YLeaf(YType.bits, "options")

                                                    self.seq_num = YLeaf(YType.str, "seq-num")

                                                    self.type = YLeaf(YType.uint16, "type")
                                                    self._segment_path = lambda: "header"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header, ['adv_router', 'age', 'checksum', 'length', 'lsa_id', 'opaque_id', 'opaque_type', 'options', 'seq_num', 'type'], name, value)


                                        class Ospfv3(Entity):
                                            """
                                            OSPFv3 LSA
                                            
                                            .. attribute:: body
                                            
                                            	Decoded OSPF LSA body data
                                            	**type**\:   :py:class:`Body <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body>`
                                            
                                            .. attribute:: header
                                            
                                            	Decoded OSPFv3 LSA header data
                                            	**type**\:   :py:class:`Header <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header>`
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3, self).__init__()

                                                self.yang_name = "ospfv3"
                                                self.yang_parent_name = "link-scope-lsa"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {"body" : ("body", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body), "header" : ("header", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header)}
                                                self._child_list_classes = {}

                                                self.body = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body()
                                                self.body.parent = self
                                                self._children_name_map["body"] = "body"
                                                self._children_yang_names.add("body")

                                                self.header = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header()
                                                self.header.parent = self
                                                self._children_name_map["header"] = "header"
                                                self._children_yang_names.add("header")
                                                self._segment_path = lambda: "ospfv3"


                                            class Body(Entity):
                                                """
                                                Decoded OSPF LSA body data.
                                                
                                                .. attribute:: as_external
                                                
                                                	AS\-External LSA
                                                	**type**\:   :py:class:`AsExternal <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal>`
                                                
                                                .. attribute:: inter_area_prefix
                                                
                                                	Inter\-Area\-Prefix LSA
                                                	**type**\:   :py:class:`InterAreaPrefix <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaPrefix>`
                                                
                                                .. attribute:: inter_area_router
                                                
                                                	Inter\-Area\-Router LSA
                                                	**type**\:   :py:class:`InterAreaRouter <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter>`
                                                
                                                .. attribute:: intra_area_prefix
                                                
                                                	Intra\-Area\-Prefix LSA
                                                	**type**\:   :py:class:`IntraAreaPrefix <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix>`
                                                
                                                .. attribute:: link
                                                
                                                	Link LSA
                                                	**type**\:   :py:class:`Link <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link>`
                                                
                                                .. attribute:: network
                                                
                                                	Network LSA
                                                	**type**\:   :py:class:`Network <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network>`
                                                
                                                .. attribute:: nssa
                                                
                                                	NSSA LSA
                                                	**type**\:   :py:class:`Nssa <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa>`
                                                
                                                .. attribute:: router
                                                
                                                	Router LSA
                                                	**type**\:   :py:class:`Router <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router>`
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body, self).__init__()

                                                    self.yang_name = "body"
                                                    self.yang_parent_name = "ospfv3"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {"as-external" : ("as_external", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal), "inter-area-prefix" : ("inter_area_prefix", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaPrefix), "inter-area-router" : ("inter_area_router", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter), "intra-area-prefix" : ("intra_area_prefix", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix), "link" : ("link", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link), "network" : ("network", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network), "nssa" : ("nssa", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa), "router" : ("router", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router)}
                                                    self._child_list_classes = {}

                                                    self.as_external = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal()
                                                    self.as_external.parent = self
                                                    self._children_name_map["as_external"] = "as-external"
                                                    self._children_yang_names.add("as-external")

                                                    self.inter_area_prefix = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaPrefix()
                                                    self.inter_area_prefix.parent = self
                                                    self._children_name_map["inter_area_prefix"] = "inter-area-prefix"
                                                    self._children_yang_names.add("inter-area-prefix")

                                                    self.inter_area_router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter()
                                                    self.inter_area_router.parent = self
                                                    self._children_name_map["inter_area_router"] = "inter-area-router"
                                                    self._children_yang_names.add("inter-area-router")

                                                    self.intra_area_prefix = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix()
                                                    self.intra_area_prefix.parent = self
                                                    self._children_name_map["intra_area_prefix"] = "intra-area-prefix"
                                                    self._children_yang_names.add("intra-area-prefix")

                                                    self.link = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link()
                                                    self.link.parent = self
                                                    self._children_name_map["link"] = "link"
                                                    self._children_yang_names.add("link")

                                                    self.network = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network()
                                                    self.network.parent = self
                                                    self._children_name_map["network"] = "network"
                                                    self._children_yang_names.add("network")

                                                    self.nssa = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa()
                                                    self.nssa.parent = self
                                                    self._children_name_map["nssa"] = "nssa"
                                                    self._children_yang_names.add("nssa")

                                                    self.router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router()
                                                    self.router.parent = self
                                                    self._children_name_map["router"] = "router"
                                                    self._children_yang_names.add("router")
                                                    self._segment_path = lambda: "body"


                                                class AsExternal(Entity):
                                                    """
                                                    AS\-External LSA.
                                                    
                                                    .. attribute:: external_route_tag
                                                    
                                                    	Route tag
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: flags
                                                    
                                                    	Flags
                                                    	**type**\:   :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal.Flags>`
                                                    
                                                    .. attribute:: forwarding_address
                                                    
                                                    	Forwarding address
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..16777215
                                                    
                                                    .. attribute:: prefix
                                                    
                                                    	Prefix
                                                    	**type**\:  str
                                                    
                                                    .. attribute:: prefix_options
                                                    
                                                    	Prefix options
                                                    	**type**\:  str
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    .. attribute:: referenced_link_state_id
                                                    
                                                    	Referenced Link State ID
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: referenced_ls_type
                                                    
                                                    	Referenced Link State type
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal, self).__init__()

                                                        self.yang_name = "as-external"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.external_route_tag = YLeaf(YType.uint32, "external-route-tag")

                                                        self.flags = YLeaf(YType.bits, "flags")

                                                        self.forwarding_address = YLeaf(YType.str, "forwarding-address")

                                                        self.metric = YLeaf(YType.uint32, "metric")

                                                        self.prefix = YLeaf(YType.str, "prefix")

                                                        self.prefix_options = YLeaf(YType.str, "prefix-options")

                                                        self.referenced_link_state_id = YLeaf(YType.uint32, "referenced-link-state-id")

                                                        self.referenced_ls_type = YLeaf(YType.uint16, "referenced-ls-type")
                                                        self._segment_path = lambda: "as-external"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal, ['external_route_tag', 'flags', 'forwarding_address', 'metric', 'prefix', 'prefix_options', 'referenced_link_state_id', 'referenced_ls_type'], name, value)


                                                class InterAreaPrefix(Entity):
                                                    """
                                                    Inter\-Area\-Prefix LSA.
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..16777215
                                                    
                                                    .. attribute:: prefix
                                                    
                                                    	Prefix
                                                    	**type**\:  str
                                                    
                                                    .. attribute:: prefix_options
                                                    
                                                    	Prefix options
                                                    	**type**\:  str
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaPrefix, self).__init__()

                                                        self.yang_name = "inter-area-prefix"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.metric = YLeaf(YType.uint32, "metric")

                                                        self.prefix = YLeaf(YType.str, "prefix")

                                                        self.prefix_options = YLeaf(YType.str, "prefix-options")
                                                        self._segment_path = lambda: "inter-area-prefix"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaPrefix, ['metric', 'prefix', 'prefix_options'], name, value)


                                                class InterAreaRouter(Entity):
                                                    """
                                                    Inter\-Area\-Router LSA.
                                                    
                                                    .. attribute:: destination_router_id
                                                    
                                                    	The Router ID of the router being described by the LSA
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..16777215
                                                    
                                                    .. attribute:: options
                                                    
                                                    	OSPFv3 LSA options
                                                    	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter.Options>`
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter, self).__init__()

                                                        self.yang_name = "inter-area-router"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.destination_router_id = YLeaf(YType.str, "destination-router-id")

                                                        self.metric = YLeaf(YType.uint32, "metric")

                                                        self.options = YLeaf(YType.bits, "options")
                                                        self._segment_path = lambda: "inter-area-router"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter, ['destination_router_id', 'metric', 'options'], name, value)


                                                class IntraAreaPrefix(Entity):
                                                    """
                                                    Intra\-Area\-Prefix LSA.
                                                    
                                                    .. attribute:: num_of_prefixes
                                                    
                                                    	Number of prefixes
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    .. attribute:: prefix_list
                                                    
                                                    	List of prefixes associated with the link
                                                    	**type**\: list of    :py:class:`PrefixList <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList>`
                                                    
                                                    .. attribute:: referenced_adv_router
                                                    
                                                    	Referenced Advertising Router
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: referenced_link_state_id
                                                    
                                                    	Referenced Link State ID
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: referenced_ls_type
                                                    
                                                    	Referenced Link State type
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix, self).__init__()

                                                        self.yang_name = "intra-area-prefix"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {"prefix-list" : ("prefix_list", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList)}

                                                        self.num_of_prefixes = YLeaf(YType.uint16, "num-of-prefixes")

                                                        self.referenced_adv_router = YLeaf(YType.str, "referenced-adv-router")

                                                        self.referenced_link_state_id = YLeaf(YType.uint32, "referenced-link-state-id")

                                                        self.referenced_ls_type = YLeaf(YType.uint16, "referenced-ls-type")

                                                        self.prefix_list = YList(self)
                                                        self._segment_path = lambda: "intra-area-prefix"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix, ['num_of_prefixes', 'referenced_adv_router', 'referenced_link_state_id', 'referenced_ls_type'], name, value)


                                                    class PrefixList(Entity):
                                                        """
                                                        List of prefixes associated with the link.
                                                        
                                                        .. attribute:: prefix  <key>
                                                        
                                                        	Prefix
                                                        	**type**\:  str
                                                        
                                                        .. attribute:: metric
                                                        
                                                        	Metric
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..16777215
                                                        
                                                        .. attribute:: prefix_options
                                                        
                                                        	Prefix options
                                                        	**type**\:  str
                                                        
                                                        	**mandatory**\: True
                                                        
                                                        

                                                        """

                                                        _prefix = 'ospf'
                                                        _revision = '2015-03-09'

                                                        def __init__(self):
                                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList, self).__init__()

                                                            self.yang_name = "prefix-list"
                                                            self.yang_parent_name = "intra-area-prefix"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {}
                                                            self._child_list_classes = {}

                                                            self.prefix = YLeaf(YType.str, "prefix")

                                                            self.metric = YLeaf(YType.uint32, "metric")

                                                            self.prefix_options = YLeaf(YType.str, "prefix-options")
                                                            self._segment_path = lambda: "prefix-list" + "[prefix='" + self.prefix.get() + "']"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList, ['prefix', 'metric', 'prefix_options'], name, value)


                                                class Link(Entity):
                                                    """
                                                    Link LSA.
                                                    
                                                    .. attribute:: link_local_interface_address
                                                    
                                                    	The originating router's link\-local interface address on the link
                                                    	**type**\: one of the below types:
                                                    
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    
                                                    ----
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                    
                                                    
                                                    ----
                                                    .. attribute:: num_of_prefixes
                                                    
                                                    	Number of prefixes
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: options
                                                    
                                                    	OSPFv3 LSA options
                                                    	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link.Options>`
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    .. attribute:: prefix_list
                                                    
                                                    	List of prefixes associated with the link
                                                    	**type**\: list of    :py:class:`PrefixList <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link.PrefixList>`
                                                    
                                                    .. attribute:: rtr_priority
                                                    
                                                    	Router Priority of the interface
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link, self).__init__()

                                                        self.yang_name = "link"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {"prefix-list" : ("prefix_list", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link.PrefixList)}

                                                        self.link_local_interface_address = YLeaf(YType.str, "link-local-interface-address")

                                                        self.num_of_prefixes = YLeaf(YType.uint32, "num-of-prefixes")

                                                        self.options = YLeaf(YType.bits, "options")

                                                        self.rtr_priority = YLeaf(YType.uint8, "rtr-priority")

                                                        self.prefix_list = YList(self)
                                                        self._segment_path = lambda: "link"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link, ['link_local_interface_address', 'num_of_prefixes', 'options', 'rtr_priority'], name, value)


                                                    class PrefixList(Entity):
                                                        """
                                                        List of prefixes associated with the link.
                                                        
                                                        .. attribute:: prefix  <key>
                                                        
                                                        	Prefix
                                                        	**type**\:  str
                                                        
                                                        .. attribute:: prefix_options
                                                        
                                                        	Prefix options
                                                        	**type**\:  str
                                                        
                                                        	**mandatory**\: True
                                                        
                                                        

                                                        """

                                                        _prefix = 'ospf'
                                                        _revision = '2015-03-09'

                                                        def __init__(self):
                                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link.PrefixList, self).__init__()

                                                            self.yang_name = "prefix-list"
                                                            self.yang_parent_name = "link"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {}
                                                            self._child_list_classes = {}

                                                            self.prefix = YLeaf(YType.str, "prefix")

                                                            self.prefix_options = YLeaf(YType.str, "prefix-options")
                                                            self._segment_path = lambda: "prefix-list" + "[prefix='" + self.prefix.get() + "']"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link.PrefixList, ['prefix', 'prefix_options'], name, value)


                                                class Network(Entity):
                                                    """
                                                    Network LSA.
                                                    
                                                    .. attribute:: attached_router
                                                    
                                                    	List of the routers attached to the network
                                                    	**type**\:  list of str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                    
                                                    .. attribute:: options
                                                    
                                                    	OSPFv3 LSA options
                                                    	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network.Options>`
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network, self).__init__()

                                                        self.yang_name = "network"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.attached_router = YLeafList(YType.str, "attached-router")

                                                        self.options = YLeaf(YType.bits, "options")
                                                        self._segment_path = lambda: "network"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network, ['attached_router', 'options'], name, value)


                                                class Nssa(Entity):
                                                    """
                                                    NSSA LSA.
                                                    
                                                    .. attribute:: external_route_tag
                                                    
                                                    	Route tag
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: flags
                                                    
                                                    	Flags
                                                    	**type**\:   :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa.Flags>`
                                                    
                                                    .. attribute:: forwarding_address
                                                    
                                                    	Forwarding address
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..16777215
                                                    
                                                    .. attribute:: prefix
                                                    
                                                    	Prefix
                                                    	**type**\:  str
                                                    
                                                    .. attribute:: prefix_options
                                                    
                                                    	Prefix options
                                                    	**type**\:  str
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    .. attribute:: referenced_link_state_id
                                                    
                                                    	Referenced Link State ID
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: referenced_ls_type
                                                    
                                                    	Referenced Link State type
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa, self).__init__()

                                                        self.yang_name = "nssa"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.external_route_tag = YLeaf(YType.uint32, "external-route-tag")

                                                        self.flags = YLeaf(YType.bits, "flags")

                                                        self.forwarding_address = YLeaf(YType.str, "forwarding-address")

                                                        self.metric = YLeaf(YType.uint32, "metric")

                                                        self.prefix = YLeaf(YType.str, "prefix")

                                                        self.prefix_options = YLeaf(YType.str, "prefix-options")

                                                        self.referenced_link_state_id = YLeaf(YType.uint32, "referenced-link-state-id")

                                                        self.referenced_ls_type = YLeaf(YType.uint16, "referenced-ls-type")
                                                        self._segment_path = lambda: "nssa"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa, ['external_route_tag', 'flags', 'forwarding_address', 'metric', 'prefix', 'prefix_options', 'referenced_link_state_id', 'referenced_ls_type'], name, value)


                                                class Router(Entity):
                                                    """
                                                    Router LSA.
                                                    
                                                    .. attribute:: flags
                                                    
                                                    	LSA option
                                                    	**type**\:   :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Flags>`
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    .. attribute:: link
                                                    
                                                    	Router LSA link
                                                    	**type**\: list of    :py:class:`Link <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Link>`
                                                    
                                                    .. attribute:: options
                                                    
                                                    	OSPFv3 LSA options
                                                    	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Options>`
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router, self).__init__()

                                                        self.yang_name = "router"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {"link" : ("link", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Link)}

                                                        self.flags = YLeaf(YType.bits, "flags")

                                                        self.options = YLeaf(YType.bits, "options")

                                                        self.link = YList(self)
                                                        self._segment_path = lambda: "router"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router, ['flags', 'options'], name, value)


                                                    class Link(Entity):
                                                        """
                                                        Router LSA link.
                                                        
                                                        .. attribute:: interface_id  <key>
                                                        
                                                        	Interface ID
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: neighbor_interface_id  <key>
                                                        
                                                        	Neighbor Interface ID
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: neighbor_router_id  <key>
                                                        
                                                        	Neighbor Router ID
                                                        	**type**\:  str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                        
                                                        .. attribute:: metric
                                                        
                                                        	Metric
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..65535
                                                        
                                                        .. attribute:: type
                                                        
                                                        	Link type
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..255
                                                        
                                                        

                                                        """

                                                        _prefix = 'ospf'
                                                        _revision = '2015-03-09'

                                                        def __init__(self):
                                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Link, self).__init__()

                                                            self.yang_name = "link"
                                                            self.yang_parent_name = "router"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {}
                                                            self._child_list_classes = {}

                                                            self.interface_id = YLeaf(YType.uint32, "interface-id")

                                                            self.neighbor_interface_id = YLeaf(YType.uint32, "neighbor-interface-id")

                                                            self.neighbor_router_id = YLeaf(YType.str, "neighbor-router-id")

                                                            self.metric = YLeaf(YType.uint16, "metric")

                                                            self.type = YLeaf(YType.uint8, "type")
                                                            self._segment_path = lambda: "link" + "[interface-id='" + self.interface_id.get() + "']" + "[neighbor-interface-id='" + self.neighbor_interface_id.get() + "']" + "[neighbor-router-id='" + self.neighbor_router_id.get() + "']"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Link, ['interface_id', 'neighbor_interface_id', 'neighbor_router_id', 'metric', 'type'], name, value)


                                            class Header(Entity):
                                                """
                                                Decoded OSPFv3 LSA header data.
                                                
                                                .. attribute:: adv_router
                                                
                                                	LSA advertising router
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: age
                                                
                                                	LSA age
                                                	**type**\:  int
                                                
                                                	**range:** 0..65535
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: checksum
                                                
                                                	LSA checksum
                                                	**type**\:  str
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: length
                                                
                                                	LSA length
                                                	**type**\:  int
                                                
                                                	**range:** 0..65535
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: lsa_id
                                                
                                                	LSA ID
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: options
                                                
                                                	OSPFv3 LSA options
                                                	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header.Options>`
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: seq_num
                                                
                                                	LSA sequence number
                                                	**type**\:  str
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: type
                                                
                                                	LSA type
                                                	**type**\:  int
                                                
                                                	**range:** 0..65535
                                                
                                                	**mandatory**\: True
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header, self).__init__()

                                                    self.yang_name = "header"
                                                    self.yang_parent_name = "ospfv3"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.adv_router = YLeaf(YType.str, "adv-router")

                                                    self.age = YLeaf(YType.uint16, "age")

                                                    self.checksum = YLeaf(YType.str, "checksum")

                                                    self.length = YLeaf(YType.uint16, "length")

                                                    self.lsa_id = YLeaf(YType.uint32, "lsa-id")

                                                    self.options = YLeaf(YType.bits, "options")

                                                    self.seq_num = YLeaf(YType.str, "seq-num")

                                                    self.type = YLeaf(YType.uint16, "type")
                                                    self._segment_path = lambda: "header"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header, ['adv_router', 'age', 'checksum', 'length', 'lsa_id', 'options', 'seq_num', 'type'], name, value)


                                class MultiArea(Entity):
                                    """
                                    Configure ospf multi\-area.
                                    
                                    .. attribute:: cost
                                    
                                    	Interface cost for multi\-area
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: multi_area_id
                                    
                                    	Multi\-area ID
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.MultiArea, self).__init__()

                                        self.yang_name = "multi-area"
                                        self.yang_parent_name = "interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.cost = YLeaf(YType.uint16, "cost")

                                        self.multi_area_id = YLeaf(YType.str, "multi-area-id")
                                        self._segment_path = lambda: "multi-area"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.MultiArea, ['cost', 'multi_area_id'], name, value)


                                class Neighbor(Entity):
                                    """
                                    List of OSPF neighbors.
                                    
                                    .. attribute:: neighbor_id  <key>
                                    
                                    	Neighbor ID
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address
                                    
                                    	Neighbor address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: bdr
                                    
                                    	Backup Designated Router
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: dr
                                    
                                    	Designated Router
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: state
                                    
                                    	OSPF neighbor state
                                    	**type**\:   :py:class:`NbrStateType <ydk.models.ietf.ietf_ospf.NbrStateType>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Neighbor, self).__init__()

                                        self.yang_name = "neighbor"
                                        self.yang_parent_name = "interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.neighbor_id = YLeaf(YType.str, "neighbor-id")

                                        self.address = YLeaf(YType.str, "address")

                                        self.bdr = YLeaf(YType.str, "bdr")

                                        self.dr = YLeaf(YType.str, "dr")

                                        self.state = YLeaf(YType.enumeration, "state")
                                        self._segment_path = lambda: "neighbor" + "[neighbor-id='" + self.neighbor_id.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Neighbor, ['neighbor_id', 'address', 'bdr', 'dr', 'state'], name, value)


                                class StaticNeighbors(Entity):
                                    """
                                    Static configured neighbors.
                                    
                                    .. attribute:: neighbor
                                    
                                    	Specify a neighbor router
                                    	**type**\: list of    :py:class:`Neighbor <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors.Neighbor>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors, self).__init__()

                                        self.yang_name = "static-neighbors"
                                        self.yang_parent_name = "interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"neighbor" : ("neighbor", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors.Neighbor)}

                                        self.neighbor = YList(self)
                                        self._segment_path = lambda: "static-neighbors"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors, [], name, value)


                                    class Neighbor(Entity):
                                        """
                                        Specify a neighbor router.
                                        
                                        .. attribute:: address  <key>
                                        
                                        	Neighbor IP address
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        	**type**\:  str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        .. attribute:: cost
                                        
                                        	Neighbor cost
                                        	**type**\:  int
                                        
                                        	**range:** 1..65535
                                        
                                        .. attribute:: poll_interval
                                        
                                        	Neighbor poll interval
                                        	**type**\:  int
                                        
                                        	**range:** 1..65535
                                        
                                        	**units**\: seconds
                                        
                                        .. attribute:: priority
                                        
                                        	Neighbor priority for DR election
                                        	**type**\:  int
                                        
                                        	**range:** 1..255
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors.Neighbor, self).__init__()

                                            self.yang_name = "neighbor"
                                            self.yang_parent_name = "static-neighbors"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.address = YLeaf(YType.str, "address")

                                            self.cost = YLeaf(YType.uint16, "cost")

                                            self.poll_interval = YLeaf(YType.uint16, "poll-interval")

                                            self.priority = YLeaf(YType.uint8, "priority")
                                            self._segment_path = lambda: "neighbor" + "[address='" + self.address.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors.Neighbor, ['address', 'cost', 'poll_interval', 'priority'], name, value)


                                class Topology(Entity):
                                    """
                                    OSPF interface topology.
                                    
                                    .. attribute:: name  <key>
                                    
                                    	One of the topology enabled on this interface
                                    	**type**\:  str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.Ribs.Rib>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Topology, self).__init__()

                                        self.yang_name = "topology"
                                        self.yang_parent_name = "interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.name = YLeaf(YType.str, "name")
                                        self._segment_path = lambda: "topology" + "[name='" + self.name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Topology, ['name'], name, value)


                                class TtlSecurity(Entity):
                                    """
                                    TTL security check.
                                    
                                    .. attribute:: enable
                                    
                                    	Enable/Disable TTL security check
                                    	**type**\:  bool
                                    
                                    .. attribute:: hops
                                    
                                    	Maximum number of hops that a OSPF packet may have traveled
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.TtlSecurity, self).__init__()

                                        self.yang_name = "ttl-security"
                                        self.yang_parent_name = "interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.enable = YLeaf(YType.boolean, "enable")

                                        self.hops = YLeaf(YType.uint8, "hops")
                                        self._segment_path = lambda: "ttl-security"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.TtlSecurity, ['enable', 'hops'], name, value)


                        class AsScopeLsas(Entity):
                            """
                            List OSPF AS scope LSA databases
                            
                            .. attribute:: lsa_type  <key>
                            
                            	OSPF AS scope LSA type
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: as_scope_lsa
                            
                            	List of OSPF AS scope LSAs
                            	**type**\: list of    :py:class:`AsScopeLsa <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa>`
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas, self).__init__()

                                self.yang_name = "as-scope-lsas"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"as-scope-lsa" : ("as_scope_lsa", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa)}

                                self.lsa_type = YLeaf(YType.uint8, "lsa-type")

                                self.as_scope_lsa = YList(self)
                                self._segment_path = lambda: "as-scope-lsas" + "[lsa-type='" + self.lsa_type.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas, ['lsa_type'], name, value)


                            class AsScopeLsa(Entity):
                                """
                                List of OSPF AS scope LSAs
                                
                                .. attribute:: lsa_id  <key>
                                
                                	LSA ID
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                
                                ----
                                .. attribute:: adv_router  <key>
                                
                                	Advertising router
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: decoded_completed
                                
                                	The OSPF LSA body is fully decoded
                                	**type**\:  bool
                                
                                .. attribute:: ospfv2
                                
                                	OSPFv2 LSA
                                	**type**\:   :py:class:`Ospfv2 <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2>`
                                
                                .. attribute:: ospfv3
                                
                                	OSPFv3 LSA
                                	**type**\:   :py:class:`Ospfv3 <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3>`
                                
                                .. attribute:: raw_data
                                
                                	The complete LSA in network byte order as received/sent over the wire
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa, self).__init__()

                                    self.yang_name = "as-scope-lsa"
                                    self.yang_parent_name = "as-scope-lsas"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"ospfv2" : ("ospfv2", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2), "ospfv3" : ("ospfv3", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3)}
                                    self._child_list_classes = {}

                                    self.lsa_id = YLeaf(YType.str, "lsa-id")

                                    self.adv_router = YLeaf(YType.str, "adv-router")

                                    self.decoded_completed = YLeaf(YType.boolean, "decoded-completed")

                                    self.raw_data = YLeaf(YType.str, "raw-data")

                                    self.ospfv2 = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2()
                                    self.ospfv2.parent = self
                                    self._children_name_map["ospfv2"] = "ospfv2"
                                    self._children_yang_names.add("ospfv2")

                                    self.ospfv3 = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3()
                                    self.ospfv3.parent = self
                                    self._children_name_map["ospfv3"] = "ospfv3"
                                    self._children_yang_names.add("ospfv3")
                                    self._segment_path = lambda: "as-scope-lsa" + "[lsa-id='" + self.lsa_id.get() + "']" + "[adv-router='" + self.adv_router.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa, ['lsa_id', 'adv_router', 'decoded_completed', 'raw_data'], name, value)


                                class Ospfv2(Entity):
                                    """
                                    OSPFv2 LSA
                                    
                                    .. attribute:: body
                                    
                                    	Decoded OSPFv2 LSA body data
                                    	**type**\:   :py:class:`Body <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body>`
                                    
                                    .. attribute:: header
                                    
                                    	Decoded OSPFv2 LSA header data
                                    	**type**\:   :py:class:`Header <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2, self).__init__()

                                        self.yang_name = "ospfv2"
                                        self.yang_parent_name = "as-scope-lsa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"body" : ("body", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body), "header" : ("header", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header)}
                                        self._child_list_classes = {}

                                        self.body = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body()
                                        self.body.parent = self
                                        self._children_name_map["body"] = "body"
                                        self._children_yang_names.add("body")

                                        self.header = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header()
                                        self.header.parent = self
                                        self._children_name_map["header"] = "header"
                                        self._children_yang_names.add("header")
                                        self._segment_path = lambda: "ospfv2"


                                    class Body(Entity):
                                        """
                                        Decoded OSPFv2 LSA body data.
                                        
                                        .. attribute:: external
                                        
                                        	External LSA
                                        	**type**\:   :py:class:`External <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External>`
                                        
                                        .. attribute:: network
                                        
                                        	Network LSA
                                        	**type**\:   :py:class:`Network <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Network>`
                                        
                                        .. attribute:: opaque
                                        
                                        	Opaque LSA
                                        	**type**\:   :py:class:`Opaque <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque>`
                                        
                                        .. attribute:: router
                                        
                                        	Router LSA
                                        	**type**\:   :py:class:`Router <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router>`
                                        
                                        .. attribute:: summary
                                        
                                        	Summary LSA
                                        	**type**\:   :py:class:`Summary <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body, self).__init__()

                                            self.yang_name = "body"
                                            self.yang_parent_name = "ospfv2"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"external" : ("external", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External), "network" : ("network", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Network), "opaque" : ("opaque", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque), "router" : ("router", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router), "summary" : ("summary", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary)}
                                            self._child_list_classes = {}

                                            self.external = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External()
                                            self.external.parent = self
                                            self._children_name_map["external"] = "external"
                                            self._children_yang_names.add("external")

                                            self.network = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Network()
                                            self.network.parent = self
                                            self._children_name_map["network"] = "network"
                                            self._children_yang_names.add("network")

                                            self.opaque = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque()
                                            self.opaque.parent = self
                                            self._children_name_map["opaque"] = "opaque"
                                            self._children_yang_names.add("opaque")

                                            self.router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router()
                                            self.router.parent = self
                                            self._children_name_map["router"] = "router"
                                            self._children_yang_names.add("router")

                                            self.summary = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary()
                                            self.summary.parent = self
                                            self._children_name_map["summary"] = "summary"
                                            self._children_yang_names.add("summary")
                                            self._segment_path = lambda: "body"


                                        class External(Entity):
                                            """
                                            External LSA.
                                            
                                            .. attribute:: network_mask
                                            
                                            	The IP address mask for the network
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: topology
                                            
                                            	Topology specific information
                                            	**type**\: list of    :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External.Topology>`
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External, self).__init__()

                                                self.yang_name = "external"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {"topology" : ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External.Topology)}

                                                self.network_mask = YLeaf(YType.str, "network-mask")

                                                self.topology = YList(self)
                                                self._segment_path = lambda: "external"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External, ['network_mask'], name, value)


                                            class Topology(Entity):
                                                """
                                                Topology specific information.
                                                
                                                .. attribute:: mt_id  <key>
                                                
                                                	The MT\-ID for topology enabled on the link
                                                	**type**\:  int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: external_route_tag
                                                
                                                	Route tag
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: flags
                                                
                                                	Flags
                                                	**type**\:   :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External.Topology.Flags>`
                                                
                                                .. attribute:: forwarding_address
                                                
                                                	Forwarding address
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: metric
                                                
                                                	Metric for the topology
                                                	**type**\:  int
                                                
                                                	**range:** 0..16777215
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External.Topology, self).__init__()

                                                    self.yang_name = "topology"
                                                    self.yang_parent_name = "external"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.mt_id = YLeaf(YType.uint8, "mt-id")

                                                    self.external_route_tag = YLeaf(YType.uint32, "external-route-tag")

                                                    self.flags = YLeaf(YType.bits, "flags")

                                                    self.forwarding_address = YLeaf(YType.str, "forwarding-address")

                                                    self.metric = YLeaf(YType.uint32, "metric")
                                                    self._segment_path = lambda: "topology" + "[mt-id='" + self.mt_id.get() + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External.Topology, ['mt_id', 'external_route_tag', 'flags', 'forwarding_address', 'metric'], name, value)


                                        class Network(Entity):
                                            """
                                            Network LSA.
                                            
                                            .. attribute:: attached_router
                                            
                                            	List of the routers attached to the network
                                            	**type**\:  list of str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                            
                                            .. attribute:: network_mask
                                            
                                            	The IP address mask for the network
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Network, self).__init__()

                                                self.yang_name = "network"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.attached_router = YLeafList(YType.str, "attached-router")

                                                self.network_mask = YLeaf(YType.str, "network-mask")
                                                self._segment_path = lambda: "network"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Network, ['attached_router', 'network_mask'], name, value)


                                        class Opaque(Entity):
                                            """
                                            Opaque LSA.
                                            
                                            .. attribute:: link_tlv
                                            
                                            	Link TLV
                                            	**type**\:   :py:class:`LinkTlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv>`
                                            
                                            .. attribute:: router_address_tlv
                                            
                                            	Router address TLV
                                            	**type**\:   :py:class:`RouterAddressTlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv>`
                                            
                                            .. attribute:: unknown_tlv
                                            
                                            	Unknown TLV
                                            	**type**\: list of    :py:class:`UnknownTlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.UnknownTlv>`
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque, self).__init__()

                                                self.yang_name = "opaque"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {"link-tlv" : ("link_tlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv), "router-address-tlv" : ("router_address_tlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv)}
                                                self._child_list_classes = {"unknown-tlv" : ("unknown_tlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.UnknownTlv)}

                                                self.link_tlv = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv()
                                                self.link_tlv.parent = self
                                                self._children_name_map["link_tlv"] = "link-tlv"
                                                self._children_yang_names.add("link-tlv")

                                                self.router_address_tlv = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv()
                                                self.router_address_tlv.parent = self
                                                self._children_name_map["router_address_tlv"] = "router-address-tlv"
                                                self._children_yang_names.add("router-address-tlv")

                                                self.unknown_tlv = YList(self)
                                                self._segment_path = lambda: "opaque"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque, [], name, value)


                                            class LinkTlv(Entity):
                                                """
                                                Link TLV.
                                                
                                                .. attribute:: admin_group
                                                
                                                	Administrative group/Resource class/Color
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: link_id
                                                
                                                	Link ID
                                                	**type**\: one of the below types:
                                                
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                	**mandatory**\: True
                                                
                                                
                                                ----
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                
                                                	**mandatory**\: True
                                                
                                                
                                                ----
                                                .. attribute:: link_type
                                                
                                                	Link type
                                                	**type**\:  int
                                                
                                                	**range:** 0..255
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: local_if_ipv4_addr
                                                
                                                	List of local interface IPv4 addresses
                                                	**type**\:  list of str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: local_remote_ipv4_addr
                                                
                                                	List of remote interface IPv4 addresses
                                                	**type**\:  list of str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: max_bandwidth
                                                
                                                	Maximum bandwidth
                                                	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                                                
                                                	**range:** \-92233720368547758.08..92233720368547758.07
                                                
                                                .. attribute:: max_reservable_bandwidth
                                                
                                                	Maximum reservable bandwidth
                                                	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                                                
                                                	**range:** \-92233720368547758.08..92233720368547758.07
                                                
                                                .. attribute:: te_metric
                                                
                                                	TE metric
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: unknown_subtlv
                                                
                                                	Unknown sub\-TLV
                                                	**type**\: list of    :py:class:`UnknownSubtlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv>`
                                                
                                                .. attribute:: unreserved_bandwidth
                                                
                                                	Unreserved bandwidth
                                                	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                                                
                                                	**range:** \-92233720368547758.08..92233720368547758.07
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv, self).__init__()

                                                    self.yang_name = "link-tlv"
                                                    self.yang_parent_name = "opaque"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {"unknown-subtlv" : ("unknown_subtlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv)}

                                                    self.admin_group = YLeaf(YType.uint32, "admin-group")

                                                    self.link_id = YLeaf(YType.str, "link-id")

                                                    self.link_type = YLeaf(YType.uint8, "link-type")

                                                    self.local_if_ipv4_addr = YLeafList(YType.str, "local-if-ipv4-addr")

                                                    self.local_remote_ipv4_addr = YLeafList(YType.str, "local-remote-ipv4-addr")

                                                    self.max_bandwidth = YLeaf(YType.str, "max-bandwidth")

                                                    self.max_reservable_bandwidth = YLeaf(YType.str, "max-reservable-bandwidth")

                                                    self.te_metric = YLeaf(YType.uint32, "te-metric")

                                                    self.unreserved_bandwidth = YLeaf(YType.str, "unreserved-bandwidth")

                                                    self.unknown_subtlv = YList(self)
                                                    self._segment_path = lambda: "link-tlv"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv, ['admin_group', 'link_id', 'link_type', 'local_if_ipv4_addr', 'local_remote_ipv4_addr', 'max_bandwidth', 'max_reservable_bandwidth', 'te_metric', 'unreserved_bandwidth'], name, value)


                                                class UnknownSubtlv(Entity):
                                                    """
                                                    Unknown sub\-TLV.
                                                    
                                                    .. attribute:: type  <key>
                                                    
                                                    	TLV type
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    .. attribute:: length
                                                    
                                                    	TLV length
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    .. attribute:: value
                                                    
                                                    	TLV value
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv, self).__init__()

                                                        self.yang_name = "unknown-subtlv"
                                                        self.yang_parent_name = "link-tlv"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.type = YLeaf(YType.uint16, "type")

                                                        self.length = YLeaf(YType.uint16, "length")

                                                        self.value = YLeaf(YType.str, "value")
                                                        self._segment_path = lambda: "unknown-subtlv" + "[type='" + self.type.get() + "']"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv, ['type', 'length', 'value'], name, value)


                                            class RouterAddressTlv(Entity):
                                                """
                                                Router address TLV.
                                                
                                                .. attribute:: router_address
                                                
                                                	Router address
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv, self).__init__()

                                                    self.yang_name = "router-address-tlv"
                                                    self.yang_parent_name = "opaque"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.router_address = YLeaf(YType.str, "router-address")
                                                    self._segment_path = lambda: "router-address-tlv"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv, ['router_address'], name, value)


                                            class UnknownTlv(Entity):
                                                """
                                                Unknown TLV.
                                                
                                                .. attribute:: type  <key>
                                                
                                                	TLV type
                                                	**type**\:  int
                                                
                                                	**range:** 0..65535
                                                
                                                .. attribute:: length
                                                
                                                	TLV length
                                                	**type**\:  int
                                                
                                                	**range:** 0..65535
                                                
                                                .. attribute:: value
                                                
                                                	TLV value
                                                	**type**\:  str
                                                
                                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.UnknownTlv, self).__init__()

                                                    self.yang_name = "unknown-tlv"
                                                    self.yang_parent_name = "opaque"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.type = YLeaf(YType.uint16, "type")

                                                    self.length = YLeaf(YType.uint16, "length")

                                                    self.value = YLeaf(YType.str, "value")
                                                    self._segment_path = lambda: "unknown-tlv" + "[type='" + self.type.get() + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.UnknownTlv, ['type', 'length', 'value'], name, value)


                                        class Router(Entity):
                                            """
                                            Router LSA.
                                            
                                            .. attribute:: flags
                                            
                                            	Flags
                                            	**type**\:   :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Flags>`
                                            
                                            .. attribute:: link
                                            
                                            	Router LSA link
                                            	**type**\: list of    :py:class:`Link <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link>`
                                            
                                            .. attribute:: num_of_links
                                            
                                            	Number of links
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router, self).__init__()

                                                self.yang_name = "router"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {"link" : ("link", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link)}

                                                self.flags = YLeaf(YType.bits, "flags")

                                                self.num_of_links = YLeaf(YType.uint16, "num-of-links")

                                                self.link = YList(self)
                                                self._segment_path = lambda: "router"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router, ['flags', 'num_of_links'], name, value)


                                            class Link(Entity):
                                                """
                                                Router LSA link.
                                                
                                                .. attribute:: link_id  <key>
                                                
                                                	Link ID
                                                	**type**\: one of the below types:
                                                
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                
                                                ----
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                
                                                
                                                ----
                                                .. attribute:: link_data  <key>
                                                
                                                	Link data
                                                	**type**\: one of the below types:
                                                
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                
                                                ----
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                
                                                ----
                                                .. attribute:: topology
                                                
                                                	Topology specific information
                                                	**type**\: list of    :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link.Topology>`
                                                
                                                .. attribute:: type
                                                
                                                	Link type
                                                	**type**\:  int
                                                
                                                	**range:** 0..255
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link, self).__init__()

                                                    self.yang_name = "link"
                                                    self.yang_parent_name = "router"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {"topology" : ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link.Topology)}

                                                    self.link_id = YLeaf(YType.str, "link-id")

                                                    self.link_data = YLeaf(YType.str, "link-data")

                                                    self.type = YLeaf(YType.uint8, "type")

                                                    self.topology = YList(self)
                                                    self._segment_path = lambda: "link" + "[link-id='" + self.link_id.get() + "']" + "[link-data='" + self.link_data.get() + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link, ['link_id', 'link_data', 'type'], name, value)


                                                class Topology(Entity):
                                                    """
                                                    Topology specific information.
                                                    
                                                    .. attribute:: mt_id  <key>
                                                    
                                                    	The MT\-ID for topology enabled on the link
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric for the topology
                                                    	**type**\:  int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link.Topology, self).__init__()

                                                        self.yang_name = "topology"
                                                        self.yang_parent_name = "link"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.mt_id = YLeaf(YType.uint8, "mt-id")

                                                        self.metric = YLeaf(YType.uint16, "metric")
                                                        self._segment_path = lambda: "topology" + "[mt-id='" + self.mt_id.get() + "']"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link.Topology, ['mt_id', 'metric'], name, value)


                                        class Summary(Entity):
                                            """
                                            Summary LSA.
                                            
                                            .. attribute:: network_mask
                                            
                                            	The IP address mask for the network
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: topology
                                            
                                            	Topology specific information
                                            	**type**\: list of    :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary.Topology>`
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary, self).__init__()

                                                self.yang_name = "summary"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {"topology" : ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary.Topology)}

                                                self.network_mask = YLeaf(YType.str, "network-mask")

                                                self.topology = YList(self)
                                                self._segment_path = lambda: "summary"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary, ['network_mask'], name, value)


                                            class Topology(Entity):
                                                """
                                                Topology specific information.
                                                
                                                .. attribute:: mt_id  <key>
                                                
                                                	The MT\-ID for topology enabled on the link
                                                	**type**\:  int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: metric
                                                
                                                	Metric for the topology
                                                	**type**\:  int
                                                
                                                	**range:** 0..16777215
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary.Topology, self).__init__()

                                                    self.yang_name = "topology"
                                                    self.yang_parent_name = "summary"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.mt_id = YLeaf(YType.uint8, "mt-id")

                                                    self.metric = YLeaf(YType.uint32, "metric")
                                                    self._segment_path = lambda: "topology" + "[mt-id='" + self.mt_id.get() + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary.Topology, ['mt_id', 'metric'], name, value)


                                    class Header(Entity):
                                        """
                                        Decoded OSPFv2 LSA header data.
                                        
                                        .. attribute:: adv_router
                                        
                                        	LSA advertising router
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: age
                                        
                                        	LSA age
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: checksum
                                        
                                        	LSA checksum
                                        	**type**\:  str
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: length
                                        
                                        	LSA length
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: lsa_id
                                        
                                        	LSA ID
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: opaque_id
                                        
                                        	Opaque id
                                        	**type**\:  int
                                        
                                        	**range:** 0..16777215
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: opaque_type
                                        
                                        	Opaque type
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: options
                                        
                                        	LSA option
                                        	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header.Options>`
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: seq_num
                                        
                                        	LSA sequence number
                                        	**type**\:  str
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: type
                                        
                                        	LSA type
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header, self).__init__()

                                            self.yang_name = "header"
                                            self.yang_parent_name = "ospfv2"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.adv_router = YLeaf(YType.str, "adv-router")

                                            self.age = YLeaf(YType.uint16, "age")

                                            self.checksum = YLeaf(YType.str, "checksum")

                                            self.length = YLeaf(YType.uint16, "length")

                                            self.lsa_id = YLeaf(YType.str, "lsa-id")

                                            self.opaque_id = YLeaf(YType.uint32, "opaque-id")

                                            self.opaque_type = YLeaf(YType.uint8, "opaque-type")

                                            self.options = YLeaf(YType.bits, "options")

                                            self.seq_num = YLeaf(YType.str, "seq-num")

                                            self.type = YLeaf(YType.uint16, "type")
                                            self._segment_path = lambda: "header"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header, ['adv_router', 'age', 'checksum', 'length', 'lsa_id', 'opaque_id', 'opaque_type', 'options', 'seq_num', 'type'], name, value)


                                class Ospfv3(Entity):
                                    """
                                    OSPFv3 LSA
                                    
                                    .. attribute:: body
                                    
                                    	Decoded OSPF LSA body data
                                    	**type**\:   :py:class:`Body <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body>`
                                    
                                    .. attribute:: header
                                    
                                    	Decoded OSPFv3 LSA header data
                                    	**type**\:   :py:class:`Header <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3, self).__init__()

                                        self.yang_name = "ospfv3"
                                        self.yang_parent_name = "as-scope-lsa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"body" : ("body", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body), "header" : ("header", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header)}
                                        self._child_list_classes = {}

                                        self.body = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body()
                                        self.body.parent = self
                                        self._children_name_map["body"] = "body"
                                        self._children_yang_names.add("body")

                                        self.header = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header()
                                        self.header.parent = self
                                        self._children_name_map["header"] = "header"
                                        self._children_yang_names.add("header")
                                        self._segment_path = lambda: "ospfv3"


                                    class Body(Entity):
                                        """
                                        Decoded OSPF LSA body data.
                                        
                                        .. attribute:: as_external
                                        
                                        	AS\-External LSA
                                        	**type**\:   :py:class:`AsExternal <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal>`
                                        
                                        .. attribute:: inter_area_prefix
                                        
                                        	Inter\-Area\-Prefix LSA
                                        	**type**\:   :py:class:`InterAreaPrefix <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaPrefix>`
                                        
                                        .. attribute:: inter_area_router
                                        
                                        	Inter\-Area\-Router LSA
                                        	**type**\:   :py:class:`InterAreaRouter <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter>`
                                        
                                        .. attribute:: intra_area_prefix
                                        
                                        	Intra\-Area\-Prefix LSA
                                        	**type**\:   :py:class:`IntraAreaPrefix <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix>`
                                        
                                        .. attribute:: link
                                        
                                        	Link LSA
                                        	**type**\:   :py:class:`Link <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link>`
                                        
                                        .. attribute:: network
                                        
                                        	Network LSA
                                        	**type**\:   :py:class:`Network <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network>`
                                        
                                        .. attribute:: nssa
                                        
                                        	NSSA LSA
                                        	**type**\:   :py:class:`Nssa <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa>`
                                        
                                        .. attribute:: router
                                        
                                        	Router LSA
                                        	**type**\:   :py:class:`Router <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body, self).__init__()

                                            self.yang_name = "body"
                                            self.yang_parent_name = "ospfv3"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"as-external" : ("as_external", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal), "inter-area-prefix" : ("inter_area_prefix", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaPrefix), "inter-area-router" : ("inter_area_router", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter), "intra-area-prefix" : ("intra_area_prefix", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix), "link" : ("link", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link), "network" : ("network", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network), "nssa" : ("nssa", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa), "router" : ("router", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router)}
                                            self._child_list_classes = {}

                                            self.as_external = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal()
                                            self.as_external.parent = self
                                            self._children_name_map["as_external"] = "as-external"
                                            self._children_yang_names.add("as-external")

                                            self.inter_area_prefix = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaPrefix()
                                            self.inter_area_prefix.parent = self
                                            self._children_name_map["inter_area_prefix"] = "inter-area-prefix"
                                            self._children_yang_names.add("inter-area-prefix")

                                            self.inter_area_router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter()
                                            self.inter_area_router.parent = self
                                            self._children_name_map["inter_area_router"] = "inter-area-router"
                                            self._children_yang_names.add("inter-area-router")

                                            self.intra_area_prefix = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix()
                                            self.intra_area_prefix.parent = self
                                            self._children_name_map["intra_area_prefix"] = "intra-area-prefix"
                                            self._children_yang_names.add("intra-area-prefix")

                                            self.link = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link()
                                            self.link.parent = self
                                            self._children_name_map["link"] = "link"
                                            self._children_yang_names.add("link")

                                            self.network = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network()
                                            self.network.parent = self
                                            self._children_name_map["network"] = "network"
                                            self._children_yang_names.add("network")

                                            self.nssa = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa()
                                            self.nssa.parent = self
                                            self._children_name_map["nssa"] = "nssa"
                                            self._children_yang_names.add("nssa")

                                            self.router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router()
                                            self.router.parent = self
                                            self._children_name_map["router"] = "router"
                                            self._children_yang_names.add("router")
                                            self._segment_path = lambda: "body"


                                        class AsExternal(Entity):
                                            """
                                            AS\-External LSA.
                                            
                                            .. attribute:: external_route_tag
                                            
                                            	Route tag
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: flags
                                            
                                            	Flags
                                            	**type**\:   :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal.Flags>`
                                            
                                            .. attribute:: forwarding_address
                                            
                                            	Forwarding address
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: metric
                                            
                                            	Metric
                                            	**type**\:  int
                                            
                                            	**range:** 0..16777215
                                            
                                            .. attribute:: prefix
                                            
                                            	Prefix
                                            	**type**\:  str
                                            
                                            .. attribute:: prefix_options
                                            
                                            	Prefix options
                                            	**type**\:  str
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: referenced_link_state_id
                                            
                                            	Referenced Link State ID
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: referenced_ls_type
                                            
                                            	Referenced Link State type
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal, self).__init__()

                                                self.yang_name = "as-external"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.external_route_tag = YLeaf(YType.uint32, "external-route-tag")

                                                self.flags = YLeaf(YType.bits, "flags")

                                                self.forwarding_address = YLeaf(YType.str, "forwarding-address")

                                                self.metric = YLeaf(YType.uint32, "metric")

                                                self.prefix = YLeaf(YType.str, "prefix")

                                                self.prefix_options = YLeaf(YType.str, "prefix-options")

                                                self.referenced_link_state_id = YLeaf(YType.uint32, "referenced-link-state-id")

                                                self.referenced_ls_type = YLeaf(YType.uint16, "referenced-ls-type")
                                                self._segment_path = lambda: "as-external"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal, ['external_route_tag', 'flags', 'forwarding_address', 'metric', 'prefix', 'prefix_options', 'referenced_link_state_id', 'referenced_ls_type'], name, value)


                                        class InterAreaPrefix(Entity):
                                            """
                                            Inter\-Area\-Prefix LSA.
                                            
                                            .. attribute:: metric
                                            
                                            	Metric
                                            	**type**\:  int
                                            
                                            	**range:** 0..16777215
                                            
                                            .. attribute:: prefix
                                            
                                            	Prefix
                                            	**type**\:  str
                                            
                                            .. attribute:: prefix_options
                                            
                                            	Prefix options
                                            	**type**\:  str
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaPrefix, self).__init__()

                                                self.yang_name = "inter-area-prefix"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.metric = YLeaf(YType.uint32, "metric")

                                                self.prefix = YLeaf(YType.str, "prefix")

                                                self.prefix_options = YLeaf(YType.str, "prefix-options")
                                                self._segment_path = lambda: "inter-area-prefix"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaPrefix, ['metric', 'prefix', 'prefix_options'], name, value)


                                        class InterAreaRouter(Entity):
                                            """
                                            Inter\-Area\-Router LSA.
                                            
                                            .. attribute:: destination_router_id
                                            
                                            	The Router ID of the router being described by the LSA
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                            
                                            .. attribute:: metric
                                            
                                            	Metric
                                            	**type**\:  int
                                            
                                            	**range:** 0..16777215
                                            
                                            .. attribute:: options
                                            
                                            	OSPFv3 LSA options
                                            	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter.Options>`
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter, self).__init__()

                                                self.yang_name = "inter-area-router"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.destination_router_id = YLeaf(YType.str, "destination-router-id")

                                                self.metric = YLeaf(YType.uint32, "metric")

                                                self.options = YLeaf(YType.bits, "options")
                                                self._segment_path = lambda: "inter-area-router"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter, ['destination_router_id', 'metric', 'options'], name, value)


                                        class IntraAreaPrefix(Entity):
                                            """
                                            Intra\-Area\-Prefix LSA.
                                            
                                            .. attribute:: num_of_prefixes
                                            
                                            	Number of prefixes
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: prefix_list
                                            
                                            	List of prefixes associated with the link
                                            	**type**\: list of    :py:class:`PrefixList <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList>`
                                            
                                            .. attribute:: referenced_adv_router
                                            
                                            	Referenced Advertising Router
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: referenced_link_state_id
                                            
                                            	Referenced Link State ID
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: referenced_ls_type
                                            
                                            	Referenced Link State type
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix, self).__init__()

                                                self.yang_name = "intra-area-prefix"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {"prefix-list" : ("prefix_list", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList)}

                                                self.num_of_prefixes = YLeaf(YType.uint16, "num-of-prefixes")

                                                self.referenced_adv_router = YLeaf(YType.str, "referenced-adv-router")

                                                self.referenced_link_state_id = YLeaf(YType.uint32, "referenced-link-state-id")

                                                self.referenced_ls_type = YLeaf(YType.uint16, "referenced-ls-type")

                                                self.prefix_list = YList(self)
                                                self._segment_path = lambda: "intra-area-prefix"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix, ['num_of_prefixes', 'referenced_adv_router', 'referenced_link_state_id', 'referenced_ls_type'], name, value)


                                            class PrefixList(Entity):
                                                """
                                                List of prefixes associated with the link.
                                                
                                                .. attribute:: prefix  <key>
                                                
                                                	Prefix
                                                	**type**\:  str
                                                
                                                .. attribute:: metric
                                                
                                                	Metric
                                                	**type**\:  int
                                                
                                                	**range:** 0..16777215
                                                
                                                .. attribute:: prefix_options
                                                
                                                	Prefix options
                                                	**type**\:  str
                                                
                                                	**mandatory**\: True
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList, self).__init__()

                                                    self.yang_name = "prefix-list"
                                                    self.yang_parent_name = "intra-area-prefix"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.prefix = YLeaf(YType.str, "prefix")

                                                    self.metric = YLeaf(YType.uint32, "metric")

                                                    self.prefix_options = YLeaf(YType.str, "prefix-options")
                                                    self._segment_path = lambda: "prefix-list" + "[prefix='" + self.prefix.get() + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList, ['prefix', 'metric', 'prefix_options'], name, value)


                                        class Link(Entity):
                                            """
                                            Link LSA.
                                            
                                            .. attribute:: link_local_interface_address
                                            
                                            	The originating router's link\-local interface address on the link
                                            	**type**\: one of the below types:
                                            
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            
                                            ----
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            
                                            ----
                                            .. attribute:: num_of_prefixes
                                            
                                            	Number of prefixes
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: options
                                            
                                            	OSPFv3 LSA options
                                            	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link.Options>`
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: prefix_list
                                            
                                            	List of prefixes associated with the link
                                            	**type**\: list of    :py:class:`PrefixList <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link.PrefixList>`
                                            
                                            .. attribute:: rtr_priority
                                            
                                            	Router Priority of the interface
                                            	**type**\:  int
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link, self).__init__()

                                                self.yang_name = "link"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {"prefix-list" : ("prefix_list", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link.PrefixList)}

                                                self.link_local_interface_address = YLeaf(YType.str, "link-local-interface-address")

                                                self.num_of_prefixes = YLeaf(YType.uint32, "num-of-prefixes")

                                                self.options = YLeaf(YType.bits, "options")

                                                self.rtr_priority = YLeaf(YType.uint8, "rtr-priority")

                                                self.prefix_list = YList(self)
                                                self._segment_path = lambda: "link"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link, ['link_local_interface_address', 'num_of_prefixes', 'options', 'rtr_priority'], name, value)


                                            class PrefixList(Entity):
                                                """
                                                List of prefixes associated with the link.
                                                
                                                .. attribute:: prefix  <key>
                                                
                                                	Prefix
                                                	**type**\:  str
                                                
                                                .. attribute:: prefix_options
                                                
                                                	Prefix options
                                                	**type**\:  str
                                                
                                                	**mandatory**\: True
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link.PrefixList, self).__init__()

                                                    self.yang_name = "prefix-list"
                                                    self.yang_parent_name = "link"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.prefix = YLeaf(YType.str, "prefix")

                                                    self.prefix_options = YLeaf(YType.str, "prefix-options")
                                                    self._segment_path = lambda: "prefix-list" + "[prefix='" + self.prefix.get() + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link.PrefixList, ['prefix', 'prefix_options'], name, value)


                                        class Network(Entity):
                                            """
                                            Network LSA.
                                            
                                            .. attribute:: attached_router
                                            
                                            	List of the routers attached to the network
                                            	**type**\:  list of str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                            
                                            .. attribute:: options
                                            
                                            	OSPFv3 LSA options
                                            	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network.Options>`
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network, self).__init__()

                                                self.yang_name = "network"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.attached_router = YLeafList(YType.str, "attached-router")

                                                self.options = YLeaf(YType.bits, "options")
                                                self._segment_path = lambda: "network"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network, ['attached_router', 'options'], name, value)


                                        class Nssa(Entity):
                                            """
                                            NSSA LSA.
                                            
                                            .. attribute:: external_route_tag
                                            
                                            	Route tag
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: flags
                                            
                                            	Flags
                                            	**type**\:   :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa.Flags>`
                                            
                                            .. attribute:: forwarding_address
                                            
                                            	Forwarding address
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: metric
                                            
                                            	Metric
                                            	**type**\:  int
                                            
                                            	**range:** 0..16777215
                                            
                                            .. attribute:: prefix
                                            
                                            	Prefix
                                            	**type**\:  str
                                            
                                            .. attribute:: prefix_options
                                            
                                            	Prefix options
                                            	**type**\:  str
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: referenced_link_state_id
                                            
                                            	Referenced Link State ID
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: referenced_ls_type
                                            
                                            	Referenced Link State type
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa, self).__init__()

                                                self.yang_name = "nssa"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.external_route_tag = YLeaf(YType.uint32, "external-route-tag")

                                                self.flags = YLeaf(YType.bits, "flags")

                                                self.forwarding_address = YLeaf(YType.str, "forwarding-address")

                                                self.metric = YLeaf(YType.uint32, "metric")

                                                self.prefix = YLeaf(YType.str, "prefix")

                                                self.prefix_options = YLeaf(YType.str, "prefix-options")

                                                self.referenced_link_state_id = YLeaf(YType.uint32, "referenced-link-state-id")

                                                self.referenced_ls_type = YLeaf(YType.uint16, "referenced-ls-type")
                                                self._segment_path = lambda: "nssa"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa, ['external_route_tag', 'flags', 'forwarding_address', 'metric', 'prefix', 'prefix_options', 'referenced_link_state_id', 'referenced_ls_type'], name, value)


                                        class Router(Entity):
                                            """
                                            Router LSA.
                                            
                                            .. attribute:: flags
                                            
                                            	LSA option
                                            	**type**\:   :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Flags>`
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: link
                                            
                                            	Router LSA link
                                            	**type**\: list of    :py:class:`Link <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Link>`
                                            
                                            .. attribute:: options
                                            
                                            	OSPFv3 LSA options
                                            	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Options>`
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router, self).__init__()

                                                self.yang_name = "router"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {"link" : ("link", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Link)}

                                                self.flags = YLeaf(YType.bits, "flags")

                                                self.options = YLeaf(YType.bits, "options")

                                                self.link = YList(self)
                                                self._segment_path = lambda: "router"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router, ['flags', 'options'], name, value)


                                            class Link(Entity):
                                                """
                                                Router LSA link.
                                                
                                                .. attribute:: interface_id  <key>
                                                
                                                	Interface ID
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: neighbor_interface_id  <key>
                                                
                                                	Neighbor Interface ID
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: neighbor_router_id  <key>
                                                
                                                	Neighbor Router ID
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                
                                                .. attribute:: metric
                                                
                                                	Metric
                                                	**type**\:  int
                                                
                                                	**range:** 0..65535
                                                
                                                .. attribute:: type
                                                
                                                	Link type
                                                	**type**\:  int
                                                
                                                	**range:** 0..255
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Link, self).__init__()

                                                    self.yang_name = "link"
                                                    self.yang_parent_name = "router"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.interface_id = YLeaf(YType.uint32, "interface-id")

                                                    self.neighbor_interface_id = YLeaf(YType.uint32, "neighbor-interface-id")

                                                    self.neighbor_router_id = YLeaf(YType.str, "neighbor-router-id")

                                                    self.metric = YLeaf(YType.uint16, "metric")

                                                    self.type = YLeaf(YType.uint8, "type")
                                                    self._segment_path = lambda: "link" + "[interface-id='" + self.interface_id.get() + "']" + "[neighbor-interface-id='" + self.neighbor_interface_id.get() + "']" + "[neighbor-router-id='" + self.neighbor_router_id.get() + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Link, ['interface_id', 'neighbor_interface_id', 'neighbor_router_id', 'metric', 'type'], name, value)


                                    class Header(Entity):
                                        """
                                        Decoded OSPFv3 LSA header data.
                                        
                                        .. attribute:: adv_router
                                        
                                        	LSA advertising router
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: age
                                        
                                        	LSA age
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: checksum
                                        
                                        	LSA checksum
                                        	**type**\:  str
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: length
                                        
                                        	LSA length
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: lsa_id
                                        
                                        	LSA ID
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: options
                                        
                                        	OSPFv3 LSA options
                                        	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header.Options>`
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: seq_num
                                        
                                        	LSA sequence number
                                        	**type**\:  str
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: type
                                        
                                        	LSA type
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header, self).__init__()

                                            self.yang_name = "header"
                                            self.yang_parent_name = "ospfv3"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.adv_router = YLeaf(YType.str, "adv-router")

                                            self.age = YLeaf(YType.uint16, "age")

                                            self.checksum = YLeaf(YType.str, "checksum")

                                            self.length = YLeaf(YType.uint16, "length")

                                            self.lsa_id = YLeaf(YType.uint32, "lsa-id")

                                            self.options = YLeaf(YType.bits, "options")

                                            self.seq_num = YLeaf(YType.str, "seq-num")

                                            self.type = YLeaf(YType.uint16, "type")
                                            self._segment_path = lambda: "header"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header, ['adv_router', 'age', 'checksum', 'length', 'lsa_id', 'options', 'seq_num', 'type'], name, value)


                        class Topology(Entity):
                            """
                            OSPF topology.
                            
                            .. attribute:: name  <key>
                            
                            	RIB
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.Ribs.Rib>`
                            
                            .. attribute:: area
                            
                            	List of ospf areas
                            	**type**\: list of    :py:class:`Area <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area>`
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology, self).__init__()

                                self.yang_name = "topology"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"area" : ("area", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area)}

                                self.name = YLeaf(YType.str, "name")

                                self.area = YList(self)
                                self._segment_path = lambda: "topology" + "[name='" + self.name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology, ['name'], name, value)


                            class Area(Entity):
                                """
                                List of ospf areas
                                
                                .. attribute:: area_id  <key>
                                
                                	Area ID
                                	**type**\: one of the below types:
                                
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                
                                
                                ----
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area, self).__init__()

                                    self.yang_name = "area"
                                    self.yang_parent_name = "topology"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.area_id = YLeaf(YType.str, "area-id")
                                    self._segment_path = lambda: "area" + "[area-id='" + self.area_id.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area, ['area_id'], name, value)

    def clone_ptr(self):
        self._top_entity = RoutingState()
        return self._top_entity

class DefaultRoutingInstance(Identity):
    """
    This identity represents either a default routing instance, or
    the only routing instance on systems that do not support
    multiple instances.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        super(DefaultRoutingInstance, self).__init__("urn:ietf:params:xml:ns:yang:ietf-routing", "ietf-routing", "ietf-routing:default-routing-instance")


class Direct(Identity):
    """
    Routing pseudo\-protocol that provides routes to directly
    connected networks.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        super(Direct, self).__init__("urn:ietf:params:xml:ns:yang:ietf-routing", "ietf-routing", "ietf-routing:direct")


class Ipv4(Identity):
    """
    This identity represents IPv4 address family.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        super(Ipv4, self).__init__("urn:ietf:params:xml:ns:yang:ietf-routing", "ietf-routing", "ietf-routing:ipv4")


class Ipv6(Identity):
    """
    This identity represents IPv6 address family.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        super(Ipv6, self).__init__("urn:ietf:params:xml:ns:yang:ietf-routing", "ietf-routing", "ietf-routing:ipv6")


class Static(Identity):
    """
    Static routing pseudo\-protocol.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        super(Static, self).__init__("urn:ietf:params:xml:ns:yang:ietf-routing", "ietf-routing", "ietf-routing:static")


class VrfRoutingInstance(Identity):
    """
    This identity represents a VRF routing instance. The type is
    distinct from the default\-routing\-instance. There may be
    multiple vrf\-routing\-interfaces.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        super(VrfRoutingInstance, self).__init__("urn:ietf:params:xml:ns:yang:ietf-routing", "ietf-routing", "ietf-routing:vrf-routing-instance")


