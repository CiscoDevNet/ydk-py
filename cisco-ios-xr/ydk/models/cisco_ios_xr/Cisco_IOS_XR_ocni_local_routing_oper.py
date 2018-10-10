""" Cisco_IOS_XR_ocni_local_routing_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ocni\-local\-routing package operational data.

This module contains definitions
for the following management objects\:
  ocni\: An OpenConfig description of a network\-instance. This
    may be a Layer 3 forwarding construct such as a virtual
    routing and forwarding (VRF) instance, or a Layer 2 instance
    such as a virtual switch instance (VSI). Mixed Layer 2 and
    Layer 3 instances are also supported.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Ocni(Entity):
    """
    An OpenConfig description of a network\-instance.
    This may be a Layer 3 forwarding construct such
    as a virtual routing and forwarding (VRF)
    instance, or a Layer 2 instance such as a virtual
    switch instance (VSI). Mixed Layer 2 and Layer 3
    instances are also supported.
    
    .. attribute:: vrfipv4
    
    	IPv4 static configuration
    	**type**\:  :py:class:`Vrfipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv4>`
    
    .. attribute:: vrfipv6
    
    	IPv6 static configuration
    	**type**\:  :py:class:`Vrfipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv6>`
    
    

    """

    _prefix = 'ocni-local-routing-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ocni, self).__init__()
        self._top_entity = None

        self.yang_name = "ocni"
        self.yang_parent_name = "Cisco-IOS-XR-ocni-local-routing-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vrfipv4", ("vrfipv4", Ocni.Vrfipv4)), ("vrfipv6", ("vrfipv6", Ocni.Vrfipv6))])
        self._leafs = OrderedDict()

        self.vrfipv4 = Ocni.Vrfipv4()
        self.vrfipv4.parent = self
        self._children_name_map["vrfipv4"] = "vrfipv4"

        self.vrfipv6 = Ocni.Vrfipv6()
        self.vrfipv6.parent = self
        self._children_name_map["vrfipv6"] = "vrfipv6"
        self._segment_path = lambda: "Cisco-IOS-XR-ocni-local-routing-oper:ocni"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ocni, [], name, value)


    class Vrfipv4(Entity):
        """
        IPv4 static configuration
        
        .. attribute:: network_instances
        
        	Network instances configured on the local system
        	**type**\:  :py:class:`NetworkInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv4.NetworkInstances>`
        
        

        """

        _prefix = 'ocni-local-routing-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ocni.Vrfipv4, self).__init__()

            self.yang_name = "vrfipv4"
            self.yang_parent_name = "ocni"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("network-instances", ("network_instances", Ocni.Vrfipv4.NetworkInstances))])
            self._leafs = OrderedDict()

            self.network_instances = Ocni.Vrfipv4.NetworkInstances()
            self.network_instances.parent = self
            self._children_name_map["network_instances"] = "network-instances"
            self._segment_path = lambda: "vrfipv4"
            self._absolute_path = lambda: "Cisco-IOS-XR-ocni-local-routing-oper:ocni/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ocni.Vrfipv4, [], name, value)


        class NetworkInstances(Entity):
            """
            Network instances configured on the local system
            
            .. attribute:: network_instance
            
            	Network instances configured on the local system
            	**type**\: list of  		 :py:class:`NetworkInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv4.NetworkInstances.NetworkInstance>`
            
            

            """

            _prefix = 'ocni-local-routing-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ocni.Vrfipv4.NetworkInstances, self).__init__()

                self.yang_name = "network-instances"
                self.yang_parent_name = "vrfipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("network-instance", ("network_instance", Ocni.Vrfipv4.NetworkInstances.NetworkInstance))])
                self._leafs = OrderedDict()

                self.network_instance = YList(self)
                self._segment_path = lambda: "network-instances"
                self._absolute_path = lambda: "Cisco-IOS-XR-ocni-local-routing-oper:ocni/vrfipv4/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ocni.Vrfipv4.NetworkInstances, [], name, value)


            class NetworkInstance(Entity):
                """
                Network instances configured on the local
                system
                
                .. attribute:: name  (key)
                
                	A unique name identifying the network instance
                	**type**\: str
                
                .. attribute:: protocols
                
                	A process (instance) of a routing protocol. Some systems may not support more than one instance of a particular routing protocol
                	**type**\:  :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols>`
                
                

                """

                _prefix = 'ocni-local-routing-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ocni.Vrfipv4.NetworkInstances.NetworkInstance, self).__init__()

                    self.yang_name = "network-instance"
                    self.yang_parent_name = "network-instances"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("protocols", ("protocols", Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.protocols = Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols()
                    self.protocols.parent = self
                    self._children_name_map["protocols"] = "protocols"
                    self._segment_path = lambda: "network-instance" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ocni-local-routing-oper:ocni/vrfipv4/network-instances/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ocni.Vrfipv4.NetworkInstances.NetworkInstance, ['name'], name, value)


                class Protocols(Entity):
                    """
                    A process (instance) of a routing protocol.
                    Some systems may not support more than one
                    instance of a particular routing protocol
                    
                    .. attribute:: protocol
                    
                    	A process (instance) of a routing protocol. Some systems may not support more than one instance of a particular routing protocol
                    	**type**\: list of  		 :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol>`
                    
                    

                    """

                    _prefix = 'ocni-local-routing-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols, self).__init__()

                        self.yang_name = "protocols"
                        self.yang_parent_name = "network-instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("protocol", ("protocol", Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol))])
                        self._leafs = OrderedDict()

                        self.protocol = YList(self)
                        self._segment_path = lambda: "protocols"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols, [], name, value)


                    class Protocol(Entity):
                        """
                        A process (instance) of a routing protocol.
                        Some systems may not support more than one
                        instance of a particular routing protocol
                        
                        .. attribute:: state
                        
                        	State parameters relating to the routing protocol instance
                        	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.State>`
                        
                        .. attribute:: static_routes
                        
                        	List of locally configured static routes
                        	**type**\:  :py:class:`StaticRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes>`
                        
                        .. attribute:: identifier
                        
                        	The protocol name for the routing or forwarding protocol to be instantiated
                        	**type**\: str
                        
                        .. attribute:: name
                        
                        	An operator\-assigned identifier for the routing or forwarding protocol. For some processes this leaf may be system defined
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ocni-local-routing-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol, self).__init__()

                            self.yang_name = "protocol"
                            self.yang_parent_name = "protocols"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("state", ("state", Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.State)), ("static-routes", ("static_routes", Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes))])
                            self._leafs = OrderedDict([
                                ('identifier', (YLeaf(YType.str, 'identifier'), ['str'])),
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ])
                            self.identifier = None
                            self.name = None

                            self.state = Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"

                            self.static_routes = Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes()
                            self.static_routes.parent = self
                            self._children_name_map["static_routes"] = "static-routes"
                            self._segment_path = lambda: "protocol"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol, ['identifier', 'name'], name, value)


                        class State(Entity):
                            """
                            State parameters relating to the routing
                            protocol instance
                            
                            .. attribute:: identifier
                            
                            	The protocol identifier for the instance
                            	**type**\: str
                            
                            .. attribute:: name
                            
                            	A unique name for the protocol instance
                            	**type**\: str
                            
                            .. attribute:: enabled
                            
                            	A boolean value indicating whether the local protocol instance is enabled
                            	**type**\: bool
                            
                            .. attribute:: default_metric
                            
                            	The default metric within the RIB for entries that are installed by this protocol instance. This value may be overridden by protocol specific configuration options. The lower the metric specified the more preferable the RIB entry is to be selected for use within the network instance. Where multiple entries have the same metric value then these equal cost paths should be treated according to the specified ECMP path selection behaviour for the instance
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ocni-local-routing-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "protocol"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('identifier', (YLeaf(YType.str, 'identifier'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                    ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                    ('default_metric', (YLeaf(YType.uint32, 'default-metric'), ['int'])),
                                ])
                                self.identifier = None
                                self.name = None
                                self.enabled = None
                                self.default_metric = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.State, ['identifier', 'name', 'enabled', 'default_metric'], name, value)


                        class StaticRoutes(Entity):
                            """
                            List of locally configured static routes
                            
                            .. attribute:: static_route
                            
                            	List of locally configured static routes
                            	**type**\: list of  		 :py:class:`StaticRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute>`
                            
                            

                            """

                            _prefix = 'ocni-local-routing-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes, self).__init__()

                                self.yang_name = "static-routes"
                                self.yang_parent_name = "protocol"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("static-route", ("static_route", Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute))])
                                self._leafs = OrderedDict()

                                self.static_route = YList(self)
                                self._segment_path = lambda: "static-routes"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes, [], name, value)


                            class StaticRoute(Entity):
                                """
                                List of locally configured static routes
                                
                                .. attribute:: prefix  (key)
                                
                                	Reference to the destination prefix list key
                                	**type**\: str
                                
                                .. attribute:: next_hops
                                
                                	A list of next\-hops to be utilised for the static route being specified
                                	**type**\:  :py:class:`NextHops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops>`
                                
                                .. attribute:: static_routes_state
                                
                                	Operational state data for static routes
                                	**type**\:  :py:class:`StaticRoutesState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.StaticRoutesState>`
                                
                                

                                """

                                _prefix = 'ocni-local-routing-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute, self).__init__()

                                    self.yang_name = "static-route"
                                    self.yang_parent_name = "static-routes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['prefix']
                                    self._child_classes = OrderedDict([("next-hops", ("next_hops", Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops)), ("static-routes-state", ("static_routes_state", Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.StaticRoutesState))])
                                    self._leafs = OrderedDict([
                                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                    ])
                                    self.prefix = None

                                    self.next_hops = Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops()
                                    self.next_hops.parent = self
                                    self._children_name_map["next_hops"] = "next-hops"

                                    self.static_routes_state = Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.StaticRoutesState()
                                    self.static_routes_state.parent = self
                                    self._children_name_map["static_routes_state"] = "static-routes-state"
                                    self._segment_path = lambda: "static-route" + "[prefix='" + str(self.prefix) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute, ['prefix'], name, value)


                                class NextHops(Entity):
                                    """
                                    A list of next\-hops to be utilised for the
                                    static route being specified.
                                    
                                    .. attribute:: next_hop
                                    
                                    	A list of next\-hops to be utilised for the static route being specified
                                    	**type**\: list of  		 :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop>`
                                    
                                    

                                    """

                                    _prefix = 'ocni-local-routing-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops, self).__init__()

                                        self.yang_name = "next-hops"
                                        self.yang_parent_name = "static-route"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("next-hop", ("next_hop", Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop))])
                                        self._leafs = OrderedDict()

                                        self.next_hop = YList(self)
                                        self._segment_path = lambda: "next-hops"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops, [], name, value)


                                    class NextHop(Entity):
                                        """
                                        A list of next\-hops to be utilised for
                                        the static route being specified.
                                        
                                        .. attribute:: index  (key)
                                        
                                        	A reference to the index of the current next\-hop. The index is intended to be a user\-specified value which can be used to reference the next\-hop in question, without any other semantics being assigned to it
                                        	**type**\: str
                                        
                                        .. attribute:: state
                                        
                                        	Operational state parameters relating to the next\-hop entry
                                        	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.State>`
                                        
                                        .. attribute:: interface_ref
                                        
                                        	Reference to an interface or subinterface
                                        	**type**\:  :py:class:`InterfaceRef <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef>`
                                        
                                        

                                        """

                                        _prefix = 'ocni-local-routing-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop, self).__init__()

                                            self.yang_name = "next-hop"
                                            self.yang_parent_name = "next-hops"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['index']
                                            self._child_classes = OrderedDict([("state", ("state", Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.State)), ("interface-ref", ("interface_ref", Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef))])
                                            self._leafs = OrderedDict([
                                                ('index', (YLeaf(YType.str, 'index'), ['str'])),
                                            ])
                                            self.index = None

                                            self.state = Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.State()
                                            self.state.parent = self
                                            self._children_name_map["state"] = "state"

                                            self.interface_ref = Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef()
                                            self.interface_ref.parent = self
                                            self._children_name_map["interface_ref"] = "interface-ref"
                                            self._segment_path = lambda: "next-hop" + "[index='" + str(self.index) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop, ['index'], name, value)


                                        class State(Entity):
                                            """
                                            Operational state parameters relating to the
                                            next\-hop entry
                                            
                                            .. attribute:: index
                                            
                                            	An user\-specified identifier utilised to uniquely reference the next\-hop entry in the next\-hop list. The value of this index has no semantic meaning other than for referencing the entry
                                            	**type**\: str
                                            
                                            .. attribute:: next_hop
                                            
                                            	The next\-hop that is to be used for the static route \- this may be specified as an IP address, an interface or a pre\-defined next\-hop type \- for instance, DROP or LOCAL\_LINK. When this leaf is not set, and the interface\-ref value is specified for the next\-hop, then the system should treat the prefix as though it is directly connected to the interface
                                            	**type**\: str
                                            
                                            .. attribute:: metric
                                            
                                            	A metric which is utilised to specify the preference of the next\-hop entry when it is injected into the RIB. The lower the metric, the more preferable the prefix is. When this value is not specified the metric is inherited from the default metric utilised for static routes within the network instance that the static routes are being instantiated. When multiple next\-hops are specified for a static route, the metric is utilised to determine which of the next\-hops is to be installed in the RIB. When multiple next\-hops have the same metric (be it specified, or simply the default) then these next\-hops should all be installed in the RIB
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ocni-local-routing-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.State, self).__init__()

                                                self.yang_name = "state"
                                                self.yang_parent_name = "next-hop"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('index', (YLeaf(YType.str, 'index'), ['str'])),
                                                    ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str'])),
                                                    ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                ])
                                                self.index = None
                                                self.next_hop = None
                                                self.metric = None
                                                self._segment_path = lambda: "state"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.State, ['index', 'next_hop', 'metric'], name, value)


                                        class InterfaceRef(Entity):
                                            """
                                            Reference to an interface or subinterface
                                            
                                            .. attribute:: state
                                            
                                            	Operational state for interface\-ref
                                            	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef.State>`
                                            
                                            

                                            """

                                            _prefix = 'ocni-local-routing-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef, self).__init__()

                                                self.yang_name = "interface-ref"
                                                self.yang_parent_name = "next-hop"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("state", ("state", Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef.State))])
                                                self._leafs = OrderedDict()

                                                self.state = Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef.State()
                                                self.state.parent = self
                                                self._children_name_map["state"] = "state"
                                                self._segment_path = lambda: "interface-ref"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef, [], name, value)


                                            class State(Entity):
                                                """
                                                Operational state for interface\-ref
                                                
                                                .. attribute:: interface
                                                
                                                	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                                                	**type**\: str
                                                
                                                .. attribute:: subinterface
                                                
                                                	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'ocni-local-routing-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef.State, self).__init__()

                                                    self.yang_name = "state"
                                                    self.yang_parent_name = "interface-ref"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                                        ('subinterface', (YLeaf(YType.uint32, 'subinterface'), ['int'])),
                                                    ])
                                                    self.interface = None
                                                    self.subinterface = None
                                                    self._segment_path = lambda: "state"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef.State, ['interface', 'subinterface'], name, value)


                                class StaticRoutesState(Entity):
                                    """
                                    Operational state data for static routes
                                    
                                    .. attribute:: prefix
                                    
                                    	Destination prefix for the static route, either IPv4 or IPv6
                                    	**type**\: str
                                    
                                    .. attribute:: set_tag
                                    
                                    	Set a generic tag value on the route. This tag can be used for filtering routes that are distributed to other routing protocols
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'ocni-local-routing-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.StaticRoutesState, self).__init__()

                                        self.yang_name = "static-routes-state"
                                        self.yang_parent_name = "static-route"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                            ('set_tag', (YLeaf(YType.str, 'set-tag'), ['str'])),
                                        ])
                                        self.prefix = None
                                        self.set_tag = None
                                        self._segment_path = lambda: "static-routes-state"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ocni.Vrfipv4.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.StaticRoutesState, ['prefix', 'set_tag'], name, value)


    class Vrfipv6(Entity):
        """
        IPv6 static configuration
        
        .. attribute:: network_instances
        
        	Network instances configured on the local system
        	**type**\:  :py:class:`NetworkInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv6.NetworkInstances>`
        
        

        """

        _prefix = 'ocni-local-routing-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ocni.Vrfipv6, self).__init__()

            self.yang_name = "vrfipv6"
            self.yang_parent_name = "ocni"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("network-instances", ("network_instances", Ocni.Vrfipv6.NetworkInstances))])
            self._leafs = OrderedDict()

            self.network_instances = Ocni.Vrfipv6.NetworkInstances()
            self.network_instances.parent = self
            self._children_name_map["network_instances"] = "network-instances"
            self._segment_path = lambda: "vrfipv6"
            self._absolute_path = lambda: "Cisco-IOS-XR-ocni-local-routing-oper:ocni/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ocni.Vrfipv6, [], name, value)


        class NetworkInstances(Entity):
            """
            Network instances configured on the local system
            
            .. attribute:: network_instance
            
            	Network instances configured on the local system
            	**type**\: list of  		 :py:class:`NetworkInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv6.NetworkInstances.NetworkInstance>`
            
            

            """

            _prefix = 'ocni-local-routing-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ocni.Vrfipv6.NetworkInstances, self).__init__()

                self.yang_name = "network-instances"
                self.yang_parent_name = "vrfipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("network-instance", ("network_instance", Ocni.Vrfipv6.NetworkInstances.NetworkInstance))])
                self._leafs = OrderedDict()

                self.network_instance = YList(self)
                self._segment_path = lambda: "network-instances"
                self._absolute_path = lambda: "Cisco-IOS-XR-ocni-local-routing-oper:ocni/vrfipv6/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ocni.Vrfipv6.NetworkInstances, [], name, value)


            class NetworkInstance(Entity):
                """
                Network instances configured on the local
                system
                
                .. attribute:: name  (key)
                
                	A unique name identifying the network instance
                	**type**\: str
                
                .. attribute:: protocols
                
                	A process (instance) of a routing protocol. Some systems may not support more than one instance of a particular routing protocol
                	**type**\:  :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols>`
                
                

                """

                _prefix = 'ocni-local-routing-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ocni.Vrfipv6.NetworkInstances.NetworkInstance, self).__init__()

                    self.yang_name = "network-instance"
                    self.yang_parent_name = "network-instances"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("protocols", ("protocols", Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.protocols = Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols()
                    self.protocols.parent = self
                    self._children_name_map["protocols"] = "protocols"
                    self._segment_path = lambda: "network-instance" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ocni-local-routing-oper:ocni/vrfipv6/network-instances/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ocni.Vrfipv6.NetworkInstances.NetworkInstance, ['name'], name, value)


                class Protocols(Entity):
                    """
                    A process (instance) of a routing protocol.
                    Some systems may not support more than one
                    instance of a particular routing protocol
                    
                    .. attribute:: protocol
                    
                    	A process (instance) of a routing protocol. Some systems may not support more than one instance of a particular routing protocol
                    	**type**\: list of  		 :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol>`
                    
                    

                    """

                    _prefix = 'ocni-local-routing-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols, self).__init__()

                        self.yang_name = "protocols"
                        self.yang_parent_name = "network-instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("protocol", ("protocol", Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol))])
                        self._leafs = OrderedDict()

                        self.protocol = YList(self)
                        self._segment_path = lambda: "protocols"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols, [], name, value)


                    class Protocol(Entity):
                        """
                        A process (instance) of a routing protocol.
                        Some systems may not support more than one
                        instance of a particular routing protocol
                        
                        .. attribute:: state
                        
                        	State parameters relating to the routing protocol instance
                        	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.State>`
                        
                        .. attribute:: static_routes
                        
                        	List of locally configured static routes
                        	**type**\:  :py:class:`StaticRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes>`
                        
                        .. attribute:: identifier
                        
                        	The protocol name for the routing or forwarding protocol to be instantiated
                        	**type**\: str
                        
                        .. attribute:: name
                        
                        	An operator\-assigned identifier for the routing or forwarding protocol. For some processes this leaf may be system defined
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ocni-local-routing-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol, self).__init__()

                            self.yang_name = "protocol"
                            self.yang_parent_name = "protocols"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("state", ("state", Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.State)), ("static-routes", ("static_routes", Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes))])
                            self._leafs = OrderedDict([
                                ('identifier', (YLeaf(YType.str, 'identifier'), ['str'])),
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ])
                            self.identifier = None
                            self.name = None

                            self.state = Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"

                            self.static_routes = Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes()
                            self.static_routes.parent = self
                            self._children_name_map["static_routes"] = "static-routes"
                            self._segment_path = lambda: "protocol"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol, ['identifier', 'name'], name, value)


                        class State(Entity):
                            """
                            State parameters relating to the routing
                            protocol instance
                            
                            .. attribute:: identifier
                            
                            	The protocol identifier for the instance
                            	**type**\: str
                            
                            .. attribute:: name
                            
                            	A unique name for the protocol instance
                            	**type**\: str
                            
                            .. attribute:: enabled
                            
                            	A boolean value indicating whether the local protocol instance is enabled
                            	**type**\: bool
                            
                            .. attribute:: default_metric
                            
                            	The default metric within the RIB for entries that are installed by this protocol instance. This value may be overridden by protocol specific configuration options. The lower the metric specified the more preferable the RIB entry is to be selected for use within the network instance. Where multiple entries have the same metric value then these equal cost paths should be treated according to the specified ECMP path selection behaviour for the instance
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ocni-local-routing-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "protocol"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('identifier', (YLeaf(YType.str, 'identifier'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                    ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                    ('default_metric', (YLeaf(YType.uint32, 'default-metric'), ['int'])),
                                ])
                                self.identifier = None
                                self.name = None
                                self.enabled = None
                                self.default_metric = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.State, ['identifier', 'name', 'enabled', 'default_metric'], name, value)


                        class StaticRoutes(Entity):
                            """
                            List of locally configured static routes
                            
                            .. attribute:: static_route
                            
                            	List of locally configured static routes
                            	**type**\: list of  		 :py:class:`StaticRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute>`
                            
                            

                            """

                            _prefix = 'ocni-local-routing-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes, self).__init__()

                                self.yang_name = "static-routes"
                                self.yang_parent_name = "protocol"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("static-route", ("static_route", Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute))])
                                self._leafs = OrderedDict()

                                self.static_route = YList(self)
                                self._segment_path = lambda: "static-routes"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes, [], name, value)


                            class StaticRoute(Entity):
                                """
                                List of locally configured static routes
                                
                                .. attribute:: prefix  (key)
                                
                                	Reference to the destination prefix list key
                                	**type**\: str
                                
                                .. attribute:: next_hops
                                
                                	A list of next\-hops to be utilised for the static route being specified
                                	**type**\:  :py:class:`NextHops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops>`
                                
                                .. attribute:: static_routes_state
                                
                                	Operational state data for static routes
                                	**type**\:  :py:class:`StaticRoutesState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.StaticRoutesState>`
                                
                                

                                """

                                _prefix = 'ocni-local-routing-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute, self).__init__()

                                    self.yang_name = "static-route"
                                    self.yang_parent_name = "static-routes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['prefix']
                                    self._child_classes = OrderedDict([("next-hops", ("next_hops", Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops)), ("static-routes-state", ("static_routes_state", Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.StaticRoutesState))])
                                    self._leafs = OrderedDict([
                                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                    ])
                                    self.prefix = None

                                    self.next_hops = Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops()
                                    self.next_hops.parent = self
                                    self._children_name_map["next_hops"] = "next-hops"

                                    self.static_routes_state = Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.StaticRoutesState()
                                    self.static_routes_state.parent = self
                                    self._children_name_map["static_routes_state"] = "static-routes-state"
                                    self._segment_path = lambda: "static-route" + "[prefix='" + str(self.prefix) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute, ['prefix'], name, value)


                                class NextHops(Entity):
                                    """
                                    A list of next\-hops to be utilised for the
                                    static route being specified.
                                    
                                    .. attribute:: next_hop
                                    
                                    	A list of next\-hops to be utilised for the static route being specified
                                    	**type**\: list of  		 :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop>`
                                    
                                    

                                    """

                                    _prefix = 'ocni-local-routing-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops, self).__init__()

                                        self.yang_name = "next-hops"
                                        self.yang_parent_name = "static-route"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("next-hop", ("next_hop", Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop))])
                                        self._leafs = OrderedDict()

                                        self.next_hop = YList(self)
                                        self._segment_path = lambda: "next-hops"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops, [], name, value)


                                    class NextHop(Entity):
                                        """
                                        A list of next\-hops to be utilised for
                                        the static route being specified.
                                        
                                        .. attribute:: index  (key)
                                        
                                        	A reference to the index of the current next\-hop. The index is intended to be a user\-specified value which can be used to reference the next\-hop in question, without any other semantics being assigned to it
                                        	**type**\: str
                                        
                                        .. attribute:: state
                                        
                                        	Operational state parameters relating to the next\-hop entry
                                        	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.State>`
                                        
                                        .. attribute:: interface_ref
                                        
                                        	Reference to an interface or subinterface
                                        	**type**\:  :py:class:`InterfaceRef <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef>`
                                        
                                        

                                        """

                                        _prefix = 'ocni-local-routing-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop, self).__init__()

                                            self.yang_name = "next-hop"
                                            self.yang_parent_name = "next-hops"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['index']
                                            self._child_classes = OrderedDict([("state", ("state", Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.State)), ("interface-ref", ("interface_ref", Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef))])
                                            self._leafs = OrderedDict([
                                                ('index', (YLeaf(YType.str, 'index'), ['str'])),
                                            ])
                                            self.index = None

                                            self.state = Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.State()
                                            self.state.parent = self
                                            self._children_name_map["state"] = "state"

                                            self.interface_ref = Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef()
                                            self.interface_ref.parent = self
                                            self._children_name_map["interface_ref"] = "interface-ref"
                                            self._segment_path = lambda: "next-hop" + "[index='" + str(self.index) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop, ['index'], name, value)


                                        class State(Entity):
                                            """
                                            Operational state parameters relating to the
                                            next\-hop entry
                                            
                                            .. attribute:: index
                                            
                                            	An user\-specified identifier utilised to uniquely reference the next\-hop entry in the next\-hop list. The value of this index has no semantic meaning other than for referencing the entry
                                            	**type**\: str
                                            
                                            .. attribute:: next_hop
                                            
                                            	The next\-hop that is to be used for the static route \- this may be specified as an IP address, an interface or a pre\-defined next\-hop type \- for instance, DROP or LOCAL\_LINK. When this leaf is not set, and the interface\-ref value is specified for the next\-hop, then the system should treat the prefix as though it is directly connected to the interface
                                            	**type**\: str
                                            
                                            .. attribute:: metric
                                            
                                            	A metric which is utilised to specify the preference of the next\-hop entry when it is injected into the RIB. The lower the metric, the more preferable the prefix is. When this value is not specified the metric is inherited from the default metric utilised for static routes within the network instance that the static routes are being instantiated. When multiple next\-hops are specified for a static route, the metric is utilised to determine which of the next\-hops is to be installed in the RIB. When multiple next\-hops have the same metric (be it specified, or simply the default) then these next\-hops should all be installed in the RIB
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ocni-local-routing-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.State, self).__init__()

                                                self.yang_name = "state"
                                                self.yang_parent_name = "next-hop"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('index', (YLeaf(YType.str, 'index'), ['str'])),
                                                    ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str'])),
                                                    ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                ])
                                                self.index = None
                                                self.next_hop = None
                                                self.metric = None
                                                self._segment_path = lambda: "state"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.State, ['index', 'next_hop', 'metric'], name, value)


                                        class InterfaceRef(Entity):
                                            """
                                            Reference to an interface or subinterface
                                            
                                            .. attribute:: state
                                            
                                            	Operational state for interface\-ref
                                            	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_local_routing_oper.Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef.State>`
                                            
                                            

                                            """

                                            _prefix = 'ocni-local-routing-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef, self).__init__()

                                                self.yang_name = "interface-ref"
                                                self.yang_parent_name = "next-hop"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("state", ("state", Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef.State))])
                                                self._leafs = OrderedDict()

                                                self.state = Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef.State()
                                                self.state.parent = self
                                                self._children_name_map["state"] = "state"
                                                self._segment_path = lambda: "interface-ref"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef, [], name, value)


                                            class State(Entity):
                                                """
                                                Operational state for interface\-ref
                                                
                                                .. attribute:: interface
                                                
                                                	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                                                	**type**\: str
                                                
                                                .. attribute:: subinterface
                                                
                                                	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'ocni-local-routing-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef.State, self).__init__()

                                                    self.yang_name = "state"
                                                    self.yang_parent_name = "interface-ref"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                                        ('subinterface', (YLeaf(YType.uint32, 'subinterface'), ['int'])),
                                                    ])
                                                    self.interface = None
                                                    self.subinterface = None
                                                    self._segment_path = lambda: "state"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.NextHops.NextHop.InterfaceRef.State, ['interface', 'subinterface'], name, value)


                                class StaticRoutesState(Entity):
                                    """
                                    Operational state data for static routes
                                    
                                    .. attribute:: prefix
                                    
                                    	Destination prefix for the static route, either IPv4 or IPv6
                                    	**type**\: str
                                    
                                    .. attribute:: set_tag
                                    
                                    	Set a generic tag value on the route. This tag can be used for filtering routes that are distributed to other routing protocols
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'ocni-local-routing-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.StaticRoutesState, self).__init__()

                                        self.yang_name = "static-routes-state"
                                        self.yang_parent_name = "static-route"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                            ('set_tag', (YLeaf(YType.str, 'set-tag'), ['str'])),
                                        ])
                                        self.prefix = None
                                        self.set_tag = None
                                        self._segment_path = lambda: "static-routes-state"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ocni.Vrfipv6.NetworkInstances.NetworkInstance.Protocols.Protocol.StaticRoutes.StaticRoute.StaticRoutesState, ['prefix', 'set_tag'], name, value)

    def clone_ptr(self):
        self._top_entity = Ocni()
        return self._top_entity

